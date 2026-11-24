"""
infrastructure.brainparts.midbrain.cranial_nerve_nuclei.right.edinger_westphal_nucleus
======================================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── cranial_nerve_nuclei
    │   ├── left
    │   │   └── ...
    │   └── right
    │       ├── oculomotor_nucleus
    │       ├── trochlear_nucleus
    │       ├── mesencephalic_trigeminal_nucleus
    │       └── edinger_westphal_nucleus   <-- THIS MODULE (leaf —
    │                                           FUNCTIONAL parent)
    └── tegmentum
        ├── left
        │   └── ...
        └── right
            ├── oculomotor_nucleus
            ├── trochlear_nucleus
            ├── mesencephalic_trigeminal_nucleus
            ├── edinger_westphal_nucleus   (SAME LEAF —
            │                               TOPOGRAPHIC parent)
            ├── substantia_nigra
            └── ...

**Primary synonym:** Right Edinger-Westphal nucleus; right EW; right
EWpg (the preganglionic parasympathetic EW — **see the EWpg/EWcp
distinction below**); right accessory oculomotor nucleus; right
nucleus of Edinger-Westphal; the right CN III preganglionic
parasympathetic nucleus.
**Cytoarchitectonic designation:** **Not a Brodmann area** (brainstem).
A **cholinergic preganglionic parasympathetic nucleus** in the
**rostral midbrain tegmentum**, **dorsomedial to the right oculomotor
nucleus**, at the level of the **superior colliculus**. It is
**cytoarchitectonically distinct** from the oculomotor nucleus,
though in close proximity. **Molecularly defined** in modern work as
the **cholinergic (ChAT⁺, VGlut2⁻) preganglionic population** —
**EWpg** — distinct from the **urocortin-1⁺ (Ucn1⁺)** centrally
projecting population — **EWcp** — that shares the same regional name.
**This leaf is EWpg only.** See *EWpg vs EWcp*.
**Part of:** The **cranial_nerve_nuclei** functional grouping
container → **right** side container (functional parent), **and** the
**tegmentum** topographic container → **right** side container
(topographic parent). **Dual-parent leaf — see *Structural parent*
below and *Cross-Listing Statement*.**
**Structural parent (FUNCTIONAL):** ``.../cranial_nerve_nuclei/right/``
→ **direct child** of the **right side container** of the
cranial_nerve_nuclei functional grouping container.
**Structural parent (TOPOGRAPHIC):** ``.../tegmentum/right/`` →
**direct child** of the **right side container** of the tegmentum
topographic container.
**Structural children:** **None.** This is a **leaf** module. The
**cholinergic phenotype** (ChAT, ACh synthesis, nicotinic and
muscarinic receptors) is a ``chemicals_hormones``-layer fact — see
*Chemicals-Layer Discipline* — and is documented as **prose**, not as
structural children.
**Boundary status (DUAL-PARENT LEAF — CROSS-LISTED between
``cranial_nerve_nuclei/right/`` and ``tegmentum/right/``):** **Boundary
case — the right Edinger-Westphal nucleus is a DUAL-PARENT LEAF.** It
is reachable by **two** structural paths:
*   **Functional path** —
    ``.../cranial_nerve_nuclei/right/edinger_westphal_nucleus/``
*   **Topographic path** —
    ``.../tegmentum/right/edinger_westphal_nucleus/``
**Both resolve to the SAME leaf** — this module. **This is the
right-side counterpart of the left leaf's dual-parent anchor** — the
same cross-listing, mirrored. Consumers resolving the leaf by
**either** path get **the same module**. Consumers must **not**
assume the two paths lead to different structures — they lead to
**one leaf**, dual-parented. See *Cross-Listing Statement*.
**Boundary status (EWpg — NOT EWcp — the preganglionic parasympathetic
population only):** **Boundary case — the right Edinger-Westphal
nucleus (this leaf) is the **preganglionic parasympathetic** EW —
**EWpg** — NOT the **centrally projecting** EW — **EWcp**.** Modern
work distinguishes **two molecularly and functionally distinct
populations** that historically shared the name "Edinger-Westphal
nucleus":
*   **EWpg** — **cholinergic (ChAT⁺)**, **preganglionic
    parasympathetic**, projects to the **ciliary ganglion** →
    sphincter pupillae and ciliary muscle — **the CN IIIp nucleus,
    and THIS LEAF**.
*   **EWcp** — **urocortin-1⁺ (Ucn1⁺)**, **centrally projecting**,
    projects to the **spinal cord and brainstem**, involved in
    **stress, feeding, alcohol response, and pain modulation** —
    **NOT the CN III system**, and **NOT this leaf**.
**They are DIFFERENT POPULATIONS that share a regional name.** The
EWcp is **not a cranial-nerve nucleus** — it does **not** project to
the ciliary ganglion, does **not** mediate the pupillary light
reflex, and is **not** part of the CN III system. Consumers must
**not** conflate EWpg with EWcp, and must **not** attribute
**stress/alcohol/feeding** functions to this leaf. **If the tree were
to include EWcp, it would be a ``.../tegmentum/right/`` leaf
only — NOT a ``.../cranial_nerve_nuclei/right/`` leaf.** See *EWpg vs
EWcp* below.
**Boundary status (NOT the right oculomotor nucleus — the oculomotor
nucleus is the SOMATIC MOTOR nucleus):** **Boundary case — the right
Edinger-Westphal nucleus is NOT the right oculomotor nucleus.** The
**right oculomotor nucleus (CN III somatic)**
(``.../cranial_nerve_nuclei/right/oculomotor_nucleus/`` **and**
``.../tegmentum/right/oculomotor_nucleus/``) is the **somatic motor**
nucleus — it innervates the **superior rectus**, **inferior rectus**,
**medial rectus**, **inferior oblique**, and **levator palpebrae
superioris**. The **right Edinger-Westphal nucleus** (here) is the
**preganglionic parasympathetic** nucleus — it innervates the
**ciliary ganglion** → **sphincter pupillae** and **ciliary
muscle**. **They are DIFFERENT NUCLEI** in **close proximity** (EW is
**dorsomedial** to the oculomotor nucleus) — the **oculomotor** is
**somatic motor**; the **Edinger-Westphal** is **preganglionic
parasympathetic**. The **CN III fascicles** carry **both** sets of
axons (somatic motor + preganglionic parasympathetic), but the
**nuclei** are **distinct**. Consumers must **not** conflate the two,
and must **not** assume a right CN III palsy implies a right EW
nuclear lesion — the **nuclear** lesion and the **fascicular** lesion
are **different** (see *Associated Disorders*).
**Boundary status (NOT the right trochlear nucleus — the trochlear
nucleus is a DIFFERENT CN):** **Boundary case — the right
Edinger-Westphal nucleus is NOT the right trochlear nucleus.** The
**right trochlear nucleus (CN IV)**
(``.../cranial_nerve_nuclei/right/trochlear_nucleus/`` **and**
``.../tegmentum/right/trochlear_nucleus/``) is the **somatic motor**
nucleus for the **superior oblique** — a **different cranial nerve**
(CN IV, not CN III). **They are DIFFERENT NUCLEI** — the **EW** is
**CN III preganglionic parasympathetic**; the **trochlear** is
**CN IV somatic motor**. Consumers must **not** conflate the two.
**Boundary status (NOT the right pretectal nucleus — the pretectal
nucleus is the AFFERENT relay, DIENCEPHALON):** **Boundary case — the
right Edinger-Westphal nucleus is NOT the right pretectal nucleus.**
The **pretectal nuclei** — the **olivary pretectal nucleus** and
the **nucleus of the optic tract** — are **diencephalon**
structures (``.../forebrain/diencephalon/pretectal_nuclei/``), at
the **diencephalon-midbrain junction**. They are the **afferent
relay** of the **pupillary light reflex** — they receive retinal
input and project **bilaterally** to **both** EW nuclei. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **pretectal
nucleus** is **diencephalon**; the **EW** is **midbrain**.
Consumers must **not** conflate the two, and must **not** resolve the
pretectal nucleus through the midbrain path. **The pupillary light
reflex spans diencephalon → midbrain → peripheral** — the pretectal
nucleus (diencephalon) projects to EW (midbrain), which projects to
the ciliary ganglion (peripheral).
**Boundary status (NOT the right ciliary ganglion — the ciliary
ganglion is PERIPHERAL, the postganglionic relay):** **Boundary case —
the right Edinger-Westphal nucleus is NOT the right ciliary
ganglion.** The **ciliary ganglion** is a **peripheral
parasympathetic ganglion** — it contains the **postganglionic
parasympathetic neuron cell bodies** that innervate the **sphincter
pupillae** and the **ciliary muscle**. It is **NOT a midbrain
structure** — it is **wired elsewhere** (in the periphery, near the
orbit). The **right EW** (here) is the **preganglionic** nucleus —
it **projects to** the ciliary ganglion; the ciliary ganglion is
**downstream** of EW. **They are DIFFERENT STRUCTURES across the
CNS-PNS boundary.** Consumers must **not** conflate the two, and must
**not** resolve the ciliary ganglion through the midbrain path.
**Boundary status (NOT the right CN III nerve or the right CN III
fascicles — the NERVE is peripheral, the FASCICLES are the
conduction pathway):** **Boundary case — the right
Edinger-Westphal nucleus is NOT the right oculomotor nerve and NOT
the right CN III fascicles.** The **right CN III nerve** is the
**peripheral axon bundle** — it is **wired elsewhere** (peripheral
nervous system). The **right CN III fascicles** traverse the **right
cerebral peduncle** (a conduction-pathway module) **en route** to
the interpeduncular fossa. **The EW axons travel IN the CN III nerve
and IN the CN III fascicles**, but the **nerve** and the
**fascicles** are **not the nucleus**. **They are DIFFERENT
STRUCTURES** — the **EW nucleus** is **grey matter**; the **CN III
fascicles** are **fibers traversing the crus cerebri**; the **CN III
nerve** is **peripheral**. Consumers must **not** conflate the EW
nucleus with the CN III nerve or with the CN III fascicles, and must
**not** forget that **EW fibers are what make the CN III palsy
pupil-involving** — a CN III **fascicular** lesion (e.g., Weber
syndrome) **does** involve EW fibers, producing **mydriasis**, but
the **lesion site** is the **fascicle**, not the **EW nucleus**. See
*Associated Disorders*.
**Boundary status (NOT the MLF — the MLF is a CONDUCTION PATHWAY):**
**Boundary case — the right Edinger-Westphal nucleus is NOT the right
MLF.** The **medial longitudinal fasciculus (MLF)** is a
**longitudinal fiber tract** — a **conduction pathway** — that
**coordinates** the **CN III**, **CN IV**, and **CN VI** nuclei for
**conjugate gaze**. It is **wired elsewhere** (as a brainstem
longitudinal tract). The **right EW** is a **nucleus** — grey matter.
**A right MLF lesion produces RIGHT INTERNUCLEAR OPHTHALMOPLEGIA
(INO) — NOT a right EW lesion and NOT a right CN III palsy.** These
are **different syndromes** — the INO is a **conduction-pathway**
deficit (**adduction weakness with abducting nystagmus**), not a
**nuclear** or **fascicular** palsy. Consumers must **not** conflate
the EW with the MLF, and must **not** resolve the MLF through the EW
path.
**Boundary status (NOT the right superior colliculus — the superior
colliculus is a TECTUM structure):** **Boundary case — the right
Edinger-Westphal nucleus is NOT the right superior colliculus.** The
**right superior colliculus**
(``.../tectum/right/superior_colliculus/``) is the
**visual/oculomotor orienting** structure — it **projects to** the
CN III nuclei via the **tectobulbar tract** to drive **saccades**
and the **visual grasp reflex**. **It does NOT project to the EW
nucleus for the pupillary light reflex** — the pupillary light
reflex afferent is the **pretectal nucleus**, not the superior
colliculus. **They are DIFFERENT STRUCTURES** — the **superior
colliculus** is **tectum**; the **EW** is **tegmentum**. Consumers
must **not** conflate the two, and must **not** assume the superior
colliculus drives the pupillary light reflex — it does not.
**Boundary status (NOT the right riMLF or the right interstitial
nucleus of Cajal — those are GAZE CENTERS, not CN nuclei):**
**Boundary case — the right Edinger-Westphal nucleus is NOT the right
riMLF and NOT the right interstitial nucleus of Cajal.** The
**riMLF** and the **interstitial nucleus of Cajal** are **vertical
gaze centers** in the rostral midbrain tegmentum — **premotor
saccade generators**, not **CN nuclei**. They are **tegmentum**
structures but are **NOT** cross-listed under
``cranial_nerve_nuclei/``. The **right EW** (here) is a **CN III
preganglionic parasympathetic** nucleus. Consumers must **not**
conflate the EW with the gaze centers, and must **not** resolve the
riMLF or interstitial nucleus of Cajal through the EW path.
**Boundary status (NOT the left Edinger-Westphal nucleus — the SIDE
boundary; and the CONSENSUAL reflex is PRETECTAL, not EW-EW
coupling):** **Boundary case — the right Edinger-Westphal nucleus is
NOT the left Edinger-Westphal nucleus, and the CONSENSUAL pupillary
light reflex is mediated at the PRETECTAL level, NOT by direct
EW-EW coupling.** The **left EW**
(``.../cranial_nerve_nuclei/left/edinger_westphal_nucleus/``
**and** ``.../tegmentum/left/edinger_westphal_nucleus/``) is the
**left** preganglionic parasympathetic nucleus. The two are
**independent nuclei** — there is **no** direct **EW-EW** coupling.
The **consensual pupillary light reflex** (light in one eye → both
pupils constrict) is mediated by the **pretectal nucleus's
bilateral projection** — the pretectal nucleus projects to **BOTH**
EW nuclei, and this **bilateral pretectal projection** is what makes
the reflex consensual. **This is the key point: the "consensual"
pathway is upstream of EW, not between the two EWs.** Consumers must
**not** conflate the right EW with the left EW, and must **not**
assume the two EWs are **directly coupled** — they are **independent
nuclei** coordinated **upstream** at the pretectal level.
**Boundary status (PREGANGGLIONIC PARASYMPATHETIC NUCLEUS — NOT a
somatic motor nucleus, NOT a sensory nucleus, NOT an oscillator, NOT
a premotor pool, NOT a conduction pathway):** **Boundary case —
the right Edinger-Westphal nucleus is a PREGANGLIONIC PARASYMPATHETIC
NUCLEUS.** In the family's **structure-class taxonomy**, it is a
**motor nucleus** — specifically an **autonomic (parasympathetic)
motor nucleus** — **not** a somatic motor nucleus (CN III, CN IV),
**not** a sensory nucleus (CN Vm), **not** an oscillator, **not** a
premotor pool, **not** a conduction pathway, and **not** a grey-matter
processing nucleus (substantia nigra, red nucleus). **Motor nuclei
carry NO coupling warning** — same rule as premotor pools, sensor
nuclei, conduction pathways, and the CN III/IV somatic motor
nuclei. Its coordination with the **left EW** is via the
**pretectal bilateral projection** — **not** intrinsic
nucleus-to-nucleus coupling. It is a **strict mirror with NO
warning**. See *Lateralization Notes* and *Design Contract*.
**Boundary status (CHEMICALS-LAYER DISCIPLINE — the cholinergic
phenotype is a chemicals_hormones-layer fact):** **Boundary case —
the right Edinger-Westphal nucleus is **cholinergic**, and the
**cholinergic phenotype** is a ``chemicals_hormones``-layer
fact.** The EW neurons **synthesize acetylcholine** (via **choline
acetyltransferase, ChAT**) and **release ACh** onto the **ciliary
ganglion** (which is **nicotinic**); the **postganglionic** fibers
release **ACh** onto the **sphincter pupillae** and **ciliary
muscle** (which are **muscarinic**). The **cholinergic phenotype**
— ChAT, ACh synthesis, nicotinic and muscarinic receptors — is a
**``chemicals_hormones``-layer fact**, not a midbrain structural
fact. Consumers must **not** import the **cholinergic phenotype**
into the midbrain structural layer; the **structural** module
documents the **anatomy** and **references** the chemicals layer as
prose. *(This is the same discipline the midbrain container imposes
on the dopaminergic phenotype of the substantia nigra and the ventral
tegmental area — see the midbrain container's Design Contract.)*

Overview
--------
The right Edinger-Westphal nucleus (right EW) is the **right CN III
preganglionic parasympathetic nucleus** — the **EWpg** population —
in the **right rostral midbrain tegmentum**, **dorsomedial to the
right oculomotor nucleus**. It is the **efferent limb** of the
**pupillary light reflex** and the **efferent limb** of the
**accommodation and miosis components of the near triad**. It is a
**dual-parent leaf** — reachable by **both** the functional path
(``.../cranial_nerve_nuclei/right/edinger_westphal_nucleus/``) and
the topographic path
(``.../tegmentum/right/edinger_westphal_nucleus/``).

**The right EW is the EWpg — the preganglionic parasympathetic EW —
NOT the EWcp.** The **EWcp** (centrally projecting, urocortin-1⁺) is
a **distinct population** — **not a CN III nucleus**, **not this
leaf**.

**The right EW is a PREGANGLIONIC PARASYMPATHETIC NUCLEUS — NOT a
somatic motor nucleus, NOT a sensory nucleus.** The **CN III somatic
motor** functions (extraocular muscles, levator palpebrae) belong to
the **right oculomotor nucleus** (``.../oculomotor_nucleus/``); the
**parasympathetic** functions (pupil constriction, lens
accommodation) belong to the **right EW** (here). **The two are
distinct nuclei** in close proximity; the **CN III fascicles** carry
**both** sets of axons.

**The right EW is a MOTOR NUCLEUS in the family's taxonomy.** It
carries **NO coupling warning** — same rule as CN III, CN IV,
premotor pools, sensor nuclei, and conduction pathways. Its
coordination with the **left EW** is via the **pretectal bilateral
projection** — **not** EW-EW coupling.

**The right EW is the right-side counterpart of the cross-listing
anchor.** This leaf is the **right-side** instance of the
**dual-parent leaf** — both structural parents named together, the
**functional parent** (``.../cranial_nerve_nuclei/right/``) and the
**topographic parent** (``.../tegmentum/right/``). Consumers
resolving the leaf by **either** path get **this module**. See
*Cross-Listing Statement*.

EWpg vs EWcp (the crucial distinction)
--------------------------------------
Modern work distinguishes **two molecularly and functionally distinct
populations** that historically shared the name "Edinger-Westphal
nucleus":

*   **EWpg — the preganglionic parasympathetic EW — THIS LEAF.**
    *   **Cholinergic (ChAT⁺).**
    *   **Preganglionic parasympathetic.**
    *   Projects to the **ciliary ganglion** → **sphincter
        pupillae** and **ciliary muscle**.
    *   Mediates the **pupillary light reflex** and the
        **accommodation and miosis components of the near triad**.
    *   **Is a cranial-nerve nucleus (CN IIIp).**

*   **EWcp — the centrally projecting EW — NOT THIS LEAF.**
    *   **Urocortin-1⁺ (Ucn1⁺)** — a CRF-family peptide.
    *   **Centrally projecting** — to the **spinal cord and
        brainstem**.
    *   Involved in **stress responses**, **feeding**, **alcohol
        consumption**, and **pain modulation**.
    *   **Is NOT a cranial-nerve nucleus** — does **not** project
        to the ciliary ganglion, does **not** mediate the
        pupillary light reflex, is **not** part of the CN III
        system.

**The EWpg and EWcp are DIFFERENT POPULATIONS** — molecularly
distinct (cholinergic vs. urocortin-1⁺), developmentally distinct,
and functionally distinct (parasympathetic vs. centrally
projecting). **They are NOT the same structure under two names** —
the **conflation is a historical artifact**, corrected in modern
work (Kozicz, Horn, and others).

**This leaf is EWpg only.** The **EWcp is out of scope** for the
`cranial_nerve_nuclei/` container — it is **not a CN nucleus**, and
it would be a **`.../tegmentum/right/` leaf only** if the tree
included it. The **boundary status** above states this explicitly.

The Right Edinger-Westphal Nucleus / Right Oculomotor Nucleus Boundary
---------------------------------------------------------------------
This is the **parasympathetic / somatic-motor** boundary in the CN III
nuclear complex:

*   **Right Edinger-Westphal nucleus** (this module) — the **CN III
    preganglionic parasympathetic** nucleus — **EWpg**.

*   **Right oculomotor nucleus**
    (``.../cranial_nerve_nuclei/right/oculomotor_nucleus/`` **and**
    ``.../tegmentum/right/oculomotor_nucleus/``) — the **CN III
    somatic motor** nucleus — **superior rectus, inferior rectus,
    medial rectus, inferior oblique, levator palpebrae superioris**.

**They are DIFFERENT NUCLEI in close proximity** — EW is
**dorsomedial** to the oculomotor nucleus. **Consumers must not
conflate the two** — the **oculomotor** is **somatic motor**; the
**EW** is **preganglionic parasympathetic**.

**A right CN III palsy that involves the pupil (mydriasis)** indicates
involvement of **EW fibers** — but the **fascicular** lesion is in
the **crus cerebri** (Weber syndrome) or along the **CN III nerve**,
not necessarily in the **EW nucleus**. **An isolated EW nuclear
lesion** would produce **pupil-only** deficit (mydriasis, loss of
light reflex, loss of accommodation) **without** extraocular palsy —
**rare** in practice, and **distinct** from a CN III nuclear or
fascicular palsy. See *Associated Disorders*.

The Right Edinger-Westphal Nucleus / Right Trochlear Nucleus Boundary
--------------------------------------------------------------------
This is the **CN IIIp / CN IV** boundary:

*   **Right Edinger-Westphal nucleus** (this module) — **CN III
    preganglionic parasympathetic**.

*   **Right trochlear nucleus**
    (``.../cranial_nerve_nuclei/right/trochlear_nucleus/`` **and**
    ``.../tegmentum/right/trochlear_nucleus/``) — **CN IV somatic
    motor** — superior oblique.

**They are DIFFERENT NUCLEI for DIFFERENT CRANIAL NERVES.**
Consumers must **not** conflate the two.

The Right Edinger-Westphal Nucleus / Pretectal Nucleus Boundary
---------------------------------------------------------------
This is the **efferent / afferent** boundary of the pupillary light
reflex — **across a lobe boundary**:

*   **Right Edinger-Westphal nucleus** (this module) — the **efferent**
    limb of the pupillary light reflex — **midbrain**.

*   **Pretectal nuclei** — the **olivary pretectal nucleus** and the
    **nucleus of the optic tract** —
    (``.../forebrain/diencephalon/pretectal_nuclei/``) — the
    **afferent** relay of the pupillary light reflex —
    **diencephalon**.

**The pretectal nucleus PROJECTS BILATERALLY to both EW nuclei** —
this is the mechanism of the **consensual pupillary light reflex**.
**They are DIFFERENT STRUCTURES across a lobe boundary** — the
**pretectal nucleus** is **diencephalon**; the **EW** is
**midbrain**. Consumers must **not** conflate the two, and must
**not** resolve the pretectal nucleus through the midbrain path.

The Right Edinger-Westphal Nucleus / Ciliary Ganglion Boundary
--------------------------------------------------------------
This is the **preganglionic / postganglionic** boundary — **across
the CNS-PNS boundary**:

*   **Right Edinger-Westphal nucleus** (this module) — the
    **preganglionic** parasympathetic nucleus — **CNS**.

*   **Right ciliary ganglion** — the **postganglionic** parasympathetic
    relay — **peripheral**, near the orbit.

**The EW PROJECTS TO the ciliary ganglion; the ciliary ganglion is
DOWNSTREAM of EW.** **They are DIFFERENT STRUCTURES across the
CNS-PNS boundary.** Consumers must **not** conflate the two.

The Right Edinger-Westphal Nucleus / CN III Nerve and CN III Fascicles Boundary
------------------------------------------------------------------------------
This is the **nucleus / nerve / fascicle** boundary:

*   **Right Edinger-Westphal nucleus** (this module) — the **nucleus**
    — grey matter.

*   **Right CN III fascicles** — the **axons** traversing the
    **right cerebral peduncle** — white matter.

*   **Right CN III nerve** — the **peripheral** axon bundle —
    peripheral nervous system.

**The EW axons travel IN the CN III fascicles and IN the CN III
nerve** — but the **nucleus** is **not** the **fascicle** and
**not** the **nerve**. **A CN III fascicular lesion** (e.g., **Weber
syndrome** — see ``.../cerebral_peduncle/right/crus_cerebri/``) **does
involve EW fibers**, producing **mydriasis**, but the **lesion site**
is the **fascicle**, not the **EW nucleus**. Consumers must **not**
conflate the three.

The Right Edinger-Westphal Nucleus / MLF Boundary
-------------------------------------------------
This is the **nucleus / conduction pathway** boundary:

*   **Right Edinger-Westphal nucleus** (this module) — the **CN IIIp
    nucleus**.

*   **Right MLF** — the **medial longitudinal fasciculus** — a
    **longitudinal fiber tract** — **conduction pathway** — wired
    elsewhere (as a brainstem tract).

**A right MLF lesion produces RIGHT INTERNUCLEAR OPHTHALMOPLEGIA
(INO) — NOT a right EW lesion and NOT a right CN III palsy.** These
are **different syndromes**. Consumers must **not** conflate the
two.

The Right Edinger-Westphal Nucleus / Superior Colliculus Boundary
-----------------------------------------------------------------
This is the **pupillary / saccadic** boundary:

*   **Right Edinger-Westphal nucleus** (this module) — the **CN IIIp
    nucleus** — mediates the **pupillary light reflex** and the
    **near triad**.

*   **Right superior colliculus**
    (``.../tectum/right/superior_colliculus/``) — the **visual and
    oculomotor orienting** structure — drives **saccades** via the
    **tectobulbar tract** to the CN III nuclei.

**The superior colliculus does NOT drive the pupillary light reflex
— that is the pretectal nucleus.** They are **different structures
in different midbrain compartments**. Consumers must **not** conflate
the two.

The Right Edinger-Westphal Nucleus / riMLF and Interstitial Nucleus of Cajal Boundary
------------------------------------------------------------------------------------
This is the **CN IIIp nucleus / gaze center** boundary:

*   **Right Edinger-Westphal nucleus** (this module) — the **CN IIIp
    nucleus**.

*   **Right riMLF** and **right interstitial nucleus of Cajal** —
    **vertical gaze centers** — **premotor saccade generators** —
    tegmentum leaves but **NOT** cross-listed under
    `cranial_nerve_nuclei/`.

**They are DIFFERENT STRUCTURES** — the **EW** is a **CN nucleus**;
the **riMLF** and **interstitial nucleus of Cajal** are **premotor
gaze centers**. Consumers must **not** conflate the two.

The Right Edinger-Westphal Nucleus / Left Edinger-Westphal Nucleus Boundary
---------------------------------------------------------------------------
This is the **side** boundary — and the **consensual reflex** is
**pretectal**, not EW-EW:

*   **Right Edinger-Westphal nucleus** (this module) — the **right
    EWpg**.

*   **Left Edinger-Westphal nucleus**
    (``.../cranial_nerve_nuclei/left/edinger_westphal_nucleus/``
    **and** ``.../tegmentum/left/edinger_westphal_nucleus/``) —
    the **left EWpg**.

**They are STRICTLY SYMMETRIC NUCLEI** — each is an **independent**
preganglionic parasympathetic nucleus. The **consensual pupillary
light reflex** (light in one eye → both pupils constrict) is mediated
by the **pretectal nucleus's bilateral projection** — the pretectal
nucleus projects to **BOTH** EW nuclei. **The two EWs are NOT
directly coupled** — the coordination is **upstream** at the
pretectal level. Consumers must **not** conflate the right EW with
the left EW, and must **not** assume the two EWs are **directly
coupled** — they are **independent nuclei coordinated upstream**.

Function in the Human Brain
---------------------------
The right Edinger-Westphal nucleus's function is **preganglionic
parasympathetic control of the right pupil and right lens** — **NOT**
somatic motor control of the extraocular muscles, **NOT** centrally
projecting stress/feeding functions:

*   **Pupillary Light Reflex — Efferent Limb (right):** The right EW
    **constricts the right pupil** in response to light. The reflex
    arc: **light → right retina → right optic nerve → right pretectal
    nucleus (diencephalon) → BILATERAL projection to right and left
    EW nuclei → right and left ciliary ganglia → right and left
    sphincter pupillae**. The **direct response** is the right pupil
    constricting when light shines in the **right** eye; the
    **consensual response** is the right pupil constricting when light
    shines in the **left** eye (mediated by the **left pretectal**
    projecting bilaterally to **both** EW nuclei). **The
    "consensual" mechanism is pretectal, not EW-EW.**

*   **Near Triad — Accommodation and Miosis (right):** The right EW
    **constricts the right pupil (miosis)** and **accommodates the
    right lens (ciliary muscle contraction)** during the **near
    response** — when the eyes converge on a near target. The
    **convergence** component is **CN III somatic** (medial rectus,
    via the **oculomotor nucleus**); the **accommodation** and
    **miosis** components are **EW** (via the **ciliary ganglion**).
    **The right EW does NOT control convergence** — that is the right
    oculomotor nucleus.

*   **NOT somatic motor.** The right EW does **not** innervate the
    extraocular muscles or the levator palpebrae — those are the
    **right oculomotor nucleus** (CN III somatic).

*   **NOT centrally projecting.** The right EW is the **preganglionic
    parasympathetic** EW — it does **NOT** project to the spinal cord
    or brainstem, and is **NOT** involved in stress, feeding, or
    alcohol responses. Those are the **EWcp** — **NOT this leaf**.

*   **NOT an oscillator.** The EW is a **motor nucleus** — it does
    **not** generate a rhythm. It **fires in response to upstream
    drive** (from the pretectal nucleus for the light reflex; from
    cortical and other forebrain centers for the near response). Its
    coordination with the contralateral EW is via the **pretectal
    bilateral projection** — **not** intrinsic EW-EW coupling.

**The unifying theme:** the right EW is the **right CN III preganglionic
parasympathetic nucleus** — the **efferent limb of the pupillary
light reflex** and the **efferent limb of the accommodation and
miosis components of the near triad**. It is **preganglionic
parasympathetic**, **NOT somatic motor** (**right oculomotor
nucleus**), **NOT centrally projecting** (**EWcp**), and **NOT an
oscillator** — it **fires in response to upstream drive**.

Associated Disorders
--------------------
The right Edinger-Westphal nucleus has **no named syndrome of its own**
— the pupillary findings that its dysfunction produces are
**components** of **CN III syndromes** (fascicular) or of
**light-near dissociation syndromes** (upstream/downstream), **not**
an **EW-nuclear** syndrome. Its clinical associations are **indirect**:

*   **Pupil-Involving CN III Palsy (INDIRECT — via the CN III
    fascicles or nerve, NOT the EW nucleus):** A **right CN III
    palsy** that involves the pupil — **right mydriasis**, loss of
    right pupillary light reflex, loss of right accommodation —
    occurs when the **CN III fascicles** are compressed by a
    **posterior communicating artery aneurysm** or **uncal
    herniation**. The **pupillomotor fibers (EW fibers)** are on the
    **superficial dorsomedial aspect** of the CN III nerve and are
    **vulnerable** to compression. The **lesion site** is the
    **fascicle** or the **nerve**, **not the EW nucleus**. **A
    pupil-sparing CN III palsy** (e.g., **diabetic ophthalmoplegia**,
    **microvascular ischemia**) is the **opposite** — the
    **pupillomotor fibers are spared** because they are
    **superficial** and the **ischemia** affects the **core of the
    nerve**. **The EW nucleus itself is rarely the site of
    pathology** — the **pupil findings** reflect **fascicular or
    nerve** lesions.

*   **Argyll Robertson Pupil (NOT an EW Nuclear Lesion — UPSTREAM
    PRETECTAL or DOWNSTREAM CILIARY):** **Argyll Robertson (AR)
    pupil** is a **light-near dissociation** — small, irregular
    pupils that **do not react to light** but **do constrict during
    the near response**. Classically associated with **neurosyphilis
    (tabes dorsalis)**, now more commonly seen in **diabetes**,
    **multiple sclerosis**, and other conditions. The **lesion
    site** is **debated** — modern work suggests **pretectal**
    (diencephalon) or **ciliary ganglion** (peripheral) or
    **postganglionic** involvement — **NOT the EW nucleus itself**.
    **AR pupil is NOT a pure EW nuclear lesion.** See the pretectal
    and ciliary ganglion modules.

*   **Parinaud Syndrome (NOT an EW Nuclear Lesion — DORSAL MIDBRAIN
    / TECTUM):** **Parinaud syndrome** — **light-near dissociation**,
    **upgaze palsy**, **convergence-retraction nystagmus**,
    **eyelid retraction (Collier sign)** — is a **dorsal midbrain
    syndrome** (superior colliculus / pretectum / posterior
    commissure). The **light-near dissociation** in Parinaud reflects
    **pretectal** involvement (diencephalon) — **NOT the EW nucleus**.
    See the superior colliculus and pretectal modules.

*   **Adie's Tonic Pupil, Holmes-Adie Syndrome, Ross Syndrome (NOT
    EW Nuclear Lesions — CILIARY GANGLION / POSTGANGLIONIC):**
    **Adie's tonic pupil** — a **large, poorly reactive pupil** with
    **tonic constriction to near** and **denervation
    supersensitivity** — is a **ciliary ganglion** or
    **postganglionic** parasympathetic lesion — **NOT an EW
    nuclear** lesion. **Holmes-Adie syndrome** (Adie's + absent
    tendon reflexes) and **Ross syndrome** (Adie's + segmental
    anhidrosis) are **also ciliary ganglion / postganglionic** —
    **NOT EW nuclear**. See the ciliary ganglion module.

*   **Isolated EW Nuclear Lesion (RARE):** A **focal lesion** of the
    **right EW nucleus** — from **small infarction**, **demyelination**,
    or **tumor** — would produce **right mydriasis**, **loss of right
    pupillary light reflex**, **loss of right accommodation** —
    **without extraocular palsy** (because the **right oculomotor
    nucleus** is spared) and **without ptosis** (levator is oculomotor
    nucleus). This is **rare in practice** — most "EW lesions"
    are **fascicular** or **nerve** lesions. **No named syndrome.**

*   **Weber Syndrome (INDIRECT — via the CN III FASCICLES in the right
    crus cerebri, NOT the EW nucleus):** **Right Weber syndrome** —
    **right CN III palsy** (including **right mydriasis** from EW
    fiber involvement) **+ left hemiplegia** — is a **right crus
    cerebri** lesion. The **EW fibers** travel in the **CN III
    fascicles** through the **right crus cerebri**, so the
    **mydriasis** is part of the **CN III palsy** — but the **lesion
    site** is the **fascicle** in the **crus cerebri**, **not the EW
    nucleus**. See ``.../cerebral_peduncle/right/crus_cerebri/``.

*   **EWcp-Related Conditions (NOT THIS LEAF — EWcp is a distinct
    population):** **Stress**, **feeding**, **alcohol consumption**,
    and **pain modulation** are functions of the **EWcp** — the
    **centrally projecting urocortin-1⁺ population** — **NOT the
    EWpg** (this leaf). The **EWcp** is **not a CN nucleus** and is
    **not wired here**.

*   **No Named "Edinger-Westphal Nucleus Syndrome":** The right EW is
    a **preganglionic parasympathetic motor nucleus** — it has **no
    named syndrome of its own**. Its clinical relevance is
    **indirect**, via the **CN III fascicles and nerve** (pupil
    involvement in CN III palsies) and the **light-near dissociation
    syndromes** (**upstream** pretectal, **downstream** ciliary
    ganglion).

**What is NOT here:** The right EW is **not** the substrate for
**Argyll Robertson pupil** (upstream / downstream — debated, **NOT**
EW nuclear), **Parinaud syndrome** (dorsal midbrain / tectum),
**Adie's tonic pupil / Holmes-Adie / Ross** (ciliary ganglion /
postganglionic), **Weber syndrome** (crus cerebri — **cross-reference**,
**NOT claim**), **Benedikt syndrome** (tegmentum — red nucleus +
CN III), **Claude syndrome** (tegmentum — red nucleus + CN III),
**Nothnagel syndrome** (tectum / colliculi), **Millard-Gubler
syndrome** (pons), **Wallenberg syndrome** (lateral medulla),
**locked-in syndrome** (basis pontis), **CCHS** (RTN), **OIRD**
(pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger complex
+ arcuate nucleus), **essential hypertension / sympathetic
overactivity** (C1 group / RVLM), **Parkinson's disease**
(substantia nigra — tegmentum), **Huntington's disease** (striatum
— telencephalon), or **Kluver-Bucy syndrome** (amygdala). Its
clinical relevance is **indirect**, via the **CN III fascicles and
nerve** and the **light-near dissociation syndromes**. **No named
Edinger-Westphal nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **right** Edinger-Westphal nucleus leaf. The right and
left EW nuclei are **bilaterally symmetric** and carry **NO coupling
warning of their own** — and they **inherit no warning from any
oscillator**:

*   **Bilateral Independent Nuclei:** Each hemisphere has its own EW
    nucleus — each is an **independent preganglionic parasympathetic
    nucleus** innervating **its own** (predominantly **ipsilateral**)
    ciliary ganglion.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to MOTOR NUCLEI):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **right EW** is a **motor nucleus** — it does
    **not** generate a rhythm, so it does **not** carry the
    **oscillator coupling warning**. Its **right** and **left**
    sides are **independent nuclei** — there is **no** EW-EW
    coupling. **This is the same rule that applies to the CN III and
    CN IV somatic motor nuclei, to the premotor pools, to the
    sensor nuclei, and to the conduction pathways:**
    **coordination is downstream (for motor) or upstream (for
    sensory), not intrinsic.**

*   **The Consensual Reflex is PRETECTAL, NOT EW-EW:** The
    **consensual pupillary light reflex** — light in one eye → both
    pupils constrict — is mediated by the **pretectal nucleus's
    bilateral projection** to **both** EW nuclei. **The two EWs are
    NOT directly coupled** — the **coordination is upstream** at the
    pretectal level. A consumer that assumes "the two EWs must be
    coupled to produce the consensual reflex" is **wrong** — the
    coupling is **pretectal**, and the two EWs are **independent**.

*   **Clinical Laterality:**
    *   A **right EW nuclear lesion** → **right mydriasis**, loss of
        **right direct** and **right consensual** pupillary light
        reflex, loss of **right accommodation** — **without**
        extraocular palsy (right oculomotor nucleus spared).
    *   A **right optic nerve lesion** (afferent) → **right pupil
        does not respond to light in the right eye (right direct
        lost)**, but **right pupil constricts to light in the left
        eye (right consensual preserved)** — because the **left
        pretectal** still projects to **both** EWs. The **right
        consensual** is preserved because the **right EW** is intact.
    *   A **right CN III fascicular lesion** (e.g., Weber syndrome) →
        **right CN III palsy** with **right mydriasis** (EW fiber
        involvement) — **plus** extraocular palsy and **left
        hemiplegia**. The **mydriasis** is EW-fiber involvement, but
        the **lesion site** is the **fascicle**, not the nucleus.
    *   A **right MLF lesion** → **right internuclear ophthalmoplegia
        (INO)** — **adduction weakness of the right eye with
        abducting nystagmus of the left eye** — **NOT** a right EW
        lesion and **NOT** a right CN III palsy. The **pupils are
        typically spared** in INO (the MLF coordinates somatic
        motor, not parasympathetic). **This is the key
        INO-vs-CN-III distinction.**
    *   **A consumer that assumes "right EW = left EW" will be
        structurally correct** (the two are symmetric), but a
        consumer that assumes the **pupil findings** of a right EW
        lesion are the **same** as a right optic nerve lesion, a
        right CN III fascicular lesion, or a right MLF lesion is
        **wrong** — each produces a **distinct** pattern.

**The right Edinger-Westphal nucleus is a strict mirror pair with the
left EW — no coupling warning, no SLEA warning, no
amygdala-lateralization warning, and no rhinencephalon-exclusion
flag** — **but with a crucial caveat**: the **consensual pupillary
light reflex** is **pretectal**, not EW-EW, and the **clinical
patterns** of right EW lesions, right optic nerve lesions, right
CN III fascicular lesions, and right MLF lesions are **distinct**.
The "strict mirror" is structural, not clinical.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only — **no** import
    from ``.../left/edinger_westphal_nucleus/``.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../forebrain/diencephalon/pretectal_nuclei/``,
    ``.../tectum/right/superior_colliculus/``,
    ``.../cerebral_peduncle/right/crus_cerebri/``, the **ciliary
    ganglion**, the **CN III nerve**, the **MLF**, the **riMLF**,
    the **interstitial nucleus of Cajal**, the **EWcp**, or any other
    container. The right EW's relationships to the right oculomotor
    nucleus, the right trochlear nucleus, the pretectal nuclei, the
    ciliary ganglion, the CN III nerve and fascicles, the MLF, the
    right superior colliculus, the riMLF, the interstitial nucleus of
    Cajal, the EWcp, and the left EW are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **cholinergic
    phenotype** (ChAT, ACh synthesis, nicotinic and muscarinic
    receptors) is a ``chemicals_hormones``-layer fact — documented as
    **prose**, **never imported**. **CHEMICALS-LAYER DISCIPLINE** is
    preserved — the cholinergic phenotype is **not** structural.
*   **DUAL-PARENT LEAF — CROSS-LISTED between
    ``cranial_nerve_nuclei/right/`` and ``tegmentum/right/``.** Both
    paths resolve to **this module**. The right-side counterpart of
    the left leaf's dual-parent anchor.
*   **CROSS-LISTING via ``AREA_PATHS``.** The leaf is cross-listed
    between the functional container (``cranial_nerve_nuclei/``) and
    the topographic container (``tegmentum/``). Consumers resolving
    by **either** path get **this module**.
*   **CONSISTENT with the ``cranial_nerve_nuclei/``,
    ``cranial_nerve_nuclei/right/``, and ``midbrain`` container child
    lists.** The CN nuclei are placed under ``tegmentum/``
    (topographic home) **and** cross-listed under
    ``cranial_nerve_nuclei/`` (functional grouping). This leaf is
    the **right-side EW** slice of that cross-listing.
*   **EWpg — NOT EWcp.** This leaf is the **preganglionic
    parasympathetic** EW. The **EWcp** (centrally projecting,
    urocortin-1⁺) is a **distinct population**, **NOT a CN III
    nucleus**, **NOT** cross-listed here. If the tree included the
    EWcp, it would be a ``.../tegmentum/right/`` leaf **only**.
*   **PREGANGGLIONIC PARASYMPATHETIC NUCLEUS — NOT a somatic motor
    nucleus, NOT a sensory nucleus, NOT an oscillator, NOT a premotor
    pool, NOT a conduction pathway.** It is a **motor nucleus** in
    the family's taxonomy.
*   **NO coupling warning — motor nuclei carry NO coupling warning.**
    Same rule as CN III, CN IV, premotor pools, sensor nuclei, and
    conduction pathways. Coordination with the contralateral EW is
    **pretectal**, **not** EW-EW.
*   **CHEMICALS-LAYER DISCIPLINE.** The **cholinergic phenotype** is
    a ``chemicals_hormones``-layer fact — documented as **prose**,
    **never imported**.
*   **CN NUCLEUS — NOT a CN nerve, NOT a CN fascicle, NOT the ciliary
    ganglion, NOT the MLF, NOT the pretectal nucleus, NOT the
    superior colliculus, NOT a gaze center.**
*   **SIDE-CONSISTENT — this leaf is the RIGHT EW.**
*   **MIRROR PARITY with ``.../left/edinger_westphal_nucleus/`` —
    strict mirror with NO warning** — but the **consensual reflex**
    is **pretectal**, **not** EW-EW, and the **clinical patterns**
    of right EW, right optic nerve, right CN III fascicular, and
    right MLF lesions are **distinct**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum/right`` ↔
    ``cranial_nerve_nuclei/right``) — not into the forebrain,
    hindbrain, or periphery. The **pretectal nucleus** and the
    **ciliary ganglion** are **separate structures** referenced as
    **prose**, not as cross-listed parents.
*   **No nested cross-listing.** This is a **single dual-parent
    leaf**. It is **not** a container.
*   **The on-disk tree is authoritative.**

Usage
-----
Resolve the leaf by **either** path (they are equivalent — **this is
the right-side dual-parent anchor**)::

    # Functional path (clinician framing):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei.right import edinger_westphal_nucleus

    # Topographic path (anatomist framing):
    from infrastructure.brainparts.midbrain.tegmentum.right import edinger_westphal_nucleus

Or by fully-qualified path string::

    functional_path = (
        "midbrain.cranial_nerve_nuclei.right.edinger_westphal_nucleus"
    )
    topographic_path = (
        "midbrain.tegmentum.right.edinger_westphal_nucleus"
    )
    # Both resolve to THIS module.

**Do not** assume the two paths lead to **different structures** —
they lead to **one leaf**, **dual-parented**. This leaf is the
**right-side** instance of the dual-parent anchor.

**Do not** assume the right Edinger-Westphal nucleus is the **EWcp**
(centrally projecting, urocortin-1⁺). This leaf is the **EWpg** —
the **preganglionic parasympathetic** EW, the **CN IIIp nucleus**.

**Do not** assume the right Edinger-Westphal nucleus is the **right
oculomotor nucleus**. The **oculomotor nucleus** is **CN III
somatic motor** (extraocular muscles, levator palpebrae); the **EW**
is **CN III preganglionic parasympathetic** (pupil, lens).

**Do not** assume the right Edinger-Westphal nucleus is the **right
trochlear nucleus**. The **trochlear nucleus** is **CN IV** — a
different cranial nerve.

**Do not** assume the right Edinger-Westphal nucleus is the **right
pretectal nucleus**. The **pretectal nucleus** is **diencephalon** —
the **afferent** relay of the pupillary light reflex, projecting
**bilaterally** to **both** EW nuclei. The **pretectal nucleus** is
**upstream** of EW.

**Do not** assume the right Edinger-Westphal nucleus is the **right
ciliary ganglion**. The **ciliary ganglion** is **peripheral** — the
**postganglionic** relay. It is **downstream** of EW.

**Do not** conflate the right Edinger-Westphal nucleus with the **CN
III nerve** or the **CN III fascicles**. The **nerve** is
**peripheral**; the **fascicles** are **fibers traversing the crus
cerebri**. The EW **axons** travel in them, but the **nucleus** is
**not** the **nerve** and **not** the **fascicle**. A **Weber
syndrome** lesion is a **fascicular** lesion — it **involves** EW
fibers (producing mydriasis), but the **lesion site** is the
**fascicle**, not the EW nucleus.

**Do not** conflate the right Edinger-Westphal nucleus with the **right
MLF**. The **MLF** is a **conduction pathway**. A **right MLF
lesion** produces **right internuclear ophthalmoplegia (INO)** — **NOT
a right EW lesion** and **NOT a right CN III palsy**. The **pupils are
typically spared** in INO.

**Do not** conflate the right Edinger-Westphal nucleus with the **right
superior colliculus**. The **superior colliculus** is **tectum** —
the **visual/oculomotor orienting** structure. It **drives the CN
III nuclei for saccades** via the tectobulbar tract, but it does
**NOT** mediate the **pupillary light reflex** — that is the
**pretectal nucleus**.

**Do not** conflate the right Edinger-Westphal nucleus with the **right
riMLF** or the **right interstitial nucleus of Cajal**. Those are
**vertical gaze centers** — **premotor saccade generators** — **not
CN nuclei**.

**Do not** import the **cholinergic phenotype** into the midbrain
structural layer. The **cholinergic phenotype** (ChAT, ACh synthesis,
nicotinic and muscarinic receptors) is a
**``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the right
Edinger-Westphal nucleus. **Motor nuclei carry NO coupling warning**
— same rule as CN III, CN IV, premotor pools, sensor nuclei, and
conduction pathways. **The consensual pupillary light reflex is
pretectal, not EW-EW coupling.**

Iterating the right Edinger-Westphal nucleus's (empty) children
(recommended consumer pattern)::

    EDINGER_WESTPHAL_NUCLEUS_RIGHT_CHILDREN = ()
    # The right Edinger-Westphal nucleus is a leaf. The cholinergic
    # phenotype (ChAT, ACh synthesis, nicotinic and muscarinic
    # receptors) is a chemicals_hormones-layer fact — documented as
    # prose, not as modules.

Reaching the **functional parent** (``cranial_nerve_nuclei/right/``)::

    # The functional parent is the right side container of the
    # cranial_nerve_nuclei functional grouping:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right
    #
    # The right EW is a child of BOTH the functional parent and the
    # topographic parent (see below).

Reaching the **topographic parent** (``tegmentum/right/``)::

    # The topographic parent is the right side container of the
    # tegmentum topographic container — the SUPERSET:
    #
    #   brainparts.midbrain.tegmentum.right
    #
    # The right EW is a child of BOTH the topographic parent and the
    # functional parent (see above).

Reaching the right oculomotor nucleus (recommended consumer pattern —
the CN III somatic nucleus)::

    # The right oculomotor nucleus is the CN III SOMATIC MOTOR
    # nucleus — extraocular muscles and levator palpebrae:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.right.oculomotor_nucleus
    #
    # The right oculomotor nucleus is SOMATIC MOTOR; the right EW is
    # PREGANGLIONIC PARASYMPATHETIC. They are DIFFERENT NUCLEI in
    # close proximity.

Reaching the right trochlear nucleus (recommended consumer pattern —
the CN IV nucleus)::

    # The right trochlear nucleus is the CN IV SOMATIC MOTOR nucleus
    # — superior oblique (the LEFT superior oblique, because the
    # right trochlear nucleus decussates):
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right.trochlear_nucleus
    #   OR: brainparts.midbrain.tegmentum.right.trochlear_nucleus
    #
    # The right trochlear nucleus is a DIFFERENT CRANIAL NERVE (CN IV)
    # than the right EW (CN IIIp).

Reaching the pretectal nuclei (recommended consumer pattern — the
AFFERENT relay, DIENCEPHALON)::

    # The pretectal nuclei — the olivary pretectal nucleus and the
    # nucleus of the optic tract — are DIENCEPHALON. They receive
    # retinal input and PROJECT BILATERALLY to both EW nuclei. The
    # BILATERAL projection is the mechanism of the CONSENSUAL
    # pupillary light reflex:
    #
    #   brainparts.forebrain.diencephalon.pretectal_nuclei
    #
    # The pretectal nuclei are UPSTREAM of EW; they are DIFFERENT
    # STRUCTURES across a lobe boundary (diencephalon -> midbrain).

Reaching the ciliary ganglion (recommended consumer pattern — the
POSTGANGLIONIC relay, PERIPHERAL)::

    # The ciliary ganglion is PERIPHERAL — it contains the
    # POSTGANGLIONIC parasympathetic neuron cell bodies that
    # innervate the sphincter pupillae and the ciliary muscle:
    #
    #   peripheral.ciliary_ganglion
    #
    # The ciliary ganglion is DOWNSTREAM of EW; it is a DIFFERENT
    # STRUCTURE across the CNS-PNS boundary.

Reaching the CN III nerve (recommended consumer pattern — the
PERIPHERAL bundle)::

    # The CN III nerve is the PERIPHERAL axon bundle — NOT a midbrain
    # structure:
    #
    #   peripheral.cranial_nerves.oculomotor
    #
    # The right EW axons travel IN the CN III nerve, but the nerve is
    # NOT the nucleus.

Reaching the right CN III fascicles (recommended consumer pattern —
the FIBERS traversing the crus cerebri)::

    # The right CN III fascicles traverse the right crus cerebri (the
    # right cerebral peduncle) en route to the interpeduncular fossa.
    # A lesion here (e.g., WEBER SYNDROME) DOES involve EW fibers,
    # producing right mydriasis, but the lesion site is the FASCICLE,
    # not the EW nucleus:
    #
    #   brainparts.midbrain.cerebral_peduncle.right.crus_cerebri
    #
    # The EW nucleus and the CN III fascicles are DIFFERENT
    # STRUCTURES — nucleus vs. fibers.

Reaching the MLF (recommended consumer pattern — the CONDUCTION
PATHWAY, NOT a CN nucleus)::

    # The MLF is a CONDUCTION PATHWAY — a longitudinal fiber tract —
    # that coordinates the CN III, CN IV, and CN VI nuclei for
    # conjugate gaze:
    #
    #   brainparts.hindbrain.myelencephalon.medulla_oblongata...
    #   medial_longitudinal_fasciculus
    #
    # A right MLF lesion produces RIGHT INTERNUCLEAR OPHTHALMOPLEGIA
    # (INO) — NOT a right EW lesion and NOT a right CN III palsy.

Reaching the right superior colliculus (recommended consumer pattern —
the SACCADE generator, NOT the pupillary light reflex)::

    # The right superior colliculus is a TECTUM structure — the
    # visual/oculomotor orienting structure that drives the CN III
    # nuclei for SACCADES (via the tectobulbar tract):
    #
    #   brainparts.midbrain.tectum.right.superior_colliculus
    #
    # The superior colliculus does NOT drive the PUPILLARY LIGHT
    # REFLEX — that is the PRETECTAL nucleus.

Reaching the right riMLF and the right interstitial nucleus of Cajal
(recommended consumer pattern — the GAZE CENTERS, NOT CN nuclei)::

    # The right riMLF and the right interstitial nucleus of Cajal are
    # VERTICAL GAZE CENTERS — premotor saccade generators — NOT CN
    # nuclei:
    #
    #   brainparts.midbrain.tegmentum.right.riMLF
    #   brainparts.midbrain.tegmentum.right.interstitial_nucleus_of_cajal
    #
    # They are tegmentum leaves but are NOT cross-listed under
    # cranial_nerve_nuclei.

Reaching the EWcp (recommended consumer pattern — the CENTRALLY
PROJECTING EW, NOT this leaf)::

    # The EWcp (centrally projecting, urocortin-1+) is a DISTINCT
    # POPULATION — NOT a CN III nucleus — involved in stress,
    # feeding, alcohol, and pain. If the tree includes it, it is a
    # tegmentum leaf ONLY (NOT a cranial_nerve_nuclei leaf):
    #
    #   brainparts.midbrain.tegmentum.right.ewcp   (if present)
    #
    # The right EW (this leaf) is EWpg — the PREGANGLIONIC
    # PARASYMPATHETIC EW. The EWcp is OUT OF SCOPE for the
    # cranial_nerve_nuclei container.

Reaching the left Edinger-Westphal nucleus (recommended consumer
pattern — the SIDE mirror; NOTE the consensual reflex is PRETECTAL,
not EW-EW)::

    # The left Edinger-Westphal nucleus is the LEFT EWpg:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.edinger_westphal_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.edinger_westphal_nucleus
    #
    # The two EW nuclei are STRICTLY SYMMETRIC and INDEPENDENT. The
    # CONSENSUAL pupillary light reflex is mediated by the
    # PRETECTAL nucleus's BILATERAL projection — NOT by EW-EW
    # coupling.

Bilateral iteration (recommended consumer pattern — NOTE the
no-coupling-warning rule and the pretectal consensual mechanism)::

    for side in ("left", "right"):
        for nucleus in (
            "oculomotor_nucleus",
            "trochlear_nucleus",
            "mesencephalic_trigeminal_nucleus",
            "edinger_westphal_nucleus",
        ):
            # Either path resolves to the same leaf — use ONE:
            path = (
                f"midbrain.cranial_nerve_nuclei.{side}.{nucleus}"
            )
            # OR:
            # path = f"midbrain.tegmentum.{side}.{nucleus}"
            #
            # resolve path through the memory/recall layer
            #
            # NOTE: the CN nuclei are MOTOR NUCLEI (CN III, CN IV),
            # a SENSORY NUCLEUS (CN Vm), and a PREGANGLIONIC
            # PARASYMPATHETIC NUCLEUS (Edinger-Westphal). NONE
            # carries a coupling warning. Coordination with the
            # contralateral side is via descending pathways (MLF,
            # posterior commissure) or via upstream bilateral
            # projections (pretectal for the pupillary light
            # reflex), not intrinsic nucleus-to-nucleus coupling.

Pupillary-light-reflex detail (not wired — consult references)::

    # The pupillary light reflex arc — the EW is the EFFERENT limb:
    #
    #   light -> retina -> optic nerve -> optic chiasm -> optic
    #   tract -> PRETECTAL NUCLEUS (diencephalon) -> BILATERAL
    #   projection to LEFT and RIGHT EW nuclei (midbrain) ->
    #   LEFT and RIGHT ciliary ganglia (peripheral) -> LEFT and
    #   RIGHT sphincter pupillae (peripheral) -> both pupils
    #   constrict
    #
    # The BILATERAL projection from the pretectal nucleus to BOTH
    # EW nuclei is the mechanism of the CONSENSUAL reflex. The two
    # EWs are NOT directly coupled.
    #
    # Do not attempt to resolve the pretectal nucleus, the ciliary
    # ganglion, or the sphincter pupillae as sub-paths of the EW
    # nucleus — they are DIFFERENT structures, and the EW is ONLY
    # the efferent midbrain limb.

Near-triad detail (not wired — consult references)::

    # The near triad — the EW contributes the ACCOMMODATION and
    # MIOSIS components:
    #
    #   convergence  -> CN III SOMATIC (medial rectus, oculomotor
    #                   nucleus) — NOT EW
    #   accommodation -> EW -> ciliary ganglion -> ciliary muscle
    #                    -> lens thickens
    #   miosis       -> EW -> ciliary ganglion -> sphincter
    #                    pupillae -> pupil constricts
    #
    # The right EW does NOT control right CONVERGENCE — that is the
    # right oculomotor nucleus.
    #
    # Do not attempt to resolve the convergence pathway or the
    # ciliary muscle as sub-paths of the EW nucleus.

Clinical-pattern detail (not wired — consult references)::

    # The right EW is the EFFERENT midbrain limb of the pupillary
    # light reflex and of the near-triad miosis/accommodation. The
    # CLINICAL PATTERNS of the related lesions are DISTINCT:
    #
    #   right optic nerve lesion  -> right direct lost, right
    #                                 consensual PRESERVED (left
    #                                 pretectal -> both EWs)
    #   right EW nuclear lesion   -> right direct AND right consensual
    #                                 lost, right accommodation lost,
    #                                 extraocular muscles SPARED
    #                                 (oculomotor nucleus spared),
    #                                 RARE in practice
    #   right CN III fascicular   -> right CN III palsy INCLUDING
    #     lesion (Weber syndrome)     mydriasis (EW fibers involved)
    #                                 PLUS left hemiplegia; lesion
    #                                 SITE is the crus cerebri, not
    #                                 the EW nucleus
    #   right MLF lesion          -> right INTERNUCLEAR
    #                                 OPHTHALMOPLEGIA (INO) —
    #                                 adduction weakness of right
    #                                 eye, abducting nystagmus of
    #                                 left eye, PUPILS SPARED
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # STRUCTURES.

References
----------
*   **Classic EW anatomy:** Warwick, R. (1954). "The ocular
    parasympathetic outflow." *Journal of Comparative Neurology*
    101:653–685. (The classic description of the EW nucleus and its
    parasympathetic outflow to the ciliary ganglion.)
*   **EWpg / EWcp distinction:** Horn, A.K.E., Eberhorn, A.C.,
    Büttner-Ennever, J.A. (2008). "Peripheral and central
    oculomotor systems." In *The Senses: A Comprehensive Reference*
    (Masland & Albright, eds.). (The modern distinction between
    EWpg — the preganglionic parasympathetic EW — and EWcp — the
    centrally projecting urocortin-1⁺ EW.)
*   **EWcp and urocortin-1:** Kozicz, T., Bittencourt, J.C., May,
    P.J., Reiner, A., Gamlin, P.D.R., Palkovits, M., Horn, A.K.E.
    (2011). "The Edinger-Westphal nucleus: a historical,
    structural, and functional appraisal of the urocortin-1
    containing centrally projecting neuron population, and its
    comparison to the parasympathetic and preganglionic neurons
    of the oculomotor nucleus." *Brain Structure and Function*
    216:1–19. (The definitive modern review distinguishing EWpg
    from EWcp; the centrally projecting urocortin-1⁺ population
    and its roles in stress, feeding, alcohol, and pain.)
*   **Pupillary light reflex — modern review:** Wilhelm, H. (2011).
    "Disorders of the pupil." *Handbook of Clinical Neurology*
    102:427–466. (The pupillary light reflex pathway — retina →
    optic nerve → pretectal nucleus → EW → ciliary ganglion →
    sphincter pupillae; the clinical syndromes.)
*   **Pupillary light reflex — pretectal relay:** Gamlin, P.D.R.
    (2002). "The pupillary light reflex and its brainstem
    pathways." In *Neuro-Ophthalmology* (Miller et al., eds.).
    (The pretectal nucleus as the afferent relay, projecting
    bilaterally to both EW nuclei — the mechanism of the
    consensual reflex.)
*   **Near triad and accommodation:** Judge, S.J. (2005).
    "Neural control of the near response." In *Neuro-Ophthalmology*
    (Miller et al., eds.). (The near triad — convergence, via the
    oculomotor nucleus; accommodation and miosis, via EW; the
    cortical and pretectal control.)
*   **Pupil-involving CN III palsy and posterior communicating
    artery aneurysm:** Trobe, J.D. (2012). *The Neurology of
    Vision*, 5th ed. (The pupil-involving CN III palsy — the
    superficial pupillomotor fibers vulnerable to compression;
    the pupil-sparing microvascular CN III palsy.)
*   **Argyll Robertson pupil:** Thompson, H.S., Pilley, S.F.J.
    (1998). "Unequal pupils. A flow chart for sorting out the
    anisocorias." *Survey of Ophthalmology* 43:263–269. (The
    light-near dissociation of the Argyll Robertson pupil — the
    historical lesion debate, and the modern view that it is not
    a pure EW nuclear lesion.)
*   **Adie's tonic pupil and the ciliary ganglion:** Holmes, G.
    (1931). "Partial iridoplegia associated with symptoms of
    other disease of the nervous system." *Proceedings of the
    Royal Society of Medicine* 24:209–228. (Adie's tonic pupil as
    a ciliary ganglion / postganglionic lesion — NOT an EW
    nuclear lesion.)
*   **INO and the MLF:** Frohman, T.C., Galetta, S.L., Fox, R.J.,
    Solomon, D., Straumann, D., Filippi, M., Zee, D.S., Frohman,
    E.M. (2008). "Pearls & Oy-sters: The medial longitudinal
    fasciculus in ocular motor physiology." *Neurology*
    70:e57–e67. (The MLF as the internuclear pathway coordinating
    CN III, IV, VI for conjugate gaze; INO as the MLF lesion
    syndrome — distinct from CN III or IV nuclear palsy; pupils
    typically spared in INO.)
*   **Weber syndrome (cross-reference — NOT this leaf):** Weber,
    H.D. (1856). "A contribution to the pathology of the crura
    cerebri." *Medico-Chirurgical Transactions* 39:121–140. (The
    original description of alternating oculomotor hemiplegia —
    the CN III fascicular lesion in the crus cerebri, involving
    EW fibers clinically but NOT an EW nuclear lesion.)
*   **Parinaud syndrome (contrast — dorsal midbrain, NOT this
    leaf):** Parinaud, H. (1883). "Paralysie des mouvements
    associés des yeux." *Annales d'Oculistique* 90:1–21.
    (Parinaud syndrome — superior colliculus / pretectum — NOT
    an EW nuclear lesion.)
*   **Pretectal nuclei (contrast — diencephalon):** Klooster, J.,
    Vrensen, G.F.J.M. (1997). "The pretectal complex of the
    rabbit: a cytoarchitectonic and hodological study."
    *Neuroscience* 76:1233–1254. (The pretectal nuclei as the
    diencephalon relay of the pupillary light reflex, projecting
    bilaterally to both EW nuclei.)
*   **Superior colliculus (contrast — tectum):** Sparks, D.L.
    (2002). "The brainstem control of saccadic eye movements."
    *Nature Reviews Neuroscience* 3:952–964. (The superior
    colliculus driving the CN III nuclei for saccades — NOT for
    the pupillary light reflex.)
*   **Cholinergic phenotype (chemicals_hormones-layer fact —
    contrast):** Woolf, N.J. (1991). "Cholinergic systems in
    mammalian brain and spinal cord." *Progress in Neurobiology*
    37:475–524. (The cholinergic phenotype — ChAT, ACh synthesis,
    nicotinic and muscarinic receptors — as a chemicals-layer
    fact documented in the EW leaf, never imported into the
    midbrain structural layer.)
*   **SLEA (contrast — the right EW is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the EW nucleus.)
*   NeuroNames — Edinger-Westphal nucleus (right); FMA —
    Edinger-Westphal nucleus (right member).
"""