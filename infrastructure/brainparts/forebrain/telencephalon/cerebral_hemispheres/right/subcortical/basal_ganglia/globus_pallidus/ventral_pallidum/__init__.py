"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
=====================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_ganglia
                    └── globus_pallidus
                        └── ventral_pallidum   <-- THIS MODULE

**Primary synonym:** Ventral pallidum (VP); ventral pallidum of the
globus pallidus; "the limbic pallidum"; subcommissural pallidum
(classical — partial).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**GABAergic output nucleus** — the **limbic/reward output** of the
ventral striatum, and part of the **ventral striatopallidal system**.
**Part of:** The **globus pallidus** container — specifically, the
**ventral** (limbic/reward) segment. Also part of the **ventral
striatopallidal system** (with the ventral striatum) and, in some
classifications, the **extended amygdala** (SLEA).
**Structural parent:** ``.../globus_pallidus/`` → **only wired
child** of the globus pallidus container.
**Structural children:** **None.** This is a **leaf** module. The
**subcommissural** and **sublenticular** parts of the ventral
pallidum, and the **cholinergic/GABAergic** neuronal populations, are
documented as **prose**, not as structural children.
**Boundary status (SLEA — FULL WARNING, completing the three-level
gradient):** **Boundary case — the ventral pallidum is part of the
sublenticular extended amygdala (SLEA) in some classifications, and
THIS is the module that carries the FULL amygdala-lateralization
warning.** The **basal ganglia container** *deferred* the warning; the
**globus pallidus container** carried it *lightly*; **this leaf**
carries it **fully** — because the ventral pallidum **itself** has
the SLEA relationship, and it is the **structure that actually
belongs to** the extended amygdala continuum (in the SLEA framing).
Consumers must **not** import **right-amygdala lateralization**
claims into the ventral pallidum — the ventral pallidum is **not**
the amygdala, **not** adjacent to the amygdala, and **not**
lateralized. The **full SLEA warning** applies here: the extended
amygdala continuum is **broadly bilateral** and **not lateralized**,
and the **right amygdala's fear association** belongs to the
**amygdala module** and to the **extended amygdala module**, **not**
to the ventral pallidum. See *Lateralization Notes*.
**Boundary status (embedded in the substantia innominata territory —
TOPOGRAPHIC, not structural):** **Boundary case — the ventral
pallidum is EMBEDDED in the SUBSTANTIA INNOMINATA's territory, but
the substantia innominata is a BASAL FOREBRAIN SIBLING, not a
parent.** The **ventral pallidum** lies **within** the **substantia
innominata**'s grey-matter territory (in the basal forebrain), and
the substantia innominata's cytoarchitecture **blends** into the
ventral pallidum laterally. But the tree wires them in **different
containers**:
*   **Ventral pallidum** — here, under
    ``.../basal_ganglia/globus_pallidus/`` (basal ganglia).
*   **Substantia innominata** —
    ``.../basal_forebrain/substantia_innominata/`` (basal forebrain).
