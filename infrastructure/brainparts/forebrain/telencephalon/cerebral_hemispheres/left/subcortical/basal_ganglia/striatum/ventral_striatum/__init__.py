"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_ganglia.striatum.ventral_striatum
==============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── basal_ganglia
                    └── striatum
                        └── ventral_striatum   <-- THIS MODULE
                            ├── nucleus_accumbens
                            └── olfactory_tubercle

**Primary synonym:** Ventral striatum; limbic striatum; "the
limbic/reward striatum"; nucleus accumbens-septum region (partial —
classical).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container node** — the parent of two ventral striatum children
(``nucleus_accumbens``, ``olfactory_tubercle``).
**Part of:** The **striatum** container — specifically, the
**VENTRAL** (limbic/reward/olfactory) half. The other half is the
**dorsal striatum** (motor/cognitive/associative).
**Structural parent:** ``.../left/subcortical/basal_ganglia/striatum/``
→ **direct child** of the striatum container.
**Structural children (two, closed set):**
``nucleus_accumbens`` and ``olfactory_tubercle``.
**Boundary status (the VENTRAL half of the striatum — NOT the dorsal
striatum):** **Boundary case — the ventral striatum is the LIMBIC/
REWARD/OLFACTORY subsystem; the DORSAL striatum is the MOTOR/
COGNITIVE/ASSOCIATIVE subsystem.** The two halves are **siblings**
under the striatum container, **anatomically separate** (ventral vs.
dorsal), and **functionally distinct** (limbic/reward/olfactory vs.
motor/cognitive/associative). The **ventral striatum** is the
**limbic/reward** half — the structure involved in **addiction**,
**depression**, and **OCD** (and the location of the **olfactory
tubercle**). The **dorsal striatum** is the **motor/cognitive** half
— the structure involved in **Parkinson's disease**,
**Huntington's disease**, **dystonia**, and **Tourette syndrome**.
Consumers must **not** conflate the two — they are **different
striatal subsystems** with **different inputs**, **different
outputs**, and **different clinical associations**.
**Boundary status (the SLEA warning — LIGHT at this level, matching
the globus pallidus container):** **Boundary case — the ventral
striatum contains the NUCLEUS ACCUMBENS, which is part of the
sublenticular extended amygdala (SLEA) in some classifications.**
The **nucleus accumbens** is a **DIRECT CHILD** of the ventral
striatum — so the warning is **LIGHT at this container level** (NOT
**deferred**, as at the striatum container), matching the **globus
pallidus container** on the **output side** (where the **ventral
pallidum** is a direct child). The **light warning** is: the nucleus
accumbens is **NOT the amygdala**, **NOT adjacent** to the amygdala,
and **NOT lateralized**; the **right-amygdala fear association**
belongs to the **amygdala module** and the **extended amygdala
module** — **NOT** to the nucleus accumbens. The **full warning**
belongs to the **nucleus_accumbens leaf**. See *Lateralization
Notes*.
**Boundary status (the TWO CHILDREN are ASYMMETRIC with respect to
the SLEA warning):** **Boundary case — the ventral striatum's two
children have DIFFERENT SLEA status: the NUCLEUS ACCUMBENS is
SLEA-bearing; the OLFACTORY TUBERCLE is SLEA-free.** The **nucleus
accumbens** — the ventral striatum's **primary reward nucleus** — is
part of the **SLEA** in some classifications, and it is the
**input-side SLEA structure** (matching the **output-side** of the
**ventral pallidum**). The **olfactory tubercle** — the **fifth and
final rhinencephalon-excluded structure** — is a **ventral striatum**
child, but it is **NOT** an **SLEA** component. **Being a ventral
striatum child does NOT make a structure SLEA-bearing** — the
**SLEA overlap is specific to the nucleus accumbens**, not to the
ventral striatum as a whole. Consumers must **not** import
amygdala-lateralization claims into the **olfactory tubercle** — it
is **SLEA-free**, and the warning does **not** apply to it.
**Boundary status (the olfactory tubercle is HERE — the FIFTH and
FINAL rhinencephalon-excluded structure):** **Boundary case — the
olfactory tubercle is a CHILD of the ventral striatum, and it is the
FIFTH and FINAL rhinencephalon-excluded structure.** The **olfactory
tubercle** — a **primary olfactory cortical target** on the
**anterior perforated substance** — is classically rhinencephalic.
The tree **excludes** it from the rhinencephalon and places it
**here**, under the **ventral striatum** (because of its **striatal-
like cytoarchitecture**). This is the **fifth and final**
rhinencephalon-excluded structure. **All five** rhinencephalon-
excluded structures are now documented at their tree locations:
*   **Amygdala** → ``medial_temporal_lobe/amygdala/``
*   **Hippocampus** → ``medial_temporal_lobe/hippocampus/``
*   **Septal nuclei** → ``basal_forebrain/septal_nuclei/``
*   **Anterior perforated substance** →
    ``basal_forebrain/anterior_perforated_substance/``
