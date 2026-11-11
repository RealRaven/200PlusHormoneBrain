"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.amygdala.autonomic_nervous_system
=============================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── medial_temporal_lobe
                    └── amygdala
                        └── autonomic_nervous_system   <-- THIS MODULE

**Primary synonym:** Autonomic nervous system (ANS) output of the
amygdala; amygdalo-autonomic pathways; central nucleus autonomic
efferents; "the amygdala's autonomic output system."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**pathway-effector system** — the **sympathetic and
parasympathetic output pathways** from the **amygdala**
(specifically the **central nucleus**) to the **hypothalamus,
brainstem, and spinal cord** autonomic centers.
**Part of:** The **amygdala** container — specifically, the
**fear-output effector** component (with the **central nucleus**
as the **fear-output source structure** and the **basolateral
nuclei** as the **fear-learning structures**). The **amygdala** is
the **fear/emotion/salience** container of the medial temporal
lobe.
**Structural parent:** ``.../right/subcortical/medial_temporal_lobe/amygdala/``
→ **direct child** of the amygdala container.
**Structural children:** **None.** This is a **leaf** module. The
**sympathetic branch**, **parasympathetic branch**, and
**specific target nuclei** (hypothalamus, PAG, parabrachial
nucleus, NTS, dorsal motor nucleus of vagus, RVLM, spinal
intermediolateral cell column) are documented as **prose**, not as
structural children.
**Boundary status (EFFECTOR SYSTEM — NOT a grey-matter structure):**
**Boundary case — the autonomic_nervous_system child is the
EFFECTOR SYSTEM (pathways and targets) of the amygdala's fear
response, NOT a grey-matter structure.** It is the **sympathetic
and parasympathetic output pathways** from the **amygdala**
(especially the **central nucleus**) to the **hypothalamus**,
**brainstem**, and **spinal cord** autonomic centers. It is **NOT
a nucleus** (like the central nucleus or basolateral nuclei), and
it is **NOT a cortical region** (like the frontotemporal cortical
system) — it is the **effector pathway system** that **translates**
the amygdala's fear signal into **autonomic responses**.
Consumers must **not** treat it as a **grey-matter structure** —
it is a **conduction-effector system**.
**Boundary status (NOT the central nucleus — the central nucleus is
the SOURCE):** **Boundary case — the autonomic_nervous_system is
NOT the central nucleus; the central nucleus is the SOURCE
structure.** The **central nucleus** (``.../central_nucleus/``) is
the **grey-matter fear-output structure** — it **integrates** the
fear signal and **projects** to the autonomic centers. The
**autonomic_nervous_system** (here) is the **effector pathway
system** — the **sympathetic and parasympathetic output pathways**
that the central nucleus **drives**. **The central nucleus is the
source; the autonomic_nervous_system is the effector system.**
Consumers must **not** conflate the two — the **central nucleus**
is the **grey-matter fear-output structure**; the
**autonomic_nervous_system** is the **effector system**.
**Boundary status (NOT the hypothalamus or brainstem — those are
the TARGETS):** **Boundary case — the autonomic_nervous_system is
NOT the hypothalamus or the brainstem; those are the TARGET
structures of the autonomic pathways.** The **hypothalamus**
(``.../diencephalon/hypothalamus/``), the **periaqueductal gray
(PAG)** (``.../midbrain/tegmentum/periaqueductal_gray/``), the
**parabrachial nucleus** (``.../hindbrain/metencephalon/pons/parabrachial_area/``),
the **nucleus of the solitary tract (NTS)** and the **dorsal motor
nucleus of the vagus** (``.../hindbrain/myelencephalon/medulla_oblongata/``),
the **rostral ventrolateral medulla (RVLM)**, and the **spinal
intermediolateral cell column** are the **TARGET structures** of
the autonomic pathways. The **autonomic_nervous_system** is the
**pathway-effector system** — the **amygdala-side output** that
**projects to** these targets. Consumers must **not** conflate the
**pathway-effector system** (here) with the **target structures**
(under diencephalon, midbrain, hindbrain, and spinal cord).
**Boundary status (NOT a neural processor — the effector system is
CONDUCTION and EFFECTOR):** **Boundary case — the
autonomic_nervous_system is a CONDUCTION-EFFECTOR system, NOT a
neural processor.** It **conducts** the amygdala's fear signal to
the autonomic centers and **drives** the autonomic effectors
(sympathetic and parasympathetic) — but it does **not process**
the signal. The **processing** happens in the **central nucleus**
(fear-output integration) and the **target structures**
(hypothalamus, brainstem, spinal cord). Consumers must **not**
treat the autonomic_nervous_system as a neural processor.
**Boundary status (SLEA-FREE — the effector system is NOT an
extended-amygdala component):** **Boundary case — the
autonomic_nervous_system is SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component** in
the amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The
**autonomic_nervous_system** is an **effector pathway system** —
it is **NOT** an extended-amygdala component, and it carries **NO
SLEA warning**. Consumers must **not** import the SLEA warning
into the autonomic_nervous_system — it is **SLEA-free**.
**Boundary status (NOT the fear-output structure — the effector
system is the OUTPUT, not the fear-output itself):** **Boundary
case — the autonomic_nervous_system is the OUTPUT of the fear
response, NOT the fear-output structure itself.** The
**fear-output structure** is the **central nucleus** — it
**integrates** the fear signal. The **autonomic_nervous_system**
is the **effector output** — it **translates** the central
nucleus's signal into **autonomic responses**. The **right-amygdala
fear association** belongs to the **central nucleus** and
**basolateral nuclei** — **NOT** to the autonomic_nervous_system.
Consumers must **not** import the right-amygdala fear association
into the autonomic_nervous_system — it is an **effector system**,
not a **fear-output structure**.
**Boundary status (NOT a single functional system — SYMPATHETIC and
PARASYMPATHETIC branches, MULTIPLE targets):** **Boundary case —
the autonomic_nervous_system is a HETEROGENEOUS effector system
with SYMPATHETIC and PARASYMPATHETIC branches and MULTIPLE
targets, not a single pathway.** The **sympathetic branch**
(thoracolumbar — **fight-or-flight**) and the **parasympathetic
branch** (craniosacral — **rest-and-digest**) are **functionally
opposite** and project to **different target structures**. The
**amygdala** (via the central nucleus) primarily drives the
**sympathetic** response to **threat** — **tachycardia**,
**hypertension**, **tachypnea**, **mydriasis**, **diaphoresis** —
but it also modulates **parasympathetic** functions (e.g.,
**gastrointestinal** responses to stress). Consumers must **not**
treat the autonomic_nervous_system as a single pathway — it is a
**heterogeneous effector system**.
**Boundary status (NOT the stria terminalis — different output
pathway):** **Boundary case — the autonomic_nervous_system is NOT
the stria terminalis.** The **stria terminalis** (wired under the
**extended amygdala** container) is the **amygdala → BNST /
septal** pathway — the **SLEA fear-anxiety continuum**
connection. The **autonomic_nervous_system** (here) is the
**amygdala → hypothalamus / brainstem / spinal cord** effector
system — the **autonomic output** pathway. They are **different
output pathways** with **different targets** (BNST / septal vs.
autonomic centers). Consumers must **not** conflate the two.
**Boundary status (NOT the medial temporal lobe, amygdala
container, or hippocampus — a leaf child of the amygdala):**
**Boundary case — the autonomic_nervous_system is a LEAF child of
the amygdala container, not the container itself, and not the
medial temporal lobe or the hippocampus.** The **amygdala**
container contains the **autonomic_nervous_system** and **nine
other children**. Consumers must **not** conflate the effector
system with the amygdala container, the medial temporal lobe, or
the hippocampus.