The relationship is **topographic** (the ventral pallidum is
**embedded in** the substantia innominata's territory), **not**
**structural** (the substantia innominata is **not** a parent of the
ventral pallidum). Consumers must **not** resolve the ventral
pallidum as a substantia-innominata child, and must **not** expect
the substantia innominata module to contain the ventral pallidum.
**Boundary status (NOT the dorsal globus pallidus — the GPe/GPi are a
documented gap):** **Boundary case — the ventral pallidum is the
LIMBIC segment; the DORSAL segments (GPe, GPi) are the MOTOR segments
and are a DOCUMENTED GAP in the parent container.** The **globus
pallidus** classically has **three segments**: the **external** (GPe)
and **internal** (GPi) segments — which are **motor** — and the
**ventral pallidum** (VP) — which is **limbic/reward**. The tree
wires **only the ventral pallidum**; the **GPe** and **GPi** are
**not wired** (a **documented gap** in the parent `globus_pallidus`
module). Consumers that need the **motor** segments must resolve
their functions as **prose** in the **parent** `globus_pallidus`
module, not here. **This module is the LIMBIC segment** — it does
**not** carry the motor functions.
**Boundary status (NOT the ventral striatum — input/output siblings):**
**Boundary case — the ventral striatum (nucleus accumbens, olfactory
tubercle) is the INPUT structure; the ventral pallidum is the OUTPUT
structure.** The **ventral striatum** is under
``.../basal_ganglia/striatum/ventral_striatum/``; the **ventral
pallidum** is here, under ``.../globus_pallidus/``. They are
**siblings** in the **ventral striatopallidal system** — the ventral
striatum projects to the ventral pallidum, and the ventral pallidum
projects to the mediodorsal thalamus and the brainstem. Consumers
that need the **input** structure must resolve the **ventral
striatum**; consumers that need the **output** structure must resolve
**this module**.
**Boundary status (NOT the extended amygdala — SLEA classificatory
overlap, wired separately):** **Boundary case — the ventral pallidum
is part of the SLEA (sublenticular extended amygdala) in some
classifications, but the tree wires it under the basal ganglia, not
under the extended amygdala.** The **extended amygdala** container
(``.../extended_amygdala/``) includes the **BNST** and the **central
amygdaloid nucleus**; the **SLEA** classification **adds** the
**ventral pallidum** and parts of the **nucleus accumbens**. The
tree **splits** them — the ventral pallidum is here, under the basal
ganglia. This is a **deliberate boundary choice**. Consumers that
need the **extended amygdala** as a unit (per the SLEA
classification) must **union** ``.../extended_amygdala/`` with
``.../ventral_pallidum/`` and
``.../striatum/ventral_striatum/nucleus_accumbens/`` — the tree
does **not** provide this union as a single path.
**Boundary status (NOT the amygdala — despite the SLEA relationship):**
**Boundary case — the ventral pallidum is NOT the amygdala, NOT
adjacent to the amygdala, and NOT lateralized.** The **SLEA
classification** puts the ventral pallidum in the **extended
amygdala continuum**, but it does **not** make it an **amygdala
structure**. The **amygdala proper** is under
``.../medial_temporal_lobe/amygdala/`` — a **sibling** of the
subcortical container, not a relative of the ventral pallidum. The
ventral pallidum is a **ventral basal ganglia output**; the amygdala
is a **medial temporal lobe nuclear complex**. They are
**functionally coupled** (via the extended amygdala continuum, in the
SLEA framing) but **anatomically separate**. Consumers must **not**
import **right-amygdala fear-processing** claims into the ventral
pallidum.
**Boundary status (GABAergic output — NOT a neural processor in the
classical sense):** **Boundary case — the ventral pallidum is a
GABAergic output nucleus, not a neural processor.** It receives
**GABAergic** and **glutamatergic** input from the ventral striatum,
and it **projects GABAergic inhibition** to its targets (mediodorsal
thalamus, lateral habenula, brainstem). It **gates** reward-related
behavior rather than **computing** it. Consumers must not treat the
ventral pallidum as a cortical processor or a deep nucleus in the
classical sense — it is an **output relay**.

Overview
--------
The ventral pallidum is the **limbic/reward output** of the basal
ganglia — the **GABAergic** nucleus that receives input from the
**ventral striatum** (nucleus accumbens, olfactory tubercle) and
projects to the **mediodorsal thalamus**, the **lateral habenula**,
and the **brainstem**. It is the **ventral counterpart** to the
**dorsal globus pallidus** (GPe/GPi), which are the **motor output**
of the basal ganglia. Together with the **ventral striatum**, it forms
the **ventral striatopallidal system** — the **limbic/reward**
subsystem of the basal ganglia.

**The ventral pallidum is the "limbic globus pallidus."** The
**dorsal** globus pallidus (GPe/GPi) processes **motor** information;
the **ventral** pallidum processes **limbic/reward** information. The
two are **anatomically separate** (dorsal vs. ventral segments) and
**functionally distinct** (motor vs. limbic/reward). The tree wires
**only the ventral pallidum** — the dorsal segments are a
**documented gap** in the parent `globus_pallidus` module.

**The ventral pallidum is the structure that carries the FULL SLEA
warning.** This is the **third level** of the **three-level warning
gradient**:
*   **Basal ganglia container** — *deferred* the warning (the
    amygdala-adjacent structure is a **grandchild**).
*   **Globus pallidus container** — carried the warning *lightly*
    (the amygdala-adjacent structure is a **direct child**).
*   **Ventral pallidum** (this module) — carries the warning
    **fully** (the structure **itself** has the SLEA relationship).

The **full warning** is: the ventral pallidum is **not the amygdala**,
**not adjacent** to the amygdala, and **not lateralized**. It is part
of the **extended amygdala continuum** (SLEA) in some
classifications, but the continuum is **broadly bilateral**, and the
**right amygdala's fear-processing association** belongs to the
**amygdala module** and the **extended amygdala module**, **not** to
the ventral pallidum.

**The ventral pallidum is EMBEDDED in the substantia innominata
territory — a topographic relationship, not a structural one.** The
ventral pallidum lies **within** the **substantia innominata**'s
grey-matter territory (in the basal forebrain). But the tree wires
them in **different containers**:
*   **Ventral pallidum** — under the **basal ganglia**.
*   **Substantia innominata** — under the **basal forebrain**.

The relationship is **topographic**: the ventral pallidum is
**embedded in** the substantia innominata's territory. It is **not**
**structural**: the substantia innominata is **not** the parent of
the ventral pallidum, and the ventral pallidum is **not** a child of
the substantia innominata. Consumers must **not** resolve the ventral
pallidum through the substantia innominata, and must **not** expect
the substantia innominata module to contain the ventral pallidum.

**The ventral pallidum is a paired structure.** Each hemisphere has
its own ventral pallidum, projecting **ipsilaterally** to its own
mediodorsal thalamus and brainstem. The two are **bilaterally
symmetric** and **functionally non-lateralized** — reward, motivation,
and addiction are **bilateral functions**. **Ventral pallidum DBS**
for depression and OCD is **bilateral**. See *Lateralization Notes*.

Subdivisions (prose, not structural children)
---------------------------------------------
The ventral pallidum is classically divided into **two parts**, whose
boundaries are **topographic**:

*   **Subcommissural part** — the **anterior** part of the ventral
    pallidum, located **ventral to the anterior commissure**. It is
    the **classical** ventral pallidum — the region described by
    **Heimer and Wilson (1975)** as the **ventral pallidum** proper.
    Its **major output** is to the **mediodorsal thalamus** and the
    **lateral habenula**; it is the **primary reward output** of the
    ventral striatum.

*   **Sublenticular part** — the **posterior** part of the ventral
    pallidum, located **ventral to the lenticular nucleus** (the
    putamen + globus pallidus). It is **continuous** with the
    **sublenticular extended amygdala (SLEA)** — the region that
    gives the SLEA classification its name. It is the **part of the
    ventral pallidum** that **overlaps** with the extended amygdala
    continuum, and it is the **anatomic basis** of the **SLEA
    warning**.

**These two parts are prose, not structural children.** The tree
does **not** wire them as sub-modules. Consumers that need
subpart-level resolution should consult the references, not the tree.
The **subcommissural/sublenticular distinction** is **topographic**
— it depends on the **anterior commissure** and the **lenticular
nucleus** as landmarks — and the **SLEA warning** applies
**specifically to the sublenticular part**, not the subcommissural
part. Consumers must **not** treat the entire ventral pallidum as
"extended amygdala" — only the **sublenticular part** overlaps with
the SLEA continuum.

The Ventral Pallidum / Dorsal Globus Pallidus Gap
-------------------------------------------------
This is the **most consequential boundary** in the module, because
the **dorsal segments are a documented gap**:

*   **Ventral pallidum** (this module) — the **limbic/reward output**
    of the basal ganglia. **Wired** as the **only child** of the
    globus pallidus container.

*   **External globus pallidus (GPe)** and **Internal globus pallidus
    (GPi)** — the **motor output** of the basal ganglia. **NOT
    wired** — a **documented gap** in the parent `globus_pallidus`
    module. Their functions are documented as **prose** in the
    **parent**.

**The ventral pallidum does NOT carry the motor functions.** It is
the **limbic/reward output**; the **dorsal segments** are the
**motor output**. Consumers that need the **motor** functions must
resolve them as **prose** in the **parent** `globus_pallidus` module,
**not** here.

The Ventral Pallidum / Substantia Innominata Boundary
-----------------------------------------------------
This is the **most commonly confused** boundary for consumers:

*   **Ventral pallidum** (this module) — the **limbic/reward output**
    of the basal ganglia. **Basal ganglia** structure — **GABAergic
    output nucleus**.

*   **Substantia innominata** —
    ``.../basal_forebrain/substantia_innominata/`` — the **grey-matter
    region** of the **basal forebrain** that **contains** the nucleus
    basalis and the magnocellular preoptic nucleus. **Basal
    forebrain** structure — **heterogeneous grey-matter region**.

**The relationship is TOPOGRAPHIC, not STRUCTURAL.** The ventral
pallidum is **embedded in** the substantia innominata's territory —
its cell bodies lie **within** the substantia innominata's
grey-matter region. But the tree wires them in **different
containers**, and the relationship is **not** parent/child.
Consumers must **not** resolve the ventral pallidum through the
substantia innominata, and must **not** expect the substantia
innominata module to contain the ventral pallidum.

The Ventral Pallidum / Ventral Striatum Boundary
------------------------------------------------
This is the **input-output** boundary of the **ventral
striatopallidal system**:

*   **Ventral striatum** —
    ``.../basal_ganglia/striatum/ventral_striatum/`` — the **input**
    structure (nucleus accumbens, olfactory tubercle). **Sibling**.

*   **Ventral pallidum** (this module) — the **output** structure.
    **Sibling**.

**They are siblings under the basal ganglia container.** The
**ventral striatopallidal circuit** connects them: the **ventral
striatum** is the **first** relay (limbic input), and the **ventral
pallidum** is the **second** relay (limbic output). Consumers that
need the **input** structure must resolve the **ventral striatum**;
consumers that need the **output** structure must resolve **this
module**.

The Ventral Pallidum / Extended Amygdala Boundary
-------------------------------------------------
This is the **SLEA** boundary — the **full warning**:

*   **Extended amygdala** (``.../extended_amygdala/``) — the **BNST**
    and the **central amygdaloid nucleus**. **Classically** the
    extended amygdala; **SLEA** adds the **ventral pallidum** and
    parts of the **nucleus accumbens**.

*   **Ventral pallidum** (this module) — the **sublenticular part**
    (the **posterior** part) is part of the **SLEA** classification.

**The tree splits them.** The ventral pallidum is under
``.../globus_pallidus/ventral_pallidum/``, and the **nucleus
accumbens** is under ``.../striatum/ventral_striatum/nucleus_accumbens/``
— **not** under the extended amygdala. This is a **deliberate
boundary choice**. Consumers that need the **extended amygdala** as a
unit (per the SLEA classification) must **union**
``.../extended_amygdala/`` with the **ventral pallidum** and **nucleus
accumbens** — the tree does **not** provide this union as a single
path.

**This module carries the FULL SLEA warning.** It is the **third
level** of the three-level warning gradient — the **structure that
actually has** the SLEA relationship. The warning is **full**:
- The **subcommissural part** — **not** part of the SLEA continuum.
  Only the **sublenticular part** is.
- The **sublenticular part** — **part** of the SLEA continuum in
  some classifications, but the **tree denies** the grouping.
- The **ventral pallidum itself** — **not the amygdala**, **not
  adjacent**, **not lateralized**.
- The **right-amygdala fear association** — belongs to the
  **amygdala module** and the **extended amygdala module**, **not**
  here.

The Ventral Pallidum / Substantia Nigra Boundary
------------------------------------------------
This is the **dopaminergic** boundary:

*   **Substantia nigra** —
    ``.../midbrain/tegmentum/substantia_nigra/`` — the **dopaminergic**
    (pars compacta) and **GABAergic** (pars reticulata) **midbrain**
    nucleus. Its **pars compacta** provides **dopaminergic input to
    the ventral striatum** (the **mesolimbic pathway**, via the
    **VTA** — see next boundary); its **pars reticulata** is a
    **GABAergic output** comparable to the **dorsal pallidum** (GPi),
    not the ventral pallidum. **Functionally related** to the basal
    ganglia but **structurally separate** (midbrain).

*   **Ventral pallidum** (this module) — the **GABAergic output** of
    the **ventral striatopallidal system**. **Telencephalic**.

**The substantia nigra is NOT a ventral pallidum child.** It is a
**midbrain** structure — functionally related (dopaminergic input to
the ventral striatum, which then projects to the ventral pallidum)
but structurally separate. Consumers must not resolve the substantia
nigra through the ventral pallidum.

The Ventral Pallidum / VTA Boundary
-----------------------------------
This is the **mesolimbic** boundary:

*   **Ventral tegmental area (VTA)** —
    ``.../midbrain/tegmentum/ventral_tegmental_area/`` — the
    **dopaminergic** midbrain nucleus that projects to the **ventral
    striatum** (nucleus accumbens) — the **mesolimbic pathway**.
    **Functionally related** to the **ventral striatopallidal
    system** (VTA → ventral striatum → ventral pallidum), but
    **structurally separate** (midbrain).

*   **Ventral pallidum** (this module) — the **GABAergic output** of
    the **ventral striatopallidal system**. **Telencephalic**.

**The VTA is the upstream dopaminergic input** to the ventral
striatopallidal system. Consumers must **not** resolve the VTA
through the ventral pallidum, and must **not** treat the VTA as
intrinsic to the ventral pallidum. The **mesolimbic pathway** (VTA →
ventral striatum → ventral pallidum) is a **functional circuit**
across three **structurally separate** regions.

Function in the Human Brain
---------------------------
The ventral pallidum's functions are **reward, motivation, and
gating of reward-related behavior**:

*   **Reward and Motivation (Primary Function):** The **ventral
    pallidum** is the **limbic/reward output** of the ventral
    striatum. It receives **GABAergic** and **glutamatergic** input
    from the **nucleus accumbens** and the **olfactory tubercle**,
    and it projects **GABAergic inhibition** to the **mediodorsal
    thalamus**, the **lateral habenula**, and the **brainstem**. Its
    **GABAergic output** is a **gating signal** for **reward-seeking
    behavior** — it **inhibits** the mediodorsal thalamus when the
    ventral striatum **does not select** a reward, and it
    **disinhibits** the thalamus when the ventral striatum **selects**
    a reward. **Lesions** impair **reward-seeking** and
    **motivation**.

*   **Hedonic "Liking" (Ventral Pallidum Function):** The ventral
    pallidum is part of the **hedonic hotspot** circuit (with the
    nucleus accumbens shell) — it is involved in the **"liking"**
    component of reward (the **pleasure** of a reward, as opposed to
    the **"wanting"** component driven by dopamine). **Opioid**
    stimulation of the ventral pallidum **enhances liking** in
    animal models.

*   **Gating of Reward-Related Behavior (Modulatory Function):** The
    ventral pallidum's **GABAergic output** is a **gating signal**
    — it **permits or inhibits** reward-seeking actions. Its
    **disinhibition** of the mediodorsal thalamus **invigorates**
    reward-seeking; its **inhibition** **suppresses** it. This is
    the **ventral pallidum's core output function**.

*   **Addiction (Ventral Pallidum Function):** The ventral pallidum
    is a **key node** in the **addiction circuit** (with the VTA,
    nucleus accumbens, and prefrontal cortex). Its **dysfunction**
    contributes to **craving**, **relapse**, and **compulsive
    drug-seeking**. **Ventral pallidum DBS** is an **experimental
    treatment** for **treatment-resistant addiction**.

*   **Depression (Ventral Pallidum Function):** The ventral pallidum
    is **overactive** in **depression** in some models. **Ventral
    pallidum DBS** has been investigated for
    **treatment-resistant depression** — results are **mixed**, but
    the target is **clinically relevant**.

*   **OCD (Ventral Pallidum Function):** The ventral pallidum is
    part of the **OCD circuit** (with the ventral striatum and
    orbitofrontal cortex). **Ventral pallidum DBS** is an
    **experimental treatment** for **treatment-resistant OCD**.

*   **Extended Amygdala Continuity (Contested — SLEA
    Classification):** The **sublenticular part** of the ventral
    pallidum is part of the **SLEA** in some classifications, giving
    it a role in **stress, anxiety, and reward** — but the tree
    **splits** it from the extended amygdala, and the SLEA
    classification is **contested**. **This is the full SLEA
    warning** — the ventral pallidum is **not the amygdala**, **not
    adjacent**, and **not lateralized**.

*   **NOT a neural processor in the classical sense.** The ventral
    pallidum is a **GABAergic output** — it **inhibits** its targets
    and **gates** reward-related behavior. It does **not** compute
    reward value or emotional salience; it **relays** the output of
    the ventral striatum to the thalamus and brainstem. Consumers
    must not treat the ventral pallidum as a cortical processor or a
    deep nucleus in the classical sense.

**The unifying theme:** the ventral pallidum is the **limbic/reward
output** of the basal ganglia — a **GABAergic gating nucleus** that
**relays** the ventral striatum's reward signal to the mediodorsal
thalamus, the lateral habenula, and the brainstem. It is **not** the
dorsal (motor) globus pallidus, **not** the substantia innominata
(though it is **embedded in** its territory), **not** the amygdala
(despite the SLEA classification), and **not** a neural processor.

Associated Disorders
--------------------
Ventral pallidum disorders are **reward, motivation, and limbic**:

*   **Addiction — Craving and Relapse (Signature Disorder):**
    The ventral pallidum is a **key node** in the **addiction
    circuit**. Its **dysfunction** contributes to **craving**,
    **relapse**, and **compulsive drug-seeking**. **Ventral pallidum
    DBS** has been investigated as an **experimental treatment** for
    **treatment-resistant addiction** (Malone et al., 2009).

*   **Treatment-Resistant Depression — Ventral Pallidum DBS:**
    **Deep brain stimulation** of the ventral pallidum (often
    targeted via the **ventral capsule/ventral striatum**, which
    includes the ventral pallidum) has been investigated for
    **treatment-resistant depression**. Results are **mixed**, but
    the target is **clinically relevant** (Malone et al., 2009).

*   **Obsessive-Compulsive Disorder — Ventral Pallidum DBS:**
    **Deep brain stimulation** of the ventral pallidum (via the
    **ventral internal capsule/ventral striatum** target) is an
    **FDA-approved** (under **Humanitarian Device Exemption**)
    treatment for **treatment-resistant OCD** (Greenberg et al.,
    2010).

*   **Motivation Deficits (Apathy):** **Ventral pallidum lesions**
    in animal models impair **motivation** and **reward-seeking** —
    they reduce **effort** for reward. In humans, ventral pallidum
    dysfunction may contribute to **apathy** in
    **neurodegenerative disease** (e.g., Parkinson's, Alzheimer's).

*   **Anhedonia (Contested):** The ventral pallidum's role in
    **hedonic "liking"** suggests a role in **anhedonia** — the
    **loss of pleasure** in **depression** — but the evidence is
    **preclinical** and **contested** in humans.

*   **Sublenticular Extended Amygdala Pathology (Contested — SLEA
    Classification):** If the **SLEA classification** is accepted,
    the **sublenticular part** of the ventral pallidum would be
    implicated in **stress, anxiety, and addiction** — but the tree
    **denies** the grouping, and the evidence is **contested**.

**What is NOT here:** The ventral pallidum is **not** the substrate
for **Parkinson's disease** (substantia nigra), **Huntington's
disease** (dorsal striatum), **dystonia** (GPi), **Kluver-Bucy
syndrome** (amygdala), or **temporal lobe epilepsy** (hippocampus).
Its clinical footprint is **reward/motivation** (addiction,
depression, OCD, apathy) and **contested** (anhedonia, SLEA
pathology) — a **distinct category** from the **dorsal** globus
pallidus's **motor** footprint.

Lateralization Notes
--------------------
This is the **right** ventral pallidum module. The ventral pallidum is
**bilaterally symmetric** and **functionally non-lateralized**:

*   **Bilateral Limbic/Reward Output:** Each ventral pallidum
    projects **ipsilaterally** to its own mediodorsal thalamus and
    brainstem. The two sides are **functionally symmetric** for
    reward, motivation, and gating. **Ventral pallidum DBS** is
    **bilateral**.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the ventral pallidum has **no documented strong
    left-lateralized or right-lateralized function**. **Addiction**,
    **depression**, and **OCD** are **bilateral** in the ventral
    pallidum.

*   **FULL SLEA WARNING (the third level of the three-level
    gradient):** The ventral pallidum **itself** has the **SLEA
    relationship** (via its sublenticular part) — **this is the
    structure that carries the full warning**, completing the
    three-level gradient from the basal ganglia container (deferred)
    to the globus pallidus container (light) to **this module**
    (full). The warning is:
    - The ventral pallidum is **not the amygdala**.
    - It is **not adjacent** to the amygdala.
    - It is **not lateralized**.
    - The **SLEA continuum** is **broadly bilateral**.
    - The **right amygdala's fear-processing association** belongs
      to the **amygdala module** and the **extended amygdala
      module** — **not** to the ventral pallidum.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (via SLEA) to the **extended amygdala
    module** — **not** to the ventral pallidum, **not** to the
    globus pallidus, and **not** to the basal ganglia. **This is the
    most important right-side warning in the entire basal ganglia
    subtree**: the **right ventral pallidum** is the structure
    **itself** that carries the SLEA relationship, and a consumer
    reading the right-side module is **exactly** the consumer most
    likely to attribute the right amygdala's fear-processing
    association to the right ventral pallidum. **Do not.** The right
    ventral pallidum is **not** the right extended amygdala, and the
    right amygdala's fear-processing association **does not**
    transfer here.

**A consumer that assumes "right ventral pallidum = left ventral
pallidum" will be structurally and functionally correct** — the two
sides are symmetric, no lateralized function has been demonstrated,
and the **FULL SLEA warning** is stated here at the leaf level. This
is a **strict-mirror pair with a light-moderate warning** — matching
the **nucleus basalis** and **substantia innominata** pattern (light
warning: Lateralization note + light Usage warning, **not** the
emphatic "Do not import" Usage block of the periamygdaloid/uncus/
subcortical group). The warning is **full** in the sense of being
**the complete SLEA statement at the leaf level**, but it is
**light-moderate** in strength — the ventral pallidum is **not
adjacent** to the amygdala, and the SLEA link is **classificatory**,
not **projectional** or **adjacent**. **The right-side module
carries the FULL SLEA warning explicitly** — matching the pattern of
the right nucleus basalis and right substantia innominata — because
the SLEA classification links the ventral pallidum to the extended
amygdala, and the right-amygdala fear association is the claim a
right-side reader is most likely to import.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../extended_amygdala/``, ``.../midbrain/``, or any other
    container. The ventral pallidum's relationships to the extended
    amygdala (SLEA), substantia nigra, VTA, and substantia innominata
    are documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **subcommissural**
    and **sublenticular** parts of the ventral pallidum, and the
    **cholinergic/GABAergic** neuronal populations, are documented as
    **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve subpart-level detail through the
    references.
*   **FULL SLEA WARNING — completing the three-level gradient.** The
    **basal ganglia container** *deferred* the warning; the **globus
    pallidus container** carried it *lightly*; **this module**
    carries it **fully**. The ventral pallidum is **not the
    amygdala**, **not adjacent** to it, and **not lateralized**. The
    **right-amygdala fear association** belongs to the **amygdala
    module** and the **extended amygdala module**, **not** here.
    **The right-side module carries the full SLEA warning
    explicitly** — a dedicated "Do not import" Usage block and a
    contrast reference — matching the right nucleus basalis and right
    substantia innominata pattern.
*   **NOT the dorsal globus pallidus.** The **GPe/GPi** are the
    **motor** segments and are a **documented gap** in the parent
    `globus_pallidus` module. **This module is the LIMBIC segment** —
    it does **not** carry the motor functions.
*   **Embedded in the substantia innominata territory — TOPOGRAPHIC,
    not structural.** The ventral pallidum lies **within** the
    substantia innominata's grey-matter region, but the substantia
    innominata is a **basal forebrain sibling**, not a parent. Do not
    resolve the ventral pallidum as a substantia-innominata child.
*   **Not the ventral striatum — sibling.** The ventral striatum is
    the **input** structure; the ventral pallidum is the **output**
    structure. They are **siblings** in the ventral striatopallidal
    system.
*   **Not the amygdala — despite the SLEA classification.** The SLEA
    link is **classificatory**, not **anatomical adjacency**. Do not
    import amygdala-lateralization claims. **The right-side module
    carries the full SLEA warning explicitly** — matching the right
    nucleus basalis and right substantia innominata pattern.
*   **Not the substantia nigra or VTA — midbrain inputs.** The
    substantia nigra and VTA are **midbrain** structures that provide
    dopaminergic input to the **ventral striatum** (upstream of the
    ventral pallidum), not to the ventral pallidum directly. Do not
    resolve them through the ventral pallidum.
*   **GABAergic output — not a neural processor.** The ventral
    pallidum is a **GABAergic output** that **gates** reward-related
    behavior; it does not **compute** reward value.
*   **No ``AREA_PATHS`` hop.** The ventral pallidum is a local leaf
    under the globus pallidus, not a cross-listed leaf.
*   **No nested cross-listing.** The ventral pallidum has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with left ventral pallidum — strict mirror
    with a full (light-moderate) warning.** Right and left ventral
    pallidum modules are **structurally identical** — same leaf
    status, same subparts documented as prose, same SLEA warning
    (full at the leaf level), same substantia-innominata topographic
    note, same ventral-striatum sibling note, same non-lateralized
    caveat. **The right-side module carries the full SLEA warning
    explicitly** — a dedicated "Do not import" Usage block and a
    contrast reference — matching the right nucleus basalis and right
    substantia innominata pattern.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.globus_pallidus import ventral_pallidum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_ganglia.globus_pallidus.ventral_pallidum"
    )