*   **Olfactory tubercle** → **here**, under the **ventral striatum**
Consumers reconstructing the **classical full rhinencephalon** must
**union** the rhinencephalon with **all five** excluded structures.
**Boundary status (the nucleus accumbens is HERE — the INPUT-SIDE
SLEA overlap):** **Boundary case — the nucleus accumbens is a CHILD
of the ventral striatum, and it is the INPUT-SIDE SLEA overlap
(matching the OUTPUT-SIDE overlap of the ventral pallidum).** The
**nucleus accumbens** — the **primary reward nucleus** of the
ventral striatum — is **part of the SLEA** in some classifications —
the **input-side SLEA overlap**, matching the **output-side overlap**
of the **ventral pallidum**. The **basal ganglia's SLEA pair** is
therefore:
*   **Input side:** nucleus accumbens (under the ventral striatum).
*   **Output side:** ventral pallidum (under the globus pallidus).
Both are **wired under the basal ganglia**, both are **split from
the extended amygdala** by the tree, and both carry the **SLEA
warning** at their respective levels — **deferred** at the container
level, **light** at the intermediate container level, and **full** at
the leaf level. See *The Ventral Striatum / Extended Amygdala
Boundary* and *Lateralization Notes*.
**Boundary status (not the dorsal striatum — sibling):** **Boundary
case — the dorsal striatum is a SIBLING under the striatum
container, not a parent or child of the ventral striatum.** The
**dorsal striatum** (caudate + putamen) is the **motor/cognitive**
half; the **ventral striatum** (nucleus accumbens + olfactory
tubercle) is the **limbic/reward/olfactory** half. They are
**structurally separate** (dorsal vs. ventral) and **functionally
distinct**. Consumers that need the **motor/cognitive** subsystem
resolve ``.../dorsal_striatum/``; consumers that need the **limbic/
reward/olfactory** subsystem resolve **this module**. **The SLEA
warning runs ONLY through the ventral side** — the dorsal striatum
is **SLEA-free**.
**Boundary status (not the globus pallidus — the VENTRAL PALLIDUM is
the output-side counterpart):** **Boundary case — the ventral
pallidum is the OUTPUT-SIDE counterpart of the ventral striatum's
NUCLEUS ACCUMBENS, and it is under the globus pallidus container,
not the striatum.** The **nucleus accumbens** (input side) →
**ventral pallidum** (output side) is the **ventral striatopallidal
circuit**. The **ventral pallidum** is under
``.../basal_ganglia/globus_pallidus/ventral_pallidum/`` — **not**
under the ventral striatum. Consumers that need the **output-side
SLEA structure** resolve the **ventral pallidum**; consumers that
need the **input-side SLEA structure** resolve the **nucleus
accumbens**. They are **two halves of the same SLEA pair** —
**separated** by the tree's **basal ganglia split** (striatum vs.
globus pallidus), but **functionally coupled** in the **ventral
striatopallidal circuit**.
**Boundary status (not a single functional system — the two children
have DIFFERENT functions):** **Boundary case — the ventral striatum
is a structural grouping of two functionally distinct children, not
a single functional system.** The **nucleus accumbens** is the
**primary reward nucleus** (reward prediction, motivation,
reinforcement learning, addiction). The **olfactory tubercle** is a
**primary olfactory cortical target** (olfactory-reward association,
olfactory-hypothalamic integration). They are **anatomically
adjacent** (on the **anterior perforated substance**), but they are
**functionally distinct** — the **nucleus accumbens** is **limbic/
reward**, the **olfactory tubercle** is **olfactory/limbic**. Consumers
must **not** treat "ventral striatum" as a single functional system.
**Boundary status (not the ventral tegmental area (VTA) — midbrain
dopaminergic INPUT):** **Boundary case — the VTA provides
DOPAMINERGIC INPUT to the ventral striatum (via the MESOLIMBIC
pathway), but it is a MIDBRAIN structure, not a ventral striatum
child.** The **VTA** → **nucleus accumbens** is the **mesolimbic
dopaminergic pathway**. Its **dysregulation** is the
**neuropathological substrate** of **addiction** — the **signature
clinical association** of the **nucleus accumbens**. The **VTA** is
under ``.../midbrain/tegmentum/ventral_tegmental_area/`` — **not**
under the ventral striatum. Consumers must **not** resolve the VTA
through the ventral striatum, and must **not** treat the ventral
striatum's dopaminergic input as intrinsic to the ventral striatum.
**The ventral striatum is the TARGET; the VTA is the SOURCE.**

