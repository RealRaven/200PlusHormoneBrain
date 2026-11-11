"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain.substantia_innominata
=============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_forebrain
                    └── substantia_innominata   <-- THIS MODULE

**Primary synonym:** Substantia innominata; substantia innominata of
Reichert (classical — see *Boundary status*); "the unnamed substance."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**grey-matter region** — not a single nucleus — between the **globus
pallidus** and the **anterior perforated substance**. Its boundaries
are **cytoarchitecturally graded**, not sharp.
**Part of:** The **basal forebrain** container — specifically, the
**ventral grey-matter region** of the basal forebrain. It **contains**
the **nucleus basalis of Meynert** (a **sibling**, not a child) and
the **magnocellular preoptic nucleus** (**not wired in the tree**),
plus **scattered cholinergic and GABAergic neurons**.
**Structural parent:** ``.../right/subcortical/basal_forebrain/`` →
**direct child** of the basal forebrain container.
**Structural children:** **None.** This is a **leaf** module. The
**nucleus basalis** and the **magnocellular preoptic nucleus** are
**embedded within** the substantia innominata's territory, but they
are **siblings** (or unwired), not children. See *The Substantia
Innominata / Nucleus Basalis Boundary* and *The Substantia Innominata
/ Magnocellular Preoptic Nucleus Gap*.
**Boundary status (REGION, not a nucleus):** **Boundary case — a
graded grey-matter region, not a single cytoarchitecturally defined
nucleus.** The substantia innominata is **not** a single nucleus
(like the nucleus basalis) and **not** a single tract (like the
fornix). It is a **region** whose boundaries are **graded**:
*   **Laterally**, it blends into the **globus pallidus**.
*   **Anteriorly**, it blends into the **anterior perforated
    substance** and the **diagonal band**.
*   **Posteriorly**, it blends into the **preoptic area** and the
    **lateral hypothalamus**.
*   **Dorsally**, it abuts the **internal capsule** and the
    **striatum**.
The **cytoarchitectonic boundaries** are **not sharp**, which is
**why it was named "unnamed"** — 19th-century anatomists could not
sharply define it. Consumers must not expect a clean boundary;
"substantia innominata" is a **region of the basal forebrain**, not a
discrete nucleus.
**Boundary status (NOT the nucleus basalis — sibling, not child):**
**Boundary case — the nucleus basalis of Meynert is EMBEDDED in the
substantia innominata, but it is a SIBLING, not a child.** The
**nucleus basalis** — the **cortically projecting cholinergic
nucleus** — lies **within** the substantia innominata's grey-matter
territory. But the tree wires **both as siblings** under the basal
forebrain:
*   ``.../basal_forebrain/nucleus_basalis/``
*   ``.../basal_forebrain/substantia_innominata/``
The nucleus basalis is **not** a child of the substantia innominata,
and the substantia innominata is **not** a container for it.
Consumers that need the **cholinergic nucleus** must resolve it at
its own path; consumers that need the **grey-matter region** must
resolve it here. They are **anatomically overlapping** but
**structurally separate**.
**Boundary status (NOT the extended amygdala — classificatory
overlap, but wired separately):** **Boundary case — the substantia
innominata is sometimes classified as part of the extended amygdala
(via the sublenticular extended amygdala, SLEA), but the tree wires
them separately.** Classical and modern literature describes the
**sublenticular extended amygdala (SLEA)** — a continuum that
includes the **substantia innominata**, the **bed nucleus of the
stria terminalis (BNST)**, and the **central amygdaloid nucleus**.
The tree **denies this grouping**: it wires
``.../extended_amygdala/`` as a **sibling** of ``.../basal_forebrain/``,
and it wires the **substantia innominata** under the **basal
forebrain**, not the extended amygdala. This is a **deliberate
boundary choice** — the tree treats the substantia innominata as a
**basal forebrain grey-matter region**, not as an extended-amygdala
component. Consumers that need the **extended amygdala** as a unit
must **union** ``.../extended_amygdala/`` with the **substantia
innominata** (among other structures). See *The Substantia Innominata
/ Extended Amygdala Boundary*.
**Boundary status (NOT the substantia nigra — name confusion):**
**Boundary case — "substantia innominata" and "substantia nigra" are
NOT the same structure.** The names are **similar** (both begin with
"substantia"), but:
*   **Substantia innominata** (this module) — **ventral basal
    forebrain**, **telencephalic**, grey-matter **region** containing
    the nucleus basalis.