Overview
--------
The autonomic nervous system child is the **effector output** of the
amygdala's fear response — the **sympathetic and parasympathetic
pathways** that translate the central nucleus's fear signal into
**autonomic responses**: **heart rate** (tachycardia), **blood
pressure** (hypertension), **respiration** (tachypnea),
**pupillary dilation** (mydriasis), **electrodermal activity**
(diaphoresis), and **gastrointestinal** responses. It is a **leaf**
module under the amygdala container, and it is the **effector
system** that the **central nucleus** drives.

**The autonomic_nervous_system is the OUTPUT of the fear response.**
The **central nucleus** (``.../central_nucleus/``) is the
**grey-matter fear-output structure** — it **integrates** the fear
signal. The **autonomic_nervous_system** (here) is the **effector
pathway system** — it **conducts** the central nucleus's signal to
the **hypothalamus**, **brainstem**, and **spinal cord** autonomic
centers, and it **drives** the **sympathetic** (fight-or-flight)
and **parasympathetic** (rest-and-digest) effectors.

**The autonomic_nervous_system is NOT the central nucleus.** The
**central nucleus** is the **source** (the grey-matter fear-output
structure); the **autonomic_nervous_system** is the **effector
system** (the pathways and targets). Consumers must **not**
conflate the two — the **central nucleus** **integrates** the
fear signal; the **autonomic_nervous_system** **executes** it.