Overview
--------
The ventral striatum is the **limbic/reward/olfactory half** of the
striatum — the **input side** of the **ventral striatopallidal
system** — and the **structural home** of the **nucleus accumbens**
(the **primary reward nucleus**) and the **olfactory tubercle** (the
**fifth and final rhinencephalon-excluded structure**). It is
**anatomically adjacent** to the **dorsal striatum** (separated by
a **graded transition** around the **internal capsule** and the
**anterior commissure**), but **functionally distinct** — the
**ventral** half is **limbic/reward/olfactory**, the **dorsal** half
is **motor/cognitive/associative**.

**The ventral striatum is the "limbic striatum."** Its **ventral**
position (vs. the dorsal striatum) and its **limbic cortical** inputs
make it the **limbic/reward** component of the striatum — the
**complement** to the **dorsal striatum's** motor/cognitive role.
The **nucleus accumbens** and **olfactory tubercle** are
**cytoarchitecturally continuous** with the **dorsal striatum** at
the **ventral striatal transition zone**, but they are **functionally
distinct** — the tree wires them as a **separate container** under
the striatum.

**The ventral striatum's two children are ASYMMETRIC with respect to
the SLEA warning.** The **nucleus accumbens** is **SLEA-bearing**
(input-side SLEA overlap, matching the **output-side** of the
**ventral pallidum**); the **olfactory tubercle** is **SLEA-free**
(it is a **ventral striatum** child, but **NOT** an extended-amygdala
component). **Being a ventral striatum child does NOT make a
structure SLEA-bearing** — the **SLEA overlap is specific to the
nucleus accumbens**, not to the ventral striatum as a whole.

**The ventral striatum contains the FIFTH and FINAL rhinencephalon-
excluded structure — the olfactory tubercle.** The **olfactory
tubercle** is under ``nucleus_accumbens/``... no — it is a
**sibling** of the nucleus accumbens, both **direct children** of
the ventral striatum. This **closes the five-structure
rhinencephalon-exclusion loop** — all five excluded structures are
now documented at their tree locations.

**The ventral striatum is the INPUT side of the basal ganglia's SLEA
pair.** The **nucleus accumbens** (a ventral striatum child) carries
the **input-side SLEA overlap**, matching the **output-side overlap**
of the **ventral pallidum**. The **basal ganglia's SLEA pair** is
therefore:
*   **Input side:** nucleus accumbens (under the ventral striatum).
*   **Output side:** ventral pallidum (under the globus pallidus).
Both are **wired under the basal ganglia**, both are **split from
the extended amygdala** by the tree, and both carry the **SLEA
warning** at their respective levels — **deferred** at the container
level, **light** at the intermediate container level, and **full** at
the leaf level.

**The ventral striatum is a paired structure.** Each hemisphere has
its own ventral striatum, with **ipsilateral** cortical and
dopaminergic input. The two sides are **bilaterally symmetric** and
**largely non-lateralized** — the **reward/motivation** functions are
**bilateral**. Some **subtle lateralization** has been reported for
the **nucleus accumbens** (left for **approach/positive affect**,
right for **avoidance/negative affect**), but it is **weak** and
**contested**. See *Lateralization Notes*.

Container Contents (two children, closed set)
----------------------------------------------
The ventral striatum container has **exactly two children**:

*   **``nucleus_accumbens``** — the **primary reward nucleus** of the
    ventral striatum. **SLEA-bearing** (input-side SLEA overlap,
    matching the **output-side** of the **ventral pallidum**).
    **Full SLEA warning** at the leaf level. **Addiction**,
    **depression**, **OCD** (with the caudate), **apathy**.

*   **``olfactory_tubercle``** — a **primary olfactory cortical
    target** on the **anterior perforated substance**. **SLEA-free**
    (it is a **ventral striatum** child, but **NOT** an
    extended-amygdala component). It is the **FIFTH and FINAL
    rhinencephalon-excluded structure** — **no SLEA warning**.

**Not children (deliberately excluded):**
*   **Dorsal striatum** — ``.../dorsal_striatum/`` — **sibling**
    (motor/cognitive half).