**Do not** assume the ventral pallidum is the **dorsal globus
pallidus** (GPe/GPi). The dorsal segments are the **motor** output
and are a **documented gap** in the parent `globus_pallidus` module.
The ventral pallidum is the **limbic/reward** output — the **only
wired child**.

**Do not** assume the ventral pallidum is a **child of the
substantia innominata**. It is **embedded in** the substantia
innominata's territory (topographic), but the substantia innominata
is a **basal forebrain sibling**, not a parent.

**Do not** assume the ventral pallidum is the **ventral striatum**.
The ventral striatum is the **input** structure; the ventral pallidum
is the **output** structure. They are **siblings**.

**Do not** assume the ventral pallidum is the **amygdala**. The SLEA
classification links them in some literature, but the ventral pallidum
is **not the amygdala**, **not adjacent** to it, and **not
lateralized**.

**Do not** import **right-amygdala lateralization claims** into the
right ventral pallidum. The **right amygdala's fear association**
belongs to the **amygdala module** and the **extended amygdala
module** — **not** here. **This is the FULL SLEA warning** — the
third level of the three-level gradient (basal ganglia → globus
pallidus → ventral pallidum). **This is the most important
right-side warning in the entire basal ganglia subtree** — the
right ventral pallidum is the structure **itself** that carries the
SLEA relationship, and a consumer reading the right-side module is
**exactly** the consumer most likely to attribute the right
amygdala's fear-processing association to the right ventral pallidum.
**Do not.** The right ventral pallidum is **not** the right extended
amygdala.