**The autonomic_nervous_system is NOT the hypothalamus or the
brainstem.** The **hypothalamus** (under diencephalon), the
**PAG** (under midbrain), the **parabrachial nucleus**, **NTS**,
**dorsal motor nucleus of the vagus** (under hindbrain), the
**RVLM**, and the **spinal intermediolateral cell column** are the
**target structures** of the autonomic pathways. The
**autonomic_nervous_system** is the **amygdala-side effector
system** — the **pathways** that **project to** these targets.

**The autonomic_nervous_system is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The autonomic_nervous_system is a paired structure.** Each
hemisphere has its own autonomic output system, with **ipsilateral**
and **bilateral** projections to the autonomic centers. The two
sides are **bilaterally symmetric** and **functionally
non-lateralized** — the **autonomic** responses are **bilateral**.
See *Lateralization Notes*.

Pathway Composition (prose, not structural children)
----------------------------------------------------
The autonomic_nervous_system is a **distributed effector system**
— documented as **prose**, not as structural children:

*   **Central nucleus → hypothalamus (lateral and paraventricular
    nuclei)** — the **HPA axis** and **sympathetic activation**
    pathway. The **central nucleus** projects to the
    **paraventricular nucleus** (CRH release → **cortisol**) and
    the **lateral hypothalamus** (**sympathetic activation**).

*   **Central nucleus → periaqueductal gray (PAG)** — the
    **defensive behavior and autonomic** pathway. The **PAG**
    coordinates **freezing**, **fight-or-flight**, and
    **autonomic** responses to **threat**.

*   **Central nucleus → parabrachial nucleus** — the
    **respiratory and cardiovascular** pathway. The **parabrachial
    nucleus** relays to the **NTS** and the **RVLM** for
    **respiratory** and **cardiovascular** control.

*   **Central nucleus → nucleus of the solitary tract (NTS)** —
    the **visceral afferent and parasympathetic** pathway. The
    **NTS** integrates **visceral afferents** and modulates
    **parasympathetic** outflow.

*   **Central nucleus → dorsal motor nucleus of the vagus** — the
    **parasympathetic** pathway. The **dorsal motor nucleus of the
    vagus** drives **parasympathetic** control of **heart rate**,
    **gastrointestinal motility**, and **secretions**.

*   **Central nucleus → rostral ventrolateral medulla (RVLM)** —
    the **sympathetic** pathway. The **RVLM** is the **sympathetic
    premotor** center — it drives **sympathetic** outflow to the
    **spinal intermediolateral cell column**.

*   **Central nucleus → spinal intermediolateral cell column** —
    the **sympathetic preganglionic** pathway. The
    **intermediolateral cell column** (T1–L2) contains the
    **sympathetic preganglionic neurons** that innervate the
    **sympathetic ganglia**.

**These pathways are prose, not structural children.** The tree
wires the **autonomic_nervous_system** as a **single leaf** under
the amygdala — the **sympathetic** and **parasympathetic** branches
and their **target nuclei** are **prose**, not structural children.
Consumers that need **pathway-level** resolution should consult the
references, not the tree.

The Autonomic_Nervous_System / Central Nucleus Boundary
-------------------------------------------------------
This is the **source-effector** boundary:

*   **Autonomic_nervous_system** (this module) — the **effector
    pathway system** (the **sympathetic and parasympathetic
    output**).

*   **Central nucleus** (``.../central_nucleus/``) — the
    **grey-matter fear-output structure** (the **source**).

**The central nucleus is the SOURCE; the autonomic_nervous_system
is the EFFECTOR SYSTEM.** Consumers must **not** conflate the two —
the **central nucleus** **integrates** the fear signal; the
**autonomic_nervous_system** **executes** it.

The Autonomic_Nervous_System / Stria Terminalis Boundary
--------------------------------------------------------
This is the **different output pathway** boundary:

*   **Autonomic_nervous_system** (this module) — the **amygdala →
    hypothalamus / brainstem / spinal cord** effector system.