*   **Substantia nigra** — **midbrain**, **mesencephalic**, pigmented
    **nucleus** (pars compacta + pars reticulata), dopaminergic
    (pars compacta) and GABAergic (pars reticulata).
They are **anatomically and functionally unrelated**. The
**substantia nigra** is under ``.../midbrain/tegmentum/substantia_nigra/``
— **not** here. Consumers must not conflate them. See *The Substantia
Innominata / Substantia Nigra Boundary*.
**Boundary status (NOT the globus pallidus — adjacent, but a basal
ganglia sibling):** **Boundary case — the globus pallidus is
ADJACENT to the substantia innominata, but it is a BASAL GANGLIA
child, not a basal forebrain child.** The **globus pallidus** lies
**medial and lateral** to the substantia innominata; its **ventral
pallidum** extends into the substantia innominata's territory. The
tree wires the **globus pallidus** under ``.../basal_ganglia/`` —
**not** under the basal forebrain. Consumers that need the globus
pallidus must resolve it through the **basal ganglia container**,
not through the substantia innominata.
**Boundary status (NOT the anterior perforated substance — adjacent,
but a sibling):** **Boundary case — the anterior perforated
substance is ADJACENT to the substantia innominata, but it is a
SIBLING under the basal forebrain.** The **anterior perforated
substance (APS)** lies **anterior** to the substantia innominata;
the substantia innominata **blends into** the APS territory. The
tree wires them as **siblings**:
*   ``.../basal_forebrain/anterior_perforated_substance/``
*   ``.../basal_forebrain/substantia_innominata/``
Consumers must not resolve the APS through the substantia innominata,
or vice versa.

Overview
--------
The substantia innominata — **"the unnamed substance"** — is a
**heterogeneous grey-matter region** of the **ventral basal
forebrain**, located **between the globus pallidus** (laterally and
medially) and the **anterior perforated substance** (anteriorly),
**below the striatum** and the **internal capsule**, and **above the
ventral surface** of the brain. It is the **structural home** of the
**nucleus basalis of Meynert** (the cortical cholinergic nucleus), the
**magnocellular preoptic nucleus** (**not wired**), and **scattered
cholinergic and GABAergic neurons** — plus it is a **transitional
region** between the **basal ganglia** and the **basal forebrain**.

**The name is a historical placeholder.** "Substantia innominata"
literally means "**unnamed substance**" in Latin — 19th-century
anatomists (including **Reichert**, who named it the *substantia
innominata of Reichert*) gave it this placeholder because they could
**not** sharply define its boundaries. It was a **region left over**
after named structures (globus pallidus, striatum, anterior perforated
substance) were subtracted from the ventral basal forebrain. The name
has **stuck** — modern anatomy still uses it — but it remains a
**region**, not a nucleus.

**The substantia innominata's boundaries are graded, not sharp.**
This is its **defining structural feature**:
*   **Laterally**, it **blends** into the **globus pallidus**
    (especially the **ventral pallidum**).
*   **Anteriorly**, it **blends** into the **anterior perforated
    substance** and the **diagonal band of Broca**.
*   **Posteriorly**, it **blends** into the **preoptic area** and the
    **lateral hypothalamus**.
*   **Dorsally**, it **abuts** the **internal capsule** and the
    **striatum**.
The **cytoarchitecture** is **heterogeneous** — cholinergic neurons,
GABAergic neurons, peptidergic neurons, and glia, **intermingled**
with fibers of passage (internal capsule, ansa lenticularis,
lenticular fasciculus). Consumers must **not** expect a clean
boundary — "substantia innominata" is a **region of the basal
forebrain**, not a discrete nucleus.

**The substantia innominata CONTAINS the nucleus basalis, but is
NOT its parent.** This is the module's **most important boundary
fact**. The **nucleus basalis of Meynert** — the **cortically
projecting cholinergic nucleus** — lies **within** the substantia
innominata's grey-matter territory. But the tree wires them as
**siblings** under the basal forebrain, not as parent and child.
Consumers that need the **cholinergic nucleus** must resolve
``.../basal_forebrain/nucleus_basalis/``; consumers that need the
**grey-matter region** must resolve this module. They are
**anatomically overlapping** but **structurally separate**.

