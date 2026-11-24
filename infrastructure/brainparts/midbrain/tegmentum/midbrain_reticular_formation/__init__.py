"""
infrastructure.brainparts.midbrain.tegmentum.midbrain_reticular_formation
========================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        ├── caudal_linear_nucleus
        │   ├── (midline leaf)
        │   ├── left               (anomalous)
        │   └── right              (anomalous)
        ├── dorsal_raphe_nucleus
        │   ├── (midline leaf)
        │   ├── left               (anomalous)
        │   └── right              (anomalous)
        ├── interpeduncular_nucleus
        │   ├── (midline leaf)
        │   ├── left               (anomalous)
        │   └── right              (anomalous)
        └── midbrain_reticular_formation    <-- THIS MODULE (DIFFUSE
                                                 BILATERAL REGION —
                                                 a single leaf, but
                                                 for a DIFFERENT
                                                 reason than the
                                                 midline nuclei)

**Primary synonym:** Midbrain reticular formation; **MRF**;
**mesencephalic reticular formation**; **formatio reticularis
mesencephali** (Latin); **the midbrain reticular core**.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). **Not a discrete nucleus.** A **diffuse reticular
region** of the **ventral midbrain tegmentum** — a **continuous,
heterogeneous** region of **interstitial neurons** (not a sharply
bounded cell group) that **spans both sides of the tegmentum** from
the **superior colliculus level** to the **pontomesencephalic
junction**. It is composed of a **heterogeneous population of
neurons** — **glutamatergic**, **cholinergic** (the
**pedunculopontine** and **laterodorsal tegmental** nuclei),
**GABAergic**, and **peptidergic** — organized as a **diffuse
reticular network**, not a **discrete nucleus**. **It has no
single transmitter**, **no single projection**, and **no sharp
boundaries** — this is what makes it a **diffuse region** rather
than a **nucleus**. Its **mesencephalic locomotor region (MLR)**
component — the **cuneiform nucleus**, the **subcuneiform
nucleus**, and the **pedunculopontine nucleus** — is the
**locomotion initiation** region. Its **ascending reticular**
component — part of the **ascending reticular activating system
(ARAS)** — is the **arousal** region. Its **descending reticular**
component — the **reticulospinal** projections — contributes to
**locomotion**, **postural control**, and **pain modulation**.
**No transmitter or neurochemical phenotype is imported** — the
**cholinergic** phenotype of the PPN and LDT, the **glutamatergic**
phenotype of the cuneiform and subcuneiform, and the other
transmitter phenotypes are **``chemicals_hormones``-layer facts**
— see *Chemicals-Layer Discipline*.
**Container status:** **This module is a LEAF** — **a diffuse
bilateral region**. It is **NOT** under ``tegmentum/left/`` or
``tegmentum/right/`` — it sits **directly under** the tegmentum
container. **It is the first "diffuse bilateral region" leaf in
the family** — a **single leaf** that is **neither paired** (like
the SN, the VTA, the red nucleus) **nor midline** (like the CLi,
the DR, the IPN). **The tree represents the MRF cleanly** — a
**single leaf** under ``tegmentum/``, **no `left/` or `right/`
nodes** — **and this is the anatomically correct representation**.
See *The Diffuse Bilateral Region — a Third Laterality Class*.
**Part of:** The **tegmentum** region container — as a **diffuse
bilateral** leaf. **The MRF is NOT a cranial nerve nucleus** and is
**NOT cross-listed** with ``cranial_nerve_nuclei/``.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — **diffuse bilateral**, **not**
a side container.
**Structural children:** **None.** This is a **leaf** module. The
**subregions** (cuneiform nucleus, subcuneiform nucleus,
pedunculopontine nucleus, laterodorsal tegmental nucleus, the
diffuse MRF proper) are documented as **prose**, not as structural
children. **A diffuse region cannot be resolved into discrete
children** — its **subregions** are **anatomical subdivisions of a
continuous region**, not **discrete nuclei**. See *Subregions (prose,
not structural children)* and *Diffuse-Region Discipline*.
**Boundary status (DIFFUSE BILATERAL REGION — a THIRD laterality
class, distinct from PAIRED and from MIDLINE):** **Boundary case —
the midbrain reticular formation is a DIFFUSE BILATERAL REGION.** It
**spans both sides of the tegmentum** as a **continuous diffuse
network** — it is **NOT a paired structure** (there is no
"left MRF" and "right MRF" — it is **one continuous region**
spanning both sides), and it is **NOT a midline nucleus** (it is
**not** a discrete nucleus on the midline — it **extends
laterally** through the whole tegmentum on both sides). **It is a
THIRD laterality class** in the family's taxonomy:
*   **Paired** — a `left/` leaf and a `right/` leaf (the **SN**,
    the **VTA**, the **red nucleus**, the **riMLF**, the
    **interstitial nucleus of Cajal**, the **CN nuclei**, etc.).
*   **Midline** — a **single midline leaf** (the **CLi**, the
    **DR**, the **IPN**) — a discrete nucleus on the midline.
*   **Diffuse bilateral** — a **single leaf** that **spans both
    sides as a continuous region** — **not paired, not midline**
    — the **MRF** (this module), and **potentially** the **PAG**
    (depending on the on-disk tree — the PAG is a **diffuse
    column** surrounding the aqueduct, and may be **diffuse
    bilateral** rather than paired or midline).
**The MRF is the FIRST "diffuse bilateral region" leaf in the
family.** Consumers must **not** assume the MRF is paired (it is
**not** — no `left/`/`right/` nodes) and must **not** assume it is
midline (it is **not** — it extends laterally across both sides).
**It is a single leaf** — a **continuous diffuse region** — and the
tree represents it **cleanly** with a **single leaf** under
``tegmentum/``. See *The Diffuse Bilateral Region — a Third
Laterality Class* and *The Clean Case — the MRF is Represented
Correctly*.
**Boundary status (CLEAN CASE — the MRF is represented correctly, and
it is the SECOND proof case for the tegmentum container amendment):**
**Boundary case — the midbrain reticular formation is CLEANLY
REPRESENTED in the tree** — a **single leaf** under ``tegmentum/``
— **no `left/` or `right/` nodes** — **and this is the anatomically
correct representation**. **This makes the MRF the first genuinely
cleanly-represented single leaf in the tegmentum since the IPN's
clean-case claim was falsified** — and it is **clean for a
DIFFERENT reason** than the CLi, DR, and IPN:
*   **The CLi, DR, and IPN are midline nuclei** — single leaves
    because they are **discrete nuclei on the midline** — and the
    tree **represents them as paired** (anomalous — their own
    `left/` and `right/` modules flag this).
*   **The MRF is a diffuse bilateral region** — a single leaf
    because it is a **continuous region spanning both sides** —
    and the tree **represents it correctly** (single leaf, no
    `left/` or `right/`).
**The MRF is the SECOND proof case for the tegmentum container
amendment** — beyond the midline nuclei, **diffuse bilateral
regions can also be single leaves** under ``tegmentum/`` — and the
tree **already represents the MRF this way**. **The tegmentum
container amendment should permit BOTH exception categories** —
**midline nuclei** AND **diffuse bilateral regions** as **direct
children** of ``tegmentum/`` — **not required** to be under
``left/`` or ``right/``. **The MRF is the existing evidence** that
**diffuse bilateral regions** are (correctly) represented as
single leaves. See *The Clean Case — the MRF is Represented
Correctly* and *Design Contract — Live amendment to the tegmentum
container*.
**Boundary status (NOT a discrete nucleus — a DIFFUSE REGION):**
**Boundary case — the midbrain reticular formation is NOT a
discrete nucleus.** It is a **diffuse reticular region** — a
**continuous network of interstitial neurons** without **sharp
boundaries** and without a **single transmitter**, **single
projection**, or **single function**. **The family's structural
class** includes **discrete nuclei** (the **SN**, the **VTA**, the
**red nucleus**, the **DR**, the **CLi**, the **IPN**, the **CN
nuclei**, etc.) and **diffuse regions** (**the MRF** — this
module; **potentially the PAG**). **A diffuse region cannot be
resolved into discrete structural children** — its **subregions**
are **anatomical subdivisions** of a **continuous region**, not
**discrete nuclei**. Consumers must **not** treat the MRF as a
**discrete nucleus** with a **single function** — it is a **diffuse
region** with a **heterogeneous set of functions** (arousal,
locomotion, sensorimotor integration, pain modulation). See
*Subregions (prose, not structural children)* and *Diffuse-Region
Discipline*.
**Boundary status (NOT a CN nucleus — NOT cross-listed with
``cranial_nerve_nuclei/``):** **Boundary case — the midbrain
reticular formation is NOT a cranial nerve nucleus.** It is a
**diffuse reticular region** — it is **not a CN nucleus** and is
**NOT cross-listed** with the ``cranial_nerve_nuclei/`` container.
The **four CN nuclei** in the tegmentum (oculomotor, trochlear,
Edinger-Westphal, mesencephalic trigeminal) are **cross-listed**
between ``tegmentum/`` and ``cranial_nerve_nuclei/`` — **the MRF
is not one of them**. Consumers must **not** look for the MRF
under ``.../cranial_nerve_nuclei/`` — it has **one path only**:
``.../tegmentum/midbrain_reticular_formation/``.
**Boundary status (NOT the PAG — the PAG SURROUNDS the cerebral
aqueduct and is a DIFFERENT diffuse region):** **Boundary case —
the midbrain reticular formation is NOT the periaqueductal gray
(PAG).** The **PAG** (``.../tegmentum/left/periaqueductal_gray/``
and the right counterpart — **OR** a midline or diffuse-bilateral
PAG, depending on the on-disk tree) **surrounds** the **cerebral
aqueduct** — it is a **diffuse column** around the aqueduct — its
**function** is **pain modulation** and **defensive behavior**.
**The MRF is VENTRAL to the PAG** — it is the **diffuse region of
the ventral tegmentum** — its **function** is **arousal**,
**locomotion**, **sensorimotor integration**, and **pain
modulation** (via projections to the PAG and the RVM). **They are
DIFFERENT DIFFUSE REGIONS in DIFFERENT positions** — the **PAG**
surrounds the aqueduct; the **MRF** is in the **ventral
tegmentum**. Consumers must **not** conflate the MRF with the
PAG, and must **not** resolve the PAG through the MRF path (or
vice versa).
**Boundary status (NOT the pontine reticular formation or the
medullary reticular formation — those are HINDBRAIN reticular
regions):** **Boundary case — the midbrain reticular formation is
NOT the pontine reticular formation or the medullary reticular
formation.** The **pontine reticular formation**
(``.../hindbrain/metencephalon/pons/.../pontine_reticular_formation/``)
and the **medullary reticular formation**
(``.../hindbrain/myencephalon/medulla_oblongata/.../medullary_
reticular_formation/``) are **rhombencephalic** — **caudal** to the
midbrain. **The MRF is mesencephalic** — **rostral** to the pons.
**The three reticular regions** — **midbrain**, **pontine**, and
**medullary** — are **continuations of the same reticular
formation** but at **different levels of the brainstem**. **They
are DIFFERENT STRUCTURES at DIFFERENT levels** — the **MRF is
midbrain**; the **pontine reticular formation** is **pons**; the
**medullary reticular formation** is **medulla**. Consumers must
**not** conflate the MRF with the pontine or medullary reticular
formation. **(The reticular formation is anatomically continuous
across the three levels — but the tree represents each level as a
separate region, and the boundaries between them are conventionally
defined by the pontomesencephalic and pontomedullary junctions.)**
**Boundary status (NOT the MLR as a separate structure — the MLR is
a SUBREGION of the MRF):** **Boundary case — the midbrain
reticular formation is NOT the mesencephalic locomotor region
(MLR) as a separate structure.** The **MLR** is the
**locomotion initiation** region — the **cuneiform nucleus**, the
**subcuneiform nucleus**, and the **pedunculopontine nucleus**
(PPN) — **within the MRF**. **The MLR is a SUBREGION of the MRF**
— **not a separate structure**. **It is documented as prose** — not
as a structural child. Consumers must **not** look for the MLR as
a separate container — it is a **functional subregion** of the
MRF, documented in the MRF's leaf. See *The Mesencephalic Locomotor
Region (MLR) — the Primary Functional Anchor* and *Subregions
(prose, not structural children)*.
**Boundary status (NOT the pedunculopontine nucleus or the
laterodorsal tegmental nucleus as separate structural children —
they are SUBREGIONS of the MRF):** **Boundary case — the midbrain
reticular formation is NOT the pedunculopontine nucleus (PPN) or
the laterodorsal tegmental nucleus (LDT) as separate structural
children.** The **PPN** and the **LDT** are **cholinergic
subregions** of the MRF — the **PPN** is involved in **locomotion**
(via the MLR), **arousal**, and **REM sleep**; the **LDT** is
involved in **REM sleep**. **They are SUBREGIONS of the MRF** —
**not separate structures**. **They are documented as prose** —
not as structural children. Consumers must **not** look for the
PPN or the LDT as separate containers — they are **functional
subregions** of the MRF, documented in the MRF's leaf. See
*Subregions (prose, not structural children)*.
**Boundary status (NOT the red nucleus, the substantia nigra, or
the VTA — those are DISCRETE NUCLEI of the tegmentum):** **Boundary
case — the midbrain reticular formation is NOT the red nucleus, the
substantia nigra, or the ventral tegmental area.** The **red
nucleus** (``.../tegmentum/left/red_nucleus/`` and the right
counterpart), the **substantia nigra**
(``.../tegmentum/left/substantia_nigra/`` and the right
counterpart), and the **VTA**
(``.../tegmentum/left/ventral_tegmental_area/`` and the right
counterpart) are **discrete nuclei** — **paired**, **sharply
bounded**, with **specific transmitters** and **specific
projections**. **The MRF is a diffuse region** — **not a discrete
nucleus** — with **heterogeneous transmitters** and **heterogeneous
projections**. **They are DIFFERENT STRUCTURES of DIFFERENT
classes** — the **red nucleus**, the **SN**, and the **VTA** are
**discrete nuclei**; the **MRF** is a **diffuse reticular
region**. Consumers must **not** conflate the MRF with the red
nucleus, the SN, or the VTA.
**Boundary status (NOT the CLi, the DR, or the IPN — those are
MIDLINE nuclei):** **Boundary case — the midbrain reticular
formation is NOT the caudal linear nucleus, the dorsal raphe
nucleus, or the interpeduncular nucleus.** The **CLi**
(``.../tegmentum/caudal_linear_nucleus/``), the **DR**
(``.../tegmentum/dorsal_raphe_nucleus/``), and the **IPN**
(``.../tegmentum/interpeduncular_nucleus/``) are **midline
nuclei** — **discrete nuclei on the midline** (though the tree
represents them as paired — anomalous). **The MRF is a diffuse
bilateral region** — **not a midline nucleus** — it **extends
laterally** across both sides of the tegmentum. **They are
DIFFERENT STRUCTURES of DIFFERENT laterality classes** — the
**CLi**, the **DR**, and the **IPN** are **midline nuclei**; the
**MRF** is a **diffuse bilateral region**. Consumers must **not**
conflate the MRF with the CLi, the DR, or the IPN.
**Boundary status (NOT the superior colliculus or the inferior
colliculus — those are TECTUM structures):** **Boundary case — the
midbrain reticular formation is NOT the superior colliculus or the
inferior colliculus.** The **superior colliculus** and the
**inferior colliculus** (``.../tectum/...``) are **tectum**
structures — **dorsal** to the cerebral aqueduct. **The MRF is a
tegmentum structure** — **ventral** to the cerebral aqueduct.
**They are DIFFERENT COMPARTMENTS of the midbrain** — the **tectum**
is **dorsal**; the **tegmentum** is **ventral**. Consumers must
**not** conflate the MRF with the colliculi, and must **not**
resolve the colliculi through the MRF path (or vice versa).
**Boundary status (NOT the pretectum — the pretectum is a separate
region at the DIENCEPHALON-MIDBRAIN JUNCTION):** **Boundary case —
the midbrain reticular formation is NOT the pretectum.** The
**pretectum** (``.../midbrain/pretectum/``) is a **separate
region** at the **diencephalon-midbrain junction** — **rostral** to
the superior colliculus — its **function** is **pupillary and
optokinetic**. **The MRF is in the ventral midbrain tegmentum** —
its **function** is **arousal, locomotion, sensorimotor
integration, pain modulation**. **They are DIFFERENT REGIONS in
DIFFERENT functional systems.** Consumers must **not** conflate the
MRF with the pretectum.
**Boundary status (NOT the cerebral peduncle or the cerebral
aqueduct — those are VENTRAL / DORSAL boundaries of the
tegmentum):** **Boundary case — the midbrain reticular formation is
NOT the cerebral peduncle or the cerebral aqueduct.** The
**cerebral peduncle** (``.../midbrain/cerebral_peduncle/``) is the
**ventral-most descending fiber bundle** — the **crus cerebri** —
**white matter** — **ventral** to the substantia nigra, the
**ventral boundary** of the tegmentum. The **cerebral aqueduct**
(``.../midbrain/cerebral_aqueduct/``) is the **midline CSF
conduit** — the **dorsal boundary** of the tegmentum. **The MRF is
the diffuse reticular region BETWEEN them** — **ventral** to the
aqueduct and **dorsal** to the cerebral peduncle. **They are
DIFFERENT STRUCTURES** — the **peduncle** is a **conduction
pathway**; the **aqueduct** is a **CSF conduit**; the **MRF** is a
**diffuse reticular region**. Consumers must **not** conflate the
MRF with the cerebral peduncle or the cerebral aqueduct.
**Boundary status (DIFFUSE RETICULAR REGION — a NEW structure class
— NOT a discrete nucleus, NOT a sensory relay, NOT a modulatory
nucleus, NOT a conduction pathway):** **Boundary case — the
midbrain reticular formation is a DIFFUSE RETICULAR REGION.** In
the family's **structure-class taxonomy**, it is a **new class** —
**diffuse reticular region** — **distinct** from:
*   **Discrete nuclei** (the **SN**, the **VTA**, the **red
    nucleus**, the **CN nuclei**, the **DR**, the **CLi**, the
    **IPN**, the **LC** — **sharply bounded** cell groups with
    **specific** transmitters and **specific** projections).
*   **Sensory relays** (the **IC**, the **pretectum** —
    **discrete** nuclei that relay **specific** sensory
    modalities).
*   **Modulatory nuclei** (the **DR**, the **CLi**, the **LC**,
    the **VTA**, the **SNc** — **discrete** nuclei that broadcast
    a **single** neuromodulator via **volume transmission**).
*   **Conduction pathways** (the **MLF**, the **tectobulbar
    tract**, the **brachia**, the **cerebral peduncle** — **white
    matter** tracts).
**The MRF is a DIFFUSE REGION** — a **continuous reticular
network** of **heterogeneous neurons** with **heterogeneous
transmitters** and **heterogeneous projections** — that
**integrates** multiple inputs (sensory, motor, autonomic) and
**projects** diffusely to multiple targets (the cortex, the basal
ganglia, the thalamus, the spinal cord, the brainstem) — its
**function** is **arousal** (the **ARAS** — the ascending reticular
activating system), **locomotion** (the **MLR** — the
mesencephalic locomotor region), **sensorimotor integration**, and
**pain modulation**. **It is NOT an oscillator, NOT a premotor
pool, NOT a motor nucleus, NOT a sensory relay, NOT a modulatory
nucleus, NOT a conduction pathway, NOT a sensorimotor integration
structure.** **Diffuse reticular regions carry NO coupling
warning** — same rule as motor nuclei, premotor pools, sensor
nuclei, relay nuclei, neuromodulatory nuclei, sensorimotor
integration structures, and conduction pathways. **The diffuse
bilateral position** — **not paired, not midline** — is the
**structural expression** of its **diffuse reticular function**:
it **spans both sides** as a **continuous reticular network**
because it **integrates** inputs and **projects** diffusely to
**bilateral targets**. **The MRF is a NEW structure class** —
**diffuse reticular region** — the **first** of its kind in the
family. See *The Diffuse Bilateral Region — a Third Laterality
Class* and *Lateralization Notes*.
**Boundary status (NO COUPLING WARNING — the MRF is a DIFFUSE
RETICULAR REGION):** **Boundary case — the midbrain reticular
formation carries NO coupling warning.** The **coupling warning**
attaches to **OSCILLATORS** (the pre-Bötzinger complex, the
Bötzinger complex, the pFRG) — and the **MRF is not an
oscillator**. **It is a diffuse reticular region** — a **single
leaf**, **not paired**, **not midline**. **Diffuse reticular
regions carry NO coupling warning** — same rule as every
non-oscillator class. The **diffuse bilateral position** is **not
a coupling hazard** — it is the **structural fact** of a **diffuse
region** that **integrates** inputs and **projects** to
**bilateral targets**. There are **no "two sides" to couple** —
the MRF is **one continuous region**.

Overview
--------
The midbrain reticular formation (MRF) is a **diffuse bilateral
reticular region** of the **ventral midbrain tegmentum** — a
**continuous, heterogeneous network** of **interstitial neurons**
that **spans both sides** of the tegmentum from the **superior
colliculus level** to the **pontomesencephalic junction**. It is
**not a discrete nucleus** — it has **no sharp boundaries**, **no
single transmitter**, **no single projection**, and **no single
function**. It is the **midbrain component** of the **reticular
formation** — the **continuous network** that extends from the
**midbrain** through the **pons** and the **medulla** — and it is
the **midbrain component** of the **ascending reticular activating
system (ARAS)** — the **arousal** system — and the **descending
reticular formation** — the **locomotion** and **postural control**
system.

**The MRF is a DIFFUSE BILATERAL REGION — a THIRD laterality class.**
It is **neither paired** (like the SN, the VTA, the red nucleus)
**nor midline** (like the CLi, the DR, the IPN). It **spans both
sides** as a **continuous diffuse network** — a **single leaf**,
but for a **different reason** than the midline nuclei. **The tree
represents it cleanly** — a **single leaf** under ``tegmentum/``,
**no `left/` or `right/` nodes** — and this is the **anatomically
correct representation**. See *The Diffuse Bilateral Region — a
Third Laterality Class* and *The Clean Case — the MRF is
Represented Correctly*.

**The MRF is the SECOND proof case for the tegmentum container
amendment.** The **CLi**, the **DR**, and the **IPN** are
**midline nuclei** — **single leaves** because they are **discrete
nuclei on the midline** — and the tree **represents them as
paired** (anomalous — their own `left/` and `right/` modules flag
this). **The MRF is a diffuse bilateral region** — a **single
leaf** because it is a **continuous region spanning both sides**
— and the tree **represents it correctly** (single leaf, no
`left/` or `right/`). **The tegmentum container amendment should
permit BOTH exception categories** — **midline nuclei** AND
**diffuse bilateral regions** as **direct children** of
``tegmentum/``. **The MRF is the existing evidence** that
**diffuse bilateral regions** are (correctly) represented as
**single leaves**.

**The MRF is a NEW structure class — the diffuse reticular region.**
It is **not a discrete nucleus** — it is a **continuous reticular
network** of **heterogeneous neurons** with **heterogeneous
transmitters** and **heterogeneous projections**. **It is NOT an
oscillator, NOT a premotor pool, NOT a motor nucleus, NOT a sensory
relay, NOT a modulatory nucleus, NOT a conduction pathway, NOT a
sensorimotor integration structure.** It is a **diffuse region**
that **integrates** multiple inputs and **projects** diffusely to
multiple targets — its **function** is **arousal** (the **ARAS**),
**locomotion** (the **MLR**), **sensorimotor integration**, and
**pain modulation**.

**The MRF carries NO coupling warning.** It is a **diffuse
reticular region** — a **single leaf**, **not paired**, **not
midline**. **Diffuse reticular regions carry NO coupling warning**
— same rule as every non-oscillator class.

**The MRF is NOT a CN nucleus.** It is a **diffuse reticular
region** — it is **not** cross-listed with
``cranial_nerve_nuclei/``. It has **one path only**.

The Diffuse Bilateral Region — a Third Laterality Class
------------------------------------------------------
**The MRF is the first "diffuse bilateral region" in the family** —
a **third laterality class** beyond **paired** and **midline**:

*   **Paired** — a `left/` leaf and a `right/` leaf. Examples: the
    **substantia nigra**, the **VTA**, the **red nucleus**, the
    **riMLF**, the **interstitial nucleus of Cajal**, the **CN
    nuclei** (cross-listed), the **PAG** (in the tree's current
    representation). **Each side is a distinct anatomical
    structure**, though often with **homologous functions** and
    **projections** to both sides.

*   **Midline** — a **single midline leaf** — a **discrete nucleus
    on the midline**. Examples: the **CLi**, the **DR**, the
    **IPN**. **Each is a single nucleus** — **not paired** — with
    **distributed projections** to **both sides**. **The tree
    represents them as paired** (anomalous — their own `left/`
    and `right/` modules flag this).

*   **Diffuse bilateral** — a **single leaf** that **spans both
    sides as a continuous region** — **not paired, not midline**.
    Example: **the MRF** (this module) — and, **potentially**, the
    **PAG** (a **diffuse column** around the aqueduct — its
    laterality depends on the on-disk tree; the tegmentum
    container's "treated as paired in the tree" framing suggests
    the tree represents it as paired, but its anatomy is
    **diffuse bilateral**).

**The MRF is the FIRST "diffuse bilateral region" leaf in the
family.** Consumers must **not** assume the MRF is paired (it is
**not** — no `left/`/`right/` nodes) and must **not** assume it is
midline (it is **not** — it extends laterally across both sides).
**It is a single leaf** — a **continuous diffuse region** — and the
tree represents it **cleanly** with a **single leaf** under
``tegmentum/``.

**The MRF's diffuse bilateral position is the structural expression
of its function.** It **integrates** multiple inputs (sensory,
motor, autonomic) and **projects** diffusely to multiple targets
(the cortex, the basal ganglia, the thalamus, the spinal cord, the
brainstem) — it **spans both sides** as a **continuous reticular
network** because it **integrates** and **projects** across
**both sides**. **It has no "left half" and "right half"** — it is
**one continuous region**.

The Clean Case — the MRF is Represented Correctly
-------------------------------------------------
**The MRF is cleanly represented in the tree.** The on-disk path
is ``tegmentum/midbrain_reticular_formation/`` — a **single leaf**
under ``tegmentum/`` — **no `left/` or `right/` nodes**. **This is
the anatomically correct representation** — the MRF is a **diffuse
bilateral region**, and a **single leaf** represents it correctly.

**This makes the MRF the first genuinely cleanly-represented single
leaf in the tegmentum since the IPN's clean-case claim was
falsified** — and it is **clean for a DIFFERENT reason** than the
CLi, DR, and IPN:

*   **The CLi, DR, and IPN** are **midline nuclei** — single
    leaves because they are **discrete nuclei on the midline** —
    and the tree **represents them as paired** (anomalous — their
    own `left/` and `right/` modules flag this).

*   **The MRF** is a **diffuse bilateral region** — a single leaf
    because it is a **continuous region spanning both sides** —
    and the tree **represents it correctly** (single leaf, no
    `left/` or `right/`).

**The MRF is the SECOND proof case for the tegmentum container
amendment.** The **tegmentum container's paired-leaf rule** —
*"each tegmentum nucleus is a paired structure (a ``left/`` leaf
and a ``right/`` leaf)"* — **was written before the CLi, the DR,
the IPN, and the MRF were added**. **It is too rigid**:
*   **Three midline nuclei** (the **CLi**, the **DR**, the
    **IPN**) — **single leaves**, but the tree represents them as
    **paired** (anomalous).
*   **One diffuse bilateral region** (the **MRF**) — **a single
    leaf**, and the tree **represents it correctly** (single
    leaf, no `left/` or `right/`).
*   **The PAG** — **potentially** a **diffuse bilateral region**
    — its laterality depends on the on-disk tree.

**The tegmentum container amendment should permit BOTH exception
categories** — **midline nuclei** AND **diffuse bilateral
regions** as **direct children** of ``tegmentum/`` — **not
required** to be under ``left/`` or ``right/``. **The MRF is the
existing evidence** that **diffuse bilateral regions** are
(correctly) represented as **single leaves**.

**The MRF is also the second clean midline-or-diffuse case that
supports Resolution B for the CLi, DR, and IPN** — **not by
providing a clean MIDLINE case** (the IPN's clean-case claim was
falsified), **but by providing a clean SINGLE-LEAF case** for a
**different type of exception** (diffuse, not midline). **The
argument for Resolution B is still valid** — **midline nuclei
should be represented as single leaves because they are midline**
— and **the MRF's clean representation adds indirect support**:
**the tree CAN represent single leaves correctly** — **and it
does, for the MRF**. **So it should also do so for the CLi, DR,
and IPN** — **and the tegmentum container amendment should
formalize both exception categories.**

Subregions (prose, not structural children)
-------------------------------------------
The midbrain reticular formation has **functional subregions** —
**anatomical subdivisions of a continuous region**, not **discrete
nuclei** — documented as **prose**, not as structural children:

*   **Cuneiform nucleus (CnF)** — the **principal locomotion
    initiation** subregion — **glutamatergic** — projects to the
    **spinal cord** (the **reticulospinal** pathway) and to the
    **reticular formation** — **initiates locomotion** (the
    **mesencephalic locomotor region** component). **Also**
    implicated in **defensive behavior** and **cardiovascular
    control**. **Subregion of the MRF** — **not a structural
    child**.

*   **Subcuneiform nucleus (SubCnF)** — a **locomotion** and
    **cardiovascular control** subregion — **glutamatergic** —
    adjacent to the **cuneiform nucleus** — **part of the
    MLR**. **Subregion of the MRF** — **not a structural child**.

*   **Pedunculopontine nucleus (PPN)** — a **cholinergic** and
    **glutamatergic** subregion — involved in **locomotion** (via
    the **MLR**), **arousal**, and **REM sleep** — the **cholinergic
    component** of the **ARAS**. **Subregion of the MRF** — **not
    a structural child**.

*   **Laterodorsal tegmental nucleus (LDT)** — a **cholinergic**
    subregion — involved in **REM sleep** and **arousal** — a
    **cholinergic component** of the **ARAS**. **Subregion of the
    MRF** — **not a structural child**.

*   **MRF proper** — the **diffuse remainder** of the midbrain
    reticular formation — **heterogeneous** — **glutamatergic**,
    **GABAergic**, **peptidergic** — **sensorimotor
    integration**, **arousal**, **pain modulation** (via
    projections to the **PAG** and the **RVM**). **Subregion of
    the MRF** — **not a structural child**.

**These subregions are prose, not structural children.** They are
**anatomical subdivisions of a continuous region** — **not
discrete nuclei**. **A diffuse region cannot be resolved into
discrete children** — its subregions are **prose**. The tree wires
the **midbrain reticular formation** as a **single leaf** under
the tegmentum container (diffuse bilateral). Consumers must **not**
resolve ``.../midbrain_reticular_formation/cuneiform_nucleus`` or
``.../midbrain_reticular_formation/pedunculopontine_nucleus`` — no
such paths exist.

The Mesencephalic Locomotor Region (MLR) — the Primary Functional
Anchor
------------------------------------------------------------------
The **mesencephalic locomotor region (MLR)** is the **best-defined
functional subregion** of the MRF — the **locomotion initiation**
region. It is composed of the **cuneiform nucleus**, the
**subcuneiform nucleus**, and the **pedunculopontine nucleus** —
**all within the MRF**. **The MLR is a SUBREGION of the MRF** —
**not a separate structure**.

**The MLR initiates locomotion** — it projects to the **spinal
cord** (the **reticulospinal** pathway) and to the **reticular
formation** — activating the **central pattern generators** for
**locomotion** (the **CPGs** in the spinal cord). **Stimulation of
the MLR elicits locomotion** in decerebrate animals — **the MLR
is the locomotion initiation region**. **The MLR is also involved
in the initiation of gait** — **in humans**, **the MLR (and
specifically the PPN)** is a **target for deep brain stimulation
in Parkinson's disease** — **to improve gait and postural
control**.

**The MLR is a SUBREGION of the MRF** — it is **documented as
prose**, **not as a structural child**. Consumers must **not**
look for the MLR as a **separate container** — it is a
**functional subregion** of the MRF, documented in the MRF's leaf.

The Ascending Reticular Activating System (ARAS) — the Arousal
Context
------------------------------------------------------------------
The **ascending reticular activating system (ARAS)** is the
**arousal** system — the **ascending reticular** component of the
reticular formation. **The MRF is the midbrain component of the
ARAS** — it **projects** to the **thalamus** (the **intralaminar
nuclei**, the **reticular nucleus**), the **hypothalamus**, the
**basal forebrain**, and the **cortex** — **activating** the
**forebrain** and **maintaining wakefulness**.

**The PPN and the LDT** — the **cholinergic subregions** of the
MRF — are the **cholinergic components** of the ARAS — they
**project** to the **thalamus**, the **basal forebrain**, and the
**cortex** — contributing to **wakefulness** and **REM sleep**.

**The MRF is the midbrain component of the ARAS** — its **arousal
function** is one of its **principal functions**. **The ARAS is a
DISTRIBUTED system** — the **MRF**, the **pons reticular
formation**, the **medulla reticular formation**, and their
**cholinergic** (PPN, LDT), **noradrenergic** (LC), and
**serotonergic** (DR) components — **together** maintain
**arousal**. **The MRF is ONE COMPONENT** of the ARAS — **not the
whole ARAS**.

The Descending Reticular Formation — the Locomotion and Postural
Control Context
----------------------------------------------------------------------------
The **descending reticular formation** is the **locomotion**,
**postural control**, and **pain modulation** system — the
**descending reticular** component of the reticular formation.
**The MRF is the midbrain component** — its **cuneiform nucleus**
and **subcuneiform nucleus** project to the **spinal cord** (the
**reticulospinal** pathway) — **initiating locomotion** and
**modulating postural control**. Its **MRF proper** projects to
the **PAG** and the **RVM** (the **rostral ventromedial medulla**)
— **contributing** to the **descending pain-modulation system**.

**The MRF is the midbrain component of the descending reticular
formation** — its **locomotion** and **pain-modulation** functions
are **two of its principal functions**. **The descending reticular
formation is a DISTRIBUTED system** — the **MRF**, the **pons
reticular formation**, the **medulla reticular formation**, and
their **raphe** (raphe magnus, RVM) components — **together**
modulate **locomotion** and **pain**. **The MRF is ONE COMPONENT**
of the descending reticular formation — **not the whole system**.

Function in the Human Brain
---------------------------
The midbrain reticular formation's functions are **arousal**,
**locomotion**, **sensorimotor integration**, and **pain
modulation** — **NOT** a sensory relay, **NOT** a modulatory
nucleus, **NOT** a motor nucleus, **NOT** a premotor pool, **NOT**
a sensorimotor integration structure, **NOT** a conduction
pathway:

*   **Arousal (the ascending reticular activating system — ARAS):**
    The MRF — **especially its cholinergic subregions** (the
    **PPN** and the **LDT**) — **projects** to the **thalamus**
    (intralaminar nuclei, reticular nucleus), the **hypothalamus**,
    the **basal forebrain**, and the **cortex** — **activating**
    the **forebrain** and **maintaining wakefulness**. **The MRF
    is the midbrain component of the ARAS** — the **arousal
    system**.

*   **Locomotion (the mesencephalic locomotor region — MLR):** The
    MRF — **especially its glutamatergic subregions** (the
    **cuneiform nucleus** and the **subcuneiform nucleus**) —
    **projects** to the **spinal cord** (the **reticulospinal**
    pathway) — **initiating** and **modulating** **locomotion**
    and **gait**. **The MRF is the midbrain component of the
    MLR** — the **locomotion initiation** region.

*   **Sensorimotor Integration:** The MRF **integrates** multiple
    sensory and motor inputs — **ascending** sensory signals,
    **descending** motor commands, **autonomic** signals — and
    **projects** to **multiple targets** — **integrating** the
    **sensorimotor** and **autonomic** functions of the
    **brainstem**. **The MRF is a diffuse integrative region** —
    **not a single-function nucleus**.

*   **Pain Modulation (via the PAG and the RVM):** The MRF
    **projects** to the **PAG** and the **RVM** (the rostral
    ventromedial medulla) — **contributing** to the **descending
    pain-modulation system**. **The MRF is a contributor** to
    **descending pain modulation** — **the PAG and the raphe
    magnus are the primary substrates**.

*   **REM Sleep (via the cholinergic subregions):** The **PPN** and
    the **LDT** — the **cholinergic subregions** of the MRF —
    are involved in **REM sleep** — **contributing** to the
    **cholinergic** component of **REM sleep regulation**. **The
    MRF is a contributor** — **the sublateral dorsal nucleus**
    (in the pons) and the **precoeruleus region** are **also**
    involved in REM sleep.

*   **NOT a sensory relay.** The MRF does **not** transduce or
    relay a specific sensory modality.

*   **NOT a modulatory nucleus.** The MRF does **not** broadcast
    a single neuromodulator via volume transmission — it is a
    **diffuse region** with **heterogeneous** transmitters and
    **heterogeneous** projections.

*   **NOT a motor nucleus.** The MRF does **not** drive muscle
    directly — it **initiates** and **modulates** locomotion via
    the **reticulospinal** pathway.

*   **NOT a premotor pool.** The MRF does **not** transform motor
    commands in the sense of the **PPRF** or the **riMLF** — it
    **initiates** locomotion at a **higher level** (the **MLR**).

*   **NOT a sensorimotor integration structure** in the sense of
    the **superior colliculus** — the SC **integrates** sensory
    input into a **saccade command**; the MRF **integrates**
    multiple inputs into **arousal** and **locomotion** — it is
    **diffuse**, not a **discrete command generator**.

*   **NOT a conduction pathway.** The MRF is **grey matter** — a
    **diffuse reticular region** — **not white matter**.

*   **NOT an oscillator.** The MRF is a **diffuse reticular
    region** — it does **not** generate a rhythm. **Diffuse
    reticular regions carry NO coupling warning** — same rule as
    every non-oscillator class.

**The unifying theme:** the MRF is a **diffuse bilateral reticular
region** of the **ventral midbrain tegmentum** — the **midbrain
component** of the **reticular formation** — the **ARAS**
(arousal) and the **descending reticular formation**
(locomotion, postural control, pain modulation). It is **not a
discrete nucleus** — it is a **continuous region** of
**heterogeneous neurons** with **heterogeneous transmitters** and
**heterogeneous projections**. It is the **first "diffuse
bilateral region"** in the family — a **single leaf**, **not
paired**, **not midline** — and the tree represents it **cleanly**
as a **single leaf**. It carries **NO coupling warning** — same
rule as every non-oscillator class.

Associated Disorders
--------------------
The midbrain reticular formation has **no named syndrome of its
own** — its clinical associations are **direct** but usually
**not localizing** — the MRF is **rarely** the **sole** site of
pathology, and its diffuse nature makes **focal syndromes**
**uncommon**:

*   **Disorders of Arousal (INDIRECT — the ARAS is distributed):**
    **Coma**, **persistent vegetative state**, **minimally
    conscious state**, and **other disorders of consciousness**
    are **associated** with **dysfunction** of the **ascending
    reticular activating system (ARAS)** — the **MRF**, the
    **pons reticular formation**, the **medulla reticular
    formation**, the **thalamus** (intralaminar nuclei), and the
    **cortex** — **together**. **The MRF is ONE COMPONENT** of
    the ARAS — **lesions of the MRF alone** are **usually not
    sufficient** to produce **coma** (the **distributed ARAS**
    and the **thalamus** provide **redundancy**) — **diffuse
    bihemispheric** or **large brainstem** lesions are **usually
    required**. **The MRF is a contributor** to **arousal
    disorders** — **the ARAS is a distributed system**, not a
    single nucleus.

*   **Gait and Postural Disorders (INDIRECT — the MLR is a
    contributor):** **Gait disorders** and **postural
    instability** — especially in **Parkinson's disease**
    (**freezing of gait**), **progressive supranuclear palsy**,
    and **vascular parkinsonism** — are **associated** with
    **dysfunction** of the **MLR** (the **PPN** and the
    **cuneiform nucleus**). **The PPN** is a **target for deep
    brain stimulation** in **Parkinson's disease** — **to
    improve gait** and **postural control**. **The MRF is a
    contributor** to **gait disorders** — **the MLR (and the
    PPN) is one component** of the **gait-control system**.

*   **REM Sleep Behavior Disorder (INDIRECT — the PPN and the LDT
    are contributors):** **REM sleep behavior disorder (RBD)** —
    the **loss of REM atonia** — is **associated** with
    **dysfunction** of the **REM sleep control system** — the
    **PPN**, the **LDT**, the **sublateral dorsal nucleus**
    (pons), and the **precoeruleus region** — **together**.
    **The MRF is a contributor** to **RBD** — **the PPN and the
    LDT are one component** of the **REM sleep control system**.

*   **Pain (INDIRECT — the PAG and the RVM are the primary
    substrates):** **Descending pain modulation** is
    **primarily mediated** by the **PAG** and the **raphe
    magnus** (RVM) — **the MRF contributes** via its
    **projections** to the **PAG** and the **RVM**. **The MRF
    is a contributor** — **the PAG and the raphe magnus are the
    primary substrates**.

*   **Disorders of Consciousness — the Retikuläre
    Formation in Stroke (DIRECT — the MRF can be involved in
    brainstem strokes):** **Brainstem strokes** — **especially
    basilar artery territory** strokes — can **involve the MRF**
    along with **other brainstem structures** — producing
    **disorders of consciousness**, **gait disorders**, and
    **autonomic dysfunction**. **The MRF is a contributor** —
    **the syndrome is usually part of a broader brainstem
    stroke syndrome** (e.g., **locked-in syndrome**, **top of
    the basilar syndrome**, **Wallenberg syndrome**).

*   **No Named "Midbrain Reticular Formation Syndrome":** The MRF
    is a **diffuse reticular region** — it has **no named
    syndrome of its own**. Its clinical relevance is **direct**
    but **usually not localizing** — its **dysfunction** is
    **typically part of a broader brainstem syndrome** —
    **disorders of consciousness**, **gait disorders**,
    **RBD**, or **brainstem stroke syndromes**. **The MRF is a
    contributor** — **not a sole or primary substrate** for any
    of these. **No named midbrain reticular formation syndrome
    exists.**

**What is NOT here:** The MRF is **not** the substrate for
**disorders of consciousness as an MRF-exclusive syndrome**
(the **ARAS is distributed** — the **MRF is one component**),
**gait disorders as an MRF-exclusive syndrome** (the **MLR** —
including the **PPN** — is **one component** of the **gait-
control system**), **REM sleep behavior disorder as an
MRF-exclusive syndrome** (the **PPN** and the **LDT** are **one
component** of the **REM sleep control system**),
**descending pain modulation as an MRF-exclusive function**
(the **PAG** and the **raphe magnus** are the primary
substrates — the **MRF is a contributor**), **Parkinson's
disease** (the **substantia nigra pars compacta** — **NOT** the
MRF), **progressive supranuclear palsy** (the **SNr**, the
**riMLF**, the **midbrain tegmentum** — **NOT** the MRF as a
sole site), **saccade disorders** (the **SC**, the **SNr**, the
**riMLF** — **NOT** the MRF), **pupillary light reflex
deficits** (the **pretectum** and the **EW nucleus** — **NOT**
the MRF), **oculomotor palsy** (the **CN III nucleus** — **NOT**
the MRF), **trochlear palsy** (the **CN IV nucleus** — **NOT**
the MRF), **trigeminal sensory deficits** (the **trigeminal
ganglion**, the **main sensory**, and the **spinal trigeminal
nucleus** — **NOT** the MRF), **CCHS** (RTN), **OIRD**
(pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger
complex + arcuate nucleus), **essential hypertension /
sympathetic overactivity** (C1 group / RVLM), **Huntington's
disease** (striatum — telencephalon), or **Kluver-Bucy
syndrome** (amygdala). Its clinical relevance is **direct** but
**usually not localizing** — its **dysfunction** is
**typically part of a broader brainstem syndrome**. **No named
midbrain reticular formation syndrome exists.**

Lateralization Notes
--------------------
This is the **midbrain reticular formation** leaf — the **first
"diffuse bilateral region" leaf in the family**. The MRF is
**diffuse bilateral** — **not paired**, **not midline**. **It has
no left/right pair** (it is **one continuous region** spanning
both sides) **and no midline position** (it is **not a discrete
nucleus on the midline** — it extends laterally across both sides
of the tegmentum). **The tree represents it CLEANLY** — one leaf
under ``tegmentum/``, **no `left/` or `right/` nodes**. **No
coupling warning** — the same rule as every non-oscillator class.

*   **Diffuse Bilateral Region — NOT Paired, NOT Midline:** The
    MRF is a **single leaf** directly under ``tegmentum/`` —
    **NOT** under ``tegmentum/left/`` or ``tegmentum/right/``
    (not paired), **NOT** a **midline nucleus** (a single nucleus
    on the midline). It is a **continuous region** that **spans
    both sides** of the tegmentum. **It is the FIRST "diffuse
    bilateral region"** — a **third laterality class** in the
    family's taxonomy (paired, midline, diffuse bilateral).

*   **Cleanly Represented in the Tree:** The MRF is **cleanly
    represented** — the tree **already does** what the
    **tegmentum container amendment** should formalize: **a
    diffuse bilateral region is a single leaf** under
    ``tegmentum/``. **The MRF is the SECOND proof case for the
    tegmentum container amendment** — after the **midline
    nuclei** (the CLi, the DR, the IPN), **which the tree
    represents as paired** (anomalous), **the MRF provides a
    clean case** — a **diffuse bilateral region** correctly
    represented as a **single leaf**.

*   **Diffuse Position = Diffuse Function:** The MRF **integrates**
    multiple inputs and **projects** diffusely to multiple
    targets — it **spans both sides** as a **continuous
    reticular network** because it **integrates** and
    **projects** across **both sides**. **It has no "left half"
    and "right half"** — it is **one continuous region**.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to DIFFUSE RETICULAR REGIONS):** The
    **pre-Bötzinger complex** carries a **coupling warning**
    because it is an **oscillator** whose two sides must
    synchronize to produce a single rhythm. The **MRF** is a
    **diffuse reticular region** — a **single leaf** — it does
    **not** generate a rhythm, so it does **not** carry the
    **oscillator coupling warning**. There are **no "two sides"
    to couple** — the MRF is **one continuous region** whose
    **diffuse projections** carry its functions to **both sides**.
    **Diffuse reticular regions carry NO coupling warning** —
    same rule as every non-oscillator class.

*   **No SLEA Warning:** The MRF is **SLEA-free** — it is **not**
    an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The MRF is **not** part
    of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The MRF is **not** a
    rhinencephalon structure.

**The MRF is the FIRST "diffuse bilateral region" leaf in the
family** — its **diffuse bilateral position**, **diffuse reticular
class**, **clean representation in the tree**, and **no coupling
warning** establish the **canonical structural pattern** for
diffuse bilateral regions. **The PAG** — a **diffuse column**
around the aqueduct — is **potentially** a **second diffuse
bilateral region**, depending on the on-disk tree. **The tegmentum
container amendment should permit BOTH midline nuclei AND diffuse
bilateral regions as direct children** — **and the MRF is the
existing evidence** that **diffuse bilateral regions** are
(correctly) represented as **single leaves**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The MRF is **diffuse
    bilateral** — there is **no** other side to import from (it
    is **one continuous region**).
*   **No cross-lobe imports.** This module does **not** import from
    the **PAG**, the **tectum**, the **pretectum**, the **cerebral
    peduncle**, the **cerebral aqueduct**, the **pontine reticular
    formation**, the **medullary reticular formation**, the **red
    nucleus**, the **substantia nigra**, the **VTA**, the **CLi**,
    the **DR**, the **IPN**, the **CN nuclei**, the **PAG**, the
    **RVM**, the **thalamus**, the **basal forebrain**, or any
    other container. The MRF's relationships to the PAG, the
    tectum, the pretectum, the cerebral peduncle, the cerebral
    aqueduct, the pontine reticular formation, the medullary
    reticular formation, the red nucleus, the substantia nigra,
    the VTA, the CLi, the DR, the IPN, the CN nuclei, the RVM,
    the thalamus, and the basal forebrain are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **cholinergic phenotype** (of the PPN and the LDT), the
    **glutamatergic phenotype** (of the cuneiform and subcuneiform
    nuclei), and the other **transmitter phenotypes** of the MRF
    neurons are **``chemicals_hormones``-layer facts** —
    documented as **prose**, **never imported**. **CHEMICALS-LAYER
    DISCIPLINE** is preserved.
*   **DIFFUSE BILATERAL REGION — a third laterality class.** The
    MRF is a **single leaf** directly under ``tegmentum/`` —
    **NOT** under ``tegmentum/left/`` or ``tegmentum/right/``
    (not paired), **NOT** a **midline nucleus** (a single nucleus
    on the midline). It is a **continuous region** that **spans
    both sides** of the tegmentum. **This is a THIRD laterality
    class** — **diffuse bilateral** — beyond **paired** and
    **midline**.
*   **CLEAN CASE — the MRF is represented correctly.** The tree
    represents the MRF **cleanly** — a **single leaf** under
    ``tegmentum/``, **no `left/` or `right/` nodes** — and this
    is the **anatomically correct representation**. **The MRF is
    the SECOND proof case for the tegmentum container
    amendment** — beyond the midline nuclei, **diffuse bilateral
    regions can also be single leaves** under ``tegmentum/`` —
    and the tree **already represents the MRF this way**.
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER — TWO exception
    categories.** The tegmentum container's **paired-leaf rule**
    — *"each tegmentum nucleus is a paired structure (a
    ``left/`` leaf and a ``right/`` leaf)"* — should be
    **AMENDED** to permit **BOTH**:
    *   **Midline nuclei** (the **CLi**, the **DR**, the
    **IPN**) — **single leaves** because they are **discrete
    nuclei on the midline**.
    *   **Diffuse bilateral regions** (the **MRF**; **potentially**
    the **PAG**) — **single leaves** because they are
    **continuous regions spanning both sides**.
    **Midline nuclei and diffuse bilateral regions are PERMITTED
    as direct children of ``tegmentum/``** — **not required** to
    be under ``left/`` or ``right/``. **The MRF is the existing
    evidence** that **diffuse bilateral regions** are
    (correctly) represented as **single leaves**.
*   **LIVE AMENDMENT TO THE MIDBRAIN CONTAINER — reinforce.** The
    midbrain container's PAG prose — *"the cerebral aqueduct and
    the periaqueductal gray are midline structures, not paired"*
    — and the tegmentum container's paired-leaf rule — *"the PAG
    is midline-adjacent but is treated as paired in the tree"* —
    are **still inconsistent with each other**. **The MRF is a
    clean third data point** — a **diffuse bilateral region**
    represented cleanly. **Both containers should be reconciled**
    to accommodate **paired**, **midline**, **and diffuse
    bilateral** structures consistently.
*   **DIFFUSE RETICULAR REGION — a new structure class.** The MRF
    is a **diffuse reticular region** — **distinct** from
    **discrete nuclei** (SN, VTA, red nucleus, CN nuclei, DR,
    CLi, IPN, LC), **sensory relays** (IC, pretectum),
    **modulatory nuclei** (DR, CLi, LC, VTA, SNc), **limbic
    relays** (IPN), **sensorimotor integration structures** (SC),
    and **conduction pathways** (MLF, tectobulbar, brachia,
    cerebral peduncle). It is a **continuous reticular network**
    of **heterogeneous neurons** with **heterogeneous
    transmitters** and **heterogeneous projections**.
*   **SUBNUCLEAR / SUBREGION DISCIPLINE — subregions are PROSE, not
    structural children.** The **cuneiform nucleus**, the
    **subcuneiform nucleus**, the **pedunculopontine nucleus**,
    the **laterodorsal tegmental nucleus**, and the **MRF proper**
    are **subregions** of a **continuous region** — **not
    discrete nuclei**, **not structural children**. **A diffuse
    region cannot be resolved into discrete children** — its
    subregions are **prose**. The **MLR** (the cuneiform +
    subcuneiform + PPN) is a **functional subregion** — also
    **prose**, **not a structural child**.
*   **NO COUPLING WARNING — diffuse reticular regions carry NO
    coupling warning.** The MRF is a **single leaf** — a **diffuse
    reticular region** — it does **not** generate a rhythm. **The
    diffuse bilateral position is not a coupling hazard** — it is
    the structural fact of a **diffuse region** that **integrates**
    inputs and **projects** to **bilateral targets**.
*   **NOT A CN NUCLEUS.** The MRF is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. It has **one path only**.
*   **NOT a discrete nucleus — a DIFFUSE REGION.** The MRF is
    **not** a **discrete nucleus** with a **single transmitter**
    and a **single function** — it is a **diffuse region** with
    **heterogeneous** transmitters and **heterogeneous**
    functions.
*   **NOT the PAG — the PAG SURROUNDS the cerebral aqueduct, and the
    MRF is VENTRAL to it.**
*   **NOT the pontine or medullary reticular formation — those are
    HINDBRAIN reticular regions** at **different levels** of the
    brainstem.
*   **NOT the MLR as a separate structure — the MLR is a SUBREGION
    of the MRF.**
*   **NOT the PPN or the LDT as separate structural children —
    they are SUBREGIONS of the MRF.**
*   **NOT the red nucleus, the substantia nigra, or the VTA —
    those are DISCRETE NUCLEI of the tegmentum.**
*   **NOT the CLi, the DR, or the IPN — those are MIDLINE nuclei.**
*   **NOT the superior colliculus or the inferior colliculus —
    those are TECTUM structures.**
*   **NOT the pretectum — the pretectum is a separate region at the
    diencephalon-midbrain junction.**
*   **NOT the cerebral peduncle or the cerebral aqueduct — those
    are VENTRAL / DORSAL boundaries of the tegmentum.**
*   **CHEMICALS-LAYER DISCIPLINE.** The **cholinergic**,
    **glutamatergic**, **GABAergic**, and **peptidergic**
    phenotypes of the MRF neurons are **``chemicals_hormones``-
    layer facts** — documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The MRF is a
    **local diffuse bilateral leaf** under the tegmentum — no
    cross-listing.
*   **No nested cross-listing.** The MRF is a **single leaf**. It
    is **not** a container.
*   **The on-disk tree is authoritative.** The on-disk tree has
    ``.../tegmentum/midbrain_reticular_formation/`` — **one
    leaf**, **diffuse bilateral**, **no `left/` or `right/`**.
    **This is the correct representation** — the MRF is a
    **diffuse bilateral region**, and the tree represents it
    cleanly. **If the tree ever represents the MRF as paired**
    (with `left/` and `right/` nodes), **that would be a
    tree-structural anomaly of the same kind the CLi, DR, and
    IPN represent** — but for a **different anatomical reason**
    (diffuse, not midline). **The MRF should be a single leaf** —
    consistent with its anatomy.

Usage
-----
Resolve the leaf by path (**one** path only — the MRF is **diffuse
bilateral**, **not** under `left/` or `right/`)::

    from infrastructure.brainparts.midbrain.tegmentum import midbrain_reticular_formation

Or by fully-qualified path string::

    path = "midbrain.tegmentum.midbrain_reticular_formation"

**Do not** assume the MRF is under
``tegmentum/midbrain_reticular_formation/left/`` or
``tegmentum/midbrain_reticular_formation/right/``. **It is a DIFFUSE
BILATERAL REGION** — a **single leaf** directly under
``tegmentum/``. **The tree represents it cleanly.** **The MRF is
the SECOND proof case for the tegmentum container amendment** —
beyond the midline nuclei (which the tree represents as paired,
anomalous), **diffuse bilateral regions can also be single
leaves** — and the tree **already represents the MRF this way**.

**Do not** assume the MRF is a **paired structure** — it is **not**
— it is a **continuous diffuse region** spanning both sides, not
two separate structures on the left and right.

**Do not** assume the MRF is a **midline nucleus** — it is **not**
— it is **not a discrete nucleus on the midline**; it **extends
laterally** across both sides of the tegmentum.

**Do not** assume the MRF is a **discrete nucleus** with a
**single transmitter** and a **single function** — it is a
**diffuse reticular region** with **heterogeneous transmitters**
and **heterogeneous functions** (arousal, locomotion,
sensorimotor integration, pain modulation).

**Do not** assume the MRF is a **cranial nerve nucleus** — it is
**not** and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the MRF is the **PAG**. The **PAG** surrounds the
cerebral aqueduct — it is **dorsal** to the MRF. The **MRF is
ventral to the PAG** — in the **ventral tegmentum**. **They are
DIFFERENT DIFFUSE REGIONS in DIFFERENT positions.**

**Do not** assume the MRF is the **pontine reticular formation** or
the **medullary reticular formation**. Those are **hindbrain**
reticular regions at **different levels** — the **MRF is midbrain**.

**Do not** assume the MRF is the **MLR** as a separate structure.
The **MLR** is a **subregion** of the MRF — the **cuneiform
nucleus**, the **subcuneiform nucleus**, and the
**pedunculopontine nucleus** — **documented as prose**, not as a
structural child.

**Do not** assume the MRF is the **PPN** or the **LDT** as separate
structural children. The **PPN** and the **LDT** are **cholinergic
subregions** of the MRF — **documented as prose**, not as
structural children.

**Do not** assume the MRF is the **red nucleus**, the **substantia
nigra**, or the **VTA** — those are **discrete nuclei** of the
tegmentum. **The MRF is a diffuse reticular region** — a
**different structure class**.

**Do not** assume the MRF is the **CLi**, the **DR**, or the
**IPN** — those are **midline nuclei**. **The MRF is a diffuse
bilateral region** — a **different laterality class**.

**Do not** assume the MRF is the **superior colliculus** or the
**inferior colliculus** — those are **tectum** structures, **dorsal**
to the aqueduct. **The MRF is a tegmentum structure**, **ventral**
to the aqueduct.

**Do not** assume the MRF is the **pretectum** — the pretectum is a
**separate region** at the diencephalon-midbrain junction.
**Different regions, different functional systems.**

**Do not** assume the MRF is the **cerebral peduncle** or the
**cerebral aqueduct** — those are **ventral / dorsal boundaries**
of the tegmentum. **The MRF is the diffuse reticular region
between them.**

**Do not** import the **cholinergic**, **glutamatergic**,
**GABAergic**, or **peptidergic** phenotypes into the midbrain
structural layer. Those are **``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the MRF. **Diffuse
reticular regions carry NO coupling warning** — same rule as every
non-oscillator class. **The diffuse bilateral position is not a
coupling hazard.**

**Do not** treat the MRF as a **paired structure** or a **midline
nucleus**. It is a **diffuse bilateral region** — a **single
leaf** — the **third laterality class**.

Iterating the midbrain reticular formation's (empty) children
(recommended consumer pattern)::

    MIDBRAIN_RETICULAR_FORMATION_CHILDREN = ()
    # The midbrain reticular formation is a leaf. The subregions
    # (cuneiform nucleus, subcuneiform nucleus, pedunculopontine
    # nucleus, laterodorsal tegmental nucleus, MRF proper) are
    # prose, not modules. The MLR (the cuneiform + subcuneiform +
    # PPN) is a functional subregion — also prose, not a module.

Bilateral iteration — **NOT APPLICABLE**::

    # The midbrain reticular formation is DIFFUSE BILATERAL — it
    # has NO left/right pair (not paired) and NO midline position
    # (it extends laterally across both sides). There is no
    # bilateral iteration for the MRF. If you find yourself writing:
    #
    #     for side in ("left", "right"):
    #         path = f"midbrain.tegmentum.{side}.midbrain_reticular_formation"
    #
    # — that is WRONG. The MRF is at:
    #
    #     midbrain.tegmentum.midbrain_reticular_formation
    #
    # — a single diffuse bilateral leaf. The tree represents the
    # MRF correctly. (This is the THIRD laterality class — paired,
    # midline, diffuse bilateral — beyond the paired structures
    # like the SN and the midline structures like the DR.)

Reaching the PAG (recommended consumer pattern — the DORSAL diffuse
region)::

    # The periaqueductal gray (PAG) SURROUNDS the cerebral aqueduct
    # — it is a DIFFUSE COLUMN around the aqueduct — its laterality
    # depends on the on-disk tree (potentially midline, paired, or
    # diffuse bilateral):
    #
    #   brainparts.midbrain.tegmentum.left.periaqueductal_gray
    #   brainparts.midbrain.tegmentum.right.periaqueductal_gray
    #   (OR: brainparts.midbrain.tegmentum.periaqueductal_gray —
    #    depending on the on-disk tree)
    #
    # The PAG is DORSAL to the MRF. The MRF projects to the PAG for
    # pain modulation. The PAG is a DIFFERENT diffuse region — pain
    # modulation and defensive behavior (PAG) vs. arousal and
    # locomotion (MRF).

Reaching the pontine reticular formation (recommended consumer
pattern — the CAUDAL reticular region)::

    # The pontine reticular formation is a HINDBRAIN reticular
    # region — CAUDAL to the midbrain:
    #
    #   brainparts.hindbrain.metencephalon.pons.pontine_reticular_formation
    #
    # The pontine reticular formation is the CAUDAL continuation of
    # the MRF — same reticular formation, different level. The MRF
    # is MIDBRAIN; the pontine reticular formation is PONS. The
    # boundaries between them are conventionally defined by the
    # pontomesencephalic junction.

Reaching the medullary reticular formation (recommended consumer
pattern — the CAUDAL reticular region)::

    # The medullary reticular formation is a HINDBRAIN reticular
    # region — CAUDAL to the pons:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.medullary_reticular_formation
    #
    # The medullary reticular formation is the CAUDAL continuation of
    # the pontine reticular formation — same reticular formation,
    # different level. The MRF is MIDBRAIN; the medullary reticular
    # formation is MEDULLA.

Reaching the MLR (recommended consumer pattern — the SUBREGION,
documented as prose)::

    # The mesencephalic locomotor region (MLR) is a SUBREGION of the
    # MRF — the cuneiform nucleus, the subcuneiform nucleus, and the
    # pedunculopontine nucleus (PPN) — the locomotion initiation
    # region. It is DOCUMENTED AS PROSE in the MRF leaf — NOT as a
    # separate container.
    #
    # Do not attempt to resolve the MLR as a sub-path of the MRF —
    # it is prose, not a module.

Reaching the PPN and the LDT (recommended consumer pattern — the
SUBREGIONS, documented as prose)::

    # The pedunculopontine nucleus (PPN) and the laterodorsal
    # tegmental nucleus (LDT) are cholinergic SUBREGIONS of the MRF
    # — involved in locomotion, arousal, and REM sleep. They are
    # DOCUMENTED AS PROSE in the MRF leaf — NOT as separate
    # containers.
    #
    # Do not attempt to resolve the PPN or the LDT as sub-paths of
    # the MRF — they are prose, not modules.

Reaching the red nucleus, the substantia nigra, and the VTA
(recommended consumer pattern — the DISCRETE NUCLEI of the
tegmentum)::

    # The red nucleus, the substantia nigra, and the VTA are
    # DISCRETE NUCLEI of the tegmentum — PAIRED:
    #
    #   brainparts.midbrain.tegmentum.left.red_nucleus
    #   brainparts.midbrain.tegmentum.right.red_nucleus
    #   brainparts.midbrain.tegmentum.left.substantia_nigra
    #   brainparts.midbrain.tegmentum.right.substantia_nigra
    #   brainparts.midbrain.tegmentum.left.ventral_tegmental_area
    #   brainparts.midbrain.tegmentum.right.ventral_tegmental_area
    #
    # The red nucleus, the SN, and the VTA are DISCRETE NUCLEI —
    # sharply bounded, specific transmitters, specific projections.
    # The MRF is a DIFFUSE REGION — heterogeneous transmitters,
    # heterogeneous projections. DIFFERENT structure classes.

Reaching the CLi, the DR, and the IPN (recommended consumer
pattern — the MIDLINE nuclei)::

    # The caudal linear nucleus (CLi), the dorsal raphe nucleus
    # (DR), and the interpeduncular nucleus (IPN) are MIDLINE
    # nuclei — single midline leaves:
    #
    #   brainparts.midbrain.tegmentum.caudal_linear_nucleus
    #   brainparts.midbrain.tegmentum.dorsal_raphe_nucleus
    #   brainparts.midbrain.tegmentum.interpeduncular_nucleus
    #
    # The CLi, the DR, and the IPN are MIDLINE NUCLEI — discrete
    # nuclei on the midline. The MRF is a DIFFUSE BILATERAL
    # REGION — not a midline nucleus. DIFFERENT laterality classes
    # (midline vs. diffuse bilateral).

Reaching the superior colliculus and the inferior colliculus
(recommended consumer pattern — the TECTUM structures)::

    # The superior colliculus and the inferior colliculus are
    # TECTUM structures — DORSAL to the cerebral aqueduct:
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #   brainparts.midbrain.tectum.right.superior_colliculus
    #   brainparts.midbrain.tectum.left.inferior_colliculus
    #   brainparts.midbrain.tectum.right.inferior_colliculus
    #   (OR: brainparts.midbrain.tectum.corpora_quadrigemina.left.superior_colliculus, etc.)
    #
    # The colliculi are TECTUM structures — DIFFERENT compartment
    # from the MRF, which is a TEGMENTUM structure. The colliculi
    # are DORSAL to the aqueduct; the MRF is VENTRAL.

Subregion detail (not wired — consult references)::

    # The midbrain reticular formation has FUNCTIONAL SUBREGIONS —
    # anatomical subdivisions of a continuous region, NOT discrete
    # nuclei:
    #
    #   cuneiform nucleus (CnF)          -> GLUTAMATERGIC —
    #                                       locomotion initiation
    #                                       (MLR component);
    #                                       defensive behavior;
    #                                       cardiovascular control
    #   subcuneiform nucleus (SubCnF)    -> GLUTAMATERGIC —
    #                                       locomotion;
    #                                       cardiovascular control;
    #                                       MLR component
    #   pedunculopontine nucleus (PPN)   -> CHOLINERGIC +
    #                                       GLUTAMATERGIC —
    #                                       locomotion (MLR);
    #                                       arousal (ARAS); REM sleep
    #   laterodorsal tegmental nucleus   -> CHOLINERGIC — REM sleep;
    #     (LDT)                             arousal (ARAS)
    #   MRF proper (diffuse remainder)   -> HETEROGENEOUS —
    #                                       glutamatergic, GABAergic,
    #                                       peptidergic — sensorimotor
    #                                       integration; arousal; pain
    #                                       modulation (via PAG, RVM)
    #
    # ALL of these subregions are SUBDIVISIONS of a continuous
    # diffuse region — NOT discrete nuclei. The MRF's subnuclear
    # organization REINFORCES its diffuse-region representation.
    #
    # Do not attempt to resolve these subregions as sub-paths of
    # the midbrain reticular formation — they are PROSE, not
    # modules.

The MRF's place in the ARAS and descending reticular formation —
detail (not wired — consult references)::

    # The midbrain reticular formation is the MIDBRAIN COMPONENT of
    # the RETICULAR FORMATION — a DISTRIBUTED system spanning:
    #
    #   ARAS (ascending reticular activating system) — AROUSAL:
    #     - MRF (midbrain) — cholinergic (PPN, LDT), glutamatergic
    #     - pontine reticular formation
    #     - medullary reticular formation
    #     - cholinergic (PPN, LDT), noradrenergic (LC), serotonergic
    #       (DR) components
    #     - PROJECTS TO: thalamus (intralaminar, reticular),
    #       hypothalamus, basal forebrain, cortex
    #
    #   DESCENDING RETICULAR FORMATION — LOCOMOTION, POSTURE,
    #   PAIN MODULATION:
    #     - MRF (midbrain) — cuneiform, subcuneiform (locomotion,
    #       via reticulospinal); MRF proper (pain, via PAG and RVM)
    #     - pontine reticular formation
    #     - medullary reticular formation
    #     - raphe magnus, RVM (pain modulation)
    #     - PROJECTS TO: spinal cord (reticulospinal);
    #       PAG; RVM
    #
    # The MRF is ONE COMPONENT of the reticular formation — NOT the
    # whole system. The reticular formation is anatomically
    # continuous across the three levels (midbrain, pons, medulla)
    # — the tree represents each level as a SEPARATE REGION, and
    # the boundaries are conventionally defined by the
    # pontomesencephalic and pontomedullary junctions.
    #
    # Do not attempt to resolve the pontine reticular formation or
    # the medullary reticular formation as sub-paths of the MRF —
    # they are DIFFERENT structures at DIFFERENT levels.

Clinical-pattern detail (not wired — consult references)::

    # The midbrain reticular formation has NO NAMED SYNDROME OF ITS
    # OWN — its clinical associations are DIRECT but usually NOT
    # LOCALIZING — the MRF is RARELY the SOLE site of pathology:
    #
    #   DISORDERS OF AROUSAL         -> INDIRECT — the ARAS is
    #     (coma, vegetative state,       DISTRIBUTED; the MRF is ONE
    #      minimally conscious state)     COMPONENT; diffuse
    #                                     bihemispheric or large
    #                                     brainstem lesions are usually
    #                                     required
    #   GAIT AND POSTURAL DISORDERS  -> INDIRECT — the MLR (PPN,
    #     (Parkinson's freezing of       cuneiform) is a CONTRIBUTOR;
    #      gait, PSP, vascular            PPN is a DBS target
    #      parkinsonism)
    #   REM SLEEP BEHAVIOR DISORDER  -> INDIRECT — the PPN and LDT
    #     (RBD)                          are CONTRIBUTORS; the
    #                                     sublateral dorsal nucleus
    #                                     (pons) is also involved
    #   PAIN (descending)            -> INDIRECT — the PAG and the
    #                                     RVM are PRIMARY substrates;
    #                                     the MRF is a CONTRIBUTOR
    #   BRAINSTEM STROKES            -> DIRECT — the MRF can be
    #     (basilar artery territory)     involved; the syndrome is
    #                                     usually part of a broader
    #                                     brainstem stroke syndrome
    #   PARKINSON'S DISEASE          -> the SNc is the PRIMARY
    #                                     substrate; the MRF (via
    #                                     the PPN) is a TARGET for
    #                                     gait DBS
    #
    # No named midbrain reticular formation syndrome exists. The
    # MRF is a CONTRIBUTOR — not a sole or primary substrate for
    # any of these.
    #
    # Do not conflate these patterns — they localize primarily to
    # the ARAS as a distributed system, the MLR, the PAG, or the
    # SNc — not to the MRF alone.

The clean diffuse-bilateral representation — detail (not wired —
structural note)::

    # The midbrain reticular formation is the FIRST CLEANLY-
    # REPRESENTED DIFFUSE BILATERAL REGION in the tree:
    #
    #   midbrain.tegmentum.midbrain_reticular_formation
    #     (ONE leaf — DIFFUSE BILATERAL — NO left/ or right/ nodes)
    #
    # This is the CORRECT representation — the MRF is a continuous
    # diffuse region spanning both sides, not a paired structure
    # and not a midline nucleus.
    #
    # THE THIRD LATERALITY CLASS — beyond:
    #   PAIRED             -> left/ + right/ leaves (SN, VTA, red
    #                         nucleus, CN nuclei, etc.)
    #   MIDLINE            -> single midline leaf (CLi, DR, IPN —
    #                         which the tree currently represents
    #                         as paired, anomalous — see their
    #                         left/ and right/ modules)
    #   DIFFUSE BILATERAL  -> single leaf, continuous region
    #                         spanning both sides (MRF — THIS LEAF;
    #                         potentially the PAG)
    #
    # THE MRF IS THE SECOND PROOF CASE for the tegmentum container
    # amendment — beyond the midline nuclei, DIFFUSE BILATERAL
    # REGIONS can also be single leaves, and the tree ALREADY
    # represents the MRF this way. The tegmentum container
    # amendment should permit BOTH midline nuclei AND diffuse
    # bilateral regions as direct children — not require them to be
    # under left/ or right/.
    #
    # The MRF's clean representation is the EXISTING EVIDENCE that
    # the tree can represent single leaves correctly — for DIFFUSE
    # BILATERAL REGIONS at least. The same principle — SINGLE LEAF
    # FOR A STRUCTURE THAT IS NOT A PAIRED NUCLEUS — applies to the
    # midline nuclei, which should follow the same clean pattern
    # (Resolution B for the CLi, DR, and IPN).

References
----------
*   **Canonical reticular formation anatomy:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (The reticular formation — its diffuse nature, its
    heterogeneous neurons, its heterogeneous projections, its
    ascending (ARAS) and descending (reticulospinal) components;
    the midbrain, pontine, and medullary levels.)
*   **Reticular formation — comprehensive review:** Moruzzi, G.,
    Magoun, H.W. (1949). "Brain stem reticular formation and
    activation of the EEG." *Electroencephalography and Clinical
    Neurophysiology* 1:455–473. (The **original description** of
    the **ascending reticular activating system (ARAS)** — the
    brainstem reticular formation and cortical arousal.)
*   **Reticular formation — modern review:** Steriade, M. (1996).
    "Arousal: revisiting the reticular activating system."
    *Science* 272:225–226. (The modern view of the ARAS — the
    reticular formation, the thalamus, and the cortex — and the
    distributed nature of arousal.)
*   **Mesencephalic locomotor region (MLR):** Shik, M.L.,
    Severin, F.V., Orlovsky, G.N. (1966). "Control of walking and
    running by means of electrical stimulation of the midbrain."
    *Biophysics* 11:756–765. (The **original description** of the
    **MLR** — the mesencephalic locomotor region — and the
    initiation of locomotion by stimulation of the midbrain
    reticular formation.)
*   **MLR — modern review:** Takakusaki, K. (2017). "Functional
    neuroanatomy for posture and gait control." *Journal of
    Movement Disorders* 10:1–17. (The MLR — the cuneiform
    nucleus, the subcuneiform nucleus, and the pedunculopontine
    nucleus — and its role in locomotion and posture.)
*   **Pedunculopontine nucleus (PPN):** Garcia-Rill, E. (1991).
    "The pedunculopontine nucleus." *Progress in Neurobiology*
    36:363–389. (The PPN — the cholinergic subregion of the MRF —
    its role in locomotion, arousal, and REM sleep.)
*   **Pedunculopontine nucleus — Parkinson's DBS:** Stefani, A.,
    Lozano, A.M., Peppe, A., et al. (2007). "Bilateral deep brain
    stimulation of the pedunculopontine and subthalamic nuclei in
    severe Parkinson's disease." *Brain* 130:1596–1607. (The PPN
    as a **DBS target** for **gait and postural control** in
    **Parkinson's disease**.)
*   **Laterodorsal tegmental nucleus (LDT):** Kayama, Y., Koyama,
    Y. (2003). "Control of sleep and wakefulness by cholinergic
    systems in the brainstem." *Sleep and Biological Rhythms*
    1:95–103. (The LDT — the cholinergic subregion of the MRF —
    its role in REM sleep and arousal.)
*   **Cuneiform nucleus and defensive behavior:** Mitchell, I.J.,
    Dean, P., Redgrave, P. (1988). "The role of the cuneiform
    nucleus in the expression of defensive behavior." *Neuroscience
    & Biobehavioral Reviews* 12:129–138. (The cuneiform nucleus —
    the glutamatergic subregion of the MRF — its role in
    locomotion and defensive behavior.)
*   **Subcuneiform nucleus:** Redgrave, P., Dean, P., Taha, E.B.,
    et al. (1986). "Studies on the roles of the cuneiform nucleus
    and the subcuneiform nucleus in the expression of defensive
    behavior." *Neuroscience* 17:393–407. (The subcuneiform
    nucleus — the glutamatergic subregion of the MRF — its role
    in locomotion and cardiovascular control.)
*   **Reticulospinal pathways:** Matsuyama, K., Mori, F., Nakajima,
    K., et al. (2004). "Locomotor role of the corticoreticular-
    reticulospinal-spinal interneuron system." *Progress in Brain
    Research* 143:239–249. (The reticulospinal pathways — the
    descending component of the MRF — and their role in
    locomotion.)
*   **Descending pain modulation (contrast — the PAG and the
    RVM):** Fields, H.L., Basbaum, A.I. (1978). "Brainstem control
    of spinal pain-transmission neurons." *Annual Review of
    Physiology* 40:217–248. (The descending pain-modulation
    system — the PAG, the RVM, and the raphe magnus — the MRF
    contributes via projections to the PAG and the RVM.)
*   **Disorders of consciousness — the ARAS:** Plum, F., Posner,
    J.B. (1980). *The Diagnosis of Stupor and Coma*, 3rd ed. (The
    ARAS — the reticular formation — and disorders of
    consciousness; the distributed nature of arousal.)
*   **Brainstem strokes — the MRF:** Bogousslavsky, J., Caplan,
    L.R. (2001). *Stroke Syndromes*, 2nd ed. (The brainstem stroke
    syndromes — including the MRF involvement in basilar artery
    strokes; the broader brainstem stroke syndromes.)
*   **PAG (contrast — the DORSAL diffuse region):** Behbehani, M.M.
    (1995). "Functional characteristics of the midbrain
    periaqueductal gray." *Progress in Neurobiology* 46:575–605.
    (The PAG — the diffuse column around the aqueduct — pain
    modulation and defensive behavior; a DIFFERENT diffuse region
    from the MRF.)
*   **Pontine and medullary reticular formation (contrast — the
    CAUDAL reticular regions):** Siegel, J.M. (2004). "The
    neurotransmitters of sleep." *Journal of Clinical Psychiatry*
    65 (Suppl. 16):4–7. (The pontine and medullary reticular
    formation — the caudal continuations of the reticular
    formation — and their roles in sleep and arousal.)
*   **SLEA (contrast — the MRF is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the midbrain reticular formation.)
*   NeuroNames — Midbrain reticular formation; FMA — Midbrain
    reticular formation. **The MRF is a diffuse region — it has
    no "left" or "right" subdivision in the standard anatomical
    atlases; it is a continuous region spanning both sides of the
    midbrain tegmentum.**
"""