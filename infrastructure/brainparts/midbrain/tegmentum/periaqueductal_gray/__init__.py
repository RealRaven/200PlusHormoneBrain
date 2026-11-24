"""
infrastructure.brainparts.midbrain.tegmentum.periaqueductal_gray
===============================================================

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
        ├── midbrain_reticular_formation
        │   ├── (diffuse bilateral leaf)
        │   ├── left               (anomalous)
        │   └── right              (anomalous)
        └── periaqueductal_gray       <-- THIS MODULE (DIFFUSE
                                          BILATERAL LEAF — CLEANLY
                                          REPRESENTED — NO left/ or
                                          right/ nodes — the ACTUAL
                                          clean case for the diffuse
                                          bilateral category)

**Primary synonym:** Periaqueductal gray; **PAG**; **periaqueductal
grey matter**; **PAGM**; **central gray** (older term);
**substantia grisea centralis** (Latin); **mesencephalic central
gray**.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). **Not a discrete nucleus.** A **diffuse bilateral
modulatory column** of **gray matter** — a **continuous column**
surrounding the **cerebral aqueduct** — in the **midbrain
tegmentum**, extending from the **diencephalon-midbrain junction**
(rostral) to the **pontomesencephalic junction** (caudal). It is
composed of a **heterogeneous population** of neurons —
**glutamatergic**, **GABAergic**, **dopaminergic**, **serotonergic**,
**cholinergic**, **opioid-containing**, **peptidergic** —
organized as **distinct longitudinal columns** (dorsal, lateral,
ventrolateral, dorsomedial) with **different functions**. **It has
no single transmitter**, **no single projection**, and **no sharp
boundaries** — this is what makes it a **diffuse region** rather
than a **nucleus**. **No transmitter or neurochemical phenotype is
imported** — the **GABAergic**, **glutamatergic**, **opioid**,
**dopaminergic**, **serotonergic**, and **cholinergic** phenotypes
of the PAG neurons are **``chemicals_hormones``-layer facts** — see
*Chemicals-Layer Discipline*.
**Container status:** **This module is a LEAF** — **a diffuse
bilateral region**. It is **NOT** under ``tegmentum/left/`` or
``tegmentum/right/`` — it sits **directly under** the tegmentum
container. **It is the SECOND diffuse bilateral region in the
family** — after the **midbrain reticular formation** — **and it is
the ACTUAL CLEAN CASE for the diffuse bilateral category.** Where
the **MRF** claimed to be clean and was **falsified** (its own
`left/` and `right/` nodes contradicted its claim), **the PAG is
actually clean** — the on-disk path is a **single leaf**, and the
tree represents it **exactly as its anatomy demands**.
**Part of:** The **tegmentum** region container — as a **diffuse
bilateral** leaf. **The PAG is NOT a cranial nerve nucleus** and is
**NOT cross-listed** with ``cranial_nerve_nuclei/``.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — **diffuse bilateral**, **not**
a side container.
**Structural children:** **None.** This is a **leaf** module. The
**subregions** (dorsal PAG, lateral PAG, ventrolateral PAG,
dorsomedial PAG) are documented as **prose**, not as structural
children. **A diffuse region cannot be resolved into discrete
children** — its **subregions** are **anatomical subdivisions of a
continuous region**, not **discrete nuclei**. See *Subregions
(prose, not structural children)* and *Diffuse-Region Discipline*.
**Boundary status (DIFFUSE BILATERAL REGION — the SECOND diffuse
bilateral region, after the MRF):** **Boundary case — the
periaqueductal gray is a DIFFUSE BILATERAL REGION.** It is a
**continuous column** of gray matter surrounding the **cerebral
aqueduct** — it **spans both sides of the midbrain** as a
**continuous region**. It is **NOT a paired structure** (there is
no "left PAG" and "right PAG" — it is **one continuous column**
surrounding the aqueduct), and it is **NOT a midline nucleus** (it
is **not a discrete nucleus on the midline** — it **surrounds the
aqueduct** and **extends laterally** into the adjacent tegmentum).
**The PAG is the SECOND diffuse bilateral region** — after the
**midbrain reticular formation** (the **first** diffuse bilateral
region). **Both are diffuse bilateral regions** — **single leaves**
that **span both sides** as **continuous regions** — **neither
paired, neither midline**. **They are functionally distinct** — the
**MRF** is the **reticular** diffuse region (arousal, locomotion,
sensorimotor integration); the **PAG** is the **modulatory** diffuse
region (pain modulation, defensive behavior, autonomic control).
**They are DIFFERENT STRUCTURES of the SAME laterality class** —
both **diffuse bilateral**. Consumers must **not** assume the PAG
is paired (it is **not** — no `left/`/`right/` nodes) and must
**not** assume it is a discrete midline nucleus (it is **not** — it
surrounds the aqueduct and extends laterally). See *The Second
Diffuse Bilateral Region* and *The PAG Settles the Two Container
Contradictions*.
**Boundary status (THE ACTUAL CLEAN CASE — the PAG is genuinely
cleanly represented, and it is the real proof case for the diffuse
bilateral category):** **Boundary case — the periaqueductal gray is
CLEANLY REPRESENTED in the tree** — a **single leaf** under
``tegmentum/`` — **no `left/` or `right/` nodes** — **and this is
the anatomically correct representation**. **The PAG is the ACTUAL
clean case for the diffuse bilateral category** — **not the
claimed-then-falsified clean case the MRF provided, but the
genuinely clean case the tree has had all along.** The MRF claimed
to be the clean case and was **falsified** by its own `left/` and
`right/` nodes (the MRF `left/` and `right/` modules explicitly say
*"the diffuse bilateral category has NO ON-DISK EVIDENCE
remaining"*). **The PAG is the ON-DISK EVIDENCE the MRF could not
be** — **the tree represents the PAG as a single leaf, and it
always has**. **The PAG is the NEW proof case** for the **diffuse
bilateral category** of the tegmentum container amendment —
**taking over the role the falsified MRF tried to play and
couldn't**:
*   **The MRF's falsification is MITIGATED at the CATEGORY level.**
    The **MRF's OWN representation** remains falsified (the MRF is
    represented as paired — anomalous), **but the CATEGORY's
    principle** — **diffuse bilateral regions are represented as
    single leaves** — is **validated by the PAG's clean
    representation**. **The category's on-disk evidence is NOT
    lost** — **it was always the PAG, not the MRF.**
*   **The PAG is the SECOND diffuse bilateral region** — and it is
    the **only clean one** in the tree. **The MRF is the first
    diffuse bilateral region** — and it is the **anomalous one**.
    **Both are diffuse bilateral regions** — **one anomalous (MRF),
    one clean (PAG)**.
*   **The tegmentum container amendment's diffuse bilateral
    category** — which the MRF `left/` and `right/` modules said
    *"has NO ON-DISK EVIDENCE remaining"* — **now has ON-DISK
    EVIDENCE: the PAG**. **The amendment's argument for the
    diffuse bilateral category is NOT purely anatomical** — **it
    has a concrete, existing, on-disk example: the PAG**. **The
    PAG is the proof case the MRF could not be.**
**Boundary status (THE PAG SETTLES THE TWO CONTAINER
CONTRADICTIONS — the midbrain container's "midline" claim and the
tegmentum container's "treated as paired" claim are BOTH
CONTRADICTED by the on-disk tree):** **Boundary case — the
periaqueductal gray is a diffuse bilateral region, and this
SETTLES two container-level contradictions that have been open
since the `midbrain/` and `tegmentum/` containers were written.**
*   **The `midbrain/` container said:** *"the cerebral aqueduct
    and the **periaqueductal gray** are **midline structures, not
    paired**."* **This is HALF-RIGHT and HALF-WRONG.**
    *   **HALF-RIGHT** — the PAG is **not paired** (the on-disk
        path is a single leaf, no `left/`/`right/` nodes). ✓
    *   **HALF-WRONG** — the PAG is **not a midline structure** in
        the sense of a **discrete midline nucleus**. It
        **surrounds the aqueduct** and **extends laterally** into
        the adjacent tegmentum. It is a **diffuse bilateral
        column**, not a **discrete midline nucleus**. ✗
    *   **The correction:** *"the **periaqueductal gray** is a
        **diffuse bilateral modulatory column** — **surrounding
        the cerebral aqueduct** and **extending laterally** into
        the adjacent tegmentum — **not a discrete midline
        nucleus**. It is correctly represented as a **single
        leaf** under `tegmentum/` (not paired, not midline)."*
*   **The `tegmentum/` container said:** *"the PAG is
    **midline-adjacent** but is **treated as paired in the
    tree**."* **This is FULLY WRONG.**
    *   **FULLY WRONG** — the PAG is **not paired** in the tree.
        The on-disk path ``tegmentum/periaqueductal_gray/`` is a
        **single leaf** — **no `left/`/`right/` nodes**. The
        "treated as paired in the tree" claim is **FALSE**.
    *   **The correction:** *"the PAG is a **diffuse bilateral
        region** — represented as a **single leaf** under
        `tegmentum/` — **not paired**. The tegmentum container's
        paired-leaf rule was **too rigid**; the PAG is the
        **second exception** (diffuse bilateral, after the MRF),
        and it is **correctly represented as a single leaf**."*
*   **Both corrections are now fully actionable** — the PAG module
    provides the on-disk evidence. **Both containers should be
    amended** — the `midbrain/` container's "midline structure"
    framing and the `tegmentum/` container's "treated as paired
    in the tree" framing. **The PAG is the source of the
    correction** — the actual on-disk representation, available
    for verification.
**Boundary status (NOT the cerebral aqueduct — the aqueduct is the
MIDLINE CSF CONDUIT that the PAG SURROUNDS):** **Boundary case —
the periaqueductal gray is NOT the cerebral aqueduct.** The
**cerebral aqueduct** (``.../midbrain/cerebral_aqueduct/``) is the
**midline CSF conduit** — a **fluid-filled space** connecting the
**third ventricle** (diencephalon) to the **fourth ventricle**
(hindbrain). **The PAG surrounds the aqueduct** — it is the
**gray-matter column** immediately **around** the aqueduct. **They
are DIFFERENT STRUCTURES** — the **aqueduct** is a **CSF space**;
the **PAG** is a **gray-matter column**. Consumers must **not**
conflate the PAG with the cerebral aqueduct.
**Boundary status (NOT the tectum — the tectum is DORSAL to the
aqueduct and the PAG):** **Boundary case — the periaqueductal gray
is NOT the tectum.** The **tectum** (``.../midbrain/tectum/``) is
the **dorsal midbrain** — the **colliculi** — **dorsal** to the
cerebral aqueduct. **The PAG is around the aqueduct** — it is the
**gray-matter column** surrounding the aqueduct — **ventral to the
tectum** and **dorsal to the tegmentum proper**. **They are
DIFFERENT COMPARTMENTS of the midbrain** — the **tectum** is
**dorsal**; the **PAG** is **around the aqueduct**; the **tegmentum
proper** is **ventral**. Consumers must **not** conflate the PAG
with the tectum.
**Boundary status (NOT the midbrain reticular formation — the MRF
is VENTRAL to the PAG):** **Boundary case — the periaqueductal
gray is NOT the midbrain reticular formation (MRF).** The **MRF**
(``.../tegmentum/midbrain_reticular_formation/``) is the **diffuse
reticular region** of the **ventral tegmentum** — **ventral** to
the PAG. **The PAG is the diffuse modulatory column around the
aqueduct** — **dorsal** to the MRF. **They are DIFFERENT diffuse
bilateral regions in DIFFERENT positions** — the **MRF** is
**reticular** (arousal, locomotion); the **PAG** is **modulatory**
(pain, defensive behavior, autonomic control). **Both are diffuse
bilateral** — **the same laterality class** — **but different
structures**. Consumers must **not** conflate the PAG with the
MRF.
**Boundary status (NOT the CLi, the DR, or the IPN — those are
MIDLINE NUCLEI):** **Boundary case — the periaqueductal gray is
NOT the caudal linear nucleus, the dorsal raphe nucleus, or the
interpeduncular nucleus.** The **CLi**
(``.../tegmentum/caudal_linear_nucleus/``), the **DR**
(``.../tegmentum/dorsal_raphe_nucleus/``), and the **IPN**
(``.../tegmentum/interpeduncular_nucleus/``) are **midline
nuclei** — **discrete nuclei on the midline** (though the tree
represents them as paired — anomalous). **The PAG is a diffuse
bilateral region** — **not a midline nucleus** — it **surrounds
the aqueduct** and **extends laterally**. **They are DIFFERENT
STRUCTURES of DIFFERENT laterality classes** — the **CLi**, the
**DR**, and the **IPN** are **midline nuclei**; the **PAG** is a
**diffuse bilateral region**. Consumers must **not** conflate the
PAG with the CLi, the DR, or the IPN.
**Boundary status (NOT the raphe magnus or the RVM — those are
MEDULLARY, DOWNSTREAM of the PAG):** **Boundary case — the
periaqueductal gray is NOT the raphe magnus or the rostral
ventromedial medulla (RVM).** The **raphe magnus** and the **RVM**
(``.../hindbrain/myencephalon/medulla_oblongata/``) are
**medullary** structures — **caudal** to the midbrain — the
**downstream targets** of the **PAG's** descending projections.
**The PAG projects TO the RVM** (and the raphe magnus) — the
**PAG → RVM → spinal cord** circuit is the **descending pain-
modulation** pathway. **The RVM is DOWNSTREAM of the PAG.** **They
are DIFFERENT STRUCTURES at DIFFERENT levels** — the **PAG** is
**midbrain**; the **RVM** is **medulla**. Consumers must **not**
conflate the PAG with the raphe magnus or the RVM.
**Boundary status (NOT the amygdala — the amygdala is the
TELENCEPHALIC limbic structure):** **Boundary case — the
periaqueductal gray is NOT the amygdala.** The **amygdala**
(``.../forebrain/telencephalon/subcortical/medial_temporal_lobe/
amygdala/``) is the **telencephalic** limbic structure — the
**fear/emotion/salience** structure. **The PAG is a midbrain
structure** — the **defensive-behavior** and **pain-modulation**
region. **The amygdala PROJECTS TO the PAG** (via the **central
nucleus** and the **bed nucleus of the stria terminalis**) — the
**amygdala → PAG** circuit is part of the **fear/defensive-
behavior** system. **The PAG is DOWNSTREAM of the amygdala** in
the **fear-conditioning** circuit (the **amygdala → PAG → defensive
behavior** pathway). **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **amygdala** is **telencephalic**; the **PAG** is
**mesencephalic**. Consumers must **not** conflate the PAG with the
amygdala.
**Boundary status (NOT the hypothalamus — the hypothalamus is the
DIENCEPHALIC structure):** **Boundary case — the periaqueductal
gray is NOT the hypothalamus.** The **hypothalamus**
(``.../forebrain/diencephalon/hypothalamus/``) is the
**diencephalic** structure — the **autonomic, endocrine, and
homeostatic** control center. **The PAG is a midbrain structure** —
the **defensive-behavior, pain-modulation, and autonomic-modulation**
region. **The hypothalamus PROJECTS TO the PAG** (via the
**medial forebrain bundle** and the **dorsal longitudinal
fasciculus**) — the **hypothalamus → PAG** circuit is part of the
**defensive-behavior** and **autonomic-control** systems. **They
are DIFFERENT STRUCTURES across a lobe boundary** — the
**hypothalamus** is **diencephalic**; the **PAG** is
**mesencephalic**. Consumers must **not** conflate the PAG with the
hypothalamus.
**Boundary status (NOT the red nucleus, the substantia nigra, or the
VTA — those are DISCRETE NUCLEI of the tegmentum):** **Boundary
case — the periaqueductal gray is NOT the red nucleus, the
substantia nigra, or the ventral tegmental area.** The **red
nucleus** (``.../tegmentum/left/red_nucleus/`` and the right
counterpart), the **substantia nigra**
(``.../tegmentum/left/substantia_nigra/`` and the right
counterpart), and the **VTA**
(``.../tegmentum/left/ventral_tegmental_area/`` and the right
counterpart) are **discrete nuclei** — **paired**, **sharply
bounded**, with **specific transmitters** and **specific
projections**. **The PAG is a diffuse region** — **not a discrete
nucleus** — with **heterogeneous transmitters** and **heterogeneous
projections**. **They are DIFFERENT STRUCTURES of DIFFERENT
classes** — the **red nucleus**, the **SN**, and the **VTA** are
**discrete nuclei**; the **PAG** is a **diffuse bilateral
region**. Consumers must **not** conflate the PAG with the red
nucleus, the SN, or the VTA.
**Boundary status (NOT the pontine reticular formation — the
pontine reticular formation is the CAUDAL reticular region):**
**Boundary case — the periaqueductal gray is NOT the pontine
reticular formation.** The **pontine reticular formation**
(``.../hindbrain/metencephalon/pons/.../pontine_reticular_formation/``)
is a **rhombencephalic** reticular region — **caudal** to the
midbrain. **The PAG is a mesencephalic structure** — it **ends at
the pontomesencephalic junction**. **They are DIFFERENT STRUCTURES
at DIFFERENT levels** — the **PAG** is **midbrain**; the
**pontine reticular formation** is **pons**. The **PAG** is the
**modulatory column** around the aqueduct; the **pontine reticular
formation** is the **reticular network** of the pons. Consumers
must **not** conflate the PAG with the pontine reticular formation.
**Boundary status (NOT the cerebral peduncle — the peduncle is the
VENTRAL surface):** **Boundary case — the periaqueductal gray is
NOT the cerebral peduncle.** The **cerebral peduncle**
(``.../midbrain/cerebral_peduncle/``) is the **ventral-most
descending fiber bundle** — the **crus cerebri** — **white matter**
— **ventral** to the substantia nigra and the tegmentum. **The PAG
is around the aqueduct** — **dorsal** to the tegmentum. **They are
DIFFERENT STRUCTURES in DIFFERENT positions** — the **peduncle** is
a **conduction pathway** (ventral); the **PAG** is a **diffuse
bilateral modulatory column** (around the aqueduct). Consumers must
**not** conflate the PAG with the cerebral peduncle.
**Boundary status (DIFFUSE BILATERAL MODULATORY COLUMN — a new
subclass of the diffuse bilateral region class — NOT a discrete
nucleus, NOT a reticular network):** **Boundary case — the
periaqueductal gray is a DIFFUSE BILATERAL MODULATORY COLUMN.** In
the family's **structure-class taxonomy**, it is a **diffuse
bilateral region** — **the same broader class** as the **midbrain
reticular formation** — **but functionally distinct**:
*   **The MRF is a diffuse reticular region** — a **continuous
    reticular network** — its function is **arousal** (the ARAS),
    **locomotion** (the MLR), **sensorimotor integration**, and
    **pain modulation** (via projections to the PAG and the RVM).
*   **The PAG is a diffuse modulatory column** — a **continuous
    gray-matter column** around the aqueduct — its function is
    **pain modulation** (the **PAG → RVM → spinal cord** descending
    pain-inhibition pathway), **defensive behavior** (fight-or-
    flight, freezing), **autonomic control** (cardiovascular,
    respiratory), **vocalization**, **reproductive behavior**, and
    **nausea and vomiting**.
**Both are diffuse bilateral regions** — **the same laterality
class** — **but functionally distinct**. **The PAG is a "diffuse
bilateral modulatory column"** — a **subclass** of the **diffuse
bilateral region** class — **distinct from the MRF's "diffuse
reticular region"**. **It is NOT a discrete nucleus, NOT a sensory
relay, NOT a modulatory nucleus in the DR/VTA sense (the PAG is a
diffuse column, not a discrete nucleus), NOT a conduction pathway,
NOT an oscillator, NOT a premotor pool, NOT a motor nucleus.** It
is a **diffuse bilateral modulatory column** — **the same broader
category as the MRF** (diffuse bilateral), **but for pain,
defensive behavior, and autonomic control rather than arousal and
locomotion**. **Diffuse bilateral regions carry NO coupling
warning** — same rule as every non-oscillator class. **The diffuse
bilateral position** — **not paired, not midline** — is the
**structural expression** of its **diffuse modulatory function**:
it **surrounds the aqueduct** as a **continuous column** because
it **integrates** inputs from **both sides** and **projects** to
**bilateral targets** (the RVM, the autonomic centers, the spinal
cord). **The PAG is the SECOND diffuse bilateral region in the
family** — and the **first genuinely clean one**. See *The Second
Diffuse Bilateral Region* and *Lateralization Notes*.
**Boundary status (NO COUPLING WARNING — the PAG is a DIFFUSE
BILATERAL MODULATORY COLUMN):** **Boundary case — the
periaqueductal gray carries NO coupling warning.** The **coupling
warning** attaches to **OSCILLATORS** (the pre-Bötzinger complex,
the Bötzinger complex, the pFRG) — and the **PAG is not an
oscillator**. **It is a diffuse bilateral modulatory column** — a
**single leaf**, **not paired**, **not midline**. **Diffuse
bilateral regions carry NO coupling warning** — same rule as every
non-oscillator class. The **diffuse bilateral position** is **not
a coupling hazard** — it is the **structural fact** of a **diffuse
column** that **integrates** inputs from **both sides** and
**projects** to **bilateral targets**. There are **no "two sides"
to couple** — the PAG is **one continuous column**.

Overview
--------
The periaqueductal gray (PAG) is a **diffuse bilateral modulatory
column** of **gray matter** surrounding the **cerebral aqueduct** —
in the **midbrain tegmentum**, extending from the **diencephalon-
midbrain junction** (rostral) to the **pontomesencephalic junction**
(caudal). It is a **continuous column** of **heterogeneous neurons**
— **glutamatergic**, **GABAergic**, **dopaminergic**,
**serotonergic**, **cholinergic**, **opioid-containing**,
**peptidergic** — organized into **distinct longitudinal columns**
(dorsal, lateral, ventrolateral, dorsomedial) with **different
functions**. It is the **principal midbrain center** for
**descending pain modulation** (the **PAG → RVM → spinal cord**
pathway), **defensive behavior** (fight-or-flight, freezing),
**autonomic control** (cardiovascular, respiratory), **vocalization**,
**reproductive behavior**, and **nausea and vomiting**.

**The PAG is a DIFFUSE BILATERAL REGION — the SECOND in the family,
after the MRF.** It is **neither paired** (like the SN, the VTA,
the red nucleus) **nor midline** (like the CLi, the DR, the IPN).
It **surrounds the aqueduct** and **extends laterally** into the
adjacent tegmentum — a **single leaf**, but for a **different
reason** than the midline nuclei. **The tree represents it
cleanly** — a **single leaf** under ``tegmentum/``, **no `left/`
or `right/` nodes** — and this is the **anatomically correct
representation**.

**The PAG is the ACTUAL CLEAN CASE for the diffuse bilateral
category** — **not the claimed-then-falsified clean case the MRF
provided, but the genuinely clean case the tree has had all
along.** The MRF claimed to be the clean case and was **falsified**
by its own `left/` and `right/` nodes (the MRF `left/` and
`right/` modules explicitly say *"the diffuse bilateral category
has NO ON-DISK EVIDENCE remaining"*). **The PAG is the ON-DISK
EVIDENCE the MRF could not be** — the tree represents the PAG as a
single leaf, and it always has. **The PAG is the NEW proof case**
for the diffuse bilateral category — **taking over the role the
falsified MRF tried to play and couldn't**. See *The Second
Diffuse Bilateral Region* and *The PAG Settles the Two Container
Contradictions*.

**The PAG SETTLES two container-level contradictions.** The
`midbrain/` container said *"the periaqueductal gray is a midline
structure, not paired"* — **half-right** (not paired) and
**half-wrong** (not a midline structure in the discrete-nucleus
sense). The `tegmentum/` container said *"the PAG is
midline-adjacent but is treated as paired in the tree"* — **fully
wrong** (the on-disk path is a single leaf). **Both containers
should be amended** — the PAG module provides the on-disk evidence
for the corrections. See *The PAG Settles the Two Container
Contradictions*.

**The PAG carries NO coupling warning.** It is a **diffuse
bilateral modulatory column** — a **single leaf**, **not paired**,
**not midline**. **Diffuse bilateral regions carry NO coupling
warning** — same rule as every non-oscillator class.

**The PAG is NOT a CN nucleus.** It is a **diffuse bilateral
modulatory column** — it is **not** cross-listed with
``cranial_nerve_nuclei/``. It has **one path only**.

The Second Diffuse Bilateral Region
-----------------------------------
**The PAG is the second diffuse bilateral region in the family** —
after the **midbrain reticular formation**. Both are **single
leaves** that **span both sides** as **continuous regions** —
**neither paired, neither midline**. **They are functionally
distinct**:

*   **MRF** (``.../tegmentum/midbrain_reticular_formation/``) — a
    **diffuse reticular region** — **ventral tegmentum** —
    **arousal** (ARAS), **locomotion** (MLR), **sensorimotor
    integration**, **pain modulation** (via the PAG and the RVM).

*   **PAG** (this module) — a **diffuse modulatory column** —
    **around the aqueduct** — **pain modulation** (the **PAG →
    RVM → spinal cord** descending pain-inhibition pathway),
    **defensive behavior** (fight-or-flight, freezing), **autonomic
    control** (cardiovascular, respiratory), **vocalization**,
    **reproductive behavior**, **nausea and vomiting**.

**Both are diffuse bilateral regions** — **the same laterality
class** — **but different structures** — **different positions**
(ventral tegmentum vs. around the aqueduct), **different
functions** (reticular/arousal/locomotion vs. modulatory/pain/
defensive behavior), **different structure subclasses** (diffuse
reticular region vs. diffuse modulatory column).

**The PAG is the ACTUAL clean case for the diffuse bilateral
category** — **the MRF was the claimed-then-falsified clean case**.
The MRF `left/` and `right/` modules **explicitly say** *"the
diffuse bilateral category has NO ON-DISK EVIDENCE remaining"* —
**this is now CORRECTED**: **the diffuse bilateral category DOES
have on-disk evidence — the PAG**. **The PAG was always there,
on-disk, single-leaf** — **the MRF's falsification did not remove
the category's on-disk evidence — it removed the MRF's clean-case
claim**. **The category's on-disk evidence is the PAG.**

**The PAG is the NEW proof case** for the diffuse bilateral
category — **taking over from the falsified MRF**. **The MRF's
falsification is mitigated at the CATEGORY level** — the
**category's principle** (diffuse bilateral regions are represented
as single leaves) is **validated by the PAG's clean
representation** — even though **the MRF's own representation**
remains falsified.

The PAG Settles the Two Container Contradictions
------------------------------------------------
**The PAG settles two container-level contradictions** that have
been open since the `midbrain/` and `tegmentum/` containers were
written:

**Contradiction 1 — the `midbrain/` container's "midline
structure" claim.**

*   **What the `midbrain/` container said:** *"the cerebral
    aqueduct and the **periaqueductal gray** are **midline
    structures, not paired**."*
*   **What is RIGHT:** the PAG is **not paired** (the on-disk
    path is a single leaf, no `left/`/`right/` nodes). ✓
*   **What is WRONG:** the PAG is **not a midline structure** in
    the sense of a **discrete midline nucleus**. It **surrounds
    the aqueduct** and **extends laterally** into the adjacent
    tegmentum. It is a **diffuse bilateral column**, not a
    **discrete midline nucleus**. ✗
*   **The correction:** *"the **periaqueductal gray** is a
    **diffuse bilateral modulatory column** — **surrounding the
    cerebral aqueduct** and **extending laterally** — **not a
    discrete midline nucleus**. It is correctly represented as
    a **single leaf** under `tegmentum/` (not paired, not
    midline)."*

**Contradiction 2 — the `tegmentum/` container's "treated as
paired in the tree" claim.**

*   **What the `tegmentum/` container said:** *"the PAG is
    **midline-adjacent** but is **treated as paired in the
    tree**."*
*   **What is WRONG:** the PAG is **not paired** in the tree. The
    on-disk path ``tegmentum/periaqueductal_gray/`` is a **single
    leaf** — **no `left/`/`right/` nodes**. The "treated as
    paired in the tree" claim is **FALSE**. ✗
*   **The correction:** *"the PAG is a **diffuse bilateral
    region** — represented as a **single leaf** under
    `tegmentum/` — **not paired**. The tegmentum container's
    paired-leaf rule was **too rigid**; the PAG is the **second
    exception** (diffuse bilateral, after the MRF), and it is
    **correctly represented as a single leaf**."*

**Both corrections are now fully actionable** — the PAG module
provides the on-disk evidence. **Both containers should be
amended** — the `midbrain/` container's "midline structure"
framing and the `tegmentum/` container's "treated as paired in
the tree" framing. **The PAG is the source of the correction** —
the actual on-disk representation, available for verification.

**The tegmentum container amendment — previously resting on the
MRF's clean case, which was falsified — now has a CONCRETE,
EXISTING, ON-DISK EXAMPLE for the diffuse bilateral category: the
PAG.** **The amendment's diffuse bilateral category is NOT purely
anatomical** — **it has a clean on-disk example**. **The PAG is
the proof case the MRF could not be.**

Subregions (prose, not structural children)
-------------------------------------------
The periaqueductal gray has **functional subregions** —
**longitudinal columns** around the aqueduct — documented as
**prose**, not as structural children:

*   **Dorsal PAG (dPAG)** — the **dorsal column** — **fear**,
    **anxiety**, **defensive behavior** (fight-or-flight,
    freezing), **cardiovascular** responses. **The dPAG is the
    "active" defensive-behavior column** — **escape**, **flight**,
    **hypertension**, **tachycardia**. **Subregion of the PAG** —
    **not a structural child**.

*   **Lateral PAG (lPAG)** — the **lateral column** — **autonomic
    control** (cardiovascular, respiratory), **defensive
    behavior**, **vocalization**. **The lPAG is the "passive"
    defensive-behavior column** — **freezing**, **hypotension**,
    **bradycardia**, **analgesia**. **Subregion of the PAG** —
    **not a structural child**.

*   **Ventrolateral PAG (vlPAG)** — the **ventrolateral column**
    — **the PRINCIPAL pain-modulation column** — the **PAG → RVM
    → spinal cord** descending pain-inhibition pathway —
    **analgesia** (via **opioid** and **non-opioid** mechanisms).
    **The vlPAG is also involved in reproductive behavior**
    (lordosis in females). **Subregion of the PAG** — **not a
    structural child**.

*   **Dorsomedial PAG (dmPAG)** — the **dorsomedial column** —
    **pain modulation**, **defensive behavior**, **autonomic
    control**. **The dmPAG is involved in the "passive"
    defensive-behavior** and **analgesia**. **Subregion of the
    PAG** — **not a structural child**.

**These subregions are prose, not structural children.** They are
**longitudinal columns** of a **continuous region** — **not
discrete nuclei**. **A diffuse region cannot be resolved into
discrete children** — its subregions are **prose**. The tree wires
the **periaqueductal gray** as a **single leaf** under the
tegmentum container (diffuse bilateral). Consumers must **not**
resolve ``.../periaqueductal_gray/dorsal_pag`` or
``.../periaqueductal_gray/ventrolateral_pag`` — no such paths
exist.

The Descending Pain-Modulation Pathway (the PAG's Primary Function)
-------------------------------------------------------------------
The **descending pain-modulation pathway** is the **PAG's primary
function** — one of the **best-defined** circuits in the brain.
The circuit is:

*   **The PAG (ventrolateral PAG)** — the **principal pain-
    modulation column** — receives **input** from the **ascending
    somatosensory** system, the **amygdala**, the **prefrontal
    cortex**, the **anterior cingulate cortex**, the **insula**,
    and the **hypothalamus**. It **projects** to the **rostral
    ventromedial medulla (RVM)**.

*   **The RVM (rostral ventromedial medulla)** — the **medullary
    pain-modulation relay** — contains the **serotonergic raphe
    magnus** and the **non-serotonergic RVM neurons** — the
    **"ON" cells** (which **facilitate** pain) and the **"OFF"
    cells** (which **inhibit** pain). The **RVM** projects to the
    **dorsal horn of the spinal cord** (the **dorsolateral
    funiculus**).

*   **The spinal cord (dorsal horn)** — the **RVM projections**
    **inhibit** the **nociceptive neurons** of the **dorsal horn**
    — **reducing** the **ascending pain signal**.

*   **The net effect** — **the PAG → RVM → spinal cord circuit
    produces ANALGESIA** — the **descending pain-inhibition**
    pathway. **The PAG is the "top" of the descending pain-
    modulation system.**

**The PAG's pain-modulation function is mediated by opioid and
non-opioid mechanisms** — the **PAG is rich in opioid receptors**
(mu, delta, kappa), and **opioid microinjection into the PAG**
produces **profound analgesia**. **The PAG is the site of action
of opioid analgesia** — the **endogenous opioid peptides**
(endorphins, enkephalins, dynorphins) act on the PAG to **activate
the descending pain-inhibition pathway**. **The PAG is also a site
of action of non-opioid analgesics** — the **cannabinoid** system,
the **serotonergic** system, and the **noradrenergic** system
**modulate** the PAG's pain-inhibition function.

The Defensive-Behavior Circuit (the PAG's Second Primary Function)
------------------------------------------------------------------
The **defensive-behavior circuit** is the **PAG's second primary
function** — the **fight-or-flight** and **freezing** responses.
The circuit is:

*   **The amygdala (central nucleus)** — the **fear-learning
    structure** — **projects** to the **PAG** (via the **bed
    nucleus of the stria terminalis** — the **BNST**) — the
    **amygdala → PAG** circuit is the **fear → defensive
    behavior** pathway.

*   **The PAG (dorsal PAG and lateral PAG)** — the **defensive-
    behavior columns** — receives **input** from the
    **amygdala**, the **medial prefrontal cortex**, the
    **hypothalamus**, and the **superior colliculus**. It
    **projects** to the **autonomic centers** (the **rostral
    ventrolateral medulla** — the **RVLM**), the **respiratory
    centers**, the **spinal cord** (the **defensive-behavior
    motor** pathways), and the **vocalization** centers.

*   **The dPAG** — the **"active" defensive-behavior column** —
    **fight-or-flight**, **escape**, **hypertension**,
    **tachycardia**.

*   **The lPAG** — the **"passive" defensive-behavior column** —
    **freezing**, **hypotension**, **bradycardia**, **analgesia**.

**The PAG is the key midbrain node** in the **defensive-behavior
circuit** — the **final common pathway** for the **fear → defensive
behavior** transformation. **The amygdala detects the threat; the
PAG executes the defensive response.** **The PAG's defensive-
behavior function is distinct from its pain-modulation function** —
the **defensive-behavior** is mediated by the **dorsal and lateral
PAG**; the **pain-modulation** is mediated by the **ventrolateral
PAG**.

The Autonomic-Control Function
------------------------------
The **PAG's autonomic-control function** is mediated by its
**projections to the autonomic centers** — the **rostral
ventrolateral medulla (RVLM)**, the **nucleus tractus solitarius
(NTS)**, the **nucleus ambiguus**, and the **hypothalamus**. **The
PAG modulates** — **cardiovascular function** (heart rate, blood
pressure), **respiratory function** (rate, depth), **thermoregulation**,
and **other autonomic functions**. **The PAG's autonomic-control
function is integrated with its defensive-behavior function** —
the **dPAG** produces the **sympathetic** response of **fight-or-
flight** (hypertension, tachycardia); the **lPAG** produces the
**parasympathetic** response of **freezing** (hypotension,
bradycardia, analgesia).

The Vocalization Function
-------------------------
The **PAG is the final common pathway for vocalization** — the
**PAG → reticular formation → laryngeal motor neurons** circuit
produces **vocalization**. **Electrical stimulation of the PAG
elicits vocalization** in animals; **PAG lesions produce mutism**
in humans. **The PAG integrates** the **emotional and motivational**
inputs (from the **amygdala**, the **hypothalamus**, the **anterior
cingulate cortex**) with the **motor** outputs (the **laryngeal
motor neurons** via the **reticular formation**) — **the PAG is the
emotional-vocalization interface**.

The Reproductive-Behavior Function
----------------------------------
The **PAG's ventrolateral column** is involved in **reproductive
behavior** — the **lordosis reflex** in females (the **PAG →
medullary reticular formation → spinal cord** circuit). **The PAG
integrates** the **hormonal** and **sensory** inputs (from the
**ventromedial hypothalamus** and the **somatosensory** system)
with the **motor** output (the **lordosis** posture). **The PAG's
reproductive-behavior function is mediated by the ventrolateral
PAG** — the **same column** as the **pain-modulation** function.

The Nausea and Vomiting Function
--------------------------------
The **PAG** is involved in **nausea and vomiting** — it **projects
to the brainstem vomiting centers** (the **nucleus tractus
solitarius**, the **area postrema**, the **parabrachial nucleus**).
**PAG stimulation can produce nausea and vomiting**; **PAG lesions
can produce nausea**. **The PAG's nausea and vomiting function is
mediated by its projections to the brainstem vomiting centers** —
the **PAG is one node** in the **nausea and vomiting** circuit.

Function in the Human Brain
---------------------------
The periaqueductal gray's functions are **descending pain
modulation**, **defensive behavior**, **autonomic control**,
**vocalization**, **reproductive behavior**, and **nausea and
vomiting** — **NOT** a sensory relay, **NOT** a motor nucleus,
**NOT** a premotor pool, **NOT** a conduction pathway:

*   **Descending Pain Modulation (the PAG's primary function):**
    The PAG — **especially the ventrolateral PAG** — **activates**
    the **descending pain-inhibition pathway** (the **PAG → RVM →
    spinal cord** circuit) — **reducing** the **ascending pain
    signal**. **The PAG is the "top" of the descending pain-
    modulation system** — **the site of action of opioid
    analgesia**. **The PAG's pain-modulation function is mediated
    by opioid and non-opioid mechanisms.**

*   **Defensive Behavior (the PAG's second primary function):** The
    PAG — **especially the dorsal PAG and the lateral PAG** —
    **integrates** the **amygdala's threat detection** with the
    **autonomic and motor** outputs — **producing** **fight-or-
    flight** (dPAG) or **freezing** (lPAG). **The PAG is the final
    common pathway for defensive behavior.**

*   **Autonomic Control:** The PAG **modulates** — **cardiovascular
    function** (heart rate, blood pressure), **respiratory
    function** (rate, depth), **thermoregulation**. **The PAG's
    autonomic-control function is integrated with its defensive-
    behavior function.**

*   **Vocalization:** The PAG is the **final common pathway for
    vocalization** — the **emotional-vocalization interface**.
    **PAG stimulation elicits vocalization**; **PAG lesions
    produce mutism**.

*   **Reproductive Behavior:** The PAG — **especially the
    ventrolateral PAG** — is involved in **reproductive behavior**
    (the **lordosis reflex** in females).

*   **Nausea and Vomiting:** The PAG **projects to the brainstem
    vomiting centers** — **contributing** to **nausea and
    vomiting**.

*   **NOT a sensory relay.** The PAG does **not** transduce or
    relay a specific sensory modality — it is a **modulatory
    column**, not a **sensory relay**.

*   **NOT a motor nucleus.** The PAG does **not** drive muscle
    directly — it **modulates** defensive behavior and
    **autonomic function** via its **projections**.

*   **NOT a premotor pool.** The PAG does **not** transform motor
    commands in the sense of the **PPRF** or the **riMLF** — it
    **initiates** defensive behavior and **descending pain
    modulation** at a **higher level**.

*   **NOT a conduction pathway.** The PAG is **grey matter** — a
    **diffuse modulatory column** — **not white matter**.

*   **NOT an oscillator.** The PAG is a **diffuse bilateral
    modulatory column** — it does **not** generate a rhythm.
    **Diffuse bilateral regions carry NO coupling warning** — same
    rule as every non-oscillator class.

**The unifying theme:** the PAG is a **diffuse bilateral modulatory
column** around the **cerebral aqueduct** — the **principal
midbrain center** for **descending pain modulation** (the **PAG →
RVM → spinal cord** pathway), **defensive behavior** (fight-or-
flight, freezing), **autonomic control** (cardiovascular,
respiratory), **vocalization**, **reproductive behavior**, and
**nausea and vomiting**. It is **not a discrete nucleus** — it is
a **continuous column** of **heterogeneous neurons** with
**heterogeneous transmitters** and **heterogeneous projections**.
It is the **second diffuse bilateral region** in the family —
**the same laterality class as the MRF** — **but functionally
distinct** (pain modulation and defensive behavior, not arousal
and locomotion). **The PAG is the ACTUAL clean case for the
diffuse bilateral category** — the **on-disk evidence the MRF
could not be**. It carries **NO coupling warning** — same rule as
every non-oscillator class.

Associated Disorders
--------------------
The periaqueductal gray has **no named syndrome of its own** — its
clinical associations are **direct** and **substantial**, via its
**descending pain-modulation**, **defensive-behavior**, and
**autonomic-control** functions — and it is a **contributor** to
several major clinical syndromes:

*   **Chronic Pain (DIRECT — the PAG's pain-modulation dysfunction
    is implicated):** The **PAG → RVM → spinal cord** descending
    pain-inhibition pathway is the **principal endogenous
    analgesia** system. **PAG dysfunction** — via **chronic
    stress**, **inflammation**, **nerve injury**, or
    **neurodegeneration** — **impairs the descending pain
    inhibition** — **contributing** to **chronic pain** (e.g.,
    **fibromyalgia**, **chronic neuropathic pain**, **chronic
    low back pain**). **The PAG is a key pain-modulation
    substrate** — **not the sole substrate** (the **RVM**, the
    **peripheral nociceptors**, and the **cortical pain
    networks** are also involved).

*   **Fear, Anxiety, and Panic Disorder (DIRECT — the PAG's
    defensive-behavior dysfunction is implicated):** The **PAG —
    amygdala** defensive-behavior circuit is **implicated** in
    **panic disorder**, **PTSD**, **generalized anxiety**, and
    **specific phobias**. **The dorsal PAG** is **implicated in
    panic** — **PAG stimulation produces panic-like responses**
    (hypertension, tachycardia, hyperventilation) in humans;
    **PAG lesions** can **reduce** panic responses. **The PAG is
    a contributor** to **fear and anxiety disorders** — the
    **amygdala**, the **BNST**, the **prefrontal cortex**, and
    the **insular cortex** are **also involved**.

*   **Defensive Behavior (DIRECT — the PAG's defensive-behavior
    function is the substrate):** **Freezing** and **fight-or-
    flight** behaviors are **mediated by the PAG** — the **dPAG**
    for **active** defensive behavior, the **lPAG** for
    **passive** defensive behavior. **PAG dysfunction** is
    **implicated in** the **behavioral inhibition** and
    **avoidance** of **anxiety disorders**.

*   **Vocalization (DIRECT — the PAG's vocalization function is
    the substrate):** **PAG lesions** produce **mutism** in
    humans — the **PAG is the final common pathway for
    vocalization**. **PAG stimulation** elicits **vocalization**
    — the **PAG is the emotional-vocalization interface**.
    **PAG dysfunction** is **implicated in** **mutism** and
    **vocalization disorders** — **rare** — **the PAG is a key
    substrate** for **emotional vocalization**.

*   **Autonomic Dysfunction (DIRECT — the PAG's autonomic-control
    function is the substrate):** **PAG dysfunction** — via
    **stroke**, **tumor**, or **neurodegeneration** — can produce
    **autonomic dysfunction** — **cardiovascular** and
    **respiratory** abnormalities. **The PAG is a contributor** —
    the **hypothalamus**, the **RVLM**, the **NTS**, and the
    **nucleus ambiguus** are **also involved**.

*   **Nausea and Vomiting (DIRECT — the PAG's nausea function is
    the substrate):** **PAG lesions** and **PAG stimulation** can
    produce **nausea and vomiting** — **the PAG projects to the
    brainstem vomiting centers**.

*   **Migraine (INDIRECT — the PAG is implicated, but the primary
    substrates are the trigeminovascular system and the
    brainstem pain-modulation system):** **Migraine** is
    **associated with** **dysfunction** of the **brainstem
    pain-modulation system** — the **PAG**, the **RVM**, the
    **peripheral trigeminal system**, the **thalamus**, and the
    **cortical pain networks** — **together**. **The PAG is a
    contributor** — **the PAG's descending pain-inhibition
    dysfunction** is **implicated in migraine**, **but the
    trigeminovascular system** (the **meningeal blood vessels**
    and the **trigeminal nerve**) is the **primary peripheral
    substrate**.

*   **No Named "Periaqueductal Gray Syndrome":** The PAG is a
    **diffuse bilateral modulatory column** — it has **no named
    syndrome of its own** — but its **clinical associations are
    direct and substantial**: it is a **contributor** to
    **chronic pain**, **fear/anxiety/panic**, **defensive
    behavior**, **vocalization disorders**, **autonomic
    dysfunction**, and **nausea and vomiting**. **The PAG is a
    key substrate** — but **not the sole substrate** — for each
    of these.

**What is NOT here:** The PAG is **not** the substrate for
**chronic pain as a PAG-exclusive syndrome** (the **PAG** is a
key descending pain-modulation substrate — the **RVM**, the
**peripheral nociceptors**, and the **cortical pain networks**
are also involved), **fear/anxiety/panic as PAG-exclusive
syndromes** (the **amygdala**, the **BNST**, the **prefrontal
cortex**, and the **insula** are also involved), **defensive
behavior as a PAG-exclusive function** (the **amygdala**
detects the threat; the **PAG** executes the response),
**vocalization disorders as PAG-exclusive** (the **PAG** is the
final common pathway — the **cortical** and **limbic** inputs are
also involved), **autonomic dysfunction as PAG-exclusive** (the
**hypothalamus**, the **RVLM**, the **NTS**, and the **nucleus
ambiguus** are also involved), **nausea and vomiting as
PAG-exclusive** (the **area postrema**, the **NTS**, and the
**parabrachial nucleus** are also involved), **saccade disorders**
(the **SC**, the **SNr**, the **riMLF** — **NOT** the PAG),
**pupillary light reflex deficits** (the **pretectum** and the
**EW nucleus** — **NOT** the PAG), **oculomotor palsy** (the
**CN III nucleus** — **NOT** the PAG), **trochlear palsy** (the
**CN IV nucleus** — **NOT** the PAG), **trigeminal sensory
deficits** (the **trigeminal ganglion**, the **main sensory**,
and the **spinal trigeminal nucleus** — **NOT** the PAG),
**CCHS** (RTN), **OIRD** (pre-Bötzinger complex — NK1R neurons),
**Rett syndrome** (pre-Bötzinger complex), **SIDS** (proposed —
pre-Bötzinger complex + arcuate nucleus), **essential
hypertension / sympathetic overactivity** (C1 group / RVLM),
**Huntington's disease** (striatum — telencephalon), or
**Kluver-Bucy syndrome** (amygdala). Its clinical relevance is
**direct and substantial** — it is a **contributor** to several
major disorders — but the disorders are **multifactorial**, and
the **PAG is one substrate among several**. **No named PAG
syndrome exists.**

Lateralization Notes
--------------------
This is the **periaqueductal gray** leaf — the **second diffuse
bilateral region** in the family, and the **first genuinely
cleanly-represented one**. The PAG is **diffuse bilateral** —
**not paired**, **not midline**. **It has no left/right pair**
(it is **one continuous column** surrounding the aqueduct) **and
no midline position** (it is **not a discrete nucleus on the
midline** — it **surrounds the aqueduct** and **extends
laterally**). **The tree represents it CLEANLY** — one leaf
under ``tegmentum/``, **no `left/` or `right/` nodes**. **No
coupling warning** — the same rule as every non-oscillator class.

*   **Diffuse Bilateral Region — NOT Paired, NOT Midline:** The
    PAG is a **single leaf** directly under ``tegmentum/`` —
    **NOT** under ``tegmentum/left/`` or ``tegmentum/right/``
    (not paired), **NOT** a **midline nucleus** (a single nucleus
    on the midline). It is a **continuous column** that
    **surrounds the aqueduct** and **extends laterally**. **It is
    the SECOND "diffuse bilateral region"** — after the **MRF**.

*   **Cleanly Represented in the Tree — the ACTUAL Clean Case:**
    The PAG is **cleanly represented** — the tree **already does**
    what the **tegmentum container amendment** should formalize:
    **a diffuse bilateral region is a single leaf** under
    ``tegmentum/``. **The PAG is the ACTUAL clean case for the
    diffuse bilateral category** — **not the claimed-then-
    falsified clean case the MRF provided, but the genuinely
    clean case the tree has had all along**. **The PAG is the NEW
    proof case** — **taking over the role the falsified MRF
    tried to play and couldn't**. **The diffuse bilateral
    category's on-disk evidence is NOT lost** — **it was always
    the PAG, not the MRF.**

*   **Diffuse Position = Diffuse Function:** The PAG
    **integrates** inputs from **both sides** (ascending
    somatosensory, cortical, limbic, hypothalamic) and
    **projects** to **bilateral targets** (the RVM, the autonomic
    centers, the spinal cord) — it **surrounds the aqueduct** as
    a **continuous column** because it **integrates** and
    **projects** across **both sides**. **It has no "left half"
    and "right half"** — it is **one continuous column**.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to DIFFUSE BILATERAL REGIONS):** The
    **pre-Bötzinger complex** carries a **coupling warning**
    because it is an **oscillator** whose two sides must
    synchronize to produce a single rhythm. The **PAG** is a
    **diffuse bilateral region** — a **single leaf** — it does
    **not** generate a rhythm, so it does **not** carry the
    **oscillator coupling warning**. There are **no "two sides"
    to couple** — the PAG is **one continuous column** whose
    **diffuse projections** carry its functions to **both
    sides**. **Diffuse bilateral regions carry NO coupling
    warning** — same rule as every non-oscillator class.

*   **No SLEA Warning:** The PAG is **SLEA-free** — it is **not**
    an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The PAG is **not**
    part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The PAG is **not** a
    rhinencephalon structure.

**The PAG is the SECOND diffuse bilateral region in the family**
— its **diffuse bilateral position**, **diffuse modulatory
column class**, **clean representation in the tree**, and **no
coupling warning** establish the **second canonical structural
pattern** for diffuse bilateral regions. **The MRF** was the
**first** — and it was **falsified**. **The PAG** was the
**second** — and it is **actually clean**. **The two diffuse
bilateral regions together** — **one anomalous (MRF), one clean
(PAG)** — **define the diffuse bilateral category**: **a
continuous region spanning both sides, represented as a single
leaf**. **The PAG validates the category** — **the MRF's
falsification did not invalidate the category**, because the
category's **on-disk evidence is the PAG**, not the MRF.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The PAG is **diffuse
    bilateral** — there is **no** other side to import from (it
    is **one continuous column**).
*   **No cross-lobe imports.** This module does **not** import
    from the **cerebral aqueduct**, the **tectum**, the
    **pretectum**, the **cerebral peduncle**, the **MRF**, the
    **CLi**, the **DR**, the **IPN**, the **CN nuclei**, the
    **raphe magnus**, the **RVM**, the **amygdala**, the
    **hypothalamus**, the **red nucleus**, the **substantia
    nigra**, the **VTA**, the **pontine reticular formation**,
    or any other container. The PAG's relationships to the
    cerebral aqueduct, the tectum, the pretectum, the cerebral
    peduncle, the MRF, the CLi, the DR, the IPN, the CN nuclei,
    the raphe magnus, the RVM, the amygdala, the hypothalamus,
    the red nucleus, the substantia nigra, the VTA, and the
    pontine reticular formation are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **GABAergic**, **glutamatergic**, **opioid**,
    **dopaminergic**, **serotonergic**, and **cholinergic**
    phenotypes of the PAG neurons are
    **``chemicals_hormones``-layer facts** — documented as
    **prose**, **never imported**. **CHEMICALS-LAYER DISCIPLINE**
    is preserved.
*   **DIFFUSE BILATERAL REGION — the SECOND in the family.** The
    PAG is a **single leaf** directly under ``tegmentum/`` —
    **NOT** under ``tegmentum/left/`` or ``tegmentum/right/``
    (not paired), **NOT** a **midline nucleus** (a single nucleus
    on the midline). It is a **continuous column** that
    **surrounds the aqueduct** and **extends laterally**. **This
    is the SECOND "diffuse bilateral region"** — after the
    **MRF**.
*   **ACTUAL CLEAN CASE — the PAG is genuinely cleanly
    represented.** The tree represents the PAG **cleanly** — a
    **single leaf** under ``tegmentum/``, **no `left/` or
    `right/` nodes** — and this is the **anatomically correct
    representation**. **The PAG is the ACTUAL clean case for the
    diffuse bilateral category** — **not the claimed-then-
    falsified clean case the MRF provided, but the genuinely
    clean case the tree has had all along**. **The PAG is the
    NEW proof case** — **taking over the role the falsified
    MRF tried to play and couldn't**. **The diffuse bilateral
    category's on-disk evidence is NOT lost** — **it was always
    the PAG, not the MRF**.
*   **SETTLES TWO CONTAINER CONTRADICTIONS.**
    *   **The `midbrain/` container said:** *"the PAG is a midline
        structure, not paired."* **Half-right** (not paired),
        **half-wrong** (not a discrete midline nucleus — it is a
        diffuse bilateral column). **The correction:** the PAG
        is a **diffuse bilateral modulatory column** — **not a
        discrete midline nucleus** — correctly represented as a
        **single leaf**.
    *   **The `tegmentum/` container said:** *"the PAG is
        midline-adjacent but is treated as paired in the tree."*
        **Fully wrong** (the on-disk path is a single leaf).
        **The correction:** the PAG is a **diffuse bilateral
        region** — **represented as a single leaf** under
        ``tegmentum/`` — **not paired**.
    *   **Both containers should be amended** — the PAG module
        provides the on-disk evidence.
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER — TWO exception
    categories, now with an ACTUAL clean case for the second
    one.** The tegmentum container's **paired-leaf rule** should
    be **AMENDED** to permit **BOTH**:
    *   **Midline nuclei** — the **CLi**, the **DR**, the
        **IPN** — **single leaves** because they are **discrete
        nuclei on the midline** (**no clean on-disk case** —
        all three are represented as paired, anomalous — the
        joint Resolution B is needed).
    *   **Diffuse bilateral regions** — the **MRF**, the **PAG**
        — **single leaves** because they are **continuous
        regions spanning both sides** (**ONE clean on-disk case:
        the PAG** — the MRF is anomalous; **the PAG is the
        actual proof case**).
    **The amendment's diffuse bilateral category now has CONCRETE
    ON-DISK EVIDENCE: the PAG.** **The amendment's midline
    category still has no clean on-disk case** — the joint
    Resolution B for the CLi, DR, and IPN is needed.
*   **LIVE AMENDMENT TO THE MIDBRAIN CONTAINER — correct the PAG
    prose.** The midbrain container said *"the cerebral aqueduct
    and the periaqueductal gray are midline structures, not
    paired."* **Half-right** (not paired), **half-wrong** (not
    midline). **The correction:** the PAG is a **diffuse
    bilateral modulatory column** — **surrounding the cerebral
    aqueduct** — **not a discrete midline nucleus**. **The
    midbrain container should be amended.**
*   **DIFFUSE BILATERAL MODULATORY COLUMN — a NEW subclass of the
    diffuse bilateral region class.** The PAG is a **diffuse
    bilateral modulatory column** — **distinct from** the MRF's
    **diffuse reticular region** (arousal, locomotion) — **but
    the SAME laterality class** (diffuse bilateral). **The PAG
    is a diffuse modulatory column** — pain modulation,
    defensive behavior, autonomic control, vocalization,
    reproductive behavior, nausea.
*   **SUBNUCLEAR / SUBREGION DISCIPLINE — subregions are PROSE,
    not structural children.** The **dorsal PAG**, **lateral
    PAG**, **ventrolateral PAG**, and **dorsomedial PAG** are
    **longitudinal columns** of a **continuous region** — **not
    discrete nuclei**, **not structural children**. **A diffuse
    region cannot be resolved into discrete children** — its
    subregions are **prose**.
*   **NO COUPLING WARNING — diffuse bilateral regions carry NO
    coupling warning.** The PAG is a **single leaf** — a
    **diffuse bilateral modulatory column** — it does **not**
    generate a rhythm. **The diffuse bilateral position is not a
    coupling hazard** — it is the structural fact of a **diffuse
    column** that **integrates** inputs and **projects** to
    **bilateral targets**.
*   **NOT A CN NUCLEUS.** The PAG is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. It has **one path only**.
*   **NOT a discrete nucleus — a DIFFUSE MODULATORY COLUMN.**
    The PAG is **not** a **discrete nucleus** with a **single
    transmitter** and a **single function** — it is a **diffuse
    column** with **heterogeneous** transmitters and
    **heterogeneous** functions.
*   **NOT the cerebral aqueduct — the aqueduct is the MIDLINE CSF
    CONDUIT that the PAG SURROUNDS.**
*   **NOT the tectum — the tectum is DORSAL to the aqueduct.**
*   **NOT the MRF — the MRF is VENTRAL to the PAG.** Different
    diffuse bilateral region.
*   **NOT the CLi, the DR, or the IPN — those are MIDLINE
    nuclei.**
*   **NOT the raphe magnus or the RVM — those are MEDULLARY,
    DOWNSTREAM of the PAG.**
*   **NOT the amygdala — the amygdala is TELENCEPHALIC.**
*   **NOT the hypothalamus — the hypothalamus is DIENCEPHALIC.**
*   **NOT the red nucleus, the SN, or the VTA — those are DISCRETE
    NUCLEI.**
*   **NOT the pontine reticular formation — that is a PONTINE
    reticular region.**
*   **NOT the cerebral peduncle — that is the VENTRAL surface
    (a conduction pathway).**
*   **CHEMICALS-LAYER DISCIPLINE.** The **GABAergic**,
    **glutamatergic**, **opioid**, **dopaminergic**,
    **serotonergic**, and **cholinergic** phenotypes of the PAG
    neurons are **``chemicals_hormones``-layer facts** —
    documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The PAG is a
    **local diffuse bilateral leaf** under the tegmentum — no
    cross-listing.
*   **No nested cross-listing.** The PAG is a **single leaf**. It
    is **not** a container.
*   **The on-disk tree is authoritative.** The on-disk tree has
    ``.../tegmentum/periaqueductal_gray/`` — **one leaf**,
    **diffuse bilateral**, **no `left/` or `right/`**. **This is
    the correct representation** — the PAG is a **diffuse
    bilateral region**, and the tree represents it cleanly.
    **The PAG is the actual proof case for the diffuse bilateral
    category.**

Usage
-----
Resolve the leaf by path (**one** path only — the PAG is **diffuse
bilateral**, **not** under `left/` or `right/`)::

    from infrastructure.brainparts.midbrain.tegmentum import periaqueductal_gray

Or by fully-qualified path string::

    path = "midbrain.tegmentum.periaqueductal_gray"

**Do not** assume the PAG is under
``tegmentum/periaqueductal_gray/left/`` or
``tegmentum/periaqueductal_gray/right/``. **It is a DIFFUSE
BILATERAL REGION** — a **single leaf** directly under
``tegmentum/``. **The tree represents it cleanly.** **The PAG is
the ACTUAL proof case for the diffuse bilateral category** — the
on-disk evidence the falsified MRF could not provide.

**Do not** assume the PAG is a **paired structure** — it is **not**
— it is a **continuous column** surrounding the aqueduct, not two
separate structures on the left and right.

**Do not** assume the PAG is a **midline nucleus** — it is **not**
— it is **not a discrete nucleus on the midline**; it **surrounds
the aqueduct** and **extends laterally** into the adjacent
tegmentum. **The `midbrain/` container's "midline structure"
framing is HALF-WRONG** — the PAG is **not paired** (correct) but
**not a discrete midline nucleus** (incorrect). **The `tegmentum/`
container's "treated as paired in the tree" framing is FULLY
WRONG** — the on-disk path is a **single leaf**.

**Do not** assume the PAG is a **discrete nucleus** with a **single
transmitter** and a **single function** — it is a **diffuse
modulatory column** with **heterogeneous transmitters** and
**heterogeneous functions** (pain modulation, defensive behavior,
autonomic control, vocalization, reproductive behavior, nausea).

**Do not** assume the PAG is a **cranial nerve nucleus** — it is
**not** and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the PAG is the **cerebral aqueduct**. The
**aqueduct** is the **midline CSF conduit** — the PAG **surrounds**
it. **They are DIFFERENT STRUCTURES** — the **aqueduct** is a
**CSF space**; the **PAG** is a **gray-matter column**.

**Do not** assume the PAG is the **tectum** — the tectum is
**dorsal** to the aqueduct. **The PAG is around the aqueduct.**

**Do not** assume the PAG is the **MRF** — the MRF is **ventral**
to the PAG. **Different diffuse bilateral region.**

**Do not** assume the PAG is the **CLi**, the **DR**, or the
**IPN** — those are **midline nuclei**. **The PAG is a diffuse
bilateral region** — a **different laterality class**.

**Do not** assume the PAG is the **raphe magnus** or the **RVM** —
those are **medullary** structures, **downstream** of the PAG. **The
PAG projects to the RVM** for descending pain modulation.

**Do not** assume the PAG is the **amygdala** or the
**hypothalamus** — those are **telencephalic** and **diencephalic**
respectively. **The PAG is mesencephalic**.

**Do not** assume the PAG is the **red nucleus**, the **substantia
nigra**, or the **VTA** — those are **discrete nuclei**. **The PAG
is a diffuse modulatory column** — a **different structure class**.

**Do not** assume the PAG is the **pontine reticular formation** —
that is a **pontine** reticular region. **The PAG is midbrain**,
at the pontomesencephalic junction.

**Do not** assume the PAG is the **cerebral peduncle** — that is
the **ventral surface** (a conduction pathway). **The PAG is around
the aqueduct.**

**Do not** import the **GABAergic**, **glutamatergic**, **opioid**,
**dopaminergic**, **serotonergic**, or **cholinergic** phenotypes
into the midbrain structural layer. Those are
**``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the PAG. **Diffuse
bilateral regions carry NO coupling warning** — same rule as every
non-oscillator class. **The diffuse bilateral position is not a
coupling hazard.**

**Do not** treat the PAG as a **paired structure** or a **midline
nucleus**. It is a **diffuse bilateral modulatory column** — a
**single leaf** — the **second diffuse bilateral region** in the
family (after the MRF).

Iterating the periaqueductal gray's (empty) children (recommended
consumer pattern)::

    PERIAQUEDUCTAL_GRAY_CHILDREN = ()
    # The periaqueductal gray is a leaf. The subregions (dorsal
    # PAG, lateral PAG, ventrolateral PAG, dorsomedial PAG) are
    # prose, not modules.

Bilateral iteration — **NOT APPLICABLE**::

    # The periaqueductal gray is DIFFUSE BILATERAL — it has NO
    # left/right pair (not paired) and NO midline position (it
    # surrounds the aqueduct and extends laterally). There is no
    # bilateral iteration for the PAG. If you find yourself
    # writing:
    #
    #     for side in ("left", "right"):
    #         path = f"midbrain.tegmentum.{side}.periaqueductal_gray"
    #
    # — that is WRONG. The PAG is at:
    #
    #     midbrain.tegmentum.periaqueductal_gray
    #
    # — a single diffuse bilateral leaf. The tree represents the
    # PAG correctly. (This is the THIRD laterality class — paired,
    # midline, diffuse bilateral — beyond the paired structures
    # like the SN and the midline structures like the DR.)

Reaching the cerebral aqueduct (recommended consumer pattern — the
MIDLINE CSF conduit that the PAG SURROUNDS)::

    # The cerebral aqueduct is the MIDLINE CSF CONDUIT that the PAG
    # SURROUNDS:
    #
    #   brainparts.midbrain.cerebral_aqueduct
    #
    # The PAG is the gray-matter column AROUND the aqueduct. They
    # are DIFFERENT STRUCTURES — the aqueduct is a CSF space; the
    # PAG is a gray-matter column.

Reaching the MRF (recommended consumer pattern — the VENTRAL
diffuse bilateral region)::

    # The midbrain reticular formation (MRF) is the VENTRAL diffuse
    # bilateral region — the diffuse reticular region of the
    # ventral tegmentum:
    #
    #   brainparts.midbrain.tegmentum.midbrain_reticular_formation
    #
    # The MRF is VENTRAL to the PAG. Both are DIFFUSE BILATERAL —
    # the same laterality class — but DIFFERENT STRUCTURES
    # (MRF = reticular, arousal/locomotion; PAG = modulatory,
    # pain/defensive behavior/autonomic).

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
    # nuclei on the midline. The PAG is a DIFFUSE BILATERAL
    # REGION — not a midline nucleus. DIFFERENT laterality classes
    # (midline vs. diffuse bilateral).

Reaching the RVM (recommended consumer pattern — the DOWNSTREAM
medullary target)::

    # The rostral ventromedial medulla (RVM) — including the raphe
    # magnus — is the DOWNSTREAM medullary target of the PAG's
    # descending pain-modulation projection:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.raphe_magnus
    #   (and the broader RVM)
    #
    # The PAG → RVM → spinal cord circuit is the DESCENDING PAIN-
    # MODULATION pathway. The PAG is UPSTREAM of the RVM.

Reaching the amygdala (recommended consumer pattern — the UPSTREAM
telencephalic input)::

    # The amygdala (especially the central nucleus) is the UPSTREAM
    # telencephalic input to the PAG — the amygdala → PAG circuit
    # is part of the fear/defensive-behavior system:
    #
    #   brainparts.forebrain.telencephalon.subcortical.medial_temporal_lobe.amygdala
    #
    # The amygdala DETECTS the threat; the PAG EXECUTES the
    # defensive response. The amygdala is UPSTREAM of the PAG in
    # the fear → defensive-behavior circuit.

Reaching the hypothalamus (recommended consumer pattern — the
UPSTREAM diencephalic input)::

    # The hypothalamus is the UPSTREAM diencephalic input to the
    # PAG — the hypothalamus → PAG circuit is part of the
    # defensive-behavior and autonomic-control systems:
    #
    #   brainparts.forebrain.diencephalon.hypothalamus
    #
    # The hypothalamus is UPSTREAM of the PAG in the autonomic and
    # defensive-behavior circuits.

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
    # The red nucleus, the SN, and the VTA are DISCRETE NUCLEI.
    # The PAG is a DIFFUSE MODULATORY COLUMN. DIFFERENT structure
    # classes.

Reaching the tectum (recommended consumer pattern — the DORSAL
midbrain compartment)::

    # The tectum — the superior colliculus and the inferior
    # colliculus — is the DORSAL midbrain compartment, DORSAL to
    # the cerebral aqueduct and the PAG:
    #
    #   brainparts.midbrain.tectum
    #
    # The tectum is DORSAL; the PAG is AROUND the aqueduct. DIFFERENT
    # compartments of the midbrain.

Reaching the cerebral peduncle (recommended consumer pattern — the
VENTRAL midbrain structure)::

    # The cerebral peduncle is the VENTRAL-most descending fiber
    # bundle — the crus cerebri — VENTRAL to the substantia nigra
    # and the tegmentum:
    #
    #   brainparts.midbrain.cerebral_peduncle
    #
    # The PAG is AROUND the aqueduct (dorsal). They are DIFFERENT
    # structures in DIFFERENT positions.

Subregion detail (not wired — consult references)::

    # The periaqueductal gray has FUNCTIONAL SUBREGIONS —
    # longitudinal columns around the aqueduct, NOT discrete nuclei:
    #
    #   dorsal PAG (dPAG)          -> "ACTIVE" defensive behavior —
    #                                  fight-or-flight, escape,
    #                                  hypertension, tachycardia;
    #                                  fear, anxiety
    #   lateral PAG (lPAG)         -> "PASSIVE" defensive behavior —
    #                                  freezing, hypotension,
    #                                  bradycardia, analgesia;
    #                                  autonomic control;
    #                                  vocalization
    #   ventrolateral PAG (vlPAG)  -> PRINCIPAL pain-modulation
    #                                  column — the PAG -> RVM ->
    #                                  spinal cord descending pain-
    #                                  inhibition pathway — analgesia
    #                                  (opioid and non-opioid);
    #                                  reproductive behavior
    #                                  (lordosis)
    #   dorsomedial PAG (dmPAG)    -> pain modulation; defensive
    #                                  behavior; autonomic control
    #
    # ALL of these subregions are LONGITUDINAL COLUMNS of a
    # continuous region — NOT discrete nuclei. The PAG's subnuclear
    # organization REINFORCES its diffuse-region representation.
    #
    # Do not attempt to resolve these subregions as sub-paths of
    # the periaqueductal gray — they are PROSE, not modules.

The descending pain-modulation pathway — detail (not wired —
consult references)::

    # The DESCENDING PAIN-MODULATION pathway — the PAG is the TOP:
    #
    #   INPUTS to the PAG:
    #     - ascending somatosensory (spinal cord, trigeminal)
    #     - amygdala (central nucleus), BNST (fear/emotion)
    #     - prefrontal cortex, anterior cingulate cortex, insula
    #     - hypothalamus (autonomic, homeostatic)
    #
    #   THE PAG (ventrolateral PAG) -> RVM (rostral ventromedial
    #   medulla, including the raphe magnus) -> SPINAL CORD (dorsal
    #   horn) -> INHIBITION of nociceptive neurons -> ANALGESIA
    #
    # The PAG is the TOP of the descending pain-inhibition system.
    # The PAG is rich in OPIOID RECEPTORS (mu, delta, kappa) —
    # opioid microinjection into the PAG produces profound
    # analgesia — the PAG is a SITE OF ACTION of opioid analgesia.
    #
    # Do not attempt to resolve the RVM, the raphe magnus, or the
    # spinal cord as sub-paths of the PAG — they are DIFFERENT
    # structures at DIFFERENT levels.

The defensive-behavior circuit — detail (not wired — consult
references)::

    # The DEFENSIVE-BEHAVIOR circuit — the PAG is the FINAL COMMON
    # PATHWAY:
    #
    #   THREAT DETECTION:
    #     - amygdala (central nucleus) — fear learning
    #     - BNST — sustained anxiety
    #     - medial prefrontal cortex — threat appraisal
    #
    #   THE PAG (dPAG, lPAG) -> AUTONOMIC + MOTOR + VOCALIZATION
    #   OUTPUTS:
    #     - RVLM (cardiovascular — hypertension, tachycardia OR
    #       hypotension, bradycardia)
    #     - respiratory centers (hyperventilation OR hypoventilation)
    #     - spinal cord motor neurons (fight/flight OR freezing)
    #     - vocalization centers (laryngeal motor neurons)
    #
    # The AMYGDALA detects the threat; the PAG EXECUTES the
    # defensive response. The dPAG produces the "active" defensive
    # response (fight-or-flight); the lPAG produces the "passive"
    # defensive response (freezing).
    #
    # Do not attempt to resolve the amygdala, the BNST, the RVLM,
    # or the spinal cord as sub-paths of the PAG — they are
    # DIFFERENT structures at DIFFERENT levels.

The clean diffuse-bilateral representation — detail (not wired —
structural note)::

    # The periaqueductal gray is the SECOND CLEANLY-REPRESENTED
    # DIFFUSE BILATERAL REGION in the tree — and the FIRST
    # GENUINELY CLEAN one:
    #
    #   midbrain.tegmentum.periaqueductal_gray
    #     (ONE leaf — DIFFUSE BILATERAL — NO left/ or right/ nodes)
    #
    # This is the CORRECT representation — the PAG is a continuous
    # column around the aqueduct, not a paired structure and not a
    # midline nucleus.
    #
    # THE SECOND DIFFUSE BILATERAL REGION — after the MRF:
    #   MRF — first diffuse bilateral region — FALSIFIED (its
    #     left/ and right/ nodes contradict its clean-case claim)
    #   PAG — second diffuse bilateral region — ACTUALLY CLEAN
    #     (the on-disk path is a single leaf — the tree represents
    #     it correctly)
    #
    # THE ACTUAL CLEAN CASE FOR THE DIFFUSE BILATERAL CATEGORY:
    # The PAG is the ON-DISK EVIDENCE the MRF could not be. The
    # MRF's falsification removed the MRF's clean-case claim, but
    # NOT the category's on-disk evidence — that was always the
    # PAG, not the MRF.
    #
    # THE PAG SETTLES TWO CONTAINER CONTRADICTIONS:
    #   - The midbrain container said "the PAG is a midline
    #     structure, not paired" — HALF-RIGHT (not paired),
    #     HALF-WRONG (not a discrete midline nucleus).
    #   - The tegmentum container said "the PAG is treated as
    #     paired in the tree" — FULLY WRONG (the on-disk path is
    #     a single leaf).
    #   BOTH CONTAINERS SHOULD BE AMENDED — the PAG provides the
    #   on-disk evidence.
    #
    # THE PAG IS THE NEW PROOF CASE for the tegmentum container
    # amendment's DIFFUSE BILATERAL category — taking over from
    # the falsified MRF. The tegmentum container amendment should
    # permit BOTH midline nuclei AND diffuse bilateral regions as
    # direct children — and the diffuse bilateral category now has
    # CONCRETE ON-DISK EVIDENCE: the PAG.

Clinical-pattern detail (not wired — consult references)::

    # The periaqueductal gray has NO NAMED SYNDROME OF ITS OWN —
    # its clinical associations are DIRECT and SUBSTANTIAL, via
    # its descending pain-modulation, defensive-behavior, and
    # autonomic-control functions:
    #
    #   CHRONIC PAIN              -> DIRECT — PAG pain-modulation
    #     (fibromyalgia, chronic      dysfunction is implicated;
    #      neuropathic pain,          the PAG -> RVM -> spinal cord
    #      chronic low back pain)     pathway is impaired; the PAG
    #                                 is a key substrate (not the
    #                                 sole substrate — the RVM, the
    #                                 peripheral nociceptors, and
    #                                 the cortical pain networks
    #                                 are also involved)
    #   FEAR / ANXIETY / PANIC    -> DIRECT — the PAG-amygdala
    #     (panic disorder, PTSD,      defensive-behavior circuit is
    #      generalized anxiety)       implicated; the dorsal PAG is
    #                                 implicated in panic; PAG
    #                                 stimulation produces panic-like
    #                                 responses; PAG lesions can reduce
    #                                 panic
    #   DEFENSIVE BEHAVIOR        -> DIRECT — the PAG is the final
    #     (freezing, fight-or-       common pathway; the dPAG for
    #      flight)                    active defensive behavior, the
    #                                 lPAG for passive
    #   VOCALIZATION              -> DIRECT — PAG lesions produce
    #     (mutism, vocalization       mutism; PAG stimulation elicits
    #      disorders)                 vocalization; the PAG is the
    #                                 final common pathway for
    #                                 emotional vocalization
    #   AUTONOMIC DYSFUNCTION     -> DIRECT — PAG dysfunction can
    #     (cardiovascular,            produce autonomic abnormalities
    #      respiratory)               (the hypothalamus, the RVLM,
    #                                 the NTS, the nucleus ambiguus
    #                                 are also involved)
    #   NAUSEA AND VOMITING       -> DIRECT — PAG lesions and
    #                                 stimulation can produce nausea
    #                                 and vomiting; the PAG projects to
    #                                 the brainstem vomiting centers
    #   MIGRAINE                  -> INDIRECT — the PAG's pain-
    #                                 modulation dysfunction is
    #                                 implicated; the primary peripheral
    #                                 substrate is the trigeminovascular
    #                                 system
    #
    # No named periaqueductal gray syndrome exists. The PAG is a
    # KEY SUBSTRATE — but NOT the sole substrate — for each of
    # these.
    #
    # Do not conflate these patterns — they localize primarily to
    # the PAG's specific columns (dPAG, lPAG, vlPAG, dmPAG), the
    # amygdala, the RVM, the hypothalamus, or the trigeminovascular
    # system — not to the PAG alone.

References
----------
*   **Canonical PAG anatomy:** Behbehani, M.M. (1995). "Functional
    characteristics of the midbrain periaqueductal gray."
    *Progress in Neurobiology* 46:575–605. (The PAG — its
    longitudinal columns (dorsal, lateral, ventrolateral,
    dorsomedial), its heterogeneous neurons, its diverse inputs
    and outputs, its role in pain modulation, defensive behavior,
    autonomic control, and vocalization.)
*   **PAG — comprehensive review:** Bandler, R., Shipley, M.T.
    (1994). "Columnar organization in the midbrain periaqueductal
    gray: modules for emotional expression?" *Trends in
    Neurosciences* 17:379–389. (The PAG's columnar organization —
    the dorsal, lateral, ventrolateral, and dorsomedial columns —
    as "modules for emotional expression.")
*   **PAG and descending pain modulation:** Fields, H.L., Basbaum,
    A.I. (1978). "Brainstem control of spinal pain-transmission
    neurons." *Annual Review of Physiology* 40:217–248. (The
    PAG → RVM → spinal cord descending pain-modulation pathway.)
*   **PAG and opioid analgesia:** Yaksh, T.L., Rudy, T.A. (1978).
    "Narcotic analgetics: CNS sites and mechanisms of action as
    revealed by intracerebral injection techniques." *Pain*
    4:299–359. (The PAG as the site of action of opioid
    analgesia — the opioid microinjection studies.)
*   **PAG — the descending pain-inhibition system review:**
    Fields, H.L., Heinricher, M.M., Mason, P. (2006). "Neurotransmitters
    in nociceptive modulatory circuits." *Annual Review of
    Neuroscience* 14:219–245. (The PAG-RVM-spinal cord descending
    pain-inhibition system — the "ON" and "OFF" cells of the RVM.)
*   **PAG — defensive behavior:** Bandler, R., Keay, K.A., Floyd,
    N., Price, J. (2000). "Central circuits mediating patterned
    autonomic activity during active vs. passive emotional
    coping." *Brain Research Bulletin* 53:95–104. (The PAG's
    role in active vs. passive defensive behavior — the dPAG for
    "active" coping, the lPAG for "passive" coping.)
*   **PAG — panic disorder and the dPAG:** Schenberg, L.C.,
    Bittencourt, A.S., Sudré, E.C., Vargas, L.C. (2001). "Modeling
    panic attacks." *Neuroscience & Biobehavioral Reviews*
    25:647–659. (The dPAG as the panic-generation site — the
    PAG stimulation studies producing panic-like responses; the
    PAG lesions reducing panic.)
*   **PAG — fear and the amygdala-PAG circuit:** LeDoux, J.E.
    (2000). "Emotion circuits in the brain." *Annual Review of
    Neuroscience* 23:155–184. (The amygdala → PAG circuit — the
    fear → defensive-behavior pathway.)
*   **PAG — vocalization:** Jürgens, U. (1994). "The role of the
    periaqueductal gray in the vocal control of the squirrel
    monkey." *Behavioural Brain Research* 65:63–73. (The PAG as
    the final common pathway for vocalization — the PAG lesions
    producing mutism; the PAG stimulation eliciting vocalization.)
*   **PAG — autonomic control:** Lovick, T.A. (1993). "Integrated
    activity of putative vasomotor neurons in the rostral
    ventrolateral medulla." *American Journal of Physiology*
    264:R1050–R1057. (The PAG's projections to the RVLM and the
    autonomic centers — the PAG's autonomic-control function.)
*   **PAG — reproductive behavior:** Lonstein, J.S., Stern, J.M.
    (1997). "Role of the midbrain periaqueductal gray in maternal
    nurturance and aggression: c-fos and electrolytic lesion
    studies in lactating rats." *Journal of Neuroscience*
    17:3364–3378. (The PAG's role in reproductive behavior and
    maternal behavior — the lordosis reflex and maternal
    aggression.)
*   **PAG — nausea and vomiting:** Hornby, P.J. (2001). "Central
    neurocircuitry of nausea." *Current Opinion in Pharmacology*
    1:591–595. (The PAG's projections to the brainstem vomiting
    centers — the PAG's role in nausea and vomiting.)
*   **MRF (contrast — the FIRST diffuse bilateral region, and the
    falsified clean case):** Moruzzi, G., Magoun, H.W. (1949).
    "Brain stem reticular formation and activation of the EEG."
    *Electroencephalography and Clinical Neurophysiology*
    1:455–473. (The MRF — the first diffuse bilateral region in
    the tree — the falsified clean case for the diffuse bilateral
    category.)
*   **Cerebral aqueduct (contrast — the CSF conduit that the PAG
    SURROUNDS):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (The cerebral aqueduct —
    the midline CSF conduit — surrounded by the PAG.)
*   **SLEA (contrast — the PAG is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the periaqueductal gray.)
*   NeuroNames — Periaqueductal gray; FMA — Periaqueductal gray.
    **The PAG is a diffuse column — it has no "left" or "right"
    subdivision in the standard anatomical atlases; it is a
    continuous column surrounding the midbrain aqueduct.**
"""