*   **Globus pallidus** — ``.../basal_ganglia/globus_pallidus/`` —
    **sibling** of the striatum container (the **output side**;
    its **ventral pallidum** is the **output-side SLEA counterpart**).
*   **Extended amygdala** — ``.../extended_amygdala/`` — **sibling**
    of the basal forebrain, not a child of the ventral striatum. The
    **nucleus accumbens** is a **classificatory overlap** with the
    extended amygdala (SLEA), but the tree **splits** them.
*   **VTA** — ``.../midbrain/tegmentum/ventral_tegmental_area/`` —
    **midbrain** (dopaminergic **input** to the ventral striatum via
    the **mesolimbic pathway**).
*   **Anterior perforated substance** —
    ``.../basal_forebrain/anterior_perforated_substance/`` — the
    **surface** on which the olfactory tubercle sits; a **basal
    forebrain sibling**, not a ventral striatum child.

The Ventral Striatum / Dorsal Striatum Boundary
-----------------------------------------------
This is the **most consequential boundary** in the module:

*   **Ventral striatum** (this module) — the **limbic/reward/
    olfactory** subsystem (nucleus accumbens + olfactory tubercle).
    **SLEA-bearing half.** Projects to the **ventral pallidum**
    (wired).

*   **Dorsal striatum** (``.../dorsal_striatum/``) — the
    **motor/cognitive/associative** subsystem (caudate + putamen).
    **SLEA-free half.** Projects to the **GPe/GPi** (a **documented
    gap**).

**They are siblings under the striatum container.** The **ventral**
half is **limbic/reward/olfactory**; the **dorsal** half is
**motor/cognitive/associative**. Consumers that need the **limbic/
reward** subsystem resolve **this module**; consumers that need the
**motor/cognitive** subsystem resolve ``.../dorsal_striatum/``.

**The SLEA asymmetry between the two siblings:** the **ventral
striatum** contains the **nucleus accumbens** (SLEA-bearing), so it
carries the **light warning** at this container level; the **dorsal
striatum** contains only **SLEA-free** children (caudate, putamen),
so it carries **NO warning**. **The warning gradient runs ONLY
through the ventral side** of the striatum.

The Ventral Striatum / Extended Amygdala Boundary
-------------------------------------------------
This is the **SLEA** boundary — the **light warning** at this level:

*   **Extended amygdala** (``.../extended_amygdala/``) — the **BNST**
    and the **central amygdaloid nucleus**. **Classically** the
    extended amygdala; **SLEA** adds the **ventral pallidum** and
    parts of the **nucleus accumbens**.

*   **Ventral striatum** (this module) — the **nucleus accumbens**
    (a direct child) is part of the **SLEA** classification. The
    **olfactory tubercle** (also a direct child) is **NOT** part of
    the SLEA — it is the **fifth rhinencephalon-excluded structure**,
    but **not** an extended-amygdala component.

**The tree splits them.** The **nucleus accumbens** is under
``.../ventral_striatum/nucleus_accumbens/``, and the **ventral
pallidum** is under
``.../globus_pallidus/ventral_pallidum/`` — **not** under the extended
amygdala. This is a **deliberate boundary choice**. Consumers that
need the **extended amygdala** as a unit (per the SLEA classification)
must **union** ``.../extended_amygdala/`` with the **nucleus
accumbens** and **ventral pallidum** — the tree does **not** provide
this union as a single path.

**The ventral striatum container carries a LIGHT warning**: the
**nucleus accumbens is a DIRECT CHILD** (not a grandchild), so the
warning is **less deferred** than at the **striatum container**
(deferred) or the **basal ganglia container** (deferred), but it is
**still not container-wide** — the **olfactory tubercle** (the other
direct child) is **NOT** SLEA-bearing. **The warning applies
specifically to the nucleus accumbens**, and the **full warning**
belongs to the **nucleus_accumbens leaf**. **The warning gradient**
from the striatum side is now:
*   **Basal ganglia container** — *deferred* (both SLEA structures are
    grandchildren).
*   **Striatum container** — *deferred* (the nucleus accumbens is a
    grandchild).
*   **Ventral striatum container** — *light* (the nucleus accumbens is
    a **direct child**; **this module**).
*   **Nucleus accumbens leaf** — *full* (the structure **itself** has
    the SLEA relationship; pending).

**The corresponding output-side gradient** (from the globus pallidus
side):
*   **Basal ganglia container** — *deferred*.
*   **Globus pallidus container** — *light* (the ventral pallidum is a
    direct child).
