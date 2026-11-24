"""
infrastructure.brainparts.midbrain.tegmentum.dorsal_raphe_nucleus
================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        ├── caudal_linear_nucleus       (midline leaf; ALSO has
        │                                anomalous left/ and right/
        │                                tree-structural nodes)
        └── dorsal_raphe_nucleus       <-- THIS MODULE (MIDLINE
                                            LEAF — cleanly represented
                                            in the tree — NO left/ or
                                            right/ nodes)

**Primary synonym:** Dorsal raphe nucleus; **DR**; **DRN**; **nucleus
raphe dorsalis** (Latin); **nucleus dorsalis raphes**; **the dorsal
raphe**; **the superior central raphe nucleus** (in some older
literature — but this is also a synonym for the median raphe in
some sources; use with care).
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **midline** **serotonergic** nucleus — the **largest
serotonergic nucleus** in the brain — located in the **midbrain
tegmentum**, at the level of the **superior colliculus** and
extending rostrally into the **rostral midbrain** (near the
diencephalon-midbrain junction) and caudally to the level of the
**inferior colliculus**. It **surrounds the cerebral aqueduct's
ventral aspect** and sits **ventral to the PAG**. Its
**serotonergic phenotype** (tryptophan hydroxylase, 5-HT synthesis,
serotonin transporters, serotonin receptors) is a
**``chemicals_hormones``-layer fact** — see *Chemicals-Layer
Discipline*.
**Container status:** **This module is a LEAF**, **midline** — it
is **NOT** under ``tegmentum/left/`` or ``tegmentum/right/`` — it
sits **directly under** the tegmentum container. **It is the FIRST
cleanly-midline leaf in the tree** — the tree represents the DR
**exactly as its anatomy demands**: one midline nucleus, one leaf.
See *The Cleanest Midline Leaf in the Tree* — this is the
**evidence** that the CLi's `left/` and `right/` nodes should be
**removed** (Resolution B).
**Part of:** The **tegmentum** region container — as a **midline**
leaf. **The DR is NOT a cranial nerve nucleus** and is **NOT
cross-listed** with ``cranial_nerve_nuclei/`` — see *NOT a CN
Nucleus*.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — **midline**, **not** a side
container.
**Structural children:** **None.** This is a **leaf** module. The
**subnuclear organization** (dorsal, ventral, ventrolateral,
interfascicular, caudal) is documented as **prose**, not as
structural children. The **serotonergic subpopulation** (the
overwhelming majority of DR neurons) and the **small non-
serotonergic subpopulation** (a minority) are **prose**, not
structural children.
**Boundary status (MIDLINE LEAF — CLEANLY REPRESENTED — NO left/ or
right/ NODES):** **Boundary case — the dorsal raphe nucleus is a
MIDLINE LEAF, and the tree represents it CLEANLY** — **directly
under** ``tegmentum/`` — **NO** ``tegmentum/dorsal_raphe_nucleus/
left/`` and **NO** ``tegmentum/dorsal_raphe_nucleus/right/``.
**The DR is the FIRST cleanly-midline leaf in the tree.** It is a
**midline serotonergic nucleus** — the **largest serotonergic
nucleus** in the brain — and its midline position is the
**structural expression** of its **modulatory function**: it
**modulates both sides** via its **distributed projections**, **not**
via intrinsic left-right coupling. **The tree represents it
correctly** — as **one midline leaf** — and the DR's clean
representation is the **contrast case** to the caudal linear
nucleus (CLi), which the tree represents with **anomalous** `left/`
and `right/` nodes (see *The Cleanest Midline Leaf in the Tree*).
Consumers must **not** look for the DR under
``.../tegmentum/dorsal_raphe_nucleus/left/`` or
``.../tegmentum/dorsal_raphe_nucleus/right/`` — **those paths do
not exist**, and if they did, they would be **tree-structural
anomalies** of the kind the CLi's `left/` and `right/` modules flag.
See *The Cleanest Midline Leaf in the Tree* and *Design Contract*.
**Boundary status (THE CLEANEST MIDLINE LEAF — the CONTRAST CASE to
the CLi):** **Boundary case — the DR is the CLEANEST midline leaf in
the tree.** The **caudal linear nucleus (CLi)** is **also** a
midline nucleus, **but** the tree represents the CLi with
**anomalous** `left/` and `right/` nodes under
``.../caudal_linear_nucleus/``. The **CLi leaf**, the **CLi `left/`
module**, and the **CLi `right/` module** all **flag** this anomaly
and recommend **Resolution B** — **removing** the `left/` and
`right/` nodes so that the CLi is represented as a **single midline
leaf**, consistent with its anatomy. **The DR is the PROOF that the
tree can do this cleanly.** The DR path is
``.../tegmentum/dorsal_raphe_nucleus/`` — **one leaf**, **midline**,
**no sides**. **The DR path is the model that the CLi's path should
follow** (per Resolution B). **The DR is the clean case; the CLi is
the anomalous case; the tree should be amended so that the CLi
follows the DR's pattern.** See *The Cleanest Midline Leaf in the
Tree* and *Design Contract — Live amendment*.
**Boundary status (NOT a CN nucleus — NOT cross-listed with
``cranial_nerve_nuclei/``):** **Boundary case — the dorsal raphe
nucleus is NOT a cranial nerve nucleus.** It is a **serotonergic
neuromodulatory nucleus** — it is **not a CN nucleus** and is
**NOT cross-listed** with the ``cranial_nerve_nuclei/`` container.
The **four CN nuclei** in the tegmentum (oculomotor, trochlear,
Edinger-Westphal, mesencephalic trigeminal) are **cross-listed**
between ``tegmentum/`` and ``cranial_nerve_nuclei/`` — **the DR is
not one of them**. Consumers must **not** look for the DR under
``.../cranial_nerve_nuclei/`` — it has **one path only**:
``.../tegmentum/dorsal_raphe_nucleus/``.
**Boundary status (NOT the caudal linear nucleus — the CLi is a
SMALLER, MORE CAUDAL, VENTRAL raphe nucleus):** **Boundary case —
the dorsal raphe nucleus is NOT the caudal linear nucleus (CLi).**
The **CLi** (``.../tegmentum/caudal_linear_nucleus/``) is a
**smaller**, **more caudal** (inferior colliculus level), and
**more ventral** midline raphe nucleus — **primarily serotonergic**
with a **dopaminergic subset** (A10 group). **The DR is LARGER,
MORE DORSAL, and MORE ROSTRAL** — the **largest serotonergic
nucleus** in the brain. They are **sibling midline raphe nuclei** —
**different structures**, **different locations**, **different
projections** (the DR projects more strongly to the forebrain; the
CLi projects more strongly to the midbrain and the diencephalon),
**different clinical weights** (the DR is the **primary**
serotonergic substrate for mood disorders; the CLi is a **smaller,
caudal contributor**). Consumers must **not** conflate the DR with
the CLi. **The DR is the primary serotonergic nucleus; the CLi is a
smaller contributor.**
**Boundary status (NOT the median raphe nucleus — the MnR is a
PONTINE raphe nucleus):** **Boundary case — the dorsal raphe nucleus
is NOT the median raphe nucleus (MnR).** The **MnR**
(``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) is a
**pons** structure — the **pontine** median raphe — the
**primary serotonergic projection to the hippocampus**. **The DR is
midbrain.** They are **DIFFERENT STRUCTURES at DIFFERENT levels** —
the **MnR** is **rhombencephalic**; the **DR** is
**mesencephalic**. **The DR and the MnR are the two major
serotonergic nuclei of the rostral raphe complex** — but they are
**different structures at different levels**. Consumers must **not**
conflate the two.
**Boundary status (NOT the rostral linear nucleus — the RLi is a
SMALLER, MORE VENTRAL raphe nucleus):** **Boundary case — the dorsal
raphe nucleus is NOT the rostral linear nucleus (RLi).** The
**RLi** is a **smaller** midline raphe nucleus — **more ventral**
and **more rostral** than the CLi. **The DR is the LARGEST and the
most dorsal/rostral of the rostral raphe complex.** They are
**sibling midline raphe nuclei** — **different structures at
different positions**. Consumers must **not** conflate the DR with
the RLi.
**Boundary status (NOT the VTA — the VTA is a PAIRED dopaminergic
nucleus):** **Boundary case — the dorsal raphe nucleus is NOT the
ventral tegmental area (VTA).** The **VTA**
(``.../tegmentum/left/ventral_tegmental_area/`` and the right
counterpart) is a **PAIRED dopaminergic nucleus** — the
**mesolimbic / mesocortical** reward pathways. **The DR is MIDLINE
and primarily SEROTONERGIC.** **Different structures** —
**different laterality** (midline vs. paired), **different primary
transmitter** (serotonergic vs. dopaminergic), **different
projections**, **different clinical systems** (the DR is the
**mood/anxiety/sleep** nucleus; the VTA is the **reward/motivation**
nucleus). Consumers must **not** conflate the DR with the VTA.
**Boundary status (NOT the substantia nigra — the SN is a PAIRED
dopaminergic/GABAergic nucleus):** **Boundary case — the dorsal
raphe nucleus is NOT the substantia nigra (SN).** The **SN**
(``.../tegmentum/left/substantia_nigra/`` and the right
counterpart) is a **PAIRED nucleus** — with the **pars compacta**
(dopaminergic; the nigrostriatal input to the basal ganglia) and
the **pars reticulata** (GABAergic; the nigrotectal inhibitory
gate). **The DR is MIDLINE and primarily serotonergic.** **Different
structures** in **different positions** and **different functional
systems**. Consumers must **not** conflate the DR with the SN.
**Boundary status (NOT the periaqueductal gray — the PAG SURROUNDS
the cerebral aqueduct, and the DR is VENTRAL to the PAG):**
**Boundary case — the dorsal raphe nucleus is NOT the periaqueductal
gray (PAG).** The **PAG** (``.../tegmentum/left/periaqueductal_gray/``
and the right counterpart — or the midline PAG, depending on the
on-disk tree) is the **pain-modulation and defensive-behavior**
region — it **surrounds** the **cerebral aqueduct** — **dorsal**
to the DR. **The DR is VENTRAL to the PAG** — in the ventral
midbrain tegmentum, **surrounding the ventral aspect of the
cerebral aqueduct**. They are **DIFFERENT STRUCTURES in DIFFERENT
positions** — the **PAG** surrounds the aqueduct dorsally; the
**DR** is **ventral to the PAG**, around the aqueduct's ventral
aspect. **The DR projects TO the PAG** (contributing to the
**descending pain-modulation system**), but the **DR is not the
PAG**. Consumers must **not** conflate the DR with the PAG.
**Boundary status (NOT the locus coeruleus — the LC is a
NORADRENERGIC nucleus):** **Boundary case — the dorsal raphe
nucleus is NOT the locus coeruleus (LC).** The **LC**
(``.../hindbrain/metencephalon/pons/locus_coeruleus/``) is the
**noradrenergic** arousal/attention nucleus — **pons** — the
**primary noradrenergic nucleus** in the brain. **The DR is
serotonergic** and **midbrain**. **They are the two major
monoaminergic modulatory nuclei** of the brainstem — **the LC is
noradrenergic, the DR is serotonergic**. **Different transmitters,
different locations, different functional systems.** Consumers must
**not** conflate the DR with the LC.
**Boundary status (NOT the medullary raphe nuclei — those are
MEDULLARY and primarily DESCENDING):** **Boundary case — the dorsal
raphe nucleus is NOT the medullary raphe nuclei.** The **raphe
magnus**, **raphe pallidus**, and **raphe obscurus**
(``.../hindbrain/myencephalon/medulla_oblongata/``) are **medullary
raphe nuclei** — the **descending serotonergic system** — the
**raphe magnus** is the **key descending pain-modulation nucleus**.
**The DR is midbrain** and **primarily ascending**. They are
**DIFFERENT STRUCTURES at DIFFERENT levels** — the **medullary
raphe nuclei are medulla**; the **DR is midbrain**. The **DR is
ascending** (forebrain, limbic, striatum, thalamus — mood, anxiety,
sleep, appetite, cognition); the **medullary raphe nuclei are
descending** (pain modulation, autonomic function, motor tone).
Consumers must **not** conflate the DR with any medullary raphe
nucleus. **(The DR does have SOME descending projections — to the
PAG, the RVM, and the spinal cord — contributing to descending
pain modulation — but its PRIMARY projection is ascending.)**
**Boundary status (SEROTONERGIC — the phenotype is a
``chemicals_hormones``-layer fact):** **Boundary case — the dorsal
raphe nucleus is **serotonergic** (the overwhelming majority of its
neurons).** The **serotonergic phenotype** (tryptophan hydroxylase,
5-HT synthesis, serotonin transporters, serotonin receptors) is a
**``chemicals_hormones``-layer fact** — the **neurochemical**
fact, **not** a structural fact. It is documented as **prose** in
the leaf and **never imported** into the midbrain structural layer.
Dependency DAG unchanged: ``chemicals_hormones → memory →
brainparts``. Consumers must **not** import the **serotonergic**
phenotype into the midbrain structural layer. **The DR has a small
non-serotonergic subpopulation** (a minority — some GABAergic,
glutamatergic, and peptidergic neurons), but the **overwhelming
majority** of DR neurons are serotonergic — this is what makes the
DR **the largest serotonergic nucleus** in the brain. See
*Chemicals-Layer Discipline* and *Design Contract*.
**Boundary status (NEUROMODULATORY NUCLEUS — a NEW structure
class — NOT an oscillator, NOT a premotor pool, NOT a motor
nucleus, NOT a sensory relay, NOT a conduction pathway):**
**Boundary case — the dorsal raphe nucleus is a NEUROMODULATORY
NUCLEUS.** In the family's **structure-class taxonomy**, it is a
**neuromodulatory nucleus** — the **same class** as the **locus
coeruleus** (noradrenergic), the **median raphe** (serotonergic),
the **caudal linear nucleus** (serotonergic + dopaminergic subset),
and the **VTA** (dopaminergic). It is **not** an **oscillator**,
**not** a **premotor pool**, **not** a **motor nucleus**, **not** a
**sensory relay**, **not** a **sensorimotor integration** structure,
and **not** a **conduction pathway**. **It modulates the
excitability of its targets** via **volume transmission** of
serotonin — that is its functional class. **The DR is the PRIMARY
serotonergic neuromodulatory nucleus in the brain** — the **largest
serotonergic nucleus** and the **principal target of SSRI
pharmacology**. **Neuromodulatory nuclei carry NO coupling
warning** — same rule as motor nuclei, premotor pools, sensor
nuclei, relay nuclei, sensorimotor integration structures, and
conduction pathways. Its **midline position** — **not paired** — is
the **structural expression** of its **modulatory, distributed**
function: it **does not have a left/right pair** because it
**modulates both sides**. See *Lateralization Notes* and *Design
Contract*.
**Boundary status (NO COUPLING WARNING — the DR is a MODULATORY
NUCLEUS):** **Boundary case — the dorsal raphe nucleus carries NO
coupling warning.** The **coupling warning** attaches to
**OSCILLATORS** (the pre-Bötzinger complex, the Bötzinger complex,
the pFRG) — and the **DR is not an oscillator**. **It is a midline
modulatory nucleus** — a **single leaf**, **not paired**.
**Neuromodulatory nuclei carry NO coupling warning** — same rule as
every non-oscillator class. The **midline position** is **not a
coupling hazard** — it is the **structural fact** of a
**distributed modulator** that **reaches both sides** via its
**projections**, **not** via intrinsic left-right coupling. There
are **no "two sides" to couple** — the DR is **one midline
nucleus**.

Overview
--------
The dorsal raphe nucleus (DR) is the **largest serotonergic nucleus
in the brain** — a **midline serotonergic neuromodulatory nucleus**
in the **midbrain tegmentum**, at the level of the **superior
colliculus** and extending rostrally and caudally, **surrounding the
ventral aspect of the cerebral aqueduct** and sitting **ventral to
the PAG**. It is the **principal serotonergic nucleus** of the
**rostral raphe complex** — the **primary** source of serotonergic
innervation to the **forebrain** (cortex, limbic system, striatum,
thalamus, hypothalamus) — and the **principal target of SSRI
pharmacology**. It is the **primary serotonergic substrate** for
**mood disorders**, **anxiety disorders**, **obsessive-compulsive
disorder**, **panic disorder**, and **REM sleep regulation**. It is
a **midline leaf** — the **first cleanly-midline leaf in the tree**
— with a **single path** under ``tegmentum/`` and **no `left/` or
`right/` nodes**. It is a **neuromodulatory nucleus** — the **same
class** as the locus coeruleus (noradrenergic), the median raphe
(serotonergic), the caudal linear nucleus (serotonergic +
dopaminergic subset), and the VTA (dopaminergic).

**The DR is a MIDLINE LEAF — CLEANLY REPRESENTED — NO left/ or
right/ nodes.** The tree represents the DR **exactly as its anatomy
demands**: **one midline nucleus, one leaf**, directly under
``tegmentum/``. **This is the FIRST cleanly-midline leaf in the
tree** — and it is the **contrast case** to the caudal linear
nucleus (CLi), which the tree represents with **anomalous** `left/`
and `right/` nodes. See *The Cleanest Midline Leaf in the Tree*.

**The DR is the PRIMARY serotonergic nucleus.** Where the CLi was a
**smaller, caudal contributor** to the ascending serotonergic
system, the **DR is the primary** — the **largest serotonergic
nucleus**, the **principal source of serotonergic forebrain
innervation**, and the **principal target of SSRI pharmacology**.
The **clinical framework** is therefore **inverted** from the
CLi's: the **CLi shared** the clinical associations **indirectly**
with the DR; the **DR owns** them. See *The DR in the Serotonergic
System*.

**The DR is NOT a CN nucleus.** It is a **serotonergic
neuromodulatory nucleus** — it is **not** cross-listed with
``cranial_nerve_nuclei/``. It has **one path only**.

**The DR is a NEUROMODULATORY NUCLEUS.** It **modulates the
excitability of its targets** via **volume transmission** of
serotonin. It is **not an oscillator**, **not a premotor pool**,
**not a motor nucleus**, **not a sensory relay**, **not a
sensorimotor integration** structure, and **not a conduction
pathway**.

**The DR carries NO coupling warning.** It is a **midline
modulatory nucleus** — a **single leaf**, **not paired**.
**Neuromodulatory nuclei carry NO coupling warning** — same rule as
every non-oscillator class.

The Cleanest Midline Leaf in the Tree
-------------------------------------
**The dorsal raphe nucleus is the FIRST cleanly-midline leaf in the
tree.** It is directly under ``tegmentum/`` — **no `left/`, no
`right/`** — and its **single midline path** is the **correct
representation** of a **midline nucleus**.

**The DR is the contrast case to the caudal linear nucleus (CLi).**
The **CLi is ALSO a midline nucleus**, **but** the tree represents
it with **anomalous** `left/` and `right/` nodes under
``.../caudal_linear_nucleus/``. The **CLi leaf**, the **CLi `left/`
module**, and the **CLi `right/` module** all **flag** the anomaly
and recommend **Resolution B** — **removing** the `left/` and
`right/` nodes so that the CLi is represented as a **single midline
leaf**, consistent with its anatomy. **The DR is the PROOF that
the tree can do this cleanly.** The DR path is
``.../tegmentum/dorsal_raphe_nucleus/`` — **one leaf**, **midline**,
**no sides**. **The DR path is the model that the CLi's path should
follow** (per Resolution B).

**The tree should be amended so that the CLi follows the DR's
pattern.** This is **Resolution B** — **remove** the CLi's `left/`
and `right/` nodes so that the CLi is a **single midline leaf**,
like the DR. **The DR is the clean case; the CLi is the anomalous
case; the tree should be amended so that the CLi follows the DR's
pattern.** See *Design Contract — Live amendment to the CLi's
representation*.

**The DR's clean representation is also evidence for the tegmentum
container amendment.** The tegmentum container's paired-leaf rule —
*"each tegmentum nucleus is a paired structure (a ``left/`` leaf and
a ``right/`` leaf)"* — was written **before** the CLi and the DR
were added. **The DR is a midline nucleus represented cleanly** —
**direct child of ``tegmentum/``, no `left/` or `right/`** — so the
paired-leaf rule **must be amended** to permit **midline nuclei**
as **direct children**, **not required** to be under `left/` or
`right/`. **The DR's clean representation is the model.** See
*Design Contract — Live amendment to the tegmentum container*.

Subnuclear Organization (prose, not structural children)
-------------------------------------------------------
The dorsal raphe nucleus has a **subnuclear organization** — the
DR is a **large, complex nucleus** with **distinct subnuclei** —
documented as **prose**, not as structural children. **The DR
subnuclei are ALL midline or midline-adjacent** — they are
**subdivisions of a single midline nucleus**, not a **left/right
pair**:

*   **Dorsal subnucleus (DRD)** — the **most dorsal** part —
    projects to the **cortex**, the **striatum**, and the
    **amygdala** — involved in **cortical arousal**, **motor
    control**, and **emotional processing**.

*   **Ventral subnucleus (DRV)** — the **ventral** part —
    projects to the **cortex**, the **thalamus**, and the
    **hypothalamus** — involved in **cortical arousal**,
    **sensory gating**, and **autonomic/endocrine regulation**.

*   **Ventrolateral subnucleus (DRVL)** — the **ventrolateral**
    part — projects to the **PAG**, the **brainstem**, and the
    **spinal cord** — involved in **pain modulation** and
    **autonomic control**.

*   **Interfascicular subnucleus (DRI)** — between the **MLF
    fascicles** — projects to the **PAG**, the **brainstem**, and
    the **hippocampus** — involved in **pain modulation** and
    **limbic processing**.

*   **Caudal subnucleus (DRC)** — the **caudal-most** part —
    projects to the **brainstem** and the **spinal cord** —
    involved in **descending pain modulation** and **autonomic
    control**.

**These subnuclei are prose, not structural children.** They are
**subdivisions of a single midline nucleus** — **not a left/right
pair**. The tree wires the **dorsal raphe nucleus** as a **single
leaf** under the tegmentum container (midline). Consumers must
**not** resolve ``.../dorsal_raphe_nucleus/dorsal_subnucleus`` — no
such path exists. **The DR subnuclei are midline subdivisions, not
left/right pairs** — a structural fact that **reinforces** the DR's
**midline-leaf** representation.

The DR in the Serotonergic System
---------------------------------
The **dorsal raphe nucleus** is the **primary serotonergic nucleus**
of the **rostral raphe complex** — the **ascending serotonergic
system**. The rostral raphe complex contains:

*   **Dorsal raphe nucleus (DR)** — **THIS LEAF** — the **largest**
    serotonergic nucleus — **primary** forebrain serotonergic
    innervation — **mood, anxiety, sleep, appetite, cognition**.

*   **Median raphe nucleus (MnR)**
    (``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) —
    **pons** — the **primary serotonergic projection to the
    hippocampus** — **mood, anxiety, memory**.

*   **Caudal linear nucleus (CLi)**
    (``.../tegmentum/caudal_linear_nucleus/``) — a **smaller**,
    **more caudal**, **more ventral** midline nucleus —
    **primarily serotonergic** with a **dopaminergic subset** —
    **ascending modulation, smaller contributor**.

*   **Rostral linear nucleus (RLi)**
    (``.../tegmentum/rostral_linear_nucleus/``) — a **smaller**
    midline nucleus — **rostral** to the CLi — **ascending
    modulation, smaller contributor**.

**The DR is the PRIMARY serotonergic nucleus** — the **largest**
serotonergic nucleus and the **principal target of SSRI
pharmacology**. Where the **CLi, the RLi, and the MnR** are
**smaller contributors** to the ascending serotonergic system, the
**DR is the primary**. **Most clinical associations of the
serotonergic system localize primarily to the DR** (or the DR + the
MnR collectively) — **NOT** to the CLi.

**The DR is ASCENDING — but it has SOME descending projections.**
The DR projects **ascending** to the forebrain (cortex, limbic
system, striatum, thalamus, hypothalamus) — the **primary**
serotonergic innervation. It **also** projects **descending** — to
the **PAG**, the **RVM** (rostral ventromedial medulla), and the
**spinal cord** — contributing to the **descending pain-modulation
system**. **The DR is primarily ascending**, with a **descending
component** — distinct from the **medullary raphe nuclei**, which
are **primarily descending**.

The DR's Place in the Neuromodulatory System
--------------------------------------------
The **dorsal raphe nucleus** is a **neuromodulatory nucleus** — the
**same class** as the **locus coeruleus** (noradrenergic), the
**median raphe** (serotonergic), the **caudal linear nucleus**
(serotonergic + dopaminergic subset), and the **VTA**
(dopaminergic). **Neuromodulatory nuclei** are a **distinct
structure class**:

*   **They are NOT sensory relays.** They do **not** transduce or
    relay a specific sensory modality. (The **IC** is a sensory
    relay; the **DR** is a modulator.)

*   **They are NOT motor nuclei.** They do **not** drive muscle.
    (The **CN III/IV nuclei** are motor nuclei; the **DR** is a
    modulator.)

*   **They are NOT premotor pools.** They do **not** transform
    motor commands. (The **PPRF**, the **riMLF**, and the
    **interstitial nucleus of Cajal** are premotor saccade
    generators; the **DR** is a modulator.)

*   **They are NOT sensorimotor integration structures.** They do
    **not** integrate sensory input into a behavioral command.
    (The **superior colliculus** is a sensorimotor integration
    structure; the **DR** is a modulator.)

*   **They are NOT conduction pathways.** They are **grey matter**
    — nuclei — **not white matter**. (The **tectobulbar tract**
    is a conduction pathway; the **DR** is a nucleus.)

*   **They MODULATE the excitability of their targets** via
    **volume transmission** of a **neuromodulator** — **serotonin**
    (for the raphe nuclei), **noradrenaline** (for the locus
    coeruleus), **dopamine** (for the VTA and the substantia nigra
    pars compacta). **The modulation is distributed and
    long-range** — it **sets the gain** of its target circuits,
    rather than **conveying a specific signal**.

**The DR is the PRIMARY serotonergic neuromodulatory nucleus** —
the **largest serotonergic nucleus** and the **principal target of
SSRI pharmacology**. **The class carries NO coupling warning** —
same rule as every non-oscillator class. **The midline position is
the structural expression of the modulatory function** — a
**distributed modulator** that **reaches both sides** does not
need a **left/right pair**; it needs a **midline nucleus** whose
projections **fan out bilaterally**. See *Lateralization Notes*.

The Dorsal Raphe Nucleus / Caudal Linear Nucleus Boundary
---------------------------------------------------------
This is the **sibling midline raphe nucleus** boundary — the **most
consequential** boundary in the leaf:

*   **Dorsal raphe nucleus** (this module) — the **largest**
    serotonergic nucleus — **primary** forebrain serotonergic
    innervation — **mood, anxiety, sleep, appetite, cognition** —
    **primary** target of SSRIs.

*   **Caudal linear nucleus (CLi)**
    (``.../tegmentum/caudal_linear_nucleus/``) — a **smaller**,
    **more caudal**, **more ventral** midline nucleus —
    **primarily serotonergic** with a **dopaminergic subset** (A10
    group) — **ascending modulation, smaller contributor**.

**They are SIBLING MIDLINE RAPHE NUCLEI** — **different
structures**, **different locations**, **different projections**
(the DR projects more strongly to the forebrain; the CLi projects
more strongly to the midbrain and the diencephalon), **different
clinical weights** (the DR is the **primary** serotonergic substrate
for mood disorders; the CLi is a **smaller, caudal contributor**).
Consumers must **not** conflate the DR with the CLi. **The DR is
the primary serotonergic nucleus; the CLi is a smaller contributor.**
See *The DR in the Serotonergic System*.

The Dorsal Raphe Nucleus / Median Raphe Nucleus Boundary
--------------------------------------------------------
This is the **midbrain / pons** raphe boundary — and the **two
major serotonergic nuclei** of the rostral raphe complex:

*   **Dorsal raphe nucleus** (this module) — **midbrain** —
    **primary forebrain serotonergic innervation**.

*   **Median raphe nucleus (MnR)**
    (``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) —
    **pons** — the **primary serotonergic projection to the
    hippocampus** — **mood, anxiety, memory**.

**The DR and the MnR are the TWO MAJOR serotonergic nuclei of the
rostral raphe complex.** **The DR is midbrain; the MnR is pons.**
**Different levels, different projections, complementary functions
in the serotonergic system.** Consumers must **not** conflate the
two. **The DR is the primary forebrain serotonergic nucleus; the
MnR is the primary hippocampal serotonergic nucleus.**

The Dorsal Raphe Nucleus / Rostral Linear Nucleus Boundary
----------------------------------------------------------
This is the **dorsal / ventral** and **larger / smaller** raphe
boundary:

*   **Dorsal raphe nucleus** (this module) — the **largest**,
    **most dorsal**, **most rostral** nucleus of the rostral raphe
    complex.

*   **Rostral linear nucleus (RLi)** — a **smaller** midline raphe
    nucleus — **more ventral** and **more rostral** — **ascending
    modulation, smaller contributor**.

**They are SIBLING MIDLINE RAPHE NUCLEI** — **different
structures** at **different positions**. Consumers must **not**
conflate the DR with the RLi.

The Dorsal Raphe Nucleus / Ventral Tegmental Area Boundary
----------------------------------------------------------
This is the **midline / paired** serotonergic vs. dopaminergic
nucleus boundary:

*   **Dorsal raphe nucleus** (this module) — **midline** —
    **primarily serotonergic**.

*   **Ventral tegmental area (VTA)**
    (``.../tegmentum/left/ventral_tegmental_area/`` and the right
    counterpart) — **PAIRED** — **primarily dopaminergic** — the
    **mesolimbic / mesocortical** reward pathways.

**The DR is MIDLINE; the VTA is PAIRED.** **The DR is primarily
SEROTONERGIC; the VTA is primarily DOPAMINERGIC.** **Different
structures** — **different laterality**, **different primary
transmitter**, **different projections**, **different clinical
systems** (the DR is the **mood/anxiety/sleep** nucleus; the VTA is
the **reward/motivation** nucleus). Consumers must **not** conflate
the DR with the VTA.

The Dorsal Raphe Nucleus / Substantia Nigra Boundary
----------------------------------------------------
This is the **midline / paired** serotonergic vs. dopaminergic /
GABAergic nucleus boundary:

*   **Dorsal raphe nucleus** (this module) — **midline** —
    **primarily serotonergic**.

*   **Substantia nigra (SN)**
    (``.../tegmentum/left/substantia_nigra/`` and the right
    counterpart) — **PAIRED** — **pars compacta** (dopaminergic;
    the nigrostriatal input to the basal ganglia) and **pars
    reticulata** (GABAergic; the nigrotectal inhibitory gate).

**Different structures** in **different positions** and **different
functional systems**. Consumers must **not** conflate the DR with
the SN.

The Dorsal Raphe Nucleus / Periaqueductal Gray Boundary
-------------------------------------------------------
This is the **ventral tegmentum / periaqueductal** boundary:

*   **Dorsal raphe nucleus** (this module) — **ventral midbrain
    tegmentum** — **ventral** to the PAG — **around the ventral
    aspect of the cerebral aqueduct**.

*   **Periaqueductal gray (PAG)**
    (``.../tegmentum/left/periaqueductal_gray/`` and the right
    counterpart — or the midline PAG, depending on the on-disk
    tree) — **surrounds** the **cerebral aqueduct** — **dorsal**
    to the DR — **pain modulation** and **defensive behavior**.

**They are DIFFERENT STRUCTURES in DIFFERENT positions** — the
**PAG** surrounds the aqueduct; the **DR** is **ventral to the
PAG**. **The DR projects TO the PAG** (contributing to the
**descending pain-modulation system**), but the **DR is not the
PAG**. Consumers must **not** conflate the DR with the PAG.

The Dorsal Raphe Nucleus / Locus Coeruleus Boundary
---------------------------------------------------
This is the **serotonergic / noradrenergic** modulatory nucleus
boundary — and the **two major monoaminergic modulatory nuclei** of
the brainstem:

*   **Dorsal raphe nucleus** (this module) — **midbrain** —
    **serotonergic** — **mood, anxiety, sleep, appetite,
    cognition**.

*   **Locus coeruleus (LC)**
    (``.../hindbrain/metencephalon/pons/locus_coeruleus/``) —
    **pons** — **noradrenergic** — **arousal, attention, stress**.

**The DR and the LC are the TWO MAJOR MONOAMINERGIC MODULATORY
NUCLEI of the brainstem.** **The DR is serotonergic; the LC is
noradrenergic.** **Different transmitters, different locations,
different functional systems.** Consumers must **not** conflate
the DR with the LC.

The Dorsal Raphe Nucleus / Medullary Raphe Nuclei Boundary
----------------------------------------------------------
This is the **ascending (midbrain) / descending (medullary)**
serotonergic boundary:

*   **Dorsal raphe nucleus** (this module) — **midbrain** —
    **primarily ascending** — **forebrain serotonergic
    innervation** — **mood, anxiety, sleep, appetite, cognition**.
    **(Some descending projections to the PAG, RVM, and spinal
    cord — contributing to descending pain modulation.)**

*   **Raphe magnus**, **raphe pallidus**, and **raphe obscurus**
    (``.../hindbrain/myencephalon/medulla_oblongata/``) —
    **medulla** — **primarily descending** — **pain modulation**
    (raphe magnus), **autonomic function**, **motor tone**.

**Different structures at different levels** — the **DR is
midbrain**; the **medullary raphe nuclei are medulla**. The **DR is
primarily ascending**; the **medullary raphe nuclei are primarily
descending**. Consumers must **not** conflate the DR with any
medullary raphe nucleus.

Function in the Human Brain
---------------------------
The dorsal raphe nucleus's function is **serotonergic
neuromodulation** — the **principal** serotonergic modulation of
the **forebrain** — **NOT** a sensory relay, **NOT** a motor
nucleus, **NOT** a premotor pool, **NOT** a sensorimotor
integration structure, **NOT** a conduction pathway:

*   **Ascending Serotonergic Modulation (the primary function):**
    The DR's **serotonergic neurons** project to the **forebrain**
    (cortex, limbic system, striatum, thalamus, hypothalamus) —
    the **principal** source of serotonergic innervation to the
    forebrain — **modulating mood, anxiety, sleep, appetite,
    cognition, and reward**.

*   **Mood Modulation (the primary clinical function):** The DR's
    projections to the **prefrontal cortex**, the **amygdala**, the
    **hippocampus**, and the **ventral striatum** modulate
    **emotional processing**, **threat detection**, **memory-
    emotion interaction**, and **reward processing** — the
    **primary serotonergic substrate** for **mood regulation**.
    **SSRIs** act on the **whole serotonergic system** but the
    **DR is the principal target**.

*   **Anxiety Modulation (the primary clinical function):** The
    DR's projections to the **amygdala**, the **bed nucleus of the
    stria terminalis** (BNST), and the **prefrontal cortex**
    modulate **fear** and **anxiety** — the **primary serotonergic
    substrate** for **anxiety regulation**.

*   **REM Sleep Regulation (the primary sleep function):** The DR's
    **serotonergic neurons** are **active during wakefulness** and
    **quiet during REM sleep** — the **REM-regulating
    serotonergic nucleus**. The **serotonergic system's** role in
    **REM sleep** is **primarily mediated by the DR** (with the
    **MnR** contributing to **non-REM** and **hippocampal**
    functions).

*   **Appetite and Feeding (the DR's serotonergic modulation):**
    The DR's projections to the **hypothalamus** modulate
    **appetite** and **feeding** — the **serotonergic regulation
    of food intake**. **(The serotonergic modulation of appetite
    is a distributed function — the DR is one contributor, along
    with the MnR and the hypothalamus.)**

*   **Descending Pain Modulation (a secondary function — the DR's
    descending projections):** The DR's **descending projections**
    — to the **PAG**, the **RVM**, and the **spinal cord** —
    contribute to the **descending pain-modulation system** —
    **the DR is one contributor** alongside the **PAG** and the
    **raphe magnus** (the **key descending pain-modulation
    nucleus**).

*   **NOT a sensory relay.** The DR does **not** transduce or
    relay a specific sensory modality.

*   **NOT a motor nucleus.** The DR does **not** drive muscle.

*   **NOT a premotor pool.** The DR does **not** transform motor
    commands.

*   **NOT a sensorimotor integration structure.** The DR does
    **not** integrate sensory input into a behavioral command.

*   **NOT a conduction pathway.** The DR is **grey matter** — a
    nucleus — **not white matter**.

*   **NOT an oscillator.** The DR is a **modulatory nucleus** —
    it does **not** generate a rhythm. **Neuromodulatory nuclei
    carry NO coupling warning** — same rule as every non-oscillator
    class.

**The unifying theme:** the DR is the **largest serotonergic
nucleus** in the brain — the **primary serotonergic
neuromodulatory nucleus** of the **forebrain** — a **midline
serotonergic nucleus** that **modulates both sides** via its
**distributed projections** and carries **NO coupling warning**.
It is the **primary serotonergic substrate** for **mood
disorders**, **anxiety disorders**, **obsessive-compulsive
disorder**, **panic disorder**, and **REM sleep regulation**. It
is a **midline leaf** — the **first cleanly-midline leaf in the
tree** — with a **single path** under ``tegmentum/`` and **no
`left/` or `right/` nodes**.

Associated Disorders
--------------------
The dorsal raphe nucleus has **no named syndrome of its own** — its
clinical associations are **direct** and **substantial**, via its
**principal serotonergic projections to the forebrain** — and it
is the **primary serotonergic substrate** for several major
clinical syndromes. **This is the inverted clinical framework from
the CLi's** — where the CLi **shared** the associations
**indirectly** with the DR, the **DR owns** them:

*   **Major Depressive Disorder (DIRECT — the DR is the PRIMARY
    serotonergic substrate):** **Major depressive disorder** is
    **associated** with **dysregulation of the serotonergic
    system** — the **DR** (cortical and limbic serotonergic
    projections) is the **primary** serotonergic nucleus in the
    disorder. **SSRIs** (selective serotonin reuptake inhibitors)
    act on the **whole serotonergic system** — but the **DR is
    the principal target**. **The dorsal raphe is the primary
    serotonergic nucleus in major depressive disorder.**

*   **Anxiety Disorders (DIRECT — the DR is a PRIMARY serotonergic
    substrate):** **Generalized anxiety disorder**, **social
    anxiety disorder**, **panic disorder**, and **obsessive-
    compulsive disorder** are **associated** with **dysregulation
    of the serotonergic system** — the **DR** (amygdala, BNST, and
    prefrontal cortex serotonergic projections) is a **primary**
    serotonergic nucleus. **SSRIs** are **first-line** treatments
    for these disorders — the **DR is a principal target**.

*   **Obsessive-Compulsive Disorder (DIRECT — the DR is a PRIMARY
    serotonergic substrate):** **OCD** is **associated** with
    **dysregulation of the cortico-striatal-thalamo-cortical
    circuits**, modulated by **serotonin** — the **DR** (striatal
    and prefrontal serotonergic projections) is a **primary**
    serotonergic nucleus. **SSRIs** are **first-line** treatments
    — the **DR is a principal target**.

*   **Sleep Disorders (DIRECT — the DR is the PRIMARY
    REM-regulating serotonergic nucleus):** The DR's **serotonergic
    neurons** are **active during wakefulness** and **quiet during
    REM sleep** — the **REM-regulating serotonergic nucleus**.
    **Insomnia**, **REM sleep behavior disorder**, and **other
    sleep disorders** can involve **serotonergic dysregulation** —
    the **DR is a primary contributor** (with the **MnR** for
    **non-REM**).

*   **Addiction (INDIRECT — the VTA is the primary dopaminergic
    substrate, the DR is a serotonergic modulator):** **Substance
    use disorders** are **primarily dopaminergic** (the **VTA**
    is the primary dopaminergic nucleus) — **but the DR's
    serotonergic projections modulate reward** and contribute to
    **addiction**. **The DR is a serotonergic modulator of
    addiction** — the **VTA is the primary dopaminergic
    substrate**.

*   **Pain (the DR is a CONTRIBUTOR — the raphe magnus and the PAG
    are the primary substrates):** **Descending pain modulation**
    is primarily mediated by the **raphe magnus** (medulla) and
    the **PAG** — **the DR contributes** via its **descending
    projections** to the **PAG** and the **RVM**. **The DR is a
    contributor** to descending pain modulation — the **raphe
    magnus is the key**.

*   **Sexual Dysfunction (DIRECT — SSRI-induced):** **SSRIs**
    produce **sexual dysfunction** via the **serotonergic
    system** — the **DR** is a **principal target**. **Sexual
    dysfunction** is one of the **most common** SSRI side
    effects — the **DR is a principal serotonergic
    substrate**.

*   **Nausea (INDIRECT — 5-HT3 receptors in the gut and area
    postrema):** **Nausea** is mediated by **5-HT3 receptors** in
    the **gut** and the **area postrema** (the **chemoreceptor
    trigger zone**) — **NOT primarily by the DR**. The **DR's
    serotonergic system** is **not the primary mediator** of
    **nausea** — **the gut and area postrema are**.
    **5-HT3 antagonists** (ondansetron) act on the **gut and
    area postrema** — **NOT on the DR**.

*   **No Named "Dorsal Raphe Nucleus Syndrome":** The DR is a
    **midline serotonergic modulatory nucleus** — it has **no
    named syndrome of its own** — but its **clinical associations
    are direct and substantial**: it is the **primary serotonergic
    substrate** for **major depressive disorder**, **anxiety
    disorders**, **obsessive-compulsive disorder**, and **sleep
    disorders** — and a **principal target** of **SSRI
    pharmacology**.

**What is NOT here:** The DR is **not** the substrate for **major
depressive disorder as a DR-EXCLUSIVE syndrome** (the DR is the
**primary** serotonergic substrate — but **depression is a
multifactorial disorder** involving **noradrenergic**,
**dopaminergic**, **glutamatergic**, **GABAergic**, and other
systems — **not a DR-exclusive syndrome**), **anxiety disorders as
DR-exclusive** (the **amygdala**, the **BNST**, the **prefrontal
cortex**, and **serotonergic** and **GABAergic** systems are
involved — the **DR is a primary serotonergic contributor**), **OCD
as DR-exclusive** (the **cortico-striatal-thalamo-cortical
circuits** are involved — the **DR is a primary serotonergic
modulator**), **schizophrenia** (a **complex polygenic disorder**
— **NOT** a single nucleus), **addiction as a DR-exclusive
syndrome** (the **VTA** is the primary dopaminergic substrate —
the **DR is a serotonergic modulator**), **Parkinson's disease**
(the **substantia nigra pars compacta** — **NOT** the DR),
**Alzheimer's disease** (the **nucleus basalis of Meynert**, the
**hippocampus**, the **cortex** — **NOT** the DR), **descending
pain modulation as a DR-exclusive function** (the **raphe magnus**
and the **PAG** are the primary substrates — the **DR is a
contributor**), **nausea as a DR function** (the **gut** and the
**area postrema** — **NOT** the DR), **saccade disorders** (the
**SC**, the **SNr**, the **riMLF** — **NOT** the DR), **pupillary
light reflex deficits** (the **pretectum** and the **EW nucleus**
— **NOT** the DR), **oculomotor palsy** (the **CN III nucleus** —
**NOT** the DR), **trochlear palsy** (the **CN IV nucleus** —
**NOT** the DR), **trigeminal sensory deficits** (the **trigeminal
ganglion**, the **main sensory**, and the **spinal trigeminal
nucleus** — **NOT** the DR), **CCHS** (RTN), **OIRD**
(pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger
complex + arcuate nucleus), **essential hypertension /
sympathetic overactivity** (C1 group / RVLM), **Huntington's
disease** (striatum — telencephalon), or **Kluver-Bucy syndrome**
(amygdala). Its clinical relevance is **direct and substantial** —
it is the **primary serotonergic substrate** for several major
disorders — but the disorders are **multifactorial**, and the
**DR is a primary serotonergic contributor**, not an **exclusive**
substrate. **No named "dorsal raphe nucleus syndrome" exists.**

Lateralization Notes
--------------------
This is the **dorsal raphe nucleus** leaf — the **first
cleanly-midline leaf in the tree**. The DR is **midline**, **not
paired** — it has **no left/right pair** and **no mirror leaf**.
**The tree represents it CLEANLY** — one midline leaf under
``tegmentum/``, **no `left/` or `right/` nodes**. **This is the
model that the CLi's path should follow** (per Resolution B). **No
coupling warning** — the same rule as every non-oscillator class.

*   **Midline Nucleus — NOT Paired:** The DR is a **single midline
    leaf** directly under ``tegmentum/`` — **NOT** under
    ``tegmentum/left/`` or ``tegmentum/right/``. It has **no
    left/right pair**, **no mirror leaf**, **no bilateral
    iteration**.

*   **Cleanly Represented in the Tree:** The DR is the **first
    cleanly-midline leaf** in the tree — the tree represents it
    **exactly as its anatomy demands**: one midline nucleus, one
    leaf. **This is the model that the CLi's path should follow**
    (per Resolution B — removing the CLi's `left/` and `right/`
    nodes). **The tree can do midline cleanly** — the DR is the
    proof.

*   **Midline Position = Modulatory Function:** The DR is a
    **serotonergic neuromodulator** — it **modulates both sides**
    via its **distributed projections**, **not** via intrinsic
    left-right coupling. **The midline position is the structural
    fact** — a **distributed modulator** has a **midline nucleus**
    whose projections **fan out bilaterally** to its targets on
    both sides.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to MODULATORY NUCLEI):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **DR** is a **modulatory nucleus** — a
    **single midline leaf** — it does **not** generate a rhythm,
    so it does **not** carry the **oscillator coupling warning**.
    There are **no "two sides" to couple** — the DR is **one
    midline nucleus** whose **distributed projections** carry its
    modulation to **both sides**. **Neuromodulatory nuclei carry
    NO coupling warning** — same rule as every non-oscillator
    class.

*   **No SLEA Warning:** The DR is **SLEA-free** — it is **not**
    an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The DR is **not** part
    of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The DR is **not** a
    rhinencephalon structure.

**The DR is the FIRST cleanly-midline leaf in the tree** — its
**midline position**, **modulatory class**, **clean representation
in the tree**, and **no coupling warning** establish the
**canonical structural pattern** for midline modulatory nuclei.
**The CLi is the anomalous case** — the tree represents the CLi
with `left/` and `right/` nodes, which its own modules flag as a
**tree-structural anomaly**. **The tree should be amended so that
the CLi follows the DR's clean pattern** (Resolution B). See *The
Cleanest Midline Leaf in the Tree*.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The DR is **midline** — there
    is **no** other hemisphere to import from.
*   **No cross-lobe imports.** This module does **not** import from
    the **PAG**, the **VTA**, the **substantia nigra**, the
    **caudal linear nucleus**, the **median raphe**, the **rostral
    linear nucleus**, the **medullary raphe nuclei**, the **locus
    coeruleus**, the **cerebral aqueduct**, or any other container.
    The DR's relationships to the PAG, the VTA, the substantia
    nigra, the CLi, the median raphe, the rostral linear nucleus,
    the medullary raphe nuclei, the locus coeruleus, and the
    cerebral aqueduct are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **serotonergic phenotype** (tryptophan hydroxylase, 5-HT
    synthesis, serotonin transporters, serotonin receptors) is a
    **``chemicals_hormones``-layer fact** — documented as
    **prose**, **never imported**. **CHEMICALS-LAYER DISCIPLINE**
    is preserved.
*   **MIDLINE LEAF — CLEANLY REPRESENTED.** The DR is a **single
    leaf** directly under ``tegmentum/`` — **NO** ``tegmentum/
    dorsal_raphe_nucleus/left/`` and **NO**
    ``tegmentum/dorsal_raphe_nucleus/right/``. **This is the
    FIRST cleanly-midline leaf in the tree** — the tree
    represents the DR **exactly as its anatomy demands**. **The
    DR path is the model that the CLi's path should follow** (per
    Resolution B — removing the CLi's `left/` and `right/`
    nodes).
*   **THE CLEANEST MIDLINE LEAF — the CONTRAST CASE to the CLi.**
    The **CLi** is **also** a midline nucleus, **but** the tree
    represents it with **anomalous** `left/` and `right/` nodes.
    **The CLi leaf, the CLi `left/` module, and the CLi `right/`
    module all flag the anomaly and recommend Resolution B** —
    **removing** the `left/` and `right/` nodes so that the CLi is
    represented as a **single midline leaf**, consistent with its
    anatomy. **The DR is the PROOF that the tree can do this
    cleanly.** The DR path is the model. The CLi path should
    follow it.
*   **LIVE AMENDMENT TO THE CLi's REPRESENTATION.** The CLi's
    `left/` and `right/` nodes should be **removed** (Resolution
    B) — following the DR's **clean midline-leaf pattern**. The
    CLi should be a **single midline leaf** under ``tegmentum/``,
    **no `left/` or `right/` nodes** — like the DR. **The DR is
    the canonical model** for a midline nucleus in the tree; the
    CLi's anomalous paired representation should be **amended** to
    follow it.
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER.** The tegmentum
    container's **paired-leaf rule** — *"each tegmentum nucleus is
    a paired structure (a ``left/`` leaf and a ``right/`` leaf)"*
    — should be **AMENDED** to state that **midline nuclei are
    permitted** as **direct children** of ``tegmentum/`` — **not
    required** to be under ``left/`` or ``right/``. The **DR is a
    midline nucleus represented cleanly** — **direct child of
    ``tegmentum/``, no `left/` or `right/`** — so the rule must
    be amended. **The DR's clean representation is the model.**
*   **LIVE AMENDMENT TO THE MIDBRAIN CONTAINER.** The midbrain
    container's prose — *"the cerebral aqueduct and the
    periaqueductal gray are midline structures, not paired"* —
    and the tegmentum container's paired-leaf rule — *"the PAG is
    midline-adjacent but is treated as paired in the tree"* — are
    **inconsistent with each other**. The **DR is another clean
    data point** — the tegmentum container **has at least two
    midline nuclei represented in the tree** (the DR cleanly, the
    CLi anomalously). **Both containers should be reconciled**
    to accommodate **midline leaves**. The **DR's clean
    representation is the model**; the **CLi's anomalous
    representation is the case to be amended**. See *The Cleanest
    Midline Leaf in the Tree*.
*   **NEUROMODULATORY NUCLEUS — a NEW structure class.** The DR is
    a **neuromodulatory nucleus** — the **same class** as the
    **locus coeruleus** (noradrenergic), the **median raphe**
    (serotonergic), the **caudal linear nucleus** (serotonergic +
    dopaminergic subset), and the **VTA** (dopaminergic). It is
    **NOT** an oscillator, **NOT** a premotor pool, **NOT** a
    motor nucleus, **NOT** a sensory relay, **NOT** a
    sensorimotor integration structure, and **NOT** a conduction
    pathway. It **modulates the excitability of its targets** via
    **volume transmission** of serotonin.
*   **NO COUPLING WARNING — neuromodulatory nuclei carry NO
    coupling warning.** The DR is a **single midline leaf** — a
    **midline modulatory nucleus** — it does **not** generate a
    rhythm. **The midline position is not a coupling hazard** —
    it is the structural fact of a **distributed modulator** that
    **reaches both sides** via its **projections**, not via
    intrinsic left-right coupling (there are no "two sides" to
    couple).
*   **NOT A CN NUCLEUS.** The DR is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. It has **one path only**.
*   **NOT the caudal linear nucleus — the CLi is a SMALLER, MORE
    CAUDAL, VENTRAL raphe nucleus.** The DR is **LARGER, MORE
    DORSAL, MORE ROSTRAL**. **The DR is the primary serotonergic
    nucleus; the CLi is a smaller contributor.**
*   **NOT the median raphe nucleus — the MnR is a PONTINE raphe
    nucleus.** Different levels — the **MnR is pons**, the **DR
    is midbrain**. **The DR and the MnR are the two major
    serotonergic nuclei of the rostral raphe complex.**
*   **NOT the rostral linear nucleus — the RLi is a SMALLER
    nucleus.** Sibling midline raphe nuclei.
*   **NOT the VTA — the VTA is a PAIRED dopaminergic nucleus.**
    The **DR is midline**; the **VTA is paired**. Different
    structures.
*   **NOT the substantia nigra — the SN is a PAIRED dopaminergic/
    GABAergic nucleus.**
*   **NOT the PAG — the PAG surrounds the cerebral aqueduct, and
    the DR is VENTRAL to the PAG.** The **DR projects to the
    PAG** for descending pain modulation.
*   **NOT the locus coeruleus — the LC is a NORADRENERGIC
    nucleus.** **The DR and the LC are the two major
    monoaminergic modulatory nuclei of the brainstem.**
*   **NOT the medullary raphe nuclei — those are MEDULLARY and
    primarily DESCENDING.** The **DR is midbrain and primarily
    ascending** (with some descending projections).
*   **CHEMICALS-LAYER DISCIPLINE.** The **serotonergic phenotype**
    is a **``chemicals_hormones``-layer fact** — documented as
    **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The DR is a
    **local midline leaf** under the tegmentum — no cross-listing.
*   **No nested cross-listing.** The DR is a **single leaf**. It
    is **not** a container.
*   **The on-disk tree is authoritative.** The on-disk tree has
    ``.../tegmentum/dorsal_raphe_nucleus/`` — **one leaf**,
    **midline**, **no `left/` or `right/`**. **This is the correct
    representation** — the DR is a midline nucleus, and the tree
    represents it cleanly. **The DR path is the model that the
    CLi's path should follow** (per Resolution B).

Usage
-----
Resolve the leaf by path (**one** path only — the DR is **midline**,
**not** under `left/` or `right/`)::

    from infrastructure.brainparts.midbrain.tegmentum import dorsal_raphe_nucleus

Or by fully-qualified path string::

    path = "midbrain.tegmentum.dorsal_raphe_nucleus"

**Do not** assume the DR is under ``tegmentum/dorsal_raphe_nucleus/
left/`` or ``tegmentum/dorsal_raphe_nucleus/right/``. **It is
MIDLINE** — a **single leaf** directly under ``tegmentum/``. **The
tree represents it cleanly.** **The DR path is the model that the
CLi's path should follow** (per Resolution B — removing the CLi's
`left/` and `right/` nodes).

**Do not** assume the DR is a **cranial nerve nucleus**. It is
**not** a CN nucleus and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the DR is the **caudal linear nucleus**. The
**CLi is a smaller, more caudal, more ventral midline raphe
nucleus** — **primarily serotonergic with a dopaminergic subset**.
**The DR is larger, more dorsal, more rostral** — **the largest
serotonergic nucleus in the brain**. **The DR is the primary
serotonergic nucleus; the CLi is a smaller contributor.**

**Do not** assume the DR is the **median raphe nucleus**. The
**MnR is a PONS** structure — a **pontine** raphe nucleus —
**not** the midbrain DR. **The DR and the MnR are the two major
serotonergic nuclei of the rostral raphe complex.**

**Do not** assume the DR is the **rostral linear nucleus**. The
**RLi is a smaller** midline raphe nucleus — **more ventral** and
**more rostral** than the CLi. **Sibling midline raphe nuclei.**

**Do not** assume the DR is the **VTA** or the **substantia
nigra**. Those are **PAIRED dopaminergic / GABAergic nuclei** —
**not midline**. **The DR is midline and serotonergic.**

**Do not** assume the DR is the **PAG**. The **PAG surrounds** the
cerebral aqueduct — it is **dorsal** to the DR. The **DR is
ventral to the PAG** — around the **ventral aspect** of the
cerebral aqueduct.

**Do not** assume the DR is the **locus coeruleus**. The **LC is a
NORADRENERGIC** nucleus — **pons** — **the two major monoaminergic
modulatory nuclei of the brainstem are the DR (serotonergic) and
the LC (noradrenergic)**. Different transmitters, different
locations, different functional systems.

**Do not** assume the DR is a **medullary raphe nucleus**. The
**raphe magnus**, **raphe pallidus**, and **raphe obscurus** are
**medulla** — the **DR is midbrain**. **The DR is primarily
ascending** (with some descending projections to the PAG, RVM, and
spinal cord); the **medullary raphe nuclei are primarily
descending**.

**Do not** import the **serotonergic phenotype** (tryptophan
hydroxylase, 5-HT, SERT, 5-HT receptors) into the midbrain
structural layer. It is a **``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the DR.
**Neuromodulatory nuclei carry NO coupling warning** — same rule as
every non-oscillator class. **The midline position is not a
coupling hazard.**

**Do not** treat the DR as a **paired structure**. It is a
**midline nucleus** — a **single leaf** — with **no left/right
pair** and **no mirror leaf**. **The tree represents it cleanly.**

Iterating the dorsal raphe nucleus's (empty) children (recommended
consumer pattern)::

    DORSAL_RAPHE_NUCLEUS_CHILDREN = ()
    # The dorsal raphe nucleus is a leaf. The subnuclear organization
    # (dorsal, ventral, ventrolateral, interfascicular, caudal) is
    # prose, not modules. The serotonergic subpopulation (majority)
    # and the small non-serotonergic subpopulation (minority) are
    # prose, not modules.

Bilateral iteration — **NOT APPLICABLE**::

    # The dorsal raphe nucleus is MIDLINE — it has NO left/right
    # pair. There is no bilateral iteration for the DR. If you find
    # yourself writing:
    #
    #     for side in ("left", "right"):
    #         path = f"midbrain.tegmentum.{side}.dorsal_raphe_nucleus"
    #
    # — that is WRONG. The DR is at:
    #
    #     midbrain.tegmentum.dorsal_raphe_nucleus
    #
    # — a single midline leaf. The tree represents the DR correctly.

Reaching the caudal linear nucleus (recommended consumer pattern —
the SIBLING MIDLINE raphe nucleus, SMALLER and MORE CAUDAL)::

    # The caudal linear nucleus (CLi) is the SIBLING MIDLINE raphe
    # nucleus — smaller, more caudal, more ventral — primarily
    # serotonergic with a dopaminergic subset (A10 group):
    #
    #   brainparts.midbrain.tegmentum.caudal_linear_nucleus
    #
    # NOTE: the CLi's tree representation is ANOMALOUS — it has
    # left/ and right/ nodes (see the CLi's own left/ and right/
    # modules). The DR is the CLEAN case; the CLi is the ANOMALOUS
    # case. The tree should be amended so that the CLi follows the
    # DR's clean pattern (Resolution B — remove the left/ and
    # right/ nodes).

Reaching the median raphe nucleus (recommended consumer pattern —
the PONTINE major raphe nucleus)::

    # The median raphe nucleus (MnR) is a PONS structure — the
    # pontine raphe nucleus — the primary serotonergic projection
    # to the hippocampus:
    #
    #   brainparts.hindbrain.metencephalon.pons.median_raphe_nucleus
    #
    # The MnR is PONS; the DR is MIDBRAIN. The DR and the MnR are
    # the TWO MAJOR serotonergic nuclei of the rostral raphe
    # complex.

Reaching the rostral linear nucleus (recommended consumer pattern —
the ROSTRAL sibling)::

    # The rostral linear nucleus (RLi) is a SMALLER midline raphe
    # nucleus — more ventral and more rostral than the CLi:
    #
    #   brainparts.midbrain.tegmentum.rostral_linear_nucleus
    #
    # The DR and the RLi are SIBLING midline raphe nuclei —
    # different positions.

Reaching the VTA (recommended consumer pattern — the PAIRED
dopaminergic nucleus)::

    # The ventral tegmental area (VTA) is a PAIRED dopaminergic
    # nucleus — the mesolimbic / mesocortical reward pathways:
    #
    #   brainparts.midbrain.tegmentum.left.ventral_tegmental_area
    #   brainparts.midbrain.tegmentum.right.ventral_tegmental_area
    #
    # The VTA is PAIRED; the DR is MIDLINE. The DR is primarily
    # serotonergic; the VTA is primarily dopaminergic.

Reaching the substantia nigra (recommended consumer pattern — the
PAIRED dopaminergic / GABAergic nucleus)::

    # The substantia nigra (SN) is a PAIRED nucleus — pars compacta
    # (dopaminergic; nigrostriatal input) and pars reticulata
    # (GABAergic; nigrotectal gate):
    #
    #   brainparts.midbrain.tegmentum.left.substantia_nigra
    #   brainparts.midbrain.tegmentum.right.substantia_nigra
    #
    # The SN is PAIRED; the DR is MIDLINE. Different structures.

Reaching the PAG (recommended consumer pattern — the
periaqueductal structure, DORSAL to the DR)::

    # The periaqueductal gray (PAG) SURROUNDS the cerebral aqueduct
    # — it is DORSAL to the DR — pain modulation and defensive
    # behavior:
    #
    #   brainparts.midbrain.tegmentum.left.periaqueductal_gray
    #   brainparts.midbrain.tegmentum.right.periaqueductal_gray
    #   (OR: brainparts.midbrain.tegmentum.periaqueductal_gray —
    #    depending on the on-disk tree)
    #
    # The PAG is DORSAL to the DR. The DR projects to the PAG for
    # descending pain modulation.

Reaching the locus coeruleus (recommended consumer pattern — the
NORADRENERGIC modulatory nucleus)::

    # The locus coeruleus (LC) is a NORADRENERGIC modulatory nucleus
    # — PONS — the two major monoaminergic modulatory nuclei of the
    # brainstem are the DR (serotonergic) and the LC
    # (noradrenergic):
    #
    #   brainparts.hindbrain.metencephalon.pons.locus_coeruleus
    #
    # The DR and the LC are the two major monoaminergic modulatory
    # nuclei. Different transmitters, different locations, different
    # functional systems.

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
    # The medullary raphe nuclei are primarily DESCENDING; the DR
    # is primarily ASCENDING (with some descending projections).

Subnuclear-organization detail (not wired — consult references)::

    # The dorsal raphe nucleus has a SUBNUCLEAR organization —
    # subdivisions of a single midline nucleus:
    #
    #   dorsal subnucleus (DRD)     -> most dorsal — cortex,
    #                                   striatum, amygdala — cortical
    #                                   arousal, motor control,
    #                                   emotional processing
    #   ventral subnucleus (DRV)    -> ventral — cortex, thalamus,
    #                                   hypothalamus — cortical arousal,
    #                                   sensory gating, autonomic/
    #                                   endocrine regulation
    #   ventrolateral subnucleus    -> ventrolateral — PAG,
    #     (DRVL)                        brainstem, spinal cord — pain
    #                                   modulation, autonomic control
    #   interfascicular subnucleus  -> between the MLF fascicles —
    #     (DRI)                         PAG, brainstem, hippocampus —
    #                                   pain modulation, limbic
    #                                   processing
    #   caudal subnucleus (DRC)     -> caudal-most — brainstem,
    #                                   spinal cord — descending pain
    #                                   modulation, autonomic control
    #
    # ALL of these subnuclei are MIDLINE or MIDLINE-ADJACENT — they
    # are SUBDIVISIONS of a single midline nucleus, NOT a
    # left/right pair. The DR's subnuclear organization REINFORCES
    # its midline-leaf representation.
    #
    # Do not attempt to resolve these subnuclei as sub-paths of the
    # dorsal raphe nucleus — they are PROSE, not modules.

The serotonergic system — detail (not wired — consult references)::

    # The dorsal raphe nucleus is the PRIMARY serotonergic nucleus
    # of the rostral raphe complex:
    #
    #   dorsal raphe nucleus (DR)   -> LARGEST; forebrain, limbic,
    #                                   striatum, thalamus, amygdala
    #                                   — mood, anxiety, sleep,
    #                                   appetite, cognition — PRIMARY
    #                                   target of SSRIs
    #   median raphe nucleus (MnR)  -> PONS; hippocampus, septum,
    #                                   hypothalamus — mood, anxiety,
    #                                   memory
    #   caudal linear nucleus (CLi) -> SMALLER; forebrain,
    #                                   diencephalon, limbic — ONE
    #                                   NODE in the ascending
    #                                   serotonergic system
    #   rostral linear nucleus      -> SMALLER; forebrain, limbic —
    #     (RLi)                         rostral to the CLi
    #
    # The rostral raphe complex projects ASCENDING. The caudal raphe
    # complex (raphe magnus, pallidus, obscurus) is in the MEDULLA
    # and projects DESCENDING. The DR is the PRIMARY ascending raphe
    # nucleus — the LARGEST serotonergic nucleus in the brain.
    #
    # Do not attempt to resolve the MnR, the CLi, the RLi, or the
    # medullary raphe nuclei as sub-paths of the DR — they are
    # DIFFERENT structures at DIFFERENT levels.

Neuromodulatory-class detail (not wired — consult references)::

    # The dorsal raphe nucleus is a NEUROMODULATORY NUCLEUS — the
    # SAME CLASS as:
    #
    #   locus coeruleus         -> NORADRENERGIC (NE) —
    #                               arousal, attention, stress
    #   dorsal raphe nucleus    -> SEROTONERGIC (5-HT) — mood,
    #                               anxiety, sleep, appetite —
    #                               THE PRIMARY SEROTONERGIC NUCLEUS
    #   median raphe nucleus    -> SEROTONERGIC (5-HT) — mood,
    #                               anxiety, memory
    #   caudal linear nucleus   -> SEROTONERGIC + DOPAMINERGIC —
    #                               smaller ascending raphe nucleus
    #   ventral tegmental area  -> DOPAMINERGIC (DA) — reward,
    #                               motivation
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
    # nucleus whose projections fan out bilaterally. The DR is the
    # CANONICAL example of a midline modulatory nucleus.

Clinical-pattern detail (not wired — consult references)::

    # The dorsal raphe nucleus is the PRIMARY serotonergic nucleus —
    # its clinical associations are DIRECT and SUBSTANTIAL:
    #
    #   MAJOR DEPRESSIVE DISORDER  -> DIRECT — the DR is the
    #                                 PRIMARY serotonergic substrate;
    #                                 SSRIs act on the whole
    #                                 serotonergic system, the DR
    #                                 is the principal target
    #   ANXIETY DISORDERS          -> DIRECT — the DR is a PRIMARY
    #     (GAD, social anxiety,        serotonergic substrate; SSRIs
    #      panic, OCD)                 are first-line
    #   SLEEP DISORDERS            -> DIRECT — the DR is the PRIMARY
    #     (especially REM)            REM-regulating serotonergic
    #                                 nucleus
    #   ADDICTION                  -> INDIRECT — the VTA is the
    #                                 primary dopaminergic substrate;
    #                                 the DR is a serotonergic
    #                                 modulator
    #   PAIN (descending)          -> CONTRIBUTOR — the raphe magnus
    #                                 and the PAG are the primary
    #                                 substrates; the DR contributes
    #                                 descending projections to the
    #                                 PAG / RVM / spinal cord
    #   SEXUAL DYSFUNCTION         -> DIRECT — SSRI-induced;
    #     (SSRI-induced)              the DR is a principal
    #                                 serotonergic target
    #   NAUSEA                     -> INDIRECT — 5-HT3 receptors in
    #                                 the gut and area postrema, NOT
    #                                 primarily the DR
    #
    # The clinical framework is INVERTED from the CLi's — the CLi
    # SHARED these associations INDIRECTLY with the DR; the DR OWNS
    # them.
    #
    # Do not conflate these patterns — they localize primarily to
    # the DR (for serotonergic disorders), the VTA (for reward), or
    # the raphe magnus / PAG (for descending pain modulation).

The clean midline representation — detail (not wired — structural
note)::

    # The DR is the FIRST CLEANLY-MIDLINE leaf in the tree:
    #
    #   midbrain.tegmentum.dorsal_raphe_nucleus
    #     (ONE leaf — MIDLINE — NO left/ or right/ nodes)
    #
    # The CLi is the ANOMALOUS case:
    #
    #   midbrain.tegmentum.caudal_linear_nucleus
    #     (midline leaf)
    #   midbrain.tegmentum.caudal_linear_nucleus.left
    #     (anomalous tree-structural side container)
    #   midbrain.tegmentum.caudal_linear_nucleus.right
    #     (anomalous tree-structural side container)
    #
    # The DR's clean representation is the MODEL — the tree
    # represents the DR exactly as its anatomy demands.
    #
    # The CLi's anomalous representation should be AMENDED — the
    # left/ and right/ nodes should be REMOVED, and the CLi should
    # be a SINGLE midline leaf, like the DR (Resolution B). This is
    # the recommendation of the CLi leaf, the CLi left/ module, and
    # the CLi right/ module — all three of which flag the anomaly.
    #
    # The DR path is the canonical structural pattern for a midline
    # nucleus in the tree; the CLi path should follow it.

References
----------
*   **Canonical raphe anatomy (human):** Hornung, J.P. (2003).
    "The human raphe nuclei and the serotonergic system." *Journal
    of Chemical Neuroanatomy* 26:331–343. (The human raphe nuclei
    — the rostral raphe complex (DR, MnR, CLi, RLi); the caudal
    raphe complex (raphe magnus, pallidus, obscurus); the
    serotonergic cell groups; the ascending and descending
    projections. **The DR is the largest serotonergic nucleus.**)
*   **Dorsal raphe — anatomy and subnuclei:** Michelsen, K.A.,
    Schmitz, C., Steinbusch, H.W.M. (2007). "The dorsal raphe
    nucleus — from silver stainings to a simplified subnuclear
    organization: review on the mesencephalic raphe nuclei."
    *Brain Research Reviews* 55:349–363. (The dorsal raphe nucleus
    — the largest serotonergic nucleus; its subnuclear organization
    (dorsal, ventral, ventrolateral, interfascicular, caudal); its
    ascending and descending projections.)
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
    complex — the DR and MnR; the differential projections of the
    two nuclei.)
*   **Dorsal raphe — forebrain serotonergic innervation:** Moore,
    R.Y., Halaris, A.E., Jones, B.E. (1978). "Serotonin neurons
    of the midbrain raphe: ascending projections." *Journal of
    Comparative Neurology* 180:417–438. (The ascending serotonergic
    projections from the dorsal and median raphe nuclei to the
    forebrain — the DR's forebrain projections.)
*   **Dorsal raphe — REM sleep:** McGinty, D.J., Harper, R.M.
    (1976). "Dorsal raphe neurons: depression of firing during
    sleep in cats." *Brain Research* 101:569–575. (The dorsal
    raphe serotonergic neurons — active during wakefulness, quiet
    during REM sleep — the REM-regulating serotonergic nucleus.)
*   **Dorsal raphe — mood and SSRIs:** Albert, P.R., Benkelfat,
    C., Descarries, L. (2012). "The neurobiology of depression —
    revisiting the serotonin hypothesis. I. Cellular and molecular
    mechanisms." *Philosophical Transactions of the Royal Society
    B* 367:2378–2381. (The serotonergic hypothesis of depression —
    the dorsal raphe as the primary serotonergic nucleus; the
    mechanisms of SSRI action.)
*   **Dorsal raphe — anxiety:** Graeff, F.G., Guimarães, F.S.,
    De Andrade, T.G., Deakin, J.F. (1996). "Role of 5-HT in
    stress, anxiety, and depression." *Pharmacology Biochemistry
    and Behavior* 54:129–141. (The role of the serotonergic
    system — the dorsal raphe — in stress, anxiety, and
    depression.)
*   **Dorsal raphe — sexual dysfunction and SSRIs:** Clayton, A.H.,
    Pradko, J.F., Croft, H.A., et al. (2002). "Prevalence of
    sexual dysfunction among newer antidepressants." *Journal of
    Clinical Psychiatry* 63:357–366. (SSRI-induced sexual
    dysfunction — the serotonergic system — the dorsal raphe as a
    principal target.)
*   **Dorsal raphe — descending pain modulation:** Fields, H.L.,
    Basbaum, A.I. (1978). "Brainstem control of spinal
    pain-transmission neurons." *Annual Review of Physiology*
    40:217–248. (The descending pain-modulation system — the
    PAG, the RVM, the raphe magnus, and the dorsal raphe's
    descending contributions.)
*   **Dorsal raphe — anatomy of the serotonergic system:** Törk,
    I. (1990). "Anatomy of the serotonergic system." *Annals of
    the New York Academy of Sciences* 600:9–34. (The anatomy of
    the serotonergic system — the raphe nuclei, the ascending and
    descending projections, the distribution of serotonergic
    fibers.)
*   **Serotonin receptors — distribution:** Pazos, A., Palacios,
    J.M. (1985). "Quantitative autoradiographic mapping of
    serotonin receptors in the rat brain. I. Serotonin-1
    receptors." *Brain Research* 346:205–230. (The distribution
    of serotonin receptors in the brain — the target fields of the
    ascending serotonergic system.)
*   **Dorsal raphe — human serotonergic cells:** Baker, K.G.,
    Halliday, G.M., Hornung, J.P., Geffen, L.B., Cotton, R.G.,
    Törk, I. (1991). "Distribution, morphology and number of
    monoamine-synthesizing and substance P-containing neurons in
    the human dorsal raphe nucleus." *Neuroscience* 42:757–775.
    (The monoamine-synthesizing neurons of the human dorsal raphe
    — the serotonergic subpopulation of the DR.)
*   **Median raphe — the pontine major raphe (contrast — PONS,
    NOT the DR):** Vertes, R.P., Crane, A.M. (1997).
    "Distribution, quantification and comparisons of
    serotonin-immunoreactive fibers in brain regions with
    different densities of the serotonin transporter." *Journal
    of Comparative Neurology* 381:293–306. (The median raphe
    nucleus — the pontine raphe nucleus — contrast with the
    midbrain DR.)
*   **Locus coeruleus — noradrenergic modulatory nucleus
    (contrast — NORADRENERGIC, NOT the DR):** Foote, S.L., Bloom,
    F.E., Aston-Jones, G. (1983). "Nucleus locus ceruleus: new
    evidence of anatomical and physiological specificity."
    *Physiological Reviews* 63:844–914. (The locus coeruleus —
    the noradrenergic modulatory nucleus — the two major
    monoaminergic modulatory nuclei of the brainstem are the
    dorsal raphe (serotonergic) and the locus coeruleus
    (noradrenergic).)
*   **VTA — dopaminergic reward nucleus (contrast — PAIRED, NOT
    the DR):** Fields, H.L., Hjelmstad, G.O., Margolis, E.B.,
    Nicola, S.M. (2007). "Ventral tegmental area neurons in
    learned appetitive behavior and positive reinforcement."
    *Annual Review of Neuroscience* 30:289–316. (The VTA — the
    paired dopaminergic reward nucleus — contrast with the
    midline serotonergic DR.)
*   **SLEA (contrast — the DR is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the dorsal raphe nucleus.)
*   NeuroNames — Dorsal raphe nucleus; FMA — Dorsal raphe nucleus.
    **The DR is a single midline nucleus — there is no "left
    dorsal raphe nucleus" and no "right dorsal raphe nucleus" in
    the standard anatomical atlases.**
"""