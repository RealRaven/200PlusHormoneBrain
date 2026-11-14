"""
infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area.medial_parabrachial_nucleus
==================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── parabrachial_area
                ├── lateral_parabrachial_nucleus
                ├── medial_parabrachial_nucleus   <-- THIS MODULE
                └── subparabrachial_nucleus
                    ├── kolliker_fuse_nucleus
                    └── pontine_respiratory_group

**Primary synonym:** Medial parabrachial nucleus; medial parabrachial
subnucleus; MPB; MPBN; "the pontine respiratory and autonomic relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — a **respiratory- and
autonomically-organized neuron cluster** in the **medial parabrachial
area**, medial to the **lateral parabrachial nucleus** and dorsal to the
**superior cerebellar peduncle** in the **dorsal pons**, beneath the
**floor of the fourth ventricle**. It is the **principal pontine relay**
for **respiratory afferent input** (from the solitary nucleus and the
retrotrapezoid nucleus) and **autonomic regulation** (cardiorespiratory
integration, hypothalamic relay).
**Part of:** The **parabrachial_area** container — specifically, the
**respiratory and autonomic** component. The **parabrachial area** is the
**dorsal tegmental visceral-sensory and respiratory-relay complex** of
the **pons**.
**Structural parent:** ``.../parabrachial_area/`` → **direct child** of
the parabrachial_area container.
**Structural children:** **None.** This is a **leaf** module. The
**respiratory-relay neurons**, **autonomic-relay neurons**, and
**hypothalamic-projection neurons** are documented as **prose**, not as
structural children — they are the **functionally distinct neuron
populations** within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
medial parabrachial nucleus is a LEAF, not a container.** It has **no
structural children**. The **respiratory-relay neurons**,
**autonomic-relay neurons**, and **hypothalamic-projection neurons** are
**prose populations**, not structural children. Consumers must **not**
treat the medial parabrachial nucleus as a container, and must **not**
assume the neuron populations exist as sub-modules.
**Boundary status (NOT the lateral parabrachial nucleus — that is a
SIBLING):** **Boundary case — the medial parabrachial nucleus is NOT the
lateral parabrachial nucleus; the lateral parabrachial nucleus is a
SIBLING under the parabrachial_area container.** The **lateral
parabrachial nucleus**
(``.../parabrachial_area/lateral_parabrachial_nucleus/``) is the
**visceral-sensory and pain/aversion relay** — it subserves **visceral
sensation**, **taste**, **pain**, **temperature**, **aversion**, and
**food intake suppression**. The **medial parabrachial nucleus** (here)
is the **respiratory and autonomic relay** — it subserves **respiratory
afferent integration** and **cardiorespiratory autonomic regulation**.
They are **DIFFERENT STRUCTURES** — different functional systems
(visceral-sensory/pain/aversion vs. respiratory/autonomic), different
downstream targets (amygdala/BNST/insula/hypothalamus/VPMpc/PAG vs.
VRG/Kölliker-Fuse/hypothalamus). They are **anatomically adjacent**
(both are in the parabrachial area) — this proximity is a **classic
source of confusion** — consumers must **not** conflate the medial
parabrachial nucleus with the lateral parabrachial nucleus.
**Boundary status (NOT the subparabrachial nucleus — that is a
SIBLING):** **Boundary case — the medial parabrachial nucleus is NOT
the subparabrachial nucleus; the subparabrachial nucleus is a SIBLING
under the parabrachial_area container.** The **subparabrachial nucleus**
(``.../parabrachial_area/subparabrachial_nucleus/``) is the **pontine
respiratory center proper** — it contains the **Kölliker-Fuse nucleus**
and the **pontine respiratory group**. The **medial parabrachial
nucleus** (here) is the **respiratory afferent and autonomic relay** —
it **receives** respiratory afferents from the **solitary nucleus** and
the **retrotrapezoid nucleus** and **projects** them to the **ventral
respiratory group** and the **Kölliker-Fuse nucleus**. They are
**DIFFERENT STRUCTURES** — different functional roles (afferent relay
and autonomic integration vs. respiratory rhythm generation and phase
switching), different downstream targets. **However**, they are
**functionally coupled** — the medial parabrachial nucleus **provides
afferent input to** the subparabrachial nucleus (especially the
Kölliker-Fuse nucleus). Consumers must **not** conflate the medial
parabrachial nucleus with the subparabrachial nucleus.
**Boundary status (NOT the Kölliker-Fuse nucleus or the pontine
respiratory group — those are STRUCTURAL NEPHEWS):** **Boundary case —
the medial parabrachial nucleus is NOT the Kölliker-Fuse nucleus or the
pontine respiratory group; those are STRUCTURAL NEPHEWS (children of the
subparabrachial nucleus, which is a sibling of the medial parabrachial
nucleus).** The **Kölliker-Fuse nucleus** and the **pontine respiratory
group** are children of the **subparabrachial_nucleus** — a **sibling**
of the medial parabrachial nucleus. They are **structural nephews** of
the medial parabrachial nucleus, not the medial parabrachial nucleus
itself. Consumers must **not** conflate the medial parabrachial nucleus
with the Kölliker-Fuse nucleus or the pontine respiratory group.
**Boundary status (NOT the superior cerebellar peduncle — that is the
WHITE-MATTER TRACT the nucleus is DORSAL to):** **Boundary case — the
medial parabrachial nucleus is the GREY-MATTER NUCLEUS, NOT the superior
cerebellar peduncle.** The **superior cerebellar peduncle** (the
"brachium conjunctivum") is the **white-matter tract** that carries
**cerebellar efferents** from the **dentate nucleus** and the
**interposed nucleus** to the **red nucleus** and the **thalamus**. The
**medial parabrachial nucleus** (here) is the **grey-matter neuron
cluster** that is **dorsal** to the superior cerebellar peduncle —
within the **parabrachial area** (the collection of nuclei flanking the
brachium). They are **DIFFERENT STRUCTURES** — the **nucleus** is grey
matter; the **peduncle** is white matter. **This distinction is the
etymological origin of the "parabrachial" name and is a classic source
of confusion** — consumers must **not** conflate the medial parabrachial
nucleus with the superior cerebellar peduncle.
**Boundary status (NOT the locus coeruleus — that is the adjacent
noradrenergic nucleus):** **Boundary case — the medial parabrachial
nucleus is NOT the locus coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain — it
is in the **pontine tegmentum**, **ventromedial** to the medial
parabrachial nucleus. The **medial parabrachial nucleus** (here) is the
**respiratory and autonomic relay**. They are **DIFFERENT STRUCTURES** —
different neurotransmitters (glutamate, etc. vs. norepinephrine),
different functional systems (respiratory/autonomic vs. noradrenergic
arousal). They are **anatomically adjacent** — this proximity is a
**classic source of confusion** — consumers must **not** conflate the
medial parabrachial nucleus with the locus coeruleus.
**Boundary status (NOT the solitary nucleus — that is the MEDULLARY
UPSTREAM SOURCE):** **Boundary case — the medial parabrachial nucleus
is NOT the solitary nucleus.** The **solitary nucleus** (nucleus tractus
solitarius, ``.../medulla_oblongata/solitary_nucleus/left/`` and
``.../right/``) is the **medullary visceral-afferent hub** for **CN VII,
IX, and X** — including **respiratory afferents** from the **carotid
body** and **aortic body** chemoreceptors, the **lung** stretch
receptors, and the **airway** receptors. The **solitary nucleus** is the
**upstream source** — it **projects to** the **medial parabrachial
nucleus** via the **central tegmental tract**. The **medial parabrachial
nucleus** (here) is the **pontine relay** that **receives** the solitary
nucleus respiratory projections and **projects** them to the **ventral
respiratory group** and the **Kölliker-Fuse nucleus**. They are
**DIFFERENT STRUCTURES** — the **solitary nucleus** is **medullary** and
**upstream**; the **medial parabrachial nucleus** is **pontine** and
**downstream**. **This distinction is clinically load-bearing** — a
**solitary nucleus** lesion causes **impaired respiratory afferent
integration** (loss of chemoreception, loss of lung stretch reflex); a
**medial parabrachial nucleus** lesion causes **impaired respiratory
relay** (respiratory rhythm dysregulation). Consumers must **not**
conflate the medial parabrachial nucleus with the solitary nucleus.
**Boundary status (NOT the retrotrapezoid nucleus — that is the MEDULLARY
CENTRAL CHEMORECEPTOR):** **Boundary case — the medial parabrachial
nucleus is NOT the retrotrapezoid nucleus (RTN).** The **RTN**
(``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
is the **medullary central chemoreceptor** — it **senses CO₂ / pH** and
**drives** the **ventral respiratory group** for **respiratory
chemoreception**. The **medial parabrachial nucleus** (here) is the
**pontine respiratory relay** — it **receives** the RTN projections and
**relays** them to the **ventral respiratory group** and the
**Kölliker-Fuse nucleus**. They are **DIFFERENT STRUCTURES** — different
brainstem levels (pons vs. medulla), different functional roles (pontine
relay vs. medullary chemoreception). **This distinction is clinically
load-bearing** — an **RTN** lesion causes **central hypoventilation**
(loss of CO₂ chemoreception); a **medial parabrachial nucleus** lesion
causes **respiratory rhythm dysregulation** without loss of
chemoreception. Consumers must **not** conflate the medial parabrachial
nucleus with the retrotrapezoid nucleus.
**Boundary status (NOT the ventral respiratory group — that is the
MEDULLARY RESPIRATORY PATTERN GENERATOR):** **Boundary case — the medial
parabrachial nucleus is NOT the ventral respiratory group (VRG).** The
**VRG** (``.../medulla_oblongata/ventral_respiratory_group/``) is the
**medullary respiratory pattern generator** — it **contains** the
**pre-Bötzinger complex** (the **respiratory rhythm generator**), the
**nucleus ambiguus** (pharyngeal/laryngeal motor), the
**retrotrapezoid nucleus** (chemoreception), and other respiratory
neurons. The **medial parabrachial nucleus** (here) is the **pontine
respiratory relay** — it **projects to** the VRG (especially the
pre-Bötzinger complex) and **modulates** the respiratory rhythm. They
are **DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine relay vs. medullary rhythm
generation). Consumers must **not** conflate the medial parabrachial
nucleus with the ventral respiratory group.
**Boundary status (NOT the dorsal respiratory group — that is the
MEDULLARY INSPIRATORY CENTER):** **Boundary case — the medial
parabrachial nucleus is NOT the dorsal respiratory group (DRG).** The
**DRG** (``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
is the **medullary inspiratory center** — it **contains** the
**inspiratory neurons** of the **solitary nucleus** and **drives** the
**phrenic nerve** for **diaphragmatic contraction**. The **medial
parabrachial nucleus** (here) is the **pontine respiratory relay** — it
**modulates** the DRG and the VRG for **respiratory phase switching**
and **respiratory rhythm**. They are **DIFFERENT STRUCTURES** —
different brainstem levels (pons vs. medulla), different functional roles
(pontine modulation vs. medullary inspiratory drive). Consumers must
**not** conflate the medial parabrachial nucleus with the dorsal
respiratory group.
**Boundary status (NOT the paramedian pontine reticular formation — that
is the horizontal gaze center):** **Boundary case — the medial
parabrachial nucleus is NOT the paramedian pontine reticular formation
(PPRF).** The **PPRF** (``.../pons/paramedian_pontine_reticular_formation/``)
is the **horizontal saccadic burst generator** — it **drives** the
abducens nucleus for **horizontal saccades**. The **medial parabrachial
nucleus** (here) is the **respiratory and autonomic relay**. They are
**DIFFERENT STRUCTURES** — different functional systems (horizontal gaze
vs. respiratory/autonomic). Consumers must **not** conflate the medial
parabrachial nucleus with the PPRF.
**Boundary status (NOT the pontine nuclei — those are basilar-pons
cortico-ponto-cerebellar relays):** **Boundary case — the medial
parabrachial nucleus is NOT the pontine nuclei.** The **pontine nuclei**
(``.../pons/pontine_nuclei/left/`` and ``.../right/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons**. The **medial
parabrachial nucleus** (here) is the **dorsal tegmental** respiratory and
autonomic-relay nucleus. They are **DIFFERENT STRUCTURES** — different
anatomical locations (basilar pons vs. dorsal tegmentum), different
functional systems (cortico-ponto-cerebellar vs. respiratory/autonomic).
Consumers must **not** conflate the medial parabrachial nucleus with the
pontine nuclei.
**Boundary status (NOT the whole pons — the pons is the grandparent):**
**Boundary case — the medial parabrachial nucleus is NOT the whole pons;
the pons is the grandparent.** The **pons** (``.../pons/``) is the
**whole metencephalic brainstem segment** — it contains the **basilar
pons**, the **pontine tegmentum**, the **pontine nuclei**, the
**corticospinal / corticobulbar tracts**, the **middle cerebellar
peduncle**, the **cranial_nerve_nuclei**, and the **parabrachial area**.
The **medial parabrachial nucleus** (here) is the **respiratory and
autonomic-relay component** of the **parabrachial area** only. Consumers
must **not** conflate the medial parabrachial nucleus with the **whole
pons**.
**Boundary status (CLASSICAL FUNCTIONAL GROUPING vs. TREE STRUCTURAL
WIRING — the medial parabrachial nucleus is CLASSICALLY part of the
pontine respiratory group, but the tree wires the pontine respiratory
group as a child of the subparabrachial nucleus):** **Boundary case —
the medial parabrachial nucleus is CLASSICALLY part of the pontine
respiratory group, but the tree wires the pontine respiratory group as a
child of the subparabrachial nucleus, NOT the medial parabrachial
nucleus.** In the **classical respiratory neurobiology literature**, the
**pontine respiratory group (PRG)** is often defined as including the
**Kölliker-Fuse nucleus** and the **medial parabrachial nucleus** (some
authors) — or the **Kölliker-Fuse nucleus** and the **subparabrachial
nucleus** (others). **In the tree**, the **pontine respiratory group**
is a **structural child** of the **subparabrachial_nucleus**, NOT the
**medial_parabrachial_nucleus**. This is a **tree-wiring decision**, not
a claim that the medial parabrachial nucleus is not functionally related
to the pontine respiratory group. **Functionally**, the medial
parabrachial nucleus **provides afferent input to** the Kölliker-Fuse
nucleus and the pontine respiratory group. **Structurally**, the medial
parabrachial nucleus is a **sibling** of the subparabrachial nucleus,
not its **parent**. Consumers must **not** assume the tree's structural
wiring matches the classical functional grouping — the tree wires the
pontine respiratory group as a child of the subparabrachial nucleus
because that is the **structural** relationship, even though the
classical **functional** grouping may include the medial parabrachial
nucleus.
**Boundary status (NOT a single uniform neuron population —
MULTIPLE functionally distinct populations):** **Boundary case — the
medial parabrachial nucleus is NOT a single uniform neuron population;
it contains MULTIPLE functionally distinct populations.** The
**respiratory-relay neurons** (the **respiratory afferent input** from
the solitary nucleus and the retrotrapezoid nucleus — they **project to**
the **ventral respiratory group** and the **Kölliker-Fuse nucleus**).
The **autonomic-relay neurons** (the **autonomic afferent input** from
the solitary nucleus — they **project to** the **hypothalamus** and the
**brainstem autonomic centers** for **cardiovascular** and
**gastrointestinal** regulation). The **hypothalamic-projection
neurons** (they **project to** the **hypothalamus** for
**neuroendocrine** and **thermoregulatory** regulation). **These neuron
populations are prose, not structural children.** Consumers must **not**
treat the medial parabrachial nucleus as a single uniform population —
it is a **functionally heterogeneous complex** with **distinct**
sub-circuits.
**Boundary status (SLEA-FREE — the medial parabrachial nucleus is NOT an
extended-amygdala component):** **Boundary case — the medial parabrachial
nucleus is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **medial parabrachial nucleus** is a **pontine
respiratory and autonomic-relay nucleus** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
**Unlike the lateral parabrachial nucleus** (which **projects to** the
central nucleus of the amygdala and the BNST), the **medial parabrachial
nucleus does NOT project to the SLEA** — it projects to the **ventral
respiratory group**, the **Kölliker-Fuse nucleus**, and the
**hypothalamus**. The medial parabrachial nucleus is **SLEA-FREE without
the "projects to SLEA" caveat** that applies to the lateral parabrachial
nucleus.

Overview
--------
The medial parabrachial nucleus is the **respiratory and autonomic relay**
of the **parabrachial area** — a **functionally heterogeneous**
grey-matter nucleus in the **medial parabrachial area**, medial to the
**lateral parabrachial nucleus** and dorsal to the **superior cerebellar
peduncle** in the **dorsal pons**. It is a **leaf** module under the
parabrachial_area container, and it is the **principal pontine relay**
for **respiratory afferent input** (from the solitary nucleus and the
retrotrapezoid nucleus) and **autonomic regulation** (cardiorespiratory
integration, hypothalamic relay).

**The medial parabrachial nucleus is a LEAF, not a container.** It has
**no structural children**. The **respiratory-relay neurons**,
**autonomic-relay neurons**, and **hypothalamic-projection neurons** are
**prose populations**, not structural children.

**The medial parabrachial nucleus is GREY-MATTER, NOT the superior
cerebellar peduncle.** The **superior cerebellar peduncle** (brachium
conjunctivum) is the **white-matter tract** that the medial parabrachial
nucleus is **dorsal to** — within the parabrachial area. They are
**DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**peduncle** is white matter. **This distinction is the etymological
origin of the name and is a classic source of confusion.**

**The medial parabrachial nucleus is NOT the lateral parabrachial
nucleus or the subparabrachial nucleus.** Those are **siblings** under
the parabrachial_area container — the **lateral parabrachial nucleus**
is the **visceral-sensory and pain/aversion relay**; the
**subparabrachial nucleus** is the **pontine respiratory center**
(containing the Kölliker-Fuse nucleus and the pontine respiratory group).
They are **DIFFERENT STRUCTURES** — different functional systems,
different downstream targets.

**The medial parabrachial nucleus is NOT the solitary nucleus.** The
**solitary nucleus** is the **medullary visceral-afferent hub** that
**projects to** the medial parabrachial nucleus. The medial parabrachial
nucleus is the **pontine downstream relay**.

**The medial parabrachial nucleus is NOT the retrotrapezoid nucleus, the
ventral respiratory group, or the dorsal respiratory group.** Those are
**medullary respiratory centers** that the medial parabrachial nucleus
**relays to** and **modulates** (directly for the VRG; indirectly for
the DRG via the solitary nucleus).

**The medial parabrachial nucleus is NOT the locus coeruleus.** The
**locus coeruleus** is the **noradrenergic nucleus** — it is
**anatomically adjacent** to the medial parabrachial nucleus, but it is
a **different structure**.

**The medial parabrachial nucleus is CLASSICALLY part of the pontine
respiratory group, but the tree wires the pontine respiratory group as a
child of the subparabrachial nucleus.** This is a **tree-wiring
decision**, not a claim that the medial parabrachial nucleus is not
functionally related to the pontine respiratory group. **Functionally**,
the medial parabrachial nucleus **provides afferent input to** the
Kölliker-Fuse nucleus and the pontine respiratory group. **Structurally**,
the medial parabrachial nucleus is a **sibling** of the subparabrachial
nucleus, not its **parent**.

**The medial parabrachial nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
**Unlike the lateral parabrachial nucleus** (which **projects to** the
central nucleus of the amygdala and the BNST), the **medial parabrachial
nucleus does NOT project to the SLEA** — it projects to the **ventral
respiratory group**, the **Kölliker-Fuse nucleus**, and the
**hypothalamus**.

Prose Population Composition (prose, not structural children)
--------------------------------------------------------------
The medial parabrachial nucleus contains **three functionally distinct
neuron populations** — documented as **prose**, not as structural
children:

*   **Respiratory-relay neurons** — the neurons that **receive**
    **respiratory afferents** from the **solitary nucleus** (lung stretch
    receptors, airway receptors, carotid body and aortic body
    chemoreceptors) and the **retrotrapezoid nucleus** (central
    chemoreceptors), and **project to** the **ventral respiratory
    group** (especially the **pre-Bötzinger complex**) and the
    **Kölliker-Fuse nucleus**. They **modulate** the **respiratory
    rhythm** and **respiratory phase switching**. **Respiratory relay
    and rhythm modulation are the functional systems** subserved
    primarily by the respiratory-relay neurons.

*   **Autonomic-relay neurons** — the neurons that **receive**
    **autonomic afferents** from the **solitary nucleus**
    (baroreceptors, cardiopulmonary receptors, gastrointestinal
    receptors) and **project to** the **hypothalamus** and the
    **brainstem autonomic centers** (rostral ventrolateral medulla,
    nucleus ambiguus) for **cardiovascular** and **gastrointestinal**
    regulation. **Autonomic relay and cardiorespiratory integration are
    the functional systems** subserved primarily by the autonomic-relay
    neurons.

*   **Hypothalamic-projection neurons** — the neurons that **project to**
    the **hypothalamus** (paraventricular nucleus, lateral hypothalamic
    area) for **neuroendocrine** and **thermoregulatory** regulation.
    They **mediate** the **hypothalamic** responses to **respiratory**
    and **autonomic** afferent input. **Hypothalamic relay and
    neuroendocrine regulation are the functional systems** subserved
    primarily by the hypothalamic-projection neurons.

**These populations are prose, not structural children.** The tree wires
the **medial parabrachial nucleus** as a **single leaf** under the
parabrachial_area container — the **respiratory-relay neurons**,
**autonomic-relay neurons**, and **hypothalamic-projection neurons** are
**prose**, not structural children. Consumers that need
**neuron-population-level** resolution should consult the references,
not the tree.

The Medial Parabrachial Nucleus / Lateral Parabrachial Nucleus Boundary
----------------------------------------------------------------------
This is the **sibling** boundary — **respiratory/autonomic vs.
visceral-sensory/pain/aversion**:

*   **Medial parabrachial nucleus** (this module) — the **respiratory
    and autonomic relay**.

*   **Lateral parabrachial nucleus**
    (``.../parabrachial_area/lateral_parabrachial_nucleus/``) — the
    **visceral-sensory and pain/aversion relay**.

**They are DIFFERENT STRUCTURES** — different functional systems
(respiratory/autonomic vs. visceral-sensory/pain/aversion), different
downstream targets (VRG/Kölliker-Fuse/hypothalamus vs.
amygdala/BNST/insula/hypothalamus/VPMpc/PAG). They are **anatomically
adjacent** (both are in the parabrachial area) — this proximity is a
**classic source of confusion** — consumers must **not** conflate the
medial parabrachial nucleus with the lateral parabrachial nucleus.

The Medial Parabrachial Nucleus / Subparabrachial Nucleus Boundary
-------------------------------------------------------------------
This is the **sibling** boundary — **respiratory afferent/autonomic relay
vs. respiratory rhythm/phase switching**:

*   **Medial parabrachial nucleus** (this module) — the **respiratory
    afferent and autonomic relay**.

*   **Subparabrachial nucleus**
    (``.../parabrachial_area/subparabrachial_nucleus/``) — the **pontine
    respiratory center** (containing the **Kölliker-Fuse nucleus** and
    the **pontine respiratory group**).

**They are DIFFERENT STRUCTURES** — different functional roles
(respiratory afferent/autonomic relay vs. respiratory rhythm/phase
switching), different downstream targets. **However**, they are
**functionally coupled** — the medial parabrachial nucleus **provides
afferent input to** the subparabrachial nucleus (especially the
Kölliker-Fuse nucleus). Consumers must **not** conflate the medial
parabrachial nucleus with the subparabrachial nucleus.

The Medial Parabrachial Nucleus / Kölliker-Fuse Nucleus and Pontine Respiratory Group Boundary
---------------------------------------------------------------------------------------------
This is the **structural nephew** boundary:

*   **Medial parabrachial nucleus** (this module) — the **respiratory
    and autonomic relay**.

*   **Kölliker-Fuse nucleus** and **pontine respiratory group** —
    **children** of the **subparabrachial_nucleus**, which is a
    **sibling** of the medial parabrachial nucleus.

**They are DIFFERENT STRUCTURES** — the **Kölliker-Fuse nucleus** and
the **pontine respiratory group** are **structural nephews** (siblings'
own children) of the medial parabrachial nucleus, not the medial
parabrachial nucleus itself. Consumers must **not** conflate the medial
parabrachial nucleus with the Kölliker-Fuse nucleus or the pontine
respiratory group.

The Medial Parabrachial Nucleus / Classical Pontine Respiratory Group Boundary
-----------------------------------------------------------------------------
This is the **classical functional grouping vs. tree structural wiring**
boundary:

*   **Medial parabrachial nucleus** (this module) — a **sibling** of the
    subparabrachial nucleus, structurally under the parabrachial_area
    container.

*   **Classical pontine respiratory group (PRG)** — in the **classical
    respiratory neurobiology literature**, the PRG is often defined as
    including the **Kölliker-Fuse nucleus** and the **medial parabrachial
    nucleus** (some authors) — or the **Kölliker-Fuse nucleus** and the
    **subparabrachial nucleus** (others).

**In the tree**, the **pontine respiratory group** is a **structural
child** of the **subparabrachial_nucleus**, NOT the
**medial_parabrachial_nucleus**. **Functionally**, the medial parabrachial
nucleus **provides afferent input to** the pontine respiratory group.
**Structurally**, the medial parabrachial nucleus is a **sibling** of the
subparabrachial nucleus, not its **parent**. Consumers must **not**
assume the tree's structural wiring matches the classical functional
grouping.

The Medial Parabrachial Nucleus / Superior Cerebellar Peduncle Boundary
-----------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **etymological
origin of the name**:

*   **Medial parabrachial nucleus** (this module) — the **grey-matter
    neuron cluster** that is dorsal to the superior cerebellar peduncle.

*   **Superior cerebellar peduncle** (brachium conjunctivum) — the
    **white-matter tract** that carries cerebellar efferents from the
    dentate and interposed nuclei to the red nucleus and the thalamus.

**They are DIFFERENT STRUCTURES.** The **nucleus** is grey matter; the
**peduncle** is white matter. The nucleus is **dorsal to** the peduncle;
it is **not** the peduncle. **This distinction is the etymological origin
of the name "parabrachial"** ("para-" = alongside, "brachium" = the
superior cerebellar peduncle) — and it is a **classic source of
confusion**. Consumers must **not** conflate the medial parabrachial
nucleus with the superior cerebellar peduncle.

The Medial Parabrachial Nucleus / Locus Coeruleus Boundary
-----------------------------------------------------------
This is the **anatomically adjacent** boundary — **respiratory/autonomic
relay vs. noradrenergic nucleus**:

*   **Medial parabrachial nucleus** (this module) — the **respiratory
    and autonomic relay**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic nucleus** — the **principal source of norepinephrine**
    in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, etc. vs. norepinephrine), different functional systems
(respiratory/autonomic vs. noradrenergic arousal). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the medial parabrachial
nucleus with the locus coeruleus.

The Medial Parabrachial Nucleus / Solitary Nucleus Boundary
-----------------------------------------------------------
This is the **upstream source vs. pontine relay** boundary:

*   **Medial parabrachial nucleus** (this module) — the **pontine
    respiratory and autonomic relay**.

*   **Solitary nucleus** (nucleus tractus solitarius,
    ``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``)
    — the **medullary visceral-afferent hub** for **CN VII, IX, and X**.

**The solitary nucleus is the upstream source** — it **projects to** the
medial parabrachial nucleus via the **central tegmental tract**. The
**medial parabrachial nucleus** (here) is the **pontine relay** that
**receives** the solitary nucleus respiratory and autonomic projections
and **projects** them to the **ventral respiratory group**, the
**Kölliker-Fuse nucleus**, and the **hypothalamus**. They are **DIFFERENT
STRUCTURES** — the **solitary nucleus** is **medullary** and
**upstream**; the **medial parabrachial nucleus** is **pontine** and
**downstream**. **This distinction is clinically load-bearing** — a
**solitary nucleus** lesion causes **impaired respiratory and autonomic
afferent integration**; a **medial parabrachial nucleus** lesion causes
**impaired respiratory and autonomic relay**. Consumers must **not**
conflate the medial parabrachial nucleus with the solitary nucleus.

The Medial Parabrachial Nucleus / Retrotrapezoid Nucleus Boundary
-----------------------------------------------------------------
This is the **central chemoreceptor** boundary — **upstream vs.
downstream**:

*   **Medial parabrachial nucleus** (this module) — the **pontine
    respiratory relay**.

*   **Retrotrapezoid nucleus (RTN)**
    (``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
    — the **medullary central chemoreceptor**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine relay vs. medullary
chemoreception). The RTN **projects to** the medial parabrachial nucleus
(among other targets), and the medial parabrachial nucleus **relays** the
RTN input to the **ventral respiratory group** and the **Kölliker-Fuse
nucleus**. **This distinction is clinically load-bearing** — an **RTN**
lesion causes **central hypoventilation** (loss of CO₂ chemoreception); a
**medial parabrachial nucleus** lesion causes **respiratory rhythm
dysregulation** without loss of chemoreception. Consumers must **not**
conflate the medial parabrachial nucleus with the retrotrapezoid nucleus.

The Medial Parabrachial Nucleus / Ventral Respiratory Group Boundary
--------------------------------------------------------------------
This is the **pontine relay vs. medullary pattern generator** boundary:

*   **Medial parabrachial nucleus** (this module) — the **pontine
    respiratory relay**.

*   **Ventral respiratory group (VRG)**
    (``.../medulla_oblongata/ventral_respiratory_group/``) — the
    **medullary respiratory pattern generator**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine relay vs. medullary rhythm
generation). The medial parabrachial nucleus **projects to** the VRG
(especially the **pre-Bötzinger complex**) and **modulates** the
respiratory rhythm. Consumers must **not** conflate the medial
parabrachial nucleus with the ventral respiratory group.

The Medial Parabrachial Nucleus / Dorsal Respiratory Group Boundary
-------------------------------------------------------------------
This is the **pontine relay vs. medullary inspiratory center** boundary:

*   **Medial parabrachial nucleus** (this module) — the **pontine
    respiratory relay**.

*   **Dorsal respiratory group (DRG)**
    (``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
    — the **medullary inspiratory center**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine modulation vs. medullary
inspiratory drive). The medial parabrachial nucleus **modulates** the DRG
(indirectly, via the VRG and the Kölliker-Fuse nucleus) for **respiratory
phase switching**. Consumers must **not** conflate the medial
parabrachial nucleus with the dorsal respiratory group.

The Medial Parabrachial Nucleus / Paramedian Pontine Reticular Formation Boundary
--------------------------------------------------------------------------------
This is the **horizontal-gaze** boundary:

*   **Medial parabrachial nucleus** (this module) — the **respiratory and
    autonomic relay**.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/paramedian_pontine_reticular_formation/``) — the
    **horizontal saccadic burst generator**.

**They are DIFFERENT STRUCTURES** — different functional systems
(horizontal gaze vs. respiratory/autonomic). Consumers must **not**
conflate the medial parabrachial nucleus with the PPRF.

The Medial Parabrachial Nucleus / Pontine Nuclei Boundary
---------------------------------------------------------
This is the **basilar-pons vs. dorsal-tegmentum** boundary:

*   **Medial parabrachial nucleus** (this module) — the **dorsal
    tegmental** respiratory and autonomic-relay nucleus.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/left/`` and
    ``.../right/``) — the **cortico-ponto-cerebellar relay** in the
    **basilar pons**.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. respiratory/autonomic). Consumers must
**not** conflate the medial parabrachial nucleus with the pontine
nuclei.

The Medial Parabrachial Nucleus / Pons Boundary
-----------------------------------------------
This is the **leaf vs. great-grandparent** boundary:

*   **Medial parabrachial nucleus** (this module) — the **respiratory
    and autonomic-relay** component of the parabrachial area only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal /
    corticobulbar tracts**, the **middle cerebellar peduncle**, the
    **cranial-nerve nuclei**, and the **parabrachial area**.

**The medial parabrachial nucleus is a great-grandchild of the pons**
(via parabrachial_area). Consumers must **not** conflate the medial
parabrachial nucleus with the **whole pons**.

The Medial Parabrachial Nucleus / SLEA Boundary
-----------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Medial parabrachial nucleus** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The medial parabrachial nucleus is NOT part of the SLEA continuum.**
It is a **pontine respiratory and autonomic-relay nucleus**, and it
carries **no SLEA warning**. **Unlike the lateral parabrachial nucleus**
(which **projects to** the central nucleus of the amygdala and the BNST),
the **medial parabrachial nucleus does NOT project to the SLEA** — it
projects to the **ventral respiratory group**, the **Kölliker-Fuse
nucleus**, and the **hypothalamus**. The medial parabrachial nucleus is
**SLEA-FREE without the "projects to SLEA" caveat** that applies to the
lateral parabrachial nucleus.

Function in the Human Brain
---------------------------
The medial parabrachial nucleus's functions are **the pontine relay for
respiratory afferent input and autonomic regulation** — **NOT a single
unified function**:

*   **Respiratory Afferent Relay (Respiratory-Relay Neurons):** The
    **respiratory-relay neurons** **receive** the **respiratory
    afferents** from the **solitary nucleus** (lung stretch receptors,
    airway receptors, carotid body and aortic body chemoreceptors) and
    the **retrotrapezoid nucleus** (central chemoreceptors) and
    **project to** the **ventral respiratory group** (especially the
    **pre-Bötzinger complex**) and the **Kölliker-Fuse nucleus**. They
    **modulate** the **respiratory rhythm** and **respiratory phase
    switching** — they are the **pontine relay** that **integrates**
    the **peripheral and central chemoreceptor** and **mechanoreceptor**
    inputs and **relays** them to the **medullary respiratory centers**.

*   **Autonomic Regulation (Autonomic-Relay Neurons):** The
    **autonomic-relay neurons** **receive** the **autonomic afferents**
    from the **solitary nucleus** (baroreceptors, cardiopulmonary
    receptors, gastrointestinal receptors) and **project to** the
    **hypothalamus** and the **brainstem autonomic centers** (rostral
    ventrolateral medulla, nucleus ambiguus) for **cardiovascular** and
    **gastrointestinal** regulation. They **mediate** the **autonomic**
    and **neuroendocrine** responses to **visceral afferent input**.

*   **Hypothalamic Relay (Hypothalamic-Projection Neurons):** The
    **hypothalamic-projection neurons** **project to** the
    **hypothalamus** (paraventricular nucleus, lateral hypothalamic area)
    for **neuroendocrine** and **thermoregulatory** regulation. They
    **mediate** the **hypothalamic** responses to **respiratory** and
    **autonomic** afferent input.

*   **NOT a neural processor in the classical sense.** The medial
    parabrachial nucleus is a **relay complex** — it **receives**
    ascending respiratory and autonomic afferents and **projects** them
    to the **medullary respiratory centers** (VRG, Kölliker-Fuse) and the
    **hypothalamus**. The **processing** of these signals happens in the
    **solitary nucleus** (visceral afferent integration), the **medial
    parabrachial nucleus** (pontine relay), the **medullary respiratory
    centers** (rhythm generation and phase switching), and the
    **hypothalamus** (autonomic and neuroendocrine regulation).

**The unifying theme:** the medial parabrachial nucleus is the **pontine
respiratory and autonomic relay** — the **principal pontine relay** for
**respiratory afferent input** and **autonomic regulation**. It is
**functionally heterogeneous** (respiratory-relay, autonomic-relay, and
hypothalamic-projection neurons), **SLEA-FREE** (and does **not** project
to the SLEA, unlike the lateral parabrachial nucleus), and **NOT the
superior cerebellar peduncle** — the **peduncle** is the white-matter
tract that the nucleus is **dorsal to**.

Associated Disorders
--------------------
The medial parabrachial nucleus has **no named "medial parabrachial
nucleus syndrome"** — its clinical associations are **neuron-population-
specific**:

*   **Respiratory-Relay Neuron Dysfunction — Respiratory Rhythm
    Dysregulation:** A lesion or dysfunction of the **respiratory-relay
    neurons** in the **medial parabrachial nucleus** causes **respiratory
    rhythm dysregulation** — **impaired respiratory phase switching**,
    **apneustic breathing** (prolonged inspiratory pauses), and
    **impaired integration** of **peripheral and central chemoreceptor**
    and **mechanoreceptor** inputs. **This is a critical clinical
    entity** — the **respiratory-relay neurons** are the **neural
    substrate** of the **pontine modulation** of the **medullary
    respiratory rhythm**, and their dysfunction is implicated in
    **central sleep apnea** and **respiratory rhythm disorders**.

*   **Autonomic-Relay Neuron Dysfunction — Cardiovascular and
    Gastrointestinal Dysregulation:** A lesion or dysfunction of the
    **autonomic-relay neurons** in the **medial parabrachial nucleus**
    causes **cardiovascular dysregulation** (impaired baroreceptor
    reflex, impaired cardiopulmonary integration) and **gastrointestinal
    dysregulation** (impaired gastrointestinal motility). **This is a
    critical clinical entity** — the **autonomic-relay neurons** are the
    **neural substrate** of the **pontine relay** of **autonomic
    afferent input**, and their dysfunction is implicated in
    **autonomic dysregulation syndromes**.

*   **Hypothalamic-Projection Neuron Dysfunction — Neuroendocrine and
    Thermoregulatory Dysregulation:** A lesion or dysfunction of the
    **hypothalamic-projection neurons** in the **medial parabrachial
    nucleus** causes **neuroendocrine dysregulation** (impaired
    hypothalamic-pituitary-adrenal axis responses, impaired
    hypothalamic-pituitary-thyroid axis responses) and **thermoregulatory
    dysregulation** (impaired hypothalamic thermoregulatory responses).
    **This is a critical clinical entity** — the **hypothalamic-
    projection neurons** are the **neural substrate** of the **pontine
    relay** of **respiratory and autonomic afferent input** to the
    **hypothalamus**, and their dysfunction is implicated in
    **neuroendocrine and thermoregulatory disorders**.

*   **Medial Parabrachial Nucleus Lesion — Pan-Modal Respiratory and
    Autonomic Deficits:** A lesion of the **medial parabrachial nucleus**
    (e.g. **pontine stroke**, **tumor**, **demyelination**) causes
    **pan-modal deficits** — **respiratory rhythm dysregulation**,
    **cardiovascular dysregulation**, **gastrointestinal dysregulation**,
    and **neuroendocrine dysregulation**. **The pan-modal pattern** is
    the **substrate** of the **respiratory and autonomic** functions of
    the medial parabrachial nucleus.

*   **Central Sleep Apnea — Medial Parabrachial Nucleus Involvement:**
    **Central sleep apnea** is a **respiratory disorder** characterized
    by **absent respiratory effort** during sleep — it is caused by
    **dysfunction** of the **central respiratory control network**,
    including the **medial parabrachial nucleus**, the **Kölliker-Fuse
    nucleus**, the **retrotrapezoid nucleus**, and the **medullary
    respiratory centers**. **The medial parabrachial nucleus** is **one
    of the neural substrates** of **central respiratory control**, and
    its dysfunction may **contribute** to **central sleep apnea**.

*   **Sudden Infant Death Syndrome (SIDS) — Medial Parabrachial Nucleus
    Involvement:** **SIDS** is a **sudden unexplained death** of an
    infant during sleep — it has been **associated** with **abnormalities**
    in the **medullary and pontine respiratory and autonomic control
    network**, including the **medial parabrachial nucleus** (reduced
    **serotonin** and **glutamate** markers, reduced **neurokinin-1**
    receptor binding). **The medial parabrachial nucleus** is **one of
    the neural substrates** of **cardiorespiratory integration**, and its
    dysfunction may **contribute** to **SIDS**.

*   **Congenital Central Hypoventilation Syndrome (CCHS) — Medial
    Parabrachial Nucleus Involvement:** **CCHS** is a **congenital
    respiratory disorder** characterized by **failure of automatic
    control of breathing** — it is caused by **PHOX2B** mutations, which
    affect the **autonomic nervous system** and the **brainstem
    respiratory and autonomic control network**, including the **medial
    parabrachial nucleus**. **The medial parabrachial nucleus** is **one
    of the neural substrates** of **central respiratory control**, and its
    dysfunction may **contribute** to **CCHS**.

*   **No Named "Medial Parabrachial Nucleus Syndrome":** The medial
    parabrachial nucleus is a **functionally heterogeneous complex** — it
    has **no named clinical syndrome**. Its clinical relevance is
    **neuron-population-specific** — **respiratory-relay neurons**
    (respiratory rhythm), **autonomic-relay neurons** (cardiovascular and
    gastrointestinal regulation), **hypothalamic-projection neurons**
    (neuroendocrine and thermoregulatory regulation).

**What is NOT here:** The medial parabrachial nucleus is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), or **trigeminal neuralgia** (trigeminal nerve root). Its
clinical relevance is **respiratory-autonomic-specific**, via the
**respiratory-relay**, **autonomic-relay**, and **hypothalamic-projection**
neurons it subserves. **No named medial parabrachial nucleus syndrome
exists.**

Lateralization Notes
--------------------
This is the **single** medial parabrachial nucleus module. The medial
parabrachial nuclei are **bilateral in real anatomy** (left and right
within the parabrachial area), but the tree wires them as a **single
module** — and the module carries **NO warning at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **medial_parabrachial_nucleus** module (here) is a **single module**
    that represents the **bilateral medial parabrachial nuclei**. The
    tree does **not** split them into left/right. Consumers must **not**
    assume a left/right split exists at the tree level — the module is a
    **single, bilateral-container representation**.

*   **Bilateral Respiratory and Autonomic Input (Structural Fact, NOT a
    Lateralization Warning):** The **medial parabrachial nucleus**
    **receives** respiratory and autonomic afferents from the
    **solitary nucleus** and the **retrotrapezoid nucleus** — the
    projections are **largely bilateral** (each medial parabrachial
    nucleus receives input from both left and right solitary nucleus and
    retrotrapezoid nucleus). This **bilateral input** is a **structural
    fact** of the **respiratory and autonomic afferent system** — it is
    **not** a functional lateralization. It is the **neural substrate**
    of the **bilateral integration** of respiratory and autonomic
    signals.

*   **Bilateral Projections to Medullary Respiratory Centers and
    Hypothalamus (Structural Fact, NOT a Lateralization Warning):** The
    **medial parabrachial nucleus** **projects** to the **ventral
    respiratory group**, the **Kölliker-Fuse nucleus**, and the
    **hypothalamus** — **bilaterally** (from both left and right medial
    parabrachial nuclei). This **bilateral projection** is a
    **structural fact** of the **respiratory and autonomic relay
    system** — it is **not** a functional lateralization. It is the
    **neural substrate** of the **bilateral modulation** of respiratory
    rhythm and autonomic regulation.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The medial
    parabrachial nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the medial
    parabrachial nucleus. **Unlike the lateral parabrachial nucleus**
    (which **projects to** the central nucleus of the amygdala and the
    BNST), the **medial parabrachial nucleus does NOT project to the
    SLEA** — it projects to the **ventral respiratory group**, the
    **Kölliker-Fuse nucleus**, and the **hypothalamus**. The medial
    parabrachial nucleus is **SLEA-FREE without the "projects to SLEA"
    caveat**.

*   **NO Amygdala-Lateralization Warning of their own (the medial
    parabrachial nucleus is RESPIRATORY/AUTONOMIC, not the fear-output):**
    The **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The medial parabrachial
    nucleus is a **pontine respiratory and autonomic-relay nucleus** —
    consumers must **not** conflate it with the **amygdala** or with the
    **fear circuit**.

**A consumer that sees "medial_parabrachial_nucleus" must understand
that the module is a SINGLE, BILATERAL-CONTAINER representation** — it
is **not** a left/right split at the tree level. The **bilateral
respiratory and autonomic input** and the **bilateral projections to
medullary respiratory centers and hypothalamus** are **structural
facts**, not lateralizations. The medial parabrachial nucleus is a
**strict-single module with NO warning at the module level** — **no SLEA
warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** medial parabrachial nuclei as a **single module** — it
    does **not** import left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../parabrachial_area/lateral_parabrachial_nucleus/``,
    ``.../parabrachial_area/subparabrachial_nucleus/``,
    ``.../pons/tegmentum/``, ``.../medulla_oblongata/``,
    ``.../midbrain/``, ``.../diencephalon/``, or any other container. The
    medial parabrachial nucleus's relationships to the **lateral
    parabrachial nucleus**, the **subparabrachial nucleus**, the
    **Kölliker-Fuse nucleus**, the **pontine respiratory group**, the
    **classical pontine respiratory group**, the **superior cerebellar
    peduncle**, the **locus coeruleus**, the **solitary nucleus**, the
    **retrotrapezoid nucleus**, the **ventral respiratory group**, the
    **dorsal respiratory group**, the **PPRF**, the **pontine nuclei**,
    the **pons**, and the **SLEA continuum** are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **respiratory-relay
    neurons**, **autonomic-relay neurons**, and **hypothalamic-projection
    neurons** are documented as **prose**, not as sub-modules. Consumers
    must not assume any exist as children; resolve neuron-population-level
    detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **medial parabrachial nucleus** is a **single module** that represents
    the **bilateral medial parabrachial nuclei** — the tree does **not**
    split them into left/right. Consumers must **not** assume a
    left/right split exists at the tree level.
*   **CLASSICAL FUNCTIONAL GROUPING vs. TREE STRUCTURAL WIRING — the
    medial parabrachial nucleus is CLASSICALLY part of the pontine
    respiratory group, but the tree wires the pontine respiratory group
    as a child of the subparabrachial nucleus.** **Functionally**, the
    medial parabrachial nucleus **provides afferent input to** the
    pontine respiratory group. **Structurally**, the medial parabrachial
    nucleus is a **sibling** of the subparabrachial nucleus, not its
    **parent**. Consumers must **not** assume the tree's structural
    wiring matches the classical functional grouping.
*   **FUNCTIONALLY HETEROGENEOUS — MULTIPLE neuron populations, not a
    single uniform nucleus.** The **respiratory-relay neurons**
    (respiratory afferent integration), **autonomic-relay neurons**
    (cardiovascular and gastrointestinal regulation), and
    **hypothalamic-projection neurons** (neuroendocrine and
    thermoregulatory regulation) are **prose**, not structural children.
    Consumers must **not** treat the medial parabrachial nucleus as a
    single uniform population.
*   **SLEA-FREE — no extended-amygdala relationship.** The medial
    parabrachial nucleus is **not** an extended-amygdala component, and
    it carries **no SLEA warning**. **Unlike the lateral parabrachial
    nucleus** (which **projects to** the central nucleus of the amygdala
    and the BNST), the **medial parabrachial nucleus does NOT project to
    the SLEA** — it projects to the **ventral respiratory group**, the
    **Kölliker-Fuse nucleus**, and the **hypothalamus**. The medial
    parabrachial nucleus is **SLEA-FREE without the "projects to SLEA"
    caveat**.
*   **NOT the fear-output — the medial parabrachial nucleus is
    RESPIRATORY/AUTONOMIC RELAY.** The **fear-output** structure is the
    **central nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**; the **fear-modulatory / extinction**
    structures are the **basomedial nuclei**. The **medial parabrachial
    nucleus** is a **pontine respiratory and autonomic-relay nucleus** —
    it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The medial parabrachial nucleus is a local
    leaf under the parabrachial_area container, not a cross-listed leaf.
*   **No nested cross-listing.** The medial parabrachial nucleus has no
    nested dual-framing module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area import medial_parabrachial_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "medial_parabrachial_nucleus"
    )

**Do not** assume the medial parabrachial nucleus is a **container**. It
is a **leaf** — its **respiratory-relay neurons**, **autonomic-relay
neurons**, and **hypothalamic-projection neurons** are **prose**, not
structural children.

**Do not** assume the medial parabrachial nucleus is **bilateralized at
the tree level**. The medial parabrachial nuclei are **bilateral in real
anatomy**, but the tree wires them as a **single module** — there is **no
left/right split**.

**Do not** assume the medial parabrachial nucleus is the **superior
cerebellar peduncle**. The **superior cerebellar peduncle** is the
**white-matter tract** that the medial parabrachial nucleus is **dorsal
to** — the "para-brachial" name reflects this **flanking/dorsal
relationship**, not identity. They are **different structures**.

**Do not** assume the medial parabrachial nucleus is the **lateral
parabrachial nucleus** or the **subparabrachial nucleus**. Those are
**siblings** under the parabrachial_area container — the **lateral
parabrachial nucleus** is the **visceral-sensory and pain/aversion
relay**; the **subparabrachial nucleus** is the **pontine respiratory
center**. They are **different structures**.

**Do not** assume the medial parabrachial nucleus is the **Kölliker-Fuse
nucleus** or the **pontine respiratory group**. Those are **structural
nephews** (children of the subparabrachial nucleus, which is a sibling of
the medial parabrachial nucleus).

**Do not** assume the tree's structural wiring matches the classical
functional grouping of the **pontine respiratory group** — in the
classical literature, the pontine respiratory group may include the
medial parabrachial nucleus; in the tree, the pontine respiratory group
is wired as a child of the **subparabrachial nucleus**, NOT the medial
parabrachial nucleus. **Functionally**, the medial parabrachial nucleus
**provides afferent input to** the pontine respiratory group.
**Structurally**, it is a **sibling** of the subparabrachial nucleus.

**Do not** assume the medial parabrachial nucleus is the **locus
coeruleus**. The **locus coeruleus** is the **noradrenergic nucleus** in
the **pontine tegmentum** — it is **anatomically adjacent** to the medial
parabrachial nucleus, but it is a **different structure**.

**Do not** assume the medial parabrachial nucleus is the **solitary
nucleus**. The **solitary nucleus** is the **medullary visceral-afferent
hub** that **projects to** the medial parabrachial nucleus.

**Do not** assume the medial parabrachial nucleus is the
**retrotrapezoid nucleus**, the **ventral respiratory group**, or the
**dorsal respiratory group**. Those are **medullary respiratory centers**
that the medial parabrachial nucleus **relays to** and **modulates**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the medial parabrachial nucleus. **The medial parabrachial
nucleus is SLEA-FREE** — it is **not** an extended-amygdala component, and
it is **NOT part of the fear circuit**. **Unlike the lateral parabrachial
nucleus**, the medial parabrachial nucleus **does NOT project to the
SLEA**.

Iterating the medial parabrachial nucleus's (empty) children (recommended
consumer pattern)::

    MEDIAL_PARABRACHIAL_NUCLEUS_CHILDREN = ()
    # The medial parabrachial nucleus is a leaf. The respiratory-relay
    # neurons, autonomic-relay neurons, and hypothalamic-projection
    # neurons are prose, not modules.

Reaching the lateral parabrachial nucleus (recommended consumer pattern —
the sibling)::

    # The lateral parabrachial nucleus is the VISCERAL-SENSORY AND
    # PAIN/AVERSION sibling under the parabrachial_area container:
    #
    #   .../parabrachial_area/lateral_parabrachial_nucleus/
    #
    # The medial parabrachial nucleus is the RESPIRATORY AND AUTONOMIC
    # sibling — different functional system, different downstream
    # targets.

Reaching the subparabrachial nucleus (recommended consumer pattern — the
sibling)::

    # The subparabrachial nucleus is the PONTINE RESPIRATORY CENTER
    # sibling under the parabrachial_area container:
    #
    #   .../parabrachial_area/subparabrachial_nucleus/
    #
    # The medial parabrachial nucleus is the RESPIRATORY AND AUTONOMIC
    # relay sibling — different functional role (afferent relay and
    # autonomic integration vs. respiratory rhythm generation and phase
    # switching).

Reaching the Kölliker-Fuse nucleus and pontine respiratory group
(recommended consumer pattern — the structural nephews)::

    # The Kölliker-Fuse nucleus and the pontine respiratory group are
    # STRUCTURAL NEPHEWS (children of the subparabrachial nucleus,
    # which is a sibling of the medial parabrachial nucleus):
    #
    #   .../parabrachial_area/subparabrachial_nucleus/kolliker_fuse_nucleus/
    #   .../parabrachial_area/subparabrachial_nucleus/pontine_respiratory_group/
    #
    # They are NOT the medial parabrachial nucleus — they are its
    # structural nephews. FUNCTIONALLY, the medial parabrachial nucleus
    # provides afferent input to the Kölliker-Fuse nucleus.

Reaching the superior cerebellar peduncle (recommended consumer pattern —
the white-matter tract the nucleus is DORSAL to)::

    # The superior cerebellar peduncle (brachium conjunctivum) is the
    # WHITE-MATTER tract that the medial parabrachial nucleus is DORSAL
    # to:
    #
    #   .../white_matter/.../superior_cerebellar_peduncle/  (or equivalent path)
    #
    # The medial parabrachial nucleus is GREY MATTER that is dorsal to
    # the peduncle; the peduncle is WHITE MATTER that connects the
    # cerebellum to the midbrain and thalamus. They are DIFFERENT
    # STRUCTURES — the anatomical juxtaposition is the etymological
    # origin of the name "para-brachial" and is a classic source of
    # confusion.

Reaching the locus coeruleus (recommended consumer pattern — the adjacent
noradrenergic nucleus)::

    # The locus coeruleus is the NORADRENERGIC nucleus in the pontine
    # tegmentum — it is ANATOMICALLY ADJACENT to the medial parabrachial
    # nucleus, but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic (source of norepinephrine);
    # the medial parabrachial nucleus is glutamatergic (respiratory and
    # autonomic relay). They are ANATOMICALLY ADJACENT but FUNCTIONALLY
    # DISTINCT.

Reaching the solitary nucleus (recommended consumer pattern — the
UPSTREAM source)::

    # The solitary nucleus (nucleus tractus solitarius) is the MEDULLARY
    # visceral-afferent hub that PROJECTS TO the medial parabrachial
    # nucleus:
    #
    #   .../medulla_oblongata/solitary_nucleus/left/  (and right/)
    #
    # The solitary nucleus is UPSTREAM; the medial parabrachial nucleus
    # is DOWNSTREAM. They are DIFFERENT STRUCTURES.

Reaching the retrotrapezoid nucleus (recommended consumer pattern — the
MEDULLARY CENTRAL CHEMORECEPTOR)::

    # The retrotrapezoid nucleus is the MEDULLARY central chemoreceptor
    # that PROJECTS TO the medial parabrachial nucleus:
    #
    #   .../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/
    #
    # The retrotrapezoid nucleus is the MEDULLARY central chemoreceptor
    # (senses CO2/pH); the medial parabrachial nucleus is the PONTINE
    # respiratory relay. They are DIFFERENT STRUCTURES.

Reaching the ventral respiratory group (recommended consumer pattern —
the MEDULLARY RESPIRATORY PATTERN GENERATOR)::

    # The ventral respiratory group (VRG) is the MEDULLARY respiratory
    # pattern generator that RECEIVES the medial parabrachial nucleus
    # projections:
    #
    #   .../medulla_oblongata/ventral_respiratory_group/
    #
    # The medial parabrachial nucleus PROJECTS TO the VRG; the VRG is a
    # DOWNSTREAM target. They are DIFFERENT STRUCTURES.

Reaching the dorsal respiratory group (recommended consumer pattern —
the MEDULLARY INSPIRATORY CENTER)::

    # The dorsal respiratory group (DRG) is the MEDULLARY inspiratory
    # center that the medial parabrachial nucleus MODULATES (indirectly,
    # via the VRG and the Kölliker-Fuse nucleus):
    #
    #   .../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/
    #
    # The medial parabrachial nucleus MODULATES the DRG; they are
    # DIFFERENT STRUCTURES.

Reaching the hypothalamus (recommended consumer pattern — the
DIENCEPHALIC target)::

    # The hypothalamus is a DIENCEPHALIC target of the medial parabrachial
    # nucleus:
    #
    #   .../diencephalon/hypothalamus/
    #
    # The medial parabrachial nucleus PROJECTS TO the hypothalamus for
    # neuroendocrine and thermoregulatory regulation; the hypothalamus is
    # a DOWNSTREAM target.

Bilateral iteration (recommended consumer pattern)::

    # The medial parabrachial nucleus is a SINGLE module (not
    # bilateralized at the tree level). The module represents the
    # BILATERAL medial parabrachial nuclei.
    medial_pb_path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "medial_parabrachial_nucleus"
    )
    # resolve medial_pb_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The medial parabrachial nucleus's neuron populations are prose, not
    # modules:
    #   respiratory-relay neurons    -> respiratory afferent input from
    #                                    solitary nucleus and
    #                                    retrotrapezoid nucleus; projects
    #                                    to VRG and Kölliker-Fuse;
    #                                    modulates respiratory rhythm and
    #                                    phase switching
    #   autonomic-relay neurons      -> autonomic afferent input from
    #                                    solitary nucleus (baroreceptors,
    #                                    cardiopulmonary, GI); projects
    #                                    to hypothalamus and brainstem
    #                                    autonomic centers; cardiovascular
    #                                    and GI regulation
    #   hypothalamic-projection      -> projects to hypothalamus
    #   neurons                        (paraventricular nucleus, lateral
    #                                    hypothalamic area);
    #                                    neuroendocrine and
    #                                    thermoregulatory regulation
    #
    # Do not attempt to resolve these as sub-paths of the medial
    # parabrachial nucleus — resolve them at the neuron-population level
    # through the references.

References
----------
*   **Canonical medial parabrachial nucleus anatomy:** Saper, C.B.,
    Loewy, A.D. (1980). "Efferent connections of the parabrachial nucleus
    in the rat." *Brain Research* 197:291–317. (Medial parabrachial
    nucleus efferents — the definitive early mapping.)
*   **Parabrachial area — review:** Saper, C.B. (2002). "The central
    autonomic nervous system: conscious visceral perception and autonomic
    function." *Annual Review of Neuroscience* 25:433–469. (Medial
    parabrachial nucleus as the pontine respiratory and autonomic relay.)
*   **Respiratory relay:** Herbert, H., Moga, M.M., Saper, C.B. (1990).
    "Connections of the parabrachial nucleus with the nucleus of the
    solitary tract and the medullary reticular formation in the rat."
    *Journal of Comparative Neurology* 293:540–580. (Medial parabrachial
    nucleus respiratory afferents from the solitary nucleus.)
*   **Pontine respiratory group — review:** Alheid, G.F., McCrimmon,
    D.R. (2008). "The chemical neuroanatomy of breathing." *Respiratory
    Physiology & Neurobiology* 164:3–11. (Medial parabrachial nucleus and
    the pontine respiratory group.)
*   **Kölliker-Fuse nucleus:** Dutschmann, M., Herbert, H. (2006). "The
    Kölliker-Fuse nucleus gates the postinspiratory phase of the
    respiratory cycle to control inspiratory off-switch and upper airway
    resistance in rat." *European Journal of Neuroscience* 24:1071–1084.
    (Kölliker-Fuse nucleus — respiratory phase switching; the medial
    parabrachial nucleus provides afferent input to it.)
*   **Retrotrapezoid nucleus:** Guyenet, P.G., Stornetta, R.L., Bayliss,
    D.A. (2008). "Central respiratory chemoreception." *Journal of
    Comparative Neurology* 506:788–798. (Retrotrapezoid nucleus —
    medullary central chemoreceptor; projects to the medial parabrachial
    nucleus.)
*   **Ventral respiratory group:** Feldman, J.L., Del Negro, C.A. (2006).
    "Looking for inspiration: new perspectives on respiratory rhythm."
    *Nature Reviews Neuroscience* 7:232–242. (Ventral respiratory group —
    medullary respiratory pattern generator; receives medial parabrachial
    nucleus projections.)
*   **Dorsal respiratory group:** Bianchi, A.L., Denavit-Saubié, M.,
    Champagnat, J. (1995). "Central control of breathing in mammals:
    neuronal circuitry, membrane properties, and neurotransmitters."
    *Physiological Reviews* 75:1–45. (Dorsal respiratory group —
    medullary inspiratory center; modulated by the medial parabrachial
    nucleus.)
*   **Central sleep apnea — medial parabrachial nucleus involvement:**
    Dempsey, J.A., Veasey, S.C., Morgan, B.J., O'Donnell, C.P. (2010).
    "Pathophysiology of sleep apnea." *Physiological Reviews* 90:47–112.
    (Central sleep apnea — central respiratory control network including
    the medial parabrachial nucleus.)
*   **SIDS — medial parabrachial nucleus involvement:** Paterson, D.S.,
    Trachtenberg, F.L., Thompson, E.G., et al. (2006). "Multiple
    serotonergic brainstem abnormalities in sudden infant death
    syndrome." *JAMA* 296:2124–2132. (SIDS — brainstem respiratory and
    autonomic control network including the medial parabrachial nucleus.)
*   **CCHS — medial parabrachial nucleus involvement:** Weese-Mayer,
    D.E., Berry-Kravis, E.M., Ceccherini, I., et al. (2010). "An official
    ATS clinical policy statement: congenital central hypoventilation
    syndrome." *American Journal of Respiratory and Critical Care
    Medicine* 181:626–644. (CCHS — PHOX2B mutations affecting the brainstem
    respiratory and autonomic control network including the medial
    parabrachial nucleus.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the
    medial parabrachial nucleus but functionally distinct.)
*   **Superior cerebellar peduncle (contrast — the white-matter tract the
    nucleus is DORSAL to):** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Superior cerebellar
    peduncle — brachium conjunctivum; the white-matter tract that the
    medial parabrachial nucleus is dorsal to.)
*   **Solitary nucleus (contrast — the MEDULLARY upstream source):**
    Saper, C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Solitary nucleus — the medullary
    visceral-afferent hub that projects to the medial parabrachial
    nucleus.)
*   **Classical pontine respiratory group vs. tree wiring (contrast —
    functional grouping vs. structural wiring):** Alheid, G.F.,
    McCrimmon, D.R. (2008). "The chemical neuroanatomy of breathing."
    *Respiratory Physiology & Neurobiology* 164:3–11. (Classical pontine
    respiratory group may include the medial parabrachial nucleus;
    the tree wires the pontine respiratory group as a child of the
    subparabrachial nucleus.)
*   **SLEA (contrast — the medial parabrachial nucleus is not
    included):** Alheid, G.F., Heimer, L. (1988). "New perspectives in
    basal forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA continuum
    — BNST, central nucleus, ventral pallidum, nucleus accumbens; NOT the
    medial parabrachial nucleus.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the medial parabrachial nucleus.)
*   NeuroNames — Medial parabrachial nucleus; FMA — Medial parabrachial
    nucleus.
"""