**Do not** assume the ventral pallidum is a **neural processor**. It
is a **GABAergic output** that **gates** reward-related behavior.

**Do not** assume the ventral pallidum is the **substantia nigra** or
the **VTA**. Those are **midbrain** structures that provide
dopaminergic input to the **ventral striatum** (upstream), not to the
ventral pallidum directly.

Iterating the ventral pallidum's (empty) children (recommended
consumer pattern)::

    VP_CHILDREN = ()
    # The ventral pallidum is a leaf. Subcommissural/sublenticular
    # parts and cholinergic/GABAergic populations are prose, not
    # modules.

Reaching the dorsal globus pallidus functions (recommended consumer
pattern — note the GAP)::

    # The external globus pallidus (GPe) and internal globus pallidus
    # (GPi) are NOT in the tree. Their functions (motor output,
    # pallidotomy/DBS targets) are documented as PROSE in the PARENT
    # `globus_pallidus` module, NOT here.
    #
    # Resolve:
    #
    #   subcortical.basal_ganglia.globus_pallidus
    #     -> parent module's "Dorsal Segment Gap" section
    #
    # Do NOT attempt to resolve a "gpe" or "gpi" path.

Reaching the substantia innominata (recommended consumer pattern —
note the TOPOGRAPHIC, not structural, relationship)::

    # The substantia innominata is a BASAL FOREBRAIN SIBLING, not a
    # parent of the ventral pallidum. The ventral pallidum is
    # EMBEDDED in the substantia innominata's territory, but they are
    # in different containers:
    #
    #   subcortical.basal_forebrain.substantia_innominata
    #
    # The relationship is TOPOGRAPHIC, not STRUCTURAL.

