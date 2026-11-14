"""
infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area.subparabrachial_nucleus.pontine_respiratory_group
======================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── parabrachial_area
                └── subparabrachial_nucleus
                    ├── kolliker_fuse_nucleus
                    └── pontine_respiratory_group   <-- THIS MODULE

**Primary synonym:** Pontine respiratory group; PRG; pontine respiratory
complex; pontine respiratory center; "the pontine respiratory rhythm
modulator group."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**functional grouping of brainstem respiratory neurons** — **not a
single anatomically delimited nucleus**. The **pontine respiratory
group** is the **broader functional concept** that **includes** the
**Kölliker-Fuse nucleus** (the anatomically delimited principal
respiratory rhythm modulator) and the **adjacent subparabrachial
neurons** — and, in some classical definitions, the **medial parabrachial
nucleus** (but the **tree does not include the medial parabrachial
nucleus** in its structural wiring of the pontine respiratory group — see
the *Classical vs. Tree Wiring Boundary* below).
**Part of:** The **subparabrachial_nucleus** sub-container of the
**parabrachial_area** container — specifically, the **pontine
respiratory rhythm modulation** component. The
**subparabrachial_nucleus** is the **pontine respiratory center**; the
**pontine respiratory group** is its **broader functional concept
child** — a **functional grouping** that **includes** the
**Kölliker-Fuse nucleus** and the **adjacent subparabrachial neurons**.
**Structural parent:** ``.../subparabrachial_nucleus/`` → **direct
child** of the subparabrachial_nucleus sub-container.
**Structural children:** **None.** This is a **leaf** module. The
**pontine respiratory group** is a **functional grouping** — it does
**not** have structural children. The **Kölliker-Fuse nucleus** (a
**sibling** in the tree) is **included** in the pontine respiratory
group **functionally**, but the **tree does not wire the Kölliker-Fuse
nucleus as a child of the pontine respiratory group** (see the
*Sibling-that-Includes-Sibling Boundary* below).
**Boundary status (LEAF at tree level — FUNCTIONAL GROUPING with NO
structural children):** **Boundary case — the pontine respiratory group
is a LEAF at the TREE level, but a FUNCTIONAL GROUPING that INCLUDES the
Kölliker-Fuse nucleus and the adjacent subparabrachial neurons.** The
tree wires the **pontine respiratory group** as a **single
`__init__.py`** — it has **no structural children**. The **Kölliker-Fuse
nucleus** is a **sibling** at the tree level (both are children of the
subparabrachial_nucleus), but the **pontine respiratory group
functionally INCLUDES the Kölliker-Fuse nucleus** (and the adjacent
subparabrachial neurons). This is a **unique tree-wiring decision**: the
tree does **not** wire the Kölliker-Fuse nucleus as a child of the
pontine respiratory group (which would create a **cycle** in the tree —
since the Kölliker-Fuse nucleus is already a sibling), so the
**functional inclusion** of the Kölliker-Fuse nucleus is documented as
**prose**, not as a **structural child**. Consumers must **not** assume
the pontine respiratory group has structural children — it is a **leaf**
at the tree level, but a **functional grouping** that **includes** its
sibling (the Kölliker-Fuse nucleus) and the adjacent subparabrachial
neurons.
**Boundary status (SIBLING-THAT-INCLUDES-SIBLING — the pontine
respiratory group is a sibling of the Kölliker-Fuse nucleus at the tree
level, but INCLUDES the Kölliker-Fuse nucleus functionally):** **Boundary
case — the pontine respiratory group is a SIBLING of the Kölliker-Fuse
nucleus at the tree level, but it INCLUDES the Kölliker-Fuse nucleus
functionally.** This is a **unique relationship in the tree** — the
pontine respiratory group and the Kölliker-Fuse nucleus are **structural
siblings** (both are children of the subparabrachial_nucleus), but the
pontine respiratory group is a **broader functional concept** that
**includes** the Kölliker-Fuse nucleus. **The tree does not wire the
Kölliker-Fuse nucleus as a child of the pontine respiratory group** —
that would create a **structural cycle** — so the **functional
inclusion** of the Kölliker-Fuse nucleus in the pontine respiratory
group is documented as **prose**, not as a **structural child**.
Consumers must **not** assume that "sibling at the tree level" implies
"no functional overlap" — the pontine respiratory group **functionally
contains** its sibling (the Kölliker-Fuse nucleus). This is the **inverse
of the pattern** seen in most prior modules: usually a **structural
sibling** is a **functionally distinct** entity; here, the pontine
respiratory group is a **structural sibling** that is **functionally a
superset** of its sibling.
**Boundary status (FUNCTIONAL GROUPING — NOT a single anatomically
delimited nucleus):** **Boundary case — the pontine respiratory group is
a FUNCTIONAL GROUPING, NOT a single anatomically delimited nucleus.**
Unlike the **Kölliker-Fuse nucleus** (which is an anatomically
delimited nucleus), the **pontine respiratory group** is the **broader
functional concept** that **groups together** the **Kölliker-Fuse
nucleus** and the **adjacent subparabrachial neurons** (and, in some
classical definitions, the **medial parabrachial nucleus**). Consumers
must **not** assume the pontine respiratory group is a **discrete
anatomical nucleus** — it is a **functional grouping** that **spans**
multiple anatomically delimited structures.
**Boundary status (NOT the Kölliker-Fuse nucleus — that is a SIBLING
that is INCLUDED in the pontine respiratory group):** **Boundary case —
the pontine respiratory group is NOT the Kölliker-Fuse nucleus; the
Kölliker-Fuse nucleus is a SIBLING that is INCLUDED in the pontine
respiratory group.** The **Kölliker-Fuse nucleus**
(``.../subparabrachial_nucleus/kolliker_fuse_nucleus/``) is the
**anatomically delimited principal respiratory rhythm modulator** —
the **inspiratory off-switch** (the Hering-Breuer reflex), the
**apneustic center** function, and the **laryngeal modulator**. The
**pontine respiratory group** (here) is the **broader functional
concept** that **includes** the **Kölliker-Fuse nucleus** and the
**adjacent subparabrachial neurons**. They are **STRUCTURAL SIBLINGS at
the tree level** — but the **pontine respiratory group functionally
INCLUDES the Kölliker-Fuse nucleus**. **This relationship is unusual** —
consumers must **not** conflate the pontine respiratory group with the
Kölliker-Fuse nucleus (they are **different levels of abstraction** —
one is a functional grouping, the other is an anatomically delimited
nucleus), but they must **also not assume they are functionally
disjoint** (the pontine respiratory group **functionally contains** the
Kölliker-Fuse nucleus). **This is the primary source of confusion** for
this module — the **sibling-that-includes-sibling** relationship.
**Boundary status (NOT the subparabrachial nucleus — that is the
PARENT):** **Boundary case — the pontine respiratory group is NOT the
subparabrachial nucleus; the subparabrachial nucleus is the PARENT.**
The **subparabrachial nucleus**
(``.../subparabrachial_nucleus/``) is the **pontine respiratory
center** — it **contains** the **Kölliker-Fuse nucleus** and the
**pontine respiratory group**. The **pontine respiratory group** (here)
is the **broader functional concept** that **includes** the
**Kölliker-Fuse nucleus** and the **adjacent subparabrachial neurons**
— it is **one of the two structural children** of the subparabrachial
nucleus. Consumers must **not** conflate the pontine respiratory group
with the subparabrachial nucleus.
**Boundary status (NOT the medial parabrachial nucleus — that is an
AUNT/UNCLE in the tree, but is INCLUDED in some CLASSICAL definitions
of the pontine respiratory group):** **Boundary case — the pontine
respiratory group is NOT the medial parabrachial nucleus; the medial
parabrachial nucleus is an "aunt/uncle" in the tree (a sibling of the
subparabrachial nucleus), but is INCLUDED in some CLASSICAL definitions
of the pontine respiratory group.** The **medial parabrachial nucleus**
(``.../parabrachial_area/medial_parabrachial_nucleus/``) is the
**respiratory and autonomic relay** — it **provides afferent input to**
the Kölliker-Fuse nucleus and the pontine respiratory group. In
**some classical definitions**, the **pontine respiratory group** is
**defined as including** the **Kölliker-Fuse nucleus** and the **medial
parabrachial nucleus** (along with the adjacent subparabrachial
neurons). In the **tree**, the **pontine respiratory group does NOT
include the medial parabrachial nucleus** — the tree wires the pontine
respiratory group as a **child of the subparabrachial nucleus** only.
**Functionally**, the medial parabrachial nucleus **provides afferent
input to** the pontine respiratory group. Consumers must **not** assume
the tree's structural wiring matches every classical definition of the
pontine respiratory group — see the *Classical vs. Tree Wiring
Boundary* below.
**Boundary status (CLASSICAL vs. TREE WIRING — the pontine respiratory
group is wired as a child of the subparabrachial nucleus in the tree,
but classical definitions may include the medial parabrachial nucleus):**
**Boundary case — the pontine respiratory group is wired as a child of
the subparabrachial nucleus in the TREE, but classical definitions may
INCLUDE the medial parabrachial nucleus.** In the **tree**, the
**pontine respiratory group** is a **structural child** of the
**subparabrachial_nucleus** — and therefore a **sibling** of the
**Kölliker-Fuse nucleus**. **Classical respiratory neurobiology
literature** sometimes defines the **pontine respiratory group** as
**including** the **Kölliker-Fuse nucleus** and the **medial
parabrachial nucleus** (along with the adjacent subparabrachial
neurons). The **tree wiring decision** is to wire the pontine
respiratory group as a **child of the subparabrachial nucleus** (and
therefore a sibling of the Kölliker-Fuse nucleus), **not** as a
**sibling-level concept** that **includes** both the Kölliker-Fuse
nucleus and the medial parabrachial nucleus. **This is a tree-wiring
decision**, not a claim that the classical functional grouping is
wrong. **Functionally**, the medial parabrachial nucleus **provides
afferent input to** the pontine respiratory group; the pontine
respiratory group **modulates** the medullary respiratory centers.
Consumers must **not** assume the tree's structural wiring matches every
classical definition — the **tree wiring** matches the **structural
relationship** (pontine respiratory group as a child of the
subparabrachial nucleus), not the **functional grouping** (which may
include the medial parabrachial nucleus).
**Boundary status (NOT the lateral parabrachial nucleus — that is an
AUNT/UNCLE):** **Boundary case — the pontine respiratory group is NOT
the lateral parabrachial nucleus; the lateral parabrachial nucleus is an
"aunt/uncle" in the tree (a sibling of the subparabrachial nucleus).**
The **lateral parabrachial nucleus**
(``.../parabrachial_area/lateral_parabrachial_nucleus/``) is the
**visceral-sensory and pain/aversion relay**. The **pontine respiratory
group** (here) is the **pontine respiratory rhythm modulator**. They
are **DIFFERENT STRUCTURES** — different functional systems
(visceral-sensory/pain/aversion vs. respiratory rhythm), different
downstream targets. Consumers must **not** conflate the pontine
respiratory group with the lateral parabrachial nucleus.
**Boundary status (GREY-MATTER NUCLEI — NOT the superior cerebellar
peduncle):** **Boundary case — the pontine respiratory group is the
GREY-MATTER NUCLEI, NOT the superior cerebellar peduncle.** The
**superior cerebellar peduncle** (the "brachium conjunctivum") is the
**white-matter tract** that carries **cerebellar efferents** from the
**dentate nucleus** and the **interposed nucleus** to the **red
nucleus** and the **thalamus**. The **pontine respiratory group**
(here) is the **grey-matter functional grouping** that is **dorsal to**
the superior cerebellar peduncle — within the **subparabrachial
region**. They are **DIFFERENT STRUCTURES** — the **functional
grouping** is grey matter; the **peduncle** is white matter. **This
distinction is the etymological origin of the "parabrachial" name and
is a classic source of confusion** — consumers must **not** conflate
the pontine respiratory group with the superior cerebellar peduncle.
**Boundary status (NOT the locus coeruleus — that is the adjacent
noradrenergic nucleus):** **Boundary case — the pontine respiratory
group is NOT the locus coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain.
The **pontine respiratory group** (here) is the **pontine respiratory
rhythm modulator**. They are **DIFFERENT STRUCTURES** — different
neurotransmitters (glutamate, etc. vs. norepinephrine), different
functional systems (respiratory rhythm modulation vs. noradrenergic
arousal). They are **anatomically adjacent** — this proximity is a
**classic source of confusion** — consumers must **not** conflate the
pontine respiratory group with the locus coeruleus.
**Boundary status (NOT the solitary nucleus — that is the MEDULLARY
UPSTREAM SOURCE):** **Boundary case — the pontine respiratory group is
NOT the solitary nucleus.** The **solitary nucleus** (nucleus tractus
solitarius, ``.../medulla_oblongata/solitary_nucleus/left/`` and
``.../right/``) is the **medullary visceral-afferent hub** for **CN
VII, IX, and X** — including **respiratory afferents** from the
**carotid body** and **aortic body** chemoreceptors, the **lung**
stretch receptors, and the **airway** receptors. The **solitary
nucleus** is the **upstream source** — it **projects to** the
**medial parabrachial nucleus** (which in turn **projects to** the
pontine respiratory group) and, to a lesser extent, **directly** to the
**Kölliker-Fuse nucleus** within the pontine respiratory group. The
**pontine respiratory group** (here) is the **pontine respiratory
rhythm modulator**. They are **DIFFERENT STRUCTURES** — the **solitary
nucleus** is **medullary** and **upstream**; the **pontine respiratory
group** is **pontine** and **downstream**. **This distinction is
clinically load-bearing** — a **solitary nucleus** lesion causes
**impaired respiratory afferent integration**; a **pontine respiratory
group** lesion causes **apneustic breathing**. Consumers must **not**
conflate the pontine respiratory group with the solitary nucleus.
**Boundary status (NOT the retrotrapezoid nucleus — that is the
MEDULLARY CENTRAL CHEMORECEPTOR):** **Boundary case — the pontine
respiratory group is NOT the retrotrapezoid nucleus (RTN).** The **RTN**
(``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
is the **medullary central chemoreceptor** — it **senses CO₂ / pH** and
**drives** the **ventral respiratory group** for **respiratory
chemoreception**. The **pontine respiratory group** (here) is the
**pontine respiratory rhythm modulator** — it **modulates** the
**medullary respiratory centers**. They are **DIFFERENT STRUCTURES** —
different brainstem levels (pons vs. medulla), different functional
roles (pontine rhythm modulation vs. medullary chemoreception).
**This distinction is clinically load-bearing** — an **RTN** lesion
causes **central hypoventilation** (loss of CO₂ chemoreception); a
**pontine respiratory group** lesion causes **apneustic breathing**
without loss of chemoreception. Consumers must **not** conflate the
pontine respiratory group with the retrotrapezoid nucleus.
**Boundary status (NOT the ventral respiratory group — that is the
MEDULLARY RESPIRATORY PATTERN GENERATOR):** **Boundary case — the
pontine respiratory group is NOT the ventral respiratory group (VRG).**
The **VRG** (``.../medulla_oblongata/ventral_respiratory_group/``) is
the **medullary respiratory pattern generator** — it **contains** the
**pre-Bötzinger complex** (the **respiratory rhythm generator**), the
**nucleus ambiguus**, the **retrotrapezoid nucleus**, and other
respiratory neurons. The **pontine respiratory group** (here) is the
**pontine respiratory rhythm modulator** — it **modulates** the VRG
(especially the **pre-Bötzinger complex**) for **respiratory phase
switching**. They are **DIFFERENT STRUCTURES** — different brainstem
levels (pons vs. medulla), different functional roles (pontine
modulation vs. medullary rhythm generation). **This distinction is
clinically load-bearing** — a **pontine respiratory group** lesion
causes **apneustic breathing**; a **VRG** lesion causes **loss of
respiratory rhythm**. Consumers must **not** conflate the pontine
respiratory group with the ventral respiratory group.
**Boundary status (NOT the pre-Bötzinger complex — that is the
MEDULLARY RHYTHM GENERATOR WITHIN the VRG):** **Boundary case — the
pontine respiratory group is NOT the pre-Bötzinger complex.** The
**pre-Bötzinger complex** is the **medullary respiratory rhythm
generator** — a **sub-region** of the **ventral respiratory group** in
the **medulla** that **generates** the **fundamental respiratory
rhythm** (the **eupneic rhythm** and the **gasping rhythm**). The
**pontine respiratory group** (here) is the **pontine respiratory
rhythm modulator** — it **modulates** the pre-Bötzinger complex for
**respiratory phase switching** and **respiratory pattern** (e.g.
**inspiratory off-switch**, **postinspiration**). They are **DIFFERENT
STRUCTURES** — different brainstem levels (pons vs. medulla), different
functional roles (pontine modulation vs. medullary rhythm generation).
**This distinction is clinically load-bearing** — the
**pre-Bötzinger complex** is the **primary rhythm generator**; the
**pontine respiratory group** is a **modulator** of that rhythm.
Consumers must **not** conflate the pontine respiratory group with the
pre-Bötzinger complex.
**Boundary status (NOT the dorsal respiratory group — that is the
MEDULLARY INSPIRATORY CENTER):** **Boundary case — the pontine
respiratory group is NOT the dorsal respiratory group (DRG).** The
**DRG** (``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
is the **medullary inspiratory center** — it **contains** the
**inspiratory neurons** of the **solitary nucleus** and **drives** the
**phrenic nerve** for **diaphragmatic contraction**. The **pontine
respiratory group** (here) is the **pontine respiratory rhythm
modulator** — it **modulates** the DRG (indirectly, via the VRG and the
pre-Bötzinger complex) for **respiratory phase switching**. They are
**DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine modulation vs. medullary
inspiratory drive). Consumers must **not** conflate the pontine
respiratory group with the dorsal respiratory group.
**Boundary status (NOT the Hering-Breuer reflex — that is a CIRCUIT,
not a structure):** **Boundary case — the pontine respiratory group is
NOT the Hering-Breuer reflex; the Hering-Breuer reflex is a CIRCUIT.**
The **Hering-Breuer reflex** is the **vagally mediated inspiratory
off-switch reflex** that **inhibits inspiration** in response to
**lung inflation** — its **afferent limb** is the **pulmonary stretch
receptors** (via the **vagus nerve** and the **solitary nucleus**); its
**central node** is the **Kölliker-Fuse nucleus** (and the **pontine
respiratory group**); its **efferent limb** is the **medullary
respiratory centers** (DRG and VRG). The **pontine respiratory group**
(here) is **one node** in this circuit — the **pontine inspiratory
off-switch** — not the circuit itself. **This distinction is clinically
load-bearing** — a **Hering-Breuer reflex** deficit causes **apneustic
breathing** and **impaired inspiratory off-switch**. Consumers must
**not** conflate the pontine respiratory group with the Hering-Breuer
reflex.
**Boundary status (NOT the apneustic center or the pneumotaxic center —
those are HISTORICAL FUNCTIONAL CONCEPTS):** **Boundary case — the
pontine respiratory group is NOT the apneustic center or the pneumotaxic
center; those are HISTORICAL FUNCTIONAL CONCEPTS.** The **apneustic
center** and the **pneumotaxic center** were **historically** described
as **distinct pontine respiratory centers** — the **apneustic center**
driving inspiration, the **pneumotaxic center** inhibiting it. **Modern
understanding** — the **pneumotaxic center** is the **Kölliker-Fuse
nucleus** (and the **pontine respiratory group**); the **apneustic
center** is **not a distinct nucleus** — **apneusis** results from
**loss** of the Kölliker-Fuse nucleus (or its connections), **not** from
**activation** of a **separate apneustic center**. The **pontine
respiratory group** is the **modern anatomical and functional concept**
that **contains** the **Kölliker-Fuse nucleus** — it is **not** the
same as the **apneustic center** or the **pneumotaxic center** (which
are **historical functional concepts**). Consumers must **not** treat
the apneustic center or the pneumotaxic center as **distinct
structures** from the pontine respiratory group — they are **historical
functional concepts** that are **now understood** in terms of the
Kölliker-Fuse nucleus and the pontine respiratory group.
**Boundary status (NOT the laryngeal motor nucleus — that is the
NUCLEUS AMBIGUUS):** **Boundary case — the pontine respiratory group is
NOT the laryngeal motor nucleus.** The **laryngeal motor neurons** are
in the **nucleus ambiguus** (in the **medulla**) — they **innervate**
the **intrinsic laryngeal muscles**. The **pontine respiratory group**
(here) is the **pontine respiratory rhythm modulator** — it
**modulates** the **laryngeal motor nucleus** (via projections to the
**nucleus ambiguus** and the **solitary nucleus**) for
**postinspiratory laryngeal adduction**. They are **DIFFERENT
STRUCTURES** — different brainstem levels (pons vs. medulla), different
functional roles (pontine laryngeal modulation vs. laryngeal motor
output). Consumers must **not** conflate the pontine respiratory group
with the laryngeal motor nucleus.
**Boundary status (NOT the PPRF or the pontine nuclei — those are
different functional systems):** **Boundary case — the pontine
respiratory group is NOT the paramedian pontine reticular formation
(PPRF) or the pontine nuclei.** The **PPRF**
(``.../pons/paramedian_pontine_reticular_formation/``) is the
**horizontal saccadic burst generator**; the **pontine nuclei**
(``.../pons/pontine_nuclei/left/`` and ``.../right/``) are the
**cortico-ponto-cerebellar relay**. The **pontine respiratory group**
(here) is the **pontine respiratory rhythm modulator**. They are
**DIFFERENT STRUCTURES** — different functional systems (horizontal
gaze / cortico-ponto-cerebellar vs. respiratory rhythm). Consumers must
**not** conflate the pontine respiratory group with the PPRF or the
pontine nuclei.
**Boundary status (NOT the whole pons — the pons is the
great-great-grandparent):** **Boundary case — the pontine respiratory
group is NOT the whole pons; the pons is the great-great-grandparent.**
The **pons** (``.../pons/``) is the **whole metencephalic brainstem
segment** — it contains the **basilar pons**, the **pontine
tegmentum**, the **pontine nuclei**, the **corticospinal /
corticobulbar tracts**, the **middle cerebellar peduncle**, the
**cranial_nerve_nuclei**, and the **parabrachial area**. The
**pontine respiratory group** (here) is the **pontine respiratory
rhythm modulator group** only. Consumers must **not** conflate the
pontine respiratory group with the **whole pons**.
**Boundary status (MULTIPLE FUNCTIONALLY DISTINCT COMPONENTS — NOT a
single uniform functional system):** **Boundary case — the pontine
respiratory group is NOT a single uniform functional system; it
includes MULTIPLE functionally distinct components.** The **Kölliker-Fuse
nucleus** (the principal pontine respiratory rhythm modulator — the
inspiratory off-switch, the apneustic center function, the laryngeal
modulator) and the **adjacent subparabrachial neurons** (which may
include additional respiratory neurons with distinct projection
targets) are **functionally distinct components** of the pontine
respiratory group. **These components are prose, not structural
children** — the tree does not wire the Kölliker-Fuse nucleus as a
child of the pontine respiratory group (they are siblings). Consumers
must **not** treat the pontine respiratory group as a single uniform
functional system — it is a **functionally heterogeneous grouping**
with **multiple functionally distinct** components.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree
level):** **Boundary case — the pontine respiratory group is a SINGLE
module at the tree level, even though the pontine respiratory group is
BILATERAL in real anatomy.** Unlike the **cranial_nerve_nuclei** module
(which has explicit ``left`` and ``right`` structural children), the
**pontine_respiratory_group** module (here) is a **single module** that
represents the **bilateral pontine respiratory group** (left and right
within the subparabrachial region). The tree does **not** split them
into left/right. Consumers must **not** assume a left/right split
exists at the tree level — the module is a **single, bilateral
representation**.
**Boundary status (SLEA-FREE — the pontine respiratory group is NOT an
extended-amygdala component):** **Boundary case — the pontine
respiratory group is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala) and
to the **BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **pontine respiratory group** is a **pontine
respiratory rhythm modulator group** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
**Unlike the lateral parabrachial nucleus** (which **projects to** the
central nucleus of the amygdala and the BNST), the **pontine
respiratory group does NOT project to the SLEA** — it projects to the
**medullary respiratory centers**, the **nucleus ambiguus**, the
**solitary nucleus**, and the **hypothalamus**. The pontine
respiratory group is **SLEA-FREE without the "projects to SLEA"
caveat**.

Overview
--------
The pontine respiratory group is the **pontine respiratory rhythm
modulator group** of the **subparabrachial nucleus** — a **functional
grouping** of respiratory neurons in the **ventral subparabrachial
region**, dorsal to the **superior cerebellar peduncle** in the **dorsal
pons**. It is a **leaf** module under the subparabrachial_nucleus
sub-container, but it is a **functional grouping** that **includes** the
**Kölliker-Fuse nucleus** (its **structural sibling**) and the
**adjacent subparabrachial neurons** (and, in some classical
definitions, the **medial parabrachial nucleus** — but the tree does
**not** include the medial parabrachial nucleus).

**The pontine respiratory group is a LEAF at the TREE level, but a
FUNCTIONAL GROUPING that INCLUDES the Kölliker-Fuse nucleus and the
adjacent subparabrachial neurons.** The tree wires the **pontine
respiratory group** as a **single `__init__.py`** — it has **no
structural children**. The **Kölliker-Fuse nucleus** is a **sibling**
at the tree level, but the **pontine respiratory group functionally
INCLUDES the Kölliker-Fuse nucleus**.

**The pontine respiratory group is a SIBLING-THAT-INCLUDES-SIBLING.**
This is a **unique relationship in the tree** — the pontine respiratory
group and the Kölliker-Fuse nucleus are **structural siblings** (both
are children of the subparabrachial_nucleus), but the pontine
respiratory group is a **broader functional concept** that **includes**
the Kölliker-Fuse nucleus. **The tree does not wire the Kölliker-Fuse
nucleus as a child of the pontine respiratory group** — that would
create a **structural cycle** — so the **functional inclusion** of the
Kölliker-Fuse nucleus in the pontine respiratory group is documented as
**prose**, not as a **structural child**.

**The pontine respiratory group is a FUNCTIONAL GROUPING, NOT a single
anatomically delimited nucleus.** Unlike the **Kölliker-Fuse nucleus**
(which is an anatomically delimited nucleus), the **pontine respiratory
group** is the **broader functional concept** that **groups together**
the **Kölliker-Fuse nucleus** and the **adjacent subparabrachial
neurons** (and, in some classical definitions, the **medial
parabrachial nucleus**).

**The pontine respiratory group is NOT the Kölliker-Fuse nucleus.** The
**Kölliker-Fuse nucleus** is the **anatomically delimited principal
respiratory rhythm modulator**; the **pontine respiratory group** is
the **broader functional concept** that **includes** the Kölliker-Fuse
nucleus. They are **STRUCTURAL SIBLINGS** at the tree level — but the
pontine respiratory group **functionally INCLUDES** the Kölliker-Fuse
nucleus. **This is the primary source of confusion for this module.**

**The pontine respiratory group is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
**Unlike the lateral parabrachial nucleus** (which **projects to** the
central nucleus of the amygdala and the BNST), the **pontine respiratory
group does NOT project to the SLEA** — it projects to the **medullary
respiratory centers**, the **nucleus ambiguus**, the **solitary
nucleus**, and the **hypothalamus**.

Prose Composition (functional grouping — not structural children)
-----------------------------------------------------------------
The pontine respiratory group is a **functional grouping** that
**includes** the following **components** — documented as **prose**, not
as structural children:

*   **Kölliker-Fuse nucleus** — the **anatomically delimited principal
    respiratory rhythm modulator**. It is the **inspiratory off-switch**
    (the Hering-Breuer reflex), the **apneustic center** function, and
    the **laryngeal modulator** for postinspiratory airway control. It
    is a **structural sibling** of the pontine respiratory group at the
    tree level (both are children of the subparabrachial_nucleus) — but
    it is **functionally INCLUDED** in the pontine respiratory group.

*   **Adjacent subparabrachial neurons** — the **respiratory neurons in
    the subparabrachial region** that are **not anatomically part of the
    Kölliker-Fuse nucleus** but are **functionally part of the pontine
    respiratory group**. These include **interneurons** and **projection
    neurons** that are **intermingled** with the Kölliker-Fuse nucleus
    and that **contribute** to the **pontine respiratory rhythm
    modulation** and **cardiorespiratory integration**.

*   **Medial parabrachial nucleus (in some classical definitions)** —
    the **respiratory and autonomic relay** that **provides afferent
    input to** the Kölliker-Fuse nucleus and the pontine respiratory
    group. **In the tree**, the medial parabrachial nucleus is **not
    included** in the pontine respiratory group (the tree wires the
    pontine respiratory group as a **child of the subparabrachial
    nucleus** only). **In some classical literature**, the pontine
    respiratory group is **defined as including** the medial parabrachial
    nucleus. **This is a tree-wiring decision**, not a claim that the
    classical functional grouping is wrong.

**These components are prose, not structural children.** The tree wires
the **pontine respiratory group** as a **single leaf** under the
subparabrachial_nucleus sub-container — the **Kölliker-Fuse nucleus**
(its structural sibling), the **adjacent subparabrachial neurons**, and
the **medial parabrachial nucleus** (in classical definitions) are
**prose**, not structural children. Consumers that need
**component-level** resolution should consult the references, not the
tree.

The Pontine Respiratory Group / Kölliker-Fuse Nucleus Boundary
-------------------------------------------------------------
This is the **sibling-that-includes-sibling** boundary — the **defining
relationship** for this module:

*   **Pontine respiratory group** (this module) — the **broader
    functional concept** that **includes** the **Kölliker-Fuse nucleus**
    and the **adjacent subparabrachial neurons**.

*   **Kölliker-Fuse nucleus**
    (``.../subparabrachial_nucleus/kolliker_fuse_nucleus/``) — the
    **anatomically delimited principal respiratory rhythm modulator**.

**They are STRUCTURAL SIBLINGS at the tree level** — both are children
of the subparabrachial_nucleus — **but the pontine respiratory group
functionally INCLUDES the Kölliker-Fuse nucleus**. **This relationship
is unusual** — consumers must **not** conflate the pontine respiratory
group with the Kölliker-Fuse nucleus (they are **different levels of
abstraction** — one is a functional grouping, the other is an
anatomically delimited nucleus), but they must **also not assume they
are functionally disjoint** (the pontine respiratory group
**functionally contains** the Kölliker-Fuse nucleus). **This is the
primary source of confusion** for this module — the
**sibling-that-includes-sibling** relationship.

The Pontine Respiratory Group / Subparabrachial Nucleus Boundary
----------------------------------------------------------------
This is the **functional grouping vs. parent** boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group** — one of the two structural
    children of the subparabrachial nucleus.

*   **Subparabrachial nucleus**
    (``.../subparabrachial_nucleus/``) — the **pontine respiratory
    center** — it **contains** the **Kölliker-Fuse nucleus** and the
    **pontine respiratory group**.

**The pontine respiratory group is a child of the subparabrachial
nucleus.** Consumers must **not** conflate the pontine respiratory
group with the **subparabrachial nucleus**.

The Pontine Respiratory Group / Medial Parabrachial Nucleus Boundary
--------------------------------------------------------------------
This is the **aunt/uncle in the tree, but included in some classical
definitions** boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group** — in the tree, it **does NOT
    include** the medial parabrachial nucleus.

*   **Medial parabrachial nucleus**
    (``.../parabrachial_area/medial_parabrachial_nucleus/``) — the
    **respiratory and autonomic relay** — a sibling of the
    subparabrachial nucleus (an "aunt/uncle" of the pontine respiratory
    group). **In some classical definitions**, it is **included** in
    the pontine respiratory group.

**They are DIFFERENT STRUCTURES** — the **medial parabrachial nucleus**
is the **respiratory and autonomic relay**; the **pontine respiratory
group** is the **pontine respiratory rhythm modulator**. **In the
tree**, the pontine respiratory group **does NOT include** the medial
parabrachial nucleus. **Functionally**, the medial parabrachial nucleus
**provides afferent input to** the pontine respiratory group. Consumers
must **not** assume the tree's structural wiring matches every
classical definition — see the *Classical vs. Tree Wiring Boundary*
below.

The Pontine Respiratory Group / Lateral Parabrachial Nucleus Boundary
---------------------------------------------------------------------
This is the **aunt/uncle** boundary — **respiratory rhythm vs.
visceral-sensory/pain/aversion**:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Lateral parabrachial nucleus**
    (``.../parabrachial_area/lateral_parabrachial_nucleus/``) — the
    **visceral-sensory and pain/aversion relay**.

**They are DIFFERENT STRUCTURES** — different functional systems
(respiratory rhythm vs. visceral-sensory/pain/aversion). Consumers must
**not** conflate the pontine respiratory group with the lateral
parabrachial nucleus.

The Pontine Respiratory Group / Superior Cerebellar Peduncle Boundary
---------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the
**etymological origin of the name**:

*   **Pontine respiratory group** (this module) — the **grey-matter
    functional grouping** that is dorsal to the superior cerebellar
    peduncle.

*   **Superior cerebellar peduncle** (brachium conjunctivum) — the
    **white-matter tract** that carries cerebellar efferents from the
    dentate and interposed nuclei to the red nucleus and the thalamus.

**They are DIFFERENT STRUCTURES.** The **functional grouping** is grey
matter; the **peduncle** is white matter. The functional grouping is
**dorsal to** the peduncle; it is **not** the peduncle. **This
distinction is the etymological origin of the name "parabrachial"**
("para-" = alongside, "brachium" = the superior cerebellar peduncle) —
and it is a **classic source of confusion**. Consumers must **not**
conflate the pontine respiratory group with the superior cerebellar
peduncle.

The Pontine Respiratory Group / Locus Coeruleus Boundary
--------------------------------------------------------
This is the **anatomically adjacent** boundary — **respiratory rhythm
vs. noradrenergic nucleus**:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic nucleus** — the **principal source of
    norepinephrine** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, etc. vs. norepinephrine), different functional systems
(respiratory rhythm vs. noradrenergic arousal). They are **anatomically
adjacent** — this proximity is a **classic source of confusion** —
consumers must **not** conflate the pontine respiratory group with the
locus coeruleus.

The Pontine Respiratory Group / Solitary Nucleus Boundary
---------------------------------------------------------
This is the **upstream source vs. pontine rhythm modulator** boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Solitary nucleus** (nucleus tractus solitarius,
    ``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``)
    — the **medullary visceral-afferent hub** for **CN VII, IX, and X**.

**The solitary nucleus is the upstream source** — it **projects to** the
**medial parabrachial nucleus** (which in turn **projects to** the
pontine respiratory group) and, to a lesser extent, **directly** to the
**Kölliker-Fuse nucleus** within the pontine respiratory group. The
**pontine respiratory group** (here) is the **pontine respiratory
rhythm modulator**. They are **DIFFERENT STRUCTURES** — the **solitary
nucleus** is **medullary** and **upstream**; the **pontine respiratory
group** is **pontine** and **downstream**. **This distinction is
clinically load-bearing** — a **solitary nucleus** lesion causes
**impaired respiratory afferent integration**; a **pontine respiratory
group** lesion causes **apneustic breathing**. Consumers must **not**
conflate the pontine respiratory group with the solitary nucleus.

The Pontine Respiratory Group / Retrotrapezoid Nucleus Boundary
---------------------------------------------------------------
This is the **central chemoreceptor** boundary — **upstream vs.
downstream**:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Retrotrapezoid nucleus (RTN)**
    (``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
    — the **medullary central chemoreceptor**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary chemoreception). The RTN **projects to** the **medial
parabrachial nucleus** (which projects to the pontine respiratory
group); the pontine respiratory group **modulates** the medullary
respiratory centers. **This distinction is clinically load-bearing** —
an **RTN** lesion causes **central hypoventilation** (loss of CO₂
chemoreception); a **pontine respiratory group** lesion causes
**apneustic breathing**. Consumers must **not** conflate the pontine
respiratory group with the retrotrapezoid nucleus.

The Pontine Respiratory Group / Ventral Respiratory Group Boundary
------------------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary pattern generator**
boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Ventral respiratory group (VRG)**
    (``.../medulla_oblongata/ventral_respiratory_group/``) — the
    **medullary respiratory pattern generator**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary rhythm generation). The pontine respiratory group **projects
to** the VRG (especially the **pre-Bötzinger complex**) and **modulates**
the respiratory rhythm. **This distinction is clinically load-bearing**
— a **pontine respiratory group** lesion causes **apneustic breathing**;
a **VRG** lesion causes **loss of respiratory rhythm**. Consumers must
**not** conflate the pontine respiratory group with the ventral
respiratory group.

The Pontine Respiratory Group / Pre-Bötzinger Complex Boundary
--------------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary rhythm generator**
boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Pre-Bötzinger complex** — the **medullary respiratory rhythm
    generator** within the **ventral respiratory group**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine modulation vs. medullary
rhythm generation). **This distinction is clinically load-bearing** —
the **pre-Bötzinger complex** is the **primary rhythm generator**; the
**pontine respiratory group** is a **modulator** of that rhythm.
Consumers must **not** conflate the pontine respiratory group with the
pre-Bötzinger complex.

The Pontine Respiratory Group / Dorsal Respiratory Group Boundary
-----------------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary inspiratory center**
boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Dorsal respiratory group (DRG)**
    (``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
    — the **medullary inspiratory center**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary inspiratory drive). The pontine respiratory group **modulates**
the DRG (indirectly, via the VRG and the pre-Bötzinger complex) for
**respiratory phase switching**. Consumers must **not** conflate the
pontine respiratory group with the dorsal respiratory group.

The Pontine Respiratory Group / Hering-Breuer Reflex Boundary
-------------------------------------------------------------
This is the **structure vs. circuit** boundary:

*   **Pontine respiratory group** (this module) — **one node** in the
    Hering-Breuer reflex circuit — the **pontine inspiratory
    off-switch**.

*   **Hering-Breuer reflex** — the **vagally mediated inspiratory
    off-switch reflex** that **inhibits inspiration** in response to
    **lung inflation** — its **afferent limb** is the **pulmonary
    stretch receptors** (via the **vagus nerve** and the **solitary
    nucleus**); its **central node** is the **Kölliker-Fuse nucleus**
    (and the **pontine respiratory group**); its **efferent limb** is
    the **medullary respiratory centers** (DRG and VRG).

**They are DIFFERENT CONCEPTS** — the **pontine respiratory group** is a
**functional grouping**; the **Hering-Breuer reflex** is a **circuit**.
**This distinction is clinically load-bearing** — a **Hering-Breuer
reflex** deficit causes **apneustic breathing** and **impaired
inspiratory off-switch**. Consumers must **not** conflate the pontine
respiratory group with the Hering-Breuer reflex.

The Pontine Respiratory Group / Apneustic Center and Pneumotaxic Center Boundary
-------------------------------------------------------------------------------
This is the **structure vs. historical functional concept** boundary:

*   **Pontine respiratory group** (this module) — the **modern anatomical
    and functional concept** that **contains** the **Kölliker-Fuse
    nucleus**.

*   **Apneustic center** and **pneumotaxic center** — the **historical
    functional concepts** of **distinct pontine respiratory centers**.
    **Modern understanding** — the **pneumotaxic center** is the
    **Kölliker-Fuse nucleus** (and the **pontine respiratory group**);
    the **apneustic center** is **not a distinct nucleus** —
    **apneusis** results from **loss** of the Kölliker-Fuse nucleus (or
    its connections), **not** from **activation** of a **separate
    apneustic center**.

**They are DIFFERENT CONCEPTS** — the **pontine respiratory group** is
the **modern anatomical and functional concept**; the **apneustic
center** and **pneumotaxic center** are **historical functional
concepts**. Consumers must **not** treat the apneustic center or the
pneumotaxic center as **distinct structures** from the pontine
respiratory group — they are **historical functional concepts** that are
**now understood** in terms of the Kölliker-Fuse nucleus and the pontine
respiratory group.

The Pontine Respiratory Group / Laryngeal Motor Nucleus Boundary
-----------------------------------------------------------------
This is the **pontine laryngeal modulation vs. medullary laryngeal motor
output** boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group** that **modulates** the
    **laryngeal motor neurons** for **postinspiratory laryngeal
    adduction**.

*   **Laryngeal motor nucleus** — the **nucleus ambiguus** (in the
    **medulla**), which **innervates** the **intrinsic laryngeal
    muscles**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine laryngeal modulation vs.
laryngeal motor output). Consumers must **not** conflate the pontine
respiratory group with the laryngeal motor nucleus.

The Pontine Respiratory Group / PPRF and Pontine Nuclei Boundary
----------------------------------------------------------------
This is the **different functional systems** boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group**.

*   **Paramedian pontine reticular formation (PPRF)** and **pontine
    nuclei** — the **horizontal saccadic burst generator** and the
    **cortico-ponto-cerebellar relay**, respectively.

**They are DIFFERENT STRUCTURES** — different functional systems
(horizontal gaze / cortico-ponto-cerebellar vs. respiratory rhythm).
Consumers must **not** conflate the pontine respiratory group with the
PPRF or the pontine nuclei.

The Pontine Respiratory Group / Pons Boundary
---------------------------------------------
This is the **functional grouping vs. great-great-grandparent** boundary:

*   **Pontine respiratory group** (this module) — the **pontine
    respiratory rhythm modulator group** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal /
    corticobulbar tracts**, the **middle cerebellar peduncle**, the
    **cranial-nerve nuclei**, and the **parabrachial area**.

**The pontine respiratory group is a great-great-grandchild of the
pons** (via parabrachial_area → subparabrachial_nucleus). Consumers must
**not** conflate the pontine respiratory group with the **whole pons**.

The Pontine Respiratory Group / SLEA Boundary
---------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Pontine respiratory group** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The pontine respiratory group is NOT part of the SLEA continuum.** It
is a **pontine respiratory rhythm modulator group**, and it carries **no
SLEA warning**. **Unlike the lateral parabrachial nucleus** (which
**projects to** the central nucleus of the amygdala and the BNST), the
**pontine respiratory group does NOT project to the SLEA** — it projects
to the **medullary respiratory centers**, the **nucleus ambiguus**, the
**solitary nucleus**, and the **hypothalamus**. The pontine respiratory
group is **SLEA-FREE without the "projects to SLEA" caveat**.

Function in the Human Brain
---------------------------
The pontine respiratory group's functions are **the pontine modulation
of respiratory rhythm and laryngeal function** — **NOT a single unified
function**:

*   **Hering-Breuer Reflex (Inspiratory Off-Switch):** The **pontine
    respiratory group** (especially the **Kölliker-Fuse nucleus**) is
    the **pontine inspiratory off-switch** of the **Hering-Breuer
    reflex** — it **receives** the **pulmonary stretch receptor**
    afferents (via the **vagus nerve** and the **solitary nucleus**) and
    **inhibits** the **medullary inspiratory centers** (DRG and VRG)
    when the **lungs are inflated** — it **terminates inspiration** and
    **initiates expiration**.

*   **Apneustic Center Function:** The **pontine respiratory group**
    **mediates** the **apneustic center** function — historically, the
    **apneustic center** was thought to be a **separate pontine center**
    that **drives inspiration**; **modern understanding** — the
    **Kölliker-Fuse nucleus** (within the pontine respiratory group) is
    the **pontine inspiratory off-switch**, and **apneusis** results
    from **loss** of the Kölliker-Fuse nucleus (or its connections),
    **not** from **activation** of a **separate apneustic center**.

*   **Laryngeal Function (Postinspiratory Phase):** The **pontine
    respiratory group** (especially the **Kölliker-Fuse nucleus**)
    **modulates** the **postinspiratory phase** of the **respiratory
    cycle** — it **controls** the **laryngeal adduction** (via the
    **nucleus ambiguus**) during the **postinspiratory phase**, which
    **regulates upper airway resistance** and **prevents aspiration**
    during **swallowing**.

*   **Cardiorespiratory Integration:** The **pontine respiratory group**
    **integrates** **respiratory** and **cardiovascular** signals — it
    **couples** the **respiratory rhythm** to the **cardiovascular
    rhythm** (the **respiratory sinus arrhythmia** — the **heart rate
    variability** that is **synchronized** with the **respiratory
    cycle**).

*   **Voluntary Control of Breathing:** The **pontine respiratory group**
    **receives** inputs from the **cerebral cortex** (via the
    **corticobulbar** and **corticopontine** pathways) — it
    **mediates** the **voluntary control of breathing** (e.g. **breath
    holding**, **voluntary hyperventilation**) by **modulating** the
    **automatic respiratory rhythm**.

*   **Defensive Behavior and Vocalization:** The **pontine respiratory
    group** **receives** inputs from the **periaqueductal gray** — it
    **contributes** to the **respiratory components** of **defensive
    behavior** (e.g. **hissing**, **vocalization**, **gasping**) and
    **vocalization** (the **respiratory control** of **speech** and
    **emotional vocalizations**).

*   **NOT a neural processor in the classical sense.** The pontine
    respiratory group is a **rhythm modulator group** — it **receives**
    ascending respiratory and autonomic afferents (from the solitary
    nucleus and the medial parabrachial nucleus) and **projects** them to
    the **medullary respiratory centers** (DRG and VRG), the **nucleus
    ambiguus**, and the **hypothalamus**. The **processing** of
    respiratory rhythm happens in the **medullary respiratory centers**
    (the **pre-Bötzinger complex** in the VRG is the **primary rhythm
    generator**), the **pontine respiratory group** (the **pontine
    respiratory rhythm modulator**), and the **hypothalamus** (autonomic
    regulation). The **pontine respiratory group** is the **pontine
    modulator** of the **medullary respiratory rhythm**.

**The unifying theme:** the pontine respiratory group is the **pontine
respiratory rhythm modulator group** — the **principal pontine
respiratory rhythm modulator group** that **includes** the
**Kölliker-Fuse nucleus** and the **adjacent subparabrachial neurons**.
It is a **functional grouping** (not a single anatomically delimited
nucleus), **SLEA-FREE** (and does **not** project to the SLEA, unlike
the lateral parabrachial nucleus), and **NOT the superior cerebellar
peduncle** — the **peduncle** is the white-matter tract that the
functional grouping is **dorsal to**.

Associated Disorders
--------------------
The pontine respiratory group has **no named "pontine respiratory group
syndrome"** — its clinical associations are **component-specific** (the
Kölliker-Fuse nucleus and the adjacent subparabrachial neurons) and
**function-specific**:

*   **Pontine Respiratory Group Lesion — Apneustic Breathing:** A lesion
    of the **pontine respiratory group** (especially the
    **Kölliker-Fuse nucleus**) causes **apneustic breathing** —
    **prolonged inspiratory pauses** with **brief expiratory phases** —
    because the **inspiratory off-switch** (the **Hering-Breuer reflex**
    and the **pneumotaxic center** function) is **lost**. **The
    apneustic center** function of the pontine respiratory group is the
    **substrate** of this pattern.

*   **Pontine Respiratory Group Lesion — Impaired Hering-Breuer
    Reflex:** A lesion of the **pontine respiratory group** (especially
    the **Kölliker-Fuse nucleus**) causes **impaired Hering-Breuer
    reflex** — the **inspiratory off-switch** in response to **lung
    stretch** is **lost** — leading to **impaired respiratory phase
    switching** and **respiratory dysregulation**.

*   **Pontine Respiratory Group Lesion — Laryngeal Dysfunction:** A
    lesion of the **pontine respiratory group** (especially the
    **Kölliker-Fuse nucleus**) causes **laryngeal dysfunction** — the
    **postinspiratory phase** of the **respiratory cycle** is **lost**,
    leading to **impaired upper airway resistance** control — this can
    contribute to **sleep-disordered breathing** (e.g. **obstructive
    sleep apnea**), **laryngeal stridor**, and **impaired protective
    airway reflexes** (aspiration risk).

*   **Pontine Respiratory Group Lesion — Impaired Cardiorespiratory
    Integration:** A lesion of the **pontine respiratory group** causes
    **impaired cardiorespiratory integration** — the **respiratory
    sinus arrhythmia** (heart rate variability synchronized with
    breathing) is **reduced or lost**, and the **coupling** of
    **respiratory** and **cardiovascular** rhythms is **impaired**.

*   **Central Sleep Apnea — Pontine Respiratory Group Involvement:**
    **Central sleep apnea** is a **respiratory disorder** characterized
    by **absent respiratory effort** during sleep — it is caused by
    **dysfunction** of the **central respiratory control network**,
    including the **pontine respiratory group**, the **medial
    parabrachial nucleus**, the **retrotrapezoid nucleus**, and the
    **medullary respiratory centers**. **The pontine respiratory group**
    is **one of the neural substrates** of **central respiratory
    control**, and its dysfunction may **contribute** to **central sleep
    apnea**.

*   **Obstructive Sleep Apnea (OSA) — Pontine Respiratory Group
    Involvement:** **Obstructive sleep apnea** is a **respiratory
    disorder** characterized by **recurrent upper airway collapse**
    during sleep — the **pontine respiratory group** (especially the
    **Kölliker-Fuse nucleus**) **modulates** the **laryngeal** and
    **pharyngeal** motor neurons for **upper airway patency** during the
    **respiratory cycle**. **Pontine respiratory group dysfunction** may
    **contribute** to **impaired upper airway control** and **OSA**
    (especially in **REM sleep**, when the **pontine respiratory group**
    and other **pontine respiratory modulators** are **less active**).

*   **Sudden Infant Death Syndrome (SIDS) — Pontine Respiratory Group
    Involvement:** **SIDS** is a **sudden unexplained death** of an
    infant during sleep — it has been **associated** with
    **abnormalities** in the **medullary and pontine respiratory and
    autonomic control network**, including the **pontine respiratory
    group** (reduced **serotonin** and **glutamate** markers, reduced
    **neurokinin-1** receptor binding). **The pontine respiratory
    group** is **one of the neural substrates** of **cardiorespiratory
    integration**, and its dysfunction may **contribute** to **SIDS**.

*   **Congenital Central Hypoventilation Syndrome (CCHS) — Pontine
    Respiratory Group Involvement:** **CCHS** is a **congenital
    respiratory disorder** characterized by **failure of automatic
    control of breathing** — it is caused by **PHOX2B** mutations, which
    affect the **autonomic nervous system** and the **brainstem
    respiratory and autonomic control network**, including the
    **pontine respiratory group**. **The pontine respiratory group** is
    **one of the neural substrates** of **central respiratory control**,
    and its dysfunction may **contribute** to **CCHS**.

*   **Rett Syndrome — Pontine Respiratory Group Involvement:** **Rett
    syndrome** is a **neurodevelopmental disorder** caused by **MECP2**
    mutations — it is characterized by **autonomic dysfunction**,
    including **respiratory dysregulation** (**apneustic breathing**,
    **breath-holding**, **hyperventilation**). The **pontine
    respiratory group** is **one of the neural substrates** of
    **respiratory rhythm modulation**, and its dysfunction may
    **contribute** to the **respiratory phenotype** of **Rett
    syndrome**.

*   **Opioid-Induced Respiratory Depression — Pontine Respiratory Group
    Involvement:** **Opioid-induced respiratory depression** is a
    **life-threatening side effect** of **opioid analgesics** — the
    **pontine respiratory group** and other **pontine respiratory
    modulators** express **μ-opioid receptors**, and **opioid
    agonists** **suppress** their **activity** — contributing to
    **respiratory depression**, **apneusis**, and **apnea**.

*   **No Named "Pontine Respiratory Group Syndrome":** The pontine
    respiratory group is a **functional grouping** — it has **no named
    clinical syndrome**. Its clinical relevance is **component-specific**
    (the Kölliker-Fuse nucleus and the adjacent subparabrachial
    neurons) and **function-specific** (Hering-Breuer reflex, apneustic
    center function, laryngeal function, cardiorespiratory integration).

**What is NOT here:** The pontine respiratory group is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), or **trigeminal neuralgia** (trigeminal nerve root). Its
clinical relevance is **respiratory-specific**, via the **Hering-Breuer
reflex**, **apneustic center** function, **laryngeal function**, and
**cardiorespiratory integration** it subserves. **No named pontine
respiratory group syndrome exists.**

Lateralization Notes
--------------------
This is the **single** pontine respiratory group module. The pontine
respiratory group is **bilateral in real anatomy** (left and right), but
the tree wires it as a **single module** — and the module carries **NO
warning at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **pontine_respiratory_group** module (here) is a **single module**
    that represents the **bilateral pontine respiratory group**. The
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level — the module is a
    **single, bilateral representation**.

*   **Bilateral Respiratory Input and Output (Structural Fact, NOT a
    Lateralization Warning):** The **pontine respiratory group**
    **receives** respiratory afferents from the **solitary nucleus** and
    the **medial parabrachial nucleus** — the projections are **largely
    bilateral**. The **pontine respiratory group** **projects** to the
    **medullary respiratory centers**, the **nucleus ambiguus**, the
    **solitary nucleus**, and the **hypothalamus** — **bilaterally**.
    This **bilateral input and output** is a **structural fact** of the
    **respiratory control system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **bilateral
    modulation** of respiratory rhythm.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The pontine
    respiratory group is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the pontine
    respiratory group. **Unlike the lateral parabrachial nucleus**
    (which **projects to** the central nucleus of the amygdala and the
    BNST), the **pontine respiratory group does NOT project to the
    SLEA** — it projects to the **medullary respiratory centers**, the
    **nucleus ambiguus**, the **solitary nucleus**, and the
    **hypothalamus**.

*   **NO Amygdala-Lateralization Warning of their own (the pontine
    respiratory group is RESPIRATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The pontine respiratory
    group is a **pontine respiratory rhythm modulator group** —
    consumers must **not** conflate it with the **amygdala** or with the
    **fear circuit**.

**A consumer that sees "pontine_respiratory_group" must understand that
the module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **bilateral respiratory input
and output** are **structural facts**, not lateralizations. The pontine
respiratory group is a **strict-single module with NO warning at the
module level** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** pontine respiratory group as a **single module** — it
    does **not** import left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../subparabrachial_nucleus/kolliker_fuse_nucleus/``,
    ``.../subparabrachial_nucleus/``, ``.../parabrachial_area/``,
    ``.../pons/tegmentum/``, ``.../medulla_oblongata/``,
    ``.../midbrain/``, ``.../diencephalon/``, or any other container.
    The pontine respiratory group's relationships to the **Kölliker-Fuse
    nucleus**, the **subparabrachial nucleus**, the **medial
    parabrachial nucleus**, the **lateral parabrachial nucleus**, the
    **superior cerebellar peduncle**, the **locus coeruleus**, the
    **solitary nucleus**, the **retrotrapezoid nucleus**, the **ventral
    respiratory group**, the **pre-Bötzinger complex**, the **dorsal
    respiratory group**, the **Hering-Breuer reflex**, the **apneustic
    center**, the **pneumotaxic center**, the **laryngeal motor
    nucleus**, the **PPRF**, the **pontine nuclei**, the **pons**, and
    the **SLEA continuum** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **Kölliker-Fuse
    nucleus** (a **structural sibling** at the tree level) is
    **functionally INCLUDED** in the pontine respiratory group, but it
    is **not wired as a structural child** (that would create a
    **structural cycle**). The **adjacent subparabrachial neurons** and
    the **medial parabrachial nucleus** (in some classical definitions)
    are **functionally included** in the pontine respiratory group, but
    are **prose**, not structural children. Consumers must not assume
    any exist as children; resolve component-level detail through the
    references.
*   **SIBLING-THAT-INCLUDES-SIBLING — the pontine respiratory group is a
    SIBLING of the Kölliker-Fuse nucleus at the tree level, but it
    INCLUDES the Kölliker-Fuse nucleus functionally.** This is a
    **unique tree-wiring decision** — consumers must **not** assume that
    "sibling at the tree level" implies "no functional overlap" — the
    pontine respiratory group **functionally contains** its sibling (the
    Kölliker-Fuse nucleus).
*   **FUNCTIONAL GROUPING — NOT a single anatomically delimited
    nucleus.** The pontine respiratory group is a **functional
    grouping** that **groups together** the **Kölliker-Fuse nucleus**
    and the **adjacent subparabrachial neurons** (and, in some classical
    definitions, the **medial parabrachial nucleus**). Consumers must
    **not** assume the pontine respiratory group is a **discrete
    anatomical nucleus**.
*   **CLASSICAL vs. TREE WIRING — the pontine respiratory group is wired
    as a child of the subparabrachial nucleus in the tree, but classical
    definitions may include the medial parabrachial nucleus.** This is a
    **tree-wiring decision**, not a claim that the classical functional
    grouping is wrong. Consumers must **not** assume the tree's
    structural wiring matches every classical definition — the **tree
    wiring** matches the **structural relationship** (pontine
    respiratory group as a child of the subparabrachial nucleus), not
    the **functional grouping** (which may include the medial
    parabrachial nucleus).
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **pontine respiratory group** is a **single module** that represents
    the **bilateral pontine respiratory group** — the tree does **not**
    split it into left/right. Consumers must **not** assume a left/right
    split exists at the tree level.
*   **MULTIPLE FUNCTIONALLY DISTINCT COMPONENTS — NOT a single uniform
    functional system.** The **Kölliker-Fuse nucleus** and the
    **adjacent subparabrachial neurons** are **functionally distinct
    components** of the pontine respiratory group. Consumers must **not**
    treat the pontine respiratory group as a single uniform functional
    system.
*   **APNEUSTIC CENTER AND PNEUMOTAXIC CENTER ARE HISTORICAL FUNCTIONAL
    CONCEPTS — NOT distinct structures.** The **apneustic center** and
    the **pneumotaxic center** are **historical functional concepts**
    that are **now understood** in terms of the Kölliker-Fuse nucleus
    and the pontine respiratory group. Consumers must **not** treat
    them as distinct structures.
*   **GREY-MATTER NUCLEI — NOT the superior cerebellar peduncle.** The
    **pontine respiratory group** is the **grey-matter functional
    grouping**; the **superior cerebellar peduncle** (brachium
    conjunctivum) is the **white-matter tract** that the functional
    grouping is **dorsal to**. **This distinction is the etymological
    origin of the name** ("para-brachial" = "alongside the brachium")
    and is a **classic source of confusion**. Consumers must **not**
    conflate the two.
*   **NOT the locus coeruleus — that is a noradrenergic nucleus.** The
    **locus coeruleus** is **anatomically adjacent** to the pontine
    respiratory group, but it is a **different structure**. Consumers
    must **not** conflate the two.
*   **NOT the Kölliker-Fuse nucleus, the subparabrachial nucleus, the
    medial parabrachial nucleus, or the lateral parabrachial nucleus.**
    Those are its **sibling** (Kölliker-Fuse nucleus), **parent**
    (subparabrachial nucleus), and **aunts/uncles** (medial and lateral
    parabrachial nuclei). They are **different structures**. Consumers
    must **not** conflate the pontine respiratory group with any of
    them.
*   **NOT the solitary nucleus, the retrotrapezoid nucleus, the ventral
    respiratory group, the pre-Bötzinger complex, or the dorsal
    respiratory group — those are UPSTREAM or DOWNSTREAM structures.**
    The **solitary nucleus** and **retrotrapezoid nucleus** are
    **upstream**; the **ventral respiratory group** (including the
    **pre-Bötzinger complex**) and **dorsal respiratory group** are
    **downstream**. They are **different structures**. Consumers must
    **not** conflate the pontine respiratory group with any of them.
*   **NOT the laryngeal motor nucleus — that is the NUCLEUS AMBIGUUS.**
    The **nucleus ambiguus** is the **laryngeal motor output**; the
    **pontine respiratory group** is the **pontine laryngeal modulator**.
    They are **different structures**. Consumers must **not** conflate
    the two.
*   **NOT the PPRF or the pontine nuclei — those are different
    functional systems.** The **PPRF** is the **horizontal gaze center**;
    the **pontine nuclei** are the **cortico-ponto-cerebellar relay**.
    Consumers must **not** conflate the pontine respiratory group with
    either of them.
*   **SLEA-FREE — no extended-amygdala relationship.** The pontine
    respiratory group is **not** an extended-amygdala component, and it
    carries **no SLEA warning**. **Unlike the lateral parabrachial
    nucleus** (which **projects to** the central nucleus of the amygdala
    and the BNST), the **pontine respiratory group does NOT project to
    the SLEA** — it projects to the **medullary respiratory centers**,
    the **nucleus ambiguus**, the **solitary nucleus**, and the
    **hypothalamus**. The pontine respiratory group is **SLEA-FREE
    without the "projects to SLEA" caveat**.
*   **NOT the fear-output — the pontine respiratory group is
    RESPIRATORY.** The **fear-output** structure is the **central
    nucleus**; the **fear-learning** structures are the **basolateral
    nuclei**; the **fear-modulatory / extinction** structures are the
    **basomedial nuclei**. The **pontine respiratory group** is a
    **pontine respiratory rhythm modulator group** — it is **not** part
    of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The pontine respiratory group is a local
    leaf under the subparabrachial_nucleus sub-container, not a
    cross-listed leaf.
*   **No nested cross-listing.** The pontine respiratory group has no
    nested dual-framing module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area.subparabrachial_nucleus import pontine_respiratory_group

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "subparabrachial_nucleus.pontine_respiratory_group"
    )

**Do not** assume the pontine respiratory group is a **container**. It is
a **leaf at the tree level** — the **Kölliker-Fuse nucleus** (a
structural sibling), the **adjacent subparabrachial neurons**, and the
**medial parabrachial nucleus** (in some classical definitions) are
**prose**, not structural children.

**Do not** assume the pontine respiratory group is **bilateralized at the
tree level**. The pontine respiratory group is **bilateral in real
anatomy**, but the tree wires it as a **single module** — there is **no
left/right split**.

**Do not** assume the pontine respiratory group is the **Kölliker-Fuse
nucleus**. The **Kölliker-Fuse nucleus** is the **anatomically delimited
principal respiratory rhythm modulator** — a **structural sibling** of
the pontine respiratory group at the tree level. The **pontine
respiratory group** is the **broader functional concept** that
**includes** the Kölliker-Fuse nucleus. **This is the primary source of
confusion for this module.**

**Do not** assume that "sibling at the tree level" implies "no functional
overlap." The **pontine respiratory group functionally INCLUDES its
sibling** (the Kölliker-Fuse nucleus) — **this is a unique relationship
in the tree**.

**Do not** assume the pontine respiratory group is the **superior
cerebellar peduncle**. The **superior cerebellar peduncle** is the
**white-matter tract** that the pontine respiratory group is **dorsal
to** — the "para-brachial" name reflects this **dorsal/flanking
relationship**, not identity. They are **different structures**.

**Do not** assume the pontine respiratory group is the **subparabrachial
nucleus**, the **medial parabrachial nucleus**, or the **lateral
parabrachial nucleus**. Those are its **parent** (subparabrachial
nucleus) and **aunts/uncles** (medial and lateral parabrachial nuclei).
They are **different structures**.

**Do not** assume the pontine respiratory group is the **Hering-Breuer
reflex**, the **apneustic center**, or the **pneumotaxic center**. Those
are **circuits and historical functional concepts**, not distinct
structures. The **pontine respiratory group** is **one node** in the
Hering-Breuer reflex circuit; the **apneustic center** and **pneumotaxic
center** are **historical functional concepts** that are **now
understood** in terms of the Kölliker-Fuse nucleus and the pontine
respiratory group.

**Do not** assume the pontine respiratory group is the **locus
coeruleus**. The **locus coeruleus** is the **noradrenergic nucleus** in
the **pontine tegmentum** — it is **anatomically adjacent** to the
pontine respiratory group, but it is a **different structure**.

**Do not** assume the pontine respiratory group is the **solitary
nucleus**, the **retrotrapezoid nucleus**, the **ventral respiratory
group**, the **pre-Bötzinger complex**, or the **dorsal respiratory
group**. Those are **upstream** or **downstream** structures — the
**solitary nucleus** and **retrotrapezoid nucleus** are **upstream**; the
**ventral respiratory group** (including the **pre-Bötzinger complex**)
and **dorsal respiratory group** are **downstream**.

**Do not** assume the pontine respiratory group is the **laryngeal motor
nucleus**. The **laryngeal motor nucleus** is the **nucleus ambiguus**
(in the **medulla**) — it is the **motor output**; the **pontine
respiratory group** is the **pontine laryngeal modulator**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the pontine respiratory group. **The pontine respiratory
group is SLEA-FREE** — it is **not** an extended-amygdala component, and
it is **NOT part of the fear circuit**. **Unlike the lateral parabrachial
nucleus**, the pontine respiratory group **does NOT project to the
SLEA**.

Iterating the pontine respiratory group's (empty) children (recommended
consumer pattern)::

    PONTINE_RESPIRATORY_GROUP_CHILDREN = ()
    # The pontine respiratory group is a leaf at the tree level. The
    # Kölliker-Fuse nucleus (a structural sibling), the adjacent
    # subparabrachial neurons, and the medial parabrachial nucleus (in
    # some classical definitions) are prose, not structural children.

Reaching the Kölliker-Fuse nucleus (recommended consumer pattern — the
sibling that is INCLUDED in the pontine respiratory group)::

    # The Kölliker-Fuse nucleus is the ANATOMICALLY DELIMITED principal
    # respiratory rhythm modulator — a STRUCTURAL SIBLING of the pontine
    # respiratory group at the tree level, but FUNCTIONALLY INCLUDED in
    # the pontine respiratory group:
    #
    #   .../subparabrachial_nucleus/kolliker_fuse_nucleus/
    #
    # The pontine respiratory group FUNCTIONALLY CONTAINS the
    # Kölliker-Fuse nucleus — this is a UNIQUE relationship in the tree
    # (the pontine respiratory group is a sibling that includes its
    # sibling).

Reaching the subparabrachial nucleus (recommended consumer pattern — the
parent)::

    # The subparabrachial nucleus is the PONTINE RESPIRATORY CENTER
    # parent that CONTAINS the Kölliker-Fuse nucleus and the pontine
    # respiratory group:
    #
    #   .../subparabrachial_nucleus/
    #
    # The pontine respiratory group is a CHILD of the subparabrachial
    # nucleus.

Reaching the medial parabrachial nucleus (recommended consumer pattern —
the aunt/uncle in the tree, INCLUDED in some CLASSICAL definitions)::

    # The medial parabrachial nucleus is the RESPIRATORY AND AUTONOMIC
    # RELAY (a sibling of the subparabrachial nucleus — an "aunt/uncle"
    # of the pontine respiratory group in the tree):
    #
    #   .../parabrachial_area/medial_parabrachial_nucleus/
    #
    # In the TREE, the pontine respiratory group does NOT include the
    # medial parabrachial nucleus. In some CLASSICAL definitions, the
    # pontine respiratory group is DEFINED as including the medial
    # parabrachial nucleus. FUNCTIONALLY, the medial parabrachial
    # nucleus provides afferent input to the pontine respiratory group.

Reaching the lateral parabrachial nucleus (recommended consumer pattern —
the aunt/uncle)::

    # The lateral parabrachial nucleus is the VISCERAL-SENSORY AND
    # PAIN/AVERSION RELAY (a sibling of the subparabrachial nucleus — an
    # "aunt/uncle" of the pontine respiratory group):
    #
    #   .../parabrachial_area/lateral_parabrachial_nucleus/
    #
    # The lateral parabrachial nucleus is a DIFFERENT functional system
    # from the pontine respiratory group.

Reaching the superior cerebellar peduncle (recommended consumer pattern —
the white-matter tract the functional grouping is DORSAL to)::

    # The superior cerebellar peduncle (brachium conjunctivum) is the
    # WHITE-MATTER tract that the pontine respiratory group is DORSAL to:
    #
    #   .../white_matter/.../superior_cerebellar_peduncle/  (or equivalent path)
    #
    # The pontine respiratory group is GREY MATTER that is dorsal to the
    # peduncle; the peduncle is WHITE MATTER that connects the cerebellum
    # to the midbrain and thalamus. They are DIFFERENT STRUCTURES — the
    # anatomical juxtaposition is the etymological origin of the name
    # "para-brachial" and is a classic source of confusion.

Reaching the locus coeruleus (recommended consumer pattern — the adjacent
noradrenergic nucleus)::

    # The locus coeruleus is the NORADRENERGIC nucleus in the pontine
    # tegmentum — it is ANATOMICALLY ADJACENT to the pontine respiratory
    # group, but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic (source of norepinephrine);
    # the pontine respiratory group is glutamatergic (respiratory rhythm
    # modulation). They are ANATOMICALLY ADJACENT but FUNCTIONALLY
    # DISTINCT.

Reaching the solitary nucleus (recommended consumer pattern — the
UPSTREAM source for the Hering-Breuer reflex)::

    # The solitary nucleus (nucleus tractus solitarius) is the MEDULLARY
    # visceral-afferent hub that PROVIDES the PULMONARY STRETCH RECEPTOR
    # afferents to the pontine respiratory group (via the vagus nerve)
    # for the Hering-Breuer reflex:
    #
    #   .../medulla_oblongata/solitary_nucleus/left/  (and right/)
    #
    # The solitary nucleus is UPSTREAM; the pontine respiratory group is
    # DOWNSTREAM. They are DIFFERENT STRUCTURES.

Reaching the ventral respiratory group and pre-Bötzinger complex
(recommended consumer pattern — the DOWNSTREAM medullary respiratory
pattern generator)::

    # The ventral respiratory group (VRG) — including the pre-Bötzinger
    # complex (the primary respiratory rhythm generator) — is the
    # DOWNSTREAM medullary respiratory center that the pontine
    # respiratory group MODULATES:
    #
    #   .../medulla_oblongata/ventral_respiratory_group/
    #
    # The pontine respiratory group MODULATES the VRG (especially the
    # pre-Bötzinger complex) for respiratory phase switching.

Reaching the dorsal respiratory group (recommended consumer pattern — the
DOWNSTREAM medullary inspiratory center)::

    # The dorsal respiratory group (DRG) is the DOWNSTREAM medullary
    # inspiratory center that the pontine respiratory group MODULATES
    # (indirectly, via the VRG and the pre-Bötzinger complex):
    #
    #   .../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/
    #
    # The pontine respiratory group MODULATES the DRG for respiratory
    # phase switching.

Reaching the nucleus ambiguus (recommended consumer pattern — the
DOWNSTREAM laryngeal motor output)::

    # The nucleus ambiguus (in the medulla) is the LARYNGEAL MOTOR
    # OUTPUT that the pontine respiratory group MODULATES for
    # postinspiratory laryngeal adduction:
    #
    #   .../medulla_oblongata/cranial_nerve_nuclei/left/nucleus_ambiguus/
    #
    # The pontine respiratory group MODULATES the nucleus ambiguus for
    # laryngeal function (upper airway resistance control, prevention of
    # aspiration during swallowing).

Bilateral iteration (recommended consumer pattern)::

    # The pontine respiratory group is a SINGLE module (not
    # bilateralized at the tree level). The module represents the
    # BILATERAL pontine respiratory group.
    prg_path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "subparabrachial_nucleus.pontine_respiratory_group"
    )
    # resolve prg_path through the memory/recall layer

Component-level detail (not wired — consult references)::

    # The pontine respiratory group's functional components are prose,
    # not modules:
    #   kolliker_fuse_nucleus     -> the anatomically delimited principal
    #                                respiratory rhythm modulator
    #                                (inspiratory off-switch, apneustic
    #                                center function, laryngeal modulator);
    #                                STRUCTURAL SIBLING of the pontine
    #                                respiratory group, FUNCTIONALLY
    #                                INCLUDED in the pontine respiratory
    #                                group
    #   adjacent subparabrachial  -> the respiratory neurons in the
    #   neurons                     subparabrachial region that are not
    #                                anatomically part of the Kölliker-Fuse
    #                                nucleus but are functionally part of
    #                                the pontine respiratory group
    #   medial_parabrachial       -> the respiratory and autonomic relay
    #   nucleus (in some             that provides afferent input to the
    #   classical definitions)       pontine respiratory group; INCLUDED
    #                                in some classical definitions of the
    #                                pontine respiratory group, but NOT
    #                                wired as part of the pontine
    #                                respiratory group in the tree
    #
    # Do not attempt to resolve these as sub-paths of the pontine
    # respiratory group — resolve them at the component level through
    # the references.

References
----------
*   **Canonical pontine respiratory group — historical:** Lumsden, T.
    (1923). "Observations on the respiratory centres in a cat." *Journal
    of Physiology* 57:354–367. (Historical description of the pontine
    respiratory centers — the apneustic center and the pneumotaxic
    center as distinct pontine respiratory centers.)
*   **Pontine respiratory group — modern review:** Alheid, G.F.,
    McCrimmon, D.R. (2008). "The chemical neuroanatomy of breathing."
    *Respiratory Physiology & Neurobiology* 164:3–11. (Pontine
    respiratory group — modern understanding; the Kölliker-Fuse nucleus
    as the principal component.)
*   **Kölliker-Fuse nucleus:** Dutschmann, M., Herbert, H. (2006). "The
    Kölliker-Fuse nucleus gates the postinspiratory phase of the
    respiratory cycle to control inspiratory off-switch and upper airway
    resistance in rat." *European Journal of Neuroscience* 24:1071–1084.
    (Kölliker-Fuse nucleus — the principal anatomically delimited
    component of the pontine respiratory group.)
*   **Hering-Breuer reflex:** Kubin, L., Alheid, G.F., Zuperku, E.J.,
    McCrimmon, D.R. (2006). "Central pathways of pulmonary and lower
    airway vagal afferents." *Journal of Applied Physiology* 101:618–627.
    (Hering-Breuer reflex — the pontine inspiratory off-switch; the
    pontine respiratory group as the central node.)
*   **Apneustic breathing:** Lumsden, T. (1923). "Observations on the
    respiratory centres in a cat." *Journal of Physiology* 57:354–367.
    (Apneustic breathing — the pontine respiratory group, including the
    Kölliker-Fuse nucleus, as the apneustic center.)
*   **Pneumotaxic center:** Stella, G. (1938). "On the mechanism of
    production and elimination of the 'apneustic' breathing." *Journal
    of Physiology* 93:10–21. (Pneumotaxic center — historical functional
    concept; modern understanding identifies it with the Kölliker-Fuse
    nucleus and the pontine respiratory group.)
*   **Pontine respiratory group and laryngeal function:** Dutschmann,
    M., Paton, J.F.R. (2002). "Influence of nasotrigeminal afferents on
    medullary respiratory neurones and upper airway patency in the rat."
    *Pflügers Archiv* 444:227–235. (Pontine respiratory group —
    laryngeal function; upper airway resistance control.)
*   **Cardiorespiratory integration:** Dick, T.E., Baekey, D.M., Paton,
    J.F.R., Lindsey, B.G., Morris, K.F. (2009). "Cardio-respiratory
    coupling and pattern elaboration in the brainstem." *Respiratory
    Physiology & Neurobiology* 168:17–25. (Pontine respiratory group —
    cardiorespiratory integration; respiratory sinus arrhythmia.)
*   **Central sleep apnea — pontine respiratory group involvement:**
    Dempsey, J.A., Veasey, S.C., Morgan, B.J., O'Donnell, C.P. (2010).
    "Pathophysiology of sleep apnea." *Physiological Reviews* 90:47–112.
    (Central sleep apnea — central respiratory control network including
    the pontine respiratory group.)
*   **Obstructive sleep apnea — pontine respiratory group involvement:**
    Horner, R.L. (2008). "Pathophysiology of obstructive sleep apnea."
    *Journal of Clinical Sleep Medicine* 4:557–562. (Obstructive sleep
    apnea — upper airway control; pontine respiratory group modulation
    of laryngeal and pharyngeal motor neurons.)
*   **SIDS — pontine respiratory group involvement:** Paterson, D.S.,
    Trachtenberg, F.L., Thompson, E.G., et al. (2006). "Multiple
    serotonergic brainstem abnormalities in sudden infant death
    syndrome." *JAMA* 296:2124–2132. (SIDS — brainstem respiratory and
    autonomic control network including the pontine respiratory group.)
*   **CCHS — pontine respiratory group involvement:** Weese-Mayer, D.E.,
    Berry-Kravis, E.M., Ceccherini, I., et al. (2010). "An official ATS
    clinical policy statement: congenital central hypoventilation
    syndrome." *American Journal of Respiratory and Critical Care
    Medicine* 181:626–644. (CCHS — PHOX2B mutations affecting the
    brainstem respiratory and autonomic control network including the
    pontine respiratory group.)
*   **Rett syndrome — pontine respiratory group involvement:** Ramirez,
    J.M., Ward, C.S., Neul, J.L. (2013). "Breathing challenges in Rett
    syndrome: lessons learned from humans and mice." *Respiratory
    Physiology & Neurobiology* 189:359–365. (Rett syndrome —
    respiratory dysregulation; the pontine respiratory group as a neural
    substrate.)
*   **Opioid-induced respiratory depression — pontine respiratory group
    involvement:** Pattinson, K.T.S. (2008). "Opioids and the control of
    respiration." *British Journal of Anaesthesia* 100:747–758.
    (Opioid-induced respiratory depression — pontine respiratory group
    and other pontine respiratory modulators express μ-opioid
    receptors.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the
    pontine respiratory group but functionally distinct.)
*   **Superior cerebellar peduncle (contrast — the white-matter tract the
    functional grouping is DORSAL to):** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Superior cerebellar
    peduncle — brachium conjunctivum; the white-matter tract that the
    pontine respiratory group is dorsal to.)
*   **Solitary nucleus (contrast — the MEDULLARY upstream source):**
    Saper, C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Solitary nucleus — the medullary
    visceral-afferent hub that provides pulmonary stretch receptor
    afferents to the pontine respiratory group.)
*   **Ventral respiratory group (contrast — the MEDULLARY respiratory
    pattern generator):** Feldman, J.L., Del Negro, C.A. (2006). "Looking
    for inspiration: new perspectives on respiratory rhythm." *Nature
    Reviews Neuroscience* 7:232–242. (Ventral respiratory group —
    medullary respiratory pattern generator; modulated by the pontine
    respiratory group.)
*   **Pre-Bötzinger complex (contrast — the MEDULLARY rhythm
    generator):** Smith, J.C., Ellenberger, H.H., Ballanyi, K., Richter,
    D.W., Feldman, J.L. (1991). "Pre-Bötzinger complex: a brainstem
    region that may generate respiratory rhythm in mammals." *Science*
    254:726–729. (Pre-Bötzinger complex — the primary respiratory rhythm
    generator within the ventral respiratory group; modulated by the
    pontine respiratory group.)
*   **Dorsal respiratory group (contrast — the MEDULLARY inspiratory
    center):** Bianchi, A.L., Denavit-Saubié, M., Champagnat, J. (1995).
    "Central control of breathing in mammals: neuronal circuitry,
    membrane properties, and neurotransmitters." *Physiological Reviews*
    75:1–45. (Dorsal respiratory group — medullary inspiratory center;
    modulated by the pontine respiratory group.)
*   **Nucleus ambiguus (contrast — the MEDULLARY laryngeal motor
    nucleus):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Nucleus ambiguus — laryngeal motor
    nucleus; modulated by the pontine respiratory group for
    postinspiratory laryngeal adduction.)
*   **Classical pontine respiratory group definitions vs. tree wiring
    (contrast — functional grouping vs. structural wiring):** Alheid,
    G.F., McCrimmon, D.R. (2008). "The chemical neuroanatomy of
    breathing." *Respiratory Physiology & Neurobiology* 164:3–11.
    (Classical pontine respiratory group may include the medial
    parabrachial nucleus; the tree wires the pontine respiratory group
    as a child of the subparabrachial nucleus.)
*   **SLEA (contrast — the pontine respiratory group is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the pontine
    respiratory group.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the pontine respiratory group.)
*   NeuroNames — Pontine respiratory group; FMA — Pontine respiratory
    group.
"""