*   **Stria terminalis** (``.../extended_amygdala/stria_terminalis/``)
    — the **amygdala → BNST / septal** pathway (the **SLEA
    fear-anxiety continuum** connection).

**They are different output pathways** with **different targets**
(hypothalamus / brainstem / spinal cord vs. BNST / septal).
Consumers must **not** conflate the two.

The Autonomic_Nervous_System / Hypothalamus and Brainstem Boundary
------------------------------------------------------------------
This is the **target** boundary:

*   **Autonomic_nervous_system** (this module) — the **effector
    pathway system**.

*   **Target structures** — the **hypothalamus** (diencephalon),
    **PAG** (midbrain), **parabrachial nucleus**, **NTS**, **dorsal
    motor nucleus of the vagus** (hindbrain), **RVLM**, and **spinal
    intermediolateral cell column** (spinal cord).

**The target structures are NOT under the amygdala** — they are
under **diencephalon**, **midbrain**, **hindbrain**, and **spinal
cord**. Consumers must **not** conflate the **effector pathway
system** (here) with the **target structures**.

The Autonomic_Nervous_System / SLEA Boundary
--------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Autonomic_nervous_system** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The autonomic_nervous_system is NOT part of the SLEA continuum.**
It is an **effector pathway system**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
autonomic_nervous_system.

Function in the Human Brain
---------------------------
The autonomic_nervous_system's function is **effector output** —
**NOT neural processing**:

*   **Sympathetic Activation (Fight-or-Flight):** The
    **amygdala** (via the **central nucleus**) drives the
    **sympathetic** response to **threat** — **tachycardia**,
    **hypertension**, **tachypnea**, **mydriasis**, **diaphoresis**,
    **pilorection**, and **splanchnic vasoconstriction**. This is
    the **effector output** of the fear response.

*   **HPA Axis Activation (Cortisol Release):** The **central
    nucleus** projects to the **paraventricular nucleus** of the
    **hypothalamus** — driving **CRH release**, **ACTH release**,
    and **cortisol** secretion. This is the **endocrine** component
    of the stress response.

*   **Parasympathetic Modulation (Rest-and-Digest):** The
    **amygdala** also **modulates** the **parasympathetic** system
    — **gastrointestinal** responses to stress (**"butterflies in
    the stomach"**), **salivary** changes, and **bladder**
    responses. The **parasympathetic** modulation is **less
    dominant** than the **sympathetic** activation, but it is
    **functionally relevant**.

*   **Freezing and Defensive Behavior (via the PAG):** The
    **amygdala → PAG** pathway drives **freezing** and **defensive
    behavior** — the **behavioral** component of the fear response,
    coordinated with the **autonomic** component.

*   **NOT a neural processor.** The **autonomic_nervous_system**
    is an **effector system** — it **conducts** and **executes**
    the fear signal but does **not process** it. The **processing**
    happens in the **central nucleus** (fear-output integration) and
    the **target structures** (hypothalamus, brainstem, spinal
    cord).

**The unifying theme:** the autonomic_nervous_system is the
**effector output** of the amygdala's fear response — the
**sympathetic and parasympathetic pathways** that translate the
central nucleus's fear signal into **autonomic responses**,
**HPA axis activation**, and **defensive behavior**. It is
**SLEA-free**, **effector**, and **NOT the fear-output structure** —
the **fear-output** is the **central nucleus**, and the
**autonomic_nervous_system** is the **effector system** that
**executes** it.

Associated Disorders
--------------------
The autonomic_nervous_system has **no named clinical syndrome** —
its clinical associations are **indirect**, via the structures it
connects:

*   **PTSD (Autonomic Hyperarousal):** The **amygdala-autonomic**
    pathway is **hyperactive** in **PTSD** — **elevated heart
    rate**, **hypertension**, **hyperventilation**, **diaphoresis**,
    and **exaggerated startle**. The **autonomic** hyperarousal is
    a **signature** of **PTSD** — the **effector system** is
    **dysregulated**.

*   **Panic Disorder (Autonomic Surge):** The **amygdala-autonomic**
    pathway is **hyperactive** in **panic disorder** — **sudden
    autonomic surges** (**tachycardia**, **dyspnea**,
    **diaphoresis**, **tremor**) that are the **core** of
    **panic attacks**.

*   **Anxiety Disorders (Autonomic Hyperactivity):** The
    **amygdala-autonomic** pathway is **hyperactive** in
    **generalized anxiety disorder** and **social anxiety
    disorder** — **chronic autonomic** symptoms (**restlessness**,
    **muscle tension**, **gastrointestinal** distress).

*   **Cardiovascular Disease (Stress-Related):** **Chronic
    amygdala-autonomic** activation contributes to
    **hypertension**, **arrhythmias**, and **coronary artery
    disease** — the **stress-autonomic** pathway is a **risk
    factor** for **cardiovascular disease**.

*   **No Named "Amygdala-Autonomic Syndrome":** The
    autonomic_nervous_system is an **effector system**, not a
    **grey-matter structure** — it has **no named clinical
    syndrome**. Its clinical relevance is **indirect**, via the
    **autonomic** responses it **drives**.

**What is NOT here:** The autonomic_nervous_system is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **fear conditioning** (central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), or **Alzheimer's disease** (hippocampus). Its
clinical relevance is **indirect**, via the **autonomic** responses
it **drives**. **No named amygdala-autonomic syndrome exists.**

Lateralization Notes
--------------------
This is the **right** autonomic_nervous_system module. The
autonomic_nervous_system is **bilaterally symmetric** and
**functionally non-lateralized** — and it carries **NO warning**:

*   **Bilateral Autonomic Output:** Each hemisphere's autonomic
    output system projects **ipsilaterally** and **bilaterally**
    to the autonomic centers. The two sides are **functionally
    symmetric** for autonomic responses.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left
    semantic / right social), the autonomic_nervous_system has
    **no documented strong left-lateralized or right-lateralized
    function**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    autonomic_nervous_system is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning or the amygdala-lateralization warning into the
    autonomic_nervous_system.

