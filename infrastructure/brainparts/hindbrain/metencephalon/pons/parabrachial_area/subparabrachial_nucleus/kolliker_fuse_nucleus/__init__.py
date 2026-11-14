"""
infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area.subparabrachial_nucleus.kolliker_fuse_nucleus
===================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── parabrachial_area
                └── subparabrachial_nucleus
                    ├── kolliker_fuse_nucleus   <-- THIS MODULE
                    └── pontine_respiratory_group

**Primary synonym:** Kölliker-Fuse nucleus; Kölliker-Fuse nucleus; KF; KFN;
nucleus of Kölliker-Fuse; nucleus subparabrachialis (some authors);
"the pontine inspiratory off-switch."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — a **respiratory- and
autonomically-organized** neuron cluster in the **ventral
subparabrachial region**, dorsal to the **superior cerebellar peduncle**
and lateral to the **medial parabrachial nucleus** in the **dorsal
pons**, beneath the **floor of the fourth ventricle**. It is the
**principal pontine respiratory rhythm modulator** and the **pontine
inspiratory off-switch** — the **neural substrate** of the
**Hering-Breuer reflex**, the **apneustic center** function, and
**laryngeal control** during the **respiratory cycle**.
**Part of:** The **subparabrachial_nucleus** sub-container of the
**parabrachial_area** container — specifically, the **pontine
respiratory rhythm modulation** component. The
**subparabrachial_nucleus** is the **pontine respiratory center**; the
**Kölliker-Fuse nucleus** is its **principal respiratory rhythm
modulator** child.
**Structural parent:** ``.../subparabrachial_nucleus/`` → **direct
child** of the subparabrachial_nucleus sub-container.
**Structural children:** **None.** This is a **leaf** module. The
**Hering-Breuer reflex** (a **reflex arc**), the **apneustic center**
(a **functional concept**), and the **laryngeal phase-switching
circuit** (a **functional circuit**) are documented as **prose and
boundary data**, not as structural children.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
Kölliker-Fuse nucleus is a LEAF, not a container.** It has **no
structural children**. The **Hering-Breuer reflex**, the **apneustic
center** function, and the **laryngeal phase-switching circuit** are
**circuits and functional concepts**, not structural children.
Consumers must **not** treat the Kölliker-Fuse nucleus as a container,
and must **not** assume the reflex circuits exist as sub-modules.
**Boundary status (NOT the pontine respiratory group — that is a
SIBLING):** **Boundary case — the Kölliker-Fuse nucleus is NOT the
pontine respiratory group; the pontine respiratory group is a SIBLING
under the subparabrachial_nucleus sub-container.** The **pontine
respiratory group**
(``.../subparabrachial_nucleus/pontine_respiratory_group/``) is the
**broader functional concept** that includes the **Kölliker-Fuse
nucleus** and the **adjacent subparabrachial neurons**. The
**Kölliker-Fuse nucleus** (here) is the **principal respiratory rhythm
modulator** — the **anatomically delimited nucleus** within the
broader pontine respiratory group concept. They are **DIFFERENT
STRUCTURES** — the **pontine respiratory group** is a **functional
concept** that **includes** the Kölliker-Fuse nucleus; the
**Kölliker-Fuse nucleus** is the **anatomically delimited** nucleus at
its core. **This relationship is unusual** — the pontine respiratory
group is both a **sibling** (in the tree) and a **container-like
concept** (in the classical literature) of the Kölliker-Fuse nucleus.
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
pontine respiratory group — the Kölliker-Fuse nucleus is **one
component** of the pontine respiratory group concept.
**Boundary status (NOT the subparabrachial nucleus — that is the
PARENT):** **Boundary case — the Kölliker-Fuse nucleus is NOT the
subparabrachial nucleus; the subparabrachial nucleus is the PARENT.**
The **subparabrachial nucleus**
(``.../subparabrachial_nucleus/``) is the **pontine respiratory
center** — it **contains** the **Kölliker-Fuse nucleus** and the
**pontine respiratory group**. The **Kölliker-Fuse nucleus** (here) is
the **principal respiratory rhythm modulator** — a **component** of the
subparabrachial nucleus, not the subparabrachial nucleus itself.
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
subparabrachial nucleus.
**Boundary status (NOT the medial parabrachial nucleus — that is an
AUNT/UNCLE):** **Boundary case — the Kölliker-Fuse nucleus is NOT the
medial parabrachial nucleus; the medial parabrachial nucleus is a
sibling of the subparabrachial nucleus (an "aunt/uncle" of the
Kölliker-Fuse nucleus at the tree level).** The **medial parabrachial
nucleus**
(``.../parabrachial_area/medial_parabrachial_nucleus/``) is the
**respiratory and autonomic relay** — it **provides afferent input to**
the Kölliker-Fuse nucleus. The **Kölliker-Fuse nucleus** (here) is the
**pontine respiratory rhythm modulator** that **receives** this
afferent input. They are **DIFFERENT STRUCTURES** — different
functional roles (respiratory afferent relay vs. respiratory rhythm
modulation). **However**, they are **functionally coupled** — the medial
parabrachial nucleus **provides afferent input to** the Kölliker-Fuse
nucleus. Consumers must **not** conflate the Kölliker-Fuse nucleus with
the medial parabrachial nucleus.
**Boundary status (NOT the lateral parabrachial nucleus — that is an
AUNT/UNCLE):** **Boundary case — the Kölliker-Fuse nucleus is NOT the
lateral parabrachial nucleus; the lateral parabrachial nucleus is a
sibling of the subparabrachial nucleus (an "aunt/uncle" of the
Kölliker-Fuse nucleus at the tree level).** The **lateral parabrachial
nucleus**
(``.../parabrachial_area/lateral_parabrachial_nucleus/``) is the
**visceral-sensory and pain/aversion relay**. The **Kölliker-Fuse
nucleus** (here) is the **pontine respiratory rhythm modulator**. They
are **DIFFERENT STRUCTURES** — different functional systems
(visceral-sensory/pain/aversion vs. respiratory rhythm), different
downstream targets. Consumers must **not** conflate the Kölliker-Fuse
nucleus with the lateral parabrachial nucleus.
**Boundary status (GREY-MATTER NUCLEUS — NOT the superior cerebellar
peduncle):** **Boundary case — the Kölliker-Fuse nucleus is the
GREY-MATTER NUCLEUS, NOT the superior cerebellar peduncle.** The
**superior cerebellar peduncle** (the "brachium conjunctivum") is the
**white-matter tract** that carries **cerebellar efferents** from the
**dentate nucleus** and the **interposed nucleus** to the **red
nucleus** and the **thalamus**. The **Kölliker-Fuse nucleus** (here) is
the **grey-matter neuron cluster** that is **dorsal** to the superior
cerebellar peduncle — within the **subparabrachial region**. They are
**DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**peduncle** is white matter. **This distinction is the etymological
origin of the "parabrachial" name and is a classic source of
confusion** — consumers must **not** conflate the Kölliker-Fuse nucleus
with the superior cerebellar peduncle.
**Boundary status (NOT the locus coeruleus — that is the adjacent
noradrenergic nucleus):** **Boundary case — the Kölliker-Fuse nucleus
is NOT the locus coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain —
it is in the **pontine tegmentum**, **ventromedial** to the
Kölliker-Fuse nucleus. The **Kölliker-Fuse nucleus** (here) is the
**pontine respiratory rhythm modulator**. They are **DIFFERENT
STRUCTURES** — different neurotransmitters (glutamate, etc. vs.
norepinephrine), different functional systems (respiratory rhythm
modulation vs. noradrenergic arousal). They are **anatomically
adjacent** — this proximity is a **classic source of confusion** —
consumers must **not** conflate the Kölliker-Fuse nucleus with the
locus coeruleus.
**Boundary status (NOT the solitary nucleus — that is the MEDULLARY
UPSTREAM SOURCE):** **Boundary case — the Kölliker-Fuse nucleus is NOT
the solitary nucleus.** The **solitary nucleus** (nucleus tractus
solitarius, ``.../medulla_oblongata/solitary_nucleus/left/`` and
``.../right/``) is the **medullary visceral-afferent hub** for **CN
VII, IX, and X** — including **respiratory afferents** from the
**carotid body** and **aortic body** chemoreceptors, the **lung**
stretch receptors, and the **airway** receptors. The **solitary
nucleus** is the **upstream source** — it **projects to** the **medial
parabrachial nucleus** (which in turn **projects to** the Kölliker-Fuse
nucleus). The **Kölliker-Fuse nucleus** (here) is the **pontine
respiratory rhythm modulator**. They are **DIFFERENT STRUCTURES** — the
**solitary nucleus** is **medullary** and **upstream**; the
**Kölliker-Fuse nucleus** is **pontine** and **downstream**. **This
distinction is clinically load-bearing** — a **solitary nucleus**
lesion causes **impaired respiratory afferent integration**; a
**Kölliker-Fuse nucleus** lesion causes **apneustic breathing**.
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
solitary nucleus.
**Boundary status (NOT the retrotrapezoid nucleus — that is the
MEDULLARY CENTRAL CHEMORECEPTOR):** **Boundary case — the
Kölliker-Fuse nucleus is NOT the retrotrapezoid nucleus (RTN).** The
**RTN**
(``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
is the **medullary central chemoreceptor** — it **senses CO₂ / pH** and
**drives** the **ventral respiratory group** for **respiratory
chemoreception**. The **Kölliker-Fuse nucleus** (here) is the
**pontine respiratory rhythm modulator** — it **modulates** the
**medullary respiratory centers**. They are **DIFFERENT STRUCTURES** —
different brainstem levels (pons vs. medulla), different functional
roles (pontine rhythm modulation vs. medullary chemoreception).
**This distinction is clinically load-bearing** — an **RTN** lesion
causes **central hypoventilation** (loss of CO₂ chemoreception); a
**Kölliker-Fuse nucleus** lesion causes **apneustic breathing**
(prolonged inspiratory pauses) without loss of chemoreception.
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
retrotrapezoid nucleus.
**Boundary status (NOT the ventral respiratory group — that is the
MEDULLARY RESPIRATORY PATTERN GENERATOR):** **Boundary case — the
Kölliker-Fuse nucleus is NOT the ventral respiratory group (VRG).** The
**VRG** (``.../medulla_oblongata/ventral_respiratory_group/``) is the
**medullary respiratory pattern generator** — it **contains** the
**pre-Bötzinger complex** (the **respiratory rhythm generator**), the
**nucleus ambiguus**, the **retrotrapezoid nucleus**, and other
respiratory neurons. The **Kölliker-Fuse nucleus** (here) is the
**pontine respiratory rhythm modulator** — it **modulates** the VRG
(especially the **pre-Bötzinger complex**) for **respiratory phase
switching**. They are **DIFFERENT STRUCTURES** — different brainstem
levels (pons vs. medulla), different functional roles (pontine
modulation vs. medullary rhythm generation). **This distinction is
clinically load-bearing** — a **Kölliker-Fuse nucleus** lesion causes
**apneustic breathing** (prolonged inspiratory pauses — the
**apneustic center** function is lost); a **VRG** lesion causes **loss
of respiratory rhythm** (the **pre-Bötzinger complex** is lost).
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
ventral respiratory group.
**Boundary status (NOT the pre-Bötzinger complex — that is the
MEDULLARY RHYTHM GENERATOR WITHIN the VRG):** **Boundary case — the
Kölliker-Fuse nucleus is NOT the pre-Bötzinger complex.** The
**pre-Bötzinger complex** is the **medullary respiratory rhythm
generator** — a **sub-region** of the **ventral respiratory group** in
the **medulla** that **generates** the **fundamental respiratory
rhythm** (the **eupneic rhythm** and the **gasping rhythm**). The
**Kölliker-Fuse nucleus** (here) is the **pontine respiratory rhythm
modulator** — it **modulates** the pre-Bötzinger complex for
**respiratory phase switching** and **respiratory pattern** (e.g.
**inspiratory off-switch**, **postinspiration**). They are **DIFFERENT
STRUCTURES** — different brainstem levels (pons vs. medulla), different
functional roles (pontine modulation vs. medullary rhythm generation).
**This distinction is clinically load-bearing** — the
**pre-Bötzinger complex** is the **primary rhythm generator**; the
**Kölliker-Fuse nucleus** is a **modulator** of that rhythm. Consumers
must **not** conflate the Kölliker-Fuse nucleus with the pre-Bötzinger
complex.
**Boundary status (NOT the dorsal respiratory group — that is the
MEDULLARY INSPIRATORY CENTER):** **Boundary case — the Kölliker-Fuse
nucleus is NOT the dorsal respiratory group (DRG).** The **DRG**
(``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
is the **medullary inspiratory center** — it **contains** the
**inspiratory neurons** of the **solitary nucleus** and **drives** the
**phrenic nerve** for **diaphragmatic contraction**. The
**Kölliker-Fuse nucleus** (here) is the **pontine respiratory rhythm
modulator** — it **modulates** the DRG (indirectly, via the VRG and
the pre-Bötzinger complex) for **respiratory phase switching**. They
are **DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine modulation vs. medullary
inspiratory drive). Consumers must **not** conflate the Kölliker-Fuse
nucleus with the dorsal respiratory group.
**Boundary status (NOT the Hering-Breuer reflex — that is a CIRCUIT,
not a structure):** **Boundary case — the Kölliker-Fuse nucleus is NOT
the Hering-Breuer reflex; the Hering-Breuer reflex is a CIRCUIT.** The
**Hering-Breuer reflex** is the **vagally mediated inspiratory
off-switch reflex** that **inhibits inspiration** in response to **lung
inflation** — its **afferent limb** is the **pulmonary stretch
receptors** (via the **vagus nerve** and the **solitary nucleus**); its
**central node** is the **Kölliker-Fuse nucleus** (and the **medial
parabrachial nucleus**); its **efferent limb** is the **medullary
respiratory centers** (DRG and VRG). The **Kölliker-Fuse nucleus** is
**one node** in this circuit — the **pontine inspiratory off-switch** —
not the circuit itself. **This distinction is clinically
load-bearing** — a **Hering-Breuer reflex** deficit (e.g. from a
**Kölliker-Fuse nucleus** lesion, or from a **vagal** lesion) causes
**apneustic breathing** and **impaired inspiratory off-switch**.
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
Hering-Breuer reflex.
**Boundary status (NOT the apneustic center — that is a FUNCTIONAL
CONCEPT, not a distinct nucleus):** **Boundary case — the
Kölliker-Fuse nucleus is NOT the apneustic center; the apneustic center
is a FUNCTIONAL CONCEPT.** The **apneustic center** is the **functional
concept** of the **pontine region** that **prolongs inspiration** when
the **pneumotaxic center** (the **Kölliker-Fuse nucleus**) is **removed
or lesioned** — historically, the **apneustic center** was thought to
be a **distinct pontine respiratory center** that **drives
inspiration**, and the **pneumotaxic center** was thought to be a
**separate pontine center** that **inhibits** the apneustic center.
**Modern understanding** — the **Kölliker-Fuse nucleus** is the
**pontine inspiratory off-switch** (the **pneumotaxic center**
concept), and **apneusis** results from **loss of the Kölliker-Fuse
nucleus** (or its **connections**), not from **activation** of a
**separate apneustic center**. Consumers must **not** conflate the
Kölliker-Fuse nucleus with a **distinct apneustic center** — the
**apneustic center** is a **historical functional concept** that is
**now understood** in terms of the **Kölliker-Fuse nucleus** and the
**medullary respiratory rhythm generators**.
**Boundary status (NOT the pneumotaxic center — that is a HISTORICAL
FUNCTIONAL CONCEPT synonymous with the Kölliker-Fuse nucleus):**
**Boundary case — the Kölliker-Fuse nucleus is NOT the pneumotaxic
center; the pneumotaxic center is a HISTORICAL FUNCTIONAL CONCEPT that
is now understood to correspond to the Kölliker-Fuse nucleus.** The
**pneumotaxic center** was **historically** described as a **pontine
respiratory center** that **inhibits inspiration** and **promotes
expiration** — the **functional opposite** of the **apneustic center**.
**Modern understanding** — the **pneumotaxic center** corresponds to
the **Kölliker-Fuse nucleus** (and the **medial parabrachial nucleus**
in some definitions), which **controls** the **inspiratory-expiratory
phase transition**. Consumers must **not** treat the **pneumotaxic
center** as a **distinct structure** from the Kölliker-Fuse nucleus —
the **pneumotaxic center** is a **functional concept** that is
**now identified** with the Kölliker-Fuse nucleus (and the medial
parabrachial nucleus).
**Boundary status (NOT the laryngeal motor nucleus — that is the
NUCLEUS AMBIGUUS):** **Boundary case — the Kölliker-Fuse nucleus is NOT
the laryngeal motor nucleus.** The **laryngeal motor neurons** are in
the **nucleus ambiguus** (in the **medulla**) — they **innervate** the
**intrinsic laryngeal muscles** (via the **recurrent laryngeal
nerve** and the **superior laryngeal nerve**). The **Kölliker-Fuse
nucleus** (here) is the **pontine respiratory rhythm modulator** — it
**modulates** the **laryngeal motor nucleus** (via projections to the
**nucleus ambiguus** and the **solitary nucleus**) for
**postinspiratory laryngeal adduction** (the **postinspiratory phase**
of the **respiratory cycle**, which **controls upper airway
resistance** and **prevents aspiration** during **swallowing**). They
are **DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine laryngeal modulation vs.
laryngeal motor output). Consumers must **not** conflate the
Kölliker-Fuse nucleus with the laryngeal motor nucleus.
**Boundary status (NOT the paramedian pontine reticular formation —
that is the horizontal gaze center):** **Boundary case — the
Kölliker-Fuse nucleus is NOT the paramedian pontine reticular formation
(PPRF).** The **PPRF**
(``.../pons/paramedian_pontine_reticular_formation/``) is the
**horizontal saccadic burst generator** — it **drives** the abducens
nucleus for **horizontal saccades**. The **Kölliker-Fuse nucleus**
(here) is the **pontine respiratory rhythm modulator**. They are
**DIFFERENT STRUCTURES** — different functional systems (horizontal
gaze vs. respiratory rhythm). Consumers must **not** conflate the
Kölliker-Fuse nucleus with the PPRF.
**Boundary status (NOT the pontine nuclei — those are basilar-pons
cortico-ponto-cerebellar relays):** **Boundary case — the
Kölliker-Fuse nucleus is NOT the pontine nuclei.** The **pontine
nuclei** (``.../pons/pontine_nuclei/left/`` and ``.../right/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons**. The
**Kölliker-Fuse nucleus** (here) is the **dorsal tegmental** pontine
respiratory rhythm modulator. They are **DIFFERENT STRUCTURES** —
different anatomical locations (basilar pons vs. dorsal tegmentum),
different functional systems (cortico-ponto-cerebellar vs.
respiratory). Consumers must **not** conflate the Kölliker-Fuse nucleus
with the pontine nuclei.
**Boundary status (NOT the whole pons — the pons is the
great-great-grandparent):** **Boundary case — the Kölliker-Fuse nucleus
is NOT the whole pons; the pons is the great-great-grandparent.** The
**pons** (``.../pons/``) is the **whole metencephalic brainstem
segment** — it contains the **basilar pons**, the **pontine
tegmentum**, the **pontine nuclei**, the **corticospinal /
corticobulbar tracts**, the **middle cerebellar peduncle**, the
**cranial_nerve_nuclei**, and the **parabrachial area**. The
**Kölliker-Fuse nucleus** (here) is the **principal pontine
respiratory rhythm modulator** only. Consumers must **not** conflate
the Kölliker-Fuse nucleus with the **whole pons**.
**Boundary status (MULTIPLE FUNCTIONALLY DISTINCT PROJECTION TARGETS —
NOT a single uniform functional system):** **Boundary case — the
Kölliker-Fuse nucleus is NOT a single uniform functional system; it
contains MULTIPLE projection targets that serve different respiratory
functions.** The **Kölliker-Fuse nucleus** projects to the **ventral
respiratory group** (especially the **pre-Bötzinger complex**) and the
**dorsal respiratory group** for **respiratory rhythm modulation**; it
projects to the **nucleus ambiguus** and the **solitary nucleus** for
**laryngeal function** and **postinspiratory control**; it projects to
the **hypothalamus**, the **rostral ventrolateral medulla**, and the
**nucleus ambiguus** for **cardiorespiratory integration**; and it
receives **strong inputs** from the **solitary nucleus**, the **medial
parabrachial nucleus**, and the **periaqueductal gray**. **These
projection targets are prose, not structural children.** Consumers must
**not** treat the Kölliker-Fuse nucleus as a single uniform functional
system — it is a **multiply connected pontine respiratory modulator**
with **multiple functionally distinct** projection targets.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree
level):** **Boundary case — the Kölliker-Fuse nucleus is a SINGLE
module at the tree level, even though the Kölliker-Fuse nuclei are
BILATERAL in real anatomy.** Unlike the **cranial_nerve_nuclei** module
(which has explicit ``left`` and ``right`` structural children), the
**kolliker_fuse_nucleus** module (here) is a **single module** that
represents the **bilateral Kölliker-Fuse nuclei** (left and right).
The tree does **not** split them into left/right. Consumers must
**not** assume a left/right split exists at the tree level — the
module is a **single, bilateral representation**.
**Boundary status (SLEA-FREE — the Kölliker-Fuse nucleus is NOT an
extended-amygdala component):** **Boundary case — the Kölliker-Fuse
nucleus is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **Kölliker-Fuse nucleus** is a **pontine respiratory
rhythm modulator** — it is **NOT** an extended-amygdala component, and
it carries **NO SLEA warning**. **Unlike the lateral parabrachial
nucleus** (which **projects to** the central nucleus of the amygdala
and the BNST), the **Kölliker-Fuse nucleus does NOT project to the
SLEA** — it projects to the **medullary respiratory centers**, the
**nucleus ambiguus**, the **solitary nucleus**, and the
**hypothalamus**. The Kölliker-Fuse nucleus is **SLEA-FREE without the
"projects to SLEA" caveat**.

Overview
--------
The Kölliker-Fuse nucleus is the **principal pontine respiratory rhythm
modulator** of the **subparabrachial nucleus** — a **multiply connected**
grey-matter nucleus in the **ventral subparabrachial region**, dorsal to
the **superior cerebellar peduncle** and lateral to the **medial
parabrachial nucleus** in the **dorsal pons**. It is a **leaf** module
under the subparabrachial_nucleus sub-container, and it is the **neural
substrate** of the **Hering-Breuer reflex**, the **apneustic center**
function, and **laryngeal control** during the **respiratory cycle**.

**The Kölliker-Fuse nucleus is a LEAF, not a container.** It has **no
structural children**. The **Hering-Breuer reflex** (a **reflex arc**),
the **apneustic center** (a **functional concept**), and the **laryngeal
phase-switching circuit** (a **functional circuit**) are **prose and
boundary data**, not structural children.

**The Kölliker-Fuse nucleus is GREY-MATTER, NOT the superior cerebellar
peduncle.** The **superior cerebellar peduncle** (brachium conjunctivum)
is the **white-matter tract** that the Kölliker-Fuse nucleus is **dorsal
to**. They are **DIFFERENT STRUCTURES** — the **nucleus** is grey matter;
the **peduncle** is white matter. **This distinction is the etymological
origin of the name and is a classic source of confusion.**

**The Kölliker-Fuse nucleus is NOT the pontine respiratory group.** The
**pontine respiratory group** is the **broader functional concept** that
**includes** the Kölliker-Fuse nucleus and the **adjacent
subparabrachial neurons** — they are **siblings** in the tree, but the
pontine respiratory group **includes** the Kölliker-Fuse nucleus in the
classical literature. Consumers must **not** conflate the Kölliker-Fuse
nucleus with the pontine respiratory group.

**The Kölliker-Fuse nucleus is NOT the subparabrachial nucleus, the
medial parabrachial nucleus, or the lateral parabrachial nucleus.**
Those are its **parent** (subparabrachial) and **aunts/uncles** (medial
and lateral parabrachial). They are **DIFFERENT STRUCTURES** — different
functional systems, different downstream targets. **Functionally**, the
medial parabrachial nucleus **provides afferent input to** the
Kölliker-Fuse nucleus.

**The Kölliker-Fuse nucleus is the APNEUSTIC CENTER — but the
"apneustic center" is a FUNCTIONAL CONCEPT, not a distinct nucleus.**
The **apneustic center** was **historically** described as a **distinct
pontine respiratory center** that **drives inspiration**; the
**pneumotaxic center** was **historically** described as a **separate
pontine center** that **inhibits** the apneustic center. **Modern
understanding** — the **pneumotaxic center** is the **Kölliker-Fuse
nucleus**; **apneusis** results from **loss** of the Kölliker-Fuse
nucleus (or its connections), not from **activation** of a **separate
apneustic center**. Consumers must **not** treat the **apneustic
center** as a **distinct structure** from the Kölliker-Fuse nucleus.

**The Kölliker-Fuse nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
**Unlike the lateral parabrachial nucleus** (which **projects to** the
central nucleus of the amygdala and the BNST), the **Kölliker-Fuse
nucleus does NOT project to the SLEA** — it projects to the **medullary
respiratory centers**, the **nucleus ambiguus**, the **solitary
nucleus**, and the **hypothalamus**.

Projection Composition (prose, not structural children)
-------------------------------------------------------
The Kölliker-Fuse nucleus has **multiple functionally distinct
projection targets** — documented as **prose**, not as structural
children:

*   **Respiratory rhythm modulation targets** — the Kölliker-Fuse nucleus
    **projects to** the **ventral respiratory group** (especially the
    **pre-Bötzinger complex**) and, **indirectly**, to the **dorsal
    respiratory group** — it **modulates** the **respiratory rhythm**
    and **inspiratory-expiratory phase transition** (the
    **Hering-Breuer reflex** and the **apneustic center** function).

*   **Laryngeal modulation targets** — the Kölliker-Fuse nucleus
    **projects to** the **nucleus ambiguus** and the **solitary
    nucleus** — it **modulates** the **postinspiratory phase** of the
    **respiratory cycle** (laryngeal adduction, upper airway resistance
    control, prevention of aspiration during swallowing).

*   **Cardiorespiratory integration targets** — the Kölliker-Fuse
    nucleus **projects to** the **hypothalamus**, the **rostral
    ventrolateral medulla**, and the **nucleus ambiguus** — it
    **integrates** the **respiratory** and **cardiovascular** rhythms
    (respiratory sinus arrhythmia).

*   **Afferent inputs** — the Kölliker-Fuse nucleus **receives** strong
    inputs from the **solitary nucleus** (respiratory afferents), the
    **medial parabrachial nucleus** (respiratory relay), the
    **periaqueductal gray** (defensive behavior and vocalization), the
    **hypothalamus**, and the **cerebral cortex** (voluntary control of
    breathing).

**These projection targets are prose, not structural children.** The
tree wires the **Kölliker-Fuse nucleus** as a **single leaf** under the
subparabrachial_nucleus sub-container — the **projection targets** are
**prose**, not structural children. Consumers that need
**projection-target-level** resolution should consult the references,
not the tree.

The Kölliker-Fuse Nucleus / Pontine Respiratory Group Boundary
--------------------------------------------------------------
This is the **sibling** boundary — **anatomically delimited nucleus vs.
broader functional concept**:

*   **Kölliker-Fuse nucleus** (this module) — the **anatomically
    delimited principal respiratory rhythm modulator**.

*   **Pontine respiratory group**
    (``.../subparabrachial_nucleus/pontine_respiratory_group/``) — the
    **broader functional concept** that **includes** the Kölliker-Fuse
    nucleus and the **adjacent subparabrachial neurons**.

**They are DIFFERENT STRUCTURES** — the **Kölliker-Fuse nucleus** is the
**anatomically delimited** nucleus at the core of the pontine
respiratory group; the **pontine respiratory group** is the **broader
functional concept** that **includes** the Kölliker-Fuse nucleus. **This
relationship is unusual** — the pontine respiratory group is both a
**sibling** (in the tree) and a **container-like concept** (in the
classical literature) of the Kölliker-Fuse nucleus. Consumers must
**not** conflate the Kölliker-Fuse nucleus with the pontine respiratory
group — the Kölliker-Fuse nucleus is **one component** of the pontine
respiratory group concept.

The Kölliker-Fuse Nucleus / Subparabrachial Nucleus Boundary
------------------------------------------------------------
This is the **leaf vs. parent** boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **principal
    respiratory rhythm modulator** — a **component** of the
    subparabrachial nucleus.

*   **Subparabrachial nucleus**
    (``.../subparabrachial_nucleus/``) — the **pontine respiratory
    center** — it **contains** the **Kölliker-Fuse nucleus** and the
    **pontine respiratory group**.

**The Kölliker-Fuse nucleus is a child of the subparabrachial nucleus.**
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
**subparabrachial nucleus**.

The Kölliker-Fuse Nucleus / Medial Parabrachial Nucleus Boundary
----------------------------------------------------------------
This is the **aunt/uncle** boundary — **pontine respiratory rhythm
modulation vs. respiratory and autonomic relay**:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Medial parabrachial nucleus**
    (``.../parabrachial_area/medial_parabrachial_nucleus/``) — the
    **respiratory and autonomic relay** — a sibling of the
    subparabrachial nucleus (an "aunt/uncle" of the Kölliker-Fuse
    nucleus).

**They are DIFFERENT STRUCTURES** — different functional roles
(respiratory rhythm modulation vs. respiratory afferent/autonomic
relay). **However**, they are **functionally coupled** — the medial
parabrachial nucleus **provides afferent input to** the Kölliker-Fuse
nucleus. Consumers must **not** conflate the Kölliker-Fuse nucleus with
the medial parabrachial nucleus.

The Kölliker-Fuse Nucleus / Lateral Parabrachial Nucleus Boundary
-----------------------------------------------------------------
This is the **aunt/uncle** boundary — **respiratory rhythm vs.
visceral-sensory/pain/aversion**:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Lateral parabrachial nucleus**
    (``.../parabrachial_area/lateral_parabrachial_nucleus/``) — the
    **visceral-sensory and pain/aversion relay** — a sibling of the
    subparabrachial nucleus (an "aunt/uncle" of the Kölliker-Fuse
    nucleus).

**They are DIFFERENT STRUCTURES** — different functional systems
(respiratory rhythm vs. visceral-sensory/pain/aversion). Consumers must
**not** conflate the Kölliker-Fuse nucleus with the lateral parabrachial
nucleus.

The Kölliker-Fuse Nucleus / Superior Cerebellar Peduncle Boundary
-----------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the
**etymological origin of the name**:

*   **Kölliker-Fuse nucleus** (this module) — the **grey-matter neuron
    cluster** that is dorsal to the superior cerebellar peduncle.

*   **Superior cerebellar peduncle** (brachium conjunctivum) — the
    **white-matter tract** that carries cerebellar efferents from the
    dentate and interposed nuclei to the red nucleus and the thalamus.

**They are DIFFERENT STRUCTURES.** The **nucleus** is grey matter; the
**peduncle** is white matter. The nucleus is **dorsal to** the peduncle;
it is **not** the peduncle. **This distinction is the etymological
origin of the name "parabrachial"** ("para-" = alongside, "brachium" =
the superior cerebellar peduncle) — and it is a **classic source of
confusion**. Consumers must **not** conflate the Kölliker-Fuse nucleus
with the superior cerebellar peduncle.

The Kölliker-Fuse Nucleus / Locus Coeruleus Boundary
----------------------------------------------------
This is the **anatomically adjacent** boundary — **respiratory rhythm
vs. noradrenergic nucleus**:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic nucleus** — the **principal source of
    norepinephrine** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, etc. vs. norepinephrine), different functional systems
(respiratory rhythm vs. noradrenergic arousal). They are **anatomically
adjacent** — this proximity is a **classic source of confusion** —
consumers must **not** conflate the Kölliker-Fuse nucleus with the
locus coeruleus.

The Kölliker-Fuse Nucleus / Solitary Nucleus Boundary
-----------------------------------------------------
This is the **upstream source vs. pontine rhythm modulator** boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Solitary nucleus** (nucleus tractus solitarius,
    ``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``)
    — the **medullary visceral-afferent hub** for **CN VII, IX, and X**.

**The solitary nucleus is the upstream source** — it **projects to** the
**medial parabrachial nucleus** (which in turn **projects to** the
Kölliker-Fuse nucleus) and, to a lesser extent, **directly to** the
Kölliker-Fuse nucleus (especially the **pulmonary stretch receptor**
afferents that mediate the **Hering-Breuer reflex**). The
**Kölliker-Fuse nucleus** (here) is the **pontine inspiratory
off-switch** that **receives** these afferents and **inhibits** the
**medullary inspiratory centers**. They are **DIFFERENT STRUCTURES** —
the **solitary nucleus** is **medullary** and **upstream**; the
**Kölliker-Fuse nucleus** is **pontine** and **downstream**. **This
distinction is clinically load-bearing** — a **solitary nucleus** lesion
causes **impaired respiratory afferent integration** (including **loss
of the Hering-Breuer reflex**); a **Kölliker-Fuse nucleus** lesion
causes **apneustic breathing**. Consumers must **not** conflate the
Kölliker-Fuse nucleus with the solitary nucleus.

The Kölliker-Fuse Nucleus / Retrotrapezoid Nucleus Boundary
-----------------------------------------------------------
This is the **central chemoreceptor** boundary — **upstream vs.
downstream**:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Retrotrapezoid nucleus (RTN)**
    (``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
    — the **medullary central chemoreceptor**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary chemoreception). The RTN **projects to** the **medial
parabrachial nucleus** (which projects to the Kölliker-Fuse nucleus);
the Kölliker-Fuse nucleus **modulates** the medullary respiratory
centers. **This distinction is clinically load-bearing** — an **RTN**
lesion causes **central hypoventilation** (loss of CO₂ chemoreception);
a **Kölliker-Fuse nucleus** lesion causes **apneustic breathing**.
Consumers must **not** conflate the Kölliker-Fuse nucleus with the
retrotrapezoid nucleus.

The Kölliker-Fuse Nucleus / Ventral Respiratory Group Boundary
--------------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary pattern generator**
boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Ventral respiratory group (VRG)**
    (``.../medulla_oblongata/ventral_respiratory_group/``) — the
    **medullary respiratory pattern generator**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary rhythm generation). The Kölliker-Fuse nucleus **projects to**
the VRG (especially the **pre-Bötzinger complex**) and **modulates** the
respiratory rhythm. **This distinction is clinically load-bearing** — a
**Kölliker-Fuse nucleus** lesion causes **apneustic breathing**; a
**VRG** lesion causes **loss of respiratory rhythm**. Consumers must
**not** conflate the Kölliker-Fuse nucleus with the ventral respiratory
group.

The Kölliker-Fuse Nucleus / Pre-Bötzinger Complex Boundary
----------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary rhythm generator**
boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Pre-Bötzinger complex** — the **medullary respiratory rhythm
    generator** within the **ventral respiratory group**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine modulation vs. medullary
rhythm generation). **This distinction is clinically load-bearing** —
the **pre-Bötzinger complex** is the **primary rhythm generator**; the
**Kölliker-Fuse nucleus** is a **modulator** of that rhythm. Consumers
must **not** conflate the Kölliker-Fuse nucleus with the pre-Bötzinger
complex.

The Kölliker-Fuse Nucleus / Dorsal Respiratory Group Boundary
-------------------------------------------------------------
This is the **pontine rhythm modulator vs. medullary inspiratory center**
boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Dorsal respiratory group (DRG)**
    (``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
    — the **medullary inspiratory center**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine rhythm modulation vs.
medullary inspiratory drive). The Kölliker-Fuse nucleus **modulates** the
DRG (indirectly, via the VRG and the pre-Bötzinger complex) for
**respiratory phase switching**. Consumers must **not** conflate the
Kölliker-Fuse nucleus with the dorsal respiratory group.

The Kölliker-Fuse Nucleus / Hering-Breuer Reflex Boundary
---------------------------------------------------------
This is the **structure vs. circuit** boundary:

*   **Kölliker-Fuse nucleus** (this module) — **one node** in the
    Hering-Breuer reflex circuit — the **pontine inspiratory
    off-switch**.

*   **Hering-Breuer reflex** — the **vagally mediated inspiratory
    off-switch reflex** that **inhibits inspiration** in response to
    **lung inflation** — its **afferent limb** is the **pulmonary
    stretch receptors** (via the **vagus nerve** and the **solitary
    nucleus**); its **central node** is the **Kölliker-Fuse nucleus**
    (and the **medial parabrachial nucleus**); its **efferent limb** is
    the **medullary respiratory centers** (DRG and VRG).

**They are DIFFERENT CONCEPTS** — the **Kölliker-Fuse nucleus** is a
**structure**; the **Hering-Breuer reflex** is a **circuit**. **This
distinction is clinically load-bearing** — a **Hering-Breuer reflex**
deficit (e.g. from a **Kölliker-Fuse nucleus** lesion, or from a
**vagal** lesion) causes **apneustic breathing** and **impaired
inspiratory off-switch**. Consumers must **not** conflate the
Kölliker-Fuse nucleus with the Hering-Breuer reflex.

The Kölliker-Fuse Nucleus / Apneustic Center Boundary
-----------------------------------------------------
This is the **structure vs. historical functional concept** boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine
    inspiratory off-switch** — the **modern anatomical substrate** of
    the **pneumotaxic center** function.

*   **Apneustic center** — the **historical functional concept** of a
    **distinct pontine respiratory center** that **drives inspiration**
    and is **inhibited by** the **pneumotaxic center**. **Modern
    understanding** — the **apneustic center** is **not a distinct
    nucleus** — **apneusis** results from **loss of the Kölliker-Fuse
    nucleus** (or its connections), **not** from **activation** of a
    **separate apneustic center**.

**They are DIFFERENT CONCEPTS** — the **Kölliker-Fuse nucleus** is the
**modern anatomical structure**; the **apneustic center** is a
**historical functional concept** that is **now understood** in terms of
the Kölliker-Fuse nucleus and the medullary respiratory rhythm
generators. **Consumers must not treat the apneustic center as a
distinct structure from the Kölliker-Fuse nucleus.**

The Kölliker-Fuse Nucleus / Pneumotaxic Center Boundary
-------------------------------------------------------
This is the **structure vs. historical functional concept synonymous
with the Kölliker-Fuse nucleus**:

*   **Kölliker-Fuse nucleus** (this module) — the **modern anatomical
    structure**.

*   **Pneumotaxic center** — the **historical functional concept** of a
    **pontine respiratory center** that **inhibits inspiration** and
    **promotes expiration** — **modern understanding** identifies the
    **pneumotaxic center** with the **Kölliker-Fuse nucleus** (and the
    **medial parabrachial nucleus** in some definitions).

**The pneumotaxic center is NOT a distinct structure from the
Kölliker-Fuse nucleus** — it is a **historical functional concept** that
is **now identified** with the Kölliker-Fuse nucleus (and the medial
parabrachial nucleus). Consumers must **not** treat the pneumotaxic
center as a distinct structure.

The Kölliker-Fuse Nucleus / Laryngeal Motor Nucleus Boundary
------------------------------------------------------------
This is the **pontine laryngeal modulation vs. medullary laryngeal motor
output** boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator** that **modulates** the **laryngeal motor neurons**
    for **postinspiratory laryngeal adduction**.

*   **Laryngeal motor nucleus** — the **nucleus ambiguus** (in the
    **medulla**), which **innervates** the **intrinsic laryngeal
    muscles**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine laryngeal modulation vs.
laryngeal motor output). Consumers must **not** conflate the
Kölliker-Fuse nucleus with the laryngeal motor nucleus.

The Kölliker-Fuse Nucleus / Paramedian Pontine Reticular Formation Boundary
--------------------------------------------------------------------------
This is the **horizontal-gaze** boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **pontine respiratory
    rhythm modulator**.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/paramedian_pontine_reticular_formation/``) — the
    **horizontal saccadic burst generator**.

**They are DIFFERENT STRUCTURES** — different functional systems
(horizontal gaze vs. respiratory rhythm). Consumers must **not** conflate
the Kölliker-Fuse nucleus with the PPRF.

The Kölliker-Fuse Nucleus / Pontine Nuclei Boundary
---------------------------------------------------
This is the **basilar-pons vs. dorsal-tegmentum** boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **dorsal tegmental**
    pontine respiratory rhythm modulator.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/left/`` and
    ``.../right/``) — the **cortico-ponto-cerebellar relay** in the
    **basilar pons**.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. respiratory). Consumers must **not**
conflate the Kölliker-Fuse nucleus with the pontine nuclei.

The Kölliker-Fuse Nucleus / Pons Boundary
-----------------------------------------
This is the **leaf vs. great-great-grandparent** boundary:

*   **Kölliker-Fuse nucleus** (this module) — the **principal pontine
    respiratory rhythm modulator** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal /
    corticobulbar tracts**, the **middle cerebellar peduncle**, the
    **cranial-nerve nuclei**, and the **parabrachial area**.

**The Kölliker-Fuse nucleus is a great-great-grandchild of the pons**
(via parabrachial_area → subparabrachial_nucleus). Consumers must **not**
conflate the Kölliker-Fuse nucleus with the **whole pons**.

The Kölliker-Fuse Nucleus / SLEA Boundary
-----------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Kölliker-Fuse nucleus** (this module) — **SLEA-FREE**. It is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The Kölliker-Fuse nucleus is NOT part of the SLEA continuum.** It is a
**pontine respiratory rhythm modulator**, and it carries **no SLEA
warning**. **Unlike the lateral parabrachial nucleus** (which
**projects to** the central nucleus of the amygdala and the BNST), the
**Kölliker-Fuse nucleus does NOT project to the SLEA** — it projects to
the **medullary respiratory centers**, the **nucleus ambiguus**, the
**solitary nucleus**, and the **hypothalamus**. The Kölliker-Fuse
nucleus is **SLEA-FREE without the "projects to SLEA" caveat**.

Function in the Human Brain
---------------------------
The Kölliker-Fuse nucleus's functions are **the pontine modulation of
respiratory rhythm and laryngeal function** — **NOT a single unified
function**:

*   **Hering-Breuer Reflex (Inspiratory Off-Switch):** The
    **Kölliker-Fuse nucleus** is the **pontine inspiratory off-switch**
    of the **Hering-Breuer reflex** — it **receives** the **pulmonary
    stretch receptor** afferents (via the **vagus nerve** and the
    **solitary nucleus**) and **inhibits** the **medullary inspiratory
    centers** (DRG and VRG) when the **lungs are inflated** — it
    **terminates inspiration** and **initiates expiration**. This is the
    **Hering-Breuer reflex** — the **vagally mediated inspiratory
    off-switch** that **protects the lungs from over-inflation** and
    **regulates respiratory rate and depth**.

*   **Apneustic Center Function:** The **Kölliker-Fuse nucleus**
    **mediates** the **apneustic center** function — historically, the
    **apneustic center** was thought to be a **separate pontine center**
    that **drives inspiration**; **modern understanding** — the
    **Kölliker-Fuse nucleus** is the **pontine inspiratory
    off-switch**, and **apneusis** (prolonged inspiration) results from
    **loss** of the Kölliker-Fuse nucleus (or its connections),
    **not** from **activation** of a **separate apneustic center**.

*   **Laryngeal Function (Postinspiratory Phase):** The **Kölliker-Fuse
    nucleus** **modulates** the **postinspiratory phase** of the
    **respiratory cycle** — it **controls** the **laryngeal adduction**
    (via the **nucleus ambiguus**) during the **postinspiratory phase**,
    which **regulates upper airway resistance** and **prevents
    aspiration** during **swallowing**. This is the **laryngeal
    function** of the Kölliker-Fuse nucleus — the **pontine modulation**
    of the **laryngeal motor neurons** for **protective airway
    reflexes**.

*   **Cardiorespiratory Integration:** The **Kölliker-Fuse nucleus**
    **integrates** **respiratory** and **cardiovascular** signals — it
    **couples** the **respiratory rhythm** to the **cardiovascular
    rhythm** (the **respiratory sinus arrhythmia** — the **heart rate
    variability** that is **synchronized** with the **respiratory
    cycle**).

*   **Voluntary Control of Breathing:** The **Kölliker-Fuse nucleus**
    **receives** inputs from the **cerebral cortex** (via the
    **corticobulbar** and **corticopontine** pathways) — it
    **mediates** the **voluntary control of breathing** (e.g. **breath
    holding**, **voluntary hyperventilation**) by **modulating** the
    **automatic respiratory rhythm**.

*   **Defensive Behavior and Vocalization:** The **Kölliker-Fuse nucleus**
    **receives** inputs from the **periaqueductal gray** — it
    **contributes** to the **respiratory components** of **defensive
    behavior** (e.g. **hissing**, **vocalization**, **gasping**) and
    **vocalization** (the **respiratory control** of **speech** and
    **emotional vocalizations**).

*   **NOT a neural processor in the classical sense.** The
    Kölliker-Fuse nucleus is a **rhythm modulator** — it **receives**
    ascending respiratory and autonomic afferents (from the solitary
    nucleus and the medial parabrachial nucleus) and **projects** them to
    the **medullary respiratory centers** (DRG and VRG), the **nucleus
    ambiguus**, and the **hypothalamus**. The **processing** of
    respiratory rhythm happens in the **medullary respiratory centers**
    (the **pre-Bötzinger complex** in the VRG is the **primary rhythm
    generator**), the **Kölliker-Fuse nucleus** (the **pontine
    inspiratory off-switch**), and the **hypothalamus** (autonomic
    regulation). The **Kölliker-Fuse nucleus** is the **pontine
    modulator** of the **medullary respiratory rhythm** — the **pontine
    inspiratory off-switch**.

**The unifying theme:** the Kölliker-Fuse nucleus is the **principal
pontine respiratory rhythm modulator** — the **pontine inspiratory
off-switch**, the **apneustic center** function, and the **laryngeal
modulator** for **postinspiratory airway control**. It is **multiply
connected** (respiratory rhythm, laryngeal function, cardiorespiratory
integration, voluntary control, defensive behavior), **SLEA-FREE** (and
does **not** project to the SLEA, unlike the lateral parabrachial
nucleus), and **NOT the superior cerebellar peduncle** — the **peduncle**
is the white-matter tract that the nucleus is **dorsal to**.

Associated Disorders
--------------------
The Kölliker-Fuse nucleus has **no named "Kölliker-Fuse nucleus
syndrome"** — its clinical associations are **function-specific**:

*   **Kölliker-Fuse Nucleus Lesion — Apneustic Breathing:** A lesion of
    the **Kölliker-Fuse nucleus** causes **apneustic breathing** —
    **prolonged inspiratory pauses** with **brief expiratory phases** —
    because the **inspiratory off-switch** (the **Hering-Breuer reflex**
    and the **pneumotaxic center** function) is **lost**. **The
    apneustic center** function of the Kölliker-Fuse nucleus is the
    **substrate** of this pattern. **This is the classic clinical sign
    of Kölliker-Fuse nucleus dysfunction** — **apneusis** — and it is
    the **primary clinical entity** associated with the Kölliker-Fuse
    nucleus.

*   **Kölliker-Fuse Nucleus Lesion — Impaired Hering-Breuer Reflex:** A
    lesion of the **Kölliker-Fuse nucleus** causes **impaired
    Hering-Breuer reflex** — the **inspiratory off-switch** in response
    to **lung stretch** is **lost** — leading to **impaired respiratory
    phase switching** and **respiratory dysregulation**.

*   **Kölliker-Fuse Nucleus Lesion — Laryngeal Dysfunction:** A lesion
    of the **Kölliker-Fuse nucleus** causes **laryngeal dysfunction** —
    the **postinspiratory phase** of the **respiratory cycle** is
    **lost**, leading to **impaired upper airway resistance** control —
    this can contribute to **sleep-disordered breathing** (e.g.
    **obstructive sleep apnea**), **laryngeal stridor**, and **impaired
    protective airway reflexes** (aspiration risk).

*   **Kölliker-Fuse Nucleus Lesion — Impaired Cardiorespiratory
    Integration:** A lesion of the **Kölliker-Fuse nucleus** causes
    **impaired cardiorespiratory integration** — the **respiratory sinus
    arrhythmia** (heart rate variability synchronized with breathing) is
    **reduced or lost**, and the **coupling** of **respiratory** and
    **cardiovascular** rhythms is **impaired**.

*   **Central Sleep Apnea — Kölliker-Fuse Nucleus Involvement:**
    **Central sleep apnea** is a **respiratory disorder** characterized
    by **absent respiratory effort** during sleep — it is caused by
    **dysfunction** of the **central respiratory control network**,
    including the **Kölliker-Fuse nucleus**, the **medial parabrachial
    nucleus**, the **retrotrapezoid nucleus**, and the **medullary
    respiratory centers**. **The Kölliker-Fuse nucleus** is **one of the
    neural substrates** of **central respiratory control**, and its
    dysfunction may **contribute** to **central sleep apnea**.

*   **Obstructive Sleep Apnea (OSA) — Kölliker-Fuse Nucleus
    Involvement:** **Obstructive sleep apnea** is a **respiratory
    disorder** characterized by **recurrent upper airway collapse**
    during sleep — the **Kölliker-Fuse nucleus** **modulates** the
    **laryngeal** and **pharyngeal** motor neurons for **upper airway
    patency** during the **respiratory cycle**. **Kölliker-Fuse nucleus
    dysfunction** may **contribute** to **impaired upper airway
    control** and **OSA** (especially in **REM sleep**, when the
    **Kölliker-Fuse nucleus** and other **pontine respiratory
    modulators** are **less active**).

*   **Sudden Infant Death Syndrome (SIDS) — Kölliker-Fuse Nucleus
    Involvement:** **SIDS** is a **sudden unexplained death** of an
    infant during sleep — it has been **associated** with
    **abnormalities** in the **medullary and pontine respiratory and
    autonomic control network**, including the **Kölliker-Fuse nucleus**
    (reduced **serotonin** and **glutamate** markers, reduced
    **neurokinin-1** receptor binding). **The Kölliker-Fuse nucleus** is
    **one of the neural substrates** of **cardiorespiratory
    integration**, and its dysfunction may **contribute** to **SIDS**.

*   **Congenital Central Hypoventilation Syndrome (CCHS) —
    Kölliker-Fuse Nucleus Involvement:** **CCHS** is a **congenital
    respiratory disorder** characterized by **failure of automatic
    control of breathing** — it is caused by **PHOX2B** mutations, which
    affect the **autonomic nervous system** and the **brainstem
    respiratory and autonomic control network**, including the
    **Kölliker-Fuse nucleus**. **The Kölliker-Fuse nucleus** is **one
    of the neural substrates** of **central respiratory control**, and
    its dysfunction may **contribute** to **CCHS**.

*   **Rett Syndrome — Kölliker-Fuse Nucleus Involvement:** **Rett
    syndrome** is a **neurodevelopmental disorder** caused by **MECP2**
    mutations — it is characterized by **autonomic dysfunction**,
    including **respiratory dysregulation** (**apneustic breathing**,
    **breath-holding**, **hyperventilation**). The **Kölliker-Fuse
    nucleus** is **one of the neural substrates** of **respiratory
    rhythm modulation**, and its dysfunction may **contribute** to the
    **respiratory phenotype** of **Rett syndrome**.

*   **Opioid-Induced Respiratory Depression — Kölliker-Fuse Nucleus
    Involvement:** **Opioid-induced respiratory depression** is a
    **life-threatening side effect** of **opioid analgesics** — the
    **Kölliker-Fuse nucleus** and other **pontine respiratory
    modulators** express **μ-opioid receptors**, and **opioid
    agonists** **suppress** their **activity** — contributing to
    **respiratory depression**, **apneusis**, and **apnea**.

*   **No Named "Kölliker-Fuse Nucleus Syndrome":** The Kölliker-Fuse
    nucleus is a **multiply connected** pontine respiratory rhythm
    modulator — it has **no named clinical syndrome**. Its clinical
    relevance is **function-specific** — **Hering-Breuer reflex**,
    **apneustic center** function, **laryngeal function**, and
    **cardiorespiratory integration**.

**What is NOT here:** The Kölliker-Fuse nucleus is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), or **trigeminal neuralgia** (trigeminal nerve root). Its
clinical relevance is **respiratory-specific**, via the **Hering-Breuer
reflex**, **apneustic center** function, **laryngeal function**, and
**cardiorespiratory integration** it subserves. **No named Kölliker-Fuse
nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **single** Kölliker-Fuse nucleus module. The Kölliker-Fuse
nuclei are **bilateral in real anatomy** (left and right), but the tree
wires them as a **single module** — and the module carries **NO warning
at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **kolliker_fuse_nucleus** module (here) is a **single module** that
    represents the **bilateral Kölliker-Fuse nuclei**. The tree does
    **not** split them into left/right. Consumers must **not** assume a
    left/right split exists at the tree level — the module is a
    **single, bilateral representation**.

*   **Bilateral Respiratory Input and Output (Structural Fact, NOT a
    Lateralization Warning):** The **Kölliker-Fuse nucleus** **receives**
    respiratory afferents from the **solitary nucleus** and the
    **medial parabrachial nucleus** — the projections are **largely
    bilateral**. The **Kölliker-Fuse nucleus** **projects** to the
    **medullary respiratory centers**, the **nucleus ambiguus**, the
    **solitary nucleus**, and the **hypothalamus** — **bilaterally**.
    This **bilateral input and output** is a **structural fact** of the
    **respiratory control system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **bilateral
    modulation** of respiratory rhythm.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The Kölliker-Fuse
    nucleus is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the Kölliker-Fuse nucleus.
    **Unlike the lateral parabrachial nucleus** (which **projects to**
    the central nucleus of the amygdala and the BNST), the
    **Kölliker-Fuse nucleus does NOT project to the SLEA** — it projects
    to the **medullary respiratory centers**, the **nucleus ambiguus**,
    the **solitary nucleus**, and the **hypothalamus**.

*   **NO Amygdala-Lateralization Warning of their own (the
    Kölliker-Fuse nucleus is RESPIRATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The Kölliker-Fuse
    nucleus is a **pontine respiratory rhythm modulator** — consumers
    must **not** conflate it with the **amygdala** or with the **fear
    circuit**.

**A consumer that sees "kolliker_fuse_nucleus" must understand that the
module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **bilateral respiratory input
and output** are **structural facts**, not lateralizations. The
Kölliker-Fuse nucleus is a **strict-single module with NO warning at the
module level** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** Kölliker-Fuse nuclei as a **single module** — it does
    **not** import left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../subparabrachial_nucleus/pontine_respiratory_group/``,
    ``.../subparabrachial_nucleus/``, ``.../parabrachial_area/``,
    ``.../pons/tegmentum/``, ``.../medulla_oblongata/``,
    ``.../midbrain/``, ``.../diencephalon/``, or any other container.
    The Kölliker-Fuse nucleus's relationships to the **pontine
    respiratory group**, the **subparabrachial nucleus**, the **medial
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
*   **Leaf module — no structural children.** The **Hering-Breuer
    reflex**, the **apneustic center**, and the **laryngeal
    phase-switching circuit** are documented as **prose and boundary
    data**, not as sub-modules. Consumers must not assume any exist as
    children; resolve function-level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **Kölliker-Fuse nucleus** is a **single module** that represents the
    **bilateral Kölliker-Fuse nuclei** — the tree does **not** split
    them into left/right. Consumers must **not** assume a left/right
    split exists at the tree level.
*   **MULTIPLY CONNECTED — MULTIPLE functionally distinct projection
    targets.** The **respiratory rhythm modulation**, **laryngeal
    modulation**, **cardiorespiratory integration**, **voluntary
    control of breathing**, and **defensive behavior and vocalization**
    projection targets are **prose**, not structural children. Consumers
    must **not** treat the Kölliker-Fuse nucleus as a single uniform
    functional system.
*   **APNEUSTIC CENTER IS A FUNCTIONAL CONCEPT — NOT a distinct
    structure.** The **apneustic center** is a **historical functional
    concept** that is **now understood** in terms of the Kölliker-Fuse
    nucleus and the medullary respiratory rhythm generators. Consumers
    must **not** treat the apneustic center as a distinct structure.
*   **PNEUMOTAXIC CENTER IS A FUNCTIONAL CONCEPT — SYNONYMOUS with the
    Kölliker-Fuse nucleus.** The **pneumotaxic center** is a
    **historical functional concept** that is **now identified** with
    the Kölliker-Fuse nucleus (and the medial parabrachial nucleus).
    Consumers must **not** treat the pneumotaxic center as a distinct
    structure.
*   **GREY-MATTER NUCLEUS — NOT the superior cerebellar peduncle.** The
    **Kölliker-Fuse nucleus** is the **grey-matter neuron cluster**; the
    **superior cerebellar peduncle** (brachium conjunctivum) is the
    **white-matter tract** that the nucleus is **dorsal to**. **This
    distinction is the etymological origin of the name** ("para-brachial"
    = "alongside the brachium") and is a **classic source of
    confusion**. Consumers must **not** conflate the two.
*   **NOT the locus coeruleus — that is a noradrenergic nucleus.** The
    **locus coeruleus** is **anatomically adjacent** to the
    Kölliker-Fuse nucleus, but it is a **different structure**.
    Consumers must **not** conflate the two.
*   **NOT the pontine respiratory group, the subparabrachial nucleus,
    the medial parabrachial nucleus, or the lateral parabrachial
    nucleus.** Those are its **sibling** (pontine respiratory group),
    **parent** (subparabrachial nucleus), and **aunts/uncles** (medial
    and lateral parabrachial nuclei). They are **different structures**.
    Consumers must **not** conflate the Kölliker-Fuse nucleus with any of
    them.
*   **NOT the solitary nucleus, the retrotrapezoid nucleus, the ventral
    respiratory group, the pre-Bötzinger complex, or the dorsal
    respiratory group — those are UPSTREAM or DOWNSTREAM structures.**
    The **solitary nucleus** and **retrotrapezoid nucleus** are
    **upstream**; the **ventral respiratory group** (including the
    **pre-Bötzinger complex**) and **dorsal respiratory group** are
    **downstream**. They are **different structures**. Consumers must
    **not** conflate the Kölliker-Fuse nucleus with any of them.
*   **NOT the laryngeal motor nucleus — that is the NUCLEUS AMBIGUUS.**
    The **nucleus ambiguus** is the **laryngeal motor output**; the
    **Kölliker-Fuse nucleus** is the **pontine laryngeal modulator**.
    They are **different structures**. Consumers must **not** conflate
    the two.
*   **NOT the PPRF or the pontine nuclei — those are different
    functional systems.** The **PPRF** is the **horizontal gaze center**;
    the **pontine nuclei** are the **cortico-ponto-cerebellar relay**.
    Consumers must **not** conflate the Kölliker-Fuse nucleus with
    either of them.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    Kölliker-Fuse nucleus is **not** an extended-amygdala component, and
    it carries **no SLEA warning**. **Unlike the lateral parabrachial
    nucleus** (which **projects to** the central nucleus of the amygdala
    and the BNST), the **Kölliker-Fuse nucleus does NOT project to the
    SLEA** — it projects to the **medullary respiratory centers**, the
    **nucleus ambiguus**, the **solitary nucleus**, and the
    **hypothalamus**. The Kölliker-Fuse nucleus is **SLEA-FREE without
    the "projects to SLEA" caveat**.
*   **NOT the fear-output — the Kölliker-Fuse nucleus is RESPIRATORY.**
    The **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **Kölliker-Fuse nucleus** is a **pontine respiratory
    rhythm modulator** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The Kölliker-Fuse nucleus is a local leaf
    under the subparabrachial_nucleus sub-container, not a cross-listed
    leaf.
*   **No nested cross-listing.** The Kölliker-Fuse nucleus has no nested
    dual-framing module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area.subparabrachial_nucleus import kolliker_fuse_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "subparabrachial_nucleus.kolliker_fuse_nucleus"
    )

**Do not** assume the Kölliker-Fuse nucleus is a **container**. It is a
**leaf** — the **Hering-Breuer reflex**, the **apneustic center**, and
the **laryngeal phase-switching circuit** are **prose and boundary
data**, not structural children.

**Do not** assume the Kölliker-Fuse nucleus is **bilateralized at the
tree level**. The Kölliker-Fuse nuclei are **bilateral in real
anatomy**, but the tree wires them as a **single module** — there is
**no left/right split**.

**Do not** assume the Kölliker-Fuse nucleus is the **superior cerebellar
peduncle**. The **superior cerebellar peduncle** is the **white-matter
tract** that the Kölliker-Fuse nucleus is **dorsal to** — the
"para-brachial" name reflects this **dorsal/flanking relationship**, not
identity. They are **different structures**.

**Do not** assume the Kölliker-Fuse nucleus is the **pontine respiratory
group**, the **subparabrachial nucleus**, the **medial parabrachial
nucleus**, or the **lateral parabrachial nucleus**. Those are its
**sibling** (pontine respiratory group), **parent** (subparabrachial
nucleus), and **aunts/uncles** (medial and lateral parabrachial nuclei).
They are **different structures**.

**Do not** assume the Kölliker-Fuse nucleus is the **Hering-Breuer
reflex**, the **apneustic center**, or the **pneumotaxic center**. Those
are **circuits and historical functional concepts**, not distinct
structures. The **Kölliker-Fuse nucleus** is **one node** in the
Hering-Breuer reflex circuit; the **apneustic center** and **pneumotaxic
center** are **historical functional concepts** that are **now
understood** in terms of the Kölliker-Fuse nucleus.

**Do not** assume the Kölliker-Fuse nucleus is the **locus coeruleus**.
The **locus coeruleus** is the **noradrenergic nucleus** in the
**pontine tegmentum** — it is **anatomically adjacent** to the
Kölliker-Fuse nucleus, but it is a **different structure**.

**Do not** assume the Kölliker-Fuse nucleus is the **solitary nucleus**,
the **retrotrapezoid nucleus**, the **ventral respiratory group**, the
**pre-Bötzinger complex**, or the **dorsal respiratory group**. Those are
**upstream** or **downstream** structures — the **solitary nucleus** and
**retrotrapezoid nucleus** are **upstream**; the **ventral respiratory
group** (including the **pre-Bötzinger complex**) and **dorsal
respiratory group** are **downstream**.

**Do not** assume the Kölliker-Fuse nucleus is the **laryngeal motor
nucleus**. The **laryngeal motor nucleus** is the **nucleus ambiguus**
(in the **medulla**) — it is the **motor output**; the
**Kölliker-Fuse nucleus** is the **pontine laryngeal modulator**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the Kölliker-Fuse nucleus. **The Kölliker-Fuse nucleus is
SLEA-FREE** — it is **not** an extended-amygdala component, and it is
**NOT part of the fear circuit**. **Unlike the lateral parabrachial
nucleus**, the Kölliker-Fuse nucleus **does NOT project to the SLEA**.

Iterating the Kölliker-Fuse nucleus's (empty) children (recommended
consumer pattern)::

    KOLLIKER_FUSE_NUCLEUS_CHILDREN = ()
    # The Kölliker-Fuse nucleus is a leaf. The Hering-Breuer reflex, the
    # apneustic center, and the laryngeal phase-switching circuit are
    # prose and boundary data, not structural children.

Reaching the pontine respiratory group (recommended consumer pattern —
the sibling)::

    # The pontine respiratory group is the BROADER FUNCTIONAL CONCEPT
    # that INCLUDES the Kölliker-Fuse nucleus and the adjacent
    # subparabrachial neurons:
    #
    #   .../subparabrachial_nucleus/pontine_respiratory_group/
    #
    # The Kölliker-Fuse nucleus is the ANATOMICALLY DELIMITED nucleus at
    # the core of the pontine respiratory group.

Reaching the subparabrachial nucleus (recommended consumer pattern — the
parent)::

    # The subparabrachial nucleus is the PONTINE RESPIRATORY CENTER
    # parent that CONTAINS the Kölliker-Fuse nucleus and the pontine
    # respiratory group:
    #
    #   .../subparabrachial_nucleus/
    #
    # The Kölliker-Fuse nucleus is a COMPONENT of the subparabrachial
    # nucleus.

Reaching the medial parabrachial nucleus (recommended consumer pattern —
the aunt/uncle)::

    # The medial parabrachial nucleus is the RESPIRATORY AND AUTONOMIC
    # RELAY (a sibling of the subparabrachial nucleus — an "aunt/uncle"
    # of the Kölliker-Fuse nucleus):
    #
    #   .../parabrachial_area/medial_parabrachial_nucleus/
    #
    # FUNCTIONALLY, the medial parabrachial nucleus provides afferent
    # input to the Kölliker-Fuse nucleus.

Reaching the lateral parabrachial nucleus (recommended consumer pattern —
the aunt/uncle)::

    # The lateral parabrachial nucleus is the VISCERAL-SENSORY AND
    # PAIN/AVERSION RELAY (a sibling of the subparabrachial nucleus — an
    # "aunt/uncle" of the Kölliker-Fuse nucleus):
    #
    #   .../parabrachial_area/lateral_parabrachial_nucleus/
    #
    # The lateral parabrachial nucleus is a DIFFERENT functional system
    # from the Kölliker-Fuse nucleus.

Reaching the superior cerebellar peduncle (recommended consumer pattern —
the white-matter tract the nucleus is DORSAL to)::

    # The superior cerebellar peduncle (brachium conjunctivum) is the
    # WHITE-MATTER tract that the Kölliker-Fuse nucleus is DORSAL to:
    #
    #   .../white_matter/.../superior_cerebellar_peduncle/  (or equivalent path)
    #
    # The Kölliker-Fuse nucleus is GREY MATTER that is dorsal to the
    # peduncle; the peduncle is WHITE MATTER that connects the cerebellum
    # to the midbrain and thalamus. They are DIFFERENT STRUCTURES — the
    # anatomical juxtaposition is the etymological origin of the name
    # "para-brachial" and is a classic source of confusion.

Reaching the locus coeruleus (recommended consumer pattern — the adjacent
noradrenergic nucleus)::

    # The locus coeruleus is the NORADRENERGIC nucleus in the pontine
    # tegmentum — it is ANATOMICALLY ADJACENT to the Kölliker-Fuse
    # nucleus, but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic (source of norepinephrine);
    # the Kölliker-Fuse nucleus is glutamatergic (respiratory rhythm
    # modulation). They are ANATOMICALLY ADJACENT but FUNCTIONALLY
    # DISTINCT.

Reaching the solitary nucleus (recommended consumer pattern — the
UPSTREAM source for the Hering-Breuer reflex)::

    # The solitary nucleus (nucleus tractus solitarius) is the MEDULLARY
    # visceral-afferent hub that PROVIDES the PULMONARY STRETCH RECEPTOR
    # afferents to the Kölliker-Fuse nucleus (via the vagus nerve) for
    # the Hering-Breuer reflex:
    #
    #   .../medulla_oblongata/solitary_nucleus/left/  (and right/)
    #
    # The solitary nucleus is UPSTREAM; the Kölliker-Fuse nucleus is
    # DOWNSTREAM. They are DIFFERENT STRUCTURES.

Reaching the ventral respiratory group and pre-Bötzinger complex
(recommended consumer pattern — the DOWNSTREAM medullary respiratory
pattern generator)::

    # The ventral respiratory group (VRG) — including the pre-Bötzinger
    # complex (the primary respiratory rhythm generator) — is the
    # DOWNSTREAM medullary respiratory center that the Kölliker-Fuse
    # nucleus MODULATES:
    #
    #   .../medulla_oblongata/ventral_respiratory_group/
    #
    # The Kölliker-Fuse nucleus MODULATES the VRG (especially the
    # pre-Bötzinger complex) for respiratory phase switching.

Reaching the dorsal respiratory group (recommended consumer pattern — the
DOWNSTREAM medullary inspiratory center)::

    # The dorsal respiratory group (DRG) is the DOWNSTREAM medullary
    # inspiratory center that the Kölliker-Fuse nucleus MODULATES
    # (indirectly, via the VRG and the pre-Bötzinger complex):
    #
    #   .../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/
    #
    # The Kölliker-Fuse nucleus MODULATES the DRG for respiratory phase
    # switching.

Reaching the nucleus ambiguus (recommended consumer pattern — the
DOWNSTREAM laryngeal motor output)::

    # The nucleus ambiguus (in the medulla) is the LARYNGEAL MOTOR
    # OUTPUT that the Kölliker-Fuse nucleus MODULATES for postinspiratory
    # laryngeal adduction:
    #
    #   .../medulla_oblongata/cranial_nerve_nuclei/left/nucleus_ambiguus/
    #
    # The Kölliker-Fuse nucleus MODULATES the nucleus ambiguus for
    # laryngeal function (upper airway resistance control, prevention of
    # aspiration during swallowing).

Bilateral iteration (recommended consumer pattern)::

    # The Kölliker-Fuse nucleus is a SINGLE module (not bilateralized at
    # the tree level). The module represents the BILATERAL Kölliker-Fuse
    # nuclei.
    kf_path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "subparabrachial_nucleus.kolliker_fuse_nucleus"
    )
    # resolve kf_path through the memory/recall layer

Function-level detail (not wired — consult references)::

    # The Kölliker-Fuse nucleus's functions are prose, not modules:
    #   Hering-Breuer reflex         -> pontine inspiratory off-switch;
    #                                    receives pulmonary stretch
    #                                    receptor afferents (via solitary
    #                                    nucleus); inhibits medullary
    #                                    inspiratory centers (DRG and
    #                                    VRG); terminates inspiration
    #                                    and initiates expiration
    #   Apneustic center function    -> loss of Kölliker-Fuse nucleus
    #                                    (or its connections) causes
    #                                    apneusis (prolonged inspiratory
    #                                    pauses); apneusis results from
    #                                    LOSS of the inspiratory off-
    #                                    switch, not activation of a
    #                                    separate apneustic center
    #   Laryngeal function           -> postinspiratory laryngeal
    #                                    adduction (via nucleus ambiguus);
    #                                    upper airway resistance control;
    #                                    prevention of aspiration during
    #                                    swallowing
    #   Cardiorespiratory integration -> coupling of respiratory and
    #                                    cardiovascular rhythms
    #                                    (respiratory sinus arrhythmia)
    #   Voluntary control of breathing -> receives cortical inputs;
    #                                    mediates voluntary control of
    #                                    breathing (breath holding,
    #                                    voluntary hyperventilation)
    #   Defensive behavior and vocalization -> receives periaqueductal
    #                                    gray inputs; contributes to
    #                                    respiratory components of
    #                                    defensive behavior (hissing,
    #                                    vocalization, gasping)
    #
    # Do not attempt to resolve these as sub-paths of the Kölliker-Fuse
    # nucleus — resolve them at the function level through the
    # references.

References
----------
*   **Canonical Kölliker-Fuse nucleus anatomy:** Kölliker, A. (1852).
    *Handbuch der Gewebelehre des Menschen*. (Original description of the
    nucleus.)
*   **Kölliker-Fuse nucleus — modern review:** Dutschmann, M., Herbert,
    H. (2006). "The Kölliker-Fuse nucleus gates the postinspiratory phase
    of the respiratory cycle to control inspiratory off-switch and upper
    airway resistance in rat." *European Journal of Neuroscience*
    24:1071–1084. (Kölliker-Fuse nucleus — respiratory phase switching;
    the principal pontine respiratory rhythm modulator.)
*   **Pontine respiratory group — review:** Alheid, G.F., McCrimmon,
    D.R. (2008). "The chemical neuroanatomy of breathing." *Respiratory
    Physiology & Neurobiology* 164:3–11. (Kölliker-Fuse nucleus and the
    pontine respiratory group.)
*   **Hering-Breuer reflex:** Kubin, L., Alheid, G.F., Zuperku, E.J.,
    McCrimmon, D.R. (2006). "Central pathways of pulmonary and lower
    airway vagal afferents." *Journal of Applied Physiology* 101:618–627.
    (Hering-Breuer reflex — the Kölliker-Fuse nucleus as the pontine
    inspiratory off-switch.)
*   **Apneustic breathing:** Lumsden, T. (1923). "Observations on the
    respiratory centres in a cat." *Journal of Physiology* 57:354–367.
    (Apneustic breathing — the pontine respiratory center, including the
    Kölliker-Fuse nucleus, as the apneustic center.)
*   **Pneumotaxic center:** Stella, G. (1938). "On the mechanism of
    production and elimination of the 'apneustic' breathing." *Journal
    of Physiology* 93:10–21. (Pneumotaxic center — historical functional
    concept; modern understanding identifies it with the Kölliker-Fuse
    nucleus.)
*   **Laryngeal function:** Dutschmann, M., Paton, J.F.R. (2002).
    "Influence of nasotrigeminal afferents on medullary respiratory
    neurones and upper airway patency in the rat." *Pflügers Archiv*
    444:227–235. (Kölliker-Fuse nucleus — laryngeal function; upper
    airway resistance control.)
*   **Cardiorespiratory integration:** Dick, T.E., Baekey, D.M., Paton,
    J.F.R., Lindsey, B.G., Morris, K.F. (2009). "Cardio-respiratory
    coupling and pattern elaboration in the brainstem." *Respiratory
    Physiology & Neurobiology* 168:17–25. (Kölliker-Fuse nucleus —
    cardiorespiratory integration; respiratory sinus arrhythmia.)
*   **Voluntary control of breathing:** Shea, S.A. (1996). "Behavioural
    and arousal-related influences on breathing in humans."
    *Experimental Physiology* 81:1–26. (Kölliker-Fuse nucleus — voluntary
    control of breathing; cortical inputs.)
*   **Defensive behavior and vocalization:** Subramanian, H.H., Balnave,
    R.J., Holstege, G. (2008). "The midbrain periaqueductal gray control
    of respiration." *Journal of Applied Physiology* 104:1224–1229.
    (Kölliker-Fuse nucleus — defensive behavior and vocalization;
    periaqueductal gray inputs.)
*   **Central sleep apnea — Kölliker-Fuse nucleus involvement:**
    Dempsey, J.A., Veasey, S.C., Morgan, B.J., O'Donnell, C.P. (2010).
    "Pathophysiology of sleep apnea." *Physiological Reviews* 90:47–112.
    (Central sleep apnea — central respiratory control network including
    the Kölliker-Fuse nucleus.)
*   **Obstructive sleep apnea — Kölliker-Fuse nucleus involvement:**
    Horner, R.L. (2008). "Pathophysiology of obstructive sleep apnea."
    *Journal of Clinical Sleep Medicine* 4:557–562. (Obstructive sleep
    apnea — upper airway control; Kölliker-Fuse nucleus modulation of
    laryngeal and pharyngeal motor neurons.)
*   **SIDS — Kölliker-Fuse nucleus involvement:** Paterson, D.S.,
    Trachtenberg, F.L., Thompson, E.G., et al. (2006). "Multiple
    serotonergic brainstem abnormalities in sudden infant death
    syndrome." *JAMA* 296:2124–2132. (SIDS — brainstem respiratory and
    autonomic control network including the Kölliker-Fuse nucleus.)
*   **CCHS — Kölliker-Fuse nucleus involvement:** Weese-Mayer, D.E.,
    Berry-Kravis, E.M., Ceccherini, I., et al. (2010). "An official ATS
    clinical policy statement: congenital central hypoventilation
    syndrome." *American Journal of Respiratory and Critical Care
    Medicine* 181:626–644. (CCHS — PHOX2B mutations affecting the
    brainstem respiratory and autonomic control network including the
    Kölliker-Fuse nucleus.)
*   **Rett syndrome — Kölliker-Fuse nucleus involvement:** Ramirez,
    J.M., Ward, C.S., Neul, J.L. (2013). "Breathing challenges in Rett
    syndrome: lessons learned from humans and mice." *Respiratory
    Physiology & Neurobiology* 189:359–365. (Rett syndrome —
    respiratory dysregulation; the Kölliker-Fuse nucleus as a neural
    substrate.)
*   **Opioid-induced respiratory depression — Kölliker-Fuse nucleus
    involvement:** Pattinson, K.T.S. (2008). "Opioids and the control of
    respiration." *British Journal of Anaesthesia* 100:747–758.
    (Opioid-induced respiratory depression — Kölliker-Fuse nucleus and
    other pontine respiratory modulators express μ-opioid receptors.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the
    Kölliker-Fuse nucleus but functionally distinct.)
*   **Superior cerebellar peduncle (contrast — the white-matter tract the
    nucleus is DORSAL to):** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Superior cerebellar
    peduncle — brachium conjunctivum; the white-matter tract that the
    Kölliker-Fuse nucleus is dorsal to.)
*   **Solitary nucleus (contrast — the MEDULLARY upstream source):**
    Saper, C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Solitary nucleus — the medullary
    visceral-afferent hub that provides pulmonary stretch receptor
    afferents to the Kölliker-Fuse nucleus.)
*   **Ventral respiratory group (contrast — the MEDULLARY respiratory
    pattern generator):** Feldman, J.L., Del Negro, C.A. (2006). "Looking
    for inspiration: new perspectives on respiratory rhythm." *Nature
    Reviews Neuroscience* 7:232–242. (Ventral respiratory group —
    medullary respiratory pattern generator; modulated by the
    Kölliker-Fuse nucleus.)
*   **Pre-Bötzinger complex (contrast — the MEDULLARY rhythm
    generator):** Smith, J.C., Ellenberger, H.H., Ballanyi, K., Richter,
    D.W., Feldman, J.L. (1991). "Pre-Bötzinger complex: a brainstem
    region that may generate respiratory rhythm in mammals." *Science*
    254:726–729. (Pre-Bötzinger complex — the primary respiratory rhythm
    generator within the ventral respiratory group; modulated by the
    Kölliker-Fuse nucleus.)
*   **Dorsal respiratory group (contrast — the MEDULLARY inspiratory
    center):** Bianchi, A.L., Denavit-Saubié, M., Champagnat, J. (1995).
    "Central control of breathing in mammals: neuronal circuitry,
    membrane properties, and neurotransmitters." *Physiological Reviews*
    75:1–45. (Dorsal respiratory group — medullary inspiratory center;
    modulated by the Kölliker-Fuse nucleus.)
*   **Nucleus ambiguus (contrast — the MEDULLARY laryngeal motor
    nucleus):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Nucleus ambiguus — laryngeal motor
    nucleus; modulated by the Kölliker-Fuse nucleus for postinspiratory
    laryngeal adduction.)
*   **SLEA (contrast — the Kölliker-Fuse nucleus is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the Kölliker-Fuse
    nucleus.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the Kölliker-Fuse nucleus.)
*   NeuroNames — Kölliker-Fuse nucleus; FMA — Kölliker-Fuse nucleus.
"""