**The substantia innominata is sometimes classified as part of the
extended amygdala, but the tree wires them separately.** The
**sublenticular extended amygdala (SLEA)** — a continuum including the
substantia innominata, the **BNST**, and the **central amygdaloid
nucleus** — is a **real anatomical classification**. But the tree
**denies it** by wiring ``.../extended_amygdala/`` as a **sibling** of
``.../basal_forebrain/``, and by wiring the substantia innominata under
the basal forebrain. This is a **deliberate boundary choice** — the
tree treats the substantia innominata as a **basal forebrain
grey-matter region**, not as an extended-amygdala component. Consumers
that need the **extended amygdala** as a unit must **union**
``.../extended_amygdala/`` with the substantia innominata (among
others). See *The Substantia Innominata / Extended Amygdala Boundary*.

**The substantia innominata is NOT the substantia nigra.** The names
are similar ("substantia" in both), but they are **anatomically and
functionally unrelated**:
*   **Substantia innominata** (this module) — **telencephalic**,
    **ventral basal forebrain**, grey-matter **region**, contains the
    nucleus basalis.
*   **Substantia nigra** — **mesencephalic**, **midbrain**,
    pigmented **nucleus**, dopaminergic (pars compacta) and GABAergic
    (pars reticulata).

The substantia nigra is under ``.../midbrain/tegmentum/substantia_nigra/``
— **not** here. Consumers must not conflate them. See *The Substantia
Innominata / Substantia Nigra Boundary*.

**The substantia innominata is a paired structure.** Each hemisphere
has its own substantia innominata, though its **medial boundaries**
are near the midline. The two sides are **bilaterally symmetric** and
**functionally non-lateralized** — the nucleus basalis's cholinergic
projections are **bilateral**, and the region's cholinergic,
GABAergic, and peptidergic contents are **bilaterally symmetric**.
See *Lateralization Notes*.

Contents (embedded structures, prose — NOT children)
----------------------------------------------------
The substantia innominata **contains** several structures, all
wired **elsewhere**:

*   **Nucleus basalis of Meynert** —
    ``.../basal_forebrain/nucleus_basalis/``. The **cortically
    projecting cholinergic nucleus** — **embedded** in the
    substantia innominata's territory, but a **sibling** in the tree,
    not a child. **This is the most important embedded structure.**

*   **Magnocellular preoptic nucleus** — **NOT wired in the tree**.
    A cholinergic/GABAergic nucleus adjacent to the nucleus basalis,
    sometimes considered part of the substantia innominata and
    sometimes part of the preoptic area. **Not present** in the tree
    dump — a **documented gap** (see *The Substantia Innominata /
    Magnocellular Preoptic Nucleus Gap*).

*   **Scattered cholinergic and GABAergic neurons** — the
    **non-nucleus-basalis** neurons of the region — **prose only**,
    not wired.

*   **Fibers of passage** — the **internal capsule**,
    **ansa lenticularis**, and **lenticular fasciculus** pass
    **through** the substantia innominata's territory. They are
    **white-matter tracts** under ``.../right/white_matter/`` — **not**
    here.

**These embedded structures are prose, not structural children.**
The tree does **not** wire them as substantia-innominata children.
Consumers that need the **nucleus basalis** must resolve it at its
own path; consumers that need the **magnocellular preoptic nucleus**
must be aware that it is **not wired** (a documented gap); consumers
that need the **fibers of passage** must resolve them under
``white_matter/``.

The Substantia Innominata / Nucleus Basalis Boundary
----------------------------------------------------
This is the **most commonly confused** boundary for consumers:

*   **Substantia innominata** (this module) — the **grey-matter
    region** between the globus pallidus and the anterior perforated
    substance. Its **boundaries are graded**, and it **contains**
    the nucleus basalis plus scattered neurons.

*   **Nucleus basalis** (``nucleus_basalis/``) — the **magnocellular
    cholinergic nucleus** embedded **within** the substantia
    innominata. Its **boundaries are cytoarchitecturally defined**
    (cholinergic neurons), and it is the **largest and most
    distinctive** cellular population within the region.

**Both are siblings under the basal forebrain.** The tree wires them
separately. Consumers that need the **cholinergic nucleus** resolve
the nucleus basalis; consumers that need the **grey-matter region**
resolve the substantia innominata. The **nucleus basalis is not a
child of the substantia innominata** — it is a **sibling** that
happens to be **embedded** in the substantia innominata's territory.

The Substantia Innominata / Extended Amygdala Boundary
------------------------------------------------------
This is the **most contested classification** for consumers:

*   **Extended amygdala** (``.../extended_amygdala/``) — a
    **limbic-forebrain continuum** including the **BNST**, the
    **central amygdaloid nucleus**, and (in some classifications)
    the **sublenticular extended amygdala (SLEA)**, which includes
    the **substantia innominata**.