*   **NO Amygdala-Lateralization Warning (the effector system is
    NOT the fear-output structure):** The **right-amygdala fear
    association** belongs to the **central nucleus** and
    **basolateral nuclei** — **NOT** to the
    **autonomic_nervous_system**. The autonomic_nervous_system is
    an **effector system**, not a **fear-output structure**.
    Consumers must **not** import the right-amygdala fear
    association into the autonomic_nervous_system. **This is true
    on the right side as well** — the right autonomic_nervous_system
    is an effector pathway system with **no SLEA relationship** and
    **no fear-output function** of its own.

**A consumer that assumes "right autonomic_nervous_system = left
autonomic_nervous_system" will be structurally correct** — the two
sides are **symmetric** and **non-lateralized**. The
autonomic_nervous_system is a **strict-mirror pair with NO
warning** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag of its own**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../central_nucleus/``, ``.../extended_amygdala/``,
    ``.../diencephalon/``, ``.../midbrain/``, ``.../hindbrain/``,
    or the **spinal cord**. The autonomic_nervous_system's
    relationships to the central nucleus, stria terminalis,
    hypothalamus, brainstem, and spinal cord are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **sympathetic**
    and **parasympathetic** branches and their **target nuclei**
    are documented as **prose**, not as sub-modules. Consumers must
    not assume any exist as children; resolve pathway-level detail
    through the references.
*   **EFFECTOR SYSTEM — NOT a grey-matter structure.** The
    autonomic_nervous_system is a **conduction-effector pathway
    system**, not a **nucleus** or a **cortical region**. Consumers
    must **not** treat it as a **grey-matter structure**.
*   **NOT the central nucleus — the central nucleus is the SOURCE.**
    The **central nucleus** is the **grey-matter fear-output
    structure**; the **autonomic_nervous_system** is the **effector
    pathway system**. Consumers must **not** conflate the two.
*   **NOT the hypothalamus or brainstem — those are the TARGETS.**
    The **hypothalamus**, **PAG**, **parabrachial nucleus**, **NTS**,
    **dorsal motor nucleus of the vagus**, **RVLM**, and **spinal
    intermediolateral cell column** are the **target structures** —
    under **diencephalon**, **midbrain**, **hindbrain**, and
    **spinal cord**. Consumers must **not** conflate the **effector
    pathway system** with the **target structures**.
*   **NOT a neural processor — the effector system is CONDUCTION
    and EFFECTOR.** The autonomic_nervous_system **conducts** and
    **executes** the fear signal but does **not process** it.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    autonomic_nervous_system is **not** an extended-amygdala
    component, and it carries **no SLEA warning**.