*   **Ventral pallidum leaf** — *full*.

**The two gradients are PARALLEL on the light and full levels** —
both the ventral striatum (input side) and the globus pallidus
(output side) are **light**; both the nucleus accumbens (input side)
and the ventral pallidum (output side) are **full**. The **input
side** has **one extra level** (the striatum container) before the
light warning, because the striatum container is **shared** between
the dorsal (no SLEA) and ventral (SLEA) subsystems.

The Ventral Striatum / Midbrain Boundary
----------------------------------------
This is the **dopaminergic input** boundary:

*   **Ventral tegmental area (VTA)** —
    ``.../midbrain/tegmentum/ventral_tegmental_area/`` — the
    **dopaminergic** midbrain nucleus that projects to the **ventral
    striatum** (nucleus accumbens) — the **mesolimbic pathway**. Its
    **dysregulation** is the **neuropathological substrate** of
    **addiction** — the **signature clinical association** of the
    **nucleus accumbens**.

*   **Substantia nigra** —
    ``.../midbrain/tegmentum/substantia_nigra/`` — the **dopaminergic**
    (pars compacta) and **GABAergic** (pars reticulata) **midbrain**
    nucleus. Its **pars compacta** projects primarily to the **dorsal
    striatum** (nigrostriatal pathway); its **pars reticulata**
    receives **striatal output** from the **dorsal striatum**. The
    **substantia nigra** does **not** project directly to the ventral
    striatum in the same way — the **VTA** is the primary dopaminergic
    input to the **ventral** striatum.

*   **Ventral striatum** (this module) — the **dopaminergic TARGET**
    (via the **mesolimbic pathway** from the **VTA**). **Telencephalic**.

**The VTA is NOT a ventral striatum child.** It is a **midbrain**
structure — functionally related (dopaminergic input to the ventral
striatum) but structurally separate. Consumers must **not** resolve
the VTA through the ventral striatum, and must **not** treat the
ventral striatum's dopaminergic input as intrinsic to the ventral
striatum. **The ventral striatum is the TARGET; the VTA is the
SOURCE.**

The Ventral Striatum / Rhinencephalon Boundary
----------------------------------------------
This is the **fifth and final** rhinencephalon-excluded structure
boundary:

*   **Rhinencephalon** (``.../left/rhinencephalon/``) — the **narrow
    olfactory definition** (bulb, tract, AON, piriform, periamygdaloid,
    uncus). The **olfactory tubercle** is **excluded** from this
    definition.

*   **Ventral striatum** (this module) — the **olfactory tubercle** is
    under ``.../ventral_striatum/olfactory_tubercle/``. It is a
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
union the rhinencephalon with **all five** excluded structures.

Function in the Human Brain
---------------------------
The ventral striatum has **two functionally distinct children**:

**Nucleus accumbens (limbic/reward — SLEA-bearing):**

*   **Reward Prediction and Motivation:** The **nucleus accumbens**
    is the **primary reward nucleus** of the ventral striatum — it
    receives **dopaminergic input** from the **VTA** (mesolimbic
    pathway) and **limbic cortical** input. It is involved in
    **reward prediction, motivation, and reinforcement learning** —
    its **dysfunction** is the **signature** of **addiction**.

*   **Motivated Behavior (Limbic-Motor Interface):** The **nucleus
    accumbens** is the **limbic-motor interface** — it receives
    **limbic** input and projects to the **ventral pallidum**, which
    then **gates** reward-related behavior. This is the **anatomical
    substrate** for **motivated behavior**.

*   **Addiction and Depression:** The **nucleus accumbens** is the
    **substrate** of **addiction** (craving, relapse) and
    **depression** (anhedonia, motivation deficits). See the
    **nucleus_accumbens module** (pending) for detail.

**Olfactory tubercle (olfactory/reward — SLEA-free):**

*   **Olfactory-Reward Association:** The **olfactory tubercle** is a
    **primary olfactory cortical target** — it receives **lateral
    olfactory stria** input and **projects to the ventral pallidum**
    (as part of the ventral striatum). It is involved in
    **olfactory-reward association** — the **integration of smell
    with reward**.

*   **Olfactory-Hypothalamic Integration:** The **olfactory tubercle**
    projects to the **lateral hypothalamus** and to the **ventral
    pallidum** — contributing to **olfactory-driven motivated
    behavior** (e.g., **food-seeking**).