Reaching the extended amygdala's SLEA components (recommended
consumer pattern — the SLEA union)::

    # The extended amygdala's SLEA classification includes the
    # ventral pallidum (sublenticular part) and parts of the nucleus
    # accumbens. The tree splits them. Consumers that need the SLEA
    # grouping must union:
    #
    #   subcortical.extended_amygdala
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The tree does not provide this union as a single path.

Reaching the ventral striatum (recommended consumer pattern)::

    # The ventral striatum is a SIBLING of the ventral pallidum —
    # the INPUT structure of the ventral striatopallidal system:
    #
    #   subcortical.basal_ganglia.striatum.ventral_striatum
    #
    # The nucleus accumbens and olfactory tubercle are its children.

Reaching the VTA and substantia nigra (recommended consumer
pattern — NOTE the midbrain boundary)::

    # The VTA and substantia nigra are MIDBRAIN structures that
    # provide dopaminergic input to the VENTRAL STRIATUM (upstream of
    # the ventral pallidum), not to the ventral pallidum directly:
    #
    #   midbrain.tegmentum.ventral_tegmental_area
    #   midbrain.tegmentum.substantia_nigra
    #
    # Do NOT resolve them through the ventral pallidum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        vp_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.globus_pallidus.ventral_pallidum"
        )
        # resolve vp_path through the memory/recall layer