*   **Substantia innominata** (this module) — a **basal forebrain
    grey-matter region** that is **classically grouped** with the
    extended amygdala in some literature.

**The tree denies the extended amygdala grouping.** It wires
``.../extended_amygdala/`` as a **sibling** of ``.../basal_forebrain/``
under ``subcortical/``, and it wires the substantia innominata under
the **basal forebrain**. This is a **deliberate boundary choice** —
the tree treats the substantia innominata as a **basal forebrain
grey-matter region**, not as an extended-amygdala component.

**Consumers that need the extended amygdala as a unit** must
**union** ``.../extended_amygdala/`` with the substantia innominata
(among other structures). The tree does **not** provide this union
as a single path — the union is a **consumer-side** operation.

The Substantia Innominata / Substantia Nigra Boundary
-----------------------------------------------------
This is the **most dangerous name confusion** in the module:

*   **Substantia innominata** (this module) — **telencephalic**,
    **ventral basal forebrain**, grey-matter **region**, contains
    the nucleus basalis. **Cholinergic** (nucleus basalis) and
    **GABAergic** (scattered neurons).

*   **Substantia nigra** — **mesencephalic**, **midbrain**,
    pigmented **nucleus**, **dopaminergic** (pars compacta) and
    **GABAergic** (pars reticulata).

**They are anatomically and functionally unrelated.** The
substantia nigra is under ``.../midbrain/tegmentum/substantia_nigra/``
— **not** here. Consumers iterating ``.../midbrain/`` and expecting
the substantia innominata there will **miss it**; consumers iterating
the basal forebrain and expecting the substantia nigra there will
**equally miss it**. The two "substantia" structures are in **different
brain regions** with **different functions** — the shared "substantia"
is a Latin word meaning "substance," not a structural relationship.

The Substantia Innominata / Magnocellular Preoptic Nucleus Gap
--------------------------------------------------------------
The **magnocellular preoptic nucleus** is a **real nucleus** embedded
in (or adjacent to) the substantia innominata — a **cholinergic/GABAergic**
population that is **classically part** of the basal forebrain
cholinergic system. But it is **NOT wired** in the tree:

*   **Not a child of the substantia innominata** — the tree shows no
    ``magnocellular_preoptic_nucleus/`` under
    ``substantia_innominata/``.
*   **Not a child of the preoptic area** — the tree shows the preoptic
    area under ``.../diencephalon/hypothalamus/anterior/preoptic_area/``,
    but no magnocellular preoptic nucleus child in the visible dump.
*   **Not wired elsewhere** — it is a **documented gap**.

This is the **second documented gap** in the basal forebrain (after the
**lateral septal nucleus** gap in the septal nuclei container). The
module documents the gap, its functions (cholinergic/GABAergic
modulation), and its **relationship to the substantia innominata**
(it is **embedded in** or **adjacent to** the region, but **not wired**).
Consumers that need the magnocellular preoptic nucleus must resolve its
functions as **prose** in this module, not as a structural child.

Function in the Human Brain
---------------------------
The substantia innominata has **no single function** — it is a
**region**, and its functions are the **aggregate** of its contents:

*   **Cortical cholinergic modulation (Nucleus Basalis Function):**
    The substantia innominata **contains** the **nucleus basalis**,
    which provides **70–80%** of cortical cholinergic innervation —
    the substrate for **arousal, attention, learning, memory
    consolidation, and cortical plasticity**. This is the region's
    **most famous function**, but it is **the nucleus basalis's
    function**, not the region's **intrinsic** function. See the
    nucleus basalis module for detail.

*   **Septohippocampal and olfactory cholinergic modulation
    (Adjacent — Diagonal Band Function):** The **diagonal band**
    **blends** into the substantia innominata's anterior territory,
    and the diagonal band's **cholinergic and GABAergic neurons**
    contribute to **hippocampal theta** and **olfactory bulb
    modulation** — but those are the **diagonal band's** functions,
    not the substantia innominata's. See the diagonal band module.

*   **Extended amygdala continuity (Contested — SLEA Classification):**
    The **sublenticular extended amygdala (SLEA)** — a continuum
    including the substantia innominata — is **sometimes** classified
    as part of the **extended amygdala** and **limbic-forebrain
    continuum**. This would give the substantia innominata a role in
    **stress, anxiety, and reward** — but the tree **denies** this
    grouping (see *The Substantia Innominata / Extended Amygdala
    Boundary*), and the SLEA classification is **contested**.