*   **NOT an SLEA component:** Despite being a **ventral striatum**
    child, the **olfactory tubercle** is **NOT** part of the **SLEA**
    — the **SLEA warning does NOT apply to it**. It is the **fifth
    rhinencephalon-excluded structure**, but **not** an extended-
    amygdala component.

**The unifying theme:** the ventral striatum is the **input side** of
the **limbic/reward basal ganglia circuit** — the **nucleus
accumbens** is **reward/motivation** (SLEA-bearing), and the
**olfactory tubercle** is **olfactory-reward association**
(SLEA-free). **Both children are fully wired**, but they are
**asymmetric** with respect to the SLEA warning — only the **nucleus
accumbens** carries it.

Associated Disorders
--------------------
The ventral striatum container has **no single syndrome** — its
children's disorders are documented in their own modules:

*   **Nucleus accumbens (limbic/reward — SLEA-bearing):**
    - **Addiction** — **nucleus accumbens dysfunction** (mesolimbic
      pathway dysregulation), producing **craving, compulsive
      drug-seeking, and relapse**.
    - **Depression** — **nucleus accumbens dysfunction**, producing
      **anhedonia and motivation deficits**.
    - **OCD** — **nucleus accumbens dysfunction** (with the caudate),
      contributing to **obsessions and compulsions**.
    - **Apathy** — **nucleus accumbens dysfunction**, producing
      **loss of motivation**.

*   **Olfactory tubercle (olfactory/reward — SLEA-free):**
    - **Olfactory dysfunction** — **olfactory tubercle involvement**
      in **anosmia, hyposmia, or olfactory agnosia**.
    - **Olfactory-reward association deficits** — **impaired
      integration of smell with reward** (e.g., **food-seeking**
      deficits).

*   **Container-level:** **no single syndrome** — the ventral striatum
  is a **structural grouping**, and its disorders are the **aggregate**
  of its children's disorders.

**What is NOT here:** The ventral striatum is **not** the substrate
for **Parkinson's disease** (that is the **putamen** — dorsal
striatum), **Huntington's disease** (that is the **caudate** — dorsal
striatum), **dystonia** (that is the **putamen**), **Tourette
syndrome** (that is the **caudate**), **Kluver-Bucy syndrome** (that
is the **amygdala**), or **temporal lobe epilepsy** (that is the
**hippocampus**). Its clinical footprint is **limbic/reward**
(addiction, depression, OCD) and **olfactory** (olfactory
dysfunction) — a **distinct category** from the **dorsal striatum's**
**motor/cognitive** footprint.

Lateralization Notes
--------------------
This is the **left** ventral striatum container. The ventral striatum
is **bilaterally symmetric** and **largely non-lateralized** — but
the **light warning** from the SLEA overlap applies at this level:

*   **Bilateral Reward Functions:** Each ventral striatum projects
    **ipsilaterally** to the ventral pallidum. The two sides are
    **functionally symmetric** for reward, motivation, and gating.
    **Addiction** and **depression** are **bilateral** in the ventral
    striatum.

*   **Partial Lateralization (Contested — Nucleus Accumbens):** The
    **nucleus accumbens** has been reported to show **subtle**
    lateralization — **left nucleus accumbens** for **approach/
    positive affect**, **right nucleus accumbens** for **avoidance/
    negative affect**. This is **weak** and **contested**, and it is
    documented in the **nucleus_accumbens module** (pending), **not**
    as a strong classification basis for the container. **The
    olfactory tubercle** has **no reported lateralization**.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the ventral striatum container has **no
    documented strong left-lateralized or right-lateralized
    function**.

*   **LIGHT SLEA WARNING (the third level of the input-side
    gradient):** The **nucleus accumbens** is a **direct child** of
    the ventral striatum with **classificatory overlap** with the
    extended amygdala (SLEA), so the **warning is LIGHT at this
    container level** — matching the **globus pallidus container** on
    the **output side** (where the **ventral pallidum** is a direct
    child). The **warning is**:
    - The **nucleus accumbens** is **not the amygdala**.
    - It is **not adjacent** to the amygdala.
    - It is **not lateralized**.
    - The **SLEA continuum** is **broadly bilateral**.
    - The **right amygdala's fear-processing association** belongs to
      the **amygdala module** and the **extended amygdala module** —
      **not** to the nucleus accumbens.
    **The warning applies specifically to the nucleus accumbens**, NOT
    to the **olfactory tubercle** (which is SLEA-free).

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module** — **not** to the ventral striatum, **not** to
    the nucleus accumbens (which is the **next level down**), and
    **not** to the olfactory tubercle (which is **SLEA-free**).
    Consumers must **not** import the right-amygdala fear association
    into the ventral striatum container.

