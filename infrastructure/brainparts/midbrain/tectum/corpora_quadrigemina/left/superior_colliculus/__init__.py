"""
infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.left.superior_colliculus
====================================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tectum
        ├── left
        │   └── superior_colliculus          (modern path — STRUCTURAL
        │                                     HOME by naming convention)
        └── corpora_quadrigemina
            └── left
                └── superior_colliculus      <-- THIS MODULE (older-term
                                                 path — SAME leaf)

**Primary synonym:** Left superior colliculus; **left SC**; **left
colliculus superior**; **left corpus quadrigeminum anterius** (older
Latin usage); **left anterior colliculus**; **left optic tectum**
(comparative-anatomy name — the SC is the **homologue** of the optic
tectum in non-mammalian vertebrates); **left tectum opticum**
(comparative name).
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **sensorimotor integration** structure in the
**rostral midbrain tectum**, at the level of the **oculomotor
nucleus (CN III)**, the **Edinger-Westphal nucleus** (CN IIIp), and
the **mesencephalic trigeminal nucleus** (CN Vm). It has a **layered
organization** — the **superficial layers** (visual, retinotopic)
and the **intermediate / deep layers** (motor map, multisensory
integration, premotor output). **It is the saccade command
generator** — the **top level** of the **saccade hierarchy** — and
the **principal visual/oculomotor orienting structure** of the
midbrain.
**Part of:** The **tectum** region container — specifically the
**left superior colliculus**, at the level of the **oculomotor /
EW / mesV nuclei** (the **rostral** colliculus). **Dual-path leaf —
reachable via both ``.../tectum/left/superior_colliculus/`` (modern
path — STRUCTURAL HOME) and
``.../tectum/corpora_quadrigemina/left/superior_colliculus/``
(older-term path — this module).** Both paths resolve to **this
leaf**. See *Structural parent* and *Dual-Path Cross-Listing*.
**Structural parent (MODERN PATH — STRUCTURAL HOME by naming
convention):** ``.../tectum/left/superior_colliculus/`` — the
**modern path** — the **structural home** for the leaf in **modern
nomenclature**. **This module and the modern-path module are the
SAME LEAF** — the two paths reach the **same substantive content**.
**Structural parent (OLDER-TERM PATH — this module's path):**
``.../tectum/corpora_quadrigemina/left/superior_colliculus/`` — the
**older-term path** — the **synonym alias** for the same leaf. **The
older-term path does NOT replace the modern path — it adds a
synonym alias.** Both paths reach **this module**.
**Structural children:** **None.** This is a **leaf** module. The
**layered organization** (superficial layers, intermediate layers,
deep layers) is documented as **prose** — not as structural
children. The **retinotopic map**, the **motor map**, and the
**multisensory maps** (visual, auditory, somatosensory) are
**prose**, not structural children. The **inputs** (retina, V1,
inferior colliculus, auditory cortex, spinal cord, trigeminal
system, FEF, SNr, fastigial nucleus) and **outputs** (PPRF, riMLF,
CN III/IV/VI nuclei, pulvinar, pretectum, PAG, inferior olive) are
**prose**, not structural children.
**Boundary status (DUAL-PATH LEAF — CROSS-LISTED between the
MODERN PATH and the OLDER-TERM PATH):** **Boundary case — the left
superior colliculus is a DUAL-PATH LEAF.** It is reachable by **two**
structural paths:
*   **Modern path (STRUCTURAL HOME by naming convention)** —
    ``.../tectum/left/superior_colliculus/``
*   **Older-term path (this module)** —
    ``.../tectum/corpora_quadrigemina/left/superior_colliculus/``
**Both paths resolve to the SAME leaf** — this module. Consumers
resolving the leaf by **either** path get **the same substantive
content**. Consumers must **not** assume the two paths lead to
**different structures** — they lead to **one leaf**, cross-listed.
See *Dual-Path Cross-Listing* and *Design Contract*.
**Boundary status (SENSORIMOTOR INTEGRATION — NOT a sensory relay):**
**Boundary case — the left superior colliculus is a SENSORIMOTOR
INTEGRATION structure, NOT a sensory relay.** It receives **visual,
auditory, and somatosensory** input and **integrates** them into a
**common orienting map** — and it generates **saccade commands** to
the **PPRF**, **riMLF**, and **CN III/IV/VI nuclei**. **The IC**
(left and right inferior colliculus) is a **sensory relay** — it
receives **auditory** input and projects to the **MGN** for
**conscious auditory perception**. **The SC and the IC are DIFFERENT
FUNCTIONAL CLASSES of colliculus** — the **SC** is **sensorimotor
integration**; the **IC** is **sensory relay**. **Both carry NO
coupling warning** — but for **different reasons** (neither is an
oscillator). Consumers must **not** conflate the SC with the IC.
**Boundary status (COMMAND LEVEL — NOT a premotor saccade
generator):** **Boundary case — the left superior colliculus is the
COMMAND LEVEL of the saccade hierarchy, NOT a premotor saccade
generator.** The **saccade hierarchy** is: **SC (command) → PPRF /
riMLF (premotor) → CN III/IV/VI nuclei (motor) → extraocular muscles
(effector)**. The **SC decides where to look** — it generates a
**saccade command** in a **motor map** of saccade vectors. The
**PPRF** (horizontal) and the **riMLF** (vertical) **transform** the
SC's command into the **premotor saccade signal** that drives the CN
nuclei. The **SC is UPSTREAM of the PPRF and riMLF** — it is **not**
a premotor saccade generator, and it is **not** a motor nucleus.
Consumers must **not** conflate the SC with the PPRF, the riMLF, or
the CN nuclei.
**Boundary status (NOT a motor nucleus — the CN III/IV/VI nuclei are
the MOTOR level):** **Boundary case — the left superior colliculus
is NOT a motor nucleus.** The **left oculomotor nucleus** (CN III),
the **left trochlear nucleus** (CN IV), and the **abducens nucleus**
(CN VI) are the **motor nuclei** that **execute** the saccade by
driving the **extraocular muscles**. The **SC** is the **command
level** — it **drives** the motor nuclei **indirectly** (via the
PPRF, riMLF, and the tectobulbar tract), but it is **not** a motor
nucleus. Consumers must **not** conflate the SC with the CN nuclei.
**Boundary status (NOT the LGN — the LGN is the VISUAL THALAMIC
RELAY to V1):** **Boundary case — the left superior colliculus is
NOT the left lateral geniculate body (LGN).** The **LGN**
(``.../forebrain/diencephalon/thalamus/lateral_geniculate_body/``)
is the **thalamic visual relay** to the **primary visual cortex
(V1)** — it is the **thalamic station** for **conscious visual
perception**. **The SC does NOT project to the LGN** — it projects
to the **pulvinar** (thalamic visual **attention**) and to the
**saccade generators** (PPRF, riMLF, CN nuclei). **They are
DIFFERENT STRUCTURES in DIFFERENT functional systems** — the
**LGN** is the **thalamic relay for conscious vision**; the **SC**
is the **midbrain orienting structure**. Consumers must **not**
conflate the SC with the LGN, and must **not** resolve the LGN
through the SC path (or vice versa).
**Boundary status (NOT the pretectum — the pretectum is the
PUPILLARY AND OPTOKINETIC region, ROSTRAL to the SC):** **Boundary
case — the left superior colliculus is NOT the pretectum.** The
**pretectum** (``.../midbrain/pretectum/``) is a **separate
region** at the **diencephalon-midbrain junction** — **rostral** to
the SC — containing the **olivary pretectal nucleus**, the
**nucleus of the optic tract**, and the **anterior, posterior, and
medial pretectal nuclei**. **The pretectum is PUPILLARY AND
OPTOKINETIC; the SC is SACCADIC AND ORIENTING.** Consumers must
**not** conflate the SC with the pretectum.
**Boundary status (NOT the inferior colliculus — the IC is a SENSORY
RELAY, the SIBLING colliculus):** **Boundary case — the left
superior colliculus is NOT the left inferior colliculus.** The
**left inferior colliculus**
(``.../tectum/left/inferior_colliculus/`` **and**
``.../tectum/corpora_quadrigemina/left/inferior_colliculus/``) is
the **auditory relay** — the **sensory relay** sibling of the SC.
**The IC is UPSTREAM of the SC's auditory-orienting input** — the
IC **projects to the SC** (for **auditory orienting** and
**audiovisual integration**). **They are DIFFERENT FUNCTIONAL
CLASSES of colliculus** — the **SC** is **sensorimotor
integration**; the **IC** is **sensory relay**. Consumers must
**not** conflate the SC with the IC.
**Boundary status (NOT the PAG — the PAG is the PAIN-MODULATION AND
DEFENSIVE-BEHAVIOR region):** **Boundary case — the left superior
colliculus is NOT the left periaqueductal gray (PAG).** The **PAG**
(``.../tegmentum/left/periaqueductal_gray/``) is the
**pain-modulation and defensive-behavior** region of the **ventral
midbrain** — **ventral** to the cerebral aqueduct. The **SC** is a
**tectum** structure — **dorsal** to the aqueduct. **The SC
projects to the PAG** (via the **tectotegmental** pathway) for
**defensive behaviors** — but the **PAG is not the SC**. Consumers
must **not** conflate the SC with the PAG.
**Boundary status (NOT the pulvinar — the pulvinar is the THALAMIC
VISUAL ATTENTION relay):** **Boundary case — the left superior
colliculus is NOT the pulvinar.** The **pulvinar**
(``.../forebrain/diencephalon/thalamus/pulvinar/``) is the
**thalamic visual attention** relay — the SC **projects to the
pulvinar** (via the **brachium of the SC** and the **tectothalamic**
pathway) for **visual attention** and **awareness**. **They are
DIFFERENT STRUCTURES** — the **pulvinar** is **diencephalic**; the
**SC** is **mesencephalic**. Consumers must **not** conflate the SC
with the pulvinar.
**Boundary status (NOT the FEF — the FEF is the CORTICAL VOLUNTARY
saccade control region):** **Boundary case — the left superior
colliculus is NOT the left frontal eye field (FEF).** The **FEF**
(``.../forebrain/telencephalon/cortex/frontal/frontal_eye_field/``)
is the **cortical voluntary saccade** control region in the
**frontal lobe** — it **projects to the SC** (via the
**corticotectal** pathway) for **voluntary saccades** and to the
**PPRF** (via the **corticoreticular** pathway) for **voluntary
horizontal saccades**. **The FEF is the CORTICAL command; the SC is
the MIDBRAIN command.** They are **DIFFERENT STRUCTURES at
DIFFERENT levels** of the saccade system. Consumers must **not**
conflate the SC with the FEF.
**Boundary status (NOT the SNr — the SNr is the BASAL GANGLIA
inhibitory saccade control region):** **Boundary case — the left
superior colliculus is NOT the left substantia nigra pars reticulata
(SNr).** The **SNr**
(``.../midbrain/tegmentum/left/substantia_nigra/pars_reticulata/``)
is the **basal ganglia inhibitory** control of saccade generation —
it **projects to the SC** (via the **nigrotectal** pathway) and
**tonically inhibits** saccade generation. **The SNr is the
inhibitory gate; the SC is the command generator.** They are
**DIFFERENT STRUCTURES** — the **SNr** is **tegmentum**; the **SC**
is **tectum**. Consumers must **not** conflate the SC with the SNr.
**Boundary status (NOT the fastigial nucleus — the fastigial nucleus
is the CEREBELLAR SACCADE ADAPTATION nucleus):** **Boundary case —
the left superior colliculus is NOT the fastigial nucleus.** The
**fastigial nucleus**
(``.../hindbrain/metencephalon/cerebellum/deep_cerebellar_nuclei/
fastigial_nucleus/``) is the **cerebellar** nucleus that **projects
to the SC** (via the **cerebellotectal** pathway) for **saccade
adaptation** and **accuracy**. **The fastigial nucleus is the
cerebellar output; the SC is the midbrain command generator.** They
are **DIFFERENT STRUCTURES** — the **fastigial** is
**cerebellar**; the **SC** is **mesencephalic**. Consumers must
**not** conflate the SC with the fastigial nucleus.
**Boundary status (NOT the brachium of the superior colliculus —
the brachium is a CONDUCTION PATHWAY):** **Boundary case — the left
superior colliculus is NOT the left brachium of the superior
colliculus (BSC).** The **BSC** is the **conduction pathway** —
**white matter** — that carries **retinal input** to the SC and
**visual attention output** from the SC to the pulvinar. **The SC is
the NUCLEUS** — **grey matter**. **They are DIFFERENT STRUCTURES** —
the **BSC** is a **conduction pathway**; the **SC** is a **nucleus**.
Consumers must **not** conflate the SC with the BSC.
**Boundary status (NOT the tectobulbar tract — the tectobulbar tract
is a CONDUCTION PATHWAY):** **Boundary case — the left superior
colliculus is NOT the left tectobulbar tract.** The **tectobulbar
tract** is the **descending conduction pathway** — **white matter** —
that carries the SC's saccade command to the **PPRF**, **riMLF**,
and **CN nuclei** (and to the **inferior olive**, the **PAG**, and
other targets). **The SC is the NUCLEUS** — **grey matter**. **They
are DIFFERENT STRUCTURES** — the **tectobulbar tract** is a
**conduction pathway**; the **SC** is a **nucleus**. Consumers must
**not** conflate the SC with the tectobulbar tract.
**Boundary status (NOT the tectoreticular pathway — the
tectoreticular pathway is a CONDUCTION PATHWAY):** **Boundary case
— the left superior colliculus is NOT the left tectoreticular
pathway.** The **tectoreticular** pathway is the **descending
conduction pathway** — **white matter** — that carries the SC's
command to the **PPRF** (horizontal saccades) and the **riMLF**
(vertical saccades). **It is a SUBSET of the tectobulbar tract**
(the tectoreticular fibers are a component of the tectobulbar
tract). **The SC is the NUCLEUS** — **grey matter**. **They are
DIFFERENT STRUCTURES** — the **tectoreticular pathway** is a
**conduction pathway**; the **SC** is a **nucleus**. Consumers must
**not** conflate the SC with the tectoreticular pathway.
**Boundary status (CONTRALATERAL RETINOTOPIC AND MOTOR MAPS — the
DEFINING ASYMMETRY of the SC):** **Boundary case — the left
superior colliculus represents the RIGHT (CONTRALATERAL) VISUAL
FIELD and generates RIGHTWARD (CONTRALATERAL) SACCADES.** This is
the **definitive asymmetric fact** of the SC — the **key
difference** from the inferior colliculus (which is **bilaterally
symmetric**). The **superficial layers** of the **left SC** receive
**direct retinal input** from the **right (contralateral) visual
field** (via the **crossed nasal retinal fibers** and the
**brachium of the SC**) and **corticotectal input** from the
**left V1** (which also represents the **right visual field**). The
**intermediate layers** contain a **motor map** that is **aligned**
with the **retinotopic map** — a given collicular location encodes a
**saccade to the corresponding location in the right visual field**,
i.e., a **rightward saccade**. **The left SC is a RIGHT-field /
RIGHT-saccade map.** **The right SC is a LEFT-field / LEFT-saccade
map.** **A consumer that assumes "left SC = left visual field" is
WRONG** — the **left SC represents the RIGHT visual field**, and a
**left SC lesion** produces **subtle deficits** in **rightward
saccades** and **right visual field orienting** (usually
**compensated** by the **right SC**). **This is the key structural
fact the mirror leaf must flip** — see *Lateralization Notes* and
*The Retinotopic Map and the Motor Map*.
**Boundary status (SENSORIMOTOR INTEGRATION — NOT an oscillator, NOT
a premotor pool, NOT a motor nucleus, NOT a conduction pathway):**
**Boundary case — the left superior colliculus is a SENSORIMOTOR
INTEGRATION structure.** In the family's **structure-class
taxonomy**, it is a **new class** — **sensorimotor integration** —
distinct from the **sensory relay** class (the **IC**, the
**pretectum**), the **premotor saccade generator** class (the
**PPRF**, the **riMLF**), and the **motor nucleus** class (the **CN
III/IV nuclei**). **The SC integrates visual, auditory, and
somatosensory input and generates a saccade command.** It is
**NOT** an **oscillator**, **NOT** a **premotor pool**, **NOT** a
**motor nucleus**, **NOT** a **conduction pathway** (the
**tectobulbar** and **tectoreticular** fibers are the conduction
pathways), and **NOT** a **sensory relay** (the **IC** and the
**pretectum** are the sensory relays). **Sensorimotor integration
structures carry NO coupling warning** — same rule as motor nuclei,
premotor pools, sensor nuclei, relay nuclei, and conduction
pathways. The **two SCs** are **independent paired sensorimotor
integration structures** — they **project bilaterally** to the
**PPRF**, **riMLF**, and **CN nuclei** (via the **tectobulbar**
tract), but this **bilateral output** is a **downstream
projection** to **bilateral targets** — **not intrinsic left-right
coupling** in the oscillator sense. **The two SCs are independent
paired structures with NO coupling warning.** See *Lateralization
Notes* and *Design Contract*.

Overview
--------
The left superior colliculus (left SC) is the **left saccade command
generator** and the **principal visual/oculomotor orienting
structure** of the midbrain — located in the **left rostral midbrain
tectum**, at the level of the **oculomotor nucleus (CN III)**, the
**Edinger-Westphal nucleus** (CN IIIp), and the **mesencephalic
trigeminal nucleus** (CN Vm). It is the **top level** of the
**saccade hierarchy** — the **sensorimotor integration** structure
that **decides where to look** and **commands the saccade**. It is a
**dual-path leaf** — reachable by **both** the modern path
(``.../tectum/left/superior_colliculus/``) and the older-term path
(``.../tectum/corpora_quadrigemina/left/superior_colliculus/``) —
**both paths resolve to this leaf**.

**The left SC is a SENSORIMOTOR INTEGRATION structure, NOT a sensory
relay.** The **inferior colliculus** is the sensory relay (auditory);
the **SC** is the **sensorimotor integration** structure (visual /
auditory / somatosensory → saccade command). **The SC and the IC are
DIFFERENT functional classes** — and **both carry NO coupling
warning** (neither is an oscillator). Consumers must **not** conflate
the SC with the IC.

**The left SC is the COMMAND LEVEL of the saccade hierarchy — NOT a
premotor saccade generator, NOT a motor nucleus.** The **saccade
hierarchy** is: **SC (command) → PPRF / riMLF (premotor) → CN III/IV/
VI nuclei (motor) → extraocular muscles (effector)**. The **SC
decides; the PPRF/riMLF execute; the CN nuclei drive; the muscles
move.** The **SC is UPSTREAM of all three downstream levels** — it is
the **command level**.

**The left SC is a CONTRALATERAL RETINOTOPIC AND MOTOR MAP — the
definitive asymmetric fact.** The **left SC** represents the **right
(contralateral) visual field** and generates **rightward
(contralateral) saccades**. The **right SC** represents the **left
visual field** and generates **leftward saccades**. **A left SC
lesion produces subtle deficits in rightward saccades and right
visual field orienting** — usually compensated by the right SC. This
is **the key structural fact the mirror leaf must flip**.

**The left SC is a paired structure with NO coupling warning.** The
**two SCs** are **independent paired sensorimotor integration
structures** — with **contralateral retinotopic and motor maps** —
and **bilateral output** to the **PPRF**, **riMLF**, and **CN
nuclei**. The **bilateral output is a downstream projection** to
**bilateral targets** — **not intrinsic left-right coupling**. The
two SCs are **independent paired structures** — **no coupling
warning**. See *Lateralization Notes*.

Dual-Path Cross-Listing
-----------------------
The **left superior colliculus** is reachable by **two structural
paths** — the **modern path** and the **older-term path**:

*   **Modern path (STRUCTURAL HOME by naming convention)** —
    ``.../tectum/left/superior_colliculus/``
*   **Older-term path (this module)** —
    ``.../tectum/corpora_quadrigemina/left/superior_colliculus/``

**Both paths resolve to the SAME leaf** — **this module**. The
**modern path** is the **structural home** for the leaf in **modern
nomenclature** — the term **"tectum"** is preferred to **"corpora
quadrigemina"** in modern anatomy, and the **modern path** carries
that preference in the tree. **The older-term path** is the
**synonym alias** — reachable because the tree preserves
**"corpora quadrigemina"** as a synonym path (see
``.../tectum/corpora_quadrigemina/`` for the historical framing).

**Consumers should resolve the leaf by ONE path** — not by both.
Enumerating **both** paths yields **duplicates** for the left
superior colliculus. **The two paths are equivalent** for the leaf
content they point at — the same substantive module.

**This is the same cross-listing mechanism** used between
``cranial_nerve_nuclei/`` and ``tegmentum/`` (for the midbrain CN
nuclei), and between ``tectum/left/`` and
``tectum/corpora_quadrigemina/left/`` (for the two colliculi). The
leaf is the **same substantive content** under both paths.

Layered Organization (prose, not structural children)
----------------------------------------------------
The left superior colliculus has a **layered organization** — **not
a subnuclear organization** in the classical sense (there are no
sharp cytoarchitectonic subnuclei), but a **functional lamination** —
documented as **prose**, not as structural children:

*   **Superficial layers** — **stratum zonale**, **stratum griseum
    superficiale**, **stratum opticum** — the **visual layers**.
    They receive **direct retinal input** (via the **brachium of
    the SC** and the **optic tract**) and **corticotectal input**
    from **V1** and the **visual association cortex**. They contain
    a **retinotopic map** of the **contralateral (right) visual
    field**. **The superficial layers process the VISUAL signal.**

*   **Intermediate layers** — **stratum griseum intermediale**,
    **stratum album intermediale** — the **motor layers**. They
    receive **multimodal input** (visual, auditory, somatosensory)
    and contain a **motor map** of **saccade vectors** (amplitude
    and direction) — **aligned** with the retinotopic map — that
    encodes **saccades to the corresponding location in the
    right visual field**. **The intermediate layers contain the
    SACCADE COMMAND.**

*   **Deep layers** — **stratum griseum profundum**, **stratum album
    profundum** — the **multisensory and premotor output layers**.
    They receive **multimodal input** (auditory from the **IC**,
    somatosensory from the **spinal cord** and the **trigeminal
    system**, and **frontal eye field** input for **voluntary**
    control) and **project** to the **PPRF**, **riMLF**, **CN
    III/IV/VI nuclei**, **pulvinar**, **pretectum**, **PAG**, and
    **inferior olive** (via the **tectobulbar**, **tectoreticular**,
    **tectothalamic**, **tectotegmental**, and **tecto-olivary**
    pathways). **The deep layers are the OUTPUT STAGE.**

**The superficial and deep layers are connected by intrinsic
circuits** — the **superficial visual layers** project to the
**intermediate motor layers**, which project to the **deep output
layers**. **The layered structure is the SC's functional
architecture** — visual input → motor command → premotor output.
Consumers must **not** resolve the individual layers as sub-paths of
the SC — they are **functional lamination**, not **structural
subnuclei**.

The Retinotopic Map and the Motor Map
-------------------------------------
The **left SC** contains **two aligned maps** — the **retinotopic
map** (in the superficial layers) and the **motor map** (in the
intermediate/deep layers). **The alignment is the key functional
fact:**

*   **Retinotopic map** — a **topographic representation** of the
    **contralateral (right) visual field** — with the **fovea**
    represented at the **rostral pole**, and the **far periphery**
    represented at the **caudal pole**. **A given collicular
    location** corresponds to a **given location in the right
    visual field**.

*   **Motor map** — a **topographic representation** of **saccade
    vectors** (amplitude and direction) — with **small saccades**
    (and **fixation**) at the **rostral pole**, and **large
    saccades** to the **far right periphery** at the **caudal
    pole**. **The motor map is ALIGNED with the retinotopic map** —
    a given collicular location encodes a **saccade to the
    corresponding location in the right visual field**. This is the
    **sensorimotor transformation** — the SC **transforms a visual
    location into a saccade command**.

**The alignment is the SC's core computation:** the **superficial
layers** see a **visual target** at a **given location** in the
**right visual field**; the **intermediate layers** at the **same
collicular location** generate a **saccade command** to that
location. **The retinotopic and motor maps are the same map** — a
**visual map** in the superficial layers and a **saccade map** in the
deeper layers, **aligned** at the same collicular coordinates.

**The left SC's maps are CONTRALATERAL** — the **left SC
represents the right visual field** and **generates rightward
saccades**. **A consumer that assumes "left SC = left visual
field" is WRONG** — the **left SC represents the right visual
field**, and a **left SC lesion** produces **subtle deficits** in
**rightward saccades** and **right visual field orienting**. This is
the **key asymmetric fact** the mirror leaf must flip.

The Fixation Zone (rostral SC) and the Saccade Zone (caudal SC)
-------------------------------------------------------------
The SC has a **rostrocaudal functional gradient** — the **rostral
pole** is the **fixation zone**; the **caudal pole** is the
**saccade zone**:

*   **Fixation Zone (rostral SC)** — the **rostral pole** of the SC
    is activated during **visual fixation** — when the eyes
    **hold** on a **foveal target**. It **inhibits saccade
    generation** and **maintains fixation** on the current target.
    **The fixation zone is present on BOTH SCs** — **each SC** has
    a **rostral fixation zone** — and the **two fixation zones**
    work **together** to **maintain binocular fixation**. **The
    fixation zone is a BILATERAL function** — **not a
    contralateral asymmetry**.

*   **Saccade Zone (caudal SC)** — the **caudal pole** of the SC
    is activated during **saccade generation** — when the eyes
    **move** to a **new target** in the **peripheral** visual
    field. It **generates a saccade command** to that target. **The
    saccade zone is CONTRALATERAL** — the **left SC's caudal
    pole** generates **rightward** saccades; the **right SC's
    caudal pole** generates **leftward** saccades. **The saccade
    zone is the contralateral asymmetry** — the **fixation zone is
    the bilateral component**.

**The rostrocaudal gradient is the SC's functional map** — it
encodes **where to look** (the **saccade command**) and **where to
hold** (the **fixation command**). **The two commands are in a
dynamic balance** — the **SC** continuously **decides** whether to
**hold fixation** (rostral) or **make a saccade** (caudal).

Multisensory Integration (the SC's sensorimotor integration
function)
-----------------------------------------------------------------
The **deep layers** of the left SC are **multisensory** — they
receive **visual**, **auditory**, and **somatosensory** input, and
they **integrate** them into a **common orienting map**. **The
integration is the SC's key sensorimotor function:**

*   **Visual input** — from the **superficial layers** (retinal and
    corticotectal) — the **visual map** of the **right visual
    field**.

*   **Auditory input** — from the **left inferior colliculus** (via
    the **brachium of the IC**) and the **auditory cortex** — the
    **auditory space map** of the **right** and **left** auditory
    hemifields (the **left IC** projects to the **left SC**, but
    the auditory map in the SC is **aligned** with the visual map —
    the **auditory space map** is **contralateral** to match the
    **visual map**).

*   **Somatosensory input** — from the **spinal cord** and the
    **trigeminal system** — the **somatosensory map** of the
    **body surface** and the **face**.

**The three maps are aligned in the deep layers** — a given
collicular location represents a **common point** in **visual,
auditory, and somatosensory space**. This is the **multisensory
integration** — the SC **integrates** the three modalities into a
**common orienting command**. **A visual stimulus, an auditory
stimulus, or a somatosensory stimulus at the same location** in
space **activates the same collicular location** — producing the
**same orienting response**.

**The multisensory integration is a SUPERADDITIVE effect** — a
**combined visual + auditory stimulus** produces a **stronger SC
response** than **either alone** — the **neural substrate** of
**multisensory enhancement** in orienting behavior.

The Saccade Hierarchy (the SC's place in the hierarchy)
-------------------------------------------------------
The **saccade hierarchy** is the **functional context** for the SC.
It is a **hierarchy** with the SC at the **command level**:

*   **SC (command level)** — the **superior colliculus** —
    **sensorimotor integration** — receives **visual, auditory, and
    somatosensory** input and generates **saccade commands** in a
    **motor map**. **The SC is at the TOP of the saccade
    hierarchy.**

*   **PPRF / riMLF (premotor level)** — the **paramedian pontine
    reticular formation** (horizontal saccades) and the **rostral
    interstitial nucleus of the MLF** (vertical saccades) —
    **premotor saccade generators** — they **transform** the SC's
    saccade command into the **premotor saccade signal** that
    drives the CN nuclei. **The PPRF and riMLF are DOWNSTREAM of
    the SC.**

*   **CN III / IV / VI nuclei (motor level)** — the **oculomotor
    nucleus** (CN III), the **trochlear nucleus** (CN IV), and the
    **abducens nucleus** (CN VI) — **motor nuclei** — they
    **execute** the saccade by driving the **extraocular muscles**.
    **The CN nuclei are DOWNSTREAM of the PPRF / riMLF.**

*   **Extraocular muscles (effector level)** — the **six
    extraocular muscles** per eye — **the effectors** of the
    saccade. **The muscles are DOWNSTREAM of the CN nuclei.**

**The SC is NOT the PPRF, the riMLF, or the CN nuclei** — it is
**UPSTREAM of them** in the saccade hierarchy. **The SC decides; the
PPRF/riMLF execute; the CN nuclei drive; the muscles move.** **Each
level is a different structure** — the SC is a **sensorimotor
integration** structure; the PPRF/riMLF are **premotor saccade
generators**; the CN nuclei are **motor nuclei**; the muscles are
**effectors**. **All four levels carry NO coupling warning** — same
rule, different structures.

**The SC's saccade command** is carried to the **PPRF** and
**riMLF** by the **tectoreticular** pathway (a subset of the
**tectobulbar tract**) — a **conduction pathway** — and to the
**CN nuclei** (and other targets) by the **tectobulbar tract** —
also a **conduction pathway**. **The tectobulbar and tectoreticular
tracts are the SC's OUTPUT** — they are **conduction pathways**,
not part of the SC itself.

The Visual Grasp Reflex (a functional context for the SC)
--------------------------------------------------------
The **visual grasp reflex** — also called the **visual orienting
reflex** — is a **primitive reflex** in which a **visual stimulus**
in the **peripheral visual field** **triggers** a **saccade** toward
it (and, in some contexts, a **grasp** or **orienting** response).
**The SC is the KEY SUBSTRATE of this reflex:**

*   **Reflex arc** — a **visual stimulus** in the **peripheral
    visual field** → **retina** → **optic nerve** → **brachium of
    the SC** → **superficial layers of the SC** → **deep layers of
    the SC** → **tectoreticular pathway** → **PPRF / riMLF** →
    **CN III/IV/VI nuclei** → **extraocular muscles** → **saccade
    toward the stimulus**.

*   **In INFANTS** — the **visual grasp reflex is PRESENT** — a
    **normal developmental stage**.

*   **In ADULTS** — the reflex is **SUPPRESSED** by **cortical
    inhibition** — the **frontal eye fields** (FEF) and the
    **prefrontal cortex** **inhibit** the SC's reflex to allow
    **voluntary** saccade control. **A FRONTAL LOBE LESION**
    **releases** the reflex — producing the **clinical "visual
    grasp reflex"** — the patient's eyes are **involuntarily drawn**
    to **visual stimuli** in the **peripheral field**. **The SC is
    the reflex's substrate; the cortex is the suppressor.**

**The visual grasp reflex is a FUNCTIONAL CONTEXT for the SC** — it
is **not the SC itself** and it is **not a structural child**. The
**reflex** is a **physiological entity** — the **SC** is its
**neural substrate**. Consumers must **not** conflate the SC with
the reflex, and must **not** resolve the reflex through the SC
path.

The Left Superior Colliculus / Left Inferior Colliculus Boundary
----------------------------------------------------------------
This is the **sensorimotor integration / sensory relay** boundary
within the left tectum:

*   **Left superior colliculus** (this module) — the **sensorimotor
    integration / saccade command generator** — **rostral** — at
    the **oculomotor / EW / mesV level**.

*   **Left inferior colliculus**
    (``.../tectum/left/inferior_colliculus/`` **and**
    ``.../tectum/corpora_quadrigemina/left/inferior_colliculus/``)
    — the **auditory relay** — **caudal** — at the **trochlear
    level**.

**They are DIFFERENT FUNCTIONAL CLASSES of colliculus** — the
**SC** is a **sensorimotor integration** structure; the **IC** is a
**sensory relay**. **Both carry NO coupling warning** — but for
**different reasons**. **The IC projects to the SC** (for
**auditory orienting** and **audiovisual integration**) — the **IC
is UPSTREAM of the SC's auditory input**. Consumers must **not**
conflate the two.

The Left Superior Colliculus / PPRF and riMLF Boundary
------------------------------------------------------
This is the **command / premotor** boundary:

*   **Left superior colliculus** (this module) — the **saccade
    command generator** — **mesencephalic** — **command level**.

*   **PPRF** (``.../hindbrain/metencephalon/pons/pprf/``) and
    **riMLF** (``.../midbrain/tegmentum/left/riMLF/``) — the
    **premotor saccade generators** — **pontine / mesencephalic**
    — **premotor level**.

**The SC is UPSTREAM of the PPRF and the riMLF** — the **SC
decides; the PPRF/riMLF execute**. **They are DIFFERENT STRUCTURES
at DIFFERENT levels** of the saccade hierarchy. Consumers must
**not** conflate the SC with the PPRF or the riMLF.

The Left Superior Colliculus / CN III/IV/VI Nuclei Boundary
-----------------------------------------------------------
This is the **command / motor** boundary:

*   **Left superior colliculus** (this module) — the **saccade
    command generator** — **tectum**.

*   **CN III/IV/VI nuclei** — the **motor nuclei** — **tegmentum**
    (CN III, IV) / **pons** (CN VI).

**The SC DRIVES the CN nuclei indirectly** (via the PPRF, riMLF,
and the tectobulbar tract) — but the **SC is not the CN nuclei**.
**They are DIFFERENT STRUCTURES at DIFFERENT levels** of the
saccade hierarchy. Consumers must **not** conflate the SC with the
CN nuclei.

The Left Superior Colliculus / LGN Boundary
-------------------------------------------
This is the **sensorimotor integration / visual thalamic relay**
boundary:

*   **Left superior colliculus** (this module) — **mesencephalic**
    — **orienting**.

*   **Left lateral geniculate body (LGN)**
    (``.../forebrain/diencephalon/thalamus/lateral_geniculate_body/``)
    — **diencephalic** — **conscious vision** (V1).

**The SC does NOT project to the LGN** — it projects to the
**pulvinar** (visual attention). **They are DIFFERENT STRUCTURES in
DIFFERENT functional systems**. Consumers must **not** conflate the
SC with the LGN.

The Left Superior Colliculus / Pulvinar Boundary
------------------------------------------------
This is the **midbrain orienting / thalamic visual attention**
boundary:

*   **Left superior colliculus** (this module) — **mesencephalic**
    — **orienting**.

*   **Pulvinar** (``.../forebrain/diencephalon/thalamus/pulvinar/``)
    — **diencephalic** — **visual attention**.

**The SC projects to the pulvinar** (via the **brachium of the
SC** and the **tectothalamic** pathway) for **visual attention**.
**They are DIFFERENT STRUCTURES** — the **pulvinar** is
**diencephalic**; the **SC** is **mesencephalic**. Consumers must
**not** conflate the SC with the pulvinar.

The Left Superior Colliculus / Pretectum Boundary
-------------------------------------------------
This is the **saccadic / pupillary-optokinetic** boundary:

*   **Left superior colliculus** (this module) — **saccadic and
    orienting** — **rostral colliculus**.

*   **Pretectum** (``.../midbrain/pretectum/``) — **pupillary and
    optokinetic** — **diencephalon-midbrain junction** — **rostral
    to the SC**.

**They are DIFFERENT REGIONS in DIFFERENT functional systems.**
Consumers must **not** conflate the SC with the pretectum.

The Left Superior Colliculus / PAG Boundary
-------------------------------------------
This is the **orienting / defensive** boundary:

*   **Left superior colliculus** (this module) — **tectum** —
    **orienting**.

*   **Left periaqueductal gray (PAG)**
    (``.../tegmentum/left/periaqueductal_gray/``) — **tegmentum** —
    **pain modulation and defensive behavior**.

**The SC projects to the PAG** (via the **tectotegmental**
pathway) for **defensive behaviors** — but the **PAG is not the
SC**. **They are DIFFERENT STRUCTURES** — the **PAG** is
**tegmentum**; the **SC** is **tectum**. Consumers must **not**
conflate the SC with the PAG.

The Left Superior Colliculus / FEF Boundary
-------------------------------------------
This is the **midbrain / cortical** saccade control boundary:

*   **Left superior colliculus** (this module) — **midbrain** —
    **reflexive and voluntary** saccade command (via cortical
    input).

*   **Left frontal eye field (FEF)**
    (``.../forebrain/telencephalon/cortex/frontal/frontal_eye_field/``)
    — **cortical** — **voluntary** saccade control.

**The FEF projects to the SC** (via the **corticotectal** pathway)
for **voluntary saccades** and to the **PPRF** (via the
**corticoreticular** pathway) for **voluntary horizontal
saccades**. **The FEF is the cortical command; the SC is the
midbrain command.** They are **DIFFERENT STRUCTURES at DIFFERENT
levels** of the saccade system. Consumers must **not** conflate the
SC with the FEF.

The Left Superior Colliculus / SNr Boundary
-------------------------------------------
This is the **excitatory / inhibitory** saccade control boundary:

*   **Left superior colliculus** (this module) — **excitatory** —
    **saccade command generator**.

*   **Left substantia nigra pars reticulata (SNr)**
    (``.../midbrain/tegmentum/left/substantia_nigra/pars_reticulata/``)
    — **inhibitory** — **tonic inhibition of saccade
    generation**.

**The SNr projects to the SC** (via the **nigrotectal** pathway) —
it **tonically inhibits** the SC's saccade generator. **The SNr is
the inhibitory gate; the SC is the command generator.** They are
**DIFFERENT STRUCTURES** — the **SNr** is **tegmentum**; the **SC**
is **tectum**. Consumers must **not** conflate the SC with the SNr.

The Left Superior Colliculus / Fastigial Nucleus Boundary
---------------------------------------------------------
This is the **midbrain / cerebellar** saccade control boundary:

*   **Left superior colliculus** (this module) — **midbrain** —
    **saccade command generator**.

*   **Fastigial nucleus**
    (``.../hindbrain/metencephalon/cerebellum/deep_cerebellar_nuclei/
    fastigial_nucleus/``) — **cerebellar** — **saccade adaptation
    and accuracy**.

**The fastigial nucleus projects to the SC** (via the
**cerebellotectal** pathway) for **saccade adaptation** — but the
**fastigial nucleus is not the SC**. **They are DIFFERENT
STRUCTURES** — the **fastigial** is **cerebellar**; the **SC** is
**mesencephalic**. Consumers must **not** conflate the SC with the
fastigial nucleus.

The Left Superior Colliculus / Brachium of the SC and Tectobulbar
Tract Boundary
----------------------------------------------------------------
This is the **nucleus / conduction pathway** boundary:

*   **Left superior colliculus** (this module) — the **nucleus** —
    **grey matter**.

*   **Left brachium of the SC (BSC)** — the **conduction pathway**
    — **white matter** — that carries **retinal input** to the SC
    and **visual attention output** from the SC to the pulvinar.

*   **Tectobulbar tract** — the **descending conduction pathway** —
    **white matter** — that carries the SC's saccade command to the
    **PPRF**, **riMLF**, and **CN nuclei**.

*   **Tectoreticular pathway** — a **subset of the tectobulbar
    tract** — carries the SC's command to the **PPRF** (horizontal
    saccades) and the **riMLF** (vertical saccades).

**The SC is the NUCLEUS** — **grey matter**. **The BSC, the
tectobulbar tract, and the tectoreticular pathway are CONDUCTION
PATHWAYS** — **white matter**. **They are DIFFERENT STRUCTURES** —
the **conduction pathways** connect the SC to its upstream and
downstream targets. Consumers must **not** conflate the SC with
these conduction pathways.

The Left Superior Colliculus / Right Superior Colliculus Boundary
-----------------------------------------------------------------
This is the **side** boundary — **paired sensorimotor integration
structures**, **CONTRALATERAL maps**, **NO coupling warning**:

*   **Left superior colliculus** (this module) — the **left
    sensorimotor integration** structure — **right visual field /
    rightward saccade** map.

*   **Right superior colliculus**
    (``.../tectum/right/superior_colliculus/`` **and**
    ``.../tectum/corpora_quadrigemina/right/superior_colliculus/``)
    — the **right sensorimotor integration** structure — **left
    visual field / leftward saccade** map.

**They are BILATERALLY SYMMETRIC PAIRED SENSORIMOTOR INTEGRATION
STRUCTURES in their cell-body locations and layered organization**
— **but their RETINOTOPIC AND MOTOR MAPS ARE CONTRALATERAL**.
**The left SC represents the RIGHT visual field and generates
RIGHTWARD saccades; the right SC represents the LEFT visual field
and generates LEFTWARD saccades.** This is the **DEFINING ASYMMETRY**
of the SC pair. **A consumer that assumes "left SC = right SC" will
be structurally correct in cell-body location and layered
organization** — but **WRONG** if they assume the two SCs
**represent the same visual field** or **generate the same saccade
direction**. The **two SCs** are **independent paired structures**
— with **contralateral maps** — and **bilateral output** to the
**PPRF**, **riMLF**, and **CN nuclei**. **They carry NO coupling
warning** — the **bilateral output** is a **downstream projection**
to **bilateral targets**, not intrinsic coupling. See
*Lateralization Notes*.

Function in the Human Brain
---------------------------
The left superior colliculus's function is **sensorimotor
integration** for **saccade generation** and **visual/oculomotor
orienting** — **NOT** conscious vision (that is the **LGN**), **NOT**
pupillary or optokinetic (that is the **pretectum**), **NOT**
auditory relay (that is the **IC**), **NOT** premotor saccade
generation (that is the **PPRF**/**riMLF**), **NOT** motor execution
(that is the **CN III/IV/VI nuclei**):

*   **Visual Orienting (the visual grasp reflex):** The left SC
    receives **visual input** from the **right visual field**
    (superficial layers) and generates a **saccade command** to
    that location (intermediate layers). The **visual grasp
    reflex** — the **automatic orienting toward a peripheral
    visual stimulus** — is mediated by the SC. In **adults**, the
    reflex is **suppressed** by **frontal cortical inhibition**;
    in **frontal lobe lesions**, the reflex is **released**.

*   **Auditory Orienting (multisensory orienting):** The left SC
    receives **auditory input** from the **left IC** (and the
    **auditory cortex**) — the **auditory space map** aligned with
    the **visual map** — and generates **saccades** toward
    **auditory targets**. The **IC → SC** projection is the
    **substrate** of **auditory orienting** and **audiovisual
    integration**.

*   **Somatosensory Orienting (multisensory orienting):** The left
    SC receives **somatosensory input** from the **spinal cord**
    and the **trigeminal system** — the **somatosensory map**
    aligned with the **visual and auditory maps** — and generates
    **saccades** toward **somatosensory targets**.

*   **Saccade Generation (the command level):** The left SC
    **generates saccade commands** in the **motor map** of the
    intermediate/deep layers — the **top level** of the **saccade
    hierarchy**. The **command** is carried by the
    **tectoreticular** pathway to the **PPRF** (horizontal) and the
    **riMLF** (vertical), and by the **tectobulbar** tract to the
    **CN III/IV/VI nuclei**. **The SC decides; the PPRF/riMLF
    execute.**

*   **Fixation Maintenance (the fixation zone):** The **rostral
    pole** of the left SC — the **fixation zone** — **maintains
    fixation** on a **foveal target** and **inhibits saccade
    generation**. **The fixation zone is BILATERAL** — **each
    SC** has a **fixation zone** — and the **two fixation
    zones** work together to **maintain binocular fixation**.

*   **Visual Attention (via the pulvinar):** The left SC projects
    to the **pulvinar** (via the **brachium of the SC** and the
    **tectothalamic** pathway) for **visual attention** —
    **covert attention** to a **visual location** before a
    **saccade** or **without a saccade**.

*   **Saccade Adaptation (via the cerebellum):** The left SC
    receives **cerebellar input** from the **fastigial nucleus**
    (via the **cerebellotectal** pathway) for **saccade
    adaptation** — the **adjustment** of **saccade amplitude**
    based on **visual error** (e.g., **prism adaptation**,
    **muscle weakness adaptation**).

*   **NOT conscious vision.** The **LGN** and the **visual cortex**
    mediate **conscious vision**; the **SC** mediates **reflexive
    orienting** and **saccade generation**.

*   **NOT pupillary or optokinetic.** The **pretectum** mediates
    the **pupillary light reflex** and the **optokinetic
    nystagmus**; the **SC** mediates **saccades**.

*   **NOT an oscillator.** The **SC** is a **sensorimotor
    integration** structure — it does **not** generate a rhythm.
    **Sensorimotor integration structures carry NO coupling
    warning** — same rule as every non-oscillator class.

**The unifying theme:** the left SC is the **left sensorimotor
integration** structure — the **saccade command generator** and the
**visual/oculomotor orienting** structure — that **integrates**
**visual, auditory, and somatosensory** input into a **common
orienting map**. It is the **top level** of the **saccade
hierarchy** — **NOT** the premotor saccade generators (**PPRF**,
**riMLF**), **NOT** the motor nuclei (**CN III/IV/VI**), and **NOT**
the effector (**extraocular muscles**). It is **NOT** a sensory
relay (**IC**), **NOT** the visual thalamic relay (**LGN**), and
**NOT** the pupillary-optokinetic region (**pretectum**). It has
**CONTRALATERAL retinotopic and motor maps** — the **left SC
represents the RIGHT visual field** and **generates RIGHTWARD
saccades** — and it carries **NO coupling warning**.

Associated Disorders
--------------------
The left superior colliculus has **no named syndrome of its own** —
its clinical associations are **direct** but usually **not
localizing** — the SC is **rarely** the **sole** site of pathology,
and its lesions are usually **compensated** by the **contralateral
SC** and by the **cortical** and **cerebellar** saccade control
systems:

*   **Visual Grasp Reflex (RELEASED by FRONTAL LOBE LESIONS — the SC
    is the SUBSTRATE, not the lesion site):** The **visual grasp
    reflex** — the **involuntary visual orienting** toward a
    **peripheral stimulus** — is **normal** in **infants** and
    **suppressed** in **adults** by **frontal cortical
    inhibition**. **A frontal lobe lesion** (FEF, prefrontal
    cortex) **releases** the reflex — producing the **clinical
    "visual grasp reflex"** — but the **lesion site is the
    FRONTAL LOBE**, not the **SC**. **The SC is the reflex's
    substrate — the cortex is the suppressor.** A **consumer that
    attributes the released reflex to an SC lesion is WRONG** —
    the **releasing lesion is cortical**; the **SC is downstream**.

*   **Unilateral SC Lesion (COMPENSATED — subtle deficits):** A
    **focal lesion** of the **left SC** — from **small
    infarction**, **demyelination** (e.g., **multiple sclerosis**),
    or **tumor** — would produce **subtle deficits** in
    **rightward saccades** (the **contralateral** direction) and in
    **right visual field orienting** — because the **left SC**
    represents the **right visual field** and generates **rightward
    saccades**. **The deficits are usually COMPENSATED** by the
    **right SC** (which also projects **bilaterally** to the
    PPRF/riMLF/CN nuclei) and by the **cortical** (FEF) and
    **cerebellar** saccade systems. **Profound saccade palsy from
    a unilateral SC lesion is RARE.**

*   **Bilateral SC Lesions (rare — usually part of a broader
    brainstem process):** **Bilateral SC lesions** — from
    **brainstem stroke**, **demyelination**, **tumor**, or
    **trauma** — would produce **more significant saccade
    deficits** (e.g., **impaired saccade initiation**, **slowed
    saccades**, **impaired visual grasp**) — usually part of a
    **broader brainstem syndrome** (e.g., **locked-in syndrome**,
    **brainstem encephalitis**, **dorsal midbrain syndrome**), not
    an **isolated SC syndrome**.

*   **Progressive Supranuclear Palsy (PSP — the SC is ATROPHIED, but
    the PRIMARY substrate is the SNr and the midbrain tegmentum):**
    **PSP** involves **SC atrophy** (visible on MRI) — but the
    **primary** substrates of the **supranuclear gaze palsy** are
    the **SNr** (the **inhibitory gate** on the SC), the
    **riMLF** (vertical saccade generator), and the **midbrain
    tegmentum** more broadly. **The SC atrophy is PART of the
    broader degeneration — NOT the primary cause of the
    supranuclear gaze palsy.** A **consumer that attributes PSP's
    gaze palsy to the SC alone is WRONG** — the **SNr** and the
    **riMLF** are the **primary** substrates.

*   **Parinaud Syndrome (DORSAL MIDBRAIN SYNDROME — the SC is
    ADJACENT, but the PRIMARY substrates are the PRETECTUM and the
    POSTERIOR COMMISSURE):** **Parinaud syndrome** — **upgaze
    palsy**, **convergence-retraction nystagmus**,
    **light-near dissociation**, **Collier sign** (eyelid
    retraction) — is a **dorsal midbrain syndrome** whose
    **primary** substrates are the **pretectum** (the **light-near
    dissociation**), the **posterior commissure** (the **upgaze
    palsy** — the crossing fibers from the **riMLF**), and the
    **posterior thalamus** (the **Collier sign**). **The SC is
    ADJACENT** — the **dorsal midbrain lesion** may involve the
    **SC** — but the **primary** substrates are the
    **pretectum**, the **posterior commissure**, and the
    **thalamus**. **The SC is NOT the primary substrate of
    Parinaud syndrome.** See ``.../midbrain/pretectum/`` for the
    **primary** substrates.

*   **Oculomotor Apraxia / Cogan Syndrome (CORTICAL — the SC is
    SPARED):** **Oculomotor apraxia** — **impaired voluntary
    saccades** with **preserved reflexive saccades** — is a
    **cortical** disorder (FEF, parietal cortex, or their
    connections). **The SC is SPARED** — the **reflexive
    saccades** (mediated by the SC) **remain intact**, while the
    **voluntary saccades** (mediated by the FEF) are **impaired**.
    **A consumer that attributes oculomotor apraxia to the SC is
    WRONG** — the **SC's reflexive pathway is the SPARED
    component**; the **cortical voluntary pathway is the impaired
    component**.

*   **Tectal Glioma (DORSAL MIDBRAIN TUMOR — the SC is ADJACENT,
    but the clinical syndrome is the PRETECTUM / POSTERIOR
    COMMISSURE / CEREBRAL AQUEDUCT involvement):** **Tectal
    gliomas** — **dorsal midbrain tumors** — can produce
    **Parinaud syndrome** (via **pretectal / posterior commissure**
    involvement) and **hydrocephalus** (via **cerebral aqueduct**
    compression). **The SC is the ADJACENT structure** — the
    **tumor** may **involve** the **SC** — but the **clinical
    syndrome** is the **dorsal midbrain syndrome**, not an
    **isolated SC syndrome**.

*   **No Named "Superior Colliculus Syndrome":** The left SC is a
    **sensorimotor integration** structure — its **isolated
    lesion** produces **subtle saccade and orienting deficits**
    (usually **compensated**) — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** but **usually
    not localizing** — most saccade and orienting clinical
    syndromes are **cortical** (FEF, parietal), **pretectal**
    (Parinaud), **cerebellar** (saccade adaptation), or **basal
    ganglia** (PSP) — not **SC** lesions.

**What is NOT here:** The left SC is **not** the substrate for
**conscious vision** (the **LGN** and the **visual cortex** —
**NOT** the SC), **pupillary light reflex deficits** (the
**pretectum** and the **EW nucleus** — **NOT** the SC),
**optokinetic nystagmus deficits** (the **pretectum** and the
**nucleus of the optic tract** — **NOT** the SC), **Parinaud
syndrome as an SC-specific syndrome** (the **pretectum** and the
**posterior commissure** are the **primary** substrates; the SC is
**adjacent**), **PSP gaze palsy as an SC-specific syndrome** (the
**SNr** and the **riMLF** are the **primary** substrates; the SC
is **atrophied** as part of **broader degeneration**),
**oculomotor apraxia** (a **cortical** FEF disorder — the **SC is
spared**), **visual grasp reflex as an SC lesion sign** (the
**releasing lesion** is **frontal cortical**; the SC is the
**substrate**), **internuclear ophthalmoplegia** (the **MLF** —
**NOT** the SC), **horizontal or vertical gaze palsy** (the
**PPRF** and the **riMLF** — **NOT** the SC), **myasthenia gravis**
(NMJ — **NOT** the SC), **Weber syndrome** (crus cerebri — CN III —
**NOT** the SC), **Benedikt / Claude / Nothnagel syndromes**
(tegmentum — CN III + red nucleus / cerebellar — **NOT** the SC),
**CCHS** (RTN), **OIRD** (pre-Bötzinger complex — NK1R neurons),
**Rett syndrome** (pre-Bötzinger complex), **SIDS** (proposed —
pre-Bötzinger complex + arcuate nucleus), **essential hypertension
/ sympathetic overactivity** (C1 group / RVLM), **Parkinson's
disease** (substantia nigra — tegmentum), **Huntington's disease**
(striatum — telencephalon), or **Kluver-Bucy syndrome** (amygdala).
Its clinical relevance is **direct** but **usually not localizing**
— most saccade and orienting clinical syndromes are **cortical**,
**pretectal**, **cerebellar**, or **basal ganglia** — not **SC**
lesions. **No named superior colliculus syndrome exists.**

Lateralization Notes
--------------------
This is the **left** superior colliculus leaf. The left and right
SCs are **bilaterally symmetric paired sensorimotor integration
structures** in their **cell-body locations** and **layered
organization** — but their **retinotopic and motor maps are
CONTRALATERAL** — and they carry **NO coupling warning**:

*   **Bilateral Paired Sensorimotor Integration Structures:** Each
    side has its own SC — each is an **independent midbrain
    sensorimotor integration structure**.

*   **CONTRALATERAL RETINOTOPIC MAP — the key asymmetric fact:**
    The **left SC** represents the **RIGHT visual field** — the
    **superficial layers** receive **direct retinal input** from
    the **right (contralateral) visual field** (via the **crossed
    nasal retinal fibers** and the **brachium of the SC**) and
    **corticotectal input** from the **left V1** (which also
    represents the **right visual field**). **The right SC**
    represents the **LEFT visual field**. **A consumer that
    assumes "left SC = left visual field" is WRONG** — the
    **left SC represents the right visual field**.

*   **CONTRALATERAL MOTOR MAP — the key asymmetric fact:** The
    **left SC** generates **RIGHTWARD (contralateral) saccades** —
    the **intermediate layers** contain a **motor map** aligned
    with the **retinotopic map** — a given collicular location
    encodes a **saccade to the corresponding location in the right
    visual field**, i.e., a **rightward saccade**. **The right SC**
    generates **LEFTWARD saccades**. **A consumer that assumes
    "left SC = leftward saccades" is WRONG** — the **left SC
    generates rightward saccades**.

*   **Fixation Zone — BILATERAL:** The **rostral pole** of **each**
    SC is the **fixation zone** — it **maintains fixation** on a
    **foveal target** and **inhibits saccade generation**. **The
    fixation zone is a BILATERAL function** — **each SC** has a
    **fixation zone** — and the **two fixation zones** work
    together to **maintain binocular fixation**. **The fixation
    zone is NOT the contralateral asymmetry** — the
    **contralateral asymmetry** is in the **peripheral (saccade)
    map**.

*   **Bilateral Output (cross-midline):** Each SC projects
    **bilaterally** to the **PPRF**, **riMLF**, and **CN III/IV/VI
    nuclei** — via the **tectobulbar** and **tectoreticular**
    tracts — **but this bilateral output is a DOWNSTREAM
    projection** to **bilateral targets** — **not intrinsic
    left-right coupling** of the two SCs in the oscillator sense.
    **The two SCs are independent paired structures** — their
    **bilateral output** is a **conduction** to **bilateral
    targets**.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to SENSORIMOTOR INTEGRATION structures):**
    The **pre-Bötzinger complex** carries a **coupling warning**
    because it is an **oscillator** whose two sides must
    synchronize to produce a single rhythm. The **left SC** is a
    **sensorimotor integration** structure — it does **not**
    generate a rhythm, so it does **not** carry the **oscillator
    coupling warning**. Its **left** and **right** sides are
    **independent sensorimotor integration structures** — there is
    **no** SC-to-SC coupling in the oscillator sense.
    **Sensorimotor integration structures carry NO coupling
    warning** — same rule as motor nuclei, premotor pools, sensor
    nuclei, relay nuclei, and conduction pathways.

*   **Clinical Laterality — the contralateral deficit pattern:**
    *   A **left SC lesion** → **subtle deficits** in
        **rightward saccades** and **right visual field
        orienting** — because the **left SC** represents the
        **right visual field** and generates **rightward
        saccades**. **Usually COMPENSATED** by the **right SC**
        and by the **cortical** (FEF) and **cerebellar** saccade
        systems. **Profound saccade palsy is RARE.**
    *   A **right SC lesion** → **subtle deficits** in
        **leftward saccades** and **left visual field
        orienting**.
    *   **A consumer that assumes "left SC lesion = left visual
        field deficit" is WRONG** — the **left SC lesion**
        produces a **RIGHT visual field deficit** (the
        **contralateral** field).

**The left superior colliculus is a strict mirror pair with the
right SC in cell-body location and layered organization** — **no
coupling warning, no SLEA warning, no amygdala-lateralization
warning, and no rhinencephalon-exclusion flag** — **but with a
crucial caveat**: the **retinotopic and motor maps are
CONTRALATERAL** — the **left SC** represents the **right visual
field** and generates **rightward saccades**, and the **right SC**
represents the **left visual field** and generates **leftward
saccades**. **The fixation zone is BILATERAL** — **each SC** has a
**fixation zone** — and the **two fixation zones** work together.
**The two SCs are exact mirrors in cell-body location and layered
organization — but their functional maps are CONTRALATERAL, not
mirror-symmetric.** See *Design Contract*.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only — **no** import
    from ``.../right/superior_colliculus/``.
*   **No cross-lobe imports.** This module does **not** import from
    the **retina**, the **LGN**, the **V1**, the **FEF**, the
    **PPRF**, the **riMLF**, the **CN III/IV/VI nuclei**, the
    **IC**, the **pretectum**, the **PAG**, the **pulvinar**, the
    **SNr**, the **fastigial nucleus**, the **brachium of the SC**,
    the **tectobulbar tract**, the **tectoreticular pathway**, or
    any other container. The left SC's relationships to the retina,
    the LGN, V1, the FEF, the PPRF, the riMLF, the CN III/IV/VI
    nuclei, the IC, the pretectum, the PAG, the pulvinar, the SNr,
    the fastigial nucleus, the BSC, the tectobulbar tract, and the
    tectoreticular pathway are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **transmitter
    phenotypes** of the SC neurons (glutamatergic, GABAergic,
    cholinergic, dopaminergic subpopulations) are
    ``chemicals_hormones``-layer facts — documented as **prose**,
    **never imported**.
*   **DUAL-PATH LEAF — CROSS-LISTED between the modern path and the
    older-term path.** Both paths resolve to **this leaf**. The
    **modern path** is the **structural home** by naming convention
    — the **older-term path** is the **synonym alias**. Consumers
    resolve by **one** path per lookup.
*   **SENSORIMOTOR INTEGRATION — NOT a sensory relay.** The **IC**
    is the sensory relay (auditory); the **SC** is the
    **sensorimotor integration** structure. Different functional
    classes.
*   **COMMAND LEVEL of the saccade hierarchy — NOT a premotor
    saccade generator, NOT a motor nucleus.** The **saccade
    hierarchy** is: SC (command) → PPRF/riMLF (premotor) → CN
    III/IV/VI nuclei (motor) → extraocular muscles (effector).
    **The SC is UPSTREAM of all three downstream levels.**
*   **CONTRALATERAL RETINOTOPIC AND MOTOR MAPS — the defining
    asymmetric fact.** The **left SC** represents the **right
    visual field** and generates **rightward saccades**. The
    **right SC** represents the **left visual field** and
    generates **leftward saccades**. **A consumer that assumes
    "left SC = left visual field" is WRONG.**
*   **FIXATION ZONE — BILATERAL.** Each SC has a **fixation
    zone** — the **two fixation zones** work together to **maintain
    binocular fixation**. **The fixation zone is NOT the
    contralateral asymmetry.**
*   **MULTISENSORY INTEGRATION.** The deep layers integrate
    **visual, auditory, and somatosensory** input into a **common
    orienting map**.
*   **VISUAL GRASP REFLEX — the SC is the SUBSTRATE, the CORTEX is
    the SUPPRESSOR.** A **frontal lobe lesion** releases the
    reflex — **the SC is not the releasing lesion site**.
*   **NOT the LGN — the LGN is the thalamic visual relay to V1.**
*   **NOT the pulvinar — the pulvinar is the thalamic visual
    attention relay.** The SC projects to the pulvinar via the
    BSC.
*   **NOT the pretectum — the pretectum is pupillary and
    optokinetic.**
*   **NOT the PAG — the PAG is pain modulation and defensive
    behavior.**
*   **NOT the FEF — the FEF is the cortical voluntary saccade
    control.**
*   **NOT the SNr — the SNr is the basal ganglia inhibitory gate.**
*   **NOT the fastigial nucleus — the fastigial nucleus is the
    cerebellar saccade adaptation nucleus.**
*   **NOT the PPRF or riMLF — those are premotor saccade
    generators.**
*   **NOT the CN III/IV/VI nuclei — those are motor nuclei.**
*   **NOT the brachium of the SC, the tectobulbar tract, or the
    tectoreticular pathway — those are CONDUCTION PATHWAYS.**
*   **SENSORIMOTOR INTEGRATION STRUCTURES CARRY NO COUPLING
    WARNING.** Same rule as every non-oscillator class. The
    **bilateral** output of each SC is a **downstream projection**
    to **bilateral targets** — not intrinsic coupling.
*   **SIDE-CONSISTENT — this leaf is the LEFT superior colliculus.**
*   **MIRROR PARITY with ``.../right/superior_colliculus/`` —
    paired and symmetric in cell-body location and layered
    organization, with NO coupling warning** — **BUT with the
    CONTRALATERAL retinotopic and motor maps as the DEFINING
    ASYMMETRY.** The mirror is **NOT clean** — the
    **retinotopic/motor maps flip** (left SC → right field; right
    SC → left field). The **fixation zone is BILATERAL** — the
    **one component** that does **not** flip.
*   **CHEMICALS-LAYER DISCIPLINE.** The **transmitter phenotypes**
    of the SC neurons are ``chemicals_hormones``-layer facts —
    documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing
    (dual path) is **within the tectum** (``tectum/left`` ↔
    ``tectum/corpora_quadrigemina/left``) — not into the forebrain
    or hindbrain. The **LGN** and **pulvinar** (diencephalon), the
    **V1** and **FEF** (telencephalon), the **PPRF** (hindbrain),
    and the **fastigial nucleus** (cerebellum) are **separate
    structures** referenced as **prose**, not as cross-listed
    parents.
*   **No nested cross-listing.** The left SC is a **single
    dual-path leaf**. It is **not** a container.
*   **The on-disk tree is authoritative.** If the tree has **both**
    ``tectum/left/superior_colliculus/`` **and**
    ``tectum/corpora_quadrigemina/left/superior_colliculus/``, then
    the left SC is reachable by **either** path. If the tree has
    **only** one of the two, that is the **sole** path — but the
    leaf is still the **same left superior colliculus**.

Usage
-----
Resolve the leaf by **either** path (they are equivalent — **this is
a dual-path anchor**)::

    # Modern path (structural home by naming convention):
    from infrastructure.brainparts.midbrain.tectum.left import superior_colliculus

    # Older-term path (this module — older-term alias):
    from infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.left import superior_colliculus

Or by fully-qualified path string::

    modern_path = (
        "midbrain.tectum.left.superior_colliculus"
    )
    older_term_path = (
        "midbrain.tectum.corpora_quadrigemina.left.superior_colliculus"
    )
    # Both resolve to THIS module.

**Do not** assume the two paths lead to **different structures** —
they lead to **one leaf**, cross-listed.

**Do not** assume the left superior colliculus is the **left
inferior colliculus**. The **SC** is the sensorimotor integration /
saccade command generator; the **IC** is the **auditory relay**.
**Different functional classes** — both carry **NO coupling
warning**, but for **different reasons**.

**Do not** assume the left superior colliculus is the **left lateral
geniculate body** (LGN). The **LGN** is the thalamic visual relay to
**V1** — **diencephalic** — **conscious vision**. The **SC** is the
midbrain **orienting** structure. **Different structures, different
functional systems.**

**Do not** assume the left superior colliculus is the **pulvinar**.
The **pulvinar** is the thalamic visual **attention** relay —
**diencephalic**. The **SC** **projects** to it, but **is not it**.

**Do not** assume the left superior colliculus is the **pretectum**.
The **pretectum** is **pupillary and optokinetic** — **rostral** to
the SC. **Different regions, different functional systems.**

**Do not** assume the left superior colliculus is the **PAG**. The
**PAG** is **pain modulation and defensive behavior** —
**tegmentum**. The **SC** **projects** to it, but **is not it**.

**Do not** assume the left superior colliculus is the **FEF**. The
**FEF** is the **cortical** voluntary saccade control region. The
**FEF** **projects** to the SC, but **is not it**.

**Do not** assume the left superior colliculus is the **SNr**. The
**SNr** is the **inhibitory gate** on the SC. **Different
structures** — the **SNr** is **tegmentum**; the **SC** is
**tectum**.

**Do not** assume the left superior colliculus is the **fastigial
nucleus**. The **fastigial nucleus** is the **cerebellar saccade
adaptation** nucleus. **Different structures** — the
**fastigial** is **cerebellar**; the **SC** is **mesencephalic**.

**Do not** assume the left superior colliculus is the **PPRF** or
the **riMLF**. Those are **premotor saccade generators** —
**downstream** of the SC in the saccade hierarchy.

**Do not** assume the left superior colliculus is the **CN III/IV/VI
nuclei**. Those are **motor nuclei** — **downstream** of the SC.

**Do not** assume the left superior colliculus is the **brachium of
the SC**, the **tectobulbar tract**, or the **tectoreticular
pathway**. Those are **conduction pathways** — **white matter**.
The **SC is a NUCLEUS** — **grey matter**.

**Do not** assume the left SC represents the **LEFT visual field**.
The **left SC represents the RIGHT visual field** (the
**contralateral** field) — and generates **RIGHTWARD saccades**.
**A consumer that assumes "left SC = left visual field" is
WRONG** — this is the **defining asymmetric fact** of the SC pair.

**Do not** assume a **left SC lesion** produces a **LEFT visual
field deficit**. The **left SC lesion** produces a **RIGHT visual
field deficit** — the **contralateral** field — and **subtle
rightward saccade deficits**. **The deficit is CONTRALATERAL to the
lesion.**

**Do not** assume the left SC's **bilateral output** to the
**PPRF**, **riMLF**, and **CN nuclei** is **intrinsic left-right
coupling**. It is a **downstream projection** to **bilateral
targets** — **not** coupling in the oscillator sense. **The two
SCs are independent paired sensorimotor integration structures.**

**Do not** attribute **conscious vision** to the left superior
colliculus. **Conscious vision** is the **LGN and visual cortex**;
the **SC** is the **reflexive orienting** and **saccade
generation** structure.

**Do not** attribute **pupillary or optokinetic function** to the
left superior colliculus. Those are the **pretectum**.

**Do not** attribute the **visual grasp reflex** as a **sign of an
SC lesion**. The **releasing lesion** is **frontal cortical** —
the **SC is the substrate**, not the **lesion site**.

**Do not** attribute **Parinaud syndrome** or **PSP gaze palsy** to
the **SC as the primary substrate**. **Parinaud** — **pretectum**
and **posterior commissure** primary; **PSP** — **SNr** and
**riMLF** primary; **the SC is adjacent** or **atrophied as part of
broader degeneration**.

**Do not** import the **transmitter phenotypes** of the SC neurons
into the midbrain structural layer. Those are
**``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the left superior
colliculus. **Sensorimotor integration structures carry NO coupling
warning** — same rule as motor nuclei, premotor pools, sensor
nuclei, relay nuclei, and conduction pathways.

Iterating the left superior colliculus's (empty) children
(recommended consumer pattern)::

    SUPERIOR_COLLICULUS_LEFT_CHILDREN = ()
    # The left superior colliculus is a leaf. The layered
    # organization (superficial, intermediate, deep) is prose, not
    # modules. The retinotopic map, the motor map, and the
    # multisensory maps are prose, not modules. The inputs (retina,
    # V1, IC, auditory cortex, spinal cord, trigeminal system, FEF,
    # SNr, fastigial nucleus) and outputs (PPRF, riMLF, CN III/IV/VI
    # nuclei, pulvinar, pretectum, PAG, inferior olive) are prose,
    # not modules.

Reaching the modern path (recommended consumer pattern — the
STRUCTURAL HOME by naming convention)::

    # The modern path is the STRUCTURAL HOME of the left SC in
    # modern nomenclature — the term "tectum" is preferred to
    # "corpora quadrigemina":
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #
    # Both paths resolve to the SAME leaf — the cross-listing
    # mechanism.

Reaching the right superior colliculus (recommended consumer
pattern — the SIDE mirror, with the CONTRALATERAL maps as the
asymmetry)::

    # The right superior colliculus is the RIGHT sensorimotor
    # integration structure — the saccade command generator:
    #
    #   brainparts.midbrain.tectum.right.superior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.right.superior_colliculus
    #
    # The two SCs are PAIRED and SYMMETRIC in cell-body location
    # and layered organization. BUT their RETINOTOPIC AND MOTOR
    # MAPS ARE CONTRALATERAL:
    #   - LEFT SC represents the RIGHT visual field and generates
    #     RIGHTWARD saccades
    #   - RIGHT SC represents the LEFT visual field and generates
    #     LEFTWARD saccades
    #
    # The CONTRALATERAL maps are the DEFINING ASYMMETRY of the pair.
    # The FIXATION ZONE is BILATERAL — each SC has a fixation zone
    # — and the two fixation zones work together to maintain
    # binocular fixation.

Reaching the left inferior colliculus (recommended consumer
pattern — the SENSORY RELAY sibling, CAUDAL)::

    # The left inferior colliculus is the SENSORY RELAY / auditory
    # structure — CAUDAL to the SC — at the trochlear level:
    #
    #   brainparts.midbrain.tectum.left.inferior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.left.inferior_colliculus
    #
    # The SC and the IC are DIFFERENT FUNCTIONAL CLASSES of
    # colliculus — the SC is sensorimotor integration; the IC is a
    # sensory relay. The IC PROJECTS TO the SC (for auditory
    # orienting and audiovisual integration).

Reaching the PPRF (recommended consumer pattern — the HORIZONTAL
PREMOTOR saccade generator, DOWNSTREAM of the SC)::

    # The PPRF is the HORIZONTAL PREMOTOR SACCADE GENERATOR — a
    # pontine premotor structure, DOWNSTREAM of the SC in the
    # saccade hierarchy:
    #
    #   brainparts.hindbrain.metencephalon.pons.pprf
    #
    # The SC DECIDES; the PPRF EXECUTES. Different structures at
    # different levels.

Reaching the riMLF and the interstitial nucleus of Cajal
(recommended consumer pattern — the VERTICAL PREMOTOR saccade
generators, DOWNSTREAM of the SC)::

    # The riMLF and the interstitial nucleus of Cajal are VERTICAL
    # PREMOTOR SACCADE GENERATORS — premotor structures,
    # DOWNSTREAM of the SC:
    #
    #   brainparts.midbrain.tegmentum.left.riMLF
    #   brainparts.midbrain.tegmentum.left.interstitial_nucleus_of_cajal
    #
    # The SC DECIDES; the riMLF / interstitial nucleus of Cajal
    # EXECUTE. Different structures at different levels.

Reaching the CN III/IV/VI nuclei (recommended consumer pattern —
the MOTOR nuclei, DOWNSTREAM of the SC)::

    # The CN III/IV/VI nuclei are the MOTOR NUCLEI that execute the
    # saccade — DOWNSTREAM of the SC:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #
    # The SC DECIDES; the CN nuclei DRIVE the extraocular muscles.
    # Different structures at different levels.

Reaching the LGN and the pulvinar (recommended consumer pattern —
the THALAMIC relays, DIFFERENT functional systems)::

    # The LGN is the VISUAL THALAMIC RELAY to V1 (conscious
    # vision); the pulvinar is the VISUAL ATTENTION thalamic relay:
    #
    #   brainparts.forebrain.diencephalon.thalamus.lateral_geniculate_body
    #   brainparts.forebrain.diencephalon.thalamus.pulvinar
    #
    # The SC does NOT project to the LGN; it DOES project to the
    # pulvinar via the brachium of the SC. Different structures,
    # different functional systems.

Reaching the pretectum (recommended consumer pattern — the
PUPILLARY AND OPTOKINETIC region, ROSTRAL to the SC)::

    # The pretectum is a SEPARATE region at the diencephalon-midbrain
    # junction — ROSTRAL to the SC:
    #
    #   brainparts.midbrain.pretectum
    #
    # The pretectum is PUPILLARY AND OPTOKINETIC; the SC is SACCADIC
    # AND ORIENTING. Different regions, different functional
    # systems.

Reaching the FEF, the SNr, and the fastigial nucleus
(recommended consumer pattern — the SACCADE CONTROL systems,
DIFFERENT levels)::

    # The FEF (cortical voluntary saccade control), the SNr (basal
    # ganglia inhibitory gate), and the fastigial nucleus
    # (cerebellar saccade adaptation) are DIFFERENT levels of
    # saccade control:
    #
    #   brainparts.forebrain.telencephalon.cortex.frontal.frontal_eye_field
    #   brainparts.midbrain.tegmentum.left.substantia_nigra.pars_reticulata
    #   brainparts.hindbrain.metencephalon.cerebellum.deep_cerebellar_nuclei.fastigial_nucleus
    #
    # The FEF is CORTICAL; the SNr is BASAL GANGLIA; the fastigial
    # is CEREBELLAR; the SC is MIDBRAIN. Different structures at
    # different levels.

Reaching the brachium of the SC, the tectobulbar tract, and the
tectoreticular pathway (recommended consumer pattern — the
CONDUCTION PATHWAYS)::

    # The brachium of the SC (BSC), the tectobulbar tract, and the
    # tectoreticular pathway (a subset of the tectobulbar tract) are
    # CONDUCTION PATHWAYS — white matter — that connect the SC to
    # its upstream and downstream targets:
    #
    #   brainparts.midbrain.tectum.left.brachium_of_the_superior_colliculus
    #   brainparts.midbrain.tectum.left.tectobulbar_tract
    #   brainparts.midbrain.tectum.left.tectoreticular_pathway
    #
    # The BSC carries retinal input to the SC and visual attention
    # output to the pulvinar. The tectobulbar and tectoreticular
    # tracts carry the SC's saccade command to the PPRF, riMLF, and
    # CN nuclei. The conduction pathways are DIFFERENT from the SC
    # (which is a nucleus).

Bilateral iteration (recommended consumer pattern — NOTE the
dual-path cross-listing, the no-coupling-warning rule, and the
CONTRALATERAL maps)::

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
            #
            # NOTE: for the SC specifically, the RETINOTOPIC AND
            # MOTOR MAPS ARE CONTRALATERAL — the LEFT SC represents
            # the RIGHT visual field and generates RIGHTWARD
            # saccades; the RIGHT SC represents the LEFT visual
            # field and generates LEFTWARD saccades. The FIXATION
            # ZONE is BILATERAL. The bilateral output of each SC
            # to the PPRF, riMLF, and CN nuclei is a DOWNSTREAM
            # projection to BILATERAL targets — not intrinsic
            # left-right coupling. The two SCs are independent
            # paired sensorimotor integration structures.

Layered-organization detail (not wired — consult references)::

    # The left superior colliculus has a LAYERED organization:
    #
    #   superficial layers    -> VISUAL — stratum zonale,
    #                             stratum griseum superficiale,
    #                             stratum opticum — RETINOTOPIC
    #                             map of the RIGHT visual field;
    #                             direct retinal input (brachium of
    #                             the SC) + corticotectal input
    #                             (left V1)
    #   intermediate layers   -> MOTOR — stratum griseum
    #                             intermediale, stratum album
    #                             intermediale — MOTOR map of
    #                             saccade vectors, ALIGNED with the
    #                             retinotopic map — encodes
    #                             RIGHTWARD saccades
    #   deep layers           -> MULTISENSORY + PREMOTOR OUTPUT —
    #                             stratum griseum profundum, stratum
    #                             album profundum — visual,
    #                             auditory, somatosensory input
    #                             integrated into a common
    #                             orienting map; output to PPRF,
    #                             riMLF, CN III/IV/VI nuclei,
    #                             pulvinar, pretectum, PAG,
    #                             inferior olive
    #
    # Do not attempt to resolve these layers as sub-paths of the
    # superior colliculus — they are PROSE, not modules.

The retinotopic-to-motor map detail (not wired — consult
references)::

    # The left superior colliculus contains TWO ALIGNED MAPS:
    #
    #   RETINOTOPIC MAP (superficial layers):
    #     - fovea at the ROSTRAL pole (the FIXATION ZONE)
    #     - far RIGHT periphery at the CAUDAL pole
    #     - a given collicular location = a given location in the
    #       RIGHT visual field
    #
    #   MOTOR MAP (intermediate / deep layers):
    #     - small saccades (and fixation) at the ROSTRAL pole
    #     - large RIGHTWARD saccades to the far RIGHT periphery at
    #       the CAUDAL pole
    #     - ALIGNED with the retinotopic map — a given collicular
    #       location = a saccade to the corresponding location in
    #       the RIGHT visual field
    #
    # The SC TRANSFORMS a visual location into a saccade command
    # via the alignment of the two maps. The maps are CONTRALATERAL
    # — the left SC represents the RIGHT visual field and generates
    # RIGHTWARD saccades. The FIXATION ZONE is BILATERAL — the
    # rostral pole of EACH SC is a fixation zone, and the two work
    # together to maintain binocular fixation.
    #
    # Do not attempt to resolve the retinotopic map or the motor
    # map as sub-paths of the SC — they are PROSE, not modules.

The saccade hierarchy detail (not wired — consult references)::

    # The saccade hierarchy — the SC is the COMMAND level:
    #
    #   SUPERIOR COLLICULUS (command level) — sensorimotor
    #     integration; receives visual, auditory, somatosensory
    #     input; generates saccade commands in a motor map
    #         |
    #         v
    #   PPRF / riMLF (premotor level) — premotor saccade
    #     generators; transform the SC's saccade command into the
    #     premotor saccade signal
    #         |
    #         v
    #   CN III / IV / VI nuclei (motor level) — motor nuclei;
    #     execute the saccade by driving the extraocular muscles
    #         |
    #         v
    #   Extraocular muscles (effector level) — the effectors of the
    #     saccade
    #
    # The SC is UPSTREAM of the PPRF/riMLF and the CN nuclei. The
    # SC decides; the PPRF/riMLF execute; the CN nuclei drive; the
    # muscles move. Each level is a DIFFERENT STRUCTURE. All four
    # levels carry NO coupling warning.
    #
    # Do not attempt to resolve the PPRF, riMLF, or CN nuclei as
    # sub-paths of the SC — they are DIFFERENT structures at
    # DIFFERENT levels of the hierarchy.

Multisensory-integration detail (not wired — consult references)::

    # The left superior colliculus deep layers integrate THREE
    # modalities:
    #
    #   VISUAL — from the superficial layers (retinal + V1) —
    #     retinotopic map of the RIGHT visual field
    #   AUDITORY — from the left IC (via the brachium of the IC)
    #     and the auditory cortex — auditory space map, aligned
    #     with the visual map (contralateral to match)
    #   SOMATOSENSORY — from the spinal cord and the trigeminal
    #     system — somatosensory map of the body surface and the
    #     face
    #
    # The three maps are ALIGNED — a given collicular location
    # represents a common point in visual, auditory, and
    # somatosensory space. A combined visual + auditory stimulus
    # produces a SUPERADDITIVE SC response — the neural substrate
    # of multisensory enhancement in orienting behavior.
    #
    # Do not attempt to resolve the individual modalities as
    # sub-paths of the SC — they are PROSE, not modules.

Clinical-pattern detail (not wired — consult references)::

    # The left superior colliculus is the LEFT SACCADE COMMAND
    # GENERATOR. The CLINICAL PATTERNS of the related lesions are
    # DISTINCT:
    #
    #   LEFT SC lesion              -> SUBTLE deficits in RIGHTWARD
    #                                   saccades and RIGHT visual
    #                                   field orienting — usually
    #                                   COMPENSATED by the right SC
    #                                   and by cortical (FEF) and
    #                                   cerebellar saccade systems.
    #                                   PROFOUND saccade palsy is
    #                                   RARE.
    #   BILATERAL SC lesions        -> MORE SIGNIFICANT saccade
    #                                   deficits (impaired saccade
    #                                   initiation, slowed saccades,
    #                                   impaired visual grasp) —
    #                                   usually part of a broader
    #                                   brainstem process, NOT an
    #                                   isolated SC syndrome
    #   VISUAL GRASP REFLEX         -> RELEASED by FRONTAL LOBE
    #     (released)                    LESIONS — the lesion site is
    #                                   the FRONTAL LOBE; the SC is
    #                                   the SUBSTRATE, NOT the lesion
    #   PARINAUD SYNDROME           -> DORSAL MIDBRAIN SYNDROME —
    #                                   primary substrates are the
    #                                   PRETECTUM (light-near
    #                                   dissociation) and the
    #                                   POSTERIOR COMMISSURE (upgaze
    #                                   palsy); the SC is ADJACENT,
    #                                   NOT the primary substrate
    #   PSP GAZE PALSY              -> primary substrates are the
    #                                   SNr (inhibitory gate) and
    #                                   the riMLF (vertical saccade
    #                                   generator); the SC is
    #                                   ATROPHIED as part of broader
    #                                   degeneration, NOT the primary
    #                                   cause
    #   OCULOMOTOR APRAXIA          -> CORTICAL (FEF) disorder —
    #     (Cogan syndrome)              voluntary saccades impaired,
    #                                   REFLEXIVE saccades PRESERVED
    #                                   (the SC's reflexive pathway
    #                                   is SPARED)
    #   TECTAL GLIOMA               -> DORSAL MIDBRAIN TUMOR — the
    #                                   SC is ADJACENT; the clinical
    #                                   syndrome is the pretectum /
    #                                   posterior commissure / cerebral
    #                                   aqueduct involvement
    #                                   (Parinaud + hydrocephalus)
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # STRUCTURES.

References
----------
*   **Canonical superior colliculus anatomy:** Sparks, D.L. (2002).
    "The brainstem control of saccadic eye movements." *Nature
    Reviews Neuroscience* 3:952–964. (The superior colliculus —
    the saccade command generator; the layered organization
    (superficial, intermediate, deep); the retinotopic and motor
    maps; the saccade hierarchy; the visual grasp reflex; the
    fixation zone.)
*   **Superior colliculus — comprehensive review:** Wurtz, R.H.,
    Albano, J.E. (1980). "Visual-motor function of the primate
    superior colliculus." *Annual Review of Neuroscience* 3:189–226.
    (The visual-motor function of the SC — the retinotopic map in
    the superficial layers; the motor map in the intermediate
    layers; the aligned maps; the visual grasp reflex.)
*   **Superior colliculus — multisensory integration:** Stein, B.E.,
    Stanford, T.R. (2008). "Multisensory integration: current issues
    from the perspective of the single neuron." *Nature Reviews
    Neuroscience* 9:255–266. (The multisensory integration in the
    SC's deep layers — visual, auditory, somatosensory input
    integrated into a common orienting map; the superadditive
    enhancement.)
*   **Superior colliculus — saccade generation:** Wurtz, R.H.,
    Goldberg, M.E. (1972). "Activity of superior colliculus in
    behaving monkey. 3. Cells discharging before eye movements."
    *Journal of Neurophysiology* 35:575–586. (The saccade-related
    activity in the SC — the motor map in the intermediate layers;
    the command-level role in saccade generation.)
*   **Superior colliculus — fixation zone:** Munoz, D.P., Wurtz,
    R.H. (1993). "Fixation cells in monkey superior colliculus. I.
    Characteristics of cell discharge." *Journal of
    Neurophysiology* 70:559–575. (The rostral fixation zone of the
    SC — its role in maintaining fixation and inhibiting saccade
    generation.)
*   **Superior colliculus — corticotectal input:** Wurtz, R.H.,
    Albano, J.E. (1980). "Visual-motor function of the primate
    superior colliculus." *Annual Review of Neuroscience* 3:189–226.
    (The corticotectal input from V1 and the visual association
    cortex; the corticotectal input from the FEF for voluntary
    saccades.)
*   **Superior colliculus — nigrotectal input:** Hikosaka, O.,
    Wurtz, R.H. (1985). "Modification of saccadic eye movements by
    GABA-related substances. I. Injection of nicotinic antagonists
    in monkey superior colliculus." *Journal of Neurophysiology*
    53:266–291. (The nigrotectal input from the SNr — the
    inhibitory gate on the SC's saccade generator.)
*   **Superior colliculus — cerebellotectal input:** Noda, H.,
    Sugita, S., Ikeda, Y. (1990). "Afferent and efferent connections
    of the oculomotor cerebellar vermis in the macaque monkey."
    *Journal of Comparative Neurology* 302:436–450. (The
    cerebellotectal input from the fastigial nucleus — saccade
    adaptation and accuracy.)
*   **Superior colliculus — tectobulbar and tectoreticular output:**
    Grantyn, A., Grantyn, R. (1982). "Axonal patterns and sites of
    termination of cat superior colliculus neurons projecting in
    the tecto-bulbo-spinal tract." *Experimental Brain Research*
    46:243–256. (The tectobulbar and tectoreticular output — the
    SC's command to the PPRF, riMLF, and CN nuclei.)
*   **Superior colliculus — pulvinar projection:** Benevento, L.A.,
    Fallon, J.H. (1975). "The ascending projections of the superior
    colliculus in the rhesus monkey (Macaca mulatta)." *Journal of
    Comparative Neurology* 160:339–362. (The SC's projection to the
    pulvinar — the tectothalamic pathway for visual attention.)
*   **Superior colliculus — PAG projection:** Behbehani, M.M.
    (1995). "Functional characteristics of the midbrain
    periaqueductal gray." *Progress in Neurobiology* 46:575–605.
    (The SC's projection to the PAG — the tectotegmental pathway
    for defensive behaviors.)
*   **Superior colliculus — inferior olive projection:** Hess, D.T.
    (1982). "The tecto-olivo-cerebellar pathway in the rat."
    *Neuroscience Letters* 32:133–137. (The SC's projection to the
    inferior olive — the tecto-olivary pathway for compensatory
    eye movements and saccadic adaptation.)
*   **Visual grasp reflex:** Denny-Brown, D. (1962). "The midbrain
    and motor integration." *Proceedings of the Royal Society of
    Medicine* 55:527–538. (The visual grasp reflex — its release by
    frontal lobe lesions; the SC as the substrate; the cortex as
    the suppressor.)
*   **Parinaud syndrome:** Parinaud, H. (1883). "Paralysie des
    mouvements associés des yeux." *Annales d'Oculistique* 90:1–21.
    (The dorsal midbrain syndrome — upgaze palsy,
    convergence-retraction nystagmus, light-near dissociation,
    Collier sign — the pretectum and posterior commissure as
    primary substrates; the SC as adjacent.)
*   **Progressive supranuclear palsy (contrast — SC atrophy, but
    primary substrates are the SNr and the riMLF):** Steele, J.C.,
    Richardson, J.C., Olszewski, J. (1964). "Progressive
    supranuclear palsy." *Archives of Neurology* 10:333–359. (PSP —
    the SNr and the riMLF as primary substrates of the supranuclear
    gaze palsy; the SC atrophy as part of broader degeneration.)
*   **Oculomotor apraxia (contrast — cortical FEF disorder, SC
    spared):** Cogan, D.G. (1952). "A type of paralysis of conjugate
    gaze (oculomotor apraxia)." *Archives of Ophthalmology*
    50:434–442. (Oculomotor apraxia — a cortical FEF disorder;
    voluntary saccades impaired, reflexive saccades preserved —
    the SC's reflexive pathway spared.)
*   **Tectal glioma:** Bognar, L., Turi, S., Bognar, M. (1999).
    "Tectal plate gliomas." *Child's Nervous System* 15:518–523.
    (Tectal gliomas — dorsal midbrain tumors; the clinical syndrome
    is the pretectum / posterior commissure / cerebral aqueduct
    involvement.)
*   **PPRF and horizontal saccades (contrast — premotor saccade
    generator, downstream of the SC):** Cohen, B., Komatsuzaki, A.
    (1972). "Eye movements induced by stimulation of the pontine
    reticular formation: evidence for integration in oculomotor
    pathways." *Experimental Neurology* 36:101–117. (The PPRF as
    the horizontal saccade generator — a premotor structure
    DOWNSTREAM of the SC.)
*   **riMLF and vertical saccades (contrast — premotor saccade
    generator, downstream of the SC):** Büttner-Ennever, J.A.,
    Büttner, U. (1988). "The reticular formation." In *Neuroanatomy
    of the Oculomotor System* (Büttner-Ennever, ed.). (The riMLF
    and the interstitial nucleus of Cajal as vertical gaze centers
    — premotor structures DOWNSTREAM of the SC.)
*   **LGN (contrast — thalamic visual relay to V1):** Casagrande,
    V.A., Xu, X. (2004). "The lateral geniculate nucleus." In *The
    Visual Neurosciences* (Chalupa & Werner, eds.). (The LGN as the
    thalamic visual relay to V1 — conscious vision — contrast with
    the SC (reflexive orienting).)
*   **Pulvinar (contrast — thalamic visual attention):** Kaas, J.H.,
    Lyon, D.C. (2007). "Pulvinar contributions to the dorsal and
    ventral streams of visual processing in primates." *Brain
    Research Reviews* 55:285–296. (The pulvinar as the thalamic
    visual attention relay — the SC's projection to the pulvinar
    via the BSC.)
*   **FEF (contrast — cortical voluntary saccade control):** Bruce,
    C.J., Goldberg, M.E. (1985). "Primate frontal eye fields. I.
    Single neurons discharging before saccades." *Journal of
    Neurophysiology* 53:603–635. (The FEF as the cortical voluntary
    saccade control region — its projection to the SC via the
    corticotectal pathway.)
*   **SNr (contrast — basal ganglia inhibitory gate):** Hikosaka,
    O., Wurtz, R.H. (1983). "Visual and oculomotor functions of
    monkey substantia nigra pars reticulata. I. Relation of visual
    and auditory responses to saccades." *Journal of
    Neurophysiology* 49:1230–1253. (The SNr as the basal ganglia
    inhibitory gate on the SC's saccade generator.)
*   **Fastigial nucleus (contrast — cerebellar saccade
    adaptation):** Noda, H., Sugita, S., Ikeda, Y. (1990). "Afferent
    and efferent connections of the oculomotor cerebellar vermis in
    the macaque monkey." *Journal of Comparative Neurology*
    302:436–450. (The fastigial nucleus as the cerebellar saccade
    adaptation nucleus — its projection to the SC via the
    cerebellotectal pathway.)
*   **SLEA (contrast — the left superior colliculus is not SLEA):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the superior colliculus.)
*   NeuroNames — Superior colliculus (left); FMA — Superior
    colliculus (left member).
"""