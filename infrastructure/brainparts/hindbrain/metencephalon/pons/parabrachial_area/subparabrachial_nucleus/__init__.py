"""
infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area.subparabrachial_nucleus
===============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── parabrachial_area
                ├── lateral_parabrachial_nucleus
                ├── medial_parabrachial_nucleus
                └── subparabrachial_nucleus   <-- THIS MODULE
                    ├── kolliker_fuse_nucleus
                    └── pontine_respiratory_group

**Primary synonym:** Subparabrachial nucleus; subparabrachial subnucleus;
SPS; SPSN; "the pontine respiratory center" (in the classical
respiratory neurobiology literature).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter sub-container** — a **respiratory- and
autonomically-organized** collection of neuron clusters in the **ventral
parabrachial area**, ventral to the **medial parabrachial nucleus** and
dorsal to the **superior cerebellar peduncle** in the **dorsal pons**,
beneath the **floor of the fourth ventricle**. It is the **pontine
respiratory center** — the **principal pontine respiratory rhythm
modulator** and **cardiorespiratory integration** node.
**Part of:** The **parabrachial_area** container — specifically, the
**pontine respiratory** component. The **parabrachial area** is the
**dorsal tegmental visceral-sensory and respiratory-relay complex** of the
**pons**.
**Structural parent:** ``.../parabrachial_area/`` → **direct child** of
the parabrachial_area container.
**Structural children:** **Two structural children** — the
``kolliker_fuse_nucleus`` (the **Kölliker-Fuse nucleus** — the **pontine
respiratory rhythm modulator**) and the ``pontine_respiratory_group``
(the **pontine respiratory group** — the **broader functional concept**
that includes the Kölliker-Fuse nucleus and the adjacent subparabrachial
neurons).
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
subparabrachial nucleus is a CONTAINER, not a leaf.** It has **two
structural children** (``kolliker_fuse_nucleus`` and
``pontine_respiratory_group``). Consumers must **not** treat the
subparabrachial nucleus as a leaf, and must **not** assume the two
sub-nuclei are absent — they are its **direct structural children**.
**Boundary status (NOT the lateral parabrachial nucleus — that is a
SIBLING):** **Boundary case — the subparabrachial nucleus is NOT the
lateral parabrachial nucleus; the lateral parabrachial nucleus is a
SIBLING under the parabrachial_area container.** The **lateral
parabrachial nucleus**
(``.../parabrachial_area/lateral_parabrachial_nucleus/``) is the
**visceral-sensory and pain/aversion relay**. The **subparabrachial
nucleus** (here) is the **pontine respiratory center** — the
**respiratory rhythm modulator**. They are **DIFFERENT STRUCTURES** —
different functional systems (visceral-sensory/pain/aversion vs.
respiratory rhythm), different downstream targets
(amygdala/BNST/insula/hypothalamus/VPMpc/PAG vs.
VRG/DRG/hypothalamus). They are **anatomically adjacent** (both are in
the parabrachial area) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the subparabrachial
nucleus with the lateral parabrachial nucleus.
**Boundary status (NOT the medial parabrachial nucleus — that is a
SIBLING):** **Boundary case — the subparabrachial nucleus is NOT the
medial parabrachial nucleus; the medial parabrachial nucleus is a
SIBLING under the parabrachial_area container.** The **medial
parabrachial nucleus**
(``.../parabrachial_area/medial_parabrachial_nucleus/``) is the
**respiratory and autonomic relay** — it **receives** respiratory
afferents from the **solitary nucleus** and the **retrotrapezoid
nucleus** and **projects to** the **ventral respiratory group** and the
**Kölliker-Fuse nucleus**. The **subparabrachial nucleus** (here) is
the **pontine respiratory center** — it **contains** the
**Kölliker-Fuse nucleus** and the **pontine respiratory group** and
**modulates** the **medullary respiratory centers** (DRG and VRG). They
are **DIFFERENT STRUCTURES** — different functional roles (afferent
relay and autonomic integration vs. respiratory rhythm modulation and
phase switching), different downstream targets. **However**, they are
**functionally coupled** — the medial parabrachial nucleus **provides
afferent input to** the subparabrachial nucleus (especially the
Kölliker-Fuse nucleus). Consumers must **not** conflate the
subparabrachial nucleus with the medial parabrachial nucleus.
**Boundary status (CONTAINS the Kölliker-Fuse nucleus and the pontine
respiratory group — those are STRUCTURAL CHILDREN):** **Boundary case —
the subparabrachial nucleus CONTAINS the Kölliker-Fuse nucleus and the
pontine respiratory group; those are its STRUCTURAL CHILDREN.** The
**Kölliker-Fuse nucleus** and the **pontine respiratory group** are
**children** of the **subparabrachial_nucleus** — they are **not** the
subparabrachial nucleus itself. The **Kölliker-Fuse nucleus** is the
**principal pontine respiratory rhythm modulator**; the **pontine
respiratory group** is the **broader functional concept** that includes
the **Kölliker-Fuse nucleus** and the **adjacent subparabrachial
neurons**. Consumers must **not** conflate the subparabrachial nucleus
with the Kölliker-Fuse nucleus or the pontine respiratory group.
**Boundary status (CLASSICAL FUNCTIONAL GROUPING vs. TREE STRUCTURAL
WIRING — the subparabrachial nucleus is the PARENT of the pontine
respiratory group in the tree, but some classical literature treats
the pontine respiratory group as a sibling-level concept):** **Boundary
case — in the TREE, the subparabrachial nucleus is the PARENT of the
pontine respiratory group; in SOME classical respiratory neurobiology
literature, the pontine respiratory group is a SIBLING-LEVEL concept
that includes both the Kölliker-Fuse nucleus and the medial
parabrachial nucleus.** The tree wires the **pontine respiratory
group** as a **structural child** of the **subparabrachial_nucleus**.
Some classical literature treats the **pontine respiratory group** as
a **functional grouping** that includes the **Kölliker-Fuse nucleus**
and the **medial parabrachial nucleus** (or, alternatively, the
**Kölliker-Fuse nucleus** and the **subparabrachial nucleus**). This is
a **tree-wiring decision**, not a claim that the classical functional
grouping is wrong. **Functionally**, the subparabrachial nucleus
**contains** the Kölliker-Fuse nucleus and the pontine respiratory
group; the **medial parabrachial nucleus provides afferent input to**
them. **Structurally**, the tree wires the pontine respiratory group as
a child of the subparabrachial nucleus (matching the **structural**
relationship). Consumers must **not** assume the tree's structural
wiring matches every classical functional grouping.
**Boundary status (GREY-MATTER NUCLEI — NOT the superior cerebellar
peduncle):** **Boundary case — the subparabrachial nucleus is the
GREY-MATTER NUCLEI, NOT the superior cerebellar peduncle.** The
**superior cerebellar peduncle** (the "brachium conjunctivum") is the
**white-matter tract** that carries **cerebellar efferents** from the
**dentate nucleus** and the **interposed nucleus** to the **red
nucleus** and the **thalamus**. The **subparabrachial nucleus** (here)
is the **grey-matter neuron cluster** that is **dorsal** to the
superior cerebellar peduncle — within the **parabrachial area** (the
collection of nuclei flanking the brachium). They are **DIFFERENT
STRUCTURES** — the **nucleus** is grey matter; the **peduncle** is
white matter. **This distinction is the etymological origin of the
"parabrachial" name and is a classic source of confusion** — consumers
must **not** conflate the subparabrachial nucleus with the superior
cerebellar peduncle.
**Boundary status (NOT the locus coeruleus — that is the adjacent
noradrenergic nucleus):** **Boundary case — the subparabrachial nucleus
is NOT the locus coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain —
it is in the **pontine tegmentum**, **ventromedial** to the
subparabrachial nucleus. The **subparabrachial nucleus** (here) is the
**pontine respiratory center**. They are **DIFFERENT STRUCTURES** —
different neurotransmitters (glutamate, etc. vs. norepinephrine),
different functional systems (respiratory rhythm modulation vs.
noradrenergic arousal). They are **anatomically adjacent** — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the subparabrachial nucleus with the locus coeruleus.
**Boundary status (NOT the solitary nucleus — that is the MEDULLARY
UPSTREAM SOURCE):** **Boundary case — the subparabrachial nucleus is
NOT the solitary nucleus.** The **solitary nucleus** (nucleus tractus
solitarius, ``.../medulla_oblongata/solitary_nucleus/left/`` and
``.../right/``) is the **medullary visceral-afferent hub** for **CN
VII, IX, and X** — including **respiratory afferents** from the
**carotid body** and **aortic body** chemoreceptors, the **lung**
stretch receptors, and the **airway** receptors. The **solitary
nucleus** is the **upstream source** — it **projects to** the
**medial parabrachial nucleus** (which in turn **projects to** the
subparabrachial nucleus) and, to a lesser extent, directly to the
subparabrachial nucleus. The **subparabrachial nucleus** (here) is the
**pontine respiratory center** that **modulates** the **medullary
respiratory centers**. They are **DIFFERENT STRUCTURES** — the
**solitary nucleus** is **medullary** and **upstream**; the
**subparabrachial nucleus** is **pontine** and **downstream**.
**This distinction is clinically load-bearing** — a **solitary
nucleus** lesion causes **impaired respiratory afferent integration**
(loss of chemoreception, loss of lung stretch reflex); a
**subparabrachial nucleus** lesion causes **respiratory rhythm
dysregulation** (apneustic breathing, impaired phase switching).
Consumers must **not** conflate the subparabrachial nucleus with the
solitary nucleus.
**Boundary status (NOT the retrotrapezoid nucleus — that is the MEDULLARY
CENTRAL CHEMORECEPTOR):** **Boundary case — the subparabrachial nucleus
is NOT the retrotrapezoid nucleus (RTN).** The **RTN**
(``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
is the **medullary central chemoreceptor** — it **senses CO₂ / pH** and
**drives** the **ventral respiratory group** for **respiratory
chemoreception**. The **subparabrachial nucleus** (here) is the
**pontine respiratory center** — it **modulates** the **medullary
respiratory centers** (DRG and VRG). They are **DIFFERENT STRUCTURES** —
different brainstem levels (pons vs. medulla), different functional
roles (pontine respiratory rhythm modulation vs. medullary
chemoreception). **This distinction is clinically load-bearing** — an
**RTN** lesion causes **central hypoventilation** (loss of CO₂
chemoreception); a **subparabrachial nucleus** lesion causes
**respiratory rhythm dysregulation** (apneustic breathing, impaired
phase switching) without loss of chemoreception. Consumers must **not**
conflate the subparabrachial nucleus with the retrotrapezoid nucleus.
**Boundary status (NOT the ventral respiratory group — that is the
MEDULLARY RESPIRATORY PATTERN GENERATOR):** **Boundary case — the
subparabrachial nucleus is NOT the ventral respiratory group (VRG).**
The **VRG** (``.../medulla_oblongata/ventral_respiratory_group/``) is
the **medullary respiratory pattern generator** — it **contains** the
**pre-Bötzinger complex** (the **respiratory rhythm generator**), the
**nucleus ambiguus** (pharyngeal/laryngeal motor), the
**retrotrapezoid nucleus** (chemoreception), and other respiratory
neurons. The **subparabrachial nucleus** (here) is the **pontine
respiratory center** — it **modulates** the VRG (especially the
**pre-Bötzinger complex**) for **respiratory phase switching** and
**respiratory rhythm**. They are **DIFFERENT STRUCTURES** — different
brainstem levels (pons vs. medulla), different functional roles
(pontine modulation vs. medullary rhythm generation). **This
distinction is clinically load-bearing** — a **subparabrachial
nucleus** lesion causes **apneustic breathing** (prolonged inspiratory
pauses — the **apneustic center** function is lost); a **VRG** lesion
causes **loss of respiratory rhythm** (the **pre-Bötzinger complex** is
lost). Consumers must **not** conflate the subparabrachial nucleus with
the ventral respiratory group.
**Boundary status (NOT the dorsal respiratory group — that is the
MEDULLARY INSPIRATORY CENTER):** **Boundary case — the subparabrachial
nucleus is NOT the dorsal respiratory group (DRG).** The **DRG**
(``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
is the **medullary inspiratory center** — it **contains** the
**inspiratory neurons** of the **solitary nucleus** and **drives** the
**phrenic nerve** for **diaphragmatic contraction**. The
**subparabrachial nucleus** (here) is the **pontine respiratory
center** — it **modulates** the DRG (indirectly, via the VRG and the
Kölliker-Fuse nucleus) for **respiratory phase switching**. They are
**DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine modulation vs. medullary
inspiratory drive). Consumers must **not** conflate the
subparabrachial nucleus with the dorsal respiratory group.
**Boundary status (NOT the paramedian pontine reticular formation — that
is the horizontal gaze center):** **Boundary case — the
subparabrachial nucleus is NOT the paramedian pontine reticular
formation (PPRF).** The **PPRF**
(``.../pons/paramedian_pontine_reticular_formation/``) is the
**horizontal saccadic burst generator** — it **drives** the abducens
nucleus for **horizontal saccades**. The **subparabrachial nucleus**
(here) is the **pontine respiratory center**. They are **DIFFERENT
STRUCTURES** — different functional systems (horizontal gaze vs.
respiratory rhythm). Consumers must **not** conflate the
subparabrachial nucleus with the PPRF.
**Boundary status (NOT the pontine nuclei — those are basilar-pons
cortico-ponto-cerebellar relays):** **Boundary case — the
subparabrachial nucleus is NOT the pontine nuclei.** The **pontine
nuclei** (``.../pons/pontine_nuclei/left/`` and ``.../right/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons**. The
**subparabrachial nucleus** (here) is the **dorsal tegmental**
respiratory center. They are **DIFFERENT STRUCTURES** — different
anatomical locations (basilar pons vs. dorsal tegmentum), different
functional systems (cortico-ponto-cerebellar vs. respiratory). Consumers
must **not** conflate the subparabrachial nucleus with the pontine
nuclei.
**Boundary status (NOT the whole pons — the pons is the
great-grandparent):** **Boundary case — the subparabrachial nucleus is
NOT the whole pons; the pons is the great-grandparent.** The **pons**
(``.../pons/``) is the **whole metencephalic brainstem segment** — it
contains the **basilar pons**, the **pontine tegmentum**, the **pontine
nuclei**, the **corticospinal / corticobulbar tracts**, the **middle
cerebellar peduncle**, the **cranial_nerve_nuclei**, and the
**parabrachial area**. The **subparabrachial nucleus** (here) is the
**pontine respiratory center** only. Consumers must **not** conflate
the subparabrachial nucleus with the **whole pons**.
**Boundary status (NOT a single uniform functional system — TWO
functionally distinct populations — Kölliker-Fuse nucleus and pontine
respiratory group):** **Boundary case — the subparabrachial nucleus is
NOT a single uniform functional system; it contains TWO functionally
distinct populations — the Kölliker-Fuse nucleus and the pontine
respiratory group.** The **Kölliker-Fuse nucleus** — the **principal
pontine respiratory rhythm modulator** — regulates the
**inspiratory-expiratory phase transition** (the **Hering-Breuer
reflex**, **apneustic center** function), **laryngeal function**, and
**cardiorespiratory integration**. The **pontine respiratory group** —
the **broader functional concept** that includes the **Kölliker-Fuse
nucleus** and the **adjacent subparabrachial neurons** — is the
**pontine respiratory rhythm modulator** that **modulates** the
**medullary respiratory centers** (DRG and VRG). **These populations
are structural children** — the tree wires them as separate structural
children of the subparabrachial nucleus. Consumers must **not** treat
the subparabrachial nucleus as a single uniform functional system — it
is a **two-population complex** with **functionally distinct**
sub-circuits.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree
level):** **Boundary case — the subparabrachial nucleus is a SINGLE
module at the tree level, even though the subparabrachial nucleus is
BILATERAL in real anatomy.** Unlike the **cranial_nerve_nuclei** module
(which has explicit ``left`` and ``right`` structural children), the
**subparabrachial_nucleus** module (here) is a **single module** that
represents the **bilateral subparabrachial nuclei** (left and right
within the parabrachial area). The tree does **not** split them into
left/right. Consumers must **not** assume a left/right split exists at
the tree level — the module is a **single, bilateral-container
representation**.
**Boundary status (SLEA-FREE — the subparabrachial nucleus is NOT an
extended-amygdala component):** **Boundary case — the subparabrachial
nucleus is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **subparabrachial nucleus** is a **pontine respiratory
center** — it is **NOT** an extended-amygdala component, and it carries
**NO SLEA warning**. **Unlike the lateral parabrachial nucleus** (which
**projects to** the central nucleus of the amygdala and the BNST), the
**subparabrachial nucleus does NOT project to the SLEA** — it projects
to the **ventral respiratory group**, the **dorsal respiratory group**,
and the **hypothalamus**. The subparabrachial nucleus is **SLEA-FREE
without the "projects to SLEA" caveat** that applies to the lateral
parabrachial nucleus.

Overview
--------
The subparabrachial nucleus is the **pontine respiratory center** of the
**parabrachial area** — a **respiratory- and autonomically-organized**
grey-matter sub-container in the **ventral parabrachial area**, ventral
to the **medial parabrachial nucleus** and dorsal to the **superior
cerebellar peduncle** in the **dorsal pons**. It is a **sub-container**
under the parabrachial_area container, with **two structural children**
— the **Kölliker-Fuse nucleus** (the **pontine respiratory rhythm
modulator**) and the **pontine respiratory group** (the **broader
functional concept** that includes the Kölliker-Fuse nucleus and the
adjacent subparabrachial neurons).

**The subparabrachial nucleus is a CONTAINER, NOT a leaf.** Its
structural children are the **Kölliker-Fuse nucleus** and the **pontine
respiratory group**.

**The subparabrachial nucleus is SINGLE at the tree level, but
BILATERAL in real anatomy.** Unlike the **cranial_nerve_nuclei** module
(which has explicit ``left`` and ``right`` structural children), the
**subparabrachial_nucleus** module (here) is a **single module** that
represents the **bilateral subparabrachial nuclei**. The tree does **not**
split them into left/right. Consumers must **not** assume a left/right
split exists at the tree level.

**The subparabrachial nucleus is GREY-MATTER, NOT the superior
cerebellar peduncle.** The **superior cerebellar peduncle** (brachium
conjunctivum) is the **white-matter tract** that the subparabrachial
nucleus is **dorsal to** — within the parabrachial area. They are
**DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the **peduncle**
is white matter. **This distinction is the etymological origin of the
name and is a classic source of confusion.**

**The subparabrachial nucleus is NOT the lateral parabrachial nucleus or
the medial parabrachial nucleus.** Those are **siblings** under the
parabrachial_area container — the **lateral parabrachial nucleus** is
the **visceral-sensory and pain/aversion relay**; the **medial
parabrachial nucleus** is the **respiratory and autonomic relay**. They
are **DIFFERENT STRUCTURES** — different functional systems, different
downstream targets. **Functionally**, the medial parabrachial nucleus
**provides afferent input to** the subparabrachial nucleus.

**The subparabrachial nucleus is CLASSICALLY part of the pontine
respiratory group — but in the TREE, the subparabrachial nucleus is the
PARENT of the pontine respiratory group.** Some classical literature
treats the pontine respiratory group as a functional grouping that
includes the **Kölliker-Fuse nucleus** and the **medial parabrachial
nucleus** (or the **Kölliker-Fuse nucleus** and the **subparabrachial
nucleus**). The tree wires the **pontine respiratory group** as a
**structural child** of the **subparabrachial_nucleus** — matching the
**structural** relationship. Consumers must **not** assume the tree's
structural wiring matches every classical functional grouping.

**The subparabrachial nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
**Unlike the lateral parabrachial nucleus** (which **projects to** the
central nucleus of the amygdala and the BNST), the **subparabrachial
nucleus does NOT project to the SLEA** — it projects to the **ventral
respiratory group**, the **dorsal respiratory group**, and the
**hypothalamus**.

Sub-Nucleus Composition (structural children, prose)
----------------------------------------------------
The subparabrachial nucleus contains **two sub-nuclei** — documented as
**structural children** (not as leaves of the subparabrachial nucleus):

*   **Kölliker-Fuse nucleus**
    (``.../subparabrachial_nucleus/kolliker_fuse_nucleus/``) — the
    **principal pontine respiratory rhythm modulator**. It **regulates**
    the **inspiratory-expiratory phase transition** — the
    **Hering-Breuer reflex** (the **inspiratory off-switch** in response
    to **lung stretch**), the **apneustic center** function (the
    **prolongation of inspiration** in the absence of the
    **pneumotaxic center**), **laryngeal function** (the
    **postinspiratory phase** of the **respiratory cycle** that controls
    **upper airway resistance**), and **cardiorespiratory integration**
    (the **coupling** of **respiratory** and **cardiovascular** rhythms).
    The **Kölliker-Fuse nucleus** is the **pontine** counterpart of the
    **medullary respiratory centers** — it **modulates** the **dorsal
    respiratory group** and the **ventral respiratory group** to
    **produce** the **eupneic respiratory rhythm**.

*   **Pontine respiratory group**
    (``.../subparabrachial_nucleus/pontine_respiratory_group/``) — the
    **broader functional concept** that includes the **Kölliker-Fuse
    nucleus** and the **adjacent subparabrachial neurons** (and, in some
    classical definitions, the **medial parabrachial nucleus** — but
    the **tree** wires the pontine respiratory group as a **child** of
    the subparabrachial nucleus, not as a **sibling-level concept** that
    includes the medial parabrachial nucleus). It is the **pontine
    respiratory rhythm modulator** that **modulates** the **medullary
    respiratory centers** (the **dorsal respiratory group** and the
    **ventral respiratory group**) to **produce** the **eupneic
    respiratory rhythm** — the **automatic, metabolic** breathing
    pattern.

**These sub-nuclei are structural children of the subparabrachial
nucleus.** The subparabrachial nucleus's **structural children** are the
**Kölliker-Fuse nucleus** and the **pontine respiratory group**.
Consumers resolving sub-nucleus detail go **through** the Kölliker-Fuse
nucleus or the pontine respiratory group.

The Subparabrachial Nucleus / Lateral Parabrachial Nucleus Boundary
------------------------------------------------------------------
This is the **sibling** boundary — **respiratory rhythm vs.
visceral-sensory/pain/aversion**:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Lateral parabrachial nucleus**
    (``.../parabrachial_area/lateral_parabrachial_nucleus/``) — the
    **visceral-sensory and pain/aversion relay**.

**They are DIFFERENT STRUCTURES** — different functional systems
(respiratory rhythm vs. visceral-sensory/pain/aversion), different
downstream targets (VRG/DRG/hypothalamus vs.
amygdala/BNST/insula/hypothalamus/VPMpc/PAG). They are **anatomically
adjacent** (both are in the parabrachial area) — this proximity is a
**classic source of confusion** — consumers must **not** conflate the
subparabrachial nucleus with the lateral parabrachial nucleus.

The Subparabrachial Nucleus / Medial Parabrachial Nucleus Boundary
------------------------------------------------------------------
This is the **sibling** boundary — **respiratory rhythm vs.
respiratory afferent/autonomic relay**:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Medial parabrachial nucleus**
    (``.../parabrachial_area/medial_parabrachial_nucleus/``) — the
    **respiratory and autonomic relay**.

**They are DIFFERENT STRUCTURES** — different functional roles
(respiratory rhythm modulation vs. respiratory afferent/autonomic
relay), different downstream targets. **However**, they are
**functionally coupled** — the medial parabrachial nucleus **provides
afferent input to** the subparabrachial nucleus (especially the
Kölliker-Fuse nucleus). Consumers must **not** conflate the
subparabrachial nucleus with the medial parabrachial nucleus.

The Subparabrachial Nucleus / Kölliker-Fuse Nucleus and Pontine Respiratory Group Boundary
-----------------------------------------------------------------------------------------
This is the **container vs. structural child** boundary:

*   **Subparabrachial nucleus** (this module) — the **container** with
    two structural children.

*   **Kölliker-Fuse nucleus** and **pontine respiratory group** — the
    **structural children** of the subparabrachial nucleus.

**They are DIFFERENT STRUCTURES** — the **Kölliker-Fuse nucleus** and
the **pontine respiratory group** are **structural children** of the
subparabrachial nucleus, not the subparabrachial nucleus itself.
Consumers must **not** conflate the subparabrachial nucleus with the
Kölliker-Fuse nucleus or the pontine respiratory group.

The Subparabrachial Nucleus / Classical Pontine Respiratory Group Boundary
--------------------------------------------------------------------------
This is the **classical functional grouping vs. tree structural wiring**
boundary:

*   **Subparabrachial nucleus** (this module) — the **container** of the
    **Kölliker-Fuse nucleus** and the **pontine respiratory group** in
    the tree.

*   **Classical pontine respiratory group (PRG)** — in the **classical
    respiratory neurobiology literature**, the PRG is often defined as
    including the **Kölliker-Fuse nucleus** and the **medial parabrachial
    nucleus** (some authors) — or the **Kölliker-Fuse nucleus** and the
    **subparabrachial nucleus** (others).

**In the tree**, the **pontine respiratory group** is a **structural
child** of the **subparabrachial_nucleus**. **Functionally**, the
subparabrachial nucleus **contains** the Kölliker-Fuse nucleus and the
pontine respiratory group; the **medial parabrachial nucleus provides
afferent input to** them. **Structurally**, the tree wires the pontine
respiratory group as a child of the subparabrachial nucleus (matching the
**structural** relationship). Consumers must **not** assume the tree's
structural wiring matches every classical functional grouping.

The Subparabrachial Nucleus / Superior Cerebellar Peduncle Boundary
-------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **etymological
origin of the name**:

*   **Subparabrachial nucleus** (this module) — the **grey-matter neuron
    cluster** that is dorsal to the superior cerebellar peduncle.

*   **Superior cerebellar peduncle** (brachium conjunctivum) — the
    **white-matter tract** that carries cerebellar efferents from the
    dentate and interposed nuclei to the red nucleus and the thalamus.

**They are DIFFERENT STRUCTURES.** The **nucleus** is grey matter; the
**peduncle** is white matter. The nucleus is **dorsal to** the peduncle;
it is **not** the peduncle. **This distinction is the etymological origin
of the name "parabrachial"** ("para-" = alongside, "brachium" = the
superior cerebellar peduncle) — and it is a **classic source of
confusion**. Consumers must **not** conflate the subparabrachial nucleus
with the superior cerebellar peduncle.

The Subparabrachial Nucleus / Locus Coeruleus Boundary
------------------------------------------------------
This is the **anatomically adjacent** boundary — **respiratory rhythm
vs. noradrenergic nucleus**:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic nucleus** — the **principal source of norepinephrine**
    in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, etc. vs. norepinephrine), different functional systems
(respiratory rhythm vs. noradrenergic arousal). They are **anatomically
adjacent** — this proximity is a **classic source of confusion** —
consumers must **not** conflate the subparabrachial nucleus with the
locus coeruleus.

The Subparabrachial Nucleus / Solitary Nucleus Boundary
-------------------------------------------------------
This is the **upstream source vs. pontine respiratory center** boundary:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Solitary nucleus** (nucleus tractus solitarius,
    ``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``)
    — the **medullary visceral-afferent hub** for **CN VII, IX, and X**.

**The solitary nucleus is the upstream source** — it **projects to** the
**medial parabrachial nucleus** (which in turn **projects to** the
subparabrachial nucleus) and, to a lesser extent, directly to the
**subparabrachial nucleus**. The **subparabrachial nucleus** (here) is
the **pontine respiratory center** that **modulates** the **medullary
respiratory centers**. They are **DIFFERENT STRUCTURES** — the
**solitary nucleus** is **medullary** and **upstream**; the
**subparabrachial nucleus** is **pontine** and **downstream**. **This
distinction is clinically load-bearing** — a **solitary nucleus** lesion
causes **impaired respiratory afferent integration**; a
**subparabrachial nucleus** lesion causes **respiratory rhythm
dysregulation**. Consumers must **not** conflate the subparabrachial
nucleus with the solitary nucleus.

The Subparabrachial Nucleus / Retrotrapezoid Nucleus Boundary
-------------------------------------------------------------
This is the **central chemoreceptor** boundary — **upstream vs.
downstream**:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Retrotrapezoid nucleus (RTN)**
    (``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
    — the **medullary central chemoreceptor**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine respiratory rhythm
modulation vs. medullary chemoreception). The RTN **projects to** the
**medial parabrachial nucleus** (which in turn **projects to** the
subparabrachial nucleus). The subparabrachial nucleus **modulates** the
medullary respiratory centers. **This distinction is clinically
load-bearing** — an **RTN** lesion causes **central hypoventilation**
(loss of CO₂ chemoreception); a **subparabrachial nucleus** lesion causes
**respiratory rhythm dysregulation** (apneustic breathing). Consumers
must **not** conflate the subparabrachial nucleus with the
retrotrapezoid nucleus.

The Subparabrachial Nucleus / Ventral Respiratory Group Boundary
----------------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary pattern generator**
boundary:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Ventral respiratory group (VRG)**
    (``.../medulla_oblongata/ventral_respiratory_group/``) — the
    **medullary respiratory pattern generator**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary rhythm generation). The subparabrachial nucleus **projects to**
the VRG (especially the **pre-Bötzinger complex**) and **modulates** the
respiratory rhythm. **This distinction is clinically load-bearing** — a
**subparabrachial nucleus** lesion causes **apneustic breathing**
(prolonged inspiratory pauses — the **apneustic center** function is
lost); a **VRG** lesion causes **loss of respiratory rhythm** (the
**pre-Bötzinger complex** is lost). Consumers must **not** conflate the
subparabrachial nucleus with the ventral respiratory group.

The Subparabrachial Nucleus / Dorsal Respiratory Group Boundary
---------------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary inspiratory center**
boundary:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Dorsal respiratory group (DRG)**
    (``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
    — the **medullary inspiratory center**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary inspiratory drive). The subparabrachial nucleus **modulates**
the DRG (via the VRG and the Kölliker-Fuse nucleus) for **respiratory
phase switching**. Consumers must **not** conflate the subparabrachial
nucleus with the dorsal respiratory group.

The Subparabrachial Nucleus / Paramedian Pontine Reticular Formation Boundary
----------------------------------------------------------------------------
This is the **horizontal-gaze** boundary:

*   **Subparabrachial nucleus** (this module) — the **pontine
    respiratory center**.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/paramedian_pontine_reticular_formation/``) — the
    **horizontal saccadic burst generator**.

**They are DIFFERENT STRUCTURES** — different functional systems
(horizontal gaze vs. respiratory rhythm). Consumers must **not** conflate
the subparabrachial nucleus with the PPRF.

The Subparabrachial Nucleus / Pontine Nuclei Boundary
-----------------------------------------------------
This is the **basilar-pons vs. dorsal-tegmentum** boundary:

*   **Subparabrachial nucleus** (this module) — the **dorsal tegmental**
    pontine respiratory center.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/left/`` and
    ``.../right/``) — the **cortico-ponto-cerebellar relay** in the
    **basilar pons**.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. respiratory). Consumers must **not**
conflate the subparabrachial nucleus with the pontine nuclei.

The Subparabrachial Nucleus / Pons Boundary
-------------------------------------------
This is the **sub-container vs. great-grandparent** boundary:

*   **Subparabrachial nucleus** (this module) — the **pontine respiratory
    center** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine tegmentum**,
    the **pontine nuclei**, the **corticospinal / corticobulbar
    tracts**, the **middle cerebellar peduncle**, the **cranial-nerve
    nuclei**, and the **parabrachial area**.

**The subparabrachial nucleus is a great-grandchild of the pons** (via
parabrachial_area). Consumers must **not** conflate the subparabrachial
nucleus with the **whole pons**.

The Subparabrachial Nucleus / SLEA Boundary
-------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Subparabrachial nucleus** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The subparabrachial nucleus is NOT part of the SLEA continuum.** It is
a **pontine respiratory center**, and it carries **no SLEA warning**.
**Unlike the lateral parabrachial nucleus** (which **projects to** the
central nucleus of the amygdala and the BNST), the **subparabrachial
nucleus does NOT project to the SLEA** — it projects to the **ventral
respiratory group**, the **dorsal respiratory group**, and the
**hypothalamus**. The subparabrachial nucleus is **SLEA-FREE without the
"projects to SLEA" caveat** that applies to the lateral parabrachial
nucleus.

Function in the Human Brain
---------------------------
The subparabrachial nucleus's functions are **the pontine modulation of
respiratory rhythm and the cardiorespiratory integration** — **NOT a
single unified function**:

*   **Respiratory Rhythm Modulation (Kölliker-Fuse Nucleus):** The
    **Kölliker-Fuse nucleus** **regulates** the **inspiratory-expiratory
    phase transition** — the **Hering-Breuer reflex** (the
    **inspiratory off-switch** in response to **lung stretch**), the
    **apneustic center** function (the **prolongation of inspiration** in
    the absence of the **pneumotaxic center**), **laryngeal function**
    (the **postinspiratory phase** of the **respiratory cycle** that
    controls **upper airway resistance**), and **cardiorespiratory
    integration** (the **coupling** of **respiratory** and
    **cardiovascular** rhythms). It **modulates** the **dorsal
    respiratory group** and the **ventral respiratory group** to
    **produce** the **eupneic respiratory rhythm**.

*   **Pontine Respiratory Rhythm Modulation (Pontine Respiratory Group):**
    The **pontine respiratory group** (the **Kölliker-Fuse nucleus** and
    the **adjacent subparabrachial neurons**) **modulates** the
    **medullary respiratory centers** (the **dorsal respiratory group**
    and the **ventral respiratory group**) to **produce** the **eupneic
    respiratory rhythm** — the **automatic, metabolic** breathing
    pattern.

*   **Cardiorespiratory Integration:** The subparabrachial nucleus
    **integrates** **respiratory** and **cardiovascular** signals — it
    **receives** **autonomic afferents** from the **solitary nucleus**
    and **projects** to the **brainstem autonomic centers** (rostral
    ventrolateral medulla, nucleus ambiguus) for **cardiorespiratory
    coupling** — the **synchronization** of **respiratory** and
    **cardiovascular** rhythms (**respiratory sinus arrhythmia**).

*   **NOT a neural processor in the classical sense.** The
    subparabrachial nucleus is a **rhythm modulator** — it **receives**
    ascending respiratory and autonomic afferents (from the solitary
    nucleus and the medial parabrachial nucleus) and **projects** them to
    the **medullary respiratory centers** (DRG and VRG) and the
    **hypothalamus**. The **processing** of respiratory rhythm happens in
    the **medullary respiratory centers** (the **pre-Bötzinger complex**
    in the VRG is the **primary rhythm generator**), the **subparabrachial
    nucleus** (the **pontine rhythm modulator** — the **Kölliker-Fuse
    nucleus** and the **pontine respiratory group**), and the
    **hypothalamus** (the **autonomic** and **neuroendocrine** regulation
    of breathing). The **subparabrachial nucleus** is the **pontine
    modulator** of the **medullary respiratory rhythm**.

**The unifying theme:** the subparabrachial nucleus is the **pontine
respiratory center** — the **principal pontine respiratory rhythm
modulator** and **cardiorespiratory integration** node. It is **two-
population** (Kölliker-Fuse nucleus and pontine respiratory group),
**SLEA-FREE** (and does **not** project to the SLEA, unlike the lateral
parabrachial nucleus), and **NOT the superior cerebellar peduncle** — the
**peduncle** is the white-matter tract that the nucleus is **dorsal to**.

Associated Disorders
--------------------
The subparabrachial nucleus has **no single named "subparabrachial
nucleus syndrome"** — its clinical associations are **sub-nucleus-
specific** (Kölliker-Fuse nucleus and pontine respiratory group) and
**neuron-population-specific** within each sub-nucleus:

*   **Kölliker-Fuse Nucleus Lesion — Apneustic Breathing:** A lesion of
    the **Kölliker-Fuse nucleus** causes **apneustic breathing** —
    **prolonged inspiratory pauses** with **brief expiratory phases** —
    because the **inspiratory off-switch** (the **Hering-Breuer reflex**
    and the **pneumotaxic center** function) is **lost**. **The apneustic
    center** function of the Kölliker-Fuse nucleus is the **substrate** of
    this pattern.

*   **Kölliker-Fuse Nucleus Lesion — Impaired Hering-Breuer Reflex:** A
    lesion of the **Kölliker-Fuse nucleus** causes **impaired Hering-
    Breuer reflex** — the **inspiratory off-switch** in response to
    **lung stretch** is **lost** — leading to **impaired respiratory
    phase switching**.

*   **Kölliker-Fuse Nucleus Lesion — Laryngeal Dysfunction:** A lesion of
    the **Kölliker-Fuse nucleus** causes **laryngeal dysfunction** — the
    **postinspiratory phase** of the **respiratory cycle** is **lost**,
    leading to **impaired upper airway resistance** control — this can
    contribute to **sleep-disordered breathing** and **laryngeal
    stridor**.

*   **Subparabrachial Nucleus Lesion — Central Respiratory Dysregulation:**
    A lesion of the **subparabrachial nucleus** (e.g. **pontine stroke**,
    **tumor**, **demyelination**) causes **central respiratory
    dysregulation** — **impaired respiratory rhythm**, **apneustic
    breathing**, **impaired Hering-Breuer reflex**, **impaired laryngeal
    function**, and **impaired cardiorespiratory integration** (loss of
    **respiratory sinus arrhythmia**). **The pan-modal pattern** is the
    **substrate** of the **pontine respiratory center** functions of the
    subparabrachial nucleus.

*   **Central Sleep Apnea — Subparabrachial Nucleus Involvement:**
    **Central sleep apnea** is a **respiratory disorder** characterized
    by **absent respiratory effort** during sleep — it is caused by
    **dysfunction** of the **central respiratory control network**,
    including the **subparabrachial nucleus** (especially the
    **Kölliker-Fuse nucleus**), the **medial parabrachial nucleus**, the
    **retrotrapezoid nucleus**, and the **medullary respiratory centers**.
    **The subparabrachial nucleus** is **one of the neural substrates**
    of **central respiratory control**, and its dysfunction may
    **contribute** to **central sleep apnea**.

*   **Sudden Infant Death Syndrome (SIDS) — Subparabrachial Nucleus
    Involvement:** **SIDS** is a **sudden unexplained death** of an
    infant during sleep — it has been **associated** with
    **abnormalities** in the **medullary and pontine respiratory and
    autonomic control network**, including the **subparabrachial
    nucleus** (reduced **serotonin** and **glutamate** markers, reduced
    **neurokinin-1** receptor binding). **The subparabrachial nucleus**
    is **one of the neural substrates** of **cardiorespiratory
    integration**, and its dysfunction may **contribute** to **SIDS**.

*   **Congenital Central Hypoventilation Syndrome (CCHS) —
    Subparabrachial Nucleus Involvement:** **CCHS** is a **congenital
    respiratory disorder** characterized by **failure of automatic
    control of breathing** — it is caused by **PHOX2B** mutations, which
    affect the **autonomic nervous system** and the **brainstem
    respiratory and autonomic control network**, including the
    **subparabrachial nucleus**. **The subparabrachial nucleus** is **one
    of the neural substrates** of **central respiratory control**, and
    its dysfunction may **contribute** to **CCHS**.

*   **Rett Syndrome — Subparabrachial Nucleus Involvement:** **Rett
    syndrome** is a **neurodevelopmental disorder** caused by **MECP2**
    mutations — it is characterized by **autonomic dysfunction**,
    including **respiratory dysregulation** (**apneustic breathing**,
    **breath-holding**, **hyperventilation**). The **subparabrachial
    nucleus** (especially the **Kölliker-Fuse nucleus**) is **one of the
    neural substrates** of **respiratory rhythm modulation**, and its
    dysfunction may **contribute** to the **respiratory phenotype** of
    **Rett syndrome**.

*   **No Named "Subparabrachial Nucleus Syndrome":** The subparabrachial
    nucleus is a **two-population complex** — it has **no named clinical
    syndrome**. Its clinical relevance is **sub-nucleus-specific** —
    **Kölliker-Fuse nucleus** (apneustic breathing, Hering-Breuer reflex,
    laryngeal function); **pontine respiratory group** (pontine
    respiratory rhythm modulation).

**What is NOT here:** The subparabrachial nucleus is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), or **trigeminal neuralgia** (trigeminal nerve root). Its clinical
relevance is **respiratory-specific**, via the **Kölliker-Fuse nucleus**
and the **pontine respiratory group** it subserves. **No named
subparabrachial nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **single** subparabrachial nucleus module. The
subparabrachial nuclei are **bilateral in real anatomy** (left and right
within the parabrachial area), but the tree wires them as a **single
module** — and the module carries **NO warning at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **subparabrachial_nucleus** module (here) is a **single module** that
    represents the **bilateral subparabrachial nuclei**. The tree does
    **not** split them into left/right. Consumers must **not** assume a
    left/right split exists at the tree level — the module is a
    **single, bilateral-container representation**.

*   **Bilateral Respiratory and Autonomic Input (Structural Fact, NOT a
    Lateralization Warning):** The **subparabrachial nucleus**
    **receives** respiratory and autonomic afferents from the **medial
    parabrachial nucleus** (which receives from the **solitary nucleus**
    and the **retrotrapezoid nucleus**) — the projections are **largely
    bilateral** (each subparabrachial nucleus receives input from both
    left and right medial parabrachial nuclei). This **bilateral input**
    is a **structural fact** of the **respiratory and autonomic afferent
    system** — it is **not** a functional lateralization.

*   **Bilateral Projections to Medullary Respiratory Centers and
    Hypothalamus (Structural Fact, NOT a Lateralization Warning):** The
    **subparabrachial nucleus** **projects** to the **ventral respiratory
    group**, the **dorsal respiratory group**, and the **hypothalamus** —
    **bilaterally** (from both left and right subparabrachial nuclei).
    This **bilateral projection** is a **structural fact** of the
    **respiratory modulation system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **bilateral
    modulation** of respiratory rhythm.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The
    subparabrachial nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the
    subparabrachial nucleus. **Unlike the lateral parabrachial nucleus**
    (which **projects to** the central nucleus of the amygdala and the
    BNST), the **subparabrachial nucleus does NOT project to the SLEA** —
    it projects to the **ventral respiratory group**, the **dorsal
    respiratory group**, and the **hypothalamus**.

*   **NO Amygdala-Lateralization Warning of their own (the
    subparabrachial nucleus is RESPIRATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The subparabrachial nucleus
    is a **pontine respiratory center** — consumers must **not** conflate
    it with the **amygdala** or with the **fear circuit**.

**A consumer that sees "subparabrachial_nucleus" must understand that
the module is a SINGLE, BILATERAL-CONTAINER representation** — it is
**not** a left/right split at the tree level. The **bilateral
respiratory and autonomic input** and the **bilateral projections to
medullary respiratory centers and hypothalamus** are **structural
facts**, not lateralizations. The subparabrachial nucleus is a
**strict-single module with NO warning at the module level** — **no SLEA
warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** subparabrachial nuclei as a **single module** — it does
    **not** import left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../parabrachial_area/lateral_parabrachial_nucleus/``,
    ``.../parabrachial_area/medial_parabrachial_nucleus/``,
    ``.../pons/tegmentum/``, ``.../medulla_oblongata/``,
    ``.../midbrain/``, ``.../diencephalon/``, or any other container. The
    subparabrachial nucleus's relationships to the **lateral parabrachial
    nucleus**, the **medial parabrachial nucleus**, the **Kölliker-Fuse
    nucleus**, the **pontine respiratory group**, the **classical
    pontine respiratory group**, the **superior cerebellar peduncle**,
    the **locus coeruleus**, the **solitary nucleus**, the
    **retrotrapezoid nucleus**, the **ventral respiratory group**, the
    **dorsal respiratory group**, the **PPRF**, the **pontine nuclei**,
    the **pons**, and the **SLEA continuum** are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children are the Kölliker-Fuse
    nucleus and the pontine respiratory group.** These are its
    **direct structural children** — not leaves of the subparabrachial
    nucleus.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **subparabrachial nucleus** is a **single module** that represents
    the **bilateral subparabrachial nuclei** — the tree does **not**
    split them into left/right. Consumers must **not** assume a
    left/right split exists at the tree level.
*   **CLASSICAL FUNCTIONAL GROUPING vs. TREE STRUCTURAL WIRING — the
    subparabrachial nucleus is the PARENT of the pontine respiratory
    group in the tree, but some classical literature treats the pontine
    respiratory group as a sibling-level concept that includes the
    medial parabrachial nucleus.** **Functionally**, the subparabrachial
    nucleus **contains** the Kölliker-Fuse nucleus and the pontine
    respiratory group; the **medial parabrachial nucleus provides
    afferent input to** them. **Structurally**, the tree wires the
    pontine respiratory group as a child of the subparabrachial nucleus
    (matching the **structural** relationship). Consumers must **not**
    assume the tree's structural wiring matches every classical
    functional grouping.
*   **GREY-MATTER NUCLEI — NOT the superior cerebellar peduncle.** The
    **subparabrachial nucleus** is the **grey-matter neuron cluster**;
    the **superior cerebellar peduncle** (brachium conjunctivum) is the
    **white-matter tract** that the nucleus is **dorsal to**. **This
    distinction is the etymological origin of the name** ("para-brachial"
    = "alongside the brachium") and is a **classic source of confusion**.
    Consumers must **not** conflate the two.
*   **NOT the locus coeruleus — that is a noradrenergic nucleus.** The
    **locus coeruleus** is **anatomically adjacent** to the
    subparabrachial nucleus, but it is a **different structure**.
    Consumers must **not** conflate the two.
*   **NOT the lateral parabrachial nucleus or the medial parabrachial
    nucleus — those are SIBLINGS.** The **lateral parabrachial nucleus**
    is the **visceral-sensory and pain/aversion relay**; the **medial
    parabrachial nucleus** is the **respiratory and autonomic relay**.
    They are **different structures**. Consumers must **not** conflate
    the subparabrachial nucleus with either of them.
*   **NOT the solitary nucleus, the retrotrapezoid nucleus, the ventral
    respiratory group, or the dorsal respiratory group — those are
    UPSTREAM or DOWNSTREAM structures.** The **solitary nucleus** and the
    **retrotrapezoid nucleus** are **upstream** (they project to the
    medial parabrachial nucleus, which projects to the subparabrachial
    nucleus); the **ventral respiratory group** and the **dorsal
    respiratory group** are **downstream** (the subparabrachial nucleus
    modulates them). They are **different structures**. Consumers must
    **not** conflate the subparabrachial nucleus with any of them.
*   **NOT the PPRF or the pontine nuclei — those are different functional
    systems.** The **PPRF** is the **horizontal gaze center**; the
    **pontine nuclei** are the **cortico-ponto-cerebellar relay**.
    Consumers must **not** conflate the subparabrachial nucleus with
    either of them.
*   **TWO FUNCTIONALLY DISTINCT SUB-NUCLEI — KÖLLIKER-FUSE NUCLEUS vs.
    PONTINE RESPIRATORY GROUP.** The **Kölliker-Fuse nucleus** (the
    **principal pontine respiratory rhythm modulator**) and the
    **pontine respiratory group** (the **broader functional concept**
    that includes the **Kölliker-Fuse nucleus** and the **adjacent
    subparabrachial neurons**) are **structural children**, not prose
    subdivisions. Consumers must **not** treat the subparabrachial
    nucleus as a single uniform functional system.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    subparabrachial nucleus is **not** an extended-amygdala component,
    and it carries **no SLEA warning**. **Unlike the lateral parabrachial
    nucleus** (which **projects to** the central nucleus of the amygdala
    and the BNST), the **subparabrachial nucleus does NOT project to the
    SLEA** — it projects to the **ventral respiratory group**, the
    **dorsal respiratory group**, and the **hypothalamus**. The
    subparabrachial nucleus is **SLEA-FREE without the "projects to
    SLEA" caveat**.
*   **NOT the fear-output — the subparabrachial nucleus is RESPIRATORY.**
    The **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **subparabrachial nucleus** is a **pontine respiratory
    center** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The subparabrachial nucleus is a local
    sub-container under the parabrachial_area container, not a
    cross-listed sub-container.
*   **No nested cross-listing.** The subparabrachial nucleus has no
    nested dual-framing module. It is a single sub-container with two
    structural children.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area import subparabrachial_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "subparabrachial_nucleus"
    )

**Do not** assume the subparabrachial nucleus is a **leaf**. It is a
**sub-container** — its structural children are the **Kölliker-Fuse
nucleus** and the **pontine respiratory group**.

**Do not** assume the subparabrachial nucleus is **bilateralized at the
tree level**. The subparabrachial nuclei are **bilateral in real
anatomy**, but the tree wires them as a **single module** — there is **no
left/right split**.

**Do not** assume the subparabrachial nucleus is the **superior
cerebellar peduncle**. The **superior cerebellar peduncle** is the
**white-matter tract** that the subparabrachial nucleus is **dorsal to**
— the "para-brachial" name reflects this **flanking/dorsal
relationship**, not identity. They are **different structures**.

**Do not** assume the subparabrachial nucleus is the **lateral
parabrachial nucleus** or the **medial parabrachial nucleus**. Those are
**siblings** under the parabrachial_area container — the **lateral
parabrachial nucleus** is the **visceral-sensory and pain/aversion
relay**; the **medial parabrachial nucleus** is the **respiratory and
autonomic relay**. They are **different structures**.

**Do not** assume the subparabrachial nucleus is the **Kölliker-Fuse
nucleus** or the **pontine respiratory group**. Those are its
**structural children** — the Kölliker-Fuse nucleus is the **principal
pontine respiratory rhythm modulator**; the pontine respiratory group is
the **broader functional concept** that includes the Kölliker-Fuse
nucleus and the adjacent subparabrachial neurons.

**Do not** assume the tree's structural wiring matches every classical
functional grouping of the **pontine respiratory group** — in the tree,
the pontine respiratory group is a **child** of the subparabrachial
nucleus; in some classical literature, the pontine respiratory group is
a **functional grouping** that includes the **Kölliker-Fuse nucleus** and
the **medial parabrachial nucleus**. **Functionally**, the subparabrachial
nucleus **contains** the Kölliker-Fuse nucleus and the pontine
respiratory group; the **medial parabrachial nucleus provides afferent
input to** them. **Structurally**, the tree wires the pontine
respiratory group as a child of the subparabrachial nucleus.

**Do not** assume the subparabrachial nucleus is the **locus coeruleus**.
The **locus coeruleus** is the **noradrenergic nucleus** in the
**pontine tegmentum** — it is **anatomically adjacent** to the
subparabrachial nucleus, but it is a **different structure**.

**Do not** assume the subparabrachial nucleus is the **solitary nucleus**,
the **retrotrapezoid nucleus**, the **ventral respiratory group**, or the
**dorsal respiratory group**. Those are **upstream** or **downstream**
structures — the **solitary nucleus** and **retrotrapezoid nucleus** are
**upstream**; the **ventral respiratory group** and **dorsal respiratory
group** are **downstream**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the subparabrachial nucleus. **The subparabrachial nucleus
is SLEA-FREE** — it is **not** an extended-amygdala component, and it is
**NOT part of the fear circuit**. **Unlike the lateral parabrachial
nucleus**, the subparabrachial nucleus **does NOT project to the SLEA**.

Iterating the subparabrachial nucleus's structural children (recommended
consumer pattern)::

    SUBPARABRACHIAL_NUCLEUS_CHILDREN = (
        "kolliker_fuse_nucleus",
        "pontine_respiratory_group",
    )
    # The subparabrachial nucleus is a sub-container. The Kölliker-Fuse
    # nucleus is the principal pontine respiratory rhythm modulator; the
    # pontine respiratory group is the broader functional concept that
    # includes the Kölliker-Fuse nucleus and the adjacent subparabrachial
    # neurons.

Iterating the subparabrachial nucleus's structural children (recommended
consumer pattern)::

    for sub in SUBPARABRACHIAL_NUCLEUS_CHILDREN:
        sub_path = (
            f"hindbrain.metencephalon.pons.parabrachial_area."
            f"subparabrachial_nucleus.{sub}"
        )
        # resolve sub_path through the memory/recall layer

Reaching the lateral parabrachial nucleus (recommended consumer pattern —
the sibling)::

    # The lateral parabrachial nucleus is the VISCERAL-SENSORY AND
    # PAIN/AVERSION sibling under the parabrachial_area container:
    #
    #   .../parabrachial_area/lateral_parabrachial_nucleus/
    #
    # The subparabrachial nucleus is the PONTINE RESPIRATORY CENTER
    # sibling — different functional system, different downstream
    # targets.

Reaching the medial parabrachial nucleus (recommended consumer pattern —
the sibling)::

    # The medial parabrachial nucleus is the RESPIRATORY AND AUTONOMIC
    # RELAY sibling under the parabrachial_area container:
    #
    #   .../parabrachial_area/medial_parabrachial_nucleus/
    #
    # The subparabrachial nucleus is the PONTINE RESPIRATORY CENTER
    # sibling — different functional role (respiratory rhythm modulation
    # vs. respiratory afferent/autonomic relay). FUNCTIONALLY, the medial
    # parabrachial nucleus provides afferent input to the
    # subparabrachial nucleus.

Reaching the superior cerebellar peduncle (recommended consumer pattern —
the white-matter tract the nucleus is DORSAL to)::

    # The superior cerebellar peduncle (brachium conjunctivum) is the
    # WHITE-MATTER tract that the subparabrachial nucleus is DORSAL to:
    #
    #   .../white_matter/.../superior_cerebellar_peduncle/  (or equivalent path)
    #
    # The subparabrachial nucleus is GREY MATTER that is dorsal to the
    # peduncle; the peduncle is WHITE MATTER that connects the cerebellum
    # to the midbrain and thalamus. They are DIFFERENT STRUCTURES — the
    # anatomical juxtaposition is the etymological origin of the name
    # "para-brachial" and is a classic source of confusion.

Reaching the locus coeruleus (recommended consumer pattern — the adjacent
noradrenergic nucleus)::

    # The locus coeruleus is the NORADRENERGIC nucleus in the pontine
    # tegmentum — it is ANATOMICALLY ADJACENT to the subparabrachial
    # nucleus, but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic (source of norepinephrine);
    # the subparabrachial nucleus is glutamatergic (respiratory rhythm
    # modulation). They are ANATOMICALLY ADJACENT but FUNCTIONALLY
    # DISTINCT.

Reaching the solitary nucleus and retrotrapezoid nucleus (recommended
consumer pattern — the UPSTREAM sources)::

    # The solitary nucleus (nucleus tractus solitarius) and the
    # retrotrapezoid nucleus (RTN) are UPSTREAM sources that project to
    # the medial parabrachial nucleus (which in turn projects to the
    # subparabrachial nucleus):
    #
    #   .../medulla_oblongata/solitary_nucleus/left/  (and right/)
    #   .../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/
    #
    # The solitary nucleus and RTN are UPSTREAM; the subparabrachial
    # nucleus is DOWNSTREAM.

Reaching the ventral respiratory group and dorsal respiratory group
(recommended consumer pattern — the DOWNSTREAM medullary respiratory
centers)::

    # The ventral respiratory group (VRG) and the dorsal respiratory
    # group (DRG) are the DOWNSTREAM medullary respiratory centers that
    # the subparabrachial nucleus MODULATES:
    #
    #   .../medulla_oblongata/ventral_respiratory_group/
    #   .../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/
    #
    # The subparabrachial nucleus MODULATES the VRG (especially the
    # pre-Bötzinger complex) and the DRG (indirectly, via the VRG and
    # the Kölliker-Fuse nucleus) for respiratory phase switching.

Reaching the hypothalamus (recommended consumer pattern — the
DIENCEPHALIC target)::

    # The hypothalamus is a DIENCEPHALIC target of the subparabrachial
    # nucleus:
    #
    #   .../diencephalon/hypothalamus/
    #
    # The subparabrachial nucleus PROJECTS TO the hypothalamus for
    # autonomic and neuroendocrine regulation; the hypothalamus is a
    # DOWNSTREAM target.

Bilateral iteration (recommended consumer pattern)::

    # The subparabrachial nucleus is a SINGLE module (not bilateralized
    # at the tree level). The module represents the BILATERAL
    # subparabrachial nuclei.
    subparabrachial_path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "subparabrachial_nucleus"
    )
    # resolve subparabrachial_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The subparabrachial nucleus's sub-nuclei are structural children:
    #   kolliker_fuse_nucleus     -> principal pontine respiratory rhythm
    #                                modulator; inspiratory-expiratory
    #                                phase transition (Hering-Breuer
    #                                reflex, apneustic center function);
    #                                laryngeal function; cardiorespiratory
    #                                integration
    #   pontine_respiratory_group -> broader functional concept that
    #                                includes the Kölliker-Fuse nucleus
    #                                and the adjacent subparabrachial
    #                                neurons; pontine respiratory rhythm
    #                                modulator (modulates the medullary
    #                                respiratory centers)
    #
    # Resolve sub-nucleus detail through the kolliker_fuse_nucleus or
    # pontine_respiratory_group modules — not through prose subdivisions
    # of the subparabrachial nucleus.

References
----------
*   **Canonical subparabrachial nucleus anatomy:** Saper, C.B., Loewy,
    A.D. (1980). "Efferent connections of the parabrachial nucleus in
    the rat." *Brain Research* 197:291–317. (Subparabrachial nucleus
    efferents — the definitive early mapping.)
*   **Parabrachial area — review:** Saper, C.B. (2002). "The central
    autonomic nervous system: conscious visceral perception and autonomic
    function." *Annual Review of Neuroscience* 25:433–469.
    (Subparabrachial nucleus as the pontine respiratory center.)
*   **Pontine respiratory group — review:** Alheid, G.F., McCrimmon,
    D.R. (2008). "The chemical neuroanatomy of breathing." *Respiratory
    Physiology & Neurobiology* 164:3–11. (Subparabrachial nucleus, the
    Kölliker-Fuse nucleus, and the pontine respiratory group.)
*   **Kölliker-Fuse nucleus:** Dutschmann, M., Herbert, H. (2006). "The
    Kölliker-Fuse nucleus gates the postinspiratory phase of the
    respiratory cycle to control inspiratory off-switch and upper airway
    resistance in rat." *European Journal of Neuroscience* 24:1071–1084.
    (Kölliker-Fuse nucleus — respiratory phase switching; the principal
    pontine respiratory rhythm modulator.)
*   **Hering-Breuer reflex:** Kubin, L., Alheid, G.F., Zuperku, E.J.,
    McCrimmon, D.R. (2006). "Central pathways of pulmonary and lower
    airway vagal afferents." *Journal of Applied Physiology* 101:618–627.
    (Hering-Breuer reflex — the Kölliker-Fuse nucleus as the pontine
    inspiratory off-switch.)
*   **Apneustic breathing:** Lumsden, T. (1923). "Observations on the
    respiratory centres in a cat." *Journal of Physiology* 57:354–367.
    (Apneustic breathing — the pontine respiratory center,
    including the Kölliker-Fuse nucleus, as the apneustic center.)
*   **Central sleep apnea — subparabrachial nucleus involvement:**
    Dempsey, J.A., Veasey, S.C., Morgan, B.J., O'Donnell, C.P. (2010).
    "Pathophysiology of sleep apnea." *Physiological Reviews* 90:47–112.
    (Central sleep apnea — central respiratory control network including
    the subparabrachial nucleus.)
*   **SIDS — subparabrachial nucleus involvement:** Paterson, D.S.,
    Trachtenberg, F.L., Thompson, E.G., et al. (2006). "Multiple
    serotonergic brainstem abnormalities in sudden infant death
    syndrome." *JAMA* 296:2124–2132. (SIDS — brainstem respiratory and
    autonomic control network including the subparabrachial nucleus.)
*   **CCHS — subparabrachial nucleus involvement:** Weese-Mayer, D.E.,
    Berry-Kravis, E.M., Ceccherini, I., et al. (2010). "An official ATS
    clinical policy statement: congenital central hypoventilation
    syndrome." *American Journal of Respiratory and Critical Care
    Medicine* 181:626–644. (CCHS — PHOX2B mutations affecting the
    brainstem respiratory and autonomic control network including the
    subparabrachial nucleus.)
*   **Rett syndrome — subparabrachial nucleus involvement:** Ramirez,
    J.M., Ward, C.S., Neul, J.L. (2013). "Breathing challenges in Rett
    syndrome: lessons learned from humans and mice." *Respiratory
    Physiology & Neurobiology* 189:359–365. (Rett syndrome —
    respiratory dysregulation; the subparabrachial nucleus and
    Kölliker-Fuse nucleus as neural substrates.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the
    subparabrachial nucleus but functionally distinct.)
*   **Superior cerebellar peduncle (contrast — the white-matter tract the
    nucleus is DORSAL to):** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Superior cerebellar
    peduncle — brachium conjunctivum; the white-matter tract that the
    subparabrachial nucleus is dorsal to.)
*   **Solitary nucleus (contrast — the MEDULLARY upstream source):**
    Saper, C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Solitary nucleus — the medullary
    visceral-afferent hub that projects to the medial parabrachial
    nucleus, which projects to the subparabrachial nucleus.)
*   **Retrotrapezoid nucleus (contrast — the MEDULLARY chemoreceptor):**
    Guyenet, P.G., Stornetta, R.L., Bayliss, D.A. (2008). "Central
    respiratory chemoreception." *Journal of Comparative Neurology*
    506:788–798. (Retrotrapezoid nucleus — medullary central
    chemoreceptor; projects to the medial parabrachial nucleus, which
    projects to the subparabrachial nucleus.)
*   **Ventral respiratory group (contrast — the MEDULLARY respiratory
    pattern generator):** Feldman, J.L., Del Negro, C.A. (2006). "Looking
    for inspiration: new perspectives on respiratory rhythm." *Nature
    Reviews Neuroscience* 7:232–242. (Ventral respiratory group —
    medullary respiratory pattern generator; modulated by the
    subparabrachial nucleus.)
*   **Dorsal respiratory group (contrast — the MEDULLARY inspiratory
    center):** Bianchi, A.L., Denavit-Saubié, M., Champagnat, J. (1995).
    "Central control of breathing in mammals: neuronal circuitry,
    membrane properties, and neurotransmitters." *Physiological Reviews*
    75:1–45. (Dorsal respiratory group — medullary inspiratory center;
    modulated by the subparabrachial nucleus.)
*   **Classical pontine respiratory group vs. tree wiring (contrast —
    functional grouping vs. structural wiring):** Alheid, G.F.,
    McCrimmon, D.R. (2008). "The chemical neuroanatomy of breathing."
    *Respiratory Physiology & Neurobiology* 164:3–11. (Classical pontine
    respiratory group may include the medial parabrachial nucleus; the
    tree wires the pontine respiratory group as a child of the
    subparabrachial nucleus.)
*   **SLEA (contrast — the subparabrachial nucleus is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the
    subparabrachial nucleus.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the subparabrachial nucleus.)
*   NeuroNames — Subparabrachial nucleus; FMA — Subparabrachial nucleus.
"""