**A consumer that assumes "left ventral striatum = right ventral
striatum" will be structurally and functionally correct** — the two
sides are **largely symmetric**, no **strong** lateralized syndrome
has been demonstrated, and the **weak** lateralization reported for
the nucleus accumbens is **contested**, not a strong classification
basis. The ventral striatum container is a **strict-mirror pair with
a LIGHT warning** — matching the **globus pallidus container** on the
**output side**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../extended_amygdala/``, or any other
    container. The ventral striatum's relationships to the VTA,
    extended amygdala, dorsal striatum, and rhinencephalon are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — two children, closed set.** The ventral
    striatum container has exactly two children: ``nucleus_accumbens``
    and ``olfactory_tubercle``. Consumers may iterate them, but
    should not assume any others exist.
*   **The TWO CHILDREN are ASYMMETRIC with respect to the SLEA
    warning.** The **nucleus accumbens** is **SLEA-bearing** (full
    warning at the leaf); the **olfactory tubercle** is **SLEA-free**
    (no warning). **Being a ventral striatum child does NOT make a
    structure SLEA-bearing** — the SLEA overlap is specific to the
    **nucleus accumbens**, not to the ventral striatum as a whole.
*   **The olfactory tubercle is HERE — the FIFTH and FINAL
    rhinencephalon-excluded structure.** This is the **last of the
    five** — **all five** are now documented at their tree locations.
    Consumers reconstructing the **classical full rhinencephalon**
    must **union** the rhinencephalon with the **ventral striatum
    container** (specifically, the olfactory tubercle).
*   **The nucleus accumbens is HERE — the INPUT-SIDE SLEA overlap.**
    The nucleus accumbens carries the **input-side SLEA overlap**,
    matching the **output-side overlap** of the **ventral pallidum**.
    The **basal ganglia's SLEA pair** is now **both sides
    identified**.
*   **Extended amygdala overlap — LIGHT warning at this level.**
    The **nucleus accumbens is a DIRECT CHILD** of the ventral
    striatum, so the warning is **light at this level** (matching
    the **globus pallidus container** on the output side) — **not
    deferred** (as at the striatum and basal ganglia containers) and
    **not full** (as at the nucleus_accumbens leaf). The **warning
    applies specifically to the nucleus accumbens**, NOT to the
    olfactory tubercle.
*   **Not the dorsal striatum — sibling.** The dorsal striatum is the
    **motor/cognitive** half; the ventral striatum is the **limbic/
    reward** half. They are **siblings** under the striatum.
*   **Not the VTA — midbrain input.** The VTA provides dopaminergic
    input to the ventral striatum (mesolimbic pathway). It is a
    **midbrain** structure, not a ventral striatum child.
*   **No ``AREA_PATHS`` hop.** The ventral striatum is a local
    container under the striatum, not a cross-listed leaf.
*   **No nested cross-listing.** The ventral striatum has no nested
    dual-framing module. It is a single container.
*   **Structural parity with right ventral striatum — strict mirror
    with a LIGHT warning.** Left and right ventral striatum modules
    are **structurally identical** — same two children, same SLEA
    asymmetry (nucleus accumbens SLEA-bearing, olfactory tubercle
    SLEA-free), same fifth rhinencephalon-excluded redirect, same
    light warning. **The right-side module carries the light warning
    explicitly** — matching the right globus pallidus container —
    because the right nucleus accumbens (the direct child) carries
    the right-amygdala association temptation.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_ganglia.striatum import ventral_striatum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "basal_ganglia.striatum.ventral_striatum"
    )

**Do not** assume the ventral striatum is the **dorsal striatum**. The
**ventral** half is **limbic/reward/olfactory** (nucleus accumbens +
olfactory tubercle); the **dorsal** half is **motor/cognitive/
associative** (caudate + putamen). They are **different striatal
subsystems**.

**Do not** assume the ventral striatum **contains** the VTA or
extended amygdala. Those are **midbrain or extended amygdala**
structures, not ventral striatum children.

**Do not** assume the ventral striatum is a **single functional
system**. Its **nucleus accumbens** (reward/motivation) and
**olfactory tubercle** (olfactory-reward association) are
**functionally distinct**.

**Do not** assume **both** ventral striatum children are
**SLEA-bearing**. The **nucleus accumbens** is **SLEA-bearing**; the
**olfactory tubercle** is **SLEA-free**. **The SLEA warning applies
specifically to the nucleus accumbens**, not to the olfactory
tubercle.