References
----------
*   **Canonical ventral pallidum anatomy:** Heimer, L., Wilson, R.D.
    (1975). "The subcortical projections of the allocortex:
    similarities in the neural associations of the hippocampus, the
    piriform cortex, and the neocortex." In *Golgi Centennial
    Symposium* (Santini, M., ed.). (Original description of the
    ventral pallidum; ventral striatopallidal system.)
*   **Ventral pallidum reward:** Smith, K.S., Tindell, A.J., Aldridge,
    J.W., Berridge, K.C. (2009). "Ventral pallidum roles in reward
    and motivation." *Behavioural Brain Research* 196:155–167.
    (Definitive review; reward, motivation, hedonic "liking".)
*   **Hedonic hotspot:** Berridge, K.C., Kringelbach, M.L. (2015).
    "Pleasure systems in the brain." *Neuron* 86:646–664. (Ventral
    pallidum in the hedonic hotspot; opioid stimulation enhances
    liking.)
*   **Ventral pallidum extended amygdala / SLEA:** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA; ventral pallidum in
    the extended amygdala continuum.)
*   **Ventral pallidum DBS for depression:** Malone, D.A., et al.
    (2009). "Deep brain stimulation of the ventral capsule/ventral
    striatum for treatment-resistant depression." *Biological
    Psychiatry* 65:267–275. (Ventral pallidum DBS for depression.)
