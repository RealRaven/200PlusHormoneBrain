"""
infrastructure.brainparts.midbrain.tegmentum.caudal_linear_nucleus
==================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        └── caudal_linear_nucleus     <-- THIS MODULE (MIDLINE LEAF —
                                          not paired — the FIRST
                                          midline tegmentum leaf)

**Primary synonym:** Caudal linear nucleus; **CLi**; caudal linear
raphe nucleus; **nucleus linearis caudalis** (Latin); the caudal
linear subdivision of the rostral raphe complex.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **midline** **serotonergic and dopaminergic**
nucleus in the **ventral midbrain tegmentum** — at the level of the
**inferior colliculus** (caudal midbrain) — near the **decussation
of the superior cerebellar peduncle**, **ventral** to the
periaqueductal gray, **medial** to the ventral tegmental area, and
**dorsal** to the interpeduncular fossa. It is **part of the
rostral raphe complex** — along with the **dorsal raphe nucleus**
(DR), the **median raphe nucleus** (MnR), and the **rostral linear
nucleus** (RLi). Its **serotonergic** phenotype (tryptophan
hydroxylase, 5-HT synthesis) is a **``chemicals_hormones``-layer
fact** — see *Chemicals-Layer Discipline*. Its **dopaminergic**
phenotype (a subset of its neurons — part of the **A10
dopaminergic cell group** alongside the VTA) is also a
**``chemicals_hormones``-layer fact**.
**Container status:** **This module is a LEAF**, **midline** — it
is **NOT** under ``tegmentum/left/`` or ``tegmentum/right/`` — it
sits **directly under** the tegmentum container. It is the **FIRST
MIDLINE LEAF** in the family — it **establishes the midline
exception** to the tegmentum container's **paired-leaf rule**. See
*The First Midline Tegmentum Leaf* and *Design Contract*.
**Part of:** The **tegmentum** region container — as a **midline**
leaf. **The CLi is NOT a cranial nerve nucleus** and is **NOT
cross-listed** with ``cranial_nerve_nuclei/`` — see *NOT a CN
Nucleus*.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — **midline**, **not** a side
container.
**Structural children:** **None.** This is a **leaf** module. The
**serotonergic** and **dopaminergic** subpopulations are documented
as **prose**, not as structural children.
**Boundary status (MIDLINE LEAF — NOT PAIRED — the FIRST MIDLINE
TEGMENTUM LEAF):** **Boundary case — the caudal linear nucleus is a
MIDLINE LEAF.** It sits **directly under** the tegmentum container
— **NOT** under ``tegmentum/left/`` or ``tegmentum/right/``. **It is
the FIRST midline tegmentum leaf in the family** — it
**establishes the midline exception** to the tegmentum container's
**paired-leaf rule**. The **paired-leaf rule** — which states that
"each tegmentum nucleus is a paired structure (a ``left/`` leaf and
a ``right/`` leaf)" — has **exceptions for midline nuclei**.
**The CLi is the first midline exception.** Consumers must **not**
assume the CLi has a `left/` and a `right/` leaf — it has **one
leaf**, at the top level of the tegmentum container. See *The First
Midline Tegmentum Leaf*.
**Boundary status (MIDLINE EXCEPTION — the tegmentum container's
paired-leaf rule has EXCEPTIONS for MIDLINE nuclei):** **Boundary
case — the tegmentum container's paired-leaf rule (which says
"each tegmentum nucleus is a paired structure — a ``left/`` leaf
and a ``right/`` leaf") has EXCEPTIONS for MIDLINE nuclei.** The
**caudal linear nucleus** is the **first exception to be written**
— it is **midline** and is a **single leaf** directly under
``tegmentum/``. The **other midline (or midline-adjacent)
tegmentum structures** — the **periaqueductal gray** (PAG; a single
midline column surrounding the aqueduct), and the **midbrain
reticular formation** (a diffuse region that may be represented as
midline) — **may also be midline**, depending on the on-disk tree.
**The tegmentum container's aggregation rule should be AMENDED** to
state that **midline nuclei are permitted** as **direct children**
of ``tegmentum/`` — not **required** to be under ``left/`` or
``right/``. This leaf is the first one that documents the exception
— **the container amendment is a follow-up**. See *Design
Contract* — *Live amendment to the tegmentum container*.
**Boundary status (NOT a CN nucleus — NOT cross-listed with
``cranial_nerve_nuclei/``):** **Boundary case — the caudal linear
nucleus is NOT a cranial nerve nucleus.** It is a **serotonergic /
dopaminergic neuromodulatory nucleus** — it is **not a CN nucleus**
and is **NOT cross-listed** with the ``cranial_nerve_nuclei/``
container. The **four CN nuclei** in the tegmentum (oculomotor,
trochlear, Edinger-Westphal, mesencephalic trigeminal) are
**cross-listed** between ``tegmentum/`` and
``cranial_nerve_nuclei/`` — **the CLi is not one of them**.
Consumers must **not** look for the CLi under
``.../cranial_nerve_nuclei/`` — it has **one path only**:
``.../tegmentum/caudal_linear_nucleus/``.
**Boundary status (NOT the dorsal raphe nucleus — the DR is a
SIBLING MIDLINE raphe nucleus):** **Boundary case — the caudal
linear nucleus is NOT the dorsal raphe nucleus (DR).** The **DR**
(``.../tegmentum/dorsal_raphe_nucleus/``) is a **separate**,
**larger**, **more dorsal** midline raphe nucleus — also
serotonergic, also part of the rostral raphe complex. **The CLi is
caudal to the DR and smaller.** They are **sibling midline raphe
nuclei** — **different structures**, **different locations**,
**different projections** (the DR projects more strongly to the
forebrain; the CLi projects more strongly to the midbrain and the
diencephalon). Consumers must **not** conflate the CLi with the
DR.
**Boundary status (NOT the median raphe nucleus — the MnR is a
PONTINE raphe nucleus):** **Boundary case — the caudal linear
nucleus is NOT the median raphe nucleus (MnR).** The **MnR**
(``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) is a
**pons** structure — the **pontine** median raphe. **The CLi is
midbrain.** They are **DIFFERENT STRUCTURES at DIFFERENT levels**
— the **MnR** is **rhombencephalic**; the **CLi** is
**mesencephalic**. The **MnR** is sometimes grouped with the
rostral raphe complex in **functional** discussions (it projects
both ascending and descending) — but the **MnR is pons**, and the
**CLi is midbrain**. Consumers must **not** conflate the two.
**Boundary status (NOT the rostral linear nucleus — the RLi is
ROSTRAL to the CLi):** **Boundary case — the caudal linear nucleus
is NOT the rostral linear nucleus (RLi).** The **RLi** is a
**separate** midline raphe nucleus — **rostral** to the CLi — also
serotonergic, also part of the rostral raphe complex. **They are
sibling linear nuclei** — **different structures at different
rostrocaudal levels** (the RLi is more rostral; the CLi is more
caudal). Consumers must **not** conflate the two.
**Boundary status (NOT the ventral tegmental area — the VTA is a
PAIRED dopaminergic nucleus):** **Boundary case — the caudal
linear nucleus is NOT the ventral tegmental area (VTA).** The
**VTA** (``.../tegmentum/left/ventral_tegmental_area/`` and the
right counterpart) is a **PAIRED dopaminergic nucleus** — the
**mesolimbic / mesocortical** reward pathways. The **CLi**
**contains some dopaminergic neurons** (part of the A10 group
alongside the VTA) — but the **CLi is MIDLINE and primarily
SEROTONERGIC**; the **VTA is PAIRED and primarily DOPAMINERGIC**.
**Different structures** — **different laterality** (midline vs.
paired), **different primary transmitter** (serotonergic vs.
dopaminergic), **different projections**. Consumers must **not**
conflate the CLi with the VTA.
**Boundary status (NOT the substantia nigra — the SN is a PAIRED
dopaminergic/GABAergic nucleus):** **Boundary case — the caudal
linear nucleus is NOT the substantia nigra (SN).** The **SN**
(``.../tegmentum/left/substantia_nigra/`` and the right
counterpart) is a **PAIRED nucleus** — with the **pars compacta**
(dopaminergic; the nigrostriatal input to the basal ganglia) and
the **pars reticulata** (GABAergic; the nigrotectal inhibitory
gate). The **CLi** is **MIDLINE and primarily serotonergic** —
**different structures** in **different positions** and **different
functional systems**. Consumers must **not** conflate the CLi with
the SN.
**Boundary status (NOT the periaqueductal gray — the PAG SURROUNDS
the cerebral aqueduct):** **Boundary case — the caudal linear
nucleus is NOT the periaqueductal gray (PAG).** The **PAG** is the
**pain-modulation and defensive-behavior** region — it **surrounds**
the **cerebral aqueduct** — **dorsal** to the CLi. **The CLi is
VENTRAL to the PAG** — in the ventral tegmentum, near the
interpeduncular fossa. **They are DIFFERENT STRUCTURES in
DIFFERENT positions** — the **PAG** surrounds the aqueduct; the
**CLi** is in the ventral tegmentum. Consumers must **not**
conflate the CLi with the PAG.
**Boundary status (NOT the dorsal raphe in the pons — that is the
MnR; NOT the raphe magnus, pallidus, or obscurus — those are
MEDULLARY):** **Boundary case — the caudal linear nucleus is NOT
the medullary raphe nuclei.** The **raphe magnus**, **raphe
pallidus**, and **raphe obscurus**
(``.../hindbrain/myencephalon/medulla_oblongata/``) are **medullary
raphe nuclei** — **different structures** at **different levels**.
The **CLi is midbrain**. Consumers must **not** conflate the CLi
with any medullary raphe nucleus.
**Boundary status (SEROTONERGIC / DOPAMINERGIC — the phenotype is a
``chemicals_hormones``-layer fact):** **Boundary case — the caudal
linear nucleus is **serotonergic** (the majority of its neurons)
and **dopaminergic** (a subset of its neurons — part of the A10
group).** **Both phenotypes are ``chemicals_hormones``-layer
facts** — the **serotonergic phenotype** (tryptophan hydroxylase,
5-HT synthesis, serotonin transporters, serotonin receptors) and
the **dopaminergic phenotype** (tyrosine hydroxylase, dopamine
synthesis, dopamine transporters, dopamine receptors) are
**neurochemical** facts, **not** structural facts. They are
documented as **prose** in the leaf and **never imported** into the
midbrain structural layer. Dependency DAG unchanged:
``chemicals_hormones → memory → brainparts``. Consumers must **not**
import the **serotonergic** or **dopaminergic** phenotype into the
midbrain structural layer. See *Chemicals-Layer Discipline* and
*Design Contract*.
**Boundary status (NEUROMODULATORY NUCLEUS — a NEW structure
class — NOT an oscillator, NOT a premotor pool, NOT a motor
nucleus, NOT a sensory relay, NOT a conduction pathway):**
**Boundary case — the caudal linear nucleus is a NEUROMODULATORY
NUCLEUS.** In the family's **structure-class taxonomy**, it is a
**new class** — **neuromodulatory nucleus** — the **same class**
as the **locus coeruleus** (noradrenergic), the **dorsal raphe**
(serotonergic), the **median raphe** (serotonergic), and the
**VTA** (dopaminergic). It is **not** an **oscillator** (it does
not generate a rhythm), **not** a **premotor pool** (it does not
transform motor commands), **not** a **motor nucleus** (it does
not drive muscle), **not** a **sensory relay** (it does not
transduce or relay sensory input), **not** a **sensorimotor
integration** structure (it does not integrate input into a
behavioral command), and **not** a **conduction pathway** (it is
grey matter, not white matter). **It modulates the excitability of
its targets** via **volume transmission** of serotonin (and
dopamine) — that is its functional class. **Neuromodulatory nuclei
carry NO coupling warning** — same rule as motor nuclei, premotor
pools, sensor nuclei, relay nuclei, sensorimotor integration
structures, and conduction pathways. Its **midline position** —
**not paired** — is the **structural expression** of its
**modulatory, distributed** function: it **does not have a
left/right pair** because it **modulates both sides**. **The CLi is
the FIRST MIDLINE MODULATORY NUCLEUS in the family** — the
structural foundation of its neurology. See *The First Midline
Tegmentum Leaf* and *Lateralization Notes*.
**Boundary status (NO COUPLING WARNING — the CLi is a MODULATORY
NUCLEUS):** **Boundary case — the caudal linear nucleus carries NO
coupling warning.** The **coupling warning** attaches to
**OSCILLATORS** (the pre-Bötzinger complex, the Bötzinger complex,
the pFRG) — and the **CLi is not an oscillator**. **It is a
midline modulatory nucleus** — a **single leaf**, **not paired**.
**Neuromodulatory nuclei carry NO coupling warning** — same rule as
every non-oscillator class. The **midline position** is **not a
coupling hazard** — it is the **structural fact** of a
**distributed modulator** that **reaches both sides** via its
**projections**, **not** via intrinsic left-right coupling (there
are no "two sides" to couple — the CLi is one midline nucleus).
Consumers must **not** import a coupling warning into the CLi, and
must **not** assume the CLi has a **left/right pair** whose **two
sides must synchronize** — it has **one midline nucleus** whose
**distributed projections** carry its modulation to both sides.

Overview
--------
The caudal linear nucleus (CLi) is a **midline serotonergic and
dopaminergic nucleus** in the **ventral midbrain tegmentum** — at
the level of the **inferior colliculus** (caudal midbrain) — near
the **decussation of the superior cerebellar peduncle**, **ventral**
to the periaqueductal gray, **medial** to the ventral tegmental
area, and **dorsal** to the interpeduncular fossa. It is **part of
the rostral raphe complex** — along with the **dorsal raphe
nucleus** (DR), the **median raphe nucleus** (MnR — technically
pontine but grouped with the rostral complex in functional
discussions), and the **rostral linear nucleus** (RLi). It is the
**first midline tegmentum leaf in the family** — its **midline
position** is the **structural expression** of its **modulatory,
distributed** function. It is a **neuromodulatory nucleus** — the
**same class** as the locus coeruleus (noradrenergic), the dorsal
raphe (serotonergic), the median raphe (serotonergic), and the VTA
(dopaminergic).

**The CLi is a MIDLINE LEAF — NOT paired.** It sits **directly
under** the tegmentum container — **NOT** under
``tegmentum/left/`` or ``tegmentum/right/``. **It is the FIRST
midline tegmentum leaf** — it **establishes the midline
exception** to the tegmentum container's **paired-leaf rule**. See
*The First Midline Tegmentum Leaf*.

**The CLi is NOT a CN nucleus.** It is a **serotonergic /
dopaminergic neuromodulatory nucleus** — it is **not** cross-listed
with ``cranial_nerve_nuclei/``. The **four CN nuclei** in the
tegmentum are cross-listed; the **CLi is not**. It has **one path
only**: ``.../tegmentum/caudal_linear_nucleus/``.

**The CLi is a NEUROMODULATORY NUCLEUS.** It **modulates the
excitability of its targets** via **volume transmission** of
serotonin (and dopamine). It is **not an oscillator**, **not a
premotor pool**, **not a motor nucleus**, **not a sensory relay**,
**not a sensorimotor integration** structure, and **not a
conduction pathway**.

**The CLi carries NO coupling warning.** It is a **midline
modulatory nucleus** — a **single leaf**, **not paired**.
**Neuromodulatory nuclei carry NO coupling warning** — same rule as
every non-oscillator class.

The First Midline Tegmentum Leaf
--------------------------------
**The caudal linear nucleus is the FIRST midline tegmentum leaf in
the family.** This is a **genuinely new structural case** — every
other tegmentum leaf written so far has been **paired**
(``tegmentum/left/<nucleus>`` + ``tegmentum/right/<nucleus>``).
The CLi sits **directly under** the tegmentum container — **no
`left/` or `right/`**. It is **one leaf**.

**Why the CLi is midline:** the CLi is a **raphe nucleus** — a
**midline serotonergic nucleus** of the **rostral raphe complex**.
Like the **dorsal raphe** and the **rostral linear nucleus**, it sits
on the **midline** — it **modulates both sides** via its
**distributed projections**, **not** via **intrinsic left-right
coupling**. **The midline position is the structural expression of
its modulatory function** — a **distributed modulator** that
**reaches both sides** does not need a **left/right pair**; it needs
a **midline nucleus** whose projections **fan out bilaterally**.

**The tegmentum container's paired-leaf rule has exceptions.** The
**paired-leaf rule** — which says "each tegmentum nucleus is a
paired structure (a ``left/`` leaf and a ``right/`` leaf)" — was
written **before** the CLi was added. **The CLi is the first
exception.** The **other midline (or midline-adjacent) tegmentum
structures** — the **periaqueductal gray** (PAG; a single midline
column surrounding the aqueduct) and the **midbrain reticular
formation** (a diffuse region that may be represented as midline) —
**may also be midline**, depending on the on-disk tree. **The
tegmentum container's aggregation rule should be AMENDED** to state
that **midline nuclei are permitted** as **direct children** of
``tegmentum/`` — **not required** to be under ``left/`` or
``right/``. This leaf is the **first** to document the exception;
**the container amendment is a follow-up.**

**The midbrain container's prose should be updated too.** The
midbrain container written earlier said "Most of its functional
children (superior colliculus, inferior colliculus, substantia
nigra, ventral tegmental area, red nucleus, oculomotor nucleus,
trochlear nucleus, Edinger-Westphal nucleus, mesencephalic
trigeminal nucleus, cerebral peduncles) are paired (left/right). The
cerebral aqueduct and the periaqueductal gray are midline
structures, not paired." — **that prose is correct for the
cerebral aqueduct** (a midline CSF space), but the **tegmentum
container** written later said the **PAG is paired** in the tree
— **a contradiction with the midbrain container's prose.** **The
CLi is a clean new data point: the tegmentum container has at least
ONE confirmed midline leaf, and the PAG may or may not be midline
depending on the on-disk tree.** **Both containers should be
reconciled** — the midbrain container's PAG prose and the
tegmentum container's paired-leaf rule both need adjustment to
accommodate **midline leaves**. The CLi is the **first** such
leaf; the reconciliation is a **follow-up amendment**.

Subnuclear Organization (prose, not structural children)
-------------------------------------------------------
The caudal linear nucleus has **no classical subnuclear
organization** in the cytoarchitectonic sense. It has a **single
population of neurons** — with **two functionally and
neurochemically distinct subpopulations** — documented as
**prose**, not as structural children:

*   **Serotonergic neurons** — the **majority** of the CLi's
    neurons — **tryptophan hydroxylase-positive (TPH⁺)**,
    **serotonin-positive (5-HT⁺)**. They project to the
    **forebrain** (cortex, limbic system, striatum) and the
    **diencephalon** (hypothalamus, thalamus) — contributing to
    the **ascending serotonergic system**.

*   **Dopaminergic neurons** — a **subset** of the CLi's neurons
    — **tyrosine hydroxylase-positive (TH⁺)**,
    **dopamine-positive (DA⁺)** — part of the **A10 dopaminergic
    cell group** alongside the **VTA**. They project to the
    **limbic system** and the **striatum** — contributing to the
    **mesolimbic / mesocortical dopaminergic system**.

**These subpopulations are prose, not structural children.** The
tree wires the **caudal linear nucleus** as a **single leaf** under
the tegmentum container (midline). Consumers must **not** resolve
``.../caudal_linear_nucleus/serotonergic_subpopulation`` — no such
path exists.

The Rostral Raphe Complex (the family context)
----------------------------------------------
The **caudal linear nucleus** is part of the **rostral raphe
complex** — the **ascending serotonergic system** of the midbrain
and rostral pons. The complex contains:

*   **Dorsal raphe nucleus (DR)** — the **largest** serotonergic
    nucleus — **dorsal** midbrain tegmentum — projects to the
    **forebrain** (cortex, limbic system, striatum, thalamus) —
    **mood, anxiety, sleep, appetite, cognition**.

*   **Median raphe nucleus (MnR)** — a **major** serotonergic
    nucleus — **pons** (rostral pons / pontomesencephalic
    junction) — projects to the **limbic system** (hippocampus,
    septum, hypothalamus) — **mood, anxiety, memory**.

*   **Caudal linear nucleus (CLi)** — **THIS LEAF** — a **smaller**
    serotonergic and dopaminergic nucleus — **ventral midbrain
    tegmentum**, at the **inferior colliculus** level — projects
    to the **forebrain, diencephalon, and limbic system**.

*   **Rostral linear nucleus (RLi)** — a **smaller** serotonergic
    nucleus — **rostral** to the CLi — projects to the
    **forebrain and limbic system**.

**The rostral raphe complex projects ASCENDING** — to the cortex,
the limbic system, the striatum, the thalamus, and the hypothalamus
— **modulating** mood, anxiety, sleep, appetite, cognition, and
reward. **The caudal raphe complex** (raphe magnus, raphe pallidus,
raphe obscurus) is in the **medulla** — it projects **DESCENDING**
to the **spinal cord** — **modulating pain** (the raphe magnus is
the key descending pain-modulation nucleus), **autonomic function**,
and **motor tone**. **The CLi is a small ascending raphe nucleus**
— one node in the **ascending serotonergic system**, one of several
**modulatory nuclei** of the rostral raphe complex.

**The CLi is NOT the DR and NOT the MnR.** The **DR** is the
**largest** and **most studied** serotonergic nucleus — the
**primary target** of SSRI pharmacology and the **primary
serotonergic nucleus** in **mood and anxiety disorders**. The
**MnR** is a **major** serotonergic nucleus — the **primary
serotonergic projection** to the **hippocampus**. **The CLi is a
smaller, caudal contributor** — **one node** in the **rostral raphe
complex**, **not the primary serotonergic nucleus** in any
clinical syndrome. Consumers must **not** conflate the CLi with
the DR or the MnR — the **clinical associations** of the
serotonergic system are **distributed** across the **DR**, the
**MnR**, the **RLi**, and the **CLi**, and the **DR is the
primary** in most clinical discussions.

The CLi's Place in the Neuromodulatory System
---------------------------------------------
The **caudal linear nucleus** is a **neuromodulatory nucleus** —
the **same class** as the **locus coeruleus** (noradrenergic), the
**dorsal raphe** (serotonergic), the **median raphe**
(serotonergic), and the **VTA** (dopaminergic). **Neuromodulatory
nuclei** are a **distinct structure class**:

*   **They are NOT sensory relays.** They do **not** transduce or
    relay a specific sensory modality. (The **IC** is a sensory
    relay; the **CLi** is a modulator.)

*   **They are NOT motor nuclei.** They do **not** drive muscle.
    (The **CN III/IV nuclei** are motor nuclei; the **CLi** is a
    modulator.)

*   **They are NOT premotor pools.** They do **not** transform
    motor commands. (The **PPRF**, the **riMLF**, and the
    **interstitial nucleus of Cajal** are premotor saccade
    generators; the **CLi** is a modulator.)

*   **They are NOT sensorimotor integration structures.** They do
    **not** integrate sensory input into a behavioral command.
    (The **superior colliculus** is a sensorimotor integration
    structure; the **CLi** is a modulator.)

*   **They are NOT conduction pathways.** They are **grey matter**
    — nuclei — **not white matter**. (The **tectobulbar tract**
    is a conduction pathway; the **CLi** is a nucleus.)

*   **They MODULATE the excitability of their targets** via
    **volume transmission** of a **neuromodulator** — **serotonin**
    (for the raphe nuclei), **noradrenaline** (for the locus
    coeruleus), **dopamine** (for the VTA and the substantia nigra
    pars compacta). **The modulation is distributed and
    long-range** — it **sets the gain** of its target circuits,
    rather than **conveying a specific signal**.

**The CLi is a NEW CLASS in the family** — the **neuromodulatory
nucleus** — the **same class** as the locus coeruleus and the
dorsal raphe, but the **first** to be written with a **serotonergic
phenotype** (the locus coeruleus was noradrenergic in my earlier
references; the VTA and SNc were dopaminergic). **The class carries
NO coupling warning** — same rule as every non-oscillator class.
**The midline position is the structural expression of the
modulatory function** — a **distributed modulator** that **reaches
both sides** does not need a **left/right pair**; it needs a
**midline nucleus** whose projections **fan out bilaterally**. See
*The First Midline Tegmentum Leaf* and *Lateralization Notes*.

The Caudal Linear Nucleus / Dorsal Raphe Nucleus Boundary
---------------------------------------------------------
This is the **sibling midline raphe nucleus** boundary — the
**most consequential** boundary in the leaf:

*   **Caudal linear nucleus** (this module) — **smaller**, **more
    caudal** (inferior colliculus level), **ventral tegmentum**
    midline — **serotonergic** (majority) and **dopaminergic**
    (subset — A10 group).

*   **Dorsal raphe nucleus (DR)**
    (``.../tegmentum/dorsal_raphe_nucleus/``) — **larger**, **more
    dorsal**, **more rostral** (superior colliculus level, some
    parts extending into the rostral midbrain) — **primarily
    serotonergic** — the **largest serotonergic nucleus**.

**They are SIBLING MIDLINE RAPHE NUCLEI** — **different
structures**, **different locations**, **different projections**
(the DR projects more strongly to the forebrain; the CLi projects
more strongly to the midbrain and the diencephalon). Consumers must
**not** conflate the CLi with the DR. **The DR is the primary
serotonergic nucleus** in most clinical discussions (mood, anxiety,
SSRI pharmacology); the **CLi is a smaller, caudal contributor**.
See *The Rostral Raphe Complex*.

The Caudal Linear Nucleus / Median Raphe Nucleus Boundary
---------------------------------------------------------
This is the **midbrain / pons** raphe boundary:

*   **Caudal linear nucleus** (this module) — **midbrain**.

*   **Median raphe nucleus (MnR)**
    (``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) —
    **pons** (rostral pons / pontomesencephalic junction) —
    **primarily serotonergic** — the **primary serotonergic
    projection to the hippocampus**.

**The MnR is a PONTINE structure; the CLi is MESENCEPHALIC.**
**Different levels.** The MnR is sometimes grouped with the rostral
raphe complex in **functional** discussions (it projects both
ascending and descending) — but the **MnR is pons**, and the **CLi
is midbrain**. Consumers must **not** conflate the two.

The Caudal Linear Nucleus / Rostral Linear Nucleus Boundary
-----------------------------------------------------------
This is the **caudal / rostral** linear nucleus boundary:

*   **Caudal linear nucleus** (this module) — **caudal** — the
    caudal linear subdivision of the rostral raphe complex.

*   **Rostral linear nucleus (RLi)** — **rostral** — the rostral
    linear subdivision.

**They are SIBLING LINEAR NUCLEI** — **different structures at
different rostrocaudal levels**. Both are **serotonergic**, both
are **midline**, both are part of the **rostral raphe complex**.
Consumers must **not** conflate the two.

The Caudal Linear Nucleus / Ventral Tegmental Area Boundary
-----------------------------------------------------------
This is the **midline / paired** dopaminergic nucleus boundary:

*   **Caudal linear nucleus** (this module) — **midline** —
    **primarily serotonergic**, **secondarily dopaminergic** (A10
    subset) — **ventral tegmentum**, near the interpeduncular
    fossa.

*   **Ventral tegmental area (VTA)**
    (``.../tegmentum/left/ventral_tegmental_area/`` and the right
    counterpart) — **PAIRED** — **primarily dopaminergic** —
    the **mesolimbic / mesocortical** reward pathways.

**The CLi is MIDLINE; the VTA is PAIRED.** **The CLi is primarily
SEROTONERGIC; the VTA is primarily DOPAMINERGIC.** **Different
structures** — **different laterality**, **different primary
transmitter**, **different projections**. Consumers must **not**
conflate the CLi with the VTA — even though the CLi is sometimes
grouped with the VTA in the **A10 dopaminergic cell group**, the
**CLi's dopaminergic component is a subset** of a
**primarily serotonergic** nucleus.

The Caudal Linear Nucleus / Substantia Nigra Boundary
-----------------------------------------------------
This is the **midline / paired** dopaminergic/GABAergic nucleus
boundary:

*   **Caudal linear nucleus** (this module) — **midline** —
    **serotonergic** (majority) and **dopaminergic** (subset).

*   **Substantia nigra (SN)**
    (``.../tegmentum/left/substantia_nigra/`` and the right
    counterpart) — **PAIRED** — **pars compacta**
    (**dopaminergic**; the nigrostriatal input to the basal
    ganglia) and **pars reticulata** (**GABAergic**; the
    nigrotectal inhibitory gate).

**Different structures** in **different positions** and **different
functional systems**. Consumers must **not** conflate the CLi with
the SN.

The Caudal Linear Nucleus / Periaqueductal Gray Boundary
--------------------------------------------------------
This is the **ventral tegmentum / periaqueductal** boundary:

*   **Caudal linear nucleus** (this module) — **ventral tegmentum**
    — **ventral** to the PAG — near the **interpeduncular fossa**.

*   **Periaqueductal gray (PAG)**
    (``.../tegmentum/left/periaqueductal_gray/`` and the right
    counterpart — or the midline PAG, depending on the on-disk
    tree) — **surrounds** the **cerebral aqueduct** — **dorsal**
    to the CLi — **pain modulation** and **defensive behavior**.

**They are DIFFERENT STRUCTURES in DIFFERENT positions** — the
**PAG** surrounds the aqueduct; the **CLi** is in the ventral
tegmentum. Consumers must **not** conflate the CLi with the PAG.

The Caudal Linear Nucleus / Medullary Raphe Nuclei Boundary
-----------------------------------------------------------
This is the **ascending (midbrain) / descending (medullary)**
serotonergic boundary:

*   **Caudal linear nucleus** (this module) — **midbrain** —
    **ascending** serotonergic system.

*   **Raphe magnus**, **raphe pallidus**, and **raphe obscurus**
    (``.../hindbrain/myencephalon/medulla_oblongata/``) —
    **medulla** — **descending** serotonergic system — the
    **raphe magnus** is the **key descending pain-modulation
    nucleus**.

**Different structures at different levels** — the **CLi is
midbrain**; the **medullary raphe nuclei are medulla**. The **CLi
is ascending**; the **medullary raphe nuclei are descending**.
Consumers must **not** conflate the CLi with any medullary raphe
nucleus.

Function in the Human Brain
---------------------------
The caudal linear nucleus's function is **serotonergic and
dopaminergic neuromodulation** — **NOT** a sensory relay, **NOT** a
motor nucleus, **NOT** a premotor pool, **NOT** a sensorimotor
integration structure, **NOT** a conduction pathway:

*   **Ascending Serotonergic Modulation (majority of CLi neurons):**
    The CLi's **serotonergic neurons** project to the **forebrain**
    (cortex, limbic system, striatum) and the **diencephalon**
    (hypothalamus, thalamus) — contributing to the **ascending
    serotonergic system** — **modulating mood, anxiety, sleep,
    appetite, cognition, and reward**.

*   **Mesolimbic / Mesocortical Dopaminergic Modulation (a subset
    of CLi neurons):** The CLi's **dopaminergic neurons** (A10
    subset) project to the **limbic system** and the **striatum**
    — contributing to the **mesolimbic / mesocortical dopaminergic
    system** — **modulating reward, motivation, and
    reinforcement**.

*   **NOT a sensory relay.** The CLi does **not** transduce or
    relay a specific sensory modality.

*   **NOT a motor nucleus.** The CLi does **not** drive muscle.

*   **NOT a premotor pool.** The CLi does **not** transform motor
    commands.

*   **NOT a sensorimotor integration structure.** The CLi does
    **not** integrate sensory input into a behavioral command.

*   **NOT a conduction pathway.** The CLi is **grey matter** — a
    nucleus — **not white matter**.

*   **NOT an oscillator.** The CLi is a **modulatory nucleus** —
    it does **not** generate a rhythm. **Neuromodulatory nuclei
    carry NO coupling warning** — same rule as every non-oscillator
    class.

**The unifying theme:** the CLi is a **midline serotonergic and
dopaminergic neuromodulatory nucleus** in the **ventral midbrain
tegmentum** — a **smaller** contributor to the **ascending
serotonergic system** and the **mesolimbic / mesocortical
dopaminergic system** — **one node** in the **rostral raphe
complex**. It is a **new structure class** in the family
(**neuromodulatory nucleus**) and the **first midline leaf**. It
carries **NO coupling warning** — same rule as every
non-oscillator class.

Associated Disorders
--------------------
The caudal linear nucleus has **no named syndrome of its own** — its
clinical associations are **indirect**, via its **distributed
serotonergic and dopaminergic projections** — and they are **shared**
with the **larger serotonergic and dopaminergic nuclei** (the
**dorsal raphe**, the **median raphe**, and the **VTA**), which are
the **primary** clinical substrates in each case:

*   **Mood Disorders (INDIRECT — the DR and MnR are the primary
    serotonergic substrates):** **Major depressive disorder**,
    **anxiety disorders**, **obsessive-compulsive disorder**, and
    **panic disorder** are **associated** with **dysregulation of
    the serotonergic system** — the **DR** (cortical and limbic
    projections) and the **MnR** (hippocampal and septal
    projections) are the **primary** nuclei in each case. **The
    CLi is a SMALLER contributor** — **one node** in the
    **serotonergic system**. **SSRIs** (selective serotonin
    reuptake inhibitors) act on the **whole serotonergic system**
    — **not on the CLi specifically**.

*   **Addiction (INDIRECT — the VTA is the primary dopaminergic
    substrate):** **Substance use disorders** are **associated**
    with **dysregulation of the mesolimbic / mesocortical
    dopaminergic system** — the **VTA** (the primary dopaminergic
    nucleus of the reward system) is the **primary** substrate.
    **The CLi's dopaminergic subset is a SMALLER contributor** —
    **one node** in the **A10 dopaminergic group**.

*   **Sleep and Circadian Regulation (INDIRECT — the DR and MnR
    are the primary serotonergic substrates):** **Serotonin**
    **modulates sleep** (especially **slow-wave sleep** and
    **REM sleep**) — the **DR** (dorsal raphe) and the **MnR**
    (median raphe) are the **primary** serotonergic nuclei in
    sleep regulation. **The CLi is a SMALLER contributor.**

*   **Pain Modulation (NOT the CLi — the RAPHE MAGNUS is the
    primary substrate):** **Descending pain modulation** is
    mediated by the **raphe magnus** (medulla) — the **key
    descending serotonergic nucleus** — and the **PAG**. **The
    CLi is an ASCENDING nucleus** — it does **not** participate
    in **descending pain modulation**. **The raphe magnus, not
    the CLi, is the pain-modulation raphe nucleus.**

*   **No Named "Caudal Linear Nucleus Syndrome":** The CLi is a
    **small modulatory nucleus** — its **isolated lesion** produces
    **no named clinical syndrome**. Its clinical relevance is
    **indirect**, via its **distributed serotonergic and
    dopaminergic projections** — and the **primary** clinical
    substrates are the **DR**, the **MnR**, and the **VTA**, not
    the **CLi**. **No named CLi syndrome exists.**

**What is NOT here:** The CLi is **not** the substrate for **major
depressive disorder** (the **DR** and the **MnR** are the primary
serotonergic substrates — **NOT** the CLi), **anxiety disorders**
(the **DR** and the **MnR** — **NOT** the CLi), **obsessive-
compulsive disorder** (the **DR** and the **cortico-striatal
circuits** — **NOT** the CLi), **schizophrenia** (a complex
polygenic disorder — **NOT** any single nucleus), **addiction**
(the **VTA** is the primary dopaminergic node — **NOT** the CLi),
**Parkinson's disease** (the **substantia nigra pars compacta** —
**NOT** the CLi), **sleep disorders** (the **DR** and the
**MnR** — **NOT** the CLi), **descending pain modulation**
(the **raphe magnus** and the **PAG** — **NOT** the CLi),
**saccade disorders** (the **SC**, the **SNr**, the **riMLF** —
**NOT** the CLi), **pupillary light reflex deficits** (the
**pretectum** and the **EW nucleus** — **NOT** the CLi),
**oculomotor palsy** (the **CN III nucleus** or its fascicles —
**NOT** the CLi), **trochlear palsy** (the **CN IV nucleus** —
**NOT** the CLi), **trigeminal sensory deficits** (the
**trigeminal ganglion**, the **main sensory**, and the **spinal
trigeminal nucleus** — **NOT** the CLi), **CCHS** (RTN), **OIRD**
(pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger
complex + arcuate nucleus), **essential hypertension /
sympathetic overactivity** (C1 group / RVLM), **Huntington's
disease** (striatum — telencephalon), or **Kluver-Bucy syndrome**
(amygdala). Its clinical relevance is **indirect**, via its
**distributed serotonergic and dopaminergic projections** — the
**DR**, the **MnR**, and the **VTA** are the **primary**
substrates. **No named caudal linear nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **caudal linear nucleus** leaf — the **first MIDLINE
leaf** in the family. The CLi is **midline**, **not paired** — it
has **no left/right pair** and **no mirror leaf**. **The midline
position is the structural expression of its modulatory function**
— a **distributed modulator** that **reaches both sides** does not
need a left/right pair; it needs a **midline nucleus** whose
projections **fan out bilaterally**. **No coupling warning** — the
same rule as every non-oscillator class.

*   **Midline Nucleus — NOT Paired:** The CLi is a **single midline
    leaf** directly under ``tegmentum/`` — **NOT** under
    ``tegmentum/left/`` or ``tegmentum/right/``. It has **no
    left/right pair**, **no mirror leaf**, **no bilateral
    iteration**.

*   **Midline Position = Modulatory Function:** The CLi is a
    **serotonergic and dopaminergic neuromodulator** — it
    **modulates both sides** via its **distributed projections**,
    **not** via intrinsic left-right coupling. **The midline
    position is the structural fact** — a **distributed
    modulator** has a **midline nucleus** whose projections
    **fan out bilaterally** to its targets on both sides.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to MODULATORY NUCLEI):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **CLi** is a **modulatory nucleus** — a
    **single midline leaf** — it does **not** generate a rhythm,
    so it does **not** carry the **oscillator coupling warning**.
    There are **no "two sides" to couple** — the CLi is **one
    midline nucleus** whose **distributed projections** carry its
    modulation to **both sides**. **Neuromodulatory nuclei carry
    NO coupling warning** — same rule as every non-oscillator
    class.

*   **No SLEA Warning:** The CLi is **SLEA-free** — it is **not**
    an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The CLi is **not**
    part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The CLi is **not** a
    rhinencephalon structure.

**The CLi is the FIRST midline leaf in the family** — its
**midline position**, **modulatory class**, and **no coupling
warning** establish a **new structural pattern** that future
midline modulatory nuclei (the **dorsal raphe**, the **rostral
linear nucleus**, the **locus coeruleus** if represented as
midline, and the **medullary raphe nuclei**) will inherit. See
*The First Midline Tegmentum Leaf*.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The CLi is **midline** — there
    is **no** other hemisphere to import from.
*   **No cross-lobe imports.** This module does **not** import from
    the **PAG**, the **VTA**, the **substantia nigra**, the
    **dorsal raphe**, the **median raphe**, the **rostral linear
    nucleus**, the **medullary raphe nuclei**, the **cerebral
    aqueduct**, or any other container. The CLi's relationships to
    the PAG, the VTA, the substantia nigra, the dorsal raphe, the
    median raphe, the rostral linear nucleus, the medullary raphe
    nuclei, and the cerebral aqueduct are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **serotonergic phenotype** (tryptophan hydroxylase, 5-HT
    synthesis, serotonin transporters, serotonin receptors) and
    the **dopaminergic phenotype** (tyrosine hydroxylase, dopamine
    synthesis, dopamine transporters, dopamine receptors) are
    **``chemicals_hormones``-layer facts** — documented as
    **prose**, **never imported**. **CHEMICALS-LAYER DISCIPLINE**
    is preserved.
*   **MIDLINE LEAF — NOT PAIRED.** The CLi is a **single leaf**
    directly under ``tegmentum/`` — **NOT** under
    ``tegmentum/left/`` or ``tegmentum/right/``. It is the **first
    midline tegmentum leaf** — it **establishes the midline
    exception** to the tegmentum container's paired-leaf rule.
*   **MIDLINE EXCEPTION.** The tegmentum container's **paired-leaf
    rule** has **exceptions for midline nuclei**. The **CLi is the
    first exception**. The **PAG** (if represented as midline) and
    the **midbrain reticular formation** (if represented as
    midline) may also be **midline** — depending on the on-disk
    tree.
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER.** The tegmentum
    container's aggregation rule — *"each tegmentum nucleus is a
    paired structure (a ``left/`` leaf and a ``right/`` leaf)"* —
    should be **AMENDED** to state that **midline nuclei are
    permitted** as **direct children** of ``tegmentum/`` — **not
    required** to be under ``left/`` or ``right/``. The **CLi is
    the first** midline leaf; the amendment is a **follow-up**.
*   **LIVE AMENDMENT TO THE MIDBRAIN CONTAINER.** The midbrain
    container's prose — *"the cerebral aqueduct and the
    periaqueductal gray are midline structures, not paired"* —
    and the tegmentum container's paired-leaf rule — *"the PAG is
    midline-adjacent but is treated as paired in the tree"* — are
    **inconsistent with each other**. The **CLi is a clean new
    data point**: the tegmentum container has at least **one
    confirmed midline leaf**. **Both containers should be
    reconciled** to accommodate **midline leaves**. The CLi is the
    **first** such leaf; the reconciliation is a **follow-up
    amendment**.
*   **NEUROMODULATORY NUCLEUS — a NEW structure class.** The CLi is
    a **neuromodulatory nucleus** — the **same class** as the
    **locus coeruleus** (noradrenergic), the **dorsal raphe**
    (serotonergic), the **median raphe** (serotonergic), and the
    **VTA** (dopaminergic). It is **NOT** an oscillator, **NOT** a
    premotor pool, **NOT** a motor nucleus, **NOT** a sensory
    relay, **NOT** a sensorimotor integration structure, and
    **NOT** a conduction pathway. It **modulates the excitability
    of its targets** via **volume transmission** of serotonin (and
    dopamine).
*   **NO COUPLING WARNING — neuromodulatory nuclei carry NO
    coupling warning.** The CLi is a **single midline leaf** — a
    **midline modulatory nucleus** — it does **not** generate a
    rhythm. **The midline position is not a coupling hazard** —
    it is the structural fact of a **distributed modulator** that
    **reaches both sides** via its **projections**, not via
    intrinsic left-right coupling (there are no "two sides" to
    couple).
*   **NOT A CN NUCLEUS.** The CLi is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. The **four CN nuclei** in the
    tegmentum are cross-listed; the **CLi is not**. It has **one
    path only**.
*   **NOT the dorsal raphe nucleus — the DR is a SIBLING midline
    raphe nucleus.** Different structures, different locations,
    different projections. **The DR is the primary serotonergic
    nucleus** in most clinical discussions; the **CLi is a
    smaller, caudal contributor**.
*   **NOT the median raphe nucleus — the MnR is a PONTINE raphe
    nucleus.** Different levels — the **MnR is pons**, the **CLi
    is midbrain**.
*   **NOT the rostral linear nucleus — the RLi is ROSTRAL to the
    CLi.** Sibling linear nuclei, different rostrocaudal levels.
*   **NOT the VTA — the VTA is a PAIRED dopaminergic nucleus.** The
    **CLi is midline**; the **VTA is paired**. The **CLi's
    dopaminergic subset is part of the A10 group** with the VTA —
    but the **CLi is primarily serotonergic**.
*   **NOT the substantia nigra — the SN is a PAIRED
    dopaminergic/GABAergic nucleus.** Different structures.
*   **NOT the PAG — the PAG surrounds the cerebral aqueduct.** The
    **CLi is ventral to the PAG** — in the ventral tegmentum.
*   **NOT the medullary raphe nuclei — those are MEDULLARY.**
    Different levels — the **CLi is midbrain**; the **raphe
    magnus, pallidus, and obscurus are medulla**.
*   **CHEMICALS-LAYER DISCIPLINE.** The **serotonergic** and
    **dopaminergic** phenotypes are **``chemicals_hormones``-layer
    facts** — documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The CLi is a
    **local midline leaf** under the tegmentum — no cross-listing.
*   **No nested cross-listing.** The CLi is a **single leaf**. It
    is **not** a container.
*   **The on-disk tree is authoritative.** If the tree represents
    the CLi as **midline** (single leaf), that is the path. If the
    tree represents the CLi as **paired** (a `left/` leaf and a
    `right/` leaf) — which would be a **structural anomaly** given
    the CLi's midline anatomy — the on-disk tree is authoritative
    but the **midline position is anatomically correct**; the tree
    should be **amended** to reflect the midline placement.

Usage
-----
Resolve the leaf by path (**one** path only — the CLi is **midline**,
**not** under `left/` or `right/`)::

    from infrastructure.brainparts.midbrain.tegmentum import caudal_linear_nucleus

Or by fully-qualified path string::

    path = "midbrain.tegmentum.caudal_linear_nucleus"

**Do not** assume the CLi is under ``tegmentum/left/`` or
``tegmentum/right/``. **It is MIDLINE** — a **single leaf** directly
under ``tegmentum/``. **It has no left/right pair** and **no mirror
leaf**. **The midbrain/tegmentum containers should be amended** to
accommodate the midline exception (see *Design Contract*).

**Do not** assume the CLi is a **cranial nerve nucleus**. It is
**not** a CN nucleus and is **NOT** cross-listed with
``cranial_nerve_nuclei/``. The **four CN nuclei** in the tegmentum
are cross-listed; the **CLi is not**.

**Do not** assume the CLi is the **dorsal raphe nucleus**. The
**DR** is a **larger**, **more dorsal**, **more rostral** midline
raphe nucleus — the **primary serotonergic nucleus** in most
clinical discussions. The **CLi is a smaller, caudal contributor**.

**Do not** assume the CLi is the **median raphe nucleus**. The
**MnR** is a **pons** structure — a **pontine** raphe nucleus —
**not** the midbrain CLi.

**Do not** assume the CLi is the **rostral linear nucleus**. The
**RLi** is **rostral** to the CLi — a **separate** midline raphe
nucleus. Both are part of the rostral raphe complex; they are
**different structures**.

**Do not** assume the CLi is the **VTA**. The **VTA** is a **PAIRED
dopaminergic nucleus** — **not midline**. The **CLi is midline and
primarily serotonergic** (its dopaminergic subset is a **smaller
contributor** to the A10 group).

**Do not** assume the CLi is the **substantia nigra**. The **SN**
is a **paired dopaminergic/GABAergic** nucleus — **not the CLi**.

**Do not** assume the CLi is the **PAG**. The **PAG** **surrounds**
the cerebral aqueduct — it is **dorsal** to the CLi. The **CLi is
ventral to the PAG** — in the ventral tegmentum.

**Do not** assume the CLi is a **medullary raphe nucleus**. The
**raphe magnus**, **raphe pallidus**, and **raphe obscurus** are
**medulla** — the **CLi is midbrain**. The **CLi is an ascending
raphe nucleus** — the **medullary raphe nuclei are descending**.

**Do not** import the **serotonergic phenotype** (tryptophan
hydroxylase, 5-HT, SERT, 5-HT receptors) or the **dopaminergic
phenotype** (tyrosine hydroxylase, DA, DAT, DA receptors) into the
midbrain structural layer. Both are **``chemicals_hormones``-layer
facts**.

**Do not** import a **coupling warning** into the CLi.
**Neuromodulatory nuclei carry NO coupling warning** — same rule as
every non-oscillator class. **The midline position is not a
coupling hazard** — it is the structural fact of a **distributed
modulator** that **reaches both sides** via its **projections**,
not via intrinsic left-right coupling.

**Do not** treat the CLi as a **paired structure**. It is a
**midline nucleus** — a **single leaf** — with **no left/right
pair** and **no mirror leaf**.

Iterating the caudal linear nucleus's (empty) children (recommended
consumer pattern)::

    CAUDAL_LINEAR_NUCLEUS_CHILDREN = ()
    # The caudal linear nucleus is a leaf. The serotonergic
    # subpopulation and the dopaminergic subpopulation (A10 subset)
    # are prose, not modules.

Bilateral iteration — **NOT APPLICABLE**::

    # The caudal linear nucleus is MIDLINE — it has NO left/right
    # pair. There is no bilateral iteration for the CLi. If you
    # find yourself writing:
    #
    #     for side in ("left", "right"):
    #         path = f"midbrain.tegmentum.{side}.caudal_linear_nucleus"
    #
    # — that is WRONG. The CLi is at:
    #
    #     midbrain.tegmentum.caudal_linear_nucleus
    #
    # — a single midline leaf.

Reaching the dorsal raphe nucleus (recommended consumer pattern —
the SIBLING MIDLINE raphe nucleus)::

    # The dorsal raphe nucleus (DR) is the SIBLING MIDLINE raphe
    # nucleus — larger, more dorsal, more rostral — the primary
    # serotonergic nucleus in most clinical discussions:
    #
    #   brainparts.midbrain.tegmentum.dorsal_raphe_nucleus
    #
    # The DR and the CLi are DIFFERENT midline raphe nuclei.
    # The DR is the primary serotonergic nucleus; the CLi is a
    # smaller, caudal contributor.

Reaching the median raphe nucleus (recommended consumer pattern —
the PONTINE raphe nucleus)::

    # The median raphe nucleus (MnR) is a PONS structure — the
    # pontine raphe nucleus — the primary serotonergic projection
    # to the hippocampus:
    #
    #   brainparts.hindbrain.metencephalon.pons.median_raphe_nucleus
    #
    # The MnR is PONS; the CLi is MIDBRAIN. Different levels.

Reaching the rostral linear nucleus (recommended consumer pattern —
the ROSTRAL sibling linear nucleus)::

    # The rostral linear nucleus (RLi) is ROSTRAL to the CLi —
    # a separate midline raphe nucleus:
    #
    #   brainparts.midbrain.tegmentum.rostral_linear_nucleus
    #
    # The RLi and the CLi are SIBLING LINEAR NUCLEI — different
    # rostrocaudal levels. Both serotonergic, both midline, both
    # part of the rostral raphe complex.

Reaching the VTA (recommended consumer pattern — the PAIRED
dopaminergic nucleus)::

    # The ventral tegmental area (VTA) is a PAIRED dopaminergic
    # nucleus — the mesolimbic / mesocortical reward pathways:
    #
    #   brainparts.midbrain.tegmentum.left.ventral_tegmental_area
    #   brainparts.midbrain.tegmentum.right.ventral_tegmental_area
    #
    # The VTA is PAIRED; the CLi is MIDLINE. The CLi's dopaminergic
    # subset is part of the A10 group WITH the VTA — but the CLi
    # is primarily serotonergic.

Reaching the substantia nigra (recommended consumer pattern — the
PAIRED dopaminergic/GABAergic nucleus)::

    # The substantia nigra (SN) is a PAIRED nucleus — pars compacta
    # (dopaminergic; nigrostriatal input) and pars reticulata
    # (GABAergic; nigrotectal gate):
    #
    #   brainparts.midbrain.tegmentum.left.substantia_nigra
    #   brainparts.midbrain.tegmentum.right.substantia_nigra
    #
    # The SN is PAIRED; the CLi is MIDLINE. Different structures.

Reaching the PAG (recommended consumer pattern — the
periaqueductal structure, DORSAL to the CLi)::

    # The periaqueductal gray (PAG) SURROUNDS the cerebral aqueduct
    # — it is DORSAL to the CLi — pain modulation and defensive
    # behavior:
    #
    #   brainparts.midbrain.tegmentum.left.periaqueductal_gray
    #   brainparts.midbrain.tegmentum.right.periaqueductal_gray
    #   (OR: brainparts.midbrain.tegmentum.periaqueductal_gray —
    #    depending on the on-disk tree)
    #
    # The PAG is DORSAL to the CLi. The PAG's laterality (midline
    # vs. paired) depends on the on-disk tree — see the tegmentum
    # container's amendment note.

Reaching the medullary raphe nuclei (recommended consumer pattern —
the DESCENDING serotonergic nuclei)::

    # The medullary raphe nuclei — raphe magnus, raphe pallidus,
    # raphe obscurus — are MEDULLARY — the descending serotonergic
    # system:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.raphe_magnus
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.raphe_pallidus
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.raphe_obscurus
    #
    # The medullary raphe nuclei are DESCENDING (pain modulation,
    # autonomic function, motor tone); the CLi is ASCENDING
    # (mood, anxiety, sleep, appetite, cognition, reward). Different
    # levels, different functional systems.

Subnuclear-organization detail (not wired — consult references)::

    # The caudal linear nucleus has NO classical subnuclear
    # organization. It has TWO functionally and neurochemically
    # distinct SUBPOPULATIONS — prose, not modules:
    #
    #   serotonergic neurons    -> the MAJORITY of the CLi's
    #                              neurons — TPH+, 5-HT+ — project
    #                              to the forebrain (cortex, limbic
    #                              system, striatum) and the
    #                              diencephalon (hypothalamus,
    #                              thalamus) — ascending serotonergic
    #                              system
    #   dopaminergic neurons    -> a SUBSET — TH+, DA+ — part of the
    #                              A10 dopaminergic cell group WITH
    #                              the VTA — project to the limbic
    #                              system and the striatum —
    #                              mesolimbic / mesocortical
    #                              dopaminergic system
    #
    # Both phenotypes are chemicals_hormones-layer facts — documented
    # as prose, never imported into the midbrain structural layer.
    #
    # Do not attempt to resolve these subpopulations as sub-paths of
    # the caudal linear nucleus — they are PROSE, not modules.

The rostral raphe complex — detail (not wired — consult
references)::

    # The caudal linear nucleus is part of the ROSTRAL RAPHE
    # COMPLEX — the ASCENDING serotonergic system:
    #
    #   dorsal raphe nucleus (DR)       -> LARGEST; forebrain,
    #                                       limbic, striatum,
    #                                       thalamus — mood,
    #                                       anxiety, sleep, appetite,
    #                                       cognition
    #   median raphe nucleus (MnR)      -> PONS; hippocampus, septum,
    #                                       hypothalamus — mood,
    #                                       anxiety, memory
    #   caudal linear nucleus (CLi)     -> SMALLER; forebrain,
    #                                       diencephalon, limbic —
    #                                       ONE NODE in the ascending
    #                                       serotonergic system
    #   rostral linear nucleus (RLi)    -> SMALLER; forebrain,
    #                                       limbic — rostral to the
    #                                       CLi
    #
    # The rostral raphe complex projects ASCENDING. The caudal raphe
    # complex (raphe magnus, pallidus, obscurus) is in the MEDULLA
    # and projects DESCENDING. The CLi is a SMALLER ascending raphe
    # nucleus — not the DR, not the MnR.
    #
    # Do not attempt to resolve the DR, the MnR, the RLi, or the
    # medullary raphe nuclei as sub-paths of the CLi — they are
    # DIFFERENT structures at DIFFERENT levels.

Neuromodulatory-class detail (not wired — consult references)::

    # The caudal linear nucleus is a NEUROMODULATORY NUCLEUS — the
    # SAME CLASS as:
    #
    #   locus coeruleus         -> NORADRENERGIC (NE) —
    #                               arousal, attention, stress
    #   dorsal raphe nucleus    -> SEROTONERGIC (5-HT) — mood,
    #                               anxiety, sleep, appetite
    #   median raphe nucleus    -> SEROTONERGIC (5-HT) — mood,
    #                               anxiety, memory
    #   ventral tegmental area  -> DOPAMINERGIC (DA) — reward,
    #                               motivation
    #   caudal linear nucleus   -> SEROTONERGIC + DOPAMINERGIC
    #                               (THIS LEAF) — ascending
    #                               modulation, smaller contributor
    #
    # Neuromodulatory nuclei modulate the EXCITABILITY of their
    # targets via VOLUME TRANSMISSION of a neuromodulator. They are
    # NOT sensory relays, NOT motor nuclei, NOT premotor pools, NOT
    # sensorimotor integration structures, NOT conduction pathways.
    # They carry NO coupling warning.
    #
    # The MIDLINE position is the structural expression of the
    # modulatory function — a distributed modulator that reaches
    # both sides does not need a left/right pair; it needs a midline
    # nucleus whose projections fan out bilaterally.

Clinical-pattern detail (not wired — consult references)::

    # The caudal linear nucleus is a SMALL modulatory nucleus — its
    # clinical associations are INDIRECT — shared with the LARGER
    # serotonergic and dopaminergic nuclei:
    #
    #   MOOD DISORDERS              -> the DR and MnR are the
    #     (depression, anxiety,        primary serotonergic
    #      OCD)                        substrates — the CLi is a
    #                                   SMALLER contributor; SSRIs
    #                                   act on the WHOLE serotonergic
    #                                   system
    #   ADDICTION                   -> the VTA is the primary
    #                                   dopaminergic substrate — the
    #                                   CLi's dopaminergic subset is a
    #                                   SMALLER contributor to the A10
    #                                   group
    #   SLEEP / CIRCADIAN           -> the DR and MnR are the
    #                                   primary serotonergic
    #                                   substrates — the CLi is a
    #                                   SMALLER contributor
    #   DESCENDING PAIN MODULATION  -> the RAPHE MAGNUS (medulla)
    #                                   and the PAG are the primary
    #                                   substrates — the CLi is
    #                                   ASCENDING, NOT descending
    #
    # No named "caudal linear nucleus syndrome" exists. The DR, the
    # MnR, and the VTA are the primary clinical substrates — the
    # CLi is a smaller, caudal contributor.
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # STRUCTURES.

References
----------
*   **Canonical raphe anatomy (human):** Hornung, J.P. (2003).
    "The human raphe nuclei and the serotonergic system." *Journal
    of Chemical Neuroanatomy* 26:331–343. (The human raphe nuclei
    — the rostral raphe complex (DR, MnR, CLi, RLi); the caudal
    raphe complex (raphe magnus, pallidus, obscurus); the
    serotonergic cell groups; the ascending and descending
    projections.)
*   **Serotonergic system:** Jacobs, B.L., Azmitia, E.C. (1992).
    "Structure and function of the brain serotonin system."
    *Physiological Reviews* 72:165–229. (The brain serotonergic
    system — the raphe nuclei, the ascending and descending
    projections, the behavioral functions of serotonin.)
*   **Rostral raphe complex — ascending projections:** Azmitia,
    E.C., Segal, M. (1978). "An autoradiographic analysis of the
    differential ascending projections of the dorsal and median
    raphe nuclei in the rat." *Journal of Comparative Neurology*
    179:641–667. (The ascending projections of the rostral raphe
    complex — the DR and MnR; the CLi's ascending projections
    overlap with the rostral raphe complex.)
*   **Caudal linear nucleus — serotonergic cells:** Halliday, G.M.,
    Törk, I. (1989). "Serotonin-like immunoreactive cells and
    fibres in the rat ventromedial mesencephalic tegmentum."
    *Brain Research Bulletin* 22:725–735. (The serotonergic cells
    of the ventromedial mesencephalic tegmentum — the CLi as a
    serotonergic nucleus of the rostral raphe complex.)
*   **Caudal linear nucleus — human:** Baker, K.G., Halliday, G.M.,
    Hornung, J.P., Geffen, L.B., Cotton, R.G., Törk, I. (1991).
    "Distribution, morphology and number of monoamine-synthesizing
    and substance P-containing neurons in the human dorsal raphe
    nucleus." *Neuroscience* 42:757–775. (The monoamine-synthesizing
    neurons of the human rostral raphe complex — the CLi and its
    serotonergic and dopaminergic subpopulations.)
*   **A10 dopaminergic cell group:** Dahlstroem, A., Fuxe, K.
    (1964). "Evidence for the existence of monoamine-containing
    neurons in the central nervous system. I. Demonstration of
    monoamines in the cell bodies of brain stem neurons." *Acta
    Physiologica Scandinavica* 62 (Suppl. 232):1–55. (The A10
    dopaminergic cell group — the VTA and the CLi's dopaminergic
    subset.)
*   **Monoamine cell groups — human:** Hökfelt, T., Johansson, O.,
    Goldstein, M. (1984). "Chemical anatomy of the brain."
    *Science* 225:1326–1334. (The monoamine cell groups —
    dopaminergic, noradrenergic, and serotonergic — and their
    brainstem nuclei.)
*   **Raphe nuclei — anatomy:** Törk, I. (1990). "Anatomy of the
    serotonergic system." *Annals of the New York Academy of
    Sciences* 600:9–34. (The anatomy of the serotonergic system —
    the raphe nuclei, the ascending and descending projections,
    the distribution of serotonergic fibers.)
*   **Serotonin receptors — distribution:** Pazos, A., Palacios,
    J.M. (1985). "Quantitative autoradiographic mapping of
    serotonin receptors in the rat brain. I. Serotonin-1
    receptors." *Brain Research* 346:205–230. (The distribution of
    serotonin receptors in the brain — the target fields of the
    ascending serotonergic system.)
*   **Raphe magnus — descending pain modulation (contrast —
    MEDULLARY, NOT the CLi):** Fields, H.L., Basbaum, A.I.
    (1978). "Brainstem control of spinal pain-transmission
    neurons." *Annual Review of Physiology* 40:217–248. (The
    raphe magnus and the descending pain-modulation system —
    contrast with the ascending CLi.)
*   **Dorsal raphe — the primary serotonergic nucleus (contrast —
    SIBLING, NOT the CLi):** Michelsen, K.A., Schmitz, C., Steinbusch,
    H.W.M. (2007). "The dorsal raphe nucleus — from silver stainings
    to a simplified subnuclear organization: review on the
    mesencephalic raphe nuclei." *Brain Research Reviews* 55:349–363.
    (The dorsal raphe nucleus — the primary serotonergic nucleus of
    the rostral raphe complex — contrast with the smaller, caudal
    CLi.)
*   **Median raphe — the pontine raphe nucleus (contrast — PONS,
    NOT the CLi):** Vertes, R.P., Crane, A.M. (1997). "Distribution,
    quantification and comparisons of serotonin-immunoreactive
    fibers in brain regions with different densities of the
    serotonin transporter." *Journal of Comparative Neurology*
    381:293–306. (The median raphe nucleus — the pontine raphe
    nucleus — contrast with the midbrain CLi.)
*   **SLEA (contrast — the CLi is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the caudal linear nucleus.)
*   NeuroNames — Caudal linear nucleus; FMA — Caudal linear
    nucleus.
"""