*   **NOT the fear-output structure — the effector system is the
    OUTPUT.** The **fear-output structure** is the **central
    nucleus**; the **autonomic_nervous_system** is the **effector
    output**. Consumers must **not** import the right-amygdala fear
    association into the autonomic_nervous_system. **The right-side
    module carries the same no-warning status** — the right
    autonomic_nervous_system is an effector pathway system with
    **no SLEA relationship** and **no fear-output function** of its
    own.
*   **NOT a single functional system — SYMPATHETIC and
    PARASYMPATHETIC branches, MULTIPLE targets.** The
    **sympathetic** and **parasympathetic** branches are
    **functionally opposite** and project to **different target
    structures**. Consumers must **not** treat the
    autonomic_nervous_system as a single pathway.
*   **NOT the stria terminalis — different output pathway.** The
    **stria terminalis** is the **amygdala → BNST / septal**
    pathway; the **autonomic_nervous_system** is the **amygdala →
    hypothalamus / brainstem / spinal cord** effector system.
*   **No ``AREA_PATHS`` hop.** The autonomic_nervous_system is a
    local leaf under the amygdala, not a cross-listed leaf.
*   **No nested cross-listing.** The autonomic_nervous_system has
    no nested dual-framing module. It is a single leaf.
*   **Structural parity with left autonomic_nervous_system —
    strict mirror with NO warning.** Right and left
    autonomic_nervous_system modules are **structurally identical**
    — same leaf status, same **effector system** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.amygdala import autonomic_nervous_system

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "medial_temporal_lobe.amygdala.autonomic_nervous_system"
    )

**Do not** assume the autonomic_nervous_system is the **central
nucleus**. The **central nucleus** is the **grey-matter fear-output
structure** (the **source**); the **autonomic_nervous_system** is
the **effector pathway system** (the **output**). They are
**different structures**.

**Do not** assume the autonomic_nervous_system is the
**hypothalamus** or the **brainstem**. Those are the **target
structures** of the autonomic pathways — under **diencephalon**,
**midbrain**, and **hindbrain**. The **autonomic_nervous_system**
is the **amygdala-side effector system**.

**Do not** assume the autonomic_nervous_system is the **stria
terminalis**. The **stria terminalis** is the **amygdala → BNST /
septal** pathway; the **autonomic_nervous_system** is the **amygdala
→ hypothalamus / brainstem / spinal cord** effector system. They
are **different output pathways**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the
autonomic_nervous_system. **The autonomic_nervous_system is
SLEA-FREE** — it is **not** an extended-amygdala component, and it
is **NOT the fear-output structure**. **The right-side module
carries the same no-warning status** — the right
autonomic_nervous_system is an effector pathway system with **no
SLEA relationship** and **no fear-output function** of its own.

**Do not** treat the autonomic_nervous_system as a **single
pathway**. It is a **heterogeneous effector system** with
**sympathetic** and **parasympathetic** branches and **multiple
target structures**.

Iterating the autonomic_nervous_system's (empty) children
(recommended consumer pattern)::

    AUTONOMIC_NERVOUS_SYSTEM_CHILDREN = ()
    # The autonomic_nervous_system is a leaf. The sympathetic and
    # parasympathetic branches and their target nuclei are prose,
    # not modules.

Reaching the central nucleus (recommended consumer pattern — the
SOURCE)::

    # The central nucleus is the SOURCE of the autonomic output —
    # the grey-matter fear-output structure:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #
    # The central nucleus INTEGRATES the fear signal; the
    # autonomic_nervous_system EXECUTES it.

Reaching the target structures (recommended consumer pattern — NOTE
the cross-container boundaries)::

    # The target structures of the autonomic pathways are under
    # DIENCEPHALON, MIDBRAIN, HINDBRAIN, and SPINAL CORD — not
    # under the amygdala:
    #
    #   diencephalon.hypothalamus
    #   midbrain.tegmentum.periaqueductal_gray
    #   hindbrain.metencephalon.pons.parabrachial_area
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.dorsal_motor_nucleus_vagus
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center...
    #   spinal_cord.gray_matter...intermediolateral_cell_column
    #
    # Do NOT resolve them through the autonomic_nervous_system.

Reaching the stria terminalis (recommended consumer pattern —
different output pathway)::

    # The stria terminalis is a DIFFERENT output pathway — the
    # amygdala → BNST / septal pathway:
    #
    #   subcortical.extended_amygdala.stria_terminalis
    #
    # The stria terminalis is the SLEA fear-anxiety pathway; the
    # autonomic_nervous_system is the autonomic effector system.