*   **Fibers of passage (Structural Function):** The substantia
    innominata contains **fibers of passage** — the **internal
    capsule** (corticospinal, corticobulbar, thalamocortical fibers),
    the **ansa lenticularis**, and the **lenticular fasciculus** —
    that pass **through** the region en route to their targets. This
    is a **structural** role, not a neural function — the substantia
    innominata is a **corridor** for fibers, not a processor.

*   **NOT a neural processor, NOT a nucleus, NOT a cholinergic
    system in its own right.** The substantia innominata is a
    **region** whose functions are the **aggregate of its contents**.
    Its **most famous function** (cortical cholinergic modulation)
    is the **nucleus basalis's** function; its **contested function**
    (extended amygdala continuity) is the **SLEA's** function; its
    **structural function** (fibers of passage) is a **corridor**
    role. The region itself is **not a processor**.

**The unifying theme:** the substantia innominata is a **heterogeneous
grey-matter region** of the ventral basal forebrain, whose functions
are the **aggregate** of its **contents** (nucleus basalis,
magnocellular preoptic nucleus [unwired], scattered neurons) and its
**fibers of passage**. It is **not a single functional system** — it
is a **region**, and its documentation must reflect that.

Associated Disorders
--------------------
Substantia innominata disorders are **the disorders of its contents**
(especially the nucleus basalis) plus **region-specific pathology**:

*   **Alzheimer's Disease (via the Nucleus Basalis):** The substantia
    innominata is the **seat** of the nucleus basalis cholinergic
    loss in Alzheimer's disease — **60–90% loss** of nucleus basalis
    neurons is the basis of the **cholinergic hypothesis** and of
    **cholinesterase-inhibitor therapy**. The **substantia innominata
    itself** is not the primary substrate — the **nucleus basalis** is
    — but the **region's pathology** is **dominated** by the
    nucleus basalis's involvement.

*   **Parkinson's Disease (via the Nucleus Basalis and Region):**
    Nucleus basalis cholinergic loss (**30–50%**) contributes to
    **cognitive impairment**, **gait dysfunction**, and **falls** in
    PD. The substantia innominata **region** may also show
    **α-synuclein pathology** in PD, contributing to local
    dysfunction.

*   **Lewy Body Dementia (via the Nucleus Basalis):** More severe
    nucleus basalis cholinergic loss (**70–80%**+) than Alzheimer's,
    contributing to the **cognitive fluctuations** and **visual
    hallucinations** of LBD. The substantia innominata region is
    **co-affected**.

*   **Vascular Dementia (Region Pathology):** Ischemia of the
    substantia innominata region (via **lenticulostriate artery**
    disease) can damage the **nucleus basalis** and **scattered
    cholinergic neurons**, contributing to **vascular cognitive
    impairment**.

*   **Hypertensive Hemorrhage (Adjacent — Lenticulostriate
    Territory):** **Putaminal hemorrhage** — the **most common site
    of hypertensive intracerebral hemorrhage** — can **extend into**
    the substantia innominata, damaging the **nucleus basalis** and
    **fibers of passage**. This is a **region-specific** vascular
    complication, adjacent to the **lenticulostriate gateway** (see
    the anterior perforated substance module).

*   **Sublenticular Extended Amygdala Pathology (Contested —
    Extended Amygdala Continuity):** If the **SLEA classification**
    is accepted, the substantia innominata would be part of the
    **extended amygdala continuum** and would be implicated in
    **stress, anxiety, and addiction** — but the tree **denies** this
    grouping, and the evidence is **contested**. Documented as a
    **contrast** disorder.

**What is NOT here:** The substantia innominata is **not** the
substrate for **Parkinson's disease** (that is the substantia nigra —
**NOT** this structure), **Huntington's disease** (striatum),
**temporal lobe epilepsy** (hippocampus), or **Kluver-Bucy syndrome**
(amygdala). Its clinical footprint is **cholinergic-cognitive**
(Alzheimer's, LBD, PD dementia, vascular dementia — via the nucleus
basalis) and **region-specific vascular** (hypertensive hemorrhage
extension) — a **distinct category** from the substantia nigra's
**dopaminergic-motor** footprint.

Lateralization Notes
--------------------
This is the **right** substantia innominata module. The substantia
innominata is **bilaterally symmetric** and **functionally
non-lateralized**:

*   **Bilateral Contents:** Each substantia innominata contains its
    **ipsilateral** nucleus basalis (projecting primarily to
    ipsilateral cortex) and its **ipsilateral** scattered cholinergic
    and GABAergic neurons. The two sides are **functionally
    symmetric** for cortical cholinergic modulation.

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the substantia innominata has **no documented left-lateralized or
    right-lateralized function**. **Alzheimer's** cholinergic loss is
    **bilateral**; **vascular dementia** is **bilateral**; **hypertensive
    hemorrhage** is **bilateral in distribution** (either side can
    bleed).

*   **Extended Amygdala Overlap (Contrast — Weak):** The substantia
    innominata's **SLEA classification** (if accepted) would put it
    in the **extended amygdala continuum**, which is **broadly
    bilaterally organized** and **not strongly lateralized**. The
    **right amygdala's fear association** belongs to the **amygdala
    module** and (weakly, via SLEA) to the **extended amygdala
    module** — **not** to the substantia innominata. **This right-side
    module is the one where a consumer is most likely to import the
    right-amygdala fear association** — because the SLEA classification
    links the substantia innominata to the extended amygdala, and a
    consumer reading the right-side module is **exactly** the consumer
    most likely to attribute the right amygdala's lateralization to
    the right substantia innominata. **Do not.** The right substantia
    innominata is **not** the right extended amygdala, and the right
    amygdala's fear-processing association **does not** transfer here.

*   **No Cortical-Level Asymmetries:** The subtle left-verbal /
    right-emotional asymmetries reported for **orbitofrontal** and
    **insular** odor processing are **cortical-level** phenomena
    **downstream** of the substantia innominata's nucleus basalis
    projection. Do not import them into the substantia innominata.

**A consumer that assumes "right substantia innominata = left
substantia innominata" will be structurally and functionally
correct** — the two sides are symmetric, no lateralized function has
been demonstrated, and the region's **bilateral contents** are the
anatomical substrate of its **bilateral functions**. This is a
**strict-mirror pair with a light warning** — the substantia
innominata has **classificatory overlap** with the extended amygdala
(SLEA), but it is **not adjacent** to the amygdala and the tree
**denies** the extended amygdala grouping. The warning is **lighter**
than the **emphatic** periamygdaloid/uncus/subcortical warnings,
**lighter** than the **moderate** parent septal nuclei warning, and
**on par with** the nucleus basalis, diagonal band, and medial septal
nucleus light warnings. **The right-side module carries the
amygdala-lateralization warning explicitly**, because the SLEA
classification is the claim a right-side reader is most likely to
import — but the warning is **moderate**, not emphatic, because the
substantia innominata is **not adjacent** to the amygdala.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``rhinencephalon/``, ``.../diencephalon/``,
    ``.../midbrain/``, or the other subcortical containers. The
    substantia innominata's relationships to the nucleus basalis,
    extended amygdala, globus pallidus, anterior perforated substance,
    and substantia nigra are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **nucleus basalis**
    and the **magnocellular preoptic nucleus** are **embedded
    structures**, not children. The **scattered cholinergic and
    GABAergic neurons** and the **fibers of passage** are **prose**,
    not children. Consumers must not assume any exist as children;
    resolve each at its own path (or note the gap).
*   **REGION, not a nucleus.** The substantia innominata is a
    **graded grey-matter region**, not a single cytoarchitecturally
    defined nucleus. Its boundaries are **fuzzy by design** — this is
    why it is called "**the unnamed substance**." Consumers must not
    expect clean boundaries.
*   **NOT the nucleus basalis — sibling, not child.** The nucleus
    basalis is **embedded in** the substantia innominata's territory,
    but the tree wires them as **siblings**. Consumers that need the
    **cholinergic nucleus** must resolve
    ``.../basal_forebrain/nucleus_basalis/``, not this module.
*   **NOT the extended amygdala — classificatory overlap, wired
    separately.** The **SLEA classification** groups the substantia
    innominata with the extended amygdala in some literature, but the
    tree **denies** this grouping by wiring them as **siblings**.
    Consumers that need the extended amygdala must **union**
    ``.../extended_amygdala/`` with this module (among others).
*   **NOT the substantia nigra — name confusion.** The substantia
    innominata (telencephalic, ventral basal forebrain) and the
    substantia nigra (mesencephalic, midbrain) are **anatomically and
    functionally unrelated**. Do not conflate them.
*   **NOT the globus pallidus — adjacent basal ganglia sibling.**
    The globus pallidus is under ``.../basal_ganglia/``, not the basal
    forebrain. The substantia innominata **blends** into the globus
    pallidus laterally, but they are **separate** in the tree.
