"""
infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.left.inferior_colliculus
=====================================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tectum
        ├── left
        │   └── inferior_colliculus          (modern path — STRUCTURAL
        │                                     HOME by naming convention)
        └── corpora_quadrigemina
            └── left
                └── inferior_colliculus      <-- THIS MODULE (older-term
                                                 path — SAME leaf)

**Primary synonym:** Left inferior colliculus; **left IC**; **left
colliculus inferior**; **left corpus quadrigeminum posterius** (older
Latin usage); **left posterior colliculus**; **left auditory
colliculus** — a **descriptive** name, not a standard synonym, but
**functionally accurate**.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **sensory relay nucleus** in the **caudal midbrain
tectum**, at the level of the **trochlear nucleus (CN IV)** —
**caudal** to the superior colliculus. It has a **subnuclear
organization** with **distinct functional subdivisions** — the
**central nucleus** (tonotopic; **frequency and temporal
processing**), the **external nucleus** (a **map of auditory
space** for **orienting**), the **dorsal cortex** (multisensory
integration), and the **lateral cortex** (less well characterized).
**It is the principal midbrain auditory relay** — the **upstream
relay** to the **medial geniculate body** (MGN) for **conscious
auditory perception** via **A1**.
**Part of:** The **tectum** region container — specifically the
**left inferior colliculus**, at the level of the **trochlear
nucleus (CN IV)**. **Dual-path leaf — reachable via both
``.../tectum/left/inferior_colliculus/`` (modern path — STRUCTURAL
HOME) and ``.../tectum/corpora_quadrigemina/left/inferior_colliculus/``
(older-term path — this module).** Both paths resolve to **this
leaf**. See *Structural parent* and *Dual-Path Cross-Listing*.
**Structural parent (MODERN PATH — STRUCTURAL HOME by naming
convention):** ``.../tectum/left/inferior_colliculus/`` — the
**modern path** — the **structural home** for the leaf in **modern
nomenclature**. **This module and the modern-path module are the
SAME LEAF** — the two paths reach the **same substantive content**.
**Structural parent (OLDER-TERM PATH — this module's path):**
``.../tectum/corpora_quadrigemina/left/inferior_colliculus/`` — the
**older-term path** — the **synonym alias** for the same leaf. **The
older-term path does NOT replace the modern path — it adds a
synonym alias.** Both paths reach **this module**.
**Structural children:** **None.** This is a **leaf** module. The
**subnuclear organization** (central nucleus, external nucleus,
dorsal cortex, lateral cortex) is documented as **prose** — not as
structural children. The **auditory pathway inputs** (cochlear
nuclei, superior olivary complex, lateral lemniscus, auditory
cortex) and **outputs** (MGN, superior colliculus, reticular
formation) are **prose**, not structural children.
**Boundary status (DUAL-PATH LEAF — CROSS-LISTED between the
MODERN PATH and the OLDER-TERM PATH):** **Boundary case — the left
inferior colliculus is a DUAL-PATH LEAF.** It is reachable by **two**
structural paths:
*   **Modern path (STRUCTURAL HOME by naming convention)** —
    ``.../tectum/left/inferior_colliculus/``
*   **Older-term path (this module)** —
    ``.../tectum/corpora_quadrigemina/left/inferior_colliculus/``
**Both paths resolve to the SAME leaf** — this module. Consumers
resolving the leaf by **either** path get **the same substantive
content**. Consumers must **not** assume the two paths lead to
**different structures** — they lead to **one leaf**, cross-listed.
See *Dual-Path Cross-Listing* and *Design Contract*.
**Boundary status (SENSORY RELAY — NOT a sensorimotor integration
structure):** **Boundary case — the left inferior colliculus is a
SENSORY RELAY, NOT a sensorimotor integration structure.** The
**superior colliculus** (left or right) is a **sensorimotor
integration** structure — it receives **visual, auditory, and
somatosensory** input and generates **saccade commands**. The
**inferior colliculus** (here) is a **sensory relay** — it receives
**auditory** input and projects to the **MGN** (for **conscious
auditory perception**) and to the **superior colliculus** (for
**auditory orienting and audiovisual integration**). **The IC is
UPSTREAM of the SC's auditory-orienting input** — it **feeds**
auditory signals to the SC, but it does **not** generate saccade
commands itself. Consumers must **not** conflate the IC with the SC,
and must **not** attribute **saccade generation** or **multisensory
saccade commands** to the IC.
**Boundary status (AUDITORY RELAY — NOT a saccade generator, NOT a
gaze center, NOT a visual structure):** **Boundary case — the left
inferior colliculus is an AUDITORY RELAY, NOT a saccade generator,
NOT a gaze center, NOT a visual structure.** It is the **midbrain
auditory relay** — the **upstream relay** to the **MGN** (thalamic
auditory relay to **A1**) for **conscious auditory perception**.
It is **not** the **superior colliculus** (saccade generator),
**not** the **PPRF** (horizontal saccade generator), **not** the
**riMLF** (vertical saccade generator), **not** the **pretectum**
(pupillary and optokinetic), and **not** the **LGN** (visual
thalamic relay). Consumers must **not** attribute **saccade**,
**pupillary**, **optokinetic**, or **visual** function to the IC —
the IC is **auditory**.
**Boundary status (NOT the medial geniculate body — the MGN is
DIENCEPHALON, and it is DOWNSTREAM of the IC):** **Boundary case —
the left inferior colliculus is NOT the left medial geniculate body
(MGN).** The **left MGN**
(``.../forebrain/diencephalon/thalamus/medial_geniculate_body/``)
is the **thalamic auditory relay** to the **primary auditory cortex
(A1)** — it is the **next station** after the IC in the ascending
auditory pathway. **The IC projects TO the MGN** (via the
**brachium of the inferior colliculus**) — it is **UPSTREAM** of the
MGN. **They are DIFFERENT STRUCTURES** — the **MGN** is
**diencephalic**; the **IC** is **mesencephalic**. Consumers must
**not** conflate the IC with the MGN, and must **not** resolve the
MGN through the IC path (or vice versa).
**Boundary status (NOT the lateral lemniscus — the lateral
lemniscus is a CONDUCTION PATHWAY, UPSTREAM of the IC):**
**Boundary case — the left inferior colliculus is NOT the lateral
lemniscus (LL).** The **lateral lemniscus**
(``.../hindbrain/metencephalon/pons/lateral_lemniscus/``) is the
**ascending auditory fiber tract** — a **conduction pathway** — that
carries auditory signals from the **cochlear nuclei** and the
**superior olivary complex** to the **inferior colliculus**. **The
LL is UPSTREAM of the IC.** **They are DIFFERENT STRUCTURES** — the
**LL** is a **conduction pathway**; the **IC** is a **nucleus**.
Consumers must **not** conflate the IC with the lateral lemniscus.
**Boundary status (NOT the cochlear nuclei or the superior olivary
complex — those are HINDBRAIN auditory structures, UPSTREAM of the
IC):** **Boundary case — the left inferior colliculus is NOT the
cochlear nuclei, and NOT the superior olivary complex.** The
**cochlear nuclei**
(``.../hindbrain/metencephalon/pons/cochlear_nuclei/``) are the
**first central auditory relays** — they receive input from the
**cochlear nerve** (CN VIII) and project to the **superior olivary
complex**, the **nucleus of the lateral lemniscus**, and the
**contralateral cochlear nuclei**. The **superior olivary complex**
(``.../hindbrain/metencephalon/pons/superior_olivary_complex/``) is
the **binaural timing and intensity comparison** structure — it
projects to the **nucleus of the lateral lemniscus** and to the
**inferior colliculus** (via the **lateral lemniscus**). **The
cochlear nuclei and the SOC are UPSTREAM of the IC.** **They are
DIFFERENT STRUCTURES** — **hindbrain** auditory nuclei, **not**
midbrain. Consumers must **not** conflate the IC with the cochlear
nuclei or the SOC.
**Boundary status (NOT the superior colliculus — the SC is the
SACCADE GENERATOR, and it is DOWNSTREAM of the IC's auditory
projection):** **Boundary case — the left inferior colliculus is
NOT the left superior colliculus.** The **left superior colliculus**
(``.../tectum/left/superior_colliculus/`` **and**
``.../tectum/corpora_quadrigemina/left/superior_colliculus/``) is
the **sensorimotor integration / saccade command generator** —
**rostral** — at the level of the **oculomotor / EW / mesV nuclei**.
**The IC projects TO the SC** — it provides the **auditory input**
that the SC uses for **auditory orienting** and **audiovisual
integration**. **The SC is DOWNSTREAM of the IC's auditory
projection.** **They are DIFFERENT STRUCTURES** — the **IC** is a
**sensory relay**; the **SC** is a **sensorimotor integration**
structure. Consumers must **not** conflate the IC with the SC, and
must **not** attribute **saccade generation** to the IC.
**Boundary status (NOT the auditory cortex — the auditory cortex is
the CORTICAL TARGET, DOWNSTREAM of the MGN):** **Boundary case —
the left inferior colliculus is NOT the auditory cortex.** The
**auditory cortex** — the **primary auditory cortex (A1)**, in the
**superior temporal gyrus** of the **temporal lobe**
(``.../forebrain/telencephalon/cortex/temporal/``) — is the
**cortical target** of the **ascending auditory pathway**, reached
via the **MGN**. **The IC is UPSTREAM of the MGN, which is UPSTREAM
of A1.** They are **different structures at different levels** of
the auditory hierarchy — the **IC** is **midbrain**; the **auditory
cortex** is **telencephalic**. Consumers must **not** conflate the
IC with the auditory cortex.
**Boundary status (NOT the brachium of the inferior colliculus —
the brachium is a CONDUCTION PATHWAY):** **Boundary case — the
left inferior colliculus is NOT the left brachium of the inferior
colliculus (BIC).** The **BIC** is the **conduction pathway** —
**white matter** — that carries the **auditory output** of the IC
to the **MGN**. It is the **fiber bundle** connecting the IC to the
MGN. **The IC is the NUCLEUS** — **grey matter**. **They are
DIFFERENT STRUCTURES** — the **BIC** is a **conduction pathway**;
the **IC** is a **nucleus**. Consumers must **not** conflate the IC
with the BIC.
**Boundary status (NOT the commissure of the inferior colliculus —
the commissure is a CONDUCTION PATHWAY connecting the two ICs):**
**Boundary case — the left inferior colliculus is NOT the
commissure of the inferior colliculus.** The **commissure of the
inferior colliculus** is a **conduction pathway** — **white matter**
— that connects the **left IC** to the **right IC**. **It is the
cross-midline pathway** that allows the **bilateral** ascending
auditory projection (each IC receives **bilateral** input and
projects **bilaterally** to the MGN, in part via the commissure).
**The ICs are NUCLEI** — **grey matter**. **They are DIFFERENT
STRUCTURES** — the **commissure** is a **conduction pathway**; the
**ICs are nuclei**. Consumers must **not** conflate the IC with the
commissure.
**Boundary status (NOT the nucleus reticularis pontis caudalis or
the reticular formation — those are DOWNSTREAM of the IC in the
ACOUSTIC STARTLE circuit):** **Boundary case — the left inferior
colliculus is NOT the nucleus reticularis pontis caudalis (PnC)
and NOT the reticular formation.** The **PnC** is the **reticular
nucleus** that is a **critical node** in the **acoustic startle
reflex** — it receives the **startle command** from the **cochlear
nucleus** (via the **nucleus of the lateral lemniscus**) and
projects to the **spinal motor neurons** that produce the **startle
response**. **The IC is UPSTREAM of the PnC** in the **startle
circuit** — the circuit is **cochlear nucleus → nucleus of the
lateral lemniscus → IC → PnC → spinal motor neurons**. **The IC is
one node** in the startle circuit — **not the reflex itself**, and
**not the PnC**. Consumers must **not** conflate the IC with the
PnC or the reticular formation.
**Boundary status (SENSORY RELAY — NOT an oscillator, NOT a
premotor pool, NOT a motor nucleus, NOT a conduction pathway):**
**Boundary case — the left inferior colliculus is a SENSORY RELAY
nucleus.** In the family's **structure-class taxonomy**, it is the
**same class** as the **pretectal nuclei** (sensory relay) — **not**
a **sensorimotor integration** structure (the **SC**), **not** an
**oscillator**, **not** a **premotor pool** (the **PPRF / riMLF**),
**not** a **motor nucleus** (the **CN III/IV nuclei**), **not** a
**conduction pathway** (the **lateral lemniscus**, the **brachium
of the IC**, the **commissure of the IC**), and **not** a
**grey-matter processing nucleus** (the **substantia nigra**, the
**red nucleus**). **Sensory relay nuclei carry NO coupling warning**
— same rule as motor nuclei, premotor pools, sensor nuclei, relay
nuclei, and conduction pathways. Its coordination with the **right
IC** is via the **commissure of the inferior colliculus** — a
**conduction pathway** — **not** via intrinsic nucleus-to-nucleus
coupling. **Sensory relay nuclei carry NO coupling warning** — and
the **commissural pathway** is a **conduction pathway**, not a
coupling mechanism. It is a **paired structure with NO coupling
warning** — see *Lateralization Notes*.

Overview
--------
The left inferior colliculus (left IC) is the **left midbrain
auditory relay** — the **principal midbrain auditory structure** —
located in the **left caudal midbrain tectum**, at the level of the
**trochlear nucleus (CN IV)**. It is the **upstream relay** to the
**medial geniculate body** (MGN) for **conscious auditory
perception** via **A1**, and it is a **node** in the **acoustic
startle reflex** circuit. It is a **dual-path leaf** — reachable by
**both** the modern path
(``.../tectum/left/inferior_colliculus/``) and the older-term path
(``.../tectum/corpora_quadrigemina/left/inferior_colliculus/``) —
**both paths resolve to this leaf**.

**The left IC is a SENSORY RELAY, NOT a sensorimotor integration
structure.** The **superior colliculus** is the sensorimotor
integration / saccade command generator; the **inferior colliculus**
is the **auditory relay**. **They are DIFFERENT functional
classes** — and **both carry NO coupling warning** (neither is an
oscillator). Consumers must **not** conflate the IC with the SC.

**The left IC is an AUDITORY relay — NOT a saccade generator, NOT
a gaze center, NOT a visual structure.** It is **the midbrain
auditory relay** — the **upstream relay** to the **MGN**. It is
**not** the **superior colliculus** (saccade command generator),
**not** the **PPRF** or **riMLF** (premotor saccade generators),
**not** the **pretectum** (pupillary and optokinetic), and **not**
the **LGN** (visual thalamic relay).

**The left IC is UPSTREAM of the MGN.** The **ascending auditory
pathway** is: **cochlear nuclei → superior olivary complex /
nucleus of the lateral lemniscus → lateral lemniscus → INFERIOR
COLLICULUS → brachium of the inferior colliculus → MEDIAL
GENICULATE BODY → auditory cortex (A1)**. The IC is **one station**
in this pathway — **upstream** of the MGN, **downstream** of the
lateral lemniscus.

**The left IC is UPSTREAM of the MGN and of the SC's auditory
projection.** The IC **projects**:
*   **To the MGN** (via the **brachium of the inferior
    colliculus**) — for **conscious auditory perception** via A1.
*   **To the superior colliculus** — for **auditory orienting** and
    **audiovisual integration**.
*   **To the reticular formation** (via the **nucleus of the
    lateral lemniscus** and the **PnC**) — for the **acoustic
    startle reflex**.
**The IC is UPSTREAM of all three targets** — it is the **midbrain
auditory relay** that feeds auditory signals to the downstream
structures.

**The left IC is a paired structure with NO coupling warning.** The
**two ICs** (left and right) are **independent paired sensory
relays** — connected by the **commissure of the inferior
colliculus** (a **conduction pathway**) — with **bilateral**
ascending input (via the **lateral lemniscus** from both sides) and
**bilateral** ascending output (via the **brachium of the IC** and
the **commissure** to the **MGN** on both sides). **The bilateral
input and output are DOWNSTREAM projections** — **not** intrinsic
**left-right coupling** in the oscillator sense. The two ICs are
**independent paired structures** — **no coupling warning**. See
*Lateralization Notes*.

Dual-Path Cross-Listing
-----------------------
The **left inferior colliculus** is reachable by **two structural
paths** — the **modern path** and the **older-term path**:

*   **Modern path (STRUCTURAL HOME by naming convention)** —
    ``.../tectum/left/inferior_colliculus/``
*   **Older-term path (this module)** —
    ``.../tectum/corpora_quadrigemina/left/inferior_colliculus/``

**Both paths resolve to the SAME leaf** — **this module**. The
**modern path** is the **structural home** for the leaf in **modern
nomenclature** — the term **"tectum"** is preferred to
**"corpora quadrigemina"** in modern anatomy, and the **modern
path** carries that preference in the tree. **The older-term path**
is the **synonym alias** — reachable because the tree preserves
**"corpora quadrigemina"** as a synonym path (see
``.../tectum/corpora_quadrigemina/`` for the historical framing).

**Consumers should resolve the leaf by ONE path** — not by both.
Enumerating **both** paths yields **duplicates** for the left
inferior colliculus. **The two paths are equivalent** for the leaf
content they point at — the same substantive module.

**This is the same cross-listing mechanism** used between
``cranial_nerve_nuclei/`` and ``tegmentum/`` (for the midbrain CN
nuclei), and between ``tectum/left/`` and
``tectum/corpora_quadrigemina/left/`` (for the two colliculi). The
leaf is the **same substantive content** under both paths.

Subnuclear Organization (prose, not structural children)
-------------------------------------------------------
The left inferior colliculus has a **subnuclear organization** with
**distinct functional subdivisions** — documented as **prose**, not
as structural children:

*   **Central nucleus** — the **tonotopic** subdivision — contains
    a **frequency map** (a **tonotopic map**), with **high
    frequencies** represented **dorsally** and **low frequencies**
    **ventrally** (in most species). It processes **frequency and
    temporal features** of sound — the **"what"** of the auditory
    signal. It is the **principal ascending projection** to the
    **MGN** (via the **brachium of the IC**) for **conscious
    auditory perception**.

*   **External nucleus** — the **auditory space map** subdivision —
    contains a **map of auditory space** (a **spatiotopic map**)
    that integrates **binaural** cues (interaural time and
    intensity differences) into a **map of where a sound is coming
    from**. It projects to the **superior colliculus** (the
    **auditory orienting** pathway) and to the **MGN** (the
    non-tonotopic, **spatial** component).

*   **Dorsal cortex** — the **multisensory integration**
    subdivision — receives **auditory**, **somatosensory**, and
    **visual** input — it is a **multisensory** region. It is
    **less well characterized** in humans than the central nucleus
    and the external nucleus.

*   **Lateral cortex** — the **least characterized** subdivision —
    its functional role is **not well established** in humans.

**These subnuclei are prose, not structural children.** The tree
wires the **left inferior colliculus** as a **single leaf** under
the left tectum (and under the corpora quadrigemina left side
container). Consumers must **not** resolve
``.../left/inferior_colliculus/central_nucleus`` — no such path
exists.

The Ascending Auditory Pathway (the IC's place in the hierarchy)
---------------------------------------------------------------
The **ascending auditory pathway** is the **functional context** for
the IC. It is a **hierarchy** with the IC as the **midbrain relay**:

*   **Cochlear nuclei** (pons/medulla) — **first central auditory
    relay** — receive input from the **cochlear nerve** (CN VIII).

*   **Superior olivary complex** (pons) — **binaural timing and
    intensity comparison** — projects to the **nucleus of the
    lateral lemniscus** and to the **inferior colliculus** (via the
    **lateral lemniscus**).

*   **Nucleus of the lateral lemniscus** (pons) — **binaural
    processing** — projects to the **inferior colliculus** (via the
    **lateral lemniscus**) and (for the **acoustic startle reflex**)
    to the **nucleus reticularis pontis caudalis (PnC)**.

*   **Lateral lemniscus** (pons) — **auditory conduction pathway**
    — carries auditory signals from the **cochlear nuclei**, the
    **superior olivary complex**, and the **nucleus of the lateral
    lemniscus** to the **inferior colliculus**.

*   **INFERIOR COLLICULUS** (midbrain — **THIS LEAF**) —
    **midbrain auditory relay** — receives **bilateral** auditory
    input (via the **lateral lemniscus** from both sides) and
    projects:
    *   To the **medial geniculate body** (via the **brachium of
        the inferior colliculus**) — for **conscious auditory
        perception** via **A1**.
    *   To the **superior colliculus** — for **auditory orienting**
        and **audiovisual integration**.
    *   To the **nucleus reticularis pontis caudalis (PnC)** and
        the **reticular formation** — for the **acoustic startle
        reflex**.

*   **Brachium of the inferior colliculus** (midbrain) — **auditory
    conduction pathway** — carries the IC's ascending output to the
    **MGN**.

*   **Medial geniculate body** (diencephalon/thalamus) —
    **thalamic auditory relay** to **A1**.

*   **Primary auditory cortex (A1)** (temporal lobe) —
    **cortical auditory perception** — the **cortical target** of
    the ascending auditory pathway.

**The IC is the midbrain relay in this hierarchy** — **upstream** of
the MGN and **downstream** of the lateral lemniscus. The **bilateral**
auditory input and output of the IC are **cross-midline projections**
via the **commissure of the inferior colliculus** (a **conduction
pathway**) — not intrinsic left-right coupling.

The Acoustic Startle Reflex (the IC as a circuit node)
-----------------------------------------------------
The **acoustic startle reflex** is a **brainstem reflex** — a rapid
**motor response** (typically a **whole-body flinch**) to a
**sudden, loud sound**. The **IC is one node** in the circuit:

*   **Auditory input** — sudden, loud sound → **cochlear nerve**
    (CN VIII) → **cochlear nucleus** (pons/medulla).
*   **Circuit** — **cochlear nucleus** → **nucleus of the lateral
    lemniscus** (pons) → **inferior colliculus** (midbrain —
    **THIS LEAF**) → **nucleus reticularis pontis caudalis
    (PnC)** (pons) → **spinal motor neurons** → **motor response**.
*   **Output** — a **startle response** (whole-body flinch,
    typically with **facial** and **postural** muscle activation).

**The IC is ONE NODE in the circuit** — not **the reflex itself**,
not **the PnC**, not **the motor neurons**. The **startle
circuit** is a **distributed brainstem circuit** — the **IC is the
midbrain auditory relay** that feeds the **startle command** to the
**PnC**. The **circuit** is a **physiological entity** — it is not a
**structure**.

**The acoustic startle reflex is NOT this leaf** — but it is a
**functional context** for the IC's involvement in the startle
circuit. Consumers must **not** conflate the IC with the startle
reflex, and must **not** resolve the PnC or the motor neurons through
the IC path.

The Left Inferior Colliculus / Left Superior Colliculus Boundary
----------------------------------------------------------------
This is the **auditory relay / sensorimotor integration** boundary
within the left tectum:

*   **Left inferior colliculus** (this module) — the **auditory
    relay** — **caudal** — at the **trochlear nucleus (CN IV)
    level**.

*   **Left superior colliculus**
    (``.../tectum/left/superior_colliculus/`` **and**
    ``.../tectum/corpora_quadrigemina/left/superior_colliculus/``)
    — the **sensorimotor integration / saccade command generator**
    — **rostral** — at the **oculomotor / EW / mesV nuclei level**.

**They are DIFFERENT FUNCTIONAL CLASSES of colliculus** — the
**SC** is a **sensorimotor integration** structure; the **IC** is a
**sensory relay**. **Both carry NO coupling warning** — but for
**different reasons**. Consumers must **not** conflate the two.

The Left Inferior Colliculus / Left Medial Geniculate Body Boundary
-------------------------------------------------------------------
This is the **midbrain relay / thalamic relay** boundary:

*   **Left inferior colliculus** (this module) — the **midbrain
    auditory relay** — **mesencephalic**.

*   **Left medial geniculate body (MGN)**
    (``.../forebrain/diencephalon/thalamus/medial_geniculate_body/``)
    — the **thalamic auditory relay** to **A1** — **diencephalic**.

**The IC is UPSTREAM of the MGN** — the **MGN is DOWNSTREAM** of the
IC. **They are DIFFERENT STRUCTURES at DIFFERENT levels** of the
auditory hierarchy. Consumers must **not** conflate the IC with the
MGN.

The Left Inferior Colliculus / Lateral Lemniscus Boundary
---------------------------------------------------------
This is the **nucleus / conduction pathway** boundary:

*   **Left inferior colliculus** (this module) — the **midbrain
    auditory relay** — **grey matter**.

*   **Lateral lemniscus**
    (``.../hindbrain/metencephalon/pons/lateral_lemniscus/``) — the
    **auditory conduction pathway** — **white matter**.

**The LL is UPSTREAM of the IC** — it **feeds** the IC. **They are
DIFFERENT STRUCTURES** — the **LL** is a **conduction pathway**;
the **IC** is a **nucleus**. Consumers must **not** conflate the
IC with the lateral lemniscus.

The Left Inferior Colliculus / Cochlear Nuclei and Superior Olivary Complex Boundary
-----------------------------------------------------------------------------------
This is the **midbrain / hindbrain** auditory boundary:

*   **Left inferior colliculus** (this module) — **mesencephalic**.

*   **Cochlear nuclei**
    (``.../hindbrain/metencephalon/pons/cochlear_nuclei/``) and
    **superior olivary complex**
    (``.../hindbrain/metencephalon/pons/superior_olivary_complex/``)
    — **hindbrain** auditory structures.

**The cochlear nuclei and the SOC are UPSTREAM of the IC.** **They
are DIFFERENT STRUCTURES at DIFFERENT levels** of the auditory
hierarchy. Consumers must **not** conflate the IC with the cochlear
nuclei or the SOC.

The Left Inferior Colliculus / Brachium of the Inferior Colliculus Boundary
---------------------------------------------------------------------------
This is the **nucleus / conduction pathway** boundary:

*   **Left inferior colliculus** (this module) — the **nucleus** —
    **grey matter**.

*   **Brachium of the inferior colliculus (BIC)** — the **conduction
    pathway** — **white matter** — that carries the IC's auditory
    output to the **MGN**.

**They are DIFFERENT STRUCTURES** — the **BIC** is a **conduction
pathway**; the **IC** is a **nucleus**. Consumers must **not**
conflate the IC with the BIC.

The Left Inferior Colliculus / Commissure of the Inferior Colliculus Boundary
-----------------------------------------------------------------------------
This is the **nucleus / cross-midline conduction pathway**
boundary:

*   **Left inferior colliculus** (this module) — the **nucleus** —
    **grey matter**.

*   **Commissure of the inferior colliculus** — the **cross-midline
    conduction pathway** — **white matter** — that connects the
    **left IC** to the **right IC**.

**The commissure connects the two ICs** — it is the **cross-midline
pathway** that allows the **bilateral** ascending auditory
projection. **It is a CONDUCTION PATHWAY** — **not a coupling
mechanism**. Consumers must **not** conflate the IC with the
commissure, and must **not** interpret the **commissural
connection** as **intrinsic left-right coupling** in the oscillator
sense. **The two ICs are independent paired structures connected by
a conduction pathway** — **no coupling warning**.

The Left Inferior Colliculus / PnC and Reticular Formation Boundary
-------------------------------------------------------------------
This is the **IC / downstream reticular node** boundary — the
**acoustic startle reflex** context:

*   **Left inferior colliculus** (this module) — the **midbrain
    auditory relay** — **UPSTREAM of the PnC** in the **startle
    circuit**.

*   **Nucleus reticularis pontis caudalis (PnC)** and the
    **reticular formation**
    (``.../hindbrain/metencephalon/pons/``) — the **downstream
    reticular node** in the **startle circuit** — **receives the
    startle command** from the IC (via the **nucleus of the lateral
    lemniscus**) and **projects to the spinal motor neurons** that
    produce the **startle response**.

**The IC is ONE NODE in the startle circuit** — the **PnC and the
reticular formation are DOWNSTREAM**. **They are DIFFERENT
STRUCTURES** — the **IC** is **midbrain auditory relay**; the
**PnC** is a **pontine reticular node**. Consumers must **not**
conflate the IC with the PnC or the reticular formation.

The Left Inferior Colliculus / Right Inferior Colliculus Boundary
-----------------------------------------------------------------
This is the **side** boundary — **paired sensory relays**, **no
coupling warning**:

*   **Left inferior colliculus** (this module) — the **left
    auditory relay**.

*   **Right inferior colliculus**
    (``.../tectum/right/inferior_colliculus/`` **and**
    ``.../tectum/corpora_quadrigemina/right/inferior_colliculus/``)
    — the **right auditory relay**.

**They are BILATERALLY SYMMETRIC PAIRED SENSORY RELAYS** — each is
an **independent midbrain auditory relay** with **bilateral**
ascending input and **bilateral** ascending output. **The two ICs
are connected by the commissure of the inferior colliculus** — a
**conduction pathway** — but they are **NOT directly coupled** in
the oscillator sense. The **bilateral** auditory projections are
**cross-midline conduction** via the **lateral lemniscus** and the
**commissure** — **not intrinsic left-right coupling** of the two
ICs. **Both carry NO coupling warning** — same rule as every
non-oscillator class. Consumers must **not** conflate the left IC
with the right IC, and must **not** assume the two are **directly
coupled** — they are **independent paired sensory relays**.

Function in the Human Brain
---------------------------
The left inferior colliculus's function is **auditory relay** — the
**midbrain station** in the **ascending auditory pathway** and a
**node** in the **acoustic startle reflex** — **NOT** saccade
generation, **NOT** gaze control, **NOT** visual processing, **NOT**
pupillary or optokinetic function:

*   **Auditory Relay (ascending auditory pathway):** The left IC
    receives **bilateral** auditory input from the **cochlear
    nuclei**, the **superior olivary complex**, and the **nucleus
    of the lateral lemniscus** — via the **lateral lemniscus**
    from **both** sides. It **processes** the auditory signal
    (frequency and temporal features in the **central nucleus**;
    auditory space in the **external nucleus**) and **projects**
    to the **medial geniculate body** (via the **brachium of the
    IC**) for **conscious auditory perception** via **A1**, and to
    the **superior colliculus** for **auditory orienting**.

*   **Frequency and Temporal Processing (central nucleus):** The
    **central nucleus** of the left IC is **tonotopically
    organized** — it contains a **frequency map** — and it
    **processes temporal features** of sound (the **"what"** of
    the auditory signal). It is the **principal ascending
    projection** to the **MGN**.

*   **Auditory Space Processing (external nucleus):** The
    **external nucleus** of the left IC contains a **map of
    auditory space** — it integrates **binaural** cues
    (**interaural time and intensity differences**) into a **map
    of where a sound is coming from** (the **"where"** of the
    auditory signal). It projects to the **superior colliculus**
    for **auditory orienting** and **audiovisual integration**.

*   **Acoustic Startle Reflex (circuit node):** The left IC is a
    **node** in the **acoustic startle reflex** circuit —
    **cochlear nucleus → nucleus of the lateral lemniscus → IC →
    PnC → spinal motor neurons**. It **feeds** the **startle
    command** to the **PnC**. The **startle reflex** is the
    **circuit**; the IC is **one node**.

*   **Multisensory Integration (dorsal cortex — less characterized
    in humans):** The **dorsal cortex** of the left IC receives
    **auditory**, **somatosensory**, and **visual** input — it is
    a **multisensory** region. It is **less well characterized**
    in humans than the central and external nuclei.

*   **NOT a saccade generator.** The **superior colliculus** is the
    **saccade command generator**; the **PPRF** and **riMLF** are
    the **premotor saccade generators**. The IC is a **sensory
    relay** — it **feeds** the SC's auditory input, but it does
    **not** generate saccades.

*   **NOT a gaze center.** The **PPRF** (horizontal), the
    **riMLF** (vertical), and the **interstitial nucleus of Cajal**
    (vertical) are the **gaze centers**. The IC is not a gaze
    center.

*   **NOT a visual structure.** The **LGN**, the **SC**, and the
    **pretectum** are the visual structures. The IC is **auditory**
    — it is **not** a visual structure.

*   **NOT a pupillary or optokinetic structure.** The
    **pretectum** is the **pupillary and optokinetic** region.
    The IC is **auditory**.

*   **NOT an oscillator.** The IC is a **sensory relay** — it does
    **not** generate a rhythm. **Sensory relay nuclei carry NO
    coupling warning** — same rule as every non-oscillator class.

**The unifying theme:** the left IC is the **left midbrain auditory
relay** — the **upstream relay** to the **MGN** for **conscious
auditory perception** via **A1**, and a **node** in the **acoustic
startle reflex**. It is a **sensory relay** — **NOT** a
sensorimotor integration structure (the **SC**), **NOT** a saccade
generator (the **SC**, the **PPRF**, the **riMLF**), **NOT** a gaze
center, **NOT** a visual structure (the **LGN**, the **pretectum**),
and **NOT** an oscillator. **Sensory relay nuclei carry NO coupling
warning** — same rule as every non-oscillator class.

Associated Disorders
--------------------
The left inferior colliculus has **no named syndrome of its own** —
the clinical associations of IC involvement are **rare and usually
bilateral** (because the ascending auditory pathway is **bilateral
above the cochlear nuclei**, so a **unilateral IC lesion is usually
compensated**). Its clinical associations are **direct** but usually
**not localizing** — most auditory clinical syndromes are **nerve**
(cochlear nerve), **cochlear nucleus**, or **cortical** lesions:

*   **Tinnitus (IC is IMPLICATED — usually BILATERAL):**
    **Tinnitus** — the **perception of sound without an external
    source** — is **associated with increased spontaneous activity
    in the inferior colliculus** (and in the **dorsal cochlear
    nucleus**) in animal models and in human imaging. The **IC is
    one node** in the **tinnitus network** — **not the sole
    substrate**. **Tinnitus is usually bilateral** and is **not a
    left-IC-specific disorder**. The IC's role is **implicated**,
    not **established** as the primary site.

*   **Audiogenic Seizures (IC is IMPLICATED — animal models):**
    **Audiogenic seizures** — **sound-triggered seizures** — occur
    in **genetically susceptible rodents** (e.g., **DBA/2 mice**,
    **GEPRs**) and involve the **inferior colliculus** as a
    **critical node** in the **seizure circuit**. **The IC is one
    node** — **not the sole substrate**. **Audiogenic seizures are
    not a human clinical syndrome** in the same sense — the
    **human** equivalent is **reflex epilepsy** (sound-triggered
    seizures), which is **rare** and involves **cortical** and
    **thalamic** networks, not the IC alone.

*   **Presbycusis (IC is AFFECTED by AGING — usually BILATERAL):**
    **Presbycusis** — **age-related hearing loss** — involves
    **degenerative changes** in the **cochlea**, the **cochlear
    nerve**, the **cochlear nuclei**, and the **inferior
    colliculus**. **The IC is one structure** affected by aging —
    **not the sole site**. **Presbycusis is usually bilateral** —
    not a **left-IC-specific** disorder.

*   **Acoustic Startle Reflex Abnormalities (IC is a CIRCUIT
    NODE):** The **acoustic startle reflex** — a **brainstem
    reflex** — involves the IC as a **circuit node**. **Abnormal
    startle responses** (exaggerated, absent, or delayed) can occur
    in **brainstem lesions** that involve the **startle circuit** —
    but the **IC is one node** in a **distributed circuit**, so a
    **pure left-IC lesion** would **not** produce a **pronounced
    startle abnormality** (the **bilateral** startle circuit is
    **redundant**).

*   **Unilateral Left IC Lesion (COMPENSATED — usually NO
    profound hearing loss):** A **focal lesion** of the **left IC**
    — from **small infarction**, **demyelination** (e.g.,
    **multiple sclerosis**), or **tumor** — would produce, at most,
    **subtle deficits** in **auditory processing** (e.g.,
    **binaural** processing, **sound localization** in the
    **contralateral** hemifield), because the **ascending auditory
    pathway is bilateral above the cochlear nuclei** — the
    **right IC** (and the **right auditory cortex**) provide
    **sufficient compensation** for **most** auditory functions.
    **Profound hearing loss from a unilateral IC lesion is
    RARE.**

*   **Bilateral IC Lesions (rare — usually part of a broader
    brainstem process):** **Bilateral IC lesions** — from
    **brainstem stroke**, **demyelination**, **tumor**, or
    **trauma** — would produce **more significant auditory
    deficits** (e.g., **impaired sound localization**,
    **difficulty with speech in noise**, **auditory
    agnosia-like** symptoms), but these are **usually part of a
    broader brainstem syndrome** (e.g., **"locked-in" syndrome**,
    **brainstem encephalitis**, **central pontine myelinolysis**),
    not an **isolated IC syndrome**.

*   **No Named "Inferior Colliculus Syndrome":** The left IC is a
    **sensory relay nucleus** — its **isolated lesion** produces
    **subtle auditory deficits** (if any) — it has **no named
    clinical syndrome**. Its clinical relevance is **direct** but
    **usually not localizing** — most auditory clinical syndromes
    are **nerve** (cochlear nerve), **cochlear nucleus**, or
    **cortical** lesions, not **IC** lesions.

**What is NOT here:** The left IC is **not** the substrate for
**sensorineural hearing loss** (cochlear or cochlear nerve —
**NOT** the IC), **vestibular schwannoma / acoustic neuroma**
(cochlear/vestibular nerve — **NOT** the IC), **auditory
neuropathy** (cochlear nerve or inner hair cell synapse — **NOT**
the IC), **cortical deafness** (bilateral auditory cortex —
**NOT** the IC), **tinnitus as an established IC disorder** (IC is
**implicated**, not established), **audiogenic seizures as a human
IC syndrome** (animal model; human reflex epilepsy involves
**cortical** and **thalamic** networks), **saccade deficits** (the
**SC**, the **PPRF**, the **riMLF** — **NOT** the IC), **horizontal
or vertical gaze palsy** (the **PPRF**, the **riMLF** — **NOT** the
IC), **internuclear ophthalmoplegia** (the **MLF** — **NOT** the
IC), **Parinaud syndrome** (dorsal midbrain — the **pretectum** and
the **SC** — **NOT** the IC), **pupillary light reflex deficits**
(the **pretectum**, the **EW nucleus** — **NOT** the IC),
**Argyll Robertson pupil** (upstream / downstream — **NOT** the
IC), **Adie's tonic pupil** (ciliary ganglion — **NOT** the IC),
**Weber syndrome** (crus cerebri — CN III — **NOT** the IC),
**Benedikt / Claude / Nothnagel syndromes** (tegmentum — CN III +
red nucleus / cerebellar — **NOT** the IC), **myasthenia gravis**
(NMJ — **NOT** the IC), **CCHS** (RTN), **OIRD** (pre-Bötzinger
complex — NK1R neurons), **Rett syndrome** (pre-Bötzinger complex),
**SIDS** (proposed — pre-Bötzinger complex + arcuate nucleus),
**essential hypertension / sympathetic overactivity** (C1 group /
RVLM), **Parkinson's disease** (substantia nigra — tegmentum),
**Huntington's disease** (striatum — telencephalon), or
**Kluver-Bucy syndrome** (amygdala). Its clinical relevance is
**direct** but **usually not localizing** — most auditory clinical
syndromes are **nerve**, **cochlear nucleus**, or **cortical**
lesions, not **IC** lesions. **No named inferior colliculus
syndrome exists.**

Lateralization Notes
--------------------
This is the **left** inferior colliculus leaf. The left and right
ICs are **bilaterally symmetric paired sensory relays** — with **NO
asymmetric subnuclear or decussation facts** — and carry **NO
coupling warning**:

*   **Bilateral Paired Sensory Relays:** Each side has its own IC —
    each is an **independent midbrain auditory relay**.

*   **Bilateral Auditory Input (cross-midline):** Each IC receives
    **bilateral** auditory input — from the **cochlear nuclei**,
    the **superior olivary complex**, and the **nucleus of the
    lateral lemniscus** on **both** sides — via the **lateral
    lemniscus** from **both** sides. **This bilateral input is a
    cross-midline conduction** — not intrinsic left-right coupling.

*   **Bilateral Auditory Output (cross-midline):** Each IC
    projects **bilaterally** to the **MGN** — via the **brachium of
    the inferior colliculus** to the **ipsilateral MGN**, and via
    the **commissure of the inferior colliculus** to the
    **contralateral IC** (which then projects to its
    **ipsilateral MGN**). **This bilateral output is a
    cross-midline conduction** — not intrinsic left-right coupling.

*   **The Commissure of the Inferior Colliculus:** The **left IC**
    and the **right IC** are **connected** by the **commissure of
    the inferior colliculus** — a **cross-midline conduction
    pathway**. **The commissure is a CONDUCTION PATHWAY** — **not
    a coupling mechanism**. The two ICs are **independent paired
    sensory relays** — **connected by a conduction pathway** — with
    **bilateral** ascending input and **bilateral** ascending
    output.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to SENSORY RELAYS):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **left IC** is a **sensory relay** — it
    does **not** generate a rhythm, so it does **not** carry the
    **oscillator coupling warning**. Its **left** and **right**
    sides are **independent sensory relays** — there is **no**
    IC-to-IC coupling in the oscillator sense. **The commissure of
    the inferior colliculus** is a **conduction pathway** — not
    a coupling mechanism. **Sensory relay nuclei carry NO coupling
    warning** — same rule as motor nuclei, premotor pools, sensor
    nuclei, and conduction pathways.

*   **Clinical Laterality — few named syndromes:**
    *   A **left IC lesion** → **subtle auditory deficits** — if
        any — typically **impaired sound localization** in the
        **contralateral** hemifield, **difficulty with speech in
        noise**, and possibly **tinnitus** (bilateral). **Profound
        hearing loss is RARE** — the ascending auditory pathway is
        **bilateral above the cochlear nuclei**, so the **right
        IC** and **right auditory cortex** provide **sufficient
        compensation**. **No named syndrome.**
    *   A **left cochlear nerve lesion** → **left sensorineural
        hearing loss** — **NOT** an IC lesion.
    *   A **left auditory cortex lesion** → **subtle auditory
        deficits** — **NOT** an IC lesion.
    *   **Bilateral IC lesions** (rare — part of a broader
        brainstem process) → **more significant auditory
        deficits** — usually part of a **broader brainstem
        syndrome**.
    *   **A consumer that assumes "left IC = right IC" will be
        structurally correct** (the two are symmetric), but a
        consumer that assumes a **left IC lesion** produces the
        same clinical picture as a **left cochlear nerve lesion**
        or a **left auditory cortex lesion** is **wrong** — the
        three localize to **different structures**.

**The left inferior colliculus is a strict mirror pair with the
right IC — no coupling warning, no SLEA warning, no
amygdala-lateralization warning, and no rhinencephalon-exclusion
flag** — **but with two crucial caveats**: (1) the **bilateral
auditory input and output** are cross-midline **conduction** via
the **lateral lemniscus** and the **commissure of the inferior
colliculus** — **not intrinsic left-right coupling**; (2) the
**clinical patterns** of left IC lesions, left cochlear nerve
lesions, and left auditory cortex lesions are **distinct** — the
IC is a **midbrain relay**, and its lesions produce **subtle**
auditory deficits (if any), not **profound hearing loss**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only — **no** import
    from ``.../right/inferior_colliculus/``.
*   **No cross-lobe imports.** This module does **not** import from
    the **cochlear nuclei**, the **superior olivary complex**, the
    **nucleus of the lateral lemniscus**, the **lateral lemniscus**,
    the **brachium of the inferior colliculus**, the **commissure
    of the inferior colliculus**, the **medial geniculate body**,
    the **auditory cortex (A1)**, the **superior colliculus**, the
    **PnC**, the **reticular formation**, or any other container.
    The left IC's relationships to the cochlear nuclei, the
    superior olivary complex, the nucleus of the lateral lemniscus,
    the lateral lemniscus, the brachium of the inferior colliculus,
    the commissure of the inferior colliculus, the medial geniculate
    body, the auditory cortex, the superior colliculus, the PnC,
    and the reticular formation are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **transmitter
    phenotypes** of the IC neurons (glutamatergic, GABAergic,
    glycinergic, cholinergic subpopulations) are
    ``chemicals_hormones``-layer facts — documented as **prose**,
    **never imported**.
*   **DUAL-PATH LEAF — CROSS-LISTED between the modern path and the
    older-term path.** Both paths resolve to **this leaf**. The
    **modern path** is the **structural home** by naming convention
    — the **older-term path** is the **synonym alias**. Consumers
    resolve by **one** path per lookup.
*   **SENSORY RELAY — NOT a sensorimotor integration structure.**
    The **SC** is the sensorimotor integration / saccade command
    generator; the **IC** is the **auditory relay**. Different
    functional classes.
*   **AUDITORY RELAY — NOT a saccade generator, NOT a gaze center,
    NOT a visual structure.** The **SC**, **PPRF**, **riMLF**,
    **pretectum**, and **LGN** are **different structures**.
*   **NOT the MGN — the MGN is DIENCEPHALON, UPSTREAM of the IC's
    target, DOWNSTREAM of the IC.**
*   **NOT the lateral lemniscus — the LL is a CONDUCTION PATHWAY,
    UPSTREAM of the IC.**
*   **NOT the cochlear nuclei or the superior olivary complex —
    those are HINDBRAIN auditory structures, UPSTREAM of the IC.**
*   **NOT the brachium of the inferior colliculus — the BIC is a
    CONDUCTION PATHWAY.**
*   **NOT the commissure of the inferior colliculus — the commissure
    is a CROSS-MIDLINE CONDUCTION PATHWAY.** The two ICs are
    **independent paired sensory relays** connected by a
    **conduction pathway** — **not intrinsic coupling**.
*   **NOT the PnC or the reticular formation — those are DOWNSTREAM
    of the IC in the ACOUSTIC STARTLE circuit.** The **IC is one
    node** — not the reflex itself.
*   **NOT the auditory cortex — the auditory cortex is the CORTICAL
    TARGET, DOWNSTREAM of the MGN, DOWNSTREAM of the IC.**
*   **SENSORY RELAY NUCLEI CARRY NO COUPLING WARNING.** Same rule
    as motor nuclei, premotor pools, sensor nuclei, relay nuclei,
    and conduction pathways. The **bilateral** auditory projections
    are cross-midline **conduction** — not intrinsic left-right
    coupling.
*   **SIDE-CONSISTENT — this leaf is the LEFT inferior colliculus.**
*   **MIRROR PARITY with ``.../right/inferior_colliculus/`` — strict
    mirror with NO warning.** The mirror is **clean** — the two
    ICs are **bilaterally symmetric paired sensory relays** with
    **no asymmetric subnuclear or decussation facts**.
*   **CHEMICALS-LAYER DISCIPLINE.** The **transmitter phenotypes**
    of the IC neurons are ``chemicals_hormones``-layer facts —
    documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing
    (dual path) is **within the tectum** (``tectum/left`` ↔
    ``tectum/corpora_quadrigemina/left``) — not into the forebrain
    or hindbrain. The **MGN** (diencephalon), the **auditory
    cortex** (telencephalon), the **cochlear nuclei** / **superior
    olivary complex** / **lateral lemniscus** / **PnC** (hindbrain),
    and the **cochlear nerve** (peripheral) are **separate
    structures** referenced as **prose**, not as cross-listed
    parents.
*   **No nested cross-listing.** The left IC is a **single
    dual-path leaf**. It is **not** a container.
*   **The on-disk tree is authoritative.** If the tree has **both**
    ``tectum/left/inferior_colliculus/`` **and**
    ``tectum/corpora_quadrigemina/left/inferior_colliculus/``, then
    the left IC is reachable by **either** path. If the tree has
    **only** one of the two, that is the **sole** path — but the
    leaf is still the **same left inferior colliculus**.

Usage
-----
Resolve the leaf by **either** path (they are equivalent — **this is
a dual-path anchor**)::

    # Modern path (structural home by naming convention):
    from infrastructure.brainparts.midbrain.tectum.left import inferior_colliculus

    # Older-term path (this module — older-term alias):
    from infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.left import inferior_colliculus

Or by fully-qualified path string::

    modern_path = (
        "midbrain.tectum.left.inferior_colliculus"
    )
    older_term_path = (
        "midbrain.tectum.corpora_quadrigemina.left.inferior_colliculus"
    )
    # Both resolve to THIS module.

**Do not** assume the two paths lead to **different structures** —
they lead to **one leaf**, cross-listed.

**Do not** assume the left inferior colliculus is the **left
superior colliculus**. The **SC** is the sensorimotor integration /
saccade command generator; the **IC** is the **auditory relay**.
**Different functional classes** — both carry **NO coupling
warning**, but for **different reasons**.

**Do not** assume the left inferior colliculus is the **left medial
geniculate body** (MGN). The **MGN** is the thalamic auditory relay
to **A1** — **diencephalic** — **downstream** of the IC. They are
**different structures at different levels** of the auditory
hierarchy.

**Do not** assume the left inferior colliculus is the **lateral
lemniscus**. The **LL** is a **conduction pathway** — **upstream**
of the IC.

**Do not** assume the left inferior colliculus is the **cochlear
nuclei** or the **superior olivary complex**. Those are
**hindbrain** auditory structures — **upstream** of the IC.

**Do not** assume the left inferior colliculus is the **brachium of
the inferior colliculus** or the **commissure of the inferior
colliculus**. Those are **conduction pathways** — the **BIC** is
the IC's output to the MGN; the **commissure** connects the two
ICs. **The IC is a NUCLEUS** — **grey matter**.

**Do not** assume the left inferior colliculus is the **PnC** or
the **reticular formation**. Those are **downstream** of the IC in
the **acoustic startle circuit**. The **IC is one node** — not the
reflex itself.

**Do not** assume the left inferior colliculus is the **auditory
cortex**. The **auditory cortex** is the **cortical target** —
**downstream** of the MGN, **downstream** of the IC.

**Do not** attribute **saccade generation**, **gaze control**,
**visual processing**, or **pupillary / optokinetic function** to
the left inferior colliculus. Those are the **SC**, the **PPRF**,
the **riMLF**, the **pretectum**, and the **LGN** — **NOT** the IC.
The IC is **auditory**.

**Do not** assume the left IC's **bilateral auditory projections**
are **intrinsic left-right coupling**. They are **cross-midline
conduction** via the **lateral lemniscus** and the **commissure of
the inferior colliculus** — **not** coupling in the oscillator
sense. **The two ICs are independent paired sensory relays.**

**Do not** import the **transmitter phenotypes** of the IC neurons
into the midbrain structural layer. Those are
**``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the left inferior
colliculus. **Sensory relay nuclei carry NO coupling warning** —
same rule as motor nuclei, premotor pools, sensor nuclei, and
conduction pathways.

Iterating the left inferior colliculus's (empty) children
(recommended consumer pattern)::

    INFERIOR_COLLICULUS_LEFT_CHILDREN = ()
    # The left inferior colliculus is a leaf. The subnuclear
    # organization (central nucleus, external nucleus, dorsal cortex,
    # lateral cortex) is prose, not modules. The auditory pathway
    # inputs (cochlear nuclei, superior olivary complex, lateral
    # lemniscus, auditory cortex) and outputs (MGN, superior
    # colliculus, reticular formation) are prose, not modules.

Reaching the modern path (recommended consumer pattern — the
STRUCTURAL HOME by naming convention)::

    # The modern path is the STRUCTURAL HOME of the left IC in
    # modern nomenclature — the term "tectum" is preferred to
    # "corpora quadrigemina":
    #
    #   brainparts.midbrain.tectum.left.inferior_colliculus
    #
    # Both paths resolve to the SAME leaf — the cross-listing
    # mechanism.

Reaching the right inferior colliculus (recommended consumer pattern
— the SIDE mirror)::

    # The right inferior colliculus is the RIGHT midbrain auditory
    # relay:
    #
    #   brainparts.midbrain.tectum.right.inferior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.right.inferior_colliculus
    #
    # The two ICs are BILATERALLY SYMMETRIC paired sensory relays —
    # with BILATERAL auditory input (via the lateral lemniscus from
    # both sides) and BILATERAL auditory output (via the brachium of
    # the IC and the commissure of the IC). The bilateral
    # projections are cross-midline CONDUCTION — not intrinsic
    # coupling.

Reaching the left superior colliculus (recommended consumer pattern
— the SENSORIMOTOR INTEGRATION counterpart, ROSTRAL)::

    # The left superior colliculus is the SENSORIMOTOR INTEGRATION /
    # saccade command generator — ROSTRAL to the IC — at the
    # oculomotor / EW / mesV level:
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.left.superior_colliculus
    #
    # The SC and the IC are DIFFERENT FUNCTIONAL CLASSES of
    # colliculus — the SC is sensorimotor integration; the IC is a
    # sensory relay. The IC PROJECTS TO the SC (for auditory
    # orienting and audiovisual integration).

Reaching the left medial geniculate body (recommended consumer
pattern — the THALAMIC AUDITORY RELAY, DOWNSTREAM of the IC)::

    # The left medial geniculate body (MGN) is the THALAMIC AUDITORY
    # RELAY to A1 — DOWNSTREAM of the left IC:
    #
    #   brainparts.forebrain.diencephalon.thalamus.medial_geniculate_body
    #
    # The IC projects to the MGN via the BRACHIUM OF THE INFERIOR
    # COLLICULUS. They are DIFFERENT STRUCTURES at DIFFERENT levels
    # of the auditory hierarchy.

Reaching the auditory cortex (recommended consumer pattern — the
CORTICAL AUDITORY TARGET, DOWNSTREAM of the MGN)::

    # The primary auditory cortex (A1) is the CORTICAL AUDITORY
    # TARGET — in the superior temporal gyrus of the temporal lobe —
    # DOWNSTREAM of the MGN, DOWNSTREAM of the IC:
    #
    #   brainparts.forebrain.telencephalon.cortex.temporal...auditory_cortex
    #
    # The IC is UPSTREAM of the MGN, which is UPSTREAM of A1.
    # Different structures at different levels.

Reaching the lateral lemniscus (recommended consumer pattern — the
AUDITORY CONDUCTION PATHWAY, UPSTREAM of the IC)::

    # The lateral lemniscus is an AUDITORY CONDUCTION PATHWAY —
    # carries auditory input from the cochlear nuclei and superior
    # olivary complex TO the IC:
    #
    #   brainparts.hindbrain.metencephalon.pons.lateral_lemniscus
    #
    # The LL is UPSTREAM of the IC — the LL FEEDS the IC.

Reaching the cochlear nuclei and the superior olivary complex
(recommended consumer pattern — the HINDBRAIN auditory structures,
UPSTREAM of the IC)::

    # The cochlear nuclei (first central auditory relay) and the
    # superior olivary complex (binaural processing) are HINDBRAIN
    # auditory structures — UPSTREAM of the IC:
    #
    #   brainparts.hindbrain.metencephalon.pons.cochlear_nuclei
    #   brainparts.hindbrain.metencephalon.pons.superior_olivary_complex
    #
    # The cochlear nuclei and the SOC are UPSTREAM of the IC.
    # Different structures at different levels of the auditory
    # hierarchy.

Reaching the brachium of the inferior colliculus and the commissure
of the inferior colliculus (recommended consumer pattern — the
CONDUCTION PATHWAYS)::

    # The brachium of the inferior colliculus (BIC) carries the IC's
    # auditory output to the MGN; the commissure of the inferior
    # colliculus connects the left IC to the right IC:
    #
    #   brainparts.midbrain.tectum.left.brachium_of_the_inferior_colliculus
    #   brainparts.midbrain.tectum.left.commissure_of_the_inferior_colliculus
    #
    # The brachium and the commissure are CONDUCTION PATHWAYS; the
    # IC is a NUCLEUS.

Reaching the PnC and the reticular formation (recommended consumer
pattern — the DOWNSTREAM reticular node in the ACOUSTIC STARTLE
circuit)::

    # The nucleus reticularis pontis caudalis (PnC) and the
    # reticular formation are DOWNSTREAM of the IC in the ACOUSTIC
    # STARTLE circuit:
    #
    #   brainparts.hindbrain.metencephalon.pons.pnc
    #
    # The acoustic startle circuit is: cochlear nucleus -> nucleus
    # of the lateral lemniscus -> IC -> PnC -> spinal motor neurons.
    # The IC is ONE NODE in the circuit — not the reflex itself.

Bilateral iteration (recommended consumer pattern — NOTE the
dual-path cross-listing and the no-coupling-warning rule)::

    for side in ("left", "right"):
        for colliculus in (
            "superior_colliculus",
            "inferior_colliculus",
        ):
            # Either path resolves to the same leaf — use ONE:
            modern_path = (
                f"midbrain.tectum.{side}.{colliculus}"
            )
            older_term_path = (
                f"midbrain.tectum.corpora_quadrigemina."
                f"{side}.{colliculus}"
            )
            # Both resolve to the SAME leaf.
            #
            # NOTE: the two colliculi (SC, IC) are in DIFFERENT
            # functional classes — SC = sensorimotor integration;
            # IC = sensory relay. BOTH carry NO coupling warning.
            # The IC's bilateral auditory projections are
            # cross-midline CONDUCTION via the lateral lemniscus
            # and the commissure of the inferior colliculus — not
            # intrinsic left-right coupling. The two ICs are
            # independent paired sensory relays.

Subnuclear-organization detail (not wired — consult references)::

    # The left inferior colliculus has a subnuclear organization:
    #
    #   central nucleus    -> TONOTOPIC (frequency map) —
    #                         frequency and temporal processing
    #                         (the "what" of the auditory signal);
    #                         principal ascending projection to
    #                         the MGN (via the brachium of the IC)
    #   external nucleus   -> AUDITORY SPACE MAP (spatiotopic) —
    #                         binaural cues (interaural time and
    #                         intensity differences) -> a map of
    #                         where a sound is coming from (the
    #                         "where"); projects to the SC (for
    #                         auditory orienting)
    #   dorsal cortex      -> MULTISENSORY INTEGRATION — auditory,
    #                         somatosensory, visual input; less
    #                         well characterized in humans
    #   lateral cortex     -> LEAST CHARACTERIZED — functional
    #                         role not well established in humans
    #
    # Do not attempt to resolve these subnuclei as sub-paths of the
    # inferior colliculus — they are PROSE, not modules.

Clinical-pattern detail (not wired — consult references)::

    # The left inferior colliculus is the LEFT MIDBRAIN AUDITORY
    # RELAY. The CLINICAL PATTERNS of the related lesions are
    # DISTINCT:
    #
    #   LEFT IC lesion              -> SUBTLE auditory deficits
    #                                   (if any): impaired sound
    #                                   localization in the
    #                                   contralateral hemifield,
    #                                   difficulty with speech in
    #                                   noise, possible tinnitus
    #                                   (bilateral). PROFOUND hearing
    #                                   loss is RARE (bilateral
    #                                   auditory pathway above
    #                                   cochlear nuclei).
    #   LEFT cochlear nerve lesion  -> LEFT SENSORINEURAL HEARING
    #                                   LOSS — NOT an IC lesion
    #   LEFT auditory cortex lesion -> SUBTLE auditory deficits —
    #                                   NOT an IC lesion
    #   BILATERAL IC lesions        -> MORE SIGNIFICANT auditory
    #                                   deficits (sound
    #                                   localization, speech in
    #                                   noise) — usually part of a
    #                                   broader brainstem process,
    #                                   NOT an isolated IC syndrome
    #   TINNITUS                    -> IMPLICATED — IC is one node
    #                                   in the tinnitus network;
    #                                   usually bilateral; NOT a
    #                                   left-IC-specific disorder
    #   AUDIOGENIC SEIZURES         -> IMPLICATED — IC is one node
    #                                   in the animal-model seizure
    #                                   circuit; human reflex
    #                                   epilepsy is RARE and involves
    #                                   CORTICAL / THALAMIC networks
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # STRUCTURES.

The ascending auditory pathway — detail (not wired — consult
references)::

    # The ascending auditory pathway — the IC is the MIDBRAIN
    # RELAY:
    #
    #   cochlear nerve (CN VIII) -> cochlear nuclei (pons/medulla)
    #     -> superior olivary complex (pons) -> nucleus of the
    #     lateral lemniscus (pons) -> lateral lemniscus (pons) ->
    #     INFERIOR COLLICULUS (midbrain — THIS LEAF) -> brachium
    #     of the inferior colliculus (midbrain) -> medial
    #     geniculate body (diencephalon/thalamus) -> auditory
    #     cortex (A1, temporal lobe)
    #
    # The IC is ONE STATION in the ascending auditory pathway —
    # downstream of the lateral lemniscus, upstream of the MGN.
    # The bilateral auditory input and output are cross-midline
    # CONDUCTION via the lateral lemniscus and the commissure of
    # the inferior colliculus — not intrinsic left-right coupling.
    #
    # Do not attempt to resolve the cochlear nuclei, the SOC, the
    # LL, the MGN, or A1 as sub-paths of the IC — they are
    # DIFFERENT structures at DIFFERENT levels of the auditory
    # hierarchy.

The acoustic startle reflex circuit — detail (not wired — consult
references)::

    # The acoustic startle reflex — the IC is ONE NODE:
    #
    #   sudden, loud sound -> cochlear nerve (CN VIII) -> cochlear
    #     nucleus (pons/medulla) -> nucleus of the lateral
    #     lemniscus (pons) -> INFERIOR COLLICULUS (midbrain — THIS
    #     LEAF) -> nucleus reticularis pontis caudalis (PnC, pons)
    #     -> spinal motor neurons -> motor response (startle)
    #
    # The IC is the MIDBRAIN AUDITORY NODE that feeds the startle
    # command to the PnC. The startle reflex is a DISTRIBUTED
    # brainstem circuit — not a structure. The IC is ONE NODE.
    #
    # Do not attempt to resolve the PnC, the reticular formation,
    # or the spinal motor neurons as sub-paths of the IC — they
    # are DIFFERENT structures at DIFFERENT levels of the startle
    # circuit.

References
----------
*   **Canonical inferior colliculus anatomy:** Ehret, G., Romand,
    R. (eds.) (1997). *The Central Auditory System*. Oxford
    University Press. (The inferior colliculus as the midbrain
    auditory relay — its subnuclear organization (central nucleus,
    external nucleus, dorsal cortex, lateral cortex), its
    ascending auditory inputs, its projections to the MGN and the
    superior colliculus, its tonotopic and spatiotopic maps.)
*   **Inferior colliculus — comprehensive review:** Winer, J.A.,
    Schreiner, C.E. (eds.) (2005). *The Inferior Colliculus: A
    Window to the Brain*. Springer. (The definitive modern review
    of the inferior colliculus — cytoarchitecture, connectivity,
    function, and its role in the auditory pathway and the startle
    circuit.)
*   **Inferior colliculus — tonotopic and spatiotopic maps:**
    Casseday, J.H., Covey, E. (1996). "A neuroethological theory of
    the function of the inferior colliculus." *Trends in
    Neurosciences* 19:401–406. (The central nucleus as the
    tonotopic subdivision; the external nucleus as the auditory
    space map subdivision — the "what" and "where" of the auditory
    signal.)
*   **Auditory space map in the external nucleus:** King, A.J.,
    Palmer, A.R. (1983). "Cells responsive to free-field auditory
    stimuli in guinea-pig superior colliculus: distribution and
    response properties." *Journal of Physiology* 342:361–381.
    (The auditory space map in the external nucleus of the inferior
    colliculus — the mechanism by which the IC computes the
    location of a sound.)
*   **Ascending auditory pathway:** Webster, D.B., Popper, A.N.,
    Fay, R.R. (eds.) (1992). *The Mammalian Auditory Pathway:
    Neuroanatomy*. Springer. (The ascending auditory pathway — the
    cochlear nuclei, superior olivary complex, lateral lemniscus,
    inferior colliculus, medial geniculate body, and auditory
    cortex; the IC as the midbrain relay.)
*   **Acoustic startle reflex:** Davis, M., Gendelman, D.S.,
    Tischler, M.D., Gendelman, P.M. (1982). "A primary acoustic
    startle circuit: lesion and stimulation studies." *Journal of
    Neuroscience* 2:791–805. (The acoustic startle reflex circuit —
    the cochlear nucleus, nucleus of the lateral lemniscus,
    inferior colliculus, PnC, and spinal motor neurons; the IC as
    one node.)
*   **Tinnitus and the inferior colliculus:** Kaltenbach, J.A.,
    Godfrey, D.A., Neumann, J.B., McCaslin, D.L., Afman, C.E.,
    Zhang, J. (1998). "Changes in spontaneous neural activity in
    the dorsal cochlear nucleus following exposure to intense
    sound: relation to threshold shift." *Hearing Research*
    124:78–84. (The IC and the dorsal cochlear nucleus in
    tinnitus — the "increased spontaneous activity" hypothesis;
    the IC is IMPLICATED, not established as the sole substrate.)
*   **Audiogenic seizures:** Faingold, C.L. (1999). "Neuronal
    networks in the genetically epilepsy-prone rat." *Advances in
    Neurology* 79:75–111. (The inferior colliculus as a critical
    node in audiogenic seizure circuits in animal models — the
    genetically epilepsy-prone rat, DBA/2 mice.)
*   **Medial geniculate body (contrast — thalamic auditory relay):**
    Winer, J.A., Schreiner, C.E. (eds.) (2005). *The Inferior
    Colliculus: A Window to the Brain*. Springer. (The MGN as the
    thalamic auditory relay to A1 — the IC projects to it via the
    brachium of the inferior colliculus.)
*   **Superior colliculus (contrast — sensorimotor integration):**
    Sparks, D.L. (2002). "The brainstem control of saccadic eye
    movements." *Nature Reviews Neuroscience* 3:952–964. (The
    superior colliculus as the saccade command generator — the IC
    projects to it for auditory orienting and audiovisual
    integration.)
*   **Cochlear nuclei and superior olivary complex (contrast —
    hindbrain auditory structures, upstream of the IC):** Cant,
    N.B., Benson, C.G. (2003). "Parallel auditory pathways: a
    review of the functional anatomy of the ascending auditory
    system." *Brain Research Bulletin* 60:457–474. (The cochlear
    nuclei and the superior olivary complex — the first central
    auditory relays — upstream of the IC.)
*   **Lateral lemniscus (contrast — conduction pathway, upstream of
    the IC):** Webster, D.B., Popper, A.N., Fay, R.R. (eds.)
    (1992). *The Mammalian Auditory Pathway: Neuroanatomy*.
    Springer. (The lateral lemniscus as the auditory conduction
    pathway carrying signals to the inferior colliculus.)
*   **Brachium of the inferior colliculus and commissure of the
    inferior colliculus (contrast — conduction pathways):** Winer,
    J.A., Schreiner, C.E. (eds.) (2005). *The Inferior Colliculus:
    A Window to the Brain*. Springer. (The brachium of the
    inferior colliculus as the IC-to-MGN pathway; the commissure
    of the inferior colliculus as the cross-midline pathway
    connecting the two ICs.)
*   **SLEA (contrast — the left inferior colliculus is not SLEA):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the inferior colliculus.)
*   NeuroNames — Inferior colliculus (left); FMA — Inferior
    colliculus (left member).
"""