Reaching the SLEA components (recommended consumer pattern — NOTE
the autonomic_nervous_system is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # autonomic_nervous_system:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The autonomic_nervous_system is SLEA-FREE.

Pathway-level detail (not wired — consult references)::

    # The autonomic_nervous_system's pathways are prose, not
    # modules:
    #   central nucleus -> hypothalamus (PVN, lateral)
    #   central nucleus -> periaqueductal gray (PAG)
    #   central nucleus -> parabrachial nucleus
    #   central nucleus -> nucleus of the solitary tract (NTS)
    #   central nucleus -> dorsal motor nucleus of the vagus
    #   central nucleus -> rostral ventrolateral medulla (RVLM)
    #   central nucleus -> spinal intermediolateral cell column
    #
    # Do not attempt to resolve these as sub-paths of the
    # autonomic_nervous_system.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ans_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.amygdala.autonomic_nervous_system"
        )
        # resolve ans_path through the memory/recall layer

References
----------
*   **Canonical amygdala-autonomic anatomy:** LeDoux, J.E., Iwata,
    J., Cicchetti, P., Reis, D.J. (1988). "Different projections
    of the central amygdaloid nucleus mediate autonomic and
    behavioral correlates of conditioned fear." *Journal of
    Neuroscience* 8:2517–2529. (Definitive amygdala-autonomic
    pathways; central nucleus → hypothalamus, PAG, brainstem.)
*   **Amygdala-autonomic review:** Davis, M. (1992). "The role of
    the amygdala in fear and anxiety." *Annual Review of
    Neuroscience* 15:353–375. (Amygdala-autonomic pathways and
    fear responses.)
*   **Central nucleus autonomic efferents:** Veening, J.G.,
    Swanson, L.W., Sawchenko, P.E. (1984). "The organization of
    projections from the central nucleus of the amygdala to
    brainstem sites involved in central autonomic regulation: a
    combined retrograde transport-immunohistochemical study."
    *Brain Research* 303:337–357. (Central nucleus → brainstem
    autonomic nuclei.)
*   **PAG and defensive behavior:** Bandler, R., Shipley, M.T.
    (1994). "Columnar organization in the midbrain periaqueductal
    gray: modules for emotional expression?" *Trends in
    Neurosciences* 17:379–389. (PAG as the defensive behavior and
    autonomic coordination center.)
*   **Parabrachial nucleus:** Chamberlin, N.L., Saper, C.B. (1994).
    "Topographic organization of respiratory responses to
    glutamate microinjection in the parabrachial nucleus of the
    rat." *Journal of Neuroscience* 14:6500–6510. (Parabrachial
    nucleus and respiratory control.)
*   **NTS and RVLM:** Dampney, R.A.L. (1994). "Functional
    organization of central pathways regulating the
    cardiovascular system." *Physiological Reviews* 74:323–364.
    (NTS, RVLM, and cardiovascular control.)
*   **PTSD autonomic hyperarousal:** Pitman, R.K., et al. (2012).
    "Biological studies of post-traumatic stress disorder."
    *Nature Reviews Neuroscience* 13:769–787. (Autonomic
    hyperarousal in PTSD.)
*   **Panic disorder autonomic surge:** Gorman, J.M., et al.
    (2000). "Neuroanatomical hypothesis of panic disorder, revised."
    *American Journal of Psychiatry* 157:493–505. (Autonomic surge
    in panic disorder.)
*   **Stria terminalis (contrast — different output pathway):**
    Price, J.L., Russchen, F.T., Amaral, D.G. (1987). "The limbic
    region. II: The amygdaloid complex." In *Handbook of Chemical
    Neuroanatomy* (Björklund, A., Hökfelt, T., Swanson, L.W.,
    eds.). (Stria terminalis as the amygdala → BNST / septal
    pathway — distinct from the autonomic effector pathways.)
*   **SLEA (contrast — the autonomic_nervous_system is not
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral
    pallidum, nucleus accumbens; NOT the autonomic_nervous_system.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical
    pathway to the right amygdala mediating 'unseen' fear."
    *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association belongs to the **central nucleus** and
    **basolateral nuclei** — not to the right autonomic_nervous_system,
    which is SLEA-free and not a fear-output structure.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Amygdala-autonomic pathways in overview.)
*   NeuroNames — Autonomic nervous system (right); FMA — Autonomic
    nervous system (right member).
"""