*   **Ventral pallidum DBS for OCD:** Greenberg, B.D., et al. (2010).
    "Deep brain stimulation of the ventral internal capsule/ventral
    striatum for obsessive-compulsive disorder." *Molecular
    Psychiatry* 15:64–79. (Ventral pallidum DBS for OCD; FDA HDE
    approval.)
*   **Ventral pallidum and addiction:** Koob, G.F., Volkow, N.D.
    (2010). "Neurocircuitry of addiction." *Neuropsychopharmacology*
    35:217–238. (Ventral pallidum in the addiction circuit.)
*   **Ventral pallidum and motivation:** Mogenson, G.J., Jones, D.L.,
    Yim, C.Y. (1980). "From motivation to action: functional
    interface between the limbic system and the motor system."
    *Progress in Neurobiology* 14:69–97. (Ventral pallidum as the
    limbic-motor interface; motivation.)
*   **Substantia innominata (contrast — topographic embedding):**
    Heimer, L., de Olmos, J., Alheid, G.F., Záborszky, L. (1999).
    "The human basal forebrain: an overview." In *The Human Nervous
    System* (Paxinos, G., ed.), 2nd ed. (Ventral pallidum embedded in
    the substantia innominata's territory; topographic, not
    structural, relationship.)
*   **Dorsal globus pallidus (contrast — documented gap):** DeLong,
    M.R., Wichmann, T. (2007). "Circuits and circuit disorders of the
    basal ganglia." *Archives of Neurology* 64:20–24. (GPe/GPi motor
    output; the dorsal segments are the motor counterpart to the
    ventral pallidum.)
*   **Substantia nigra and VTA (contrast — midbrain inputs):** Braak,
    H., et al. (2003). "Staging of brain pathology related to
    sporadic Parkinson's disease." *Neurobiology of Aging*
    24:197–211. (Substantia nigra and VTA as midbrain structures
    providing dopaminergic input to the ventral striatum; upstream of
    the ventral pallidum.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the right ventral pallidum —
    the SLEA classification is classificatory, not lateralized, and
    the right amygdala's fear association belongs to the **amygdala
    module** and the **extended amygdala module**.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Ventral pallidum in overview.)
*   NeuroNames — Ventral pallidum (right); FMA — Ventral pallidum
    (right member).
"""