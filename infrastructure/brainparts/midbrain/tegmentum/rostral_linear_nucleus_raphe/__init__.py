"""
infrastructure.brainparts.midbrain.tegmentum.rostral_linear_nucleus_raphe
=======================================================================

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
        ├── periaqueductal_gray     (diffuse bilateral leaf — CLEAN)
        ├── red_nucleus             (structure container)
        ├── rostral_interstitial_nucleus_mlf (structure container)
        └── rostral_linear_nucleus_raphe      <-- THIS MODULE (MIDLINE
            └── (single leaf)                   LEAF — the FIRST
                                                ACTUAL CLEAN MIDLINE
                                                LEAF IN THE TREE)

**Primary synonym:** Rostral linear nucleus of the raphe; **RLi**;
**rostral linear nucleus**; **nucleus linearis rostralis** (Latin);
**rostral linear subdivision of the rostral raphe complex**; **the
rostral linear raphe nucleus**.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **midline serotonergic nucleus** in the **ventral
midbrain tegmentum** — at the level of the **caudal diencephalon /
rostral midbrain**, near the **ventral tegmental area** and the
**interpeduncular fossa**, **rostral and ventral to the caudal
linear nucleus (CLi)**. It is a **small** nucleus — smaller than
the DR — composed **primarily of serotonergic neurons**
(tryptophan hydroxylase-positive, 5-HT-positive) — **part of the
rostral raphe complex**. **The serotonergic phenotype** is a
**``chemicals_hormones``-layer fact** — see *Chemicals-Layer
Discipline*. **Unlike the CLi**, which has a **dopaminergic
subpopulation** (part of the A10 group), the RLi is **primarily
serotonergic** — it does **not** have a significant dopaminergic
subpopulation.
**Container status:** **This module is a LEAF**, **midline** — it
is **NOT** under ``tegmentum/left/`` or ``tegmentum/right/`` — it
sits **directly under** the tegmentum container. **It is the FIRST
ACTUAL CLEANLY-REPRESENTED MIDLINE LEAF IN THE TREE** — the on-disk
path is a **single leaf**
(``tegmentum/rostral_linear_nucleus_raphe/``) with **no `left/` or
`right/` nodes**. **The CLi and the DR are BOTH represented as
paired** (anomalous — their own `left/` and `right/` modules flag
this). **The IPN was held up as the clean midline case and was
FALSIFIED** — its own `left/` and `right/` nodes contradict its
clean-case claim. **The RLi is the ACTUAL clean midline case** —
**the one the CLi, the DR, and the IPN should follow** (Resolution
B). See *The First Actual Clean Midline Leaf*.
**Part of:** The **tegmentum** region container — as a **midline**
leaf. **The RLi is NOT a cranial nerve nucleus** and is **NOT
cross-listed** with ``cranial_nerve_nuclei/``.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — **midline**, **not** a side
container.
**Structural children:** **None.** This is a **leaf** module. The
**serotonergic neuron population** is **the whole nucleus**, not a
structural child — the RLi has **no classical subnuclear
organization** (unlike the DR's dorsal / ventral / ventrolateral /
interfascicular / caudal subnuclei). **The serotonergic neurons**
are documented as **prose**, not as structural children.
**Boundary status (MIDLINE LEAF — THE FIRST ACTUAL CLEANLY-
REPRESENTED MIDLINE LEAF IN THE TREE):** **Boundary case — the
rostral linear nucleus of the raphe is a MIDLINE LEAF, and the
tree represents it CLEANLY** — **directly under** ``tegmentum/`` —
**NO** ``tegmentum/rostral_linear_nucleus_raphe/left/`` and
**NO** ``tegmentum/rostral_linear_nucleus_raphe/right/``. **The RLi
is the FIRST ACTUAL CLEANLY-REPRESENTED MIDLINE LEAF IN THE TREE**
— the **on-disk path is a single leaf**. **The CLi and the DR are
BOTH represented as paired** (anomalous — their own `left/` and
`right/` modules flag this). **The IPN was held up as the clean
midline case and was FALSIFIED** — its own `left/` and `right/`
nodes contradict its clean-case claim (see the IPN's own `left/`
and `right/` modules). **The RLi is the ACTUAL clean midline
case** — **not a claimed-then-falsified clean case, but the
genuinely clean case the tree has for the midline category**.
**The RLi's clean representation RESTORES the on-disk evidence for
the midline exception category** of the tegmentum container
amendment — which the IPN falsification had erased. **The midline
category now has ONE clean on-disk example: the RLi.** **The
tegmentum container amendment's midline exception category now has
the on-disk evidence it needed** — **the RLi is the actual clean
midline case the CLi, the DR, and the IPN should follow**
(Resolution B). See *The First Actual Clean Midline Leaf* and
*The Midline Category Restored*.
**Boundary status (THE FIRST ACTUAL CLEAN MIDLINE LEAF — the CASE
the CLi, DR, and IPN should follow — and the RESTORATION of the
midline category's on-disk evidence):** **Boundary case — the RLi
is the FIRST ACTUAL CLEANLY-REPRESENTED MIDLINE LEAF IN THE TREE —
the case the CLi, the DR, and the IPN should follow (Resolution B)
— and the restoration of the midline category's on-disk evidence.**
*   **The CLi** (``.../tegmentum/caudal_linear_nucleus/``) — a
    **midline** serotonergic/dopaminergic nucleus — is
    **represented as paired** (anomalous —
    ``.../caudal_linear_nucleus/left/`` and
    ``.../caudal_linear_nucleus/right/``). Its own leaf, its
    `left/` module, and its `right/` module all flag the
    anomaly and recommend **Resolution B** — removing the
    `left/` and `right/` nodes so that the CLi is represented
    as a **single midline leaf**, consistent with its anatomy.
*   **The DR** (``.../tegmentum/dorsal_raphe_nucleus/``) — a
    **midline** serotonergic nucleus — is **represented as
    paired** (anomalous — ``.../dorsal_raphe_nucleus/left/``
    and ``.../dorsal_raphe_nucleus/right/``). Its own leaf
    **assumed a clean representation** (its own "the tree
    represents the DR cleanly" framing was **FALSIFIED** by
    the on-disk `left/` and `right/` nodes), and its `left/`
    and `right/` modules flag the **falsified-assumption**
    and recommend **Resolution B**.
*   **The IPN** (``.../tegmentum/interpeduncular_nucleus/``) — a
    **midline** GABAergic limbic relay — was **held up as the
    clean midline case** and was **FALSIFIED** — its own
    `left/` and `right/` modules flag the **falsified-proof-
    case** and recommend **Resolution B**.
*   **The RLi** (this module) — a **midline** serotonergic
    nucleus — is **actually clean** — the **on-disk path is a
    single leaf**, and the tree represents it **exactly as
    its anatomy demands**.
**The RLi is the FIRST ACTUAL CLEAN midline leaf in the tree** —
**the case the CLi, the DR, and the IPN should follow**
(Resolution B). **The RLi's clean representation RESTORES the
on-disk evidence for the midline exception category** of the
tegmentum container amendment — **the midline category now has
ONE clean on-disk example: the RLi** (parallel to the diffuse
bilateral category's clean example: the PAG). **The tegmentum
container amendment's TWO exception categories BOTH now have
clean on-disk examples** — **the midline category: the RLi**
**and** **the diffuse bilateral category: the PAG** — **even
though the CLi, the DR, the IPN, and the MRF remain anomalous
(paired representations) and the joint Resolution B is still
needed for them**. **The RLi's clean representation is the
PROOF that the tree CAN represent midline nuclei cleanly** — the
**actual proof the IPN could not provide**. See *The First
Actual Clean Midline Leaf* and *The Midline Category Restored*.
**Boundary status (MIDLINE CATEGORY RESTORED — the tegmentum
container amendment's midline exception category now has on-disk
evidence — the RLi):** **Boundary case — the RLi RESTORES the
on-disk evidence for the midline exception category of the
tegmentum container amendment.** **The CLi, the DR, and the IPN
are all represented as paired** (anomalous — their own `left/`
and `right/` modules flag this), so the **midline category had
NO clean on-disk example** — **the IPN's clean-case claim was
falsified**. **The RLi is actually clean** — a **single leaf** —
**so the midline category now has ONE clean on-disk example**.
**The tegmentum container amendment's TWO exception categories
BOTH now have clean on-disk examples:**
*   **Midline category** — **the RLi** (this module) — a
    **single midline leaf**, correctly represented.
*   **Diffuse bilateral category** — **the PAG**
    (``.../tegmentum/periaqueductal_gray/``) — a **single
    diffuse bilateral leaf**, correctly represented.
**The tegmentum container amendment's evidence base is now
COMPLETE** — **both exception categories have at least one clean
on-disk example** — **the RLi for the midline category** and
**the PAG for the diffuse bilateral category**. **The CLi, the
DR, the IPN, and the MRF remain anomalous** — **the joint
Resolution B is still needed for them** — but **the categories
themselves are now evidenced by the RLi and the PAG**. **The
tegmentum container amendment is now fully evidenced** — the
**midline exception category** by the **RLi**, the **diffuse
bilateral exception category** by the **PAG**, and the **paired
structure-container pattern** by the **red nucleus** and the
**riMLF**. **The three patterns the amendment needs to
acknowledge are ALL now evidenced by clean on-disk examples.**
See *The Midline Category Restored* and *Design Contract — Live
amendment to the tegmentum container*.
**Boundary status (NOT a CN nucleus — NOT cross-listed with
``cranial_nerve_nuclei/``):** **Boundary case — the rostral linear
nucleus of the raphe is NOT a cranial nerve nucleus.** It is a
**serotonergic neuromodulatory nucleus** — it is **not a CN
nucleus** and is **NOT cross-listed** with the
``cranial_nerve_nuclei/`` container. The **four CN nuclei** in the
tegmentum (oculomotor, trochlear, Edinger-Westphal,
mesencephalic trigeminal) are **cross-listed** between
``tegmentum/`` and ``cranial_nerve_nuclei/`` — **the RLi is not
one of them**. Consumers must **not** look for the RLi under
``.../cranial_nerve_nuclei/`` — it has **one path only**:
``.../tegmentum/rostral_linear_nucleus_raphe/``.
**Boundary status (NOT the caudal linear nucleus — the CLi is the
CAUDAL sibling linear nucleus, and it has a dopaminergic
subpopulation the RLi does not):** **Boundary case — the rostral
linear nucleus of the raphe is NOT the caudal linear nucleus
(CLi).** The **CLi** (``.../tegmentum/caudal_linear_nucleus/``) is
the **caudal** sibling linear nucleus — **more caudal**, **more
ventral**, **at the level of the inferior colliculus** — with
**two functionally and neurochemically distinct subpopulations**:
a **serotonergic** majority and a **dopaminergic** minority (part
of the **A10 group** with the **VTA**). **The RLi** (here) is the
**rostral** sibling — **more rostral**, **more dorsal**, **at the
level of the caudal diencephalon / rostral midbrain** — and it is
**primarily serotonergic** — it does **not** have a significant
dopaminergic subpopulation. **They are SIBLING LINEAR NUCLEI** —
**different structures at different rostrocaudal levels**,
**different transmitter compositions** (the CLi has both
serotonergic and dopaminergic; the RLi is primarily
serotonergic), and **different tree representations** (the CLi
is anomalous paired; the RLi is actually clean). Consumers must
**not** conflate the RLi with the CLi.
**Boundary status (NOT the dorsal raphe nucleus — the DR is the
LARGEST serotonergic nucleus, a SIBLING midline raphe nucleus):**
**Boundary case — the rostral linear nucleus of the raphe is NOT
the dorsal raphe nucleus (DR).** The **DR**
(``.../tegmentum/dorsal_raphe_nucleus/``) is the **largest
serotonergic nucleus in the brain** — the **principal serotonergic
nucleus** of the **forebrain** — the **primary target of SSRI
pharmacology**. **The RLi** (here) is a **smaller** serotonergic
nucleus — **more rostral and more ventral than the DR** — a
**smaller contributor** to the **ascending serotonergic system**.
**They are SIBLING MIDLINE RAPHE NUCLEI** — **different
structures**, **different sizes**, **different projections**
(the DR projects more strongly to the forebrain; the RLi projects
more locally to the midbrain and diencephalon), **different
clinical weights** (the DR is the **primary** serotonergic
substrate for mood disorders; the RLi is a **smaller
contributor**), **and different tree representations** (the DR is
anomalous paired; the RLi is actually clean). Consumers must
**not** conflate the RLi with the DR. **The DR is the primary
serotonergic nucleus; the RLi is a smaller contributor.**
**Boundary status (NOT the median raphe nucleus — the MnR is a
PONTINE raphe nucleus):** **Boundary case — the rostral linear
nucleus of the raphe is NOT the median raphe nucleus (MnR).** The
**MnR** (``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``)
is a **pons** structure — the **pontine** median raphe — the
**primary serotonergic projection to the hippocampus**. **The RLi
is midbrain.** They are **DIFFERENT STRUCTURES at DIFFERENT
levels** — the **MnR** is **rhombencephalic**; the **RLi** is
**mesencephalic**. **The MnR is sometimes grouped with the rostral
raphe complex in functional discussions** — but the **MnR is
pons**, and the **RLi is midbrain**. Consumers must **not**
conflate the RLi with the MnR.
**Boundary status (NOT the VTA or the substantia nigra — those are
PAIRED dopaminergic nuclei):** **Boundary case — the rostral
linear nucleus of the raphe is NOT the ventral tegmental area
(VTA) or the substantia nigra (SN).** The **VTA**
(``.../tegmentum/left/ventral_tegmental_area/`` and the right
counterpart) and the **SN**
(``.../tegmentum/left/substantia_nigra/`` and the right
counterpart) are **PAIRED dopaminergic nuclei**. **The RLi is
MIDLINE and primarily SEROTONERGIC** — it is **not** a dopaminergic
nucleus. **The CLi** (the RLi's caudal sibling) has a
dopaminergic subset — but **the RLi does not**. **The VTA and the
SN are the PAIRED dopaminergic nuclei; the RLi is a MIDLINE
serotonergic nucleus.** Consumers must **not** conflate the RLi
with the VTA or the SN — **even though the RLi sits near the VTA
anatomically**.
**Boundary status (NOT the periaqueductal gray — the PAG is a
DIFFUSE BILATERAL region):** **Boundary case — the rostral linear
nucleus of the raphe is NOT the periaqueductal gray (PAG).** The
**PAG** (``.../tegmentum/periaqueductal_gray/``) is a **diffuse
bilateral region** — a **continuous column** around the
**cerebral aqueduct** — **pain modulation** and **defensive
behavior**. **The RLi is a midline nucleus** — a **small discrete
nucleus on the midline** — **ascending serotonergic modulation**.
**They are DIFFERENT STRUCTURES of DIFFERENT laterality classes**
— the **PAG is diffuse bilateral**; the **RLi is midline**.
Consumers must **not** conflate the RLi with the PAG.
**Boundary status (NOT the midbrain reticular formation — the MRF is
a DIFFUSE BILATERAL reticular region):** **Boundary case — the
rostral linear nucleus of the raphe is NOT the midbrain reticular
formation (MRF).** The **MRF**
(``.../tegmentum/midbrain_reticular_formation/``) is a **diffuse
bilateral reticular region** — **arousal**, **locomotion**,
**sensorimotor integration**. **The RLi is a midline nucleus** —
a **small discrete nucleus on the midline** — **ascending
serotonergic modulation**. **They are DIFFERENT STRUCTURES of
DIFFERENT laterality classes** — the **MRF is diffuse
bilateral**; the **RLi is midline**. Consumers must **not**
conflate the RLi with the MRF.
**Boundary status (NOT the interpeduncular nucleus — the IPN is a
MIDLINE GABAergic limbic relay):** **Boundary case — the rostral
linear nucleus of the raphe is NOT the interpeduncular nucleus
(IPN).** The **IPN** (``.../tegmentum/interpeduncular_nucleus/``)
is a **midline GABAergic limbic relay** — the **principal
downstream relay of the habenula** — **pain modulation**,
**defensive behavior**, **autonomic control**, **vocalization**,
**reproductive behavior**, **nausea and vomiting**. **The RLi is
a midline serotonergic neuromodulatory nucleus** — a **smaller
contributor** to the **ascending serotonergic system**. **They are
SIBLING MIDLINE NUCLEI** — **different structures**,
**different transmitter classes** (the IPN is GABAergic; the RLi
is serotonergic), **different functional systems** (the IPN is a
**limbic relay**; the RLi is a **serotonergic neuromodulator**),
**and different tree representations** (the IPN was held up as
the clean midline case and was **falsified**; the RLi is
**actually clean**). Consumers must **not** conflate the RLi with
the IPN.
**Boundary status (NOT the red nucleus or the riMLF — those are
PAIRED premotor relays):** **Boundary case — the rostral linear
nucleus of the raphe is NOT the red nucleus or the riMLF.** The
**red nucleus** (``.../tegmentum/red_nucleus/``) is a **paired
premotor motor relay** — the **rubrospinal motor coordination**.
The **riMLF**
(``.../tegmentum/rostral_interstitial_nucleus_mlf/``) is a
**paired premotor saccade generator** — the **vertical saccade
generator**. **The RLi is a midline serotonergic neuromodulatory
nucleus** — an **ascending serotonergic modulator**. **They are
DIFFERENT STRUCTURES of DIFFERENT laterality classes and DIFFERENT
structure classes** — the **red nucleus** and the **riMLF** are
**paired premotor relays** (structure containers); the **RLi** is
a **midline neuromodulatory nucleus** (single leaf). Consumers
must **not** conflate the RLi with the red nucleus or the riMLF.
**Boundary status (SEROTONERGIC — the phenotype is a
``chemicals_hormones``-layer fact):** **Boundary case — the
rostral linear nucleus of the raphe is **serotonergic** (the
overwhelming majority of its neurons).** The **serotonergic
phenotype** (tryptophan hydroxylase, 5-HT synthesis, serotonin
transporters, serotonin receptors) is a
**``chemicals_hormones``-layer fact** — the **neurochemical**
fact, **not** a structural fact. It is documented as **prose** in
the leaf and **never imported** into the midbrain structural
layer. Dependency DAG unchanged: ``chemicals_hormones → memory →
brainparts``. **The RLi does NOT have a significant dopaminergic
subpopulation** (unlike its caudal sibling, the **CLi** — which
has an A10 dopaminergic subset). **The serotonergic phenotype is
the RLi's principal transmitter identity.** Consumers must **not**
import the **serotonergic** phenotype into the midbrain structural
layer. See *Chemicals-Layer Discipline* and *Design Contract*.
**Boundary status (NEUROMODULATORY NUCLEUS — a NEW structure
class — NOT an oscillator, NOT a premotor pool, NOT a motor
nucleus, NOT a sensory relay, NOT a conduction pathway):**
**Boundary case — the rostral linear nucleus of the raphe is a
NEUROMODULATORY NUCLEUS.** In the family's **structure-class
taxonomy**, it is a **neuromodulatory nucleus** — the **same
class** as the **locus coeruleus** (noradrenergic), the **dorsal
raphe** (serotonergic), the **median raphe** (serotonergic), the
**caudal linear nucleus** (serotonergic + dopaminergic subset),
and the **VTA** (dopaminergic). It is **not** an **oscillator**
(it does not generate a rhythm), **not** a **premotor pool** (it
does not transform motor commands), **not** a **motor nucleus**
(it does not drive muscle), **not** a **sensory relay** (it does
not transduce or relay sensory input), **not** a **sensorimotor
integration** structure (it does not integrate input into a
behavioral command), and **not** a **conduction pathway** (it is
grey matter, not white matter). **It modulates the excitability
of its targets** via **volume transmission** of serotonin — that
is its functional class. **Neuromodulatory nuclei carry NO
coupling warning** — same rule as motor nuclei, premotor pools,
sensor nuclei, relay nuclei, sensorimotor integration structures,
and conduction pathways. Its **midline position** — **not
paired** — is the **structural expression** of its
**modulatory, distributed** function: it **does not have a
left/right pair** because it **modulates both sides**. See
*Lateralization Notes* and *Design Contract*.
**Boundary status (NO COUPLING WARNING — the RLi is a MODULATORY
NUCLEUS):** **Boundary case — the rostral linear nucleus of the
raphe carries NO coupling warning.** The **coupling warning**
attaches to **OSCILLATORS** (the pre-Bötzinger complex, the
Bötzinger complex, the pFRG) — and the **RLi is not an
oscillator**. **It is a midline modulatory nucleus** — a **single
leaf**, **not paired**. **Neuromodulatory nuclei carry NO
coupling warning** — same rule as every non-oscillator class.
**The midline position is not a coupling hazard** — it is the
**structural fact** of a **distributed modulator** that
**reaches both sides** via its **projections**, **not** via
intrinsic left-right coupling (there are no "two sides" to
couple — the RLi is one midline nucleus). Consumers must **not**
import a coupling warning into the RLi.

Overview
--------
The rostral linear nucleus of the raphe (RLi) is a **midline
serotonergic neuromodulatory nucleus** in the **ventral midbrain
tegmentum** — at the level of the **caudal diencephalon / rostral
midbrain**, near the **ventral tegmental area** and the
**interpeduncular fossa** — **rostral and ventral to the caudal
linear nucleus (CLi)**. It is a **small** nucleus — smaller than
the **dorsal raphe nucleus (DR)** — composed **primarily of
serotonergic neurons** — **part of the rostral raphe complex**
(along with the DR, the MnR, and the CLi). **The RLi is the FIRST
ACTUAL CLEANLY-REPRESENTED MIDLINE LEAF IN THE TREE** — the on-disk
path is a **single leaf**
(``tegmentum/rostral_linear_nucleus_raphe/``) with **no `left/` or
`right/` nodes** — **the ACTUAL clean midline case the CLi, the
DR, and the IPN should follow (Resolution B)**, and **the
restoration of the midline category's on-disk evidence** that the
IPN falsification had erased. **The RLi's clean representation
gives the tegmentum container amendment's midline exception
category its clean on-disk example** — **parallel to the diffuse
bilateral category's clean example, the PAG**.

**The RLi is a MIDLINE LEAF — and the FIRST ACTUAL CLEAN ONE in the
tree.** The **CLi**, the **DR**, and the **IPN** are **all
represented as paired** (anomalous — their own `left/` and
`right/` modules flag this); **the IPN was held up as the clean
midline case and was falsified**; **the RLi is actually clean** —
a **single leaf**, as its anatomy demands. **The RLi is the
ACTUAL clean midline case the tree has been looking for** — the
**proof that the tree CAN represent midline nuclei cleanly** that
the IPN could not provide.

**The RLi RESTORES the on-disk evidence for the midline exception
category of the tegmentum container amendment.** The **CLi**, the
**DR**, and the **IPN** are anomalous; the **midline category had
NO clean on-disk example** after the IPN falsification. **The RLi
is actually clean** — **so the midline category now has ONE clean
on-disk example**. **The tegmentum container amendment's TWO
exception categories BOTH now have clean on-disk examples** — the
**midline category: the RLi** **and** the **diffuse bilateral
category: the PAG**.

**The RLi is a NEUROMODULATORY NUCLEUS.** It **modulates the
excitability of its targets** via **volume transmission** of
serotonin. It is **not an oscillator**, **not a premotor pool**,
**not a motor nucleus**, **not a sensory relay**, **not a
sensorimotor integration** structure, and **not a conduction
pathway**. **Neuromodulatory nuclei carry NO coupling warning** —
same rule as every non-oscillator class.

**The RLi is NOT a CN nucleus.** It is a **serotonergic
neuromodulatory nucleus** — it is **not** cross-listed with
``cranial_nerve_nuclei/``. It has **one path only**.

The First Actual Clean Midline Leaf
-----------------------------------
**The RLi is the FIRST ACTUAL CLEANLY-REPRESENTED MIDLINE LEAF in
the tree.** The on-disk path is
``tegmentum/rostral_linear_nucleus_raphe/`` — a **single leaf** —
**no `left/` or `right/`** — and this is the **anatomically correct
representation** for a midline nucleus.

**The CLi, the DR, and the IPN are all represented as paired** —
anomalous:

*   **CLi** (``.../tegmentum/caudal_linear_nucleus/``) — **midline**
    serotonergic/dopaminergic nucleus, **represented as paired**
    (``.../caudal_linear_nucleus/left/`` and
    ``.../caudal_linear_nucleus/right/``). Its own leaf, its
    `left/` module, and its `right/` module all flag the anomaly
    and recommend **Resolution B**.

*   **DR** (``.../tegmentum/dorsal_raphe_nucleus/``) — **midline**
    serotonergic nucleus, **represented as paired**
    (``.../dorsal_raphe_nucleus/left/`` and
    ``.../dorsal_raphe_nucleus/right/``). Its own leaf
    **assumed a clean representation** and was **falsified**;
    its `left/` and `right/` modules flag the
    **falsified-assumption** and recommend **Resolution B**.

*   **IPN** (``.../tegmentum/interpeduncular_nucleus/``) —
    **midline** GABAergic limbic relay — was **held up as the
    clean midline case** and was **falsified**; its own `left/`
    and `right/` modules flag the **falsified-proof-case** and
    recommend **Resolution B**.

**The RLi is actually clean.** It is **what the IPN claimed to be
but was not** — an **existing, on-disk, single-leaf, midline
nucleus** directly under ``tegmentum/``. **The RLi is the ACTUAL
clean midline case** — **the case the CLi, the DR, and the IPN
should follow (Resolution B)**. **The RLi path is the model that
the CLi, DR, and IPN's paths should follow** — **remove the
`left/` and `right/` nodes; all three become clean midline
leaves, like the RLi**.

**The RLi's clean representation RESTORES the on-disk evidence for
the midline exception category of the tegmentum container
amendment** — **the evidence the IPN falsification had erased**.
**The midline category now has ONE clean on-disk example: the
RLi** — **parallel to the diffuse bilateral category's clean
example: the PAG**. **The tegmentum container amendment's TWO
exception categories BOTH now have clean on-disk examples** —
**even though the CLi, the DR, the IPN, and the MRF remain
anomalous (paired representations) and the joint Resolution B is
still needed for them**.

The Midline Category Restored
-----------------------------
**The RLi restores the on-disk evidence for the midline exception
category of the tegmentum container amendment.** The IPN
falsification had left the midline category with **no clean
on-disk example** — every midline nucleus (CLi, DR, IPN) was
represented as paired. **The RLi is actually clean** — **so the
midline category now has ONE clean on-disk example**.

**The tegmentum container amendment's THREE patterns — ALL now
evidenced by clean on-disk examples:**

*   **Paired structure-container pattern** — the **red nucleus**
    (``.../tegmentum/red_nucleus/`` — a structure container with
    **substantive paired leaves**) and the **riMLF**
    (``.../tegmentum/rostral_interstitial_nucleus_mlf/`` — a
    structure container with **substantive paired leaves**).
    **Both are clean on-disk examples** — the tree represents
    them as structure containers with `left/` and `right/`
    children, **and this is the anatomically correct
    representation** for a paired structure.

*   **Midline leaf pattern** — the **RLi** (this module) — a
    **single midline leaf**, correctly represented. **ONE clean
    on-disk example.**

*   **Diffuse bilateral leaf pattern** — the **PAG**
    (``.../tegmentum/periaqueductal_gray/``) — a **single diffuse
    bilateral leaf**, correctly represented. **ONE clean on-disk
    example.** (The **MRF** — the other diffuse bilateral
    region — is anomalous, but **the PAG alone provides a clean
    on-disk example for the diffuse bilateral category**.)

**The tegmentum container amendment's evidence base is now
COMPLETE** — **all three patterns have clean on-disk examples**:
*   **Paired structure containers** — the **red nucleus**, the
    **riMLF**
*   **Midline leaves** — the **RLi**
*   **Diffuse bilateral leaves** — the **PAG**

**The CLi, the DR, the IPN, and the MRF remain anomalous** — **the
joint Resolution B is still needed for them** — **but the
categories the amendment addresses are ALL now evidenced by
clean on-disk examples**. **The tegmentum container amendment can
now rest on concrete, existing, on-disk evidence for all three
patterns** — not on the anatomy alone. **The amendment should
acknowledge the three patterns** — **paired structure containers,
midline leaves, diffuse bilateral leaves** — **and cite the
red nucleus, the riMLF, the RLi, and the PAG as the clean on-disk
examples**.

**The joint Resolution B for the CLi, the DR, and the IPN is still
needed** — **the three midline nuclei remain anomalous** — **but
the RLi and the PAG provide the clean on-disk examples that show
the tree CAN represent midline and diffuse bilateral structures
cleanly**. **The RLi is the actual clean midline case the CLi,
the DR, and the IPN should follow** (Resolution B); **the PAG is
the actual clean diffuse bilateral case the MRF should follow**
(the MRF's own clean-case claim was falsified — **the PAG
provides the clean case the MRF could not**).

The Rostral Raphe Complex (the family context)
----------------------------------------------
The **rostral linear nucleus of the raphe** is part of the **rostral
raphe complex** — the **ascending serotonergic system** of the
midbrain and rostral pons. The complex contains:

*   **Dorsal raphe nucleus (DR)**
    (``.../tegmentum/dorsal_raphe_nucleus/``) — the **largest**
    serotonergic nucleus — **mood, anxiety, sleep, appetite,
    cognition** — **primary target of SSRI pharmacology**.

*   **Median raphe nucleus (MnR)**
    (``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) —
    a **major** serotonergic nucleus — **pons** — the **primary
    serotonergic projection to the hippocampus** — **mood,
    anxiety, memory**.

*   **Caudal linear nucleus (CLi)**
    (``.../tegmentum/caudal_linear_nucleus/``) — a **smaller**
    serotonergic **and** dopaminergic nucleus — **more caudal**,
    **more ventral** — **ascending modulation, smaller
    contributor**.

*   **Rostral linear nucleus of the raphe (RLi)** — **THIS
    MODULE** — a **smaller** serotonergic nucleus — **more
    rostral**, **more ventral** — **ascending modulation,
    smaller contributor**. **The RLi does NOT have a
    significant dopaminergic subpopulation** (unlike the CLi).

**The RLi is a smaller, rostral contributor** to the **ascending
serotonergic system** — **one node** in the **rostral raphe
complex** — **not the primary serotonergic nucleus** in any
clinical syndrome. **The DR is the primary**; the **MnR** is a
**major** serotonergic nucleus; the **CLi** and the **RLi** are
**smaller contributors**. **The RLi is the SMALLEST of the four**
— the most rostral and ventral.

**The RLi is NOT the DR and NOT the MnR** — the **primary** and
**major** serotonergic nuclei are the **DR** (the largest) and the
**MnR** (the pontine major raphe). **The CLi and the RLi are the
smaller linear nuclei** — **sibling linear nuclei at different
rostrocaudal levels** (the **CLi is caudal**; the **RLi is
rostral**). **The RLi is the ROSTRAL sibling** — **the most
rostral of the four** — **smaller and more ventral than the
DR**, **more rostral and more dorsal than the CLi**.

Function in the Human Brain
---------------------------
The rostral linear nucleus of the raphe's function is
**serotonergic neuromodulation** — a **smaller contributor** to
the **ascending serotonergic system** — **NOT** a sensory relay,
**NOT** a motor nucleus, **NOT** a premotor pool, **NOT** a
sensorimotor integration structure, **NOT** a conduction pathway:

*   **Ascending Serotonergic Modulation (the RLi's primary
    function):** The RLi's **serotonergic neurons** project to the
    **midbrain** and the **diencephalon** — contributing to the
    **ascending serotonergic system** — **modulating** the
    **excitability** of its targets. **The RLi is a SMALLER
    contributor** — **the DR is the primary serotonergic
    nucleus**; the **MnR is the pontine major raphe**; the **CLi
    and the RLi are the smaller linear nuclei**.

*   **The RLi is NOT the primary serotonergic substrate for any
    clinical syndrome.** The **DR** is the **primary** — **mood,
    anxiety, sleep, appetite, cognition**; the **MnR** is the
    **pontine major raphe** — **hippocampal serotonergic
    projection**. **The RLi is a smaller contributor** — **its
    clinical associations are indirect** and **shared with the
    larger nuclei**.

*   **NOT a sensory relay.** The RLi does **not** transduce or
    relay a specific sensory modality.

*   **NOT a modulatory nucleus in the sense of being the primary
    neuromodulatory nucleus.** The RLi **is** a **neuromodulatory
    nucleus** (it broadcasts serotonin via volume transmission) —
    but it is a **smaller** one — **the DR is the primary**.

*   **NOT a motor nucleus.** The RLi does **not** drive muscle.

*   **NOT a premotor pool.** The RLi does **not** transform motor
    commands.

*   **NOT a sensorimotor integration structure.** The RLi does
    **not** integrate sensory input into a behavioral command.

*   **NOT a conduction pathway.** The RLi is **grey matter** — a
    nucleus — **not white matter**.

*   **NOT an oscillator.** The RLi is a **modulatory nucleus** —
    it does **not** generate a rhythm. **Neuromodulatory nuclei
    carry NO coupling warning** — same rule as every non-oscillator
    class.

**The unifying theme:** the RLi is a **smaller serotonergic
neuromodulatory nucleus** in the **ventral midbrain tegmentum** —
a **contributor** to the **ascending serotonergic system** —
**one node** in the **rostral raphe complex**. It is a **midline
leaf** — **the FIRST ACTUAL CLEANLY-REPRESENTED MIDLINE LEAF in
the tree** — **the actual clean midline case the CLi, the DR, and
the IPN should follow** (Resolution B), and **the restoration of
the midline category's on-disk evidence**. It carries **NO
coupling warning** — same rule as every non-oscillator class.

Associated Disorders
--------------------
The rostral linear nucleus of the raphe has **no named syndrome of
its own** — its clinical associations are **indirect**, via its
**distributed serotonergic projections** — and they are **shared
with the larger serotonergic nuclei** (the **DR**, the **MnR**,
the **CLi**), which are the **primary** clinical substrates in
each case:

*   **Mood Disorders (INDIRECT — the DR and MnR are the primary
    serotonergic substrates):** **Major depressive disorder**,
    **anxiety disorders**, **obsessive-compulsive disorder**, and
    **panic disorder** are **associated** with **dysregulation of
    the serotonergic system** — the **DR** (cortical and limbic
    projections) and the **MnR** (hippocampal and septal
    projections) are the **primary** nuclei in each case. **The
    RLi is a SMALLER contributor** — **one node** in the
    **serotonergic system**. **SSRIs** act on the **whole
    serotonergic system** — **not on the RLi specifically**.

*   **Addiction (INDIRECT — the VTA is the primary dopaminergic
    substrate):** **Substance use disorders** are **associated**
    with **dysregulation of the mesolimbic / mesocortical
    dopaminergic system** — the **VTA** (the primary dopaminergic
    nucleus of the reward system) is the **primary** substrate.
    **The RLi's serotonergic projections are a SMALLER
    contributor** — the **CLi's dopaminergic subset** is closer
    to the A10 dopaminergic group; **the RLi is primarily
    serotonergic**.

*   **Sleep and Circadian Regulation (INDIRECT — the DR and MnR
    are the primary serotonergic substrates):** **Serotonin**
    **modulates sleep** — the **DR** (dorsal raphe) and the
    **MnR** (median raphe) are the **primary** serotonergic
    nuclei in sleep regulation. **The RLi is a SMALLER
    contributor.**

*   **Pain Modulation (NOT the RLi — the RAPHE MAGNUS is the
    primary substrate):** **Descending pain modulation** is
    mediated by the **raphe magnus** (medulla) — the **key
    descending serotonergic nucleus** — and the **PAG**. **The
    RLi is an ASCENDING nucleus** — it does **not** participate
    in **descending pain modulation**.

*   **No Named "Rostral Linear Nucleus Syndrome":** The RLi is a
    **small serotonergic modulatory nucleus** — its **isolated
    lesion** produces **no named clinical syndrome**. Its
    clinical relevance is **indirect**, via its **distributed
    serotonergic projections** — and the **primary** clinical
    substrates are the **DR**, the **MnR**, and the **CLi**, not
    the **RLi**. **No named RLi syndrome exists.**

**What is NOT here:** The RLi is **not** the substrate for **major
depressive disorder** (the **DR** and the **MnR** are the primary
serotonergic substrates — **NOT** the RLi), **anxiety disorders**
(the **DR** and the **MnR** — **NOT** the RLi), **obsessive-
compulsive disorder** (the **DR** and the **cortico-striatal
circuits** — **NOT** the RLi), **schizophrenia** (a complex
polygenic disorder — **NOT** any single nucleus), **addiction**
(the **VTA** is the primary dopaminergic node — **NOT** the RLi),
**Parkinson's disease** (the **substantia nigra pars compacta** —
**NOT** the RLi), **sleep disorders** (the **DR** and the
**MnR** — **NOT** the RLi), **descending pain modulation**
(the **raphe magnus** and the **PAG** — **NOT** the RLi),
**saccade disorders** (the **SC**, the **SNr**, the **riMLF** —
**NOT** the RLi), **pupillary light reflex deficits** (the
**pretectum** and the **EW nucleus** — **NOT** the RLi),
**oculomotor palsy** (the **CN III nucleus** — **NOT** the RLi),
**trochlear palsy** (the **CN IV nucleus** — **NOT** the RLi),
**trigeminal sensory deficits** (the **trigeminal ganglion**, the
**main sensory**, and the **spinal trigeminal nucleus** — **NOT**
the RLi), **CCHS** (RTN), **OIRD** (pre-Bötzinger complex —
NK1R neurons), **Rett syndrome** (pre-Bötzinger complex),
**SIDS** (proposed — pre-Bötzinger complex + arcuate nucleus),
**essential hypertension / sympathetic overactivity** (C1 group /
RVLM), **Huntington's disease** (striatum — telencephalon), or
**Kluver-Bucy syndrome** (amygdala). Its clinical relevance is
**indirect**, via its **distributed serotonergic projections** —
the **DR**, the **MnR**, and the **CLi** are the **primary**
substrates. **No named RLi syndrome exists.**

Lateralization Notes
--------------------
This is the **rostral linear nucleus of the raphe** leaf — the
**FIRST ACTUAL CLEANLY-REPRESENTED MIDLINE LEAF in the tree**.
The RLi is **midline**, **not paired** — it has **no left/right
pair** and **no mirror leaf**. **The tree represents it CLEANLY**
— one midline leaf under ``tegmentum/``, **no `left/` or
`right/` nodes**. **This is the ACTUAL clean midline case the
CLi, the DR, and the IPN should follow** (Resolution B). **No
coupling warning** — the same rule as every non-oscillator
class.

*   **Midline Nucleus — NOT Paired:** The RLi is a **single
    midline leaf** directly under ``tegmentum/`` — **NOT** under
    ``tegmentum/left/`` or ``tegmentum/right/``. It has **no
    left/right pair**, **no mirror leaf**, **no bilateral
    iteration**.

*   **Cleanly Represented in the Tree — the FIRST ACTUAL Clean
    Midline Leaf:** The RLi is the **FIRST ACTUAL
    cleanly-represented midline leaf** in the tree — the tree
    represents it **exactly as its anatomy demands**: one
    midline nucleus, one leaf. **The CLi, the DR, and the IPN
    are all represented as paired** — anomalous — so **the RLi
    is the FIRST ACTUAL clean midline leaf in the tree**. **This
    is the case the CLi, the DR, and the IPN should follow**
    (Resolution B — remove their `left/` and `right/` nodes).
    **The tree CAN do midline cleanly** — **the RLi is the
    proof** — **the actual proof the IPN could not provide**.

*   **Midline Category Restored:** The RLi's clean representation
    **restores the on-disk evidence for the midline exception
    category** of the tegmentum container amendment — **the
    evidence the IPN falsification had erased**. **The midline
    category now has ONE clean on-disk example: the RLi** —
    **parallel to the diffuse bilateral category's clean
    example: the PAG**.

*   **Midline Position = Modulatory Function:** The RLi is a
    **serotonergic neuromodulator** — it **modulates both
    sides** via its **distributed projections**, **not** via
    intrinsic left-right coupling. **The midline position is
    the structural fact** — a **distributed modulator** has a
    **midline nucleus** whose projections **fan out
    bilaterally** to its targets on both sides.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to MODULATORY NUCLEI):** The
    **pre-Bötzinger complex** carries a **coupling warning**
    because it is an **oscillator** whose two sides must
    synchronize to produce a single rhythm. The **RLi** is a
    **modulatory nucleus** — a **single midline leaf** — it
    does **not** generate a rhythm, so it does **not** carry
    the **oscillator coupling warning**. There are **no "two
    sides" to couple** — the RLi is **one midline nucleus**
    whose **distributed projections** carry its modulation to
    **both sides**. **Neuromodulatory nuclei carry NO coupling
    warning** — same rule as every non-oscillator class.

*   **No SLEA Warning:** The RLi is **SLEA-free** — it is **not**
    an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The RLi is **not**
    part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The RLi is **not** a
    rhinencephalon structure.

**The RLi is the FIRST ACTUAL CLEAN midline leaf in the tree** —
its **midline position**, **neuromodulatory class**, **clean
representation in the tree**, and **no coupling warning**
establish the **canonical structural pattern** for midline
modulatory nuclei. **The CLi, the DR, and the IPN are the
anomalous cases** — the tree represents them with `left/` and
`right/` nodes, which their own modules flag as
**tree-structural anomalies**. **The tree should be amended so
that the CLi, the DR, and the IPN follow the RLi's clean
pattern** (Resolution B). See *The First Actual Clean Midline
Leaf* and *The Midline Category Restored*.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The RLi is **midline** —
    there is **no** other hemisphere to import from.
*   **No cross-lobe imports.** This module does **not** import from
    the **PAG**, the **VTA**, the **substantia nigra**, the
    **caudal linear nucleus**, the **dorsal raphe**, the **median
    raphe**, the **medullary raphe nuclei**, the **locus
    coeruleus**, the **cerebral aqueduct**, or any other
    container. The RLi's relationships to the PAG, the VTA, the
    substantia nigra, the CLi, the DR, the MnR, the medullary
    raphe nuclei, the locus coeruleus, and the cerebral aqueduct
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **serotonergic phenotype** (tryptophan hydroxylase, 5-HT
    synthesis, serotonin transporters, serotonin receptors) is a
    **``chemicals_hormones``-layer fact** — documented as
    **prose**, **never imported**. **CHEMICALS-LAYER DISCIPLINE**
    is preserved. **The RLi does NOT have a significant
    dopaminergic subpopulation** — **the serotonergic phenotype
    is the RLi's principal transmitter identity** (unlike the
    CLi, which has both).
*   **MIDLINE LEAF — the FIRST ACTUAL CLEAN ONE in the tree.**
    The RLi is a **single leaf** directly under ``tegmentum/`` —
    **NO** ``tegmentum/rostral_linear_nucleus_raphe/left/`` and
    **NO** ``tegmentum/rostral_linear_nucleus_raphe/right/``.
    **This is the FIRST ACTUAL cleanly-represented midline leaf
    in the tree** — the tree represents the RLi **exactly as
    its anatomy demands**. **The RLi path is the model that the
    CLi's, the DR's, and the IPN's paths should follow**
    (Resolution B — removing their `left/` and `right/` nodes).
*   **THE FIRST ACTUAL CLEAN MIDLINE LEAF — the case the CLi,
    DR, and IPN should follow.** The **CLi**, the **DR**, and
    the **IPN** are **all represented as paired** (anomalous);
    the **IPN was held up as the clean midline case and was
    falsified**. **The RLi is actually clean** — the **ACTUAL
    clean midline case the tree has been looking for** — **the
    case the CLi, the DR, and the IPN should follow**
    (Resolution B).
*   **MIDLINE CATEGORY RESTORED — the tegmentum container
    amendment's midline exception category now has on-disk
    evidence.** The **RLi** is the **actual clean midline case**
    — the **restoration of the midline category's on-disk
    evidence** the IPN falsification had erased. **The midline
    category now has ONE clean on-disk example: the RLi** —
    **parallel to the diffuse bilateral category's clean
    example: the PAG**. **The tegmentum container amendment's
    evidence base is now COMPLETE** — **all three patterns
    have clean on-disk examples** (paired structure containers:
    the red nucleus, the riMLF; midline leaves: the RLi;
    diffuse bilateral leaves: the PAG).
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER — now FULLY
    EVIDENCED.** The tegmentum container's **paired-leaf rule**
    — *"each tegmentum nucleus is a paired structure (a
    ``left/`` leaf and a ``right/`` leaf)"* — should be
    **AMENDED** to acknowledge **THREE patterns**:
    *   **Paired structure containers** (the **red nucleus**,
        the **riMLF** — substantive paired leaves).
    *   **Midline leaves** (the **RLi** — the **actual clean
        on-disk example**; and the **CLi**, **DR**, **IPN** —
        **pending the joint Resolution B**).
    *   **Diffuse bilateral leaves** (the **PAG** — the
        **actual clean on-disk example**; and the **MRF** —
        **pending Resolution B**).
    **The amendment's evidence base is now COMPLETE** — **all
    three patterns have clean on-disk examples** — **the red
    nucleus and the riMLF for paired structure containers**,
    **the RLi for midline leaves**, and **the PAG for diffuse
    bilateral leaves**. **The amendment no longer rests on
    anatomy alone** — **it has clean on-disk evidence for all
    three patterns**.
*   **JOINT RESOLUTION B STILL NEEDED.** The **CLi**, the
    **DR**, the **IPN**, and the **MRF** remain **anomalous**
    — **the joint Resolution B is still needed for them**. **The
    RLi and the PAG provide the clean on-disk examples that
    show the tree CAN represent midline and diffuse bilateral
    structures cleanly** — **the joint Resolution B for the CLi,
    DR, IPN, and MRF is now supported by on-disk evidence,
    not just anatomy**.
*   **NEUROMODULATORY NUCLEUS — the same class as the DR, the
    CLi, the MnR, and the LC.** The RLi is a **neuromodulatory
    nucleus** — it **modulates the excitability of its targets**
    via **volume transmission** of serotonin. It is **NOT** an
    oscillator, **NOT** a premotor pool, **NOT** a motor
    nucleus, **NOT** a sensory relay, **NOT** a sensorimotor
    integration structure, and **NOT** a conduction pathway.
*   **NO COUPLING WARNING — neuromodulatory nuclei carry NO
    coupling warning.** The RLi is a **single midline leaf** —
    a **midline modulatory nucleus** — it does **not** generate
    a rhythm. **The midline position is not a coupling
    hazard** — it is the structural fact of a **distributed
    modulator** that **reaches both sides** via its
    **projections**, not via intrinsic left-right coupling
    (there are no "two sides" to couple).
*   **NOT A CN NUCLEUS.** The RLi is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. It has **one path only**.
*   **NOT the CLi — the CLi is the CAUDAL sibling linear
    nucleus.** The CLi has a **dopaminergic subpopulation** (A10
    group) the RLi does not. The CLi is anomalous paired; the
    RLi is actually clean.
*   **NOT the DR — the DR is the LARGEST serotonergic nucleus.**
    The DR is the **primary** serotonergic substrate for mood
    disorders; the RLi is a **smaller contributor**. The DR is
    anomalous paired; the RLi is actually clean.
*   **NOT the MnR — the MnR is a PONTINE raphe nucleus.**
*   **NOT the VTA or the SN — those are PAIRED dopaminergic
    nuclei.** The RLi is **midline and primarily serotonergic**.
*   **NOT the PAG — the PAG is a DIFFUSE BILATERAL region.** The
    RLi is a **midline nucleus**.
*   **NOT the MRF — the MRF is a DIFFUSE BILATERAL reticular
    region.** The RLi is a **midline nucleus**.
*   **NOT the IPN — the IPN is a MIDLINE GABAergic limbic
    relay.** The RLi is a **midline serotonergic neuromodulatory
    nucleus** — **different transmitter class, different
    functional system**.
*   **NOT the red nucleus or the riMLF — those are PAIRED
    premotor relays.** The RLi is a **midline neuromodulatory
    nucleus**.
*   **CHEMICALS-LAYER DISCIPLINE.** The **serotonergic
    phenotype** is a **``chemicals_hormones``-layer fact** —
    documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The RLi is a
    **local midline leaf** under the tegmentum — no
    cross-listing.
*   **No nested cross-listing.** The RLi is a **single leaf**.
    It is **not** a container.
*   **The on-disk tree is authoritative.** The on-disk tree has
    ``.../tegmentum/rostral_linear_nucleus_raphe/`` — **one
    leaf**, **midline**, **no `left/` or `right/`**. **This is
    the correct representation** — the RLi is a midline
    nucleus, and the tree represents it cleanly. **The RLi
    path is the model that the CLi's, DR's, and IPN's paths
    should follow** (Resolution B).

Usage
-----
Resolve the leaf by path (**one** path only — the RLi is
**midline**, **not** under `left/` or `right/`)::

    from infrastructure.brainparts.midbrain.tegmentum import rostral_linear_nucleus_raphe

Or by fully-qualified path string::

    path = "midbrain.tegmentum.rostral_linear_nucleus_raphe"

**Do not** assume the RLi is under
``tegmentum/rostral_linear_nucleus_raphe/left/`` or
``tegmentum/rostral_linear_nucleus_raphe/right/``. **It is
MIDLINE** — a **single leaf** directly under ``tegmentum/``. **The
tree represents it cleanly.** **The RLi is the FIRST ACTUAL
cleanly-represented midline leaf in the tree** — **the actual
clean midline case the CLi, the DR, and the IPN should follow**
(Resolution B). **The RLi path is the model that their paths
should follow.**

**Do not** assume the RLi is a **cranial nerve nucleus**. It is
**not** a CN nucleus and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the RLi is the **caudal linear nucleus**. The
**CLi** is the **caudal** sibling linear nucleus — **more
caudal**, **more ventral**, **with a dopaminergic subpopulation
(A10 group)** the RLi does not have. **The RLi is the ROSTRAL
sibling** — **more rostral**, **more dorsal**, **primarily
serotonergic** — **the RLi does NOT have a significant
dopaminergic subpopulation**.

**Do not** assume the RLi is the **dorsal raphe nucleus**. The
**DR** is the **largest serotonergic nucleus in the brain** —
the **primary** serotonergic substrate for mood disorders; the
**RLi is a smaller contributor**.

**Do not** assume the RLi is the **median raphe nucleus**. The
**MnR** is a **pons** structure.

**Do not** assume the RLi is the **VTA** or the **substantia
nigra**. Those are **PAIRED dopaminergic nuclei** — **the RLi is
midline and primarily serotonergic**.

**Do not** assume the RLi is the **PAG** or the **MRF**. Those are
**diffuse bilateral regions** — **the RLi is a midline nucleus**.

**Do not** assume the RLi is the **IPN**. The **IPN** is a
**midline GABAergic limbic relay** — **the RLi is a midline
serotonergic neuromodulatory nucleus**.

**Do not** assume the RLi is the **red nucleus** or the
**riMLF**. Those are **paired premotor relays** — **the RLi is a
midline neuromodulatory nucleus**.

**Do not** import the **serotonergic phenotype** into the
midbrain structural layer. It is a
**``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the RLi.
**Neuromodulatory nuclei carry NO coupling warning** — same rule
as every non-oscillator class.

**Do not** treat the RLi as a **paired structure**. It is a
**midline nucleus** — a **single leaf** — with **no left/right
pair** and **no mirror leaf**. **The tree represents it
cleanly** — **the FIRST ACTUAL clean midline leaf in the tree**.

Iterating the rostral linear nucleus of the raphe's (empty)
children (recommended consumer pattern)::

    ROSTRAL_LINEAR_NUCLEUS_RAPHE_CHILDREN = ()
    # The RLi is a leaf. The serotonergic neuron population IS the
    # nucleus (the RLi has no classical subnuclear organization,
    # unlike the DR). The serotonergic neurons are prose, not
    # modules.

Bilateral iteration — **NOT APPLICABLE**::

    # The RLi is MIDLINE — it has NO left/right pair. There is no
    # bilateral iteration for the RLi. If you find yourself
    # writing:
    #
    #     for side in ("left", "right"):
    #         path = f"midbrain.tegmentum.{side}.rostral_linear_nucleus_raphe"
    #
    # — that is WRONG. The RLi is at:
    #
    #     midbrain.tegmentum.rostral_linear_nucleus_raphe
    #
    # — a single midline leaf. The tree represents the RLi
    # correctly — the FIRST ACTUAL clean midline leaf in the tree.

Reaching the caudal linear nucleus (recommended consumer pattern —
the CAUDAL sibling linear nucleus)::

    # The caudal linear nucleus (CLi) is the SIBLING LINEAR NUCLEUS
    # — more caudal, more ventral, with a dopaminergic
    # subpopulation (A10 group):
    #
    #   brainparts.midbrain.tegmentum.caudal_linear_nucleus
    #
    # NOTE: the CLi's tree representation is ANOMALOUS — it has
    # left/ and right/ nodes (see the CLi's own left/ and right/
    # modules). The RLi is the ACTUAL clean midline case; the CLi
    # is the ANOMALOUS case. The tree should be amended so that
    # the CLi follows the RLi's clean pattern (Resolution B —
    # remove the left/ and right/ nodes).

Reaching the dorsal raphe nucleus (recommended consumer pattern —
the LARGEST serotonergic nucleus, a sibling midline raphe)::

    # The dorsal raphe nucleus (DR) is the LARGEST serotonergic
    # nucleus in the brain — the primary serotonergic nucleus of
    # the forebrain:
    #
    #   brainparts.midbrain.tegmentum.dorsal_raphe_nucleus
    #
    # NOTE: the DR's tree representation is ANOMALOUS — it has
    # left/ and right/ nodes (the DR leaf's clean-case framing
    # was falsified). The RLi is the ACTUAL clean midline case;
    # the DR is the ANOMALOUS case. The tree should be amended so
    # that the DR follows the RLi's clean pattern (Resolution B).

Reaching the median raphe nucleus (recommended consumer pattern —
the PONTINE major raphe)::

    # The median raphe nucleus (MnR) is a PONS structure — the
    # pontine median raphe:
    #
    #   brainparts.hindbrain.metencephalon.pons.median_raphe_nucleus
    #
    # The MnR is PONS; the RLi is MIDBRAIN.

Reaching the PAG (recommended consumer pattern — the clean
diffuse bilateral example)::

    # The periaqueductal gray (PAG) is the CLEAN DIFFUSE BILATERAL
    # example — a single diffuse bilateral leaf — the clean case
    # for the diffuse bilateral category, parallel to the RLi as
    # the clean case for the midline category:
    #
    #   brainparts.midbrain.tegmentum.periaqueductal_gray
    #
    # The RLi (midline) and the PAG (diffuse bilateral) are BOTH
    # cleanly represented — the tegmentum container amendment's
    # TWO exception categories now have clean on-disk examples.

Reaching the red nucleus or the riMLF (recommended consumer
pattern — the paired structure containers)::

    # The red nucleus and the riMLF are the PAIRED STRUCTURE
    # CONTAINERS — the clean case for the paired
    # structure-container pattern:
    #
    #   brainparts.midbrain.tegmentum.red_nucleus
    #   brainparts.midbrain.tegmentum.rostral_interstitial_nucleus_mlf
    #
    # The tegmentum container amendment's THREE patterns — paired
    # structure containers (red nucleus, riMLF), midline leaves
    # (RLi), diffuse bilateral leaves (PAG) — ALL now have clean
    # on-disk examples.

Reaching the VTA or the substantia nigra (recommended consumer
pattern — the PAIRED dopaminergic nuclei)::

    # The ventral tegmental area (VTA) and the substantia nigra
    # (SN) are PAIRED dopaminergic nuclei:
    #
    #   brainparts.midbrain.tegmentum.left.ventral_tegmental_area
    #   brainparts.midbrain.tegmentum.right.ventral_tegmental_area
    #   brainparts.midbrain.tegmentum.left.substantia_nigra
    #   brainparts.midbrain.tegmentum.right.substantia_nigra
    #
    # The VTA and the SN are PAIRED; the RLi is MIDLINE. The VTA
    # and the SN are primarily DOPAMINERGIC; the RLi is
    # primarily SEROTONERGIC.

Reaching the IPN (recommended consumer pattern — the MIDLINE
GABAergic limbic relay)::

    # The interpeduncular nucleus (IPN) is a MIDLINE GABAergic
    # limbic relay — the principal downstream relay of the
    # habenula:
    #
    #   brainparts.midbrain.tegmentum.interpeduncular_nucleus
    #
    # NOTE: the IPN was held up as the clean midline case and was
    # FALSIFIED — its own left/ and right/ nodes contradict its
    # clean-case claim. The RLi is the ACTUAL clean midline case;
    # the IPN is the ANOMALOUS case. The tree should be amended so
    # that the IPN follows the RLi's clean pattern (Resolution B).

The rostral raphe complex — detail (not wired — consult
references)::

    # The rostral linear nucleus of the raphe is part of the
    # ROSTRAL RAPHE COMPLEX — the ASCENDING serotonergic system:
    #
    #   dorsal raphe nucleus (DR)       -> LARGEST; forebrain,
    #                                       limbic, striatum,
    #                                       thalamus — mood,
    #                                       anxiety, sleep, appetite,
    #                                       cognition — PRIMARY
    #                                       target of SSRIs
    #   median raphe nucleus (MnR)      -> PONS; hippocampus, septum,
    #                                       hypothalamus — mood,
    #                                       anxiety, memory
    #   caudal linear nucleus (CLi)     -> SMALLER; forebrain,
    #                                       diencephalon, limbic —
    #                                       serotonergic AND
    #                                       dopaminergic (A10 group)
    #   rostral linear nucleus (RLi)    -> SMALLEST; more rostral,
    #                                       more dorsal — serotonergic
    #                                       (NO dopaminergic subset)
    #
    # The RLi is the SMALLEST of the four — the most rostral and
    # dorsal. It is PRIMARILY SEROTONERGIC — it does NOT have a
    # significant dopaminergic subpopulation (unlike the CLi).
    #
    # Do not attempt to resolve the DR, the MnR, the CLi, or the
    # medullary raphe nuclei as sub-paths of the RLi — they are
    # DIFFERENT structures at DIFFERENT levels.

The midline category restored — detail (not wired — structural
note)::

    # The RLi RESTORES the on-disk evidence for the midline
    # exception category of the tegmentum container amendment —
    # the evidence the IPN falsification had erased:
    #
    #   THE MIDLINE CATEGORY:
    #     - CLi (anomalous paired — Resolution B pending)
    #     - DR  (anomalous paired — Resolution B pending)
    #     - IPN (anomalous paired — Resolution B pending)
    #     - RLi (ACTUALLY CLEAN — single midline leaf)
    #
    #   THE DIFFUSE BILATERAL CATEGORY:
    #     - MRF (anomalous paired — Resolution B pending)
    #     - PAG (ACTUALLY CLEAN — single diffuse bilateral leaf)
    #
    #   THE PAIRED STRUCTURE-CONTAINER PATTERN:
    #     - red nucleus (clean structure container — paired
    #       substantive leaves)
    #     - riMLF (clean structure container — paired substantive
    #       leaves)
    #
    # ALL THREE patterns the tegmentum container amendment
    # addresses NOW have clean on-disk examples: the RLi
    # (midline), the PAG (diffuse bilateral), the red nucleus and
    # riMLF (paired structure containers).
    #
    # The joint Resolution B for the CLi, the DR, the IPN, and
    # the MRF is still needed — the four anomalous cases — but
    # the RLi and the PAG provide the clean on-disk examples
    # that show the tree CAN represent midline and diffuse
    # bilateral structures cleanly. The tegmentum container
    # amendment can now rest on concrete, existing, on-disk
    # evidence for all three patterns — not on anatomy alone.

Clinical-pattern detail (not wired — consult references)::

    # The RLi has NO NAMED SYNDROME OF ITS OWN — its clinical
    # associations are INDIRECT — shared with the LARGER
    # serotonergic nuclei:
    #
    #   MOOD DISORDERS              -> the DR and MnR are the
    #     (depression, anxiety,        primary serotonergic
    #      OCD)                        substrates — the RLi is a
    #                                   SMALLER contributor; SSRIs
    #                                   act on the WHOLE serotonergic
    #                                   system
    #   ADDICTION                   -> the VTA is the primary
    #                                   dopaminergic substrate — the
    #                                   RLi's serotonergic projections
    #                                   are a SMALLER contributor
    #   SLEEP / CIRCADIAN           -> the DR and MnR are the
    #                                   primary serotonergic
    #                                   substrates — the RLi is a
    #                                   SMALLER contributor
    #   DESCENDING PAIN MODULATION  -> the RAPHE MAGNUS (medulla)
    #                                   and the PAG are the primary
    #                                   substrates — the RLi is
    #                                   ASCENDING, NOT descending
    #
    # No named "rostral linear nucleus syndrome" exists. The DR,
    # the MnR, and the CLi are the primary clinical substrates —
    # the RLi is a smaller contributor.
    #
    # Do not conflate these patterns — they localize primarily to
    # the DR, the MnR, or the CLi — not to the RLi alone.

References
----------
*   **Canonical raphe anatomy (human):** Hornung, J.P. (2003).
    "The human raphe nuclei and the serotonergic system."
    *Journal of Chemical Neuroanatomy* 26:331–343. (The human
    raphe nuclei — the rostral raphe complex (DR, MnR, CLi,
    RLi); the caudal raphe complex (raphe magnus, pallidus,
    obscurus); the serotonergic cell groups; the ascending and
    descending projections.)
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
    complex — the DR and MnR; the CLi and RLi's ascending
    projections overlap with the rostral raphe complex.)
*   **Rostral linear nucleus — serotonergic cells:** Halliday,
    G.M., Törk, I. (1989). "Serotonin-like immunoreactive cells
    and fibres in the rat ventromedial mesencephalic tegmentum."
    *Brain Research Bulletin* 22:725–735. (The serotonergic cells
    of the ventromedial mesencephalic tegmentum — the RLi as a
    serotonergic nucleus of the rostral raphe complex.)
*   **Rostral linear nucleus — human:** Baker, K.G., Halliday,
    G.M., Hornung, J.P., Geffen, L.B., Cotton, R.G., Törk, I.
    (1991). "Distribution, morphology and number of monoamine-
    synthesizing and substance P-containing neurons in the human
    dorsal raphe nucleus." *Neuroscience* 42:757–775. (The
    monoamine-synthesizing neurons of the human rostral raphe
    complex — the RLi and its serotonergic subpopulations.)
*   **A10 dopaminergic cell group (contrast — the CLi has a
    dopaminergic subset, the RLi does not):** Dahlstroem, A.,
    Fuxe, K. (1964). "Evidence for the existence of
    monoamine-containing neurons in the central nervous system.
    I. Demonstration of monoamines in the cell bodies of brain
    stem neurons." *Acta Physiologica Scandinavica* 62 (Suppl.
    232):1–55. (The A10 dopaminergic cell group — the VTA and
    the CLi's dopaminergic subset; **the RLi is primarily
    serotonergic and does NOT have a significant dopaminergic
    subset**.)
*   **Monoamine cell groups — human:** Hökfelt, T., Johansson,
    O., Goldstein, M. (1984). "Chemical anatomy of the brain."
    *Science* 225:1326–1334. (The monoamine cell groups —
    dopaminergic, noradrenergic, and serotonergic — and their
    brainstem nuclei.)
*   **Raphe nuclei — anatomy:** Törk, I. (1990). "Anatomy of the
    serotonergic system." *Annals of the New York Academy of
    Sciences* 600:9–34. (The anatomy of the serotonergic system
    — the raphe nuclei, the ascending and descending
    projections, the distribution of serotonergic fibers.)
*   **Serotonin receptors — distribution:** Pazos, A., Palacios,
    J.M. (1985). "Quantitative autoradiographic mapping of
    serotonin receptors in the rat brain. I. Serotonin-1
    receptors." *Brain Research* 346:205–230. (The distribution
    of serotonin receptors in the brain — the target fields of
    the ascending serotonergic system.)
*   **Raphe magnus — descending pain modulation (contrast —
    MEDULLARY, NOT the RLi):** Fields, H.L., Basbaum, A.I.
    (1978). "Brainstem control of spinal pain-transmission
    neurons." *Annual Review of Physiology* 40:217–248. (The
    raphe magnus and the descending pain-modulation system —
    contrast with the ascending RLi.)
*   **Dorsal raphe — the primary serotonergic nucleus (contrast —
    SIBLING, NOT the RLi):** Michelsen, K.A., Schmitz, C.,
    Steinbusch, H.W.M. (2007). "The dorsal raphe nucleus — from
    silver stainings to a simplified subnuclear organization:
    review on the mesencephalic raphe nuclei." *Brain Research
    Reviews* 55:349–363. (The dorsal raphe nucleus — the
    primary serotonergic nucleus of the rostral raphe complex —
    contrast with the smaller, more rostral RLi.)
*   **Median raphe — the pontine raphe nucleus (contrast — PONS,
    NOT the RLi):** Vertes, R.P., Crane, A.M. (1997).
    "Distribution, quantification and comparisons of serotonin-
    immunoreactive fibers in brain regions with different
    densities of the serotonin transporter." *Journal of
    Comparative Neurology* 381:293–306. (The median raphe
    nucleus — the pontine raphe nucleus — contrast with the
    midbrain RLi.)
*   **CLi — the caudal sibling linear nucleus (contrast — the
    CLi has a dopaminergic subset):** Halliday, G.M., Törk, I.
    (1989). "Serotonin-like immunoreactive cells and fibres in
    the rat ventromedial mesencephalic tegmentum." *Brain
    Research Bulletin* 22:725–735. (The CLi — the caudal
    sibling linear nucleus, with a dopaminergic subpopulation
    the RLi does not have.)
*   **SLEA (contrast — the RLi is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the rostral linear nucleus of the raphe.)
*   NeuroNames — Rostral linear nucleus of the raphe; FMA —
    Rostral linear nucleus. **The RLi is a single midline
    nucleus — there is no "left rostral linear nucleus" or
    "right rostral linear nucleus" in the standard anatomical
    atlases.**
"""