**Do not** import **amygdala-lateralization claims** into the ventral
striatum container. The **nucleus accumbens** (a direct child) has
**classificatory overlap** with the extended amygdala (SLEA), but the
warning is **LIGHT at this container level** — the **full warning**
belongs to the **nucleus_accumbens leaf**, and the **olfactory
tubercle is NOT SLEA-bearing**.

Iterating the ventral striatum container's two children (recommended
consumer pattern)::

    VENTRAL_STRIATUM_CHILDREN = (
        "nucleus_accumbens",
        "olfactory_tubercle",
    )
    # Closed set. The two children are ASYMMETRIC with respect to
    # the SLEA warning: nucleus_accumbens is SLEA-bearing,
    # olfactory_tubercle is SLEA-free.

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
    # NOTE: the olfactory tubercle is NOT part of the SLEA union.

Reaching the VTA (recommended consumer pattern — NOTE the midbrain
boundary)::

    # The VTA is FUNCTIONALLY related to the ventral striatum
    # (dopaminergic input, mesolimbic pathway) but STRUCTURALLY
    # separate (midbrain):
    #
    #   midbrain.tegmentum.ventral_tegmental_area
    #
    # The VTA is the SOURCE of the dopaminergic input; the ventral
    # striatum is the TARGET.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        vs_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.striatum.ventral_striatum"
        )
        # resolve vs_path through the memory/recall layer

References
----------
*   **Canonical ventral striatum anatomy:** Heimer, L., Wilson, R.D.
    (1975). "The subcortical projections of the allocortex:
    similarities in the neural associations of the hippocampus, the
    piriform cortex, and the neocortex." In *Golgi Centennial
    Symposium* (Santini, M., ed.). (Ventral striatum; nucleus
    accumbens; olfactory tubercle as ventral striatum structures.)
*   **Ventral striatum functional anatomy:** Mogenson, G.J., Jones,
    D.L., Yim, C.Y. (1980). "From motivation to action: functional
    interface between the limbic system and the motor system."
    *Progress in Neurobiology* 14:69–97. (Ventral striatum as
    limbic-motor interface; nucleus accumbens.)
*   **Dorsal vs ventral striatum:** Voorn, P., Vanderschuren, L.J.,
    Groenewegen, H.J., Robbins, T.W., Pennartz, C.M. (2004). "Putting
    a spin on the dorsal-ventral divide of the striatum." *Trends in
    Neurosciences* 27:468–474. (Dorsal/ventral functional
    distinction.)
*   **Nucleus accumbens reward:** Berridge, K.C., Kringelbach, M.L.
    (2015). "Pleasure systems in the brain." *Neuron* 86:646–664.
    (Nucleus accumbens in reward and hedonic processing.)
*   **Olfactory tubercle:** Heimer, L., Wilson, R.D. (1975). "The
    subcortical projections of the allocortex: similarities in the
    neural associations of the hippocampus, the piriform cortex, and
    the neocortex." In *Golgi Centennial Symposium* (Santini, M.,
    ed.). (Olfactory tubercle as a ventral striatum structure;
    olfactory-reward association.)
*   **Extended amygdala / SLEA:** Alheid, G.F., Heimer, L. (1988).
    "New perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA; nucleus accumbens and ventral pallidum in the
    extended amygdala continuum.)
*   **Addiction:** Koob, G.F., Volkow, N.D. (2010). "Neurocircuitry
    of addiction." *Neuropsychopharmacology* 35:217–238. (Nucleus
    accumbens and ventral striatum in addiction.)
*   **VTA / mesolimbic pathway (contrast):** Nestler, E.J. (2005).
    "Is there a common molecular pathway for addiction?" *Nature
    Neuroscience* 8:1445–1449. (VTA as the source of dopaminergic
    input to the ventral striatum; the VTA is a midbrain structure,
    not a ventral striatum child.)
*   **Nucleus accumbens lateralization (weak, contested):** Davidson,
    R.J., Irwin, W. (1999). "The functional neuroanatomy of emotion
    and affective style." *Trends in Cognitive Sciences* 3:11–21.
    (Left/right nucleus accumbens and approach/avoidance — weak,
    contested lateralization.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the ventral striatum container
    — the nucleus accumbens's SLEA relationship is light-warned at
    this level and full-warned at the nucleus_accumbens leaf, and the
    olfactory tubercle is SLEA-free.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Ventral striatum in overview.)
*   NeuroNames — Ventral striatum (left); FMA — Ventral striatum
    (left member).
"""