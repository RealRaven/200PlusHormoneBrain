"""
infrastructure.brainparts.midbrain.tegmentum.interpeduncular_nucleus
===================================================================

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
        └── interpeduncular_nucleus    <-- THIS MODULE (MIDLINE
                                           LEAF — CLEANLY
                                           REPRESENTED — NO left/
                                           or right/ nodes)

**Primary synonym:** Interpeduncular nucleus; **IPN**; **nucleus
interpeduncularis** (Latin); **ganglion interpedunculare** (older
term); the **interpeduncular ganglion** (older term).
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **midline** **GABAergic limbic relay nucleus** in the
**ventral midbrain tegmentum** — in the **interpeduncular fossa**
(the space **between the two cerebral peduncles**) — at the level of
the **caudal midbrain / pontomesencephalic junction**. It is the
**principal downstream relay** of the **habenula** (epithalamus,
dorsal diencephalon) — the **habenula → fasciculus retroflexus →
interpeduncular nucleus** circuit is one of the **best-defined
limbic circuits** in the brain. Its **GABAergic phenotype** (the
principal output transmitter) and its **cholinergic input** from the
medial habenula are **``chemicals_hormones``-layer facts** — see
*Chemicals-Layer Discipline*.
**Container status:** **This module is a LEAF**, **midline** — it
is **NOT** under ``tegmentum/left/`` or ``tegmentum/right/`` — it
sits **directly under** the tegmentum container. **It is the FIRST
GENUINELY CLEANLY-REPRESENTED MIDLINE LEAF IN THE TREE** — the
on-disk tree path is a **single leaf** (``tegmentum/interpeduncular_
nucleus/``) with **no `left/` or `right/` nodes**. **The CLi and
the DR are BOTH represented as paired** (anomalous — see their
``left/`` and ``right/`` modules); **the IPN is represented
cleanly** — **the IPN path is the existing model the CLi and DR
should follow** (Resolution B). See *The Clean Midline Leaf — the
Model the CLi and DR Should Follow*.
**Part of:** The **tegmentum** region container — as a **midline**
leaf. **The IPN is NOT a cranial nerve nucleus** and is **NOT
cross-listed** with ``cranial_nerve_nuclei/`` — see *NOT a CN
Nucleus*.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — **midline**, **not** a side
container.
**Structural children:** **None.** This is a **leaf** module. The
**subnuclear organization** (central, intermediate, dorsal,
lateral, rostral, caudal subnuclei) is documented as **prose**, not
as structural children. The **GABAergic projection neurons** and
the **local-circuit interneurons** are **prose**, not structural
children. **The habenula** (the **input**) and the **fasciculus
retroflexus** (the **conduction pathway**) and the **output targets**
(the raphe, VTA, SN, PAG) are **prose** — **not** structural
children and **not** structural parents.
**Boundary status (MIDLINE LEAF — CLEANLY REPRESENTED — NO left/ or
right/ NODES):** **Boundary case — the interpeduncular nucleus is a
MIDLINE LEAF, and the tree represents it CLEANLY** — **directly
under** ``tegmentum/`` — **NO** ``tegmentum/interpeduncular_
nucleus/left/`` and **NO** ``tegmentum/interpeduncular_nucleus/
right/``. **The IPN is the FIRST GENUINELY CLEANLY-REPRESENTED
MIDLINE LEAF IN THE TREE.** It is a **midline limbic relay
nucleus** — the principal downstream relay of the **habenula** — and
its midline position is the **structural expression** of its
**relay function**: it receives the **habenular input** (from both
the **medial habenula** and the **lateral habenula**, via the
**fasciculus retroflexus**) and sends **GABAergic projections** to
**bilateral targets** (the raphe nuclei, the VTA, the substantia
nigra, the PAG) — it **modulates both sides** via its **distributed
projections**, **not** via intrinsic left-right coupling. **The tree
represents the IPN correctly** — as **one midline leaf** — and the
IPN's clean representation is:
*   **The FIRST GENUINELY CLEAN midline leaf** in the tree — the
    **CLi** and the **DR** are **both represented as paired**
    (anomalous), so the tree has **no other clean midline leaf**
    **besides the IPN**.
*   **The MODEL** the CLi and the DR should follow (Resolution B —
    remove their `left/` and `right/` nodes so they become clean
    midline leaves, like the IPN).
*   **The EVIDENCE** that the tree **can** represent midline nuclei
    cleanly — **the DR leaf claimed this, but the DR itself was
    falsified** (the DR has `left/` and `right/` nodes). **The IPN
    is the actual existing clean case** — the tree **does** do
    midline cleanly, for the IPN.
*   **The PROOF CASE** for the **tegmentum container amendment** —
    midline nuclei **can** be **direct children** of
    ``tegmentum/``, and the IPN is the **existing example**.
Consumers must **not** look for the IPN under
``.../tegmentum/interpeduncular_nucleus/left/`` or
``.../tegmentum/interpeduncular_nucleus/right/`` — **those paths do
not exist**, and if they ever did, they would be **tree-structural
anomalies** of the kind the CLi's and the DR's `left/` and `right/`
modules flag. **The IPN path is the model the CLi and DR should
follow.** See *The Clean Midline Leaf — the Model the CLi and DR
Should Follow*.
**Boundary status (THE CLEAN MIDLINE LEAF — the MODEL the CLi and DR
should follow):** **Boundary case — the IPN is the CLEANEST midline
leaf in the tree — and it is the MODEL the CLi and the DR should
follow (Resolution B).**
*   **The CLi** (``.../tegmentum/caudal_linear_nucleus/``) — a
    **midline** serotonergic/dopaminergic nucleus — is **represented
    as paired** (anomalous — ``.../caudal_linear_nucleus/left/``
    and ``.../caudal_linear_nucleus/right/``). The **CLi leaf**,
    the **CLi `left/` module**, and the **CLi `right/` module** all
    flag the anomaly and recommend **Resolution B** — **removing**
    the `left/` and `right/` nodes so that the CLi is represented
    as a **single midline leaf**, consistent with its anatomy.
*   **The DR** (``.../tegmentum/dorsal_raphe_nucleus/``) — a
    **midline** serotonergic nucleus — is **represented as paired**
    (anomalous — ``.../dorsal_raphe_nucleus/left/`` and
    ``.../dorsal_raphe_nucleus/right/``). The **DR leaf** **assumed
    a clean representation** (its own "the tree represents the DR
    cleanly" framing was **FALSIFIED** by the on-disk `left/` and
    `right/` nodes), and its **`left/` and `right/` modules** flag
    the **falsified-assumption** and recommend **Resolution B**.
*   **The IPN** (this module) — a **midline** limbic relay nucleus —
    is **represented cleanly** — **a single leaf** under
    ``tegmentum/``, **no `left/` or `right/` nodes** — **the
    correct representation**.
**The IPN is the FIRST GENUINELY CLEAN midline leaf in the tree.**
**It is the model the CLi and DR should follow** — the tree
**already does** midline cleanly for the IPN, so it **can** for the
CLi and DR too. **The DR leaf's "clean case" framing was
premature** — the DR itself turned out to be paired. **The IPN
provides what the DR leaf could not** — an actual, existing,
on-disk clean midline leaf. **Resolution B for the CLi and DR has
its proof case: the IPN.**
**Boundary status (NOT a CN nucleus — NOT cross-listed with
``cranial_nerve_nuclei/``):** **Boundary case — the interpeduncular
nucleus is NOT a cranial nerve nucleus.** It is a **limbic relay
nucleus** — it is **not a CN nucleus** and is **NOT cross-listed**
with the ``cranial_nerve_nuclei/`` container. The **four CN nuclei**
in the tegmentum (oculomotor, trochlear, Edinger-Westphal,
mesencephalic trigeminal) are **cross-listed** between
``tegmentum/`` and ``cranial_nerve_nuclei/`` — **the IPN is not one
of them**. Consumers must **not** look for the IPN under
``.../cranial_nerve_nuclei/`` — it has **one path only**:
``.../tegmentum/interpeduncular_nucleus/``.
**Boundary status (NOT the habenula — the habenula is the
EPITHALAMUS INPUT):** **Boundary case — the interpeduncular nucleus
is NOT the habenula.** The **habenula** (``.../forebrain/
diencephalon/epithalamus/habenular_nuclei/``) is the **epithalamus**
input — the **medial habenula** and the **lateral habenula** — in
the **dorsal diencephalon**. The **habenula** is the **upstream
source** of the **habenulointerpeduncular tract** (the **fasciculus
retroflexus**). **The IPN is the DOWNSTREAM target** of the
habenula. **They are DIFFERENT STRUCTURES across a lobe boundary**
— the **habenula** is **diencephalic**; the **IPN** is
**mesencephalic**. Consumers must **not** conflate the IPN with the
habenula, and must **not** resolve the habenula through the IPN path
(or vice versa).
**Boundary status (NOT the fasciculus retroflexus — the fasciculus
is the CONDUCTION PATHWAY):** **Boundary case — the interpeduncular
nucleus is NOT the fasciculus retroflexus (the habenulointerpeduncular
tract).** The **fasciculus retroflexus** is the **conduction
pathway** — **white matter** — that connects the **habenula** to
the **IPN**. **The fasciculus is UPSTREAM of the IPN** — it
**carries** the habenular input to the IPN. **The IPN is the
NUCLEUS** — **grey matter** — at the **end** of the tract. **They
are DIFFERENT STRUCTURES** — the **fasciculus retroflexus** is a
**conduction pathway**; the **IPN** is a **nucleus**. Consumers
must **not** conflate the IPN with the fasciculus retroflexus.
**Boundary status (NOT the dorsal raphe — the DR is a DOWNSTREAM
TARGET):** **Boundary case — the interpeduncular nucleus is NOT the
dorsal raphe nucleus (DR).** The **DR**
(``.../tegmentum/dorsal_raphe_nucleus/``) is a **midline serotonergic
modulatory nucleus** — **one of the IPN's principal DOWNSTREAM
targets**. **The IPN projects GABAergic axons TO the DR** — the IPN
**inhibits** the DR. **The DR is DOWNSTREAM of the IPN.** **They are
DIFFERENT STRUCTURES** — the **IPN** is a **GABAergic limbic
relay**; the **DR** is a **serotonergic modulatory nucleus**.
Consumers must **not** conflate the IPN with the DR.
**Boundary status (NOT the median raphe — the MnR is a DOWNSTREAM
TARGET):** **Boundary case — the interpeduncular nucleus is NOT the
median raphe nucleus (MnR).** The **MnR**
(``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) is a
**pons** serotonergic nucleus — **one of the IPN's principal
DOWNSTREAM targets**. **The IPN projects GABAergic axons TO the
MnR** — the IPN **inhibits** the MnR. **The MnR is DOWNSTREAM of the
IPN.** **They are DIFFERENT STRUCTURES at DIFFERENT levels** — the
**IPN** is **midbrain**; the **MnR** is **pons**.
**Boundary status (NOT the VTA — the VTA is a DOWNSTREAM TARGET):**
**Boundary case — the interpeduncular nucleus is NOT the ventral
tegmental area (VTA).** The **VTA**
(``.../tegmentum/left/ventral_tegmental_area/`` and the right
counterpart) is a **paired dopaminergic nucleus** — **one of the
IPN's DOWNSTREAM targets**. **The IPN projects GABAergic axons TO
the VTA** — the IPN **inhibits** the VTA. **The VTA is DOWNSTREAM of
the IPN.** **They are DIFFERENT STRUCTURES** — the **IPN** is
**midline, GABAergic, limbic relay**; the **VTA** is **paired,
dopaminergic, reward nucleus**.
**Boundary status (NOT the substantia nigra — the SN is a DOWNSTREAM
TARGET):** **Boundary case — the interpeduncular nucleus is NOT the
substantia nigra (SN).** The **SN**
(``.../tegmentum/left/substantia_nigra/`` and the right
counterpart) is a **paired nucleus** — **pars compacta**
(dopaminergic) and **pars reticulata** (GABAergic) — **one of the
IPN's DOWNSTREAM targets** (especially the **pars compacta**). **The
IPN projects GABAergic axons TO the SN** — the IPN **inhibits** the
SN. **The SN is DOWNSTREAM of the IPN.** **They are DIFFERENT
STRUCTURES** — the **IPN** is **midline, GABAergic, limbic relay**;
the **SN** is **paired, dopaminergic/GABAergic, motor/limbic
nucleus**.
**Boundary status (NOT the periaqueductal gray — the PAG is a
DOWNSTREAM TARGET):** **Boundary case — the interpeduncular nucleus
is NOT the periaqueductal gray (PAG).** The **PAG**
(``.../tegmentum/left/periaqueductal_gray/`` and the right
counterpart — or the midline PAG, depending on the on-disk tree) is
the **pain-modulation and defensive-behavior** region — **one of the
IPN's DOWNSTREAM targets**. **The IPN projects GABAergic axons TO
the PAG** — the IPN **modulates** the PAG. **The PAG is DOWNSTREAM
of the IPN.** **They are DIFFERENT STRUCTURES** — the **IPN** is in
the **ventral tegmentum** (interpeduncular fossa); the **PAG** is
**around the aqueduct** (dorsal tegmentum).
**Boundary status (NOT the cerebral peduncles — the peduncles are
the LATERAL NEIGHBORS):** **Boundary case — the interpeduncular
nucleus is NOT the cerebral peduncles.** The **cerebral peduncles**
(``.../midbrain/cerebral_peduncle/``) are the **ventral-most
descending fiber bundles** — the **crus cerebri** — **white matter**
— the **lateral boundaries** of the **interpeduncular fossa**. **The
IPN sits IN the interpeduncular fossa** — **between** the two
cerebral peduncles. **They are DIFFERENT STRUCTURES** — the
**peduncles** are **conduction pathways**; the **IPN** is a
**nucleus**. Consumers must **not** conflate the IPN with the
cerebral peduncles.
**Boundary status (NOT the substantia innominata / basal forebrain
— those are UPSTREAM AFFERENTS):** **Boundary case — the
interpeduncular nucleus is NOT the substantia innominata or the
basal forebrain.** The **substantia innominata** and the **basal
forebrain** (``.../forebrain/telencephalon/subcortical/basal_
forebrain/``) are **telencephalic** structures — **upstream
afferents** that project to the **habenula** (via the **stria
medullaris** and the **medial forebrain bundle**), which in turn
projects to the **IPN** (via the **fasciculus retroflexus**). **The
IPN is DOWNSTREAM of the basal forebrain** — **not the basal
forebrain**. **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **basal forebrain** is **telencephalic**; the
**IPN** is **mesencephalic**. Consumers must **not** conflate the
IPN with the basal forebrain.
**Boundary status (NOT the epithalamus — the epithalamus is the
ROSTRAL NEIGHBOR, and the HABENULA is in it):** **Boundary case —
the interpeduncular nucleus is NOT the epithalamus.** The
**epithalamus** (``.../forebrain/diencephalon/epithalamus/``) is a
**diencephalic** region — it contains the **habenula** (medial and
lateral), the **pineal gland**, the **stria medullaris**, the
**posterior commissure**, and the **habenular commissure**. **The
IPN is the DOWNSTREAM relay of the habenula** — **not the
epithalamus**. **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **epithalamus** is **diencephalic**; the **IPN** is
**mesencephalic**.
**Boundary status (NOT the pons — the pons is the CAUDAL NEIGHBOR):**
**Boundary case — the interpeduncular nucleus is NOT the pons.** The
**pons** (``.../hindbrain/metencephalon/pons/``) is the
**rhombencephalic** structure — **caudal** to the midbrain, across
the **pontomesencephalic junction**. **The IPN is at the caudal
midbrain / pontomesencephalic junction** — but it is a **midbrain**
structure, **not a pontine** one. **They are DIFFERENT STRUCTURES
across a lobe boundary.** Consumers must **not** conflate the IPN
with the pons.
**Boundary status (LIMBIC RELAY NUCLEUS — a NEW structure class —
NOT a sensory relay, NOT a neuromodulatory nucleus):** **Boundary
case — the interpeduncular nucleus is a LIMBIC RELAY NUCLEUS.** In
the family's **structure-class taxonomy**, it is a **relay nucleus**
— the **same broader family** as the **sensory relay nuclei** (the
**IC**, the **pretectal nuclei**) — **but for LIMBIC/EMOTIONAL
signals rather than sensory ones**. It is **NOT** a **sensory
relay** (it does not transduce or relay a sensory modality), **NOT**
a **neuromodulatory nucleus** (it does not broadcast to the whole
brain via volume transmission — it **relays** specific limbic
signals via **point-to-point projections**), **NOT** a **motor
nucleus**, **NOT** a **premotor pool**, **NOT** a **sensorimotor
integration** structure, and **NOT** a **conduction pathway**. **It
is a RELAY** — it receives the habenular input and **relays** it,
via **GABAergic** projections, to the raphe, the VTA, the SN, and
the PAG. **Relay nuclei carry NO coupling warning** — same rule as
motor nuclei, premotor pools, sensor nuclei, neuromodulatory
nuclei, sensorimotor integration structures, and conduction
pathways. Its **midline position** — **not paired** — is the
**structural expression** of its **relay function**: the habenula
and the IPN are **midline structures** that **relay bilateral
signals** to **bilateral targets**. **The IPN is a NEW structure
class** — **limbic relay nucleus** — the same family as the sensory
relays, but for limbic rather than sensory signals. See
*Lateralization Notes* and *Design Contract*.
**Boundary status (GABAergic — the OUTPUT phenotype is a
``chemicals_hormones``-layer fact):** **Boundary case — the
interpeduncular nucleus is **GABAergic** — its **principal output
is GABA.** The **GABAergic phenotype** (GAD, GABA synthesis, GABA
transporters, GABA-A and GABA-B receptors) is a
**``chemicals_hormones``-layer fact** — the **neurochemical** fact,
**not** a structural fact. It is documented as **prose** in the leaf
and **never imported** into the midbrain structural layer.
Dependency DAG unchanged: ``chemicals_hormones → memory →
brainparts``. **The IPN also receives cholinergic input from the
medial habenula** — the **cholinergic phenotype** (in the medial
habenula, not the IPN itself) is also a **``chemicals_hormones``-
layer fact** — documented in the habenula leaf, **not** here. **The
IPN's principal output transmitter is GABA** — that is the
structural chemical fact. Consumers must **not** import the
**GABAergic** or **cholinergic** phenotypes into the midbrain
structural layer. See *Chemicals-Layer Discipline* and *Design
Contract*.
**Boundary status (NO COUPLING WARNING — the IPN is a LIMBIC RELAY
NUCLEUS):** **Boundary case — the interpeduncular nucleus carries NO
coupling warning.** The **coupling warning** attaches to
**OSCILLATORS** (the pre-Bötzinger complex, the Bötzinger complex,
the pFRG) — and the **IPN is not an oscillator**. **It is a midline
limbic relay nucleus** — a **single leaf**, **not paired**.
**Relay nuclei carry NO coupling warning** — same rule as every
non-oscillator class. The **midline position** is **not a coupling
hazard** — it is the **structural fact** of a **midline relay**
that **reaches both sides** via its **projections**, **not** via
intrinsic left-right coupling. There are **no "two sides" to
couple** — the IPN is **one midline nucleus**.

Overview
--------
The interpeduncular nucleus (IPN) is the **principal downstream
relay of the habenula** — a **midline GABAergic limbic relay
nucleus** in the **ventral midbrain tegmentum**, in the
**interpeduncular fossa** (the space between the two cerebral
peduncles) — at the level of the **caudal midbrain /
pontomesencephalic junction**. It is the **downstream node** of one
of the **best-defined limbic circuits** in the brain — the
**habenula → fasciculus retroflexus → IPN → raphe/VTA/SN/PAG**
circuit. It is the **first genuinely cleanly-represented midline
leaf in the tree** — the on-disk tree path is a **single leaf**
(``tegmentum/interpeduncular_nucleus/``) with **no `left/` or
`right/` nodes** — and it is the **model the CLi and DR should
follow** (Resolution B — remove their `left/` and `right/` nodes).
It is a **limbic relay nucleus** — the same broader family as the
sensory relay nuclei (the IC, the pretectum), but for **limbic**
rather than **sensory** signals.

**The IPN is a MIDLINE LEAF — CLEANLY REPRESENTED.** The tree
represents the IPN **exactly as its anatomy demands**: **one midline
nucleus, one leaf**, directly under ``tegmentum/``. **This is the
first genuinely cleanly-represented midline leaf in the tree** —
the **CLi** and the **DR** are **both represented as paired**
(anomalous), so the tree has **no other clean midline leaf** besides
the IPN. **The IPN path is the existing model the CLi and DR should
follow.** See *The Clean Midline Leaf — the Model the CLi and DR
Should Follow*.

**The IPN is a LIMBIC RELAY NUCLEUS.** It is a **relay** — the
**same broader family** as the sensory relay nuclei (the IC, the
pretectum) — **but for limbic/emotional signals**, not sensory
ones. It receives the habenular input and **relays** it, via
**GABAergic** projections, to the raphe, the VTA, the SN, and the
PAG. **It is NOT a neuromodulatory nucleus** (it relays point-to-
point signals, not volume-transmitted modulation), **NOT a motor
nucleus**, **NOT a premotor pool**, **NOT a sensorimotor integration**
structure, **NOT a sensory relay**, and **NOT a conduction pathway**.

**The IPN is a GABAergic gate on the ascending serotonergic and
dopaminergic systems.** Its **GABAergic output** to the **raphe
nuclei** (the DR and the MnR), the **VTA**, the **substantia
nigra**, and the **PAG** **inhibits** those targets — the IPN is a
**GABAergic brake** on the **ascending serotonergic and dopaminergic
systems**. This is the **structural basis** of the IPN's role in the
**anti-reward / aversion** circuit — the **lateral habenula → IPN →
GABAergic inhibition of the VTA and the raphe** — the circuit that
**suppresses reward-seeking behavior** and **promotes behavioral
inhibition**.

**The IPN is NOT a CN nucleus.** It is a **limbic relay nucleus** —
it is **not** cross-listed with ``cranial_nerve_nuclei/``. It has
**one path only**.

**The IPN carries NO coupling warning.** It is a **midline relay
nucleus** — a **single leaf**, **not paired**. **Relay nuclei carry
NO coupling warning** — same rule as every non-oscillator class.

The Clean Midline Leaf — the Model the CLi and DR Should Follow
--------------------------------------------------------------
**The IPN is the FIRST GENUINELY CLEANLY-REPRESENTED MIDLINE LEAF in
the tree.** It is directly under ``tegmentum/`` — **no `left/`, no
`right/`** — and its **single midline path** is the **correct
representation** of a **midline nucleus**.

**The CLi and the DR are both represented as paired** — anomalous:

*   **CLi** (``.../tegmentum/caudal_linear_nucleus/``) — **midline**
    nucleus, **represented as paired** (``.../caudal_linear_nucleus/
    left/`` and ``.../caudal_linear_nucleus/right/``). Its **leaf**,
    its **`left/` module**, and its **`right/` module** all **flag
    the anomaly** and recommend **Resolution B** — remove the
    `left/` and `right/` nodes.

*   **DR** (``.../tegmentum/dorsal_raphe_nucleus/``) — **midline**
    nucleus, **represented as paired** (``.../dorsal_raphe_nucleus/
    left/`` and ``.../dorsal_raphe_nucleus/right/``). Its leaf
    **assumed a clean representation** — its own **"the tree
    represents the DR cleanly"** framing was **FALSIFIED** by the
    on-disk `left/` and `right/` nodes — and its **`left/` and
    `right/` modules** flag the **falsified-assumption** and
    recommend **Resolution B**.

**The IPN is the actual clean case.** It is **what the DR leaf
claimed the DR was, but is not** — an existing, on-disk,
single-leaf, midline nucleus directly under ``tegmentum/``. **The
IPN path is the model the CLi and DR should follow.** Remove the
CLi's `left/` and `right/` nodes; remove the DR's `left/` and
`right/` nodes; both become **clean midline leaves**, like the
IPN. **Resolution B for the CLi and the DR has its proof case: the
IPN.**

**The IPN is also the proof case for the tegmentum container
amendment.** The tegmentum container's paired-leaf rule — *"each
tegmentum nucleus is a paired structure (a ``left/`` leaf and a
``right/`` leaf)"* — was written **before** the CLi, the DR, and
the IPN were added. **The IPN is a midline nucleus represented
cleanly** — **direct child of ``tegmentum/``, no `left/` or
`right/`** — so the paired-leaf rule **must be amended** to permit
**midline nuclei** as **direct children**, **not required** to be
under `left/` or `right/`. **The IPN is the existing example.**
See *Design Contract — Live amendment to the tegmentum container*.

**The IPN is also the proof case for the midbrain container
amendment.** The midbrain container's PAG prose — *"the cerebral
aqueduct and the periaqueductal gray are midline structures, not
paired"* — and the tegmentum container's paired-leaf rule — *"the
PAG is midline-adjacent but is treated as paired in the tree"* —
are **inconsistent with each other**. **The IPN is a clean third
data point** — a midline nucleus represented cleanly. **The tree can
do midline cleanly** — the IPN is the proof. **Both containers
should be reconciled** to accommodate **midline leaves** consistently.

Subnuclear Organization (prose, not structural children)
-------------------------------------------------------
The interpeduncular nucleus has a **subnuclear organization** — the
IPN is a **complex nucleus** with **distinct subnuclei** —
documented as **prose**, not as structural children. **The IPN
subnuclei are ALL midline or midline-adjacent** — they are
**subdivisions of a single midline nucleus**, not a **left/right
pair**:

*   **Central subnucleus** — the **main output** subnucleus —
    **GABAergic** projections to the **dorsal raphe** and the
    **median raphe** — the **GABAergic brake on the serotonergic
    system**. The **central subnucleus** is the **principal output**
    of the IPN.

*   **Intermediate subnucleus** — **GABAergic** projections to the
    **VTA** — the **GABAergic brake on the dopaminergic reward
    system**.

*   **Dorsal subnucleus** — smaller; projections to the **PAG** and
    the **reticular formation**.

*   **Lateral subnucleus** — smaller; projections to the
    **substantia nigra** and the **reticular formation**.

*   **Rostral subnucleus** — smaller; receives the **habenular
    input** and projects to the **central subnucleus**.

*   **Caudal subnucleus** — smaller; projections to the **raphe**
    and the **reticular formation**.

**These subnuclei are prose, not structural children.** They are
**subdivisions of a single midline nucleus** — **not a left/right
pair**. The tree wires the **interpeduncular nucleus** as a
**single leaf** under the tegmentum container (midline). Consumers
must **not** resolve ``.../interpeduncular_nucleus/central_
subnucleus`` — no such path exists. **The IPN subnuclei are
midline subdivisions, not left/right pairs** — a structural fact
that **reinforces** the IPN's **clean midline-leaf**
representation. **The IPN's internal organization is midline, just
as its tree representation is.**

The Habenular Circuit (the IPN's functional context)
---------------------------------------------------
The **interpeduncular nucleus** is the **principal downstream
relay** of the **habenula** — the **habenula → fasciculus
retroflexus → IPN → raphe/VTA/SN/PAG** circuit is one of the
**best-defined limbic circuits** in the brain. The circuit has two
components:

*   **The medial habenula (MHb) → IPN pathway** — the **MHb** is a
    **cholinergic** and **substance-P**-containing structure in the
    **epithalamus** (dorsal diencephalon). It projects to the IPN
    via the **dorsal part** of the **fasciculus retroflexus** —
    **cholinergic** input to the IPN. The **MHb → IPN** pathway is
    implicated in **nicotine withdrawal**, **nicotine aversion**,
    and **anxiety-related behaviors**. **The IPN receives the
    cholinergic input** and **relays** it (via **GABAergic**
    output) to the **raphe** and the **VTA** — the **MHb → IPN →
    GABAergic inhibition of the reward system** circuit.

*   **The lateral habenula (LHb) → IPN pathway** — the **LHb** is
    a **glutamatergic** structure in the **epithalamus** — the
    **"anti-reward" nucleus** — it is **activated by negative
    reward prediction error**, **stress**, **pain**, and **aversive
    stimuli**. It projects to the IPN via the **ventral part** of
    the **fasciculus retroflexus** — **glutamatergic** input to the
    IPN. The **LHb → IPN** pathway is the **anti-reward / aversion**
    circuit — the circuit that **suppresses reward-seeking
    behavior** and **promotes behavioral inhibition**. **The IPN
    receives the glutamatergic input** and **relays** it (via
    **GABAergic** output) to the **raphe** and the **VTA** — the
    **LHb → IPN → GABAergic inhibition of the reward system**
    circuit.

**The IPN is the key downstream relay of BOTH habenular pathways**
— the **MHb (nicotine/aversion)** and the **LHb (anti-reward/
aversion)** — and its **GABAergic output** is the **common brake**
on the ascending **serotonergic** (raphe) and **dopaminergic**
(VTA, SN) systems.

**The IPN is a GABAergic gate** — it **inhibits** the ascending
serotonergic and dopaminergic systems, **promoting** **behavioral
inhibition** and **negative affect** — the **structural basis** of
the **LHb/IPN anti-reward circuit** and the **MHb/IPN nicotine
circuit**.

The IPN's Place in the Limbic Relay System
------------------------------------------
The **interpeduncular nucleus** is a **limbic relay nucleus** — the
**same broader family** as the **sensory relay nuclei** (the **IC**,
the **pretectal nuclei**) — **but for limbic/emotional signals
rather than sensory ones**. **Relay nuclei** are a **distinct
structure class**:

*   **They RECEIVE input** from an **upstream source** and **RELAY
    it** — via **point-to-point projections** — to **downstream
    targets**. **The IPN receives the habenular input** (via the
    fasciculus retroflexus) and **relays** it (via **GABAergic**
    projections) to the raphe, the VTA, the SN, and the PAG.

*   **They are NOT sensory relays** in the **strict** sense — the
    **IC** and the **pretectum** relay **sensory** modalities
    (auditory, visual). **The IPN relays LIMBIC/EMOTIONAL
    signals** — the **habenular anti-reward and aversion
    signals**. **The IPN is a LIMBIC relay** — a **subtype** of
    the relay nucleus class.

*   **They are NOT neuromodulatory nuclei** — the **DR**, the
    **CLi**, the **locus coeruleus**, and the **VTA** are
    **neuromodulatory** — they **broadcast** to the whole brain via
    **volume transmission**. **The IPN relays point-to-point
    signals** — it **projects** to **specific targets** (the
    raphe, the VTA, the SN, the PAG) with **GABAergic synapses**,
    not **volume transmission**. **The IPN is a relay**, not a
    **modulator**.

*   **They are NOT motor nuclei, NOT premotor pools, NOT
    sensorimotor integration structures, NOT conduction pathways.**
    The **IPN is a relay** — the **same broader family** as the
    sensory relays, but for **limbic** signals.

**The IPN is a NEW structure class** — **limbic relay nucleus** —
the **same broader family** as the **sensory relay nuclei**, but
for **limbic/emotional signals**. **The class carries NO coupling
warning** — same rule as every non-oscillator class. **The midline
position is the structural expression of the relay function** — a
**midline relay** that **reaches both sides** does not need a
**left/right pair**; it needs a **midline nucleus** whose
projections **fan out bilaterally**. See *Lateralization Notes*.

The Interpeduncular Nucleus / Habenula Boundary
-----------------------------------------------
This is the **input relay / input source** boundary — the **most
consequential** boundary in the leaf:

*   **Interpeduncular nucleus** (this module) — the **downstream
    relay** — **GABAergic** — in the **ventral midbrain
    tegmentum** (interpeduncular fossa).

*   **Habenula** (``.../forebrain/diencephalon/epithalamus/habenular_
    nuclei/``) — the **upstream source** — the **medial habenula**
    (cholinergic) and the **lateral habenula** (glutamatergic) —
    in the **epithalamus** (dorsal diencephalon).

**The habenula is the UPSTREAM source; the IPN is the DOWNSTREAM
relay.** The **fasciculus retroflexus** (the
**habenulointerpeduncular tract**) is the **conduction pathway**
connecting them. **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **habenula** is **diencephalic**; the **IPN** is
**mesencephalic**. Consumers must **not** conflate the IPN with the
habenula, and must **not** resolve the habenula through the IPN path
(or vice versa).

The Interpeduncular Nucleus / Fasciculus Retroflexus Boundary
-------------------------------------------------------------
This is the **nucleus / conduction pathway** boundary:

*   **Interpeduncular nucleus** (this module) — the **nucleus** —
    **grey matter** — the **downstream relay**.

*   **Fasciculus retroflexus (habenulointerpeduncular tract)** — the
    **conduction pathway** — **white matter** — the **habenular
    input** to the IPN.

**The fasciculus retroflexus is UPSTREAM of the IPN** — it
**carries** the habenular input to the IPN. **The IPN is the
NUCLEUS** — **grey matter** — at the **end** of the tract. **They
are DIFFERENT STRUCTURES** — the **fasciculus retroflexus** is a
**conduction pathway**; the **IPN** is a **nucleus**. Consumers
must **not** conflate the IPN with the fasciculus retroflexus.

The Interpeduncular Nucleus / Dorsal Raphe Nucleus Boundary
-----------------------------------------------------------
This is the **relay / output target** boundary:

*   **Interpeduncular nucleus** (this module) — the **GABAergic
    limbic relay** — **midline**.

*   **Dorsal raphe nucleus (DR)**
    (``.../tegmentum/dorsal_raphe_nucleus/``) — a **midline
    serotonergic modulatory nucleus** — **one of the IPN's
    principal DOWNSTREAM targets**.

**The IPN projects GABAergic axons TO the DR** — it **inhibits** the
DR. **The DR is DOWNSTREAM of the IPN.** **They are DIFFERENT
STRUCTURES** — the **IPN** is a **GABAergic limbic relay**; the
**DR** is a **serotonergic modulatory nucleus**.

The Interpeduncular Nucleus / Median Raphe Nucleus Boundary
-----------------------------------------------------------
This is the **midbrain relay / pontine target** boundary:

*   **Interpeduncular nucleus** (this module) — the **GABAergic
    limbic relay** — **midbrain**.

*   **Median raphe nucleus (MnR)**
    (``.../hindbrain/metencephalon/pons/median_raphe_nucleus/``) —
    a **pons** serotonergic nucleus — **one of the IPN's principal
    DOWNSTREAM targets**.

**The IPN projects GABAergic axons TO the MnR** — it **inhibits**
the MnR. **The MnR is DOWNSTREAM of the IPN.** **They are DIFFERENT
STRUCTURES at DIFFERENT levels** — the **IPN** is **midbrain**; the
**MnR** is **pons**.

The Interpeduncular Nucleus / Ventral Tegmental Area Boundary
-------------------------------------------------------------
This is the **relay / dopaminergic target** boundary:

*   **Interpeduncular nucleus** (this module) — the **GABAergic
    limbic relay** — **midline**.

*   **Ventral tegmental area (VTA)**
    (``.../tegmentum/left/ventral_tegmental_area/`` and the right
    counterpart) — a **paired dopaminergic nucleus** — **one of the
    IPN's DOWNSTREAM targets**.

**The IPN projects GABAergic axons TO the VTA** — it **inhibits** the
VTA. **The VTA is DOWNSTREAM of the IPN.** **They are DIFFERENT
STRUCTURES** — the **IPN** is **midline, GABAergic, limbic relay**;
the **VTA** is **paired, dopaminergic, reward nucleus**.

The Interpeduncular Nucleus / Substantia Nigra Boundary
-------------------------------------------------------
This is the **relay / dopaminergic-GABAergic target** boundary:

*   **Interpeduncular nucleus** (this module) — the **GABAergic
    limbic relay** — **midline**.

*   **Substantia nigra (SN)**
    (``.../tegmentum/left/substantia_nigra/`` and the right
    counterpart) — a **paired nucleus** — **pars compacta**
    (dopaminergic) and **pars reticulata** (GABAergic) — **one of
    the IPN's DOWNSTREAM targets** (especially the **pars
    compacta**).

**The IPN projects GABAergic axons TO the SN** — it **inhibits** the
SN. **The SN is DOWNSTREAM of the IPN.** **They are DIFFERENT
STRUCTURES.**

The Interpeduncular Nucleus / Periaqueductal Gray Boundary
----------------------------------------------------------
This is the **ventral relay / dorsal modulatory target** boundary:

*   **Interpeduncular nucleus** (this module) — the **GABAergic
    limbic relay** — in the **ventral tegmentum** (interpeduncular
    fossa).

*   **Periaqueductal gray (PAG)**
    (``.../tegmentum/left/periaqueductal_gray/`` and the right
    counterpart — or the midline PAG, depending on the on-disk
    tree) — the **pain-modulation and defensive-behavior** region
    — **one of the IPN's DOWNSTREAM targets**.

**The IPN projects GABAergic axons TO the PAG** — it **modulates**
the PAG. **The PAG is DOWNSTREAM of the IPN.** **They are DIFFERENT
STRUCTURES in DIFFERENT positions** — the **IPN** is in the
**ventral tegmentum**; the **PAG** is **around the aqueduct**
(dorsal tegmentum).

The Interpeduncular Nucleus / Cerebral Peduncles Boundary
---------------------------------------------------------
This is the **nucleus / conduction pathway** boundary — and the
**interpeduncular fossa** context:

*   **Interpeduncular nucleus** (this module) — the **nucleus** —
    **grey matter** — **in the interpeduncular fossa**.

*   **Cerebral peduncles** (``.../midbrain/cerebral_peduncle/``) —
    the **ventral-most descending fiber bundles** — the **crus
    cerebri** — **white matter** — the **lateral boundaries** of
    the interpeduncular fossa.

**The IPN sits IN the interpeduncular fossa** — **between** the two
cerebral peduncles. **They are DIFFERENT STRUCTURES** — the
**peduncles** are **conduction pathways**; the **IPN** is a
**nucleus**. Consumers must **not** conflate the IPN with the
cerebral peduncles.

The Interpeduncular Nucleus / Substantia Innominata and Basal Forebrain Boundary
-------------------------------------------------------------------------------
This is the **midbrain relay / telencephalic afferent** boundary:

*   **Interpeduncular nucleus** (this module) — the **midbrain
    relay** — **mesencephalic**.

*   **Substantia innominata** and the **basal forebrain**
    (``.../forebrain/telencephalon/subcortical/basal_forebrain/``)
    — **telencephalic** — **upstream afferents** that project to the
    **habenula** (via the **stria medullaris** and the **medial
    forebrain bundle**), which in turn projects to the **IPN** (via
    the **fasciculus retroflexus**).

**The IPN is DOWNSTREAM of the basal forebrain** — **not the basal
forebrain**. **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **basal forebrain** is **telencephalic**; the
**IPN** is **mesencephalic**.

The Interpeduncular Nucleus / Epithalamus Boundary
--------------------------------------------------
This is the **midbrain relay / diencephalic input source** boundary:

*   **Interpeduncular nucleus** (this module) — the **midbrain
    relay** — **mesencephalic**.

*   **Epithalamus** (``.../forebrain/diencephalon/epithalamus/``) —
    the **diencephalic** region — it contains the **habenula**
    (medial and lateral), the **pineal gland**, the **stria
    medullaris**, the **posterior commissure**, and the
    **habenular commissure**.

**The IPN is DOWNSTREAM of the habenula** — **not the epithalamus**.
**They are DIFFERENT STRUCTURES across a lobe boundary** — the
**epithalamus** is **diencephalic**; the **IPN** is
**mesencephalic**. The **IPN** is the **downstream relay** of the
habenula — which is **one** of the epithalamus structures.

The Interpeduncular Nucleus / Pons Boundary
-------------------------------------------
This is the **midbrain / rhombencephalic** boundary:

*   **Interpeduncular nucleus** (this module) — the **midbrain
    relay** — **mesencephalic** — at the **caudal midbrain /
    pontomesencephalic junction**.

*   **Pons** (``.../hindbrain/metencephalon/pons/``) — the
    **rhombencephalic** structure — **caudal** to the midbrain,
    across the **pontomesencephalic junction**.

**The IPN is at the caudal midbrain / pontomesencephalic junction**
— but it is a **midbrain** structure, **not a pontine** one.
**They are DIFFERENT STRUCTURES across a lobe boundary.** Consumers
must **not** conflate the IPN with the pons.

Function in the Human Brain
---------------------------
The interpeduncular nucleus's function is **limbic relay** —
**GABAergic inhibition** of the ascending serotonergic and
dopaminergic systems — **NOT** a sensory relay, **NOT** a
neuromodulatory nucleus, **NOT** a motor nucleus, **NOT** a
premotor pool, **NOT** a sensorimotor integration structure, **NOT**
a conduction pathway:

*   **Relay of the Habenular Anti-Reward Signal (the primary
    function):** The **lateral habenula (LHb)** — the **"anti-reward"
    nucleus** — is **activated by negative reward prediction
    error**, **stress**, **pain**, and **aversive stimuli**. It
    **projects** to the **IPN** (via the **ventral fasciculus
    retroflexus**), and the IPN **relays** the signal via
    **GABAergic** projections to the **raphe** and the **VTA** —
    **inhibiting** the ascending serotonergic and dopaminergic
    systems. **The IPN is the GABAergic gate** on the **anti-reward
    circuit** — it **suppresses reward-seeking behavior** and
    **promotes behavioral inhibition**.

*   **Relay of the Habenular Nicotine/Aversion Signal (the secondary
    function):** The **medial habenula (MHb)** — **cholinergic**,
    **substance-P**-containing — projects to the **IPN** (via the
    **dorsal fasciculus retroflexus**), and the IPN **relays** the
    signal via **GABAergic** projections to the **raphe** and the
    **VTA** — **inhibiting** the ascending serotonergic and
    dopaminergic systems. **The IPN is the GABAergic gate** on the
    **nicotine/aversion circuit** — it **mediates** **nicotine
    withdrawal**, **nicotine aversion**, and **anxiety-related
    behaviors**.

*   **GABAergic Inhibition of the Ascending Serotonergic System:**
    The IPN's **GABAergic projections** to the **dorsal raphe** and
    the **median raphe** **inhibit** the serotonergic system — the
    **IPN is a GABAergic brake** on the **serotonergic system**.
    **The IPN's inhibition of the raphe** is the **structural basis**
    of the **LHb/IPN anti-reward circuit's effect on mood and
    anxiety** — it **suppresses serotonergic activity**,
    **promoting** **negative affect** and **behavioral
    inhibition**.

*   **GABAergic Inhibition of the Ascending Dopaminergic System:**
    The IPN's **GABAergic projections** to the **VTA** and the
    **substantia nigra** **inhibit** the dopaminergic system — the
    **IPN is a GABAergic brake** on the **dopaminergic system**.
    **The IPN's inhibition of the VTA and the SN** is the
    **structural basis** of the **LHb/IPN anti-reward circuit's
    effect on reward** — it **suppresses dopaminergic activity**,
    **promoting** **anhedonia** and **behavioral inhibition**.

*   **Modulation of the PAG:** The IPN's **GABAergic projections**
    to the **PAG** **modulate** the **pain-modulation and
    defensive-behavior** region — the **IPN is a modulator** of the
    **PAG's defensive responses**.

*   **NOT a sensory relay.** The IPN does **not** transduce or
    relay a specific sensory modality.

*   **NOT a neuromodulatory nucleus.** The IPN does **not** broadcast
    to the whole brain via volume transmission — it **relays**
    point-to-point signals via **GABAergic** synapses to
    **specific targets**.

*   **NOT a motor nucleus.** The IPN does **not** drive muscle.

*   **NOT a premotor pool.** The IPN does **not** transform motor
    commands.

*   **NOT a sensorimotor integration structure.** The IPN does
    **not** integrate sensory input into a behavioral command.

*   **NOT a conduction pathway.** The IPN is **grey matter** — a
    nucleus — **not white matter**.

*   **NOT an oscillator.** The IPN is a **relay nucleus** — it does
    **not** generate a rhythm. **Relay nuclei carry NO coupling
    warning** — same rule as every non-oscillator class.

**The unifying theme:** the IPN is a **midline GABAergic limbic
relay nucleus** — the **principal downstream relay of the habenula**
— the **GABAergic gate** on the ascending serotonergic and
dopaminergic systems. It is the **downstream node** of the
**LHb/IPN anti-reward circuit** (suppression of reward-seeking,
behavioral inhibition) and the **MHb/IPN nicotine/aversion circuit**
(nicotine withdrawal, nicotine aversion, anxiety). It is a **limbic
relay nucleus** — the same broader family as the sensory relays, but
for limbic signals — and it is the **first genuinely cleanly-
represented midline leaf in the tree** — a **midline nucleus
represented cleanly** — the **model the CLi and DR should follow**.

Associated Disorders
--------------------
The interpeduncular nucleus has **no named syndrome of its own** —
its clinical associations are **direct** and **substantial**, via
its **GABAergic relay of the habenular anti-reward and aversion
signals** — and it is a **contributor** to several major clinical
syndromes. **The habenula is the primary substrate** in several of
these — the **IPN is the downstream relay**:

*   **Major Depressive Disorder (DIRECT — the LHb/IPN circuit is the
    "anti-reward" circuit, implicated in depression):** The
    **LHb/IPN circuit** — the **lateral habenula → IPN → GABAergic
    inhibition of the VTA and the raphe** — is **implicated** in
    **major depressive disorder**. **LHb hyperactivity** produces
    **anhedonia** and **behavioral despair** — the **IPN is the
    downstream relay** of the LHb's anti-reward signal. **Deep brain
    stimulation of the lateral habenula** has been investigated for
    **treatment-resistant depression** — **the IPN is part of the
    downstream circuit**.

*   **Nicotine Withdrawal and Nicotine Aversion (DIRECT — the
    MHb/IPN pathway):** The **MHb/IPN pathway** is **implicated**
    in **nicotine withdrawal**, **nicotine aversion**, and
    **anxiety-related behaviors**. **α3β4 nicotinic receptors** in
    the **MHb/IPN pathway** are a **target** for **smoking
    cessation** — **varenicline** (a partial nicotinic agonist)
    acts partly via the **MHb/IPN pathway**. **The IPN is a
    contributor** to the nicotine/aversion circuit.

*   **Stress Responses (DIRECT — the LHb/IPN circuit):** The
    **LHb/IPN circuit** is **activated** by **stress** and
    **aversive stimuli** — the **IPN is a contributor** to the
    **stress response** (via its GABAergic inhibition of the VTA
    and the raphe).

*   **Pain-Related Aversion (DIRECT — the LHb/IPN circuit):** The
    **LHb/IPN circuit** is **implicated** in **pain-related
    aversion** — the **IPN is a contributor** (via its GABAergic
    inhibition of the VTA and the raphe, and its modulation of the
    PAG).

*   **Schizophrenia (INDIRECT — lower IPN volume, altered habenular
    function):** The **habenula/IPN circuit** has been **implicated**
    in **schizophrenia** — **lower IPN volume** and **altered
    habenular function** have been reported. **The IPN is a
    contributor** to the broader habenular circuit that is
    implicated in schizophrenia.

*   **Addiction (INDIRECT — the VTA is the primary dopaminergic
    substrate, the LHb/IPN circuit modulates reward):** **Substance
    use disorders** are **primarily dopaminergic** (the **VTA** is
    the primary dopaminergic nucleus) — **the LHb/IPN circuit
    modulates reward-seeking** via its GABAergic inhibition of the
    VTA. **The IPN is a modulator** of the reward circuit — the
    **VTA is the primary dopaminergic substrate**.

*   **No Named "Interpeduncular Nucleus Syndrome":** The IPN is a
    **small midline limbic relay** — it has **no named syndrome of
    its own** — but its **clinical associations are direct and
    substantial**: it is a **contributor** to **major depressive
    disorder**, **nicotine withdrawal**, **nicotine aversion**,
    **stress responses**, **pain-related aversion**, and
    **schizophrenia** — and a **modulator** of the **reward
    circuit** and the **serotonergic system**. **The habenula is
    the primary substrate** in several of these; the **IPN is the
    downstream relay**.

**What is NOT here:** The IPN is **not** the substrate for **major
depressive disorder as an IPN-exclusive syndrome** (the **LHb/IPN
circuit** is implicated — the **habenula is the primary substrate**,
the **IPN is the downstream relay**; depression is a multifactorial
disorder), **nicotine withdrawal as an IPN-exclusive syndrome** (the
**MHb/IPN pathway** is implicated — the **habenula is the primary
substrate**), **schizophrenia as an IPN-exclusive syndrome** (a
**complex polygenic disorder**), **addiction as an IPN-exclusive
syndrome** (the **VTA** is the primary dopaminergic substrate — the
**IPN is a modulator**), **Parkinson's disease** (the **substantia
nigra pars compacta** — **NOT** the IPN), **Alzheimer's disease**
(the **nucleus basalis of Meynert**, the **hippocampus**, the
**cortex** — **NOT** the IPN), **descending pain modulation as an
IPN-exclusive function** (the **raphe magnus** and the **PAG** are
the primary substrates — the **IPN modulates the PAG**),
**saccade disorders** (the **SC**, the **SNr**, the **riMLF** —
**NOT** the IPN), **pupillary light reflex deficits** (the
**pretectum** and the **EW nucleus** — **NOT** the IPN),
**oculomotor palsy** (the **CN III nucleus** — **NOT** the IPN),
**trochlear palsy** (the **CN IV nucleus** — **NOT** the IPN),
**trigeminal sensory deficits** (the **trigeminal ganglion**, the
**main sensory**, and the **spinal trigeminal nucleus** — **NOT**
the IPN), **CCHS** (RTN), **OIRD** (pre-Bötzinger complex — NK1R
neurons), **Rett syndrome** (pre-Bötzinger complex), **SIDS**
(proposed — pre-Bötzinger complex + arcuate nucleus), **essential
hypertension / sympathetic overactivity** (C1 group / RVLM),
**Huntington's disease** (striatum — telencephalon), or
**Kluver-Bucy syndrome** (amygdala). Its clinical relevance is
**direct and substantial** — it is a **contributor** to several
major disorders — but the disorders are **multifactorial**, and the
**habenula is the primary substrate** in several of them; the
**IPN is the downstream relay**. **No named "interpeduncular
nucleus syndrome" exists.**

Lateralization Notes
--------------------
This is the **interpeduncular nucleus** leaf — the **first
genuinely cleanly-represented midline leaf in the tree**. The IPN
is **midline**, **not paired** — it has **no left/right pair** and
**no mirror leaf**. **The tree represents it CLEANLY** — one
midline leaf under ``tegmentum/``, **no `left/` or `right/` nodes**.
**This is the model that the CLi's and the DR's paths should
follow** (Resolution B). **No coupling warning** — the same rule as
every non-oscillator class.

*   **Midline Nucleus — NOT Paired:** The IPN is a **single midline
    leaf** directly under ``tegmentum/`` — **NOT** under
    ``tegmentum/left/`` or ``tegmentum/right/``. It has **no
    left/right pair**, **no mirror leaf**, **no bilateral
    iteration**.

*   **Cleanly Represented in the Tree — the FIRST Genuinely Clean
    Midline Leaf:** The IPN is the **first genuinely
    cleanly-represented midline leaf** in the tree — the tree
    represents it **exactly as its anatomy demands**: one midline
    nucleus, one leaf. **The CLi and the DR are both represented
    as paired** — anomalous — so **the IPN is the ONLY clean
    midline leaf in the tree**. **This is the model that the
    CLi's and the DR's paths should follow** (Resolution B —
    remove their `left/` and `right/` nodes). **The tree can do
    midline cleanly** — the IPN is the proof. **The DR leaf
    claimed this for the DR, but the DR was falsified — the IPN
    is the actual existing clean case.**

*   **Midline Position = Relay Function:** The IPN is a **GABAergic
    limbic relay** — it **receives** the habenular input (from
    both the MHb and the LHb) and **relays** it via **GABAergic**
    projections to **bilateral targets** (the raphe, the VTA, the
    SN, the PAG). **The midline position is the structural fact**
    — a **midline relay** has a **midline nucleus** whose
    projections **fan out bilaterally** to its targets on both
    sides. **It has no "two sides" to couple** — the IPN is one
    midline nucleus.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to RELAY NUCLEI):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **IPN** is a **relay nucleus** — a **single
    midline leaf** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. There are
    **no "two sides" to couple** — the IPN is **one midline
    nucleus** whose **distributed projections** carry its relay
    signal to **both sides**. **Relay nuclei carry NO coupling
    warning** — same rule as every non-oscillator class.

*   **No SLEA Warning:** The IPN is **SLEA-free** — it is **not**
    an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The IPN is **not** part
    of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The IPN is **not** a
    rhinencephalon structure.

**The IPN is the FIRST GENUINELY CLEAN midline leaf in the tree** —
its **midline position**, **limbic relay class**, **clean
representation in the tree**, and **no coupling warning** establish
the **canonical structural pattern** for midline relay nuclei. **The
CLi and the DR are the anomalous cases** — the tree represents them
with `left/` and `right/` nodes, which their own modules flag as
**tree-structural anomalies**. **The tree should be amended so that
the CLi and the DR follow the IPN's clean pattern** (Resolution B).
See *The Clean Midline Leaf — the Model the CLi and DR Should
Follow*.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The IPN is **midline** — there
    is **no** other hemisphere to import from.
*   **No cross-lobe imports.** This module does **not** import from
    the **habenula**, the **fasciculus retroflexus**, the **PAG**,
    the **VTA**, the **substantia nigra**, the **caudal linear
    nucleus**, the **dorsal raphe**, the **median raphe**, the
    **medullary raphe nuclei**, the **locus coeruleus**, the
    **cerebral peduncles**, the **basal forebrain**, the
    **epithalamus**, the **pons**, or any other container. The
    IPN's relationships to the habenula, the fasciculus retroflexus,
    the PAG, the VTA, the substantia nigra, the caudal linear
    nucleus, the dorsal raphe, the median raphe, the medullary
    raphe nuclei, the locus coeruleus, the cerebral peduncles, the
    basal forebrain, the epithalamus, and the pons are documented
    as **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **GABAergic
    phenotype** (the IPN's principal output) and the **cholinergic
    phenotype** (in the medial habenula, the IPN's input) are
    **``chemicals_hormones``-layer facts** — documented as
    **prose**, **never imported**. **CHEMICALS-LAYER DISCIPLINE**
    is preserved.
*   **MIDLINE LEAF — CLEANLY REPRESENTED.** The IPN is a **single
    leaf** directly under ``tegmentum/`` — **NO**
    ``tegmentum/interpeduncular_nucleus/left/`` and **NO**
    ``tegmentum/interpeduncular_nucleus/right/``. **This is the
    FIRST GENUINELY CLEANLY-REPRESENTED MIDLINE LEAF IN THE
    TREE.** **The IPN path is the model that the CLi's and the
    DR's paths should follow** (Resolution B — removing their
    `left/` and `right/` nodes).
*   **THE CLEAN MIDLINE LEAF — the MODEL the CLi and DR should
    follow.** The **CLi** and the **DR** are **both represented as
    paired** (anomalous). The **CLi leaf**, the **CLi `left/`**,
    the **CLi `right/`**, the **DR leaf**, the **DR `left/`**, and
    the **DR `right/`** all flag the anomaly and recommend
    **Resolution B** — removing their `left/` and `right/` nodes so
    that they become clean midline leaves, like the IPN. **The IPN
    is the existing, on-disk, clean case** — **the proof case the
    DR leaf claimed the DR was, but is not.**
*   **LIVE AMENDMENT TO THE CLi's REPRESENTATION.** The CLi's
    `left/` and `right/` nodes should be **removed** (Resolution
    B) — following the IPN's **clean midline-leaf pattern**. The
    CLi should be a **single midline leaf** under ``tegmentum/``,
    **no `left/` or `right/` nodes** — like the IPN.
*   **LIVE AMENDMENT TO THE DR's REPRESENTATION.** The DR's
    `left/` and `right/` nodes should be **removed** (Resolution
    B) — following the IPN's **clean midline-leaf pattern**. The DR
    should be a **single midline leaf** under ``tegmentum/``, **no
    `left/` or `right/` nodes** — like the IPN. **This RESTORES the
    DR leaf's clean-case framing** (the DR leaf **assumed** a clean
    representation, which its own `left/` and `right/` modules
    falsified — restoring the clean case makes the DR leaf's
    framing **true again**).
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER.** The tegmentum
    container's **paired-leaf rule** — *"each tegmentum nucleus is
    a paired structure (a ``left/`` leaf and a ``right/`` leaf)"*
    — should be **AMENDED** to state that **midline nuclei are
    permitted** as **direct children** of ``tegmentum/`` — **not
    required** to be under ``left/`` or ``right/``. **The IPN is a
    midline nucleus represented cleanly** — **direct child of
    ``tegmentum/``, no `left/` or `right/`** — so the rule must
    be amended. **The IPN's clean representation is the existing
    model.**
*   **LIVE AMENDMENT TO THE MIDBRAIN CONTAINER.** The midbrain
    container's PAG prose — *"the cerebral aqueduct and the
    periaqueductal gray are midline structures, not paired"* —
    and the tegmentum container's paired-leaf rule — *"the PAG is
    midline-adjacent but is treated as paired in the tree"* — are
    **inconsistent with each other**. The **IPN is a clean third
    data point** — a midline nucleus represented cleanly. **Both
    containers should be reconciled** to accommodate **midline
    leaves** consistently.
*   **LIMBIC RELAY NUCLEUS — a NEW structure class.** The IPN is a
    **limbic relay nucleus** — the **same broader family** as the
    **sensory relay nuclei** (the IC, the pretectum) — **but for
    limbic/emotional signals rather than sensory ones**. It is
    **NOT** a sensory relay, **NOT** a neuromodulatory nucleus,
    **NOT** a motor nucleus, **NOT** a premotor pool, **NOT** a
    sensorimotor integration structure, and **NOT** a conduction
    pathway. It **receives** the habenular input and **relays** it
    (via **GABAergic** projections) to the raphe, the VTA, the SN,
    and the PAG.
*   **GABAergic — the output phenotype is a
    ``chemicals_hormones``-layer fact.** The IPN's principal output
    is **GABA** — the **GABAergic phenotype** is a
    ``chemicals_hormones``-layer fact. Documented as **prose**,
    **never imported**.
*   **NO COUPLING WARNING — relay nuclei carry NO coupling
    warning.** The IPN is a **single midline leaf** — a **midline
    relay nucleus** — it does **not** generate a rhythm. **The
    midline position is not a coupling hazard** — it is the
    structural fact of a **midline relay** that **reaches both
    sides** via its **projections**, not via intrinsic left-right
    coupling.
*   **NOT A CN NUCLEUS.** The IPN is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. It has **one path only**.
*   **NOT the habenula — the habenula is the EPITHALAMUS INPUT.**
*   **NOT the fasciculus retroflexus — the fasciculus is the
    CONDUCTION PATHWAY.**
*   **NOT the dorsal raphe — the DR is a DOWNSTREAM TARGET.** The
    IPN **inhibits** the DR via **GABAergic** projections.
*   **NOT the median raphe — the MnR is a DOWNSTREAM TARGET.** The
    IPN **inhibits** the MnR.
*   **NOT the VTA — the VTA is a DOWNSTREAM TARGET.** The IPN
    **inhibits** the VTA.
*   **NOT the substantia nigra — the SN is a DOWNSTREAM TARGET.**
    The IPN **inhibits** the SN.
*   **NOT the PAG — the PAG is a DOWNSTREAM TARGET.** The IPN
    **modulates** the PAG.
*   **NOT the cerebral peduncles — the peduncles are the LATERAL
    NEIGHBORS.**
*   **NOT the basal forebrain — the basal forebrain is an UPSTREAM
    AFFERENT** (via the habenula).
*   **NOT the epithalamus — the epithalamus is the DIENCEPHALIC
    INPUT SOURCE.**
*   **NOT the pons — the pons is the RHOMBENCEPHALIC CAUDAL
    NEIGHBOR.**
*   **CHEMICALS-LAYER DISCIPLINE.** The **GABAergic** and
    **cholinergic** phenotypes are **``chemicals_hormones``-layer
    facts** — documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The IPN is a
    **local midline leaf** under the tegmentum — no cross-listing.
*   **No nested cross-listing.** The IPN is a **single leaf**. It
    is **not** a container.
*   **The on-disk tree is authoritative.** The on-disk tree has
    ``.../tegmentum/interpeduncular_nucleus/`` — **one leaf**,
    **midline**, **no `left/` or `right/`**. **This is the correct
    representation** — the IPN is a midline nucleus, and the tree
    represents it cleanly. **The IPN path is the model that the
    CLi's and DR's paths should follow** (Resolution B).

Usage
-----
Resolve the leaf by path (**one** path only — the IPN is **midline**,
**not** under `left/` or `right/`)::

    from infrastructure.brainparts.midbrain.tegmentum import interpeduncular_nucleus

Or by fully-qualified path string::

    path = "midbrain.tegmentum.interpeduncular_nucleus"

**Do not** assume the IPN is under
``tegmentum/interpeduncular_nucleus/left/`` or
``tegmentum/interpeduncular_nucleus/right/``. **It is MIDLINE** — a
**single leaf** directly under ``tegmentum/``. **The tree represents
it cleanly.** **The IPN path is the model that the CLi's and DR's
paths should follow** (Resolution B — removing their `left/` and
`right/` nodes).

**Do not** assume the IPN is a **cranial nerve nucleus**. It is
**not** a CN nucleus and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the IPN is the **habenula**. The **habenula** is
the **epithalamus input** — **diencephalic** — the **upstream
source** of the **habenulointerpeduncular tract**. **The IPN is the
DOWNSTREAM relay.** **They are DIFFERENT STRUCTURES across a lobe
boundary.**

**Do not** assume the IPN is the **fasciculus retroflexus**. The
**fasciculus retroflexus** is the **conduction pathway** — **white
matter** — between the habenula and the IPN. **The IPN is the
NUCLEUS** — **grey matter**.

**Do not** assume the IPN is the **dorsal raphe**, the **median
raphe**, the **VTA**, the **substantia nigra**, or the **PAG**.
Those are **DOWNSTREAM TARGETS** of the IPN's **GABAergic**
projections — **the IPN inhibits or modulates them**.

**Do not** assume the IPN is the **cerebral peduncles**. The
**peduncles** are the **lateral neighbors** — the **cerebral
peduncles** flank the **interpeduncular fossa** where the IPN sits.

**Do not** assume the IPN is the **basal forebrain** or the
**epithalamus**. The **basal forebrain** is an **upstream
afferent** (via the habenula); the **epithalamus** is the
**diencephalic input source** (contains the habenula). **The IPN is
midbrain** — downstream of both.

**Do not** assume the IPN is the **pons**. The **pons** is the
**rhombencephalic caudal neighbor** — the IPN is at the **caudal
midbrain**, near the pontomesencephalic junction.

**Do not** import the **GABAergic phenotype** (GAD, GABA, GAT,
GABA-A/GABA-B receptors) or the **cholinergic phenotype** (in the
medial habenula, the IPN's input) into the midbrain structural
layer. Both are **``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the IPN. **Relay
nuclei carry NO coupling warning** — same rule as every non-
oscillator class. **The midline position is not a coupling
hazard.**

**Do not** treat the IPN as a **paired structure**. It is a
**midline nucleus** — a **single leaf** — with **no left/right
pair** and **no mirror leaf**. **The tree represents it cleanly.**

Iterating the interpeduncular nucleus's (empty) children
(recommended consumer pattern)::

    INTERPEDUNCULAR_NUCLEUS_CHILDREN = ()
    # The interpeduncular nucleus is a leaf. The subnuclear
    # organization (central, intermediate, dorsal, lateral, rostral,
    # caudal) is prose, not modules. The GABAergic projection
    # neurons and the local-circuit interneurons are prose, not
    # modules.

Bilateral iteration — **NOT APPLICABLE**::

    # The interpeduncular nucleus is MIDLINE — it has NO left/right
    # pair. There is no bilateral iteration for the IPN. If you
    # find yourself writing:
    #
    #     for side in ("left", "right"):
    #         path = f"midbrain.tegmentum.{side}.interpeduncular_nucleus"
    #
    # — that is WRONG. The IPN is at:
    #
    #     midbrain.tegmentum.interpeduncular_nucleus
    #
    # — a single midline leaf. The tree represents the IPN correctly.

Reaching the habenula (recommended consumer pattern — the
DIENCEPHALIC INPUT SOURCE)::

    # The habenula is the DIENCEPHALIC INPUT SOURCE — the medial
    # habenula (cholinergic) and the lateral habenula
    # (glutamatergic) — in the epithalamus (dorsal diencephalon):
    #
    #   brainparts.forebrain.diencephalon.epithalamus.habenular_nuclei
    #
    # The habenula is UPSTREAM of the IPN — it projects to the IPN
    # via the fasciculus retroflexus. The IPN is the DOWNSTREAM
    # relay.

Reaching the fasciculus retroflexus (recommended consumer pattern —
the CONDUCTION PATHWAY)::

    # The fasciculus retroflexus (habenulointerpeduncular tract) is
    # the CONDUCTION PATHWAY — white matter — connecting the
    # habenula to the IPN:
    #
    #   brainparts.forebrain.diencephalon.epithalamus.fasciculus_retroflexus
    #
    # The fasciculus is UPSTREAM of the IPN — it carries the
    # habenular input to the IPN. The IPN is the NUCLEUS at the end
    # of the tract.

Reaching the dorsal raphe (recommended consumer pattern — the
DOWNSTREAM TARGET)::

    # The dorsal raphe nucleus (DR) is one of the IPN's principal
    # DOWNSTREAM TARGETS — the IPN projects GABAergic axons to the
    # DR, INHIBITING it:
    #
    #   brainparts.midbrain.tegmentum.dorsal_raphe_nucleus
    #
    # The DR is DOWNSTREAM of the IPN. The IPN is the GABAergic
    # brake on the DR (and the serotonergic system).

Reaching the median raphe (recommended consumer pattern — the
DOWNSTREAM TARGET)::

    # The median raphe nucleus (MnR) is one of the IPN's principal
    # DOWNSTREAM TARGETS — the IPN projects GABAergic axons to the
    # MnR, INHIBITING it:
    #
    #   brainparts.hindbrain.metencephalon.pons.median_raphe_nucleus
    #
    # The MnR is DOWNSTREAM of the IPN. The IPN is the GABAergic
    # brake on the MnR (and the serotonergic system).

Reaching the VTA (recommended consumer pattern — the DOWNSTREAM
TARGET)::

    # The ventral tegmental area (VTA) is one of the IPN's DOWNSTREAM
    # TARGETS — the IPN projects GABAergic axons to the VTA,
    # INHIBITING it:
    #
    #   brainparts.midbrain.tegmentum.left.ventral_tegmental_area
    #   brainparts.midbrain.tegmentum.right.ventral_tegmental_area
    #
    # The VTA is DOWNSTREAM of the IPN. The IPN is the GABAergic
    # brake on the VTA (and the dopaminergic reward system).

Reaching the substantia nigra (recommended consumer pattern — the
DOWNSTREAM TARGET)::

    # The substantia nigra (SN) is one of the IPN's DOWNSTREAM
    # TARGETS — the IPN projects GABAergic axons to the SN,
    # INHIBITING it:
    #
    #   brainparts.midbrain.tegmentum.left.substantia_nigra
    #   brainparts.midbrain.tegmentum.right.substantia_nigra
    #
    # The SN is DOWNSTREAM of the IPN.

Reaching the PAG (recommended consumer pattern — the DOWNSTREAM
TARGET)::

    # The periaqueductal gray (PAG) is one of the IPN's DOWNSTREAM
    # TARGETS — the IPN projects GABAergic axons to the PAG,
    # MODULATING it:
    #
    #   brainparts.midbrain.tegmentum.left.periaqueductal_gray
    #   brainparts.midbrain.tegmentum.right.periaqueductal_gray
    #   (OR: brainparts.midbrain.tegmentum.periaqueductal_gray —
    #    depending on the on-disk tree)
    #
    # The PAG is DOWNSTREAM of the IPN.

Reaching the cerebral peduncles (recommended consumer pattern — the
LATERAL NEIGHBORS)::

    # The cerebral peduncles are the LATERAL NEIGHBORS of the IPN —
    # they flank the interpeduncular fossa where the IPN sits:
    #
    #   brainparts.midbrain.cerebral_peduncle
    #
    # The IPN sits IN the interpeduncular fossa — BETWEEN the two
    # cerebral peduncles.

Subnuclear-organization detail (not wired — consult references)::

    # The interpeduncular nucleus has a SUBNUCLEAR organization —
    # subdivisions of a single midline nucleus:
    #
    #   central subnucleus      -> MAIN OUTPUT — GABAergic to the
    #                              dorsal raphe and the median raphe
    #                              — the GABAergic brake on the
    #                              serotonergic system
    #   intermediate subnucleus -> GABAergic to the VTA — the
    #                              GABAergic brake on the dopaminergic
    #                              reward system
    #   dorsal subnucleus       -> smaller; PAG and reticular
    #                              formation
    #   lateral subnucleus      -> smaller; substantia nigra and
    #                              reticular formation
    #   rostral subnucleus      -> smaller; receives the habenular
    #                              input; projects to the central
    #                              subnucleus
    #   caudal subnucleus       -> smaller; raphe and reticular
    #                              formation
    #
    # ALL of these subnuclei are MIDLINE or MIDLINE-ADJACENT — they
    # are SUBDIVISIONS of a single midline nucleus, NOT a left/right
    # pair. The IPN's subnuclear organization REINFORCES its
    # midline-leaf representation.
    #
    # Do not attempt to resolve these subnuclei as sub-paths of the
    # interpeduncular nucleus — they are PROSE, not modules.

The habenular circuit — detail (not wired — consult references)::

    # The habenula -> fasciculus retroflexus -> IPN -> raphe/VTA/
    # SN/PAG circuit — the IPN is the KEY DOWNSTREAM RELAY:
    #
    #   MEDIAL HABENULA (cholinergic, substance-P)
    #     -> dorsal fasciculus retroflexus
    #     -> IPN
    #     -> GABAergic projection to the raphe, the VTA
    #     -> NICOTINE WITHDRAWAL, NICOTINE AVERSION, ANXIETY
    #
    #   LATERAL HABENULA (glutamatergic — the "anti-reward" nucleus)
    #     -> ventral fasciculus retroflexus
    #     -> IPN
    #     -> GABAergic projection to the raphe, the VTA
    #     -> NEGATIVE REWARD PREDICTION ERROR, STRESS, PAIN, AVERSIVE
    #        STIMULI — SUPPRESSES REWARD-SEEKING, PROMOTES
    #        BEHAVIORAL INHIBITION
    #
    # The IPN is the GABAergic BRAKE on the ascending serotonergic
    # (raphe) and dopaminergic (VTA, SN) systems — the structural
    # basis of the anti-reward and nicotine/aversion circuits.
    #
    # Do not attempt to resolve the habenula, the fasciculus
    # retroflexus, the raphe, the VTA, the SN, or the PAG as
    # sub-paths of the IPN — they are DIFFERENT structures at
    # DIFFERENT levels.

Limbic-relay-class detail (not wired — consult references)::

    # The interpeduncular nucleus is a LIMBIC RELAY NUCLEUS — the
    # SAME BROADER FAMILY as the sensory relay nuclei (the IC, the
    # pretectum), but for LIMBIC/EMOTIONAL signals:
    #
    #   inferior colliculus          -> SENSORY RELAY (auditory)
    #   pretectal nuclei             -> SENSORY RELAY (visual —
    #                                    pupillary, optokinetic)
    #   interpeduncular nucleus      -> LIMBIC RELAY (habenular anti-
    #                                    reward and aversion signals)
    #
    # Relay nuclei RECEIVE input from an upstream source and RELAY
    # it — via POINT-TO-POINT projections — to downstream targets.
    # They are NOT sensory relays in the strict sense (the IC and the
    # pretectum are), NOT neuromodulatory nuclei (the DR, the CLi,
    # the locus coeruleus, the VTA are), NOT motor nuclei, NOT
    # premotor pools, NOT sensorimotor integration structures, NOT
    # conduction pathways.
    #
    # They carry NO coupling warning.

Clinical-pattern detail (not wired — consult references)::

    # The interpeduncular nucleus is the KEY DOWNSTREAM RELAY of
    # the habenula — its clinical associations are DIRECT and
    # SUBSTANTIAL:
    #
    #   MAJOR DEPRESSIVE DISORDER  -> DIRECT — the LHb/IPN
    #                                 "anti-reward" circuit is
    #                                 implicated; the habenula is the
    #                                 primary substrate, the IPN is
    #                                 the downstream relay; DBS of
    #                                 the LHb is investigational for
    #                                 treatment-resistant depression
    #   NICOTINE WITHDRAWAL AND    -> DIRECT — the MHb/IPN pathway;
    #     NICOTINE AVERSION            α3β4 nicotinic receptors in
    #                                 the MHb/IPN pathway are a target
    #                                 for smoking cessation
    #                                 (varenicline acts partly here)
    #   STRESS RESPONSES           -> DIRECT — the LHb/IPN circuit
    #                                 is activated by stress and
    #                                 aversive stimuli
    #   PAIN-RELATED AVERSION      -> DIRECT — the LHb/IPN circuit
    #                                 is implicated; the IPN also
    #                                 modulates the PAG
    #   SCHIZOPHRENIA              -> INDIRECT — lower IPN volume,
    #                                 altered habenular function have
    #                                 been reported
    #   ADDICTION                  -> INDIRECT — the VTA is the
    #                                 primary dopaminergic substrate;
    #                                 the LHb/IPN circuit modulates
    #                                 reward-seeking
    #
    # The habenula is the primary substrate in several of these —
    # the IPN is the downstream relay.
    #
    # Do not conflate these patterns — they localize primarily to
    # the habenula (for habenular circuit disorders), the VTA (for
    # reward), or the raphe (for serotonergic disorders).

The clean midline representation — detail (not wired — structural
note)::

    # The IPN is the FIRST GENUINELY CLEANLY-REPRESENTED MIDLINE
    # LEAF in the tree:
    #
    #   midbrain.tegmentum.interpeduncular_nucleus
    #     (ONE leaf — MIDLINE — NO left/ or right/ nodes)
    #
    # The CLi is an ANOMALOUS case:
    #
    #   midbrain.tegmentum.caudal_linear_nucleus
    #     (midline leaf)
    #   midbrain.tegmentum.caudal_linear_nucleus.left
    #     (anomalous tree-structural side container)
    #   midbrain.tegmentum.caudal_linear_nucleus.right
    #     (anomalous tree-structural side container)
    #
    # The DR is ALSO an ANOMALOUS case:
    #
    #   midbrain.tegmentum.dorsal_raphe_nucleus
    #     (midline leaf — with a clean-case framing that was
    #      FALSIFIED by the on-disk left/ and right/ nodes)
    #   midbrain.tegmentum.dorsal_raphe_nucleus.left
    #     (anomalous tree-structural side container — flags
    #      the falsified clean-case assumption)
    #   midbrain.tegmentum.dorsal_raphe_nucleus.right
    #     (anomalous tree-structural side container — flags
    #      the falsified clean-case assumption)
    #
    # The IPN's clean representation is the ACTUAL MODEL — the tree
    # represents the IPN exactly as its anatomy demands.
    #
    # The CLi's and the DR's anomalous representations should be
    # AMENDED — their left/ and right/ nodes should be REMOVED, and
    # they should be SINGLE midline leaves, like the IPN
    # (Resolution B). This is the recommendation of the CLi leaf,
    # the CLi left/ module, the CLi right/ module, the DR leaf,
    # the DR left/ module, and the DR right/ module — ALL SIX of
    # which flag the anomaly (or the falsified assumption).
    #
    # The IPN path is the canonical structural pattern for a midline
    # nucleus in the tree; the CLi and the DR should follow it.

References
----------
*   **Canonical interpeduncular nucleus anatomy:** Herkenham, M.,
    Nauta, W.J.H. (1979). "Efferent connections of the habenular
    nuclei in the rat." *Journal of Comparative Neurology*
    187:19–47. (The habenular efferents — the **fasciculus
    retroflexus** to the **interpeduncular nucleus** — the
    habenula → IPN circuit.)
*   **Interpeduncular nucleus — subnuclear organization:** Groenewegen,
    H.J., Ahlenius, S., Haber, S.N., Kowall, N.W., Nauta, W.J.H.
    (1986). "Cytoarchitecture, fiber connections, and some
    histochemical aspects of the interpeduncular nucleus in the
    rat." *Journal of Comparative Neurology* 249:428–442. (The
    IPN's subnuclear organization — central, intermediate, dorsal,
    lateral, rostral, caudal subnuclei; the efferent projections.)
*   **Interpeduncular nucleus — GABAergic output:** Kawaja, M.D.,
    Flumerfelt, B.A., Hrycyshyn, A.W. (1990). "A topographical
    analysis of the projections of the interpeduncular nucleus in
    the rat." *Journal of Comparative Neurology* 293:585–601.
    (The IPN's efferent projections — to the dorsal raphe, the
    median raphe, the VTA, the substantia nigra, and the PAG.)
*   **Habenula — medial and lateral:** Sutherland, R.J. (1982).
    "The dorsal diencephalic conduction system: a review of the
    anatomy and functions of the habenular complex."
    *Neuroscience & Biobehavioral Reviews* 6:1–13. (The habenular
    complex — the medial habenula (cholinergic) and the lateral
    habenula (glutamatergic); the fasciculus retroflexus; the
    habenula → IPN circuit.)
*   **Lateral habenula — the "anti-reward" nucleus:** Matsumoto,
    M., Hikosaka, O. (2007). "Lateral habenula as a source of
    negative reward signals in dopamine neurons." *Nature*
    447:1111–1115. (The lateral habenula as the "anti-reward"
    nucleus — the negative reward prediction error signal; the
    LHb → IPN → VTA circuit.)
*   **Lateral habenula — depression and DBS:** Sartorius, A.,
    Kiening, K.L., Kirsch, P., et al. (2010). "Remission of major
    depression under deep brain stimulation of the lateral
    habenula in a therapy-refractory patient." *Biological
    Psychiatry* 67:e9–e11. (Deep brain stimulation of the lateral
    habenula for treatment-resistant depression — the LHb/IPN
    circuit is the downstream relay.)
*   **Medial habenula — nicotine and aversion:** Fowler, C.D.,
    Lu, Q., Johnson, P.M., Marks, M.J., Kenny, P.J. (2011).
    "Habenular α3β4 nicotinic acetylcholine receptor signaling
    is required for nicotine withdrawal." *Nature* 476:365–368.
    (The medial habenula's α3β4 nicotinic receptors — the
    MHb → IPN pathway — nicotine withdrawal, nicotine aversion.)
*   **IPN — nicotine aversion:** Frahm, S., Ślimak, M.A., Ferrarese,
    L., et al. (2011). "Aversion to nicotine is mediated by the
    medial habenula." *Nature Neuroscience* 14:990–997. (The
    medial habenula → IPN pathway — nicotine aversion.)
*   **Interpeduncular nucleus — GABAergic brake on the VTA:**
    Morley, B.J. (1986). "The interpeduncular nucleus."
    *International Review of Neurobiology* 28:157–182. (The IPN —
    the GABAergic relay of the habenular input to the raphe, the
    VTA, the SN, and the PAG.)
*   **IPN — schizophrenia and volume:** Kha, H.T., Craig, K.,
    Hooper, L., Heng, S., Bernstein, H.G., Bogerts, B., O'Donnell,
    B.F. (2007). "Interpeduncular nucleus volume reduction in
    schizophrenia." *Schizophrenia Research* 93:114–122. (Lower
    IPN volume in schizophrenia — the habenula/IPN circuit is
    implicated.)
*   **IPN — schizophrenia and habenular function:** Shepard, P.D.
    (2006). "The habenula and schizophrenia." In *The Basal
    Ganglia VIII* (Bolam et al., eds.). (The habenula/IPN circuit
    in schizophrenia — altered habenular function.)
*   **IPN — the habenular circuit and stress:** Viswanath, H.,
    Carter, A.Q., Baldwin, P.R., Molfese, D.L., Salas, R. (2014).
    "The medial habenula: still neglected." *Frontiers in Human
    Neuroscience* 7:931. (The habenula/IPN circuit — stress,
    anxiety, and aversion.)
*   **Fasciculus retroflexus — the habenulointerpeduncular tract:**
    Herkenham, M., Nauta, W.J.H. (1979). "Efferent connections of
    the habenular nuclei in the rat." *Journal of Comparative
    Neurology* 187:19–47. (The fasciculus retroflexus — the
    conduction pathway between the habenula and the IPN.)
*   **Basal forebrain — the habenular afferents:** Parent, A.,
    Gravel, S., Côté, P.Y., Pioro, E. (1988). "The efferent
    projections of the basal forebrain in the rat."
    *Neuroscience* 25:69–84. (The basal forebrain's efferents —
    including the stria medullaris and the medial forebrain
    bundle, which project to the habenula, which projects to the
    IPN.)
*   **Dorsal raphe (contrast — the IPN's principal output target):**
    Michelsen, K.A., Schmitz, C., Steinbusch, H.W.M. (2007). "The
    dorsal raphe nucleus — from silver stainings to a simplified
    subnuclear organization: review on the mesencephalic raphe
    nuclei." *Brain Research Reviews* 55:349–363. (The dorsal
    raphe nucleus — one of the IPN's principal output targets.)
*   **VTA (contrast — the IPN's output target):** Fields, H.L.,
    Hjelmstad, G.O., Margolis, E.B., Nicola, S.M. (2007).
    "Ventral tegmental area neurons in learned appetitive behavior
    and positive reinforcement." *Annual Review of Neuroscience*
    30:289–316. (The VTA — one of the IPN's output targets.)
*   **PAG (contrast — the IPN's output target):** Behbehani, M.M.
    (1995). "Functional characteristics of the midbrain
    periaqueductal gray." *Progress in Neurobiology* 46:575–605.
    (The PAG — one of the IPN's output targets.)
*   **SLEA (contrast — the IPN is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the interpeduncular nucleus.)
*   NeuroNames — Interpeduncular nucleus; FMA — Interpeduncular
    nucleus. **The IPN is a single midline nucleus — there is no
    "left interpeduncular nucleus" and no "right interpeduncular
    nucleus" in the standard anatomical atlases.**
"""