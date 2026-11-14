"""
infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area
=======================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── parabrachial_area   <-- THIS MODULE
                ├── lateral_parabrachial_nucleus
                ├── medial_parabrachial_nucleus
                └── subparabrachial_nucleus
                    ├── kolliker_fuse_nucleus
                    └── pontine_respiratory_group

**Primary synonym:** Parabrachial area; parabrachial complex; parabrachial
nuclei; "the pontine visceral-sensory and respiratory-relay complex."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter complex** — a **heterogeneous collection** of
**pontine nuclei** flanking the **superior cerebellar peduncle** (the
"brachium conjunctivum") in the **dorsal pons**, beneath the **floor of
the fourth ventricle**. It is the **principal pontine relay** for
**visceral sensation**, **taste**, **pain**, **temperature**,
**respiratory control**, **autonomic regulation**, and **aversion / food
intake**.
**Part of:** The **pons** container — specifically, the **dorsal
tegmental** component. The **pons** is the **metencephalic** brainstem
segment.
**Structural parent:** ``.../pons/`` → **direct child** of the pons
container.
**Structural children:** **Three structural children** — two **leaves**
(``lateral_parabrachial_nucleus``, ``medial_parabrachial_nucleus``) and
one **sub-container** (``subparabrachial_nucleus``, which itself has two
children: ``kolliker_fuse_nucleus`` and ``pontine_respiratory_group``).
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
parabrachial area is a CONTAINER, not a leaf.** It has **three structural
children** — ``lateral_parabrachial_nucleus``,
``medial_parabrachial_nucleus``, and ``subparabrachial_nucleus``. The
``subparabrachial_nucleus`` is itself a **sub-container** with two
children (``kolliker_fuse_nucleus`` and ``pontine_respiratory_group``).
Consumers must **not** treat the parabrachial area as a leaf, and must
**not** assume the three sub-nuclei are absent — they are its **direct
structural children**.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the parabrachial area is a SINGLE module at the tree
level, even though the parabrachial nuclei are BILATERAL in real
anatomy.** Unlike the **cranial_nerve_nuclei** module (which has
explicit ``left`` and ``right`` structural children), the
**parabrachial_area** module (here) is a **single module** that
represents the **bilateral parabrachial nuclei** (left and right flanking
the superior cerebellar peduncle). The tree does **not** split them into
left/right. Consumers must **not** assume a left/right split exists at
the tree level — the module is a **single, bilateral-container
representation**. Any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere.
**Boundary status (GREY-MATTER NUCLEI — NOT the superior cerebellar
peduncle):** **Boundary case — the parabrachial area is the GREY-MATTER
NUCLEI, NOT the superior cerebellar peduncle.** The **superior cerebellar
peduncle** (the "brachium conjunctivum") is the **white-matter tract**
that carries **cerebellar efferents** from the **dentate nucleus** and
the **interposed nucleus** to the **red nucleus** and the **thalamus**.
The **parabrachial nuclei** (here) are the **grey-matter neuron clusters**
that **flank** the superior cerebellar peduncle — hence the name
"para-brachial" (alongside the brachium). They are **DIFFERENT
STRUCTURES** — the **nuclei** are grey matter; the **peduncle** is white
matter. **This distinction is the etymological origin of the name and is
a classic source of confusion** — consumers must **not** conflate the
parabrachial nuclei with the superior cerebellar peduncle. The nuclei
**flank** the peduncle; they are **not** the peduncle.
**Boundary status (NOT the locus coeruleus — that is a noradrenergic
nucleus in the tegmentum):** **Boundary case — the parabrachial area is
NOT the locus coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain — it
is in the **pontine tegmentum**, **ventromedial** to the parabrachial
area. The **parabrachial nuclei** (here) are the **visceral-sensory and
respiratory-relay** nuclei. They are **DIFFERENT STRUCTURES** — different
neurotransmitters (glutamate, CGRP, etc. vs. norepinephrine), different
functional systems (visceral/respiratory vs. noradrenergic arousal). They
are **anatomically adjacent** (both are in the dorsal pons near the
floor of the fourth ventricle) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the parabrachial area with
the locus coeruleus.
**Boundary status (NOT the pontine nuclei — those are basilar-pons
cortico-ponto-cerebellar relays):** **Boundary case — the parabrachial
area is NOT the pontine nuclei.** The **pontine nuclei**
(``.../pons/pontine_nuclei/left/`` and ``.../right/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons** — they
**receive** corticopontine fibers from the cerebral cortex and **project**
to the **contralateral cerebellar cortex** via the **middle cerebellar
peduncle**. The **parabrachial nuclei** (here) are the **dorsal
tegmental** visceral-sensory and respiratory-relay nuclei. They are
**DIFFERENT STRUCTURES** — different anatomical location (basilar pons
vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. visceral-sensory/respiratory). Consumers
must **not** conflate the parabrachial area with the pontine nuclei.
**Boundary status (NOT the superior olivary complex — that is an
auditory brainstem relay):** **Boundary case — the parabrachial area is
NOT the superior olivary complex.** The **superior olivary complex**
(``.../pons/superior_olivary_complex/left/`` and ``.../right/``) is the
**auditory brainstem relay** — it **receives** cochlear nuclei
projections and **processes interaural time and intensity differences**
for **sound localization**. The **parabrachial nuclei** (here) are the
**visceral-sensory and respiratory-relay** nuclei. They are **DIFFERENT
STRUCTURES** — different functional systems (auditory vs.
visceral/respiratory), different anatomical locations. Consumers must
**not** conflate the parabrachial area with the superior olivary
complex.
**Boundary status (NOT the paramedian pontine reticular formation — that
is the horizontal gaze center):** **Boundary case — the parabrachial area
is NOT the paramedian pontine reticular formation (PPRF).** The **PPRF**
(``.../pons/paramedian_pontine_reticular_formation/``) is the
**horizontal saccadic burst generator** — it **drives** the abducens
nucleus for **horizontal saccades**. The **parabrachial nuclei** (here)
are the **visceral-sensory and respiratory-relay** nuclei. They are
**DIFFERENT STRUCTURES** — different functional systems (horizontal gaze
vs. visceral/respiratory). Consumers must **not** conflate the
parabrachial area with the PPRF.
**Boundary status (NOT the solitary nucleus — that is the MEDULLARY
visceral-afferent hub that PROJECTS TO the parabrachial area):**
**Boundary case — the parabrachial area is NOT the solitary nucleus.**
The **solitary nucleus** (nucleus tractus solitarius,
``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``) is
the **medullary visceral-afferent hub** for **CN VII, IX, and X** —
**taste**, **visceral sensation**, **baroreception**, **respiratory
chemoreception**, and **gastrointestinal** afferents. The **solitary
nucleus** is the **upstream source** — it **projects to** the
**parabrachial area** via the **central tegmental tract**. The
**parabrachial area** (here) is the **pontine relay** that **receives**
the solitary nucleus projections and **relays** them to the **amygdala**,
**BNST**, **insula**, **hypothalamus**, and **thalamus**. They are
**DIFFERENT STRUCTURES** — the **solitary nucleus** is **medullary** and
**upstream**; the **parabrachial area** is **pontine** and
**downstream**. Consumers must **not** conflate the parabrachial area
with the solitary nucleus.
**Boundary status (NOT the Kölliker-Fuse nucleus or the pontine
respiratory group — those are STRUCTURAL GRANDCHILDREN):** **Boundary
case — the parabrachial area is NOT the Kölliker-Fuse nucleus or the
pontine respiratory group; those are STRUCTURAL GRANDCHILDREN (children
of the subparabrachial nucleus).** The **Kölliker-Fuse nucleus** and the
**pontine respiratory group** are **children** of the
**subparabrachial_nucleus**, which is itself a **child** of the
**parabrachial_area**. They are **structural grandchildren** of the
parabrachial area, not the parabrachial area itself. Consumers must
**not** conflate the parabrachial area with the Kölliker-Fuse nucleus or
the pontine respiratory group.
**Boundary status (NOT the central nucleus of the amygdala, the BNST, the
insula, the hypothalamus, or the thalamus — those are DOWNSTREAM
targets):** **Boundary case — the parabrachial area is NOT the central
nucleus of the amygdala, the BNST, the insula, the hypothalamus, or the
thalamus.** The **parabrachial area** (here) **projects to** these
structures — it is the **upstream source** of the ascending
visceral-sensory, pain, and respiratory projections. The **central
nucleus of the amygdala**, the **BNST**, the **insula**, the
**hypothalamus**, and the **VPMpc thalamus** are the **downstream
targets**. They are **DIFFERENT STRUCTURES** — the **parabrachial area**
is **pontine** and **upstream**; the **downstream targets** are
**forebrain** and **downstream**. Consumers must **not** conflate the
parabrachial area with any of its downstream targets.
**Boundary status (NOT the periaqueductal gray — that is a MIDBRAIN
target):** **Boundary case — the parabrachial area is NOT the
periaqueductal gray (PAG).** The **PAG**
(``.../midbrain/tegmentum/periaqueductal_gray/``) is the **midbrain
pain-modulation and defensive-behavior center** — it **receives** the
parabrachial area projections and **projects** to the **rostral
ventromedial medulla** and the **spinal cord** for **descending pain
modulation**. The **parabrachial area** (here) is the **pontine
visceral-sensory relay**. They are **DIFFERENT STRUCTURES** — different
brainstem levels (pons vs. midbrain), different functional roles
(ascending relay vs. descending modulation). Consumers must **not**
conflate the parabrachial area with the PAG.
**Boundary status (NOT the retrotrapezoid nucleus — that is a MEDULLARY
respiratory chemoreceptor):** **Boundary case — the parabrachial area is
NOT the retrotrapezoid nucleus (RTN).** The **RTN**
(``.../medulla_oblongata/ventral_respiratory_group/left/retrotrapezoid_nucleus/``)
is the **medullary respiratory chemoreceptor** — it **senses CO₂ / pH**
and **drives** the **ventral respiratory group** for **respiratory
chemoreception**. The **parabrachial area** (here) is the **pontine
respiratory and visceral-sensory relay** — its **subparabrachial
nucleus** contains the **pontine respiratory group** (Kölliker-Fuse
nucleus), which **regulates respiratory rhythm** (inspiratory-expiratory
phase transition). They are **DIFFERENT STRUCTURES** — different
brainstem levels (pons vs. medulla), different functional roles (pontine
respiratory rhythm vs. medullary chemoreception). Consumers must **not**
conflate the parabrachial area with the retrotrapezoid nucleus.
**Boundary status (NOT the ventral respiratory group — that is a
MEDULLARY respiratory center):** **Boundary case — the parabrachial area
is NOT the ventral respiratory group (VRG).** The **VRG**
(``.../medulla_oblongata/ventral_respiratory_group/``) is the
**medullary respiratory pattern generator** — it **contains** the
**pre-Bötzinger complex** (the **respiratory rhythm generator**), the
**nucleus ambiguus** (pharyngeal/laryngeal motor), and the
**retrotrapezoid nucleus** (chemoreception). The **parabrachial area**
(here) is the **pontine respiratory relay** — its **pontine respiratory
group** (Kölliker-Fuse nucleus) **modulates** the VRG. They are
**DIFFERENT STRUCTURES** — different brainstem levels (pons vs. medulla),
different functional roles (pontine modulation vs. medullary rhythm
generation). Consumers must **not** conflate the parabrachial area with
the VRG.
**Boundary status (NOT the dorsal respiratory group — that is a MEDULLARY
respiratory center):** **Boundary case — the parabrachial area is NOT the
dorsal respiratory group (DRG).** The **DRG**
(``.../medulla_oblongata/respiratory_center/dorsal_respiratory_group/left/``)
is the **medullary respiratory center** — it **contains** the
**inspiratory neurons** of the **solitary nucleus** and **drives** the
**phrenic nerve** for **diaphragmatic contraction**. The **parabrachial
area** (here) is the **pontine respiratory relay** — its **pontine
respiratory group** (Kölliker-Fuse nucleus) **modulates** the DRG and the
VRG for **respiratory phase switching**. They are **DIFFERENT
STRUCTURES** — different brainstem levels (pons vs. medulla), different
functional roles (pontine modulation vs. medullary inspiratory drive).
Consumers must **not** conflate the parabrachial area with the DRG.
**Boundary status (NOT the whole pons — the pons is the parent):**
**Boundary case — the parabrachial area is NOT the whole pons; the pons
is the PARENT.** The **pons** (``.../pons/``) is the **whole
metencephalic brainstem segment** — it contains the **basilar pons**, the
**pontine tegmentum**, the **pontine nuclei**, the **corticospinal /
corticobulbar tracts**, the **middle cerebellar peduncle**, the
**cranial_nerve_nuclei**, and the **parabrachial area**. The
**parabrachial area** (here) is the **dorsal tegmental visceral-sensory
and respiratory-relay nuclei only**. Consumers must **not** conflate the
parabrachial area with the **whole pons**.
**Boundary status (NOT a single functional system — MULTIPLE sub-nuclei
with DIFFERENT functions):** **Boundary case — the parabrachial area is a
HETEROGENEOUS collection of THREE sub-nuclei with DIFFERENT functions,
not a single uniform system.** The **lateral parabrachial nucleus**
subserves **visceral sensation**, **taste**, **pain**, **temperature**,
**aversion**, and **food intake**. The **medial parabrachial nucleus**
subserves **respiratory** and **autonomic** relay. The
**subparabrachial nucleus** — containing the **Kölliker-Fuse nucleus**
and the **pontine respiratory group** — subserves **respiratory rhythm**
and **autonomic regulation**. **Each sub-nucleus is functionally
distinct** — the tree wires them as **separate structural children**.
Consumers must **not** treat the parabrachial area as a single uniform
system — it is a **distributed collection** of functionally distinct
nuclei.
**Boundary status (SLEA-FREE — the parabrachial area is NOT an
extended-amygdala component):** **Boundary case — the parabrachial area
is SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus**
(the **only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired elsewhere). The
**parabrachial area** is a **pontine visceral-sensory and
respiratory-relay complex** — it is **NOT** an extended-amygdala
component, and it carries **NO SLEA warning**. **However**, the
parabrachial area **projects to** the **central nucleus of the amygdala**
and the **BNST** — these are **downstream SLEA targets**, not components
of the parabrachial area. Consumers must **not** conflate the
parabrachial area with the SLEA continuum — the parabrachial area is
**upstream** of the SLEA, not part of it.

Overview
--------
The parabrachial area is the **pontine visceral-sensory and
respiratory-relay complex** — a **heterogeneous collection** of **three
sub-nuclei** (the **lateral parabrachial nucleus**, the **medial
parabrachial nucleus**, and the **subparabrachial nucleus**) flanking the
**superior cerebellar peduncle** in the **dorsal pons**. It is the
**principal pontine relay** for **visceral sensation**, **taste**,
**pain**, **temperature**, **respiratory control**, **autonomic
regulation**, and **aversion / food intake**. It is a **single module**
at the tree level (not bilateralized) with **three structural children**
(two leaves + one sub-container).

**The parabrachial area is a CONTAINER, NOT a leaf.** Its structural
children are the **lateral parabrachial nucleus**, the **medial
parabrachial nucleus**, and the **subparabrachial nucleus** (which is
itself a sub-container with the **Kölliker-Fuse nucleus** and the
**pontine respiratory group**).

**The parabrachial area is SINGLE at the tree level, but BILATERAL in
real anatomy.** Unlike the **cranial_nerve_nuclei** module (which has
explicit ``left`` and ``right`` structural children), the
**parabrachial_area** module (here) is a **single module** that
represents the **bilateral parabrachial nuclei** (left and right flanking
the superior cerebellar peduncle). The tree does **not** split them into
left/right. Consumers must **not** assume a left/right split exists at
the tree level.

**The parabrachial area is GREY-MATTER NUCLEI, NOT the superior
cerebellar peduncle.** The **superior cerebellar peduncle** (brachium
conjunctivum) is the **white-matter tract** that the parabrachial nuclei
**flank** — hence the name "para-brachial" (alongside the brachium). They
are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**peduncle** is white matter. **This distinction is the etymological
origin of the name and is a classic source of confusion.**

**The parabrachial area is NOT the locus coeruleus.** The **locus
coeruleus** is the **noradrenergic nucleus** in the **pontine
tegmentum** — it is **anatomically adjacent** to the parabrachial area,
but it is a **different structure** (noradrenergic vs.
visceral/respiratory relay).

**The parabrachial area is HETEROGENEOUS.** The three sub-nuclei are
**functionally distinct** — **lateral** (visceral sensation, taste, pain,
temperature, aversion, food intake), **medial** (respiratory and
autonomic relay), and **subparabrachial** (respiratory rhythm, autonomic
regulation). The tree wires them as **separate structural children**.

**The parabrachial area is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**. **It
does, however, project to** the **central nucleus of the amygdala** and
the **BNST** — the **downstream SLEA targets** — making it a **key
ascending input** to the extended amygdala.

Sub-Nucleus Composition (structural children, prose)
----------------------------------------------------
The parabrachial area contains **three sub-nuclei** — documented as
**structural children** (not as leaves of the parabrachial area):

*   **Lateral parabrachial nucleus**
    (``.../parabrachial_area/lateral_parabrachial_nucleus/``) — the
    **visceral-sensory and pain relay**. It **receives** ascending
    visceral afferents from the **solitary nucleus** (taste, visceral
    sensation, baroreception, respiratory chemoreception) and ascending
    pain and temperature afferents from the **spinal cord dorsal horn**
    (lamina I, via the **spinoparabrachial tract**). It **projects to**
    the **central nucleus of the amygdala**, the **BNST**, the
    **insula**, the **hypothalamus**, the **VPMpc thalamus**, and the
    **periaqueductal gray**. It is critical for **learned taste
    aversion**, **food intake suppression**, **pain modulation**, and
    **thermal sensation**.

*   **Medial parabrachial nucleus**
    (``.../parabrachial_area/medial_parabrachial_nucleus/``) — the
    **respiratory and autonomic relay**. It **receives** respiratory
    afferents from the **solitary nucleus** and the **retrotrapezoid
    nucleus**. It **projects to** the **ventral respiratory group** (in
    the medulla) and the **Kölliker-Fuse nucleus**. It is involved in
    **respiratory rhythm** and **autonomic regulation**.

*   **Subparabrachial nucleus**
    (``.../parabrachial_area/subparabrachial_nucleus/``) — a
    **sub-container** with two structural children:
    *   **Kölliker-Fuse nucleus** — the **pontine respiratory center**
        that regulates the **inspiratory-expiratory phase transition**
        (the **Hering-Breuer reflex**, **apneustic center** function),
        **laryngeal function**, and **cardiorespiratory integration**.
    *   **Pontine respiratory group** — the **broader functional
        concept** that includes the **Kölliker-Fuse nucleus** and the
        **adjacent subparabrachial neurons** (and, classically, the
        **medial parabrachial nucleus**). It is the **pontine
        respiratory rhythm modulator** that **modulates** the
        **medullary respiratory centers** (the **dorsal respiratory
        group** and the **ventral respiratory group**).

**These sub-nuclei are structural children of the parabrachial area.**
The parabrachial area's **structural children** are the **lateral
parabrachial nucleus**, the **medial parabrachial nucleus**, and the
**subparabrachial nucleus**; the **subparabrachial nucleus** is a
**sub-container** with the **Kölliker-Fuse nucleus** and the **pontine
respiratory group** as its children. Consumers resolving sub-nucleus
detail go **through** the lateral, medial, or subparabrachial nucleus.

The Parabrachial Area / Superior Cerebellar Peduncle Boundary
-------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **etymological
origin of the name**:

*   **Parabrachial area** (this module) — the **grey-matter neuron
    clusters** flanking the superior cerebellar peduncle.

*   **Superior cerebellar peduncle** (brachium conjunctivum) — the
    **white-matter tract** that carries cerebellar efferents from the
    dentate and interposed nuclei to the red nucleus and the thalamus.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**peduncle** is white matter. The nuclei **flank** the peduncle; they are
**not** the peduncle. **This distinction is the etymological origin of
the name "parabrachial"** ("para-" = alongside, "brachium" = the
superior cerebellar peduncle) — and it is a **classic source of
confusion**. Consumers must **not** conflate the parabrachial area with
the superior cerebellar peduncle.

The Parabrachial Area / Locus Coeruleus Boundary
------------------------------------------------
This is the **anatomically adjacent** boundary — **visceral/respiratory
relay vs. noradrenergic nucleus**:

*   **Parabrachial area** (this module) — the **visceral-sensory,
    respiratory, and autonomic relay**.

*   **Locus coeruleus**
    (``.../pons/tegmentum/locus_coeruleus/``) — the **noradrenergic
    nucleus** — the **principal source of norepinephrine** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, CGRP, etc. vs. norepinephrine), different functional systems
(visceral/respiratory vs. noradrenergic arousal). They are **anatomically
adjacent** (both are in the dorsal pons near the floor of the fourth
ventricle) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the parabrachial area with the locus
coeruleus.

The Parabrachial Area / Pontine Nuclei Boundary
-----------------------------------------------
This is the **basilar-pons vs. dorsal-tegmentum** boundary:

*   **Parabrachial area** (this module) — the **dorsal tegmental**
    visceral-sensory and respiratory-relay nuclei.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/left/`` and
    ``.../right/``) — the **cortico-ponto-cerebellar relay** in the
    **basilar pons**.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. visceral/respiratory). Consumers must
**not** conflate the parabrachial area with the pontine nuclei.

The Parabrachial Area / Superior Olivary Complex Boundary
--------------------------------------------------------
This is the **auditory-relay** boundary:

*   **Parabrachial area** (this module) — the **visceral-sensory and
    respiratory-relay** nuclei.

*   **Superior olivary complex**
    (``.../pons/superior_olivary_complex/left/`` and ``.../right/``) —
    the **auditory brainstem relay** for **sound localization**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory vs. visceral/respiratory), different anatomical locations.
Consumers must **not** conflate the parabrachial area with the superior
olivary complex.

The Parabrachial Area / Paramedian Pontine Reticular Formation Boundary
----------------------------------------------------------------------
This is the **horizontal-gaze** boundary:

*   **Parabrachial area** (this module) — the **visceral-sensory and
    respiratory-relay** nuclei.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/paramedian_pontine_reticular_formation/``) — the
    **horizontal saccadic burst generator**.

**They are DIFFERENT STRUCTURES** — different functional systems
(horizontal gaze vs. visceral/respiratory). Consumers must **not**
conflate the parabrachial area with the PPRF.

The Parabrachial Area / Solitary Nucleus Boundary
-------------------------------------------------
This is the **upstream source vs. pontine relay** boundary:

*   **Parabrachial area** (this module) — the **pontine visceral-sensory
    and respiratory-relay** nuclei.

*   **Solitary nucleus** (nucleus tractus solitarius,
    ``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``)
    — the **medullary visceral-afferent hub** for **CN VII, IX, and X**.

**The solitary nucleus is the upstream source** — it **projects to** the
parabrachial area via the **central tegmental tract**. The **parabrachial
area** (here) is the **pontine relay** that **receives** the solitary
nucleus projections and **relays** them to the forebrain. They are
**DIFFERENT STRUCTURES** — the **solitary nucleus** is **medullary** and
**upstream**; the **parabrachial area** is **pontine** and **downstream**.
Consumers must **not** conflate the parabrachial area with the solitary
nucleus.

The Parabrachial Area / Kölliker-Fuse Nucleus and Pontine Respiratory Group Boundary
-----------------------------------------------------------------------------------
This is the **container vs. structural grandchild** boundary:

*   **Parabrachial area** (this module) — the **container** with three
    structural children.

*   **Kölliker-Fuse nucleus** and **pontine respiratory group** — the
    **structural grandchildren** (children of the
    ``subparabrachial_nucleus``, which is itself a child of the
    parabrachial area).

**They are DIFFERENT STRUCTURES** — the **Kölliker-Fuse nucleus** and the
**pontine respiratory group** are **structural grandchildren** of the
parabrachial area, not the parabrachial area itself. Consumers must **not**
conflate the parabrachial area with the Kölliker-Fuse nucleus or the
pontine respiratory group.

The Parabrachial Area / Central Nucleus of the Amygdala, BNST, Insula, Hypothalamus, and Thalamus Boundary
---------------------------------------------------------------------------------------------------------
This is the **upstream relay vs. downstream targets** boundary:

*   **Parabrachial area** (this module) — the **pontine visceral-sensory
    and respiratory-relay** nuclei — **upstream**.

*   **Central nucleus of the amygdala**, **BNST**, **insula**,
    **hypothalamus**, and **VPMpc thalamus** — the **forebrain downstream
    targets** — **downstream**.

**They are DIFFERENT STRUCTURES** — the **parabrachial area** is
**pontine** and **upstream**; the **downstream targets** are **forebrain**
and **downstream**. The parabrachial area **projects to** these structures
— it is the **upstream source** of the ascending visceral-sensory, pain,
and respiratory projections. Consumers must **not** conflate the
parabrachial area with any of its downstream targets.

The Parabrachial Area / Periaqueductal Gray Boundary
----------------------------------------------------
This is the **ascending relay vs. descending modulation** boundary:

*   **Parabrachial area** (this module) — the **pontine visceral-sensory
    and respiratory-relay** nuclei — **upstream**.

*   **Periaqueductal gray (PAG)**
    (``.../midbrain/tegmentum/periaqueductal_gray/``) — the **midbrain
    pain-modulation and defensive-behavior center** — **downstream**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
midbrain), different functional roles (ascending relay vs. descending
modulation). The parabrachial area **projects to** the PAG. Consumers
must **not** conflate the parabrachial area with the PAG.

The Parabrachial Area / Retrotrapezoid Nucleus, Ventral Respiratory Group, and Dorsal Respiratory Group Boundary
--------------------------------------------------------------------------------------------------------------
This is the **pontine vs. medullary respiratory center** boundary:

*   **Parabrachial area** (this module) — the **pontine respiratory
    relay** — its **subparabrachial nucleus** contains the **pontine
    respiratory group** (Kölliker-Fuse nucleus) that **modulates** the
    medullary respiratory centers.

*   **Retrotrapezoid nucleus**, **ventral respiratory group (VRG)**, and
    **dorsal respiratory group (DRG)** — the **medullary respiratory
    centers**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (pontine modulation vs. medullary
rhythm generation and chemoreception). The parabrachial area's **pontine
respiratory group** **modulates** the medullary respiratory centers.
Consumers must **not** conflate the parabrachial area with the medullary
respiratory centers.

The Parabrachial Area / Pons Boundary
-------------------------------------
This is the **container vs. parent** boundary:

*   **Parabrachial area** (this module) — the **dorsal tegmental
    visceral-sensory and respiratory-relay** nuclei only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine tegmentum**,
    the **pontine nuclei**, the **corticospinal / corticobulbar
    tracts**, the **middle cerebellar peduncle**, the **cranial-nerve
    nuclei**, and the **parabrachial area**.

**The parabrachial area is a child of the pons.** Consumers must **not**
conflate the parabrachial area with the **whole pons**.

The Parabrachial Area / SLEA Boundary
-------------------------------------
This is the **SLEA** boundary — **NOT an SLEA component, but UPSTREAM of
the SLEA**:

*   **Parabrachial area** (this module) — **SLEA-FREE**. It is **not** an
    extended-amygdala component, and it carries **no SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The parabrachial area is NOT part of the SLEA continuum.** It is a
**pontine visceral-sensory and respiratory-relay complex**, and it carries
**no SLEA warning**. **However**, the parabrachial area **projects to**
the **central nucleus of the amygdala** and the **BNST** — these are
**downstream SLEA targets**, not components of the parabrachial area.
Consumers must **not** conflate the parabrachial area with the SLEA
continuum — the parabrachial area is **upstream** of the SLEA, not part
of it.

Function in the Human Brain
---------------------------
The parabrachial area's functions are **the pontine relay for visceral
sensation, taste, pain, temperature, respiratory control, autonomic
regulation, and aversion / food intake** — **NOT a single unified
function**:

*   **Visceral Sensory Relay (Lateral Parabrachial Nucleus):** The
    **lateral parabrachial nucleus** receives ascending visceral
    afferents from the **solitary nucleus** (taste, visceral sensation,
    baroreception, respiratory chemoreception) and **projects** to the
    **central nucleus of the amygdala**, the **BNST**, the **insula**,
    the **hypothalamus**, and the **VPMpc thalamus**. It is the
    **principal pontine relay** for **visceral sensation** and **taste**.

*   **Pain and Temperature Relay (Lateral Parabrachial Nucleus):** The
    **lateral parabrachial nucleus** receives ascending pain and
    temperature afferents from the **spinal cord dorsal horn** (lamina
    I, via the **spinoparabrachial tract**) and **projects** to the
    **central nucleus of the amygdala** (for **emotional** and
    **autonomic** aspects of pain), the **hypothalamus**, and the
    **periaqueductal gray** (for **descending pain modulation**). It is
    the **principal pontine relay** for **pain** and **temperature**
    sensation.

*   **Aversion and Food Intake (Lateral Parabrachial Nucleus):** The
    **lateral parabrachial nucleus** is critical for **learned taste
    aversion** (the association between a novel taste and visceral
    illness) and **food intake suppression** — the **CGRP-expressing
    neurons** in the lateral parabrachial nucleus **project to** the
    **central nucleus of the amygdala** and **mediate** the
    **suppression of feeding** in response to **visceral malaise**.

*   **Respiratory Relay (Medial Parabrachial Nucleus):** The **medial
    parabrachial nucleus** receives respiratory afferents from the
    **solitary nucleus** and the **retrotrapezoid nucleus** and
    **projects** to the **ventral respiratory group** and the
    **Kölliker-Fuse nucleus**. It is involved in **respiratory rhythm**
    and **autonomic regulation**.

*   **Pontine Respiratory Rhythm Modulation (Subparabrachial Nucleus,
    Kölliker-Fuse Nucleus, Pontine Respiratory Group):** The
    **Kölliker-Fuse nucleus** and the **pontine respiratory group** are
    the **pontine respiratory centers** that **modulate** the
    **medullary respiratory centers** (DRG and VRG). They regulate the
    **inspiratory-expiratory phase transition** (the **Hering-Breuer
    reflex**, **apneustic center** function), **laryngeal function**,
    and **cardiorespiratory integration**.

*   **Autonomic Regulation (All Sub-Nuclei):** The parabrachial area
    **participates** in **autonomic regulation** — it **receives**
    ascending autonomic afferents from the solitary nucleus and
    **projects** to the **hypothalamus** and the **brainstem autonomic
    centers** for **cardiovascular**, **respiratory**, and
    **gastrointestinal** regulation.

*   **NOT a neural processor in the classical sense.** The parabrachial
    area is a **relay complex** — it **receives** ascending visceral,
    pain, and respiratory afferents and **projects** them to the
    forebrain (visceral sensation, taste, pain, aversion) and to the
    medullary respiratory centers (respiratory rhythm). The **processing**
    of these signals happens in the **solitary nucleus** (visceral
    afferent integration), the **parabrachial area** (pontine relay), and
    the **forebrain targets** (conscious perception, emotional
    responses, autonomic regulation).

**The unifying theme:** the parabrachial area is the **pontine
visceral-sensory and respiratory-relay complex** — the **principal
pontine relay** for **visceral sensation**, **taste**, **pain**,
**temperature**, **respiratory control**, **autonomic regulation**, and
**aversion / food intake**. It is **heterogeneous** (three functionally
distinct sub-nuclei), **SLEA-free** (but **upstream** of the SLEA — it
**projects to** the central nucleus and BNST), and **NOT the superior
cerebellar peduncle** — the **peduncle** is the white-matter tract that
the nuclei **flank**.

Associated Disorders
--------------------
The parabrachial area has **no single named "parabrachial area syndrome"
as a collection** — its clinical associations are **sub-nucleus-specific**:

*   **Lateral Parabrachial Nucleus Lesion — Impaired Visceral Sensation,
    Taste, Pain, and Temperature; Impaired Food Intake Regulation:**
    A lesion of the **lateral parabrachial nucleus** causes **impaired
    visceral sensation** (blunted visceral pain, impaired
    baroreception), **impaired taste** (blunted taste perception),
    **impaired pain and temperature sensation** on the **contralateral
    body** (because the spinoparabrachial tract crosses), and **impaired
    food intake regulation** (loss of **learned taste aversion** and
    **food intake suppression** in response to visceral malaise).

*   **Medial Parabrachial Nucleus Lesion — Respiratory and Autonomic
    Dysregulation:** A lesion of the **medial parabrachial nucleus**
    causes **respiratory dysregulation** (impaired respiratory rhythm)
    and **autonomic dysregulation** (impaired cardiovascular and
    gastrointestinal regulation).

*   **Subparabrachial Nucleus / Kölliker-Fuse Nucleus Lesion —
    Respiratory Rhythm Dysregulation:** A lesion of the **Kölliker-Fuse
    nucleus** or the **pontine respiratory group** causes **respiratory
    rhythm dysregulation** — **impaired inspiratory-expiratory phase
    transition** (the **apneustic center** function is lost),
    **impaired Hering-Breuer reflex**, and **impaired laryngeal
    function**. In experimental animals, **Kölliker-Fuse lesions** cause
    **apneustic breathing** (prolonged inspiratory pauses).

*   **Parabrachial Area Lesion in Humans — Central Respiratory
    Dysregulation:** A lesion of the **parabrachial area** in humans
    (e.g. **pontine stroke**, **tumor**, **demyelination**) can cause
    **central respiratory dysregulation** (impaired respiratory rhythm,
    **Ondine's curse** — central hypoventilation), **impaired visceral
    sensation**, and **impaired taste**.

*   **Pontine Stroke — Parabrachial Area Involvement:** A **pontine
    stroke** (e.g. **basilar artery** territory) can involve the
    **parabrachial area** — causing **respiratory dysregulation**
    (central hypoventilation, apneustic breathing), **impaired visceral
    sensation**, **impaired taste**, and **impaired pain and temperature
    sensation**. The **parabrachial area** is the **substrate** of the
    **respiratory and visceral-sensory** components of **pontine
    stroke**.

*   **Wernicke's Encephalopathy — Parabrachial Area Involvement:**
    **Wernicke's encephalopathy** (thiamine deficiency) can affect the
    **parabrachial area** (among other brainstem and diencephalic
    structures), contributing to **autonomic dysregulation** and
    **respiratory abnormalities**.

*   **No Named "Parabrachial Area Syndrome":** The parabrachial area is
    a **heterogeneous collection** of three sub-nuclei — it has **no
    named clinical syndrome as a collection**. Its clinical relevance is
    **sub-nucleus-specific** — **lateral parabrachial nucleus** →
    **visceral sensation, taste, pain, temperature, aversion, food
    intake**; **medial parabrachial nucleus** → **respiratory and
    autonomic relay**; **subparabrachial nucleus** (Kölliker-Fuse) →
    **respiratory rhythm**.

**What is NOT here:** The parabrachial area is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), or **trigeminal neuralgia** (trigeminal nerve root). Its
clinical relevance is **visceral-sensory-respiratory-specific**, via the
**lateral, medial, and subparabrachial nuclei** it subserves. **No named
parabrachial area syndrome exists as a collection.**

Lateralization Notes
--------------------
This is the **single** parabrachial area module. The parabrachial nuclei
are **bilateral in real anatomy** (left and right flanking the superior
cerebellar peduncle), but the tree wires them as a **single module** —
and the module carries **NO warning at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **parabrachial_area** module (here) is a **single module** that
    represents the **bilateral parabrachial nuclei** (left and right
    flanking the superior cerebellar peduncle). The tree does **not**
    split them into left/right. Consumers must **not** assume a
    left/right split exists at the tree level — the module is a
    **single, bilateral-container representation**.

*   **Bilateral Anatomy — Contested Lateralization (Documented in the
    Literature, Not Wired):** The **parabrachial nuclei** are
    **bilateral in real anatomy** — there are **left and right**
    parabrachial nuclei flanking the **left and right** superior
    cerebellar peduncles. Some studies suggest **left/right
    lateralization** in **taste** and **visceral** processing (e.g. the
    **left parabrachial nucleus** may be more involved in **taste** and
    **visceral** processing in some species). This lateralization is
    **contested** and is **documented in the literature** — it is **not
    wired** as structural children. Consumers must **not** import a
    lateralization warning into the parabrachial area — there is **none
    at the module level**.

*   **NO Extended-Amygdala Warning (SLEA-free module):** The parabrachial
    area is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the parabrachial area.
    **However**, the parabrachial area **projects to** the **central
    nucleus of the amygdala** and the **BNST** — these are **downstream
    SLEA targets**, not components of the parabrachial area. The
    **parabrachial area** is **upstream** of the SLEA, not part of it.

*   **NO Amygdala-Lateralization Warning of their own (the parabrachial
    area is VISCERAL/RESPIRATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The parabrachial area is a
    **pontine visceral-sensory and respiratory-relay complex** —
    consumers must **not** conflate it with the **amygdala** or with the
    **fear circuit**. **Note**: the parabrachial area **projects to**
    the central nucleus (a fear-output structure), but the parabrachial
    area itself is **not** part of the fear circuit — it is an
    **upstream visceral/pain relay**.

**A consumer that sees "parabrachial_area" must understand that the
module is a SINGLE, BILATERAL-CONTAINER representation** — it is **not**
a left/right split at the tree level. Any lateralization is **contested**
and documented in the literature. The parabrachial area is a
**strict-single module with NO warning at the module level** — **no SLEA
warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** parabrachial nuclei as a **single module** — it does
    **not** import left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../pons/tegmentum/``, ``.../medulla_oblongata/``,
    ``.../midbrain/``, ``.../diencephalon/``, ``.../cortex/``, or any
    other container. The parabrachial area's relationships to the
    **superior cerebellar peduncle**, the **locus coeruleus**, the
    **pontine nuclei**, the **superior olivary complex**, the **PPRF**,
    the **solitary nucleus**, the **Kölliker-Fuse nucleus**, the
    **pontine respiratory group**, the **central nucleus of the
    amygdala**, the **BNST**, the **insula**, the **hypothalamus**, the
    **VPMpc thalamus**, the **periaqueductal gray**, the
    **retrotrapezoid nucleus**, the **ventral respiratory group**, the
    **dorsal respiratory group**, and the **pons** are documented as
    **prose and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children are the THREE sub-nuclei.**
    The **subparabrachial nucleus** is itself a **sub-container** with
    the **Kölliker-Fuse nucleus** and the **pontine respiratory group**
    as its children.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **parabrachial area** is a **single module** that represents the
    **bilateral parabrachial nuclei** — the tree does **not** split them
    into left/right. Consumers must **not** assume a left/right split
    exists at the tree level. Any lateralization is **contested** and
    documented in the literature, not wired.
*   **GREY-MATTER NUCLEI — NOT the superior cerebellar peduncle.** The
    **parabrachial area** is the **grey-matter neuron clusters**; the
    **superior cerebellar peduncle** (brachium conjunctivum) is the
    **white-matter tract** that the nuclei **flank**. **This distinction
    is the etymological origin of the name** ("para-brachial" =
    "alongside the brachium") and is a **classic source of confusion**.
    Consumers must **not** conflate the two.
*   **NOT the locus coeruleus — that is a noradrenergic nucleus.** The
    **locus coeruleus** is **anatomically adjacent** to the parabrachial
    area, but it is a **different structure**. Consumers must **not**
    conflate the two.
*   **NOT the pontine nuclei — those are basilar-pons
    cortico-ponto-cerebellar relays.** The **pontine nuclei** are in
    the **basilar pons**; the **parabrachial area** is in the **dorsal
    tegmentum**. Consumers must **not** conflate the two.
*   **NOT the superior olivary complex — that is an auditory brainstem
    relay.** Consumers must **not** conflate the two.
*   **NOT the paramedian pontine reticular formation — that is the
    horizontal gaze center.** Consumers must **not** conflate the two.
*   **NOT the solitary nucleus — that is the MEDULLARY
    visceral-afferent hub that PROJECTS TO the parabrachial area.** The
    **solitary nucleus** is **upstream**; the **parabrachial area** is
    **downstream**. Consumers must **not** conflate the two.
*   **NOT the Kölliker-Fuse nucleus or the pontine respiratory group —
    those are STRUCTURAL GRANDCHILDREN.** The **Kölliker-Fuse nucleus**
    and the **pontine respiratory group** are children of the
    **subparabrachial nucleus**, which is itself a child of the
    **parabrachial area**. They are **not** the parabrachial area
    itself. Consumers must **not** conflate the two.
*   **NOT the central nucleus of the amygdala, the BNST, the insula, the
    hypothalamus, or the thalamus — those are DOWNSTREAM targets.** The
    parabrachial area **projects to** these structures. They are **not**
    the parabrachial area itself. Consumers must **not** conflate the
    two.
*   **NOT the periaqueductal gray — that is a MIDBRAIN target.** The
    parabrachial area **projects to** the PAG. They are **different
    structures**. Consumers must **not** conflate the two.
*   **NOT the retrotrapezoid nucleus, the ventral respiratory group, or
    the dorsal respiratory group — those are MEDULLARY respiratory
    centers.** The parabrachial area's **pontine respiratory group**
    **modulates** the medullary respiratory centers. They are
    **different structures**. Consumers must **not** conflate the two.
*   **NOT a single functional system — MULTIPLE sub-nuclei.** The
    **lateral parabrachial nucleus** (visceral sensation, taste, pain,
    temperature, aversion, food intake), the **medial parabrachial
    nucleus** (respiratory and autonomic relay), and the
    **subparabrachial nucleus** (respiratory rhythm) are **functionally
    distinct**. Consumers must **not** treat the parabrachial area as a
    single uniform system.
*   **SLEA-FREE — no extended-amygdala relationship.** The parabrachial
    area is **not** an extended-amygdala component, and it carries **no
    SLEA warning**. **However**, the parabrachial area **projects to**
    the **central nucleus of the amygdala** and the **BNST** — these are
    **downstream SLEA targets**, not components of the parabrachial
    area. The **parabrachial area** is **upstream** of the SLEA, not
    part of it.
*   **NOT the fear-output — the parabrachial area is VISCERAL/RESPIRATORY
    RELAY.** The **fear-output** structure is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **parabrachial area** is a **pontine visceral-sensory
    and respiratory-relay complex** — it is **not** part of the fear
    circuit. **It projects to** the central nucleus (a fear-output
    structure), but the parabrachial area itself is **not** a fear
    structure.
*   **No ``AREA_PATHS`` hop.** The parabrachial area is a local container
    under the pons, not a cross-listed container.
*   **No nested cross-listing.** The parabrachial area has no nested
    dual-framing module. It is a single container with three structural
    children.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import parabrachial_area

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.parabrachial_area"
    )

**Do not** assume the parabrachial area is a **leaf**. It is a
**container** — its structural children are the **lateral parabrachial
nucleus**, the **medial parabrachial nucleus**, and the
**subparabrachial nucleus** (which is itself a sub-container with the
**Kölliker-Fuse nucleus** and the **pontine respiratory group**).

**Do not** assume the parabrachial area is **bilateralized at the tree
level**. The parabrachial nuclei are **bilateral in real anatomy**, but
the tree wires them as a **single module** — there is **no left/right
split**. Any lateralization is **contested** and documented in the
literature, not wired.

**Do not** assume the parabrachial area is the **superior cerebellar
peduncle**. The **superior cerebellar peduncle** is the **white-matter
tract** that the parabrachial nuclei **flank** — the "para-brachial" name
reflects this **flanking relationship**, not identity. They are
**different structures**.

**Do not** assume the parabrachial area is the **locus coeruleus**. The
**locus coeruleus** is the **noradrenergic nucleus** in the **pontine
tegmentum** — it is **anatomically adjacent** to the parabrachial area,
but it is a **different structure**.

**Do not** assume the parabrachial area is the **pontine nuclei**, the
**superior olivary complex**, or the **paramedian pontine reticular
formation**. Those are **different structures** — different functional
systems (cortico-ponto-cerebellar, auditory, horizontal gaze) in
different anatomical locations.

**Do not** assume the parabrachial area is the **solitary nucleus**. The
**solitary nucleus** is the **medullary visceral-afferent hub** that
**projects to** the parabrachial area. The parabrachial area is the
**pontine downstream relay**.

**Do not** assume the parabrachial area is the **Kölliker-Fuse nucleus**
or the **pontine respiratory group**. Those are **structural
grandchildren** (children of the subparabrachial nucleus).

**Do not** assume the parabrachial area is the **central nucleus of the
amygdala**, the **BNST**, the **insula**, the **hypothalamus**, the
**VPMpc thalamus**, or the **periaqueductal gray**. Those are
**downstream targets** of the parabrachial area.

**Do not** assume the parabrachial area is the **retrotrapezoid
nucleus**, the **ventral respiratory group**, or the **dorsal
respiratory group**. Those are **medullary respiratory centers** that
the parabrachial area's **pontine respiratory group** **modulates**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the parabrachial area. **The parabrachial area is
SLEA-FREE** — it is **not** an extended-amygdala component, and it is
**NOT part of the fear circuit**. **Note**: the parabrachial area
**projects to** the central nucleus (a fear-output structure), but the
parabrachial area itself is **not** a fear structure.

Iterating the parabrachial area's structural children (recommended
consumer pattern)::

    PARABRACHIAL_AREA_CHILDREN = (
        "lateral_parabrachial_nucleus",
        "medial_parabrachial_nucleus",
        "subparabrachial_nucleus",
    )
    # The parabrachial area is a container. The subparabrachial nucleus
    # is itself a sub-container with the Kölliker-Fuse nucleus and the
    # pontine respiratory group as its children.

Iterating the parabrachial area's sub-nuclei (recommended consumer
pattern)::

    for sub in PARABRACHIAL_AREA_CHILDREN:
        sub_path = (
            f"hindbrain.metencephalon.pons.parabrachial_area.{sub}"
        )
        # resolve sub_path through the memory/recall layer

Reaching the subparabrachial nucleus's sub-children (recommended consumer
pattern — the sub-container)::

    for sub in ("kolliker_fuse_nucleus", "pontine_respiratory_group"):
        sub_path = (
            f"hindbrain.metencephalon.pons.parabrachial_area."
            f"subparabrachial_nucleus.{sub}"
        )
        # resolve sub_path through the memory/recall layer

Reaching the superior cerebellar peduncle (recommended consumer pattern —
the white-matter tract the nuclei FLANK)::

    # The superior cerebellar peduncle (brachium conjunctivum) is the
    # WHITE-MATTER tract that the parabrachial nuclei FLANK:
    #
    #   .../white_matter/.../superior_cerebellar_peduncle/  (or equivalent path)
    #
    # The parabrachial nuclei are GREY MATTER that flank the peduncle;
    # the peduncle is WHITE MATTER that connects the cerebellum to the
    # midbrain and thalamus. They are DIFFERENT STRUCTURES — the
    # anatomical juxtaposition is the etymological origin of the name
    # "para-brachial" and is a classic source of confusion.

Reaching the locus coeruleus (recommended consumer pattern — the
adjacent noradrenergic nucleus)::

    # The locus coeruleus is the NORADRENERGIC nucleus in the pontine
    # tegmentum — it is ANATOMICALLY ADJACENT to the parabrachial area,
    # but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic (source of norepinephrine);
    # the parabrachial area is glutamatergic/CGRP-ergic (visceral/pain
    # relay). They are ANATOMICALLY ADJACENT but FUNCTIONALLY DISTINCT.

Reaching the solitary nucleus (recommended consumer pattern — the
UPSTREAM source)::

    # The solitary nucleus (nucleus tractus solitarius) is the MEDULLARY
    # visceral-afferent hub that PROJECTS TO the parabrachial area:
    #
    #   .../medulla_oblongata/solitary_nucleus/left/  (and right/)
    #
    # The solitary nucleus is UPSTREAM; the parabrachial area is
    # DOWNSTREAM. They are DIFFERENT STRUCTURES.

Reaching the central nucleus of the amygdala (recommended consumer
pattern — the DOWNSTREAM target)::

    # The central nucleus of the amygdala is a DOWNSTREAM target of the
    # lateral parabrachial nucleus:
    #
    #   .../cerebral_hemispheres/left/subcortical/medial_temporal_lobe/amygdala/central_nucleus/
    #
    # The parabrachial area PROJECTS TO the central nucleus; the central
    # nucleus is a DOWNSTREAM target — it is ALSO an SLEA component.
    # The parabrachial area itself is NOT an SLEA component.

Reaching the BNST (recommended consumer pattern — the DOWNSTREAM
target)::

    # The bed nucleus of the stria terminalis (BNST) is a DOWNSTREAM
    # target of the lateral parabrachial nucleus:
    #
    #   .../subcortical/extended_amygdala/stria_terminalis/bed_nucleus_of_stria_terminalis/
    #
    # The parabrachial area PROJECTS TO the BNST; the BNST is a
    # DOWNSTREAM target — it is ALSO an SLEA component. The parabrachial
    # area itself is NOT an SLEA component.

Reaching the insula, hypothalamus, and VPMpc thalamus (recommended
consumer pattern — DOWNSTREAM targets)::

    # The insula, hypothalamus, and VPMpc thalamus are DOWNSTREAM targets
    # of the lateral parabrachial nucleus:
    #
    #   .../cerebral_hemispheres/left/cortex/insular/
    #   .../diencephalon/hypothalamus/
    #   .../diencephalon/thalamus/left/ventral_nuclear_group/ventral_posterior_nucleus/ventral_posterior_medial_nucleus/
    #
    # The parabrachial area PROJECTS TO these structures; they are
    # DOWNSTREAM targets.

Reaching the periaqueductal gray (recommended consumer pattern — the
DOWNSTREAM target)::

    # The periaqueductal gray (PAG) is a DOWNSTREAM target of the lateral
    # parabrachial nucleus:
    #
    #   .../midbrain/tegmentum/periaqueductal_gray/
    #
    # The parabrachial area PROJECTS TO the PAG; the PAG is a DOWNSTREAM
    # target (midbrain pain-modulation and defensive-behavior center).

Reaching the retrotrapezoid nucleus, ventral respiratory group, and
dorsal respiratory group (recommended consumer pattern — the MEDULLARY
respiratory centers)::

    # The retrotrapezoid nucleus, ventral respiratory group, and dorsal
    # respiratory group are the MEDULLARY respiratory centers that the
    # parabrachial area's pontine respiratory group MODULATES:
    #
    #   .../medulla_oblongata/ventral_respiratory_group/...
    #   .../medulla_oblongata/respiratory_center/dorsal_respiratory_group/...
    #
    # The parabrachial area's pontine respiratory group MODULATES the
    # medullary respiratory centers. They are DIFFERENT STRUCTURES.

Bilateral iteration (recommended consumer pattern)::

    # The parabrachial area is a SINGLE module (not bilateralized at the
    # tree level). The module represents the BILATERAL parabrachial
    # nuclei. Any lateralization is contested and documented in the
    # literature, not wired.
    parabrachial_path = (
        "hindbrain.metencephalon.pons.parabrachial_area"
    )
    # resolve parabrachial_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The parabrachial area's sub-nuclei are structural children (not
    # prose subdivisions):
    #   lateral_parabrachial_nucleus -> visceral sensation, taste, pain,
    #                                    temperature, aversion, food intake
    #                                    (projects to central nucleus of
    #                                    the amygdala, BNST, insula,
    #                                    hypothalamus, VPMpc thalamus, PAG)
    #   medial_parabrachial_nucleus  -> respiratory and autonomic relay
    #                                    (projects to VRG and Kölliker-Fuse)
    #   subparabrachial_nucleus      -> pontine respiratory center
    #                                    (contains Kölliker-Fuse nucleus
    #                                    and pontine respiratory group)
    #
    # Resolve sub-nucleus detail through the lateral_parabrachial_nucleus,
    # medial_parabrachial_nucleus, or subparabrachial_nucleus modules —
    # not through prose subdivisions of the parabrachial area.

References
----------
*   **Canonical parabrachial anatomy:** Saper, C.B., Loewy, A.D. (1980).
    "Efferent connections of the parabrachial nucleus in the rat."
    *Brain Research* 197:291–317. (Parabrachial area efferents — the
    definitive early mapping.)
*   **Parabrachial area — review:** Saper, C.B. (2002). "The central
    autonomic nervous system: conscious visceral perception and autonomic
    function." *Annual Review of Neuroscience* 25:433–469. (Parabrachial
    area as the pontine visceral relay.)
*   **Visceral sensory relay:** Herbert, H., Moga, M.M., Saper, C.B.
    (1990). "Connections of the parabrachial nucleus with the nucleus of
    the solitary tract and the medullary reticular formation in the rat."
    *Journal of Comparative Neurology* 293:540–580. (Parabrachial area
    visceral afferents from the solitary nucleus.)
*   **Pain and temperature relay:** Craig, A.D. (2002). "How do you
    feel? Interoception: the sense of the physiological condition of the
    body." *Nature Reviews Neuroscience* 3:655–666. (Spinoparabrachial
    tract — lamina I pain and temperature afferents to the lateral
    parabrachial nucleus.)
*   **Aversion and food intake:** Carter, M.E., Soden, M.E., Zweifel,
    L.S., Palmiter, R.D. (2013). "Genetic identification of a neural
    circuit that suppresses appetite." *Nature* 503:111–114.
    (CGRP-expressing lateral parabrachial neurons — learned taste
    aversion and food intake suppression.)
*   **Pontine respiratory group:** Alheid, G.F., McCrimmon, D.R. (2008).
    "The chemical neuroanatomy of breathing." *Respiratory Physiology &
    Neurobiology* 164:3–11. (Kölliker-Fuse nucleus and the pontine
    respiratory group.)
*   **Kölliker-Fuse nucleus:** Dutschmann, M., Herbert, H. (2006). "The
    Kölliker-Fuse nucleus gates the postinspiratory phase of the
    respiratory cycle to control inspiratory off-switch and upper airway
    resistance in rat." *European Journal of Neuroscience* 24:1071–1084.
    (Kölliker-Fuse nucleus — respiratory phase switching.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the
    parabrachial area but functionally distinct.)
*   **Superior cerebellar peduncle (contrast — the white-matter tract the
    nuclei FLANK):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Superior cerebellar peduncle —
    brachium conjunctivum; the white-matter tract that the parabrachial
    nuclei flank.)
*   **Solitary nucleus (contrast — the MEDULLARY upstream source):**
    Saper, C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Solitary nucleus — the medullary
    visceral-afferent hub that projects to the parabrachial area.)
*   **Central nucleus of the amygdala (contrast — the DOWNSTREAM SLEA
    target):** LeDoux, J.E. (2007). "The amygdala." *Current Biology*
    17:R868–R874. (Central nucleus of the amygdala — fear-output
    structure; downstream target of the lateral parabrachial nucleus.)
*   **BNST (contrast — the DOWNSTREAM SLEA target):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (BNST — SLEA component; downstream target of
    the lateral parabrachial nucleus.)
*   **Periaqueductal gray (contrast — the MIDBRAIN downstream target):**
    Behbehani, M.M. (1995). "Functional characteristics of the midbrain
    periaqueductal gray." *Progress in Neurobiology* 46:575–605.
    (Periaqueductal gray — midbrain pain-modulation center; downstream
    target of the lateral parabrachial nucleus.)
*   **Retrotrapezoid nucleus (contrast — the MEDULLARY chemoreceptor):**
    Guyenet, P.G., Stornetta, R.L., Bayliss, D.A. (2008). "Central
    respiratory chemoreception." *Journal of Comparative Neurology*
    506:788–798. (Retrotrapezoid nucleus — medullary respiratory
    chemoreceptor; distinct from the parabrachial area.)
*   **Ventral respiratory group (contrast — the MEDULLARY respiratory
    pattern generator):** Feldman, J.L., Del Negro, C.A. (2006).
    "Looking for inspiration: new perspectives on respiratory rhythm."
    *Nature Reviews Neuroscience* 7:232–242. (Ventral respiratory group —
    medullary respiratory pattern generator; distinct from the
    parabrachial area.)
*   **Dorsal respiratory group (contrast — the MEDULLARY inspiratory
    center):** Bianchi, A.L., Denavit-Saubié, M., Champagnat, J. (1995).
    "Central control of breathing in mammals: neuronal circuitry,
    membrane properties, and neurotransmitters." *Physiological Reviews*
    75:1–45. (Dorsal respiratory group — medullary inspiratory center;
    distinct from the parabrachial area.)
*   **SLEA (contrast — the parabrachial area is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the parabrachial area. The
    parabrachial area PROJECTS TO the SLEA components, but is not part
    of the continuum.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the parabrachial area. **Note**: the parabrachial area
    projects to the central nucleus, but the parabrachial area itself is
    not a fear structure.)
*   NeuroNames — Parabrachial nuclei; FMA — Parabrachial nucleus.
"""