*   **NOT the anterior perforated substance — adjacent basal
    forebrain sibling.** The APS is a **sibling** under the basal
    forebrain. The substantia innominata **blends** into the APS
    anteriorly, but they are **separate** in the tree.
*   **Magnocellular preoptic nucleus — DOCUMENTED GAP.** The
    **magnocellular preoptic nucleus** is a **real nucleus** adjacent
    to the nucleus basalis, but it is **NOT wired** in the tree.
    Consumers that need it must resolve its functions as **prose** in
    this module, not as a structural child.
*   **No ``AREA_PATHS`` hop.** The substantia innominata is a local
    leaf under the basal forebrain, not a cross-listed leaf.
*   **No nested cross-listing.** The substantia innominata has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left substantia innominata — strict
    mirror with a light warning.** Right and left substantia
    innominata modules are **structurally identical** — same leaf
    status, same region-not-nucleus caveat, same nucleus-basalis
    sibling note, same extended-amygdala classificatory-overlap note,
    same substantia-nigra name-confusion flag, same magnocellular
    preoptic gap. **The amygdala-lateralization warning is light**,
    matching the nucleus basalis, diagonal band, and medial septal
    nucleus light-warning category. **The right-side module keeps the
    warning light** — no dedicated Usage block, no emphatic contrast
    reference, only a **moderate** Lateralization note — because the
    substantia innominata is **not adjacent** to the amygdala, and the
    SLEA classification is a **weak** link.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain import substantia_innominata

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_forebrain.substantia_innominata"
    )

**Do not** assume the substantia innominata **contains** the nucleus
basalis as a child. The nucleus basalis is a **sibling** under the
basal forebrain, **embedded in** the substantia innominata's territory
but **not wired** under it.

**Do not** assume the substantia innominata **is** the nucleus
basalis, or vice versa. They are **anatomically overlapping** but
**structurally separate**.

**Do not** assume the substantia innominata **is** the substantia
nigra. They share the word "substantia" but are **anatomically and
functionally unrelated** — telencephalic vs. mesencephalic, basal
forebrain vs. midbrain, grey-matter region vs. pigmented nucleus.

**Do not** assume the substantia innominata **contains** the
magnocellular preoptic nucleus as a child. It is a **real nucleus**
adjacent to the nucleus basalis, but it is **NOT wired** in the
tree — a **documented gap**.

**Do not** assume the substantia innominata **is** the extended
amygdala, or contains it. The **SLEA classification** groups them
in some literature, but the tree **denies** the grouping by wiring
them as **siblings**.

**Do not** assume the substantia innominata is a **nucleus**. It is
a **graded grey-matter region** — "the unnamed substance" — whose
boundaries are **fuzzy by design**.

**Do not** assume the substantia innominata is under the **basal
ganglia**. It is under the **basal forebrain**; the globus pallidus
is a **basal ganglia sibling**.

**Do not** import **right-amygdala lateralization claims** into the
right substantia innominata. The SLEA classification links the
substantia innominata to the extended amygdala, but the right
amygdala's fear-processing association belongs to the **amygdala
module** and (weakly, via SLEA) to the **extended amygdala module** —
**not** here.

Iterating the substantia innominata's (empty) children (recommended
consumer pattern)::

    SI_CHILDREN = ()
    # The substantia innominata is a leaf. The nucleus basalis,
    # magnocellular preoptic nucleus, scattered neurons, and fibers
    # of passage are embedded structures / prose, not modules.

Reaching the nucleus basalis (recommended consumer pattern)::

    # The nucleus basalis is EMBEDDED in the substantia innominata
    # but is a SIBLING, not a child. Resolve it at its own path:
    #
    #   subcortical.basal_forebrain.nucleus_basalis
    #
    # The substantia innominata is the REGION; the nucleus basalis
    # is the NUCLEUS embedded in it. They are siblings.

Reaching the extended amygdala (recommended consumer pattern)::

    # The extended amygdala is a SIBLING of the basal forebrain, not
    # a container for the substantia innominata. Resolve it at its
    # own path:
    #
    #   subcortical.extended_amygdala
    #
    # If the SLEA classification is needed, UNION extended_amygdala
    # with substantia_innominata (and other SLEA components) at the
    # consumer level. The tree does not provide this union.

Reaching the substantia nigra (recommended consumer pattern — NOTE
the name confusion)::

    # The substantia nigra is NOT this structure. It is in the
    # midbrain:
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # Do NOT resolve substantia nigra through the basal forebrain.
    # The two "substantia" structures are unrelated.

Reaching the magnocellular preoptic nucleus's FUNCTIONS (recommended
consumer pattern — note the GAP)::

    # The magnocellular preoptic nucleus is NOT in the tree (a
    # documented gap). Its functions are documented as PROSE in this
    # module. If you need a path for it, you must:
    #
    #   1. Note the gap in your registry.
    #   2. Optionally, document it as a "virtual" or "prose-only"
    #      node, with a clear "NOT IN TREE" marker.
    #
    # Do NOT attempt to resolve a "magnocellular_preoptic_nucleus"
    # path — it does not exist in the tree.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        si_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.substantia_innominata"
        )
        # resolve si_path through the memory/recall layer

References
----------
*   **Canonical basal forebrain anatomy:** Heimer, L., de Olmos, J.,
    Alheid, G.F., Záborszky, L. (1999). "The human basal forebrain:
    an overview." In *The Human Nervous System* (Paxinos, G., ed.),
    2nd ed. (Definitive overview; substantia innominata as a
    grey-matter region; nucleus basalis; magnocellular preoptic
    nucleus; SLEA.)
*   **Etymology and classical anatomy:** Reichert, K.B. (1859). *Der
    Bau des menschlichen Gehirns*. (Original description; the name
    "substantia innominata of Reichert.")
*   **Cholinergic system:** Mesulam, M.-M., Mufson, E.J., Levey,
    A.I., Wainer, B.H. (1983). "Cholinergic innervation of cortex
    by the basal forebrain." *Journal of Comparative Neurology*
    214:170–197. (Nucleus basalis within the substantia innominata;
    cholinergic system.)
*   **Extended amygdala / SLEA:** Alheid, G.F., Heimer, L. (1988).
    "New perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience* 27:1–39.
    (Sublenticular extended amygdala; substantia innominata in the
    extended amygdala continuum.)
*   **SLEA and stress:** de Olmos, J.S., Heimer, L. (1999). "The
    concepts of the ventral striatopallidal system and extended
    amygdala." *Annals of the New York Academy of Sciences*
    877:1–32. (SLEA; substantia innominata; extended amygdala
    continuum; contested classification.)
*   **Alzheimer's cholinergic hypothesis:** Whitehouse, P.J., et al.
    (1982). "Alzheimer's disease and senile dementia: loss of
    neurons in the basal forebrain." *Science* 215:1237–1239.
    (Nucleus basalis loss in Alzheimer's; substantia innominata
    pathology.)
*   **Lewy body dementia cholinergic loss:** Perry, E.K., et al.
    (1994). "Cholinergic and dopaminergic activities in senile
    dementia of Lewy body type." *Alzheimer Disease and Associated
    Disorders* 8:48–56. (More severe nucleus basalis loss in LBD;
    substantia innominata involvement.)
*   **Parkinson's cholinergic loss:** Bohnen, N.I., et al. (2003).
    "Cortical cholinergic function is more severely affected in
    parkinsonian dementia than in Alzheimer disease."
    *Archives of Neurology* 60:1745–1748. (Nucleus basalis
    cholinergic loss in PD dementia; substantia innominata region.)
*   **Substantia nigra (name-confusion contrast):** Braak, H., et
    al. (2003). "Staging of brain pathology related to sporadic
    Parkinson's disease." *Neurobiology of Aging* 24:197–211.
    (Substantia nigra pathology in PD; the substantia nigra is
    **NOT** the substantia innominata — contrast reference.)
*   **Magnocellular preoptic nucleus:** Saper, C.B. (2002). "The
    central autonomic nervous system." In *The Human Nervous
    System* (Paxinos, G., ed.), 2nd ed. (Magnocellular preoptic
    nucleus as a basal forebrain structure adjacent to the nucleus
    basalis; often grouped with the substantia innominata.)
*   **Internal capsule and fibers of passage:** Nieuwenhuys, R.,
    Voogd, J., van Huijzen, C. (2008). *The Human Central Nervous
    System*, 4th ed. (Internal capsule, ansa lenticularis, lenticular
    fasciculus; fibers passing through the substantia innominata
    territory.)
*   **Vascular dementia:** Román, G.C., et al. (1993). "Vascular
    dementia: diagnostic criteria for research studies."
    *Neurology* 43:250–260. (Vascular dementia; lenticulostriate
    ischemia of the substantia innominata region.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the substantia innominata —
    it belongs to the amygdala module and, weakly via SLEA, to the
    extended amygdala module.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Substantia innominata in overview.)
*   NeuroNames — Substantia innominata (right); FMA — Substantia
    innominata (right member).
"""