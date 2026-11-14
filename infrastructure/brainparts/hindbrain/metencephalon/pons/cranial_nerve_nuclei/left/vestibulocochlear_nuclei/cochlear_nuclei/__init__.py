"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei.cochlear_nuclei
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── left
                    └── vestibulocochlear_nuclei
                        └── cochlear_nuclei   <-- THIS MODULE

**Primary synonym:** Left cochlear nuclei; left auditory nuclei; left
cochlear nuclear complex; left CN VIII cochlear division nuclei; "the
left first-order central auditory relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nuclear complex** — a **heterogeneous
collection** of **left-side auditory nuclei** at the **left
pontomedullary junction**, on the **dorsolateral surface of the left
inferior cerebellar peduncle**. It is the **sole central target** of the
**left cochlear nerve** (the cochlear division of left CN VIII) and the
**first-order central auditory relay**.
**Part of:** The **vestibulocochlear_nuclei** sub-container of the
**left** container of the **cranial_nerve_nuclei** container —
specifically, the **special sensory (auditory)** component. The
**vestibulocochlear_nuclei** is the **left-side half** of the **CN VIII
special sensory** nuclear complex; the **cochlear_nuclei** is its
**auditory sub-container**.
**Structural parent:** ``.../vestibulocochlear_nuclei/`` → **direct
child** of the vestibulocochlear_nuclei sub-container.
**Structural children:** **None.** This is a **leaf** module at the
**tree level** — but it is a **conceptual sub-container** of **three
prose subdivisions** (anterior ventral cochlear nucleus, posterior
ventral cochlear nucleus, dorsal cochlear nucleus). The **AVCN**,
**PVCN**, and **DCN** are documented as **prose**, not as structural
children.
**Boundary status (LEAF at tree level — CONCEPTUAL SUB-CONTAINER of
prose subdivisions):** **Boundary case — the cochlear nuclei are a LEAF
at the TREE level, but a CONCEPTUAL SUB-CONTAINER of THREE PROSE
SUBDIVISIONS.** The tree wires the **cochlear nuclei** as a **single
`__init__.py`** — they have **no structural children**. The **anterior
ventral cochlear nucleus (AVCN)**, **posterior ventral cochlear nucleus
(PVCN)**, and **dorsal cochlear nucleus (DCN)** are **prose
subdivisions**, not structural children. Consumers must **not** assume
AVCN, PVCN, or DCN exist as structural sub-modules — they must resolve
sub-nucleus detail through the references, not the tree.
**Boundary status (SPECIAL SENSORY — AUDITORY — NOT general sensory):**
**Boundary case — the cochlear nuclei are SPECIAL SENSORY (AUDITORY),
NOT general sensory.** Unlike the **chief sensory trigeminal nucleus**
(general sensory — discriminative touch from the face), the **cochlear
nuclei** (here) subserve **hearing** (the **special auditory sense**).
They are **DIFFERENT STRUCTURES** — different sensory modalities
(special auditory vs. general somatosensory), different cranial nerves
(VIII vs. V), different peripheral receptors (hair cells in the organ
of Corti vs. mechanoreceptors in the face). Consumers must **not**
conflate the **cochlear nuclei** with the **chief sensory trigeminal
nucleus** or any other general sensory nucleus.
**Boundary status (NOT the vestibular nuclei — that is the OTHER
sub-container of the vestibulocochlear nuclei):** **Boundary case —
the cochlear nuclei are NOT the vestibular nuclei.** The **left
vestibular nuclei**
(``.../vestibulocochlear_nuclei/vestibular_nuclei/``) are the **other
structural child** of the vestibulocochlear_nuclei sub-container —
they subserve **balance and spatial orientation** (the special
vestibular sense). The **left cochlear nuclei** (here) subserve
**hearing** (the special auditory sense). They are **DIFFERENT
STRUCTURES** — different functional systems (auditory vs. vestibular),
different peripheral receptors (organ of Corti vs. semicircular canals,
utricle, saccule), different ascending pathways. They are **both under
the vestibulocochlear_nuclei sub-container**, but they are
**functionally distinct sub-containers**. Consumers must **not**
conflate the **cochlear nuclei** with the **vestibular nuclei**.
**Boundary status (GREY-MATTER NUCLEI — NOT the cochlear NERVE):**
**Boundary case — the cochlear nuclei are the GREY-MATTER NUCLEI, NOT
the cochlear nerve.** The **left cochlear nerve** (the cochlear
division of left CN VIII) is the **white-matter axon bundle** that
**carries** the **primary auditory axons** from the **left spiral
ganglion** to the **left cochlear nuclei**. The **cochlear nuclei**
(here) are the **grey-matter neuron clusters** that **receive** those
axons and **relay** the auditory signal **upward**. They are
**DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the **nerve**
is white matter. Consumers must **not** conflate the **nuclei** with
the **nerve** — the nuclei are the **central sensory relays**; the
nerve is the **peripheral conduction infrastructure**.
**Boundary status (NOT the cochlea — that is the PERIPHERAL RECEPTOR):**
**Boundary case — the cochlear nuclei are NOT the cochlea.** The **left
cochlea** is the **peripheral sensory organ** of hearing — it contains
the **organ of Corti** with its **hair cells**, which **transduce**
sound into neural signals. The **cochlear nuclei** (here) are the
**central grey-matter relays** that **receive** those signals. They are
**DIFFERENT STRUCTURES** — the **cochlea** is a peripheral sensory
organ; the **nuclei** are central nervous system. Consumers must **not**
conflate the **central nuclei** with the **peripheral receptor**.
**Boundary status (NOT the spiral ganglion — that is a PERIPHERAL
SENSORY GANGLION):** **Boundary case — the cochlear nuclei are NOT the
spiral ganglion.** The **left spiral ganglion** (cochlear ganglion) is
the **peripheral sensory ganglion** that contains the **primary
auditory neuron cell bodies** for the left cochlea. The **cochlear
nuclei** (here) are the **central grey-matter nuclei** that **receive**
the axons from the spiral ganglion. They are **DIFFERENT STRUCTURES** —
the **ganglion** is peripheral; the **nuclei** are central. Consumers
must **not** conflate the **central nuclei** with the **peripheral
ganglion**.
**Boundary status (NOT the vestibulocochlear nerve — that is the WHOLE
CN VIII):** **Boundary case — the cochlear nuclei are NOT the
vestibulocochlear nerve.** The **left vestibulocochlear nerve** (left
CN VIII) is the **whole nerve** — it contains the **cochlear division**
(from the left cochlea) and the **vestibular division** (from the left
vestibular apparatus). The **cochlear nuclei** (here) are the **central
grey-matter nuclei** that **receive** the axons of the **cochlear
division only**. They are **DIFFERENT STRUCTURES** — the **nuclei** are
central grey matter; the **nerve** is the **whole peripheral nerve**
that carries both divisions. Consumers must **not** conflate the
**cochlear nuclei** with the **vestibulocochlear nerve**.
**Boundary status (NOT the superior olivary complex — that is DOWNSTREAM
of the cochlear nuclei):** **Boundary case — the cochlear nuclei are
NOT the superior olivary complex.** The **left superior olivary complex**
(``.../pons/superior_olivary_complex/left/``) is the **auditory
brainstem relay** that **receives** the **projections** from the **left
cochlear nuclei** (and the **right cochlear nuclei**, via the **right
trapezoid body**) and **processes** **interaural time and intensity
differences** for **sound localization**. The **cochlear nuclei** (here)
are **upstream** of the superior olivary complex — they are the **first
central relay** for audition. They are **DIFFERENT STRUCTURES** — the
**cochlear nuclei** are the **first-order central auditory relay**; the
**superior olivary complex** is the **second-order binaural processing
center**. Consumers must **not** conflate the **cochlear nuclei** with
the **superior olivary complex**.
**Boundary status (NOT the inferior colliculus — that is MIDBRAIN and it
is DOWNSTREAM):** **Boundary case — the cochlear nuclei are NOT the
inferior colliculus.** The **left inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
is the **midbrain auditory relay** that **receives** the **ascending
auditory projections** from the **superior olivary complex** and the
**lateral lemniscus** and **projects** to the **medial geniculate body**
of the thalamus. The **cochlear nuclei** (here) are **upstream** of the
inferior colliculus — they are the **first central relay**. Consumers
must **not** conflate the **cochlear nuclei** with the **inferior
colliculus**.
**Boundary status (NOT the medial geniculate body — that is THALAMIC and
it is DOWNSTREAM):** **Boundary case — the cochlear nuclei are NOT the
medial geniculate body.** The **left medial geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
is the **thalamic auditory relay** that **receives** the **ascending
auditory projections** from the **inferior colliculus** and **projects**
to the **primary auditory cortex**. The **cochlear nuclei** (here) are
**upstream** of the medial geniculate body — they are the **first
central relay**. Consumers must **not** conflate the **cochlear nuclei**
with the **medial geniculate body**.
**Boundary status (NOT the primary auditory cortex — that is CORTICAL
and it is DOWNSTREAM):** **Boundary case — the cochlear nuclei are NOT
the primary auditory cortex.** The **left primary auditory cortex**
(Heschl's gyrus, Brodmann areas 41 and 42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
is the **cortical target** of the **ascending auditory pathway**. The
**cochlear nuclei** (here) are **far upstream** of the primary auditory
cortex — they are the **first central relay**. Consumers must **not**
conflate the **cochlear nuclei** with the **primary auditory cortex**.
**Boundary status (NOT the trapezoid body — that is the WHITE-MATTER
DECUSSATING TRACT):** **Boundary case — the cochlear nuclei are NOT the
trapezoid body.** The **left trapezoid body** is the **white-matter
decussating tract** that **carries** the axons from the **left cochlear
nuclei** (especially the **AVCN** globular bushy cells) to the
**contralateral (right) superior olivary complex** — the **neural
substrate** of **interaural time and intensity difference** processing.
The **cochlear nuclei** (here) are the **grey-matter neuron clusters**
that **give rise to** those axons. They are **DIFFERENT STRUCTURES** —
the **nuclei** are grey matter; the **trapezoid body** is white matter.
Consumers must **not** conflate the **cochlear nuclei** with the
**trapezoid body**.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
ASCENDING TRACT):** **Boundary case — the cochlear nuclei are NOT the
lateral lemniscus.** The **left lateral lemniscus** is the **white-matter
ascending tract** that **carries** the axons from the **superior olivary
complex** (and the **cochlear nuclei** directly, via the **intermediate
acoustic stria**) to the **inferior colliculus**. The **cochlear
nuclei** (here) are the **grey-matter neuron clusters** that
**contribute** axons to the lateral lemniscus (via the intermediate
acoustic stria). They are **DIFFERENT STRUCTURES** — the **nuclei** are
grey matter; the **lateral lemniscus** is white matter. Consumers must
**not** conflate the **cochlear nuclei** with the **lateral lemniscus**.
**Boundary status (NOT the inferior cerebellar peduncle — that is the
WHITE-MATTER TRACT on which the nuclei SIT):** **Boundary case — the
cochlear nuclei are NOT the inferior cerebellar peduncle.** The **left
inferior cerebellar peduncle** (restiform body) is the **white-matter
tract** on whose **dorsolateral surface** the **cochlear nuclei** are
**anatomically located** — it carries **cerebellar afferents and
efferents**. The **cochlear nuclei** (here) are the **grey-matter
neuron clusters** that sit **on** the inferior cerebellar peduncle.
They are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**peduncle** is white matter. **The anatomical juxtaposition** (the
nuclei sit on the peduncle) is a **classic source of confusion** —
consumers must **not** conflate the **cochlear nuclei** with the
**inferior cerebellar peduncle**.
**Boundary status (NOT the cerebellum — that is the metencephalic
SIBLING the peduncle connects to):** **Boundary case — the cochlear
nuclei are NOT the cerebellum.** The **left cerebellum**
(``.../metencephalon/cerebellum/hemispheres/left/``) is the **left
metencephalic cerebellar half**. The **cochlear nuclei** are located
**near** the **left inferior cerebellar peduncle** (which connects to
the cerebellum), but the **cochlear nuclei** and the **cerebellum** are
**DIFFERENT STRUCTURES** — the **cochlear nuclei** are the **auditory
brainstem relay**; the **cerebellum** is the **metencephalic cerebellar
half**. Consumers must **not** conflate the **cochlear nuclei** with
the **cerebellum**.
**Boundary status (NOT the vestibular nuclei — even though they are the
OTHER sub-container of the vestibulocochlear nuclei):** **Boundary
case — the cochlear nuclei are NOT the vestibular nuclei, even though
they are the OTHER sub-container of the vestibulocochlear nuclei.** The
**left vestibular nuclei**
(``.../vestibulocochlear_nuclei/vestibular_nuclei/``) subserve
**balance and spatial orientation**; the **left cochlear nuclei**
(here) subserve **hearing**. They are **both under the
vestibulocochlear_nuclei sub-container**, but they are **functionally
distinct** — **different sensory modalities** (auditory vs. vestibular),
**different peripheral receptors** (organ of Corti vs. semicircular
canals, utricle, saccule), **different ascending pathways** (auditory
pathway vs. vestibular pathways to extraocular motor nuclei,
cerebellum, thalamus, cortex). Consumers must **not** conflate the
**cochlear nuclei** with the **vestibular nuclei**.
**Boundary status (NOT the facial nerve nucleus, superior salivatory
nucleus, abducens nucleus, chief sensory trigeminal nucleus, or motor
trigeminal nucleus — those are CN V, VI, VII SIBLINGS):** **Boundary
case — the cochlear nuclei are NOT the facial nerve nucleus, superior
salivatory nucleus, abducens nucleus, chief sensory trigeminal nucleus,
or motor trigeminal nucleus.** Those are **sibling nuclei** under the
left container of the cranial_nerve_nuclei — they subserve **different
cranial nerves** (VII, VII, VI, V, V) and **different functional
systems** (branchial motor, parasympathetic, somatic motor, general
sensory, branchial motor). The **cochlear nuclei** (here) are the **CN
VIII auditory special sensory nuclei**. Consumers must **not** conflate
the **cochlear nuclei** with any of the **CN V, CN VI, or CN VII sibling
nuclei**.
**Boundary status (NOT a single uniform nucleus — THREE functionally
distinct PROSE SUBDIVISIONS):** **Boundary case — the cochlear nuclei
are NOT a single uniform nucleus; they contain THREE functionally
distinct prose subdivisions.** The **anterior ventral cochlear nucleus
(AVCN)** — **spherical bushy cells** and **globular bushy cells** —
**processes timing and intensity** information critical for **sound
localization**. The **posterior ventral cochlear nucleus (PVCN)** —
**octopus cells** — **processes temporal onset** and **rapid temporal
transients** (critical for **speech perception**). The **dorsal
cochlear nucleus (DCN)** — **fusiform cells** and **cartwheel cells** —
**process spectral cues** and **complex sound features** (including
**spectral notches** used for **vertical sound localization** by the
**pinna**). These **prose subdivisions** are **not structural
children**. Consumers must **not** treat the cochlear nuclei as a single
uniform nucleus — they are a **three-population complex** with
**functionally distinct** sub-circuits.
**Boundary status (NOT the whole vestibulocochlear_nuclei sub-container
— a sub-container child of the vestibulocochlear_nuclei):** **Boundary
case — the cochlear nuclei are a SUB-CONTAINER child of the
vestibulocochlear_nuclei sub-container, not the sub-container itself,
and not the whole cranial_nerve_nuclei container.** The
**vestibulocochlear_nuclei** sub-container contains the **cochlear
nuclei** and the **vestibular nuclei**. The **cranial_nerve_nuclei**
container contains the **vestibulocochlear_nuclei** and **five other
children**. Consumers must **not** conflate the cochlear nuclei with the
**vestibulocochlear_nuclei** sub-container or the **cranial_nerve_nuclei**
container.
**Boundary status (NOT the right cochlear nuclei — strict mirror, no
warning):** **Boundary case — the left cochlear nuclei are NOT the right
cochlear nuclei; the two are a STRICT MIRROR PAIR with NO warning at
the sub-container level.** The **right cochlear nuclei**
(``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/``)
are the **structurally identical** right-side counterpart — same three
prose subdivisions (AVCN, PVCN, DCN), same auditory special sensory
function, same bilateral framing. The two sides are **strictly
mirrored** — any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere. Consumers must
**not** import a lateralization warning into the left cochlear nuclei —
there is **none at the sub-container level** beyond the **auditory
structural facts** documented below.
**Boundary status (SLEA-FREE — the cochlear nuclei are NOT an
extended-amygdala component):** **Boundary case — the cochlear nuclei
are SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus**
(the **only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired elsewhere). The
**cochlear nuclei** are **auditory special sensory brainstem nuclei** —
they are **NOT** an extended-amygdala component, and they carry **NO
SLEA warning**. Consumers must **not** import the SLEA warning into the
cochlear nuclei — they are **SLEA-free**.

Overview
--------
The cochlear nuclei are the **auditory special sensory** nuclei for
**left CN VIII** — the **sole central target** of the **left cochlear
nerve** (the cochlear division of left CN VIII) and the **first-order
central auditory relay**. They are a **leaf** module at the **tree
level** — with **no structural children** — but they are a
**conceptual sub-container** of **three prose subdivisions**: the
**anterior ventral cochlear nucleus (AVCN)**, the **posterior ventral
cochlear nucleus (PVCN)**, and the **dorsal cochlear nucleus (DCN)**.

**The cochlear nuclei are a LEAF at the TREE level, but a CONCEPTUAL
SUB-CONTAINER of THREE PROSE SUBDIVISIONS.** The tree wires the
**cochlear nuclei** as a **single `__init__.py`** — they have **no
structural children**. The **AVCN**, **PVCN**, and **DCN** are **prose
subdivisions**, not structural children. Consumers must **not** assume
AVCN, PVCN, or DCN exist as structural sub-modules.

**The cochlear nuclei are SPECIAL SENSORY (AUDITORY), NOT general
sensory.** They subserve **hearing** — the **special auditory sense** —
not general somatosensation. They are **DIFFERENT STRUCTURES** from the
**chief sensory trigeminal nucleus** or any other general sensory
nucleus.

**The cochlear nuclei are NOT the vestibular nuclei.** The **vestibular
nuclei** are the **other sub-container** of the vestibulocochlear
nuclei — they subserve **balance and spatial orientation**. They are
**DIFFERENT STRUCTURES** — different sensory modalities, different
peripheral receptors, different ascending pathways. They are **both
under the vestibulocochlear_nuclei sub-container**, but they are
**functionally distinct**. Consumers must **not** conflate the
**cochlear nuclei** with the **vestibular nuclei**.

**The cochlear nuclei are GREY-MATTER NUCLEI, NOT the cochlear NERVE.**
The **cochlear nerve** (the cochlear division of left CN VIII) is the
**white-matter axon bundle** that **carries** the primary auditory
axons from the left spiral ganglion. The **cochlear nuclei** (here) are
the **grey-matter neuron clusters** that **receive** those axons. They
are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**nerve** is white matter.

**The cochlear nuclei are a THREE-POPULATION complex.** The **AVCN**,
**PVCN**, and **DCN** are **functionally distinct prose subdivisions**.
Consumers must **not** treat the cochlear nuclei as a single uniform
nucleus — they are a **three-population complex** with **functionally
distinct** sub-circuits.

**The cochlear nuclei are SLEA-FREE.** They are **not** an
extended-amygdala component, and they carry **no SLEA warning**.

Prose Subdivision Composition (prose, not structural children)
--------------------------------------------------------------
The cochlear nuclei contain **three prose subdivisions** — documented as
**prose**, not as structural children:

*   **Anterior ventral cochlear nucleus (AVCN)** — the **anterior
    portion** of the **ventral cochlear nucleus** (anterior to the
    **nerve root**). The AVCN contains **spherical bushy cells** and
    **globular bushy cells** — the **spherical bushy cells** receive
    **endbulbs of Held** from the **auditory nerve** and **preserve
    temporal precision** for **interaural time difference** processing;
    the **globular bushy cells** project via the **trapezoid body** to
    the **medial nucleus of the trapezoid body** and the
    **contralateral superior olivary complex** for **interaural
    intensity difference** processing. **The AVCN is the principal
    output to the superior olivary complex** — it is the **primary
    substrate** of **sound localization**.

*   **Posterior ventral cochlear nucleus (PVCN)** — the **posterior
    portion** of the **ventral cochlear nucleus**. The PVCN contains
    **octopus cells** — which receive **broadband auditory input** and
    **detect temporal onsets** and **rapid temporal transients**
    (critical for **speech perception** and **sound-onset
    detection**). The PVCN also contains **multipolar cells** and
    **small cells** that project to the **inferior colliculus** (via
    the **intermediate acoustic stria**) and the **contralateral
    cochlear nuclei** (via the **commissural fibers**).

*   **Dorsal cochlear nucleus (DCN)** — the **dorsal portion** of the
    cochlear nuclei, on the **dorsolateral surface** of the **inferior
    cerebellar peduncle**. The DCN contains **fusiform cells** (the
    principal output neurons), **cartwheel cells** (inhibitory
    interneurons), **granule cells**, and **stellate cells** — the
    **DCN** has a **cerebellum-like cortical structure** and
    **processes spectral cues** and **complex sound features**
    (including **spectral notches** used for **vertical sound
    localization** by the **pinna** and **head-related transfer
    functions**). The DCN is the **principal output to the inferior
    colliculus** (via the **dorsal acoustic stria**) — it is the
    **primary substrate** of **spectral cue processing**.

**These subdivisions are prose, not structural children.** The tree
wires the **cochlear nuclei** as a **single leaf** — the **AVCN**,
**PVCN**, and **DCN** are **prose**, not structural children. Consumers
that need **sub-nucleus-level** resolution should consult the
references, not the tree.

The Cochlear Nuclei / Cochlear Nerve Boundary
---------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Cochlear nuclei** (this module) — the **grey-matter neuron
    clusters** at the left pontomedullary junction.

*   **Cochlear nerve** (the cochlear division of left CN VIII) — the
    **white-matter axon bundle** that carries the primary auditory
    axons from the left spiral ganglion.

**They are DIFFERENT STRUCTURES.** The **nuclei** are the **central
sensory relays**; the **nerve** is the **peripheral conduction
infrastructure**. Consumers must **not** conflate the two — the
**cochlear nuclei** are the **nuclei**; the **cochlear nerve** is the
**nerve**.

The Cochlear Nuclei / Cochlea Boundary
--------------------------------------
This is the **central vs. peripheral** boundary:

*   **Cochlear nuclei** (this module) — the **central grey-matter
    relays**.

*   **Cochlea** — the **peripheral sensory organ** of hearing —
    containing the **organ of Corti** with its **hair cells**, which
    **transduce** sound into neural signals.

**They are DIFFERENT STRUCTURES** — the **cochlea** is a peripheral
sensory organ; the **nuclei** are central nervous system. Consumers
must **not** conflate the **central nuclei** with the **peripheral
receptor**.

The Cochlear Nuclei / Spiral Ganglion Boundary
----------------------------------------------
This is the **central vs. peripheral** boundary — **nuclei vs.
ganglion**:

*   **Cochlear nuclei** (this module) — the **central grey-matter
    nuclei** that **receive** the primary auditory axons.

*   **Spiral ganglion** (cochlear ganglion) — the **peripheral sensory
    ganglion** that contains the **primary auditory neuron cell bodies**.

**They are DIFFERENT STRUCTURES** — the **ganglion** is peripheral; the
**nuclei** are central. Consumers must **not** conflate the **central
nuclei** with the **peripheral ganglion**.

The Cochlear Nuclei / Vestibular Nuclei Boundary
------------------------------------------------
This is the **other sub-container** boundary — **auditory vs.
vestibular**, both under the vestibulocochlear nuclei:

*   **Cochlear nuclei** (this module) — the **auditory** special
    sensory nuclei — **hearing**.

*   **Vestibular nuclei**
    (``.../vestibulocochlear_nuclei/vestibular_nuclei/``) — the
    **vestibular** special sensory nuclei — **balance and spatial
    orientation**.

**They are DIFFERENT STRUCTURES** — different sensory modalities
(auditory vs. vestibular), different peripheral receptors, different
ascending pathways. They are **both under the vestibulocochlear_nuclei
sub-container**, but they are **functionally distinct**. Consumers must
**not** conflate the **cochlear nuclei** with the **vestibular nuclei**.

The Cochlear Nuclei / Superior Olivary Complex Boundary
-------------------------------------------------------
This is the **auditory brainstem relay** boundary — **upstream vs.
downstream**:

*   **Cochlear nuclei** (this module) — the **first central auditory
    relay**.

*   **Superior olivary complex**
    (``.../pons/superior_olivary_complex/left/``) — the **auditory
    brainstem relay** that **receives** the cochlear nuclei
    projections (via the **trapezoid body**) and **processes**
    **interaural time and intensity differences** for **sound
    localization**.

**The cochlear nuclei are UPSTREAM** of the superior olivary complex —
the **cochlear nuclei** are the **first-order central auditory relay**;
the **superior olivary complex** is the **second-order binaural
processing center**. Consumers must **not** conflate the **cochlear
nuclei** with the **superior olivary complex**.

The Cochlear Nuclei / Inferior Colliculus Boundary
--------------------------------------------------
This is the **midbrain auditory relay** boundary — **upstream vs.
downstream**:

*   **Cochlear nuclei** (this module) — the **first central auditory
    relay**.

*   **Inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
    — the **midbrain auditory relay** that receives the ascending
    auditory projections from the superior olivary complex and the
    lateral lemniscus and projects to the medial geniculate body.

**The cochlear nuclei are UPSTREAM** of the inferior colliculus — they
are the **first central auditory relay**. Consumers must **not**
conflate the **cochlear nuclei** with the **inferior colliculus**.

The Cochlear Nuclei / Medial Geniculate Body Boundary
-----------------------------------------------------
This is the **thalamic auditory relay** boundary — **upstream vs.
downstream**:

*   **Cochlear nuclei** (this module) — the **first central auditory
    relay**.

*   **Medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
    — the **thalamic auditory relay** that receives the ascending
    auditory projections from the inferior colliculus and projects to
    the primary auditory cortex.

**The cochlear nuclei are UPSTREAM** of the medial geniculate body —
they are the **first central auditory relay**. Consumers must **not**
conflate the **cochlear nuclei** with the **medial geniculate body**.

The Cochlear Nuclei / Primary Auditory Cortex Boundary
------------------------------------------------------
This is the **cortical auditory target** boundary — **upstream vs.
downstream**:

*   **Cochlear nuclei** (this module) — the **first central auditory
    relay**.

*   **Primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
    42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
    — the **cortical target** of the ascending auditory pathway.

**The cochlear nuclei are UPSTREAM** of the primary auditory cortex —
they are the **first central auditory relay**. Consumers must **not**
conflate the **cochlear nuclei** with the **primary auditory cortex**.

The Cochlear Nuclei / Trapezoid Body Boundary
---------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the
**decussating tract**:

*   **Cochlear nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the trapezoid body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the axons from the **cochlear nuclei** (especially the
    **AVCN** globular bushy cells) to the **contralateral (right)
    superior olivary complex**.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**trapezoid body** is white matter. Consumers must **not** conflate the
**cochlear nuclei** with the **trapezoid body**.

The Cochlear Nuclei / Lateral Lemniscus Boundary
------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **ascending
tract**:

*   **Cochlear nuclei** (this module) — the **grey-matter neuron
    clusters** that **contribute** axons to the lateral lemniscus.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the axons from the **superior olivary complex** (and
    the **cochlear nuclei**, via the **intermediate acoustic stria**) to
    the **inferior colliculus**.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**lateral lemniscus** is white matter. Consumers must **not** conflate
the **cochlear nuclei** with the **lateral lemniscus**.

The Cochlear Nuclei / Inferior Cerebellar Peduncle Boundary
-----------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **peduncle
the nuclei SIT ON**:

*   **Cochlear nuclei** (this module) — the **grey-matter neuron
    clusters**.

*   **Inferior cerebellar peduncle** (restiform body) — the
    **white-matter tract** on whose **dorsolateral surface** the
    **cochlear nuclei** are **anatomically located**.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**peduncle** is white matter. **The anatomical juxtaposition** (the
nuclei sit on the peduncle) is a **classic source of confusion** —
consumers must **not** conflate the **cochlear nuclei** with the
**inferior cerebellar peduncle**.

The Cochlear Nuclei / Cerebellum Boundary
-----------------------------------------
This is the **metencephalic-sibling** boundary — **nuclei near the
cerebellar peduncle vs. cerebellum itself**:

*   **Cochlear nuclei** (this module) — the **auditory brainstem
    relay**.

*   **Cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/left/``) — the **left
    metencephalic cerebellar half**.

**The cochlear nuclei are located near the left inferior cerebellar
peduncle** (which connects to the cerebellum), but the **cochlear
nuclei** and the **cerebellum** are **DIFFERENT STRUCTURES** — the
**cochlear nuclei** are the **auditory brainstem relay**; the
**cerebellum** is the **metencephalic cerebellar half**. Consumers must
**not** conflate the **cochlear nuclei** with the **cerebellum**.

The Cochlear Nuclei / CN V, VI, VII Sibling Nuclei Boundary
-----------------------------------------------------------
This is the **sibling** boundary — **CN VIII auditory vs. other
functional systems**:

*   **Cochlear nuclei** (this module) — the **CN VIII auditory special
    sensory** nuclei — **hearing**.

*   **Chief sensory trigeminal nucleus** (CN V general sensory),
    **motor trigeminal nucleus** (CN V branchial motor), **abducens
    nucleus** (CN VI somatic motor), **facial nerve nucleus** (CN VII
    branchial motor), **superior salivatory nucleus** (CN VII
    parasympathetic) — the **sibling nuclei** under the left container
    of the cranial_nerve_nuclei.

**They are DIFFERENT STRUCTURES** — different cranial nerves, different
functional systems, different peripheral targets. Consumers must **not**
conflate the **cochlear nuclei** with any of the **CN V, CN VI, or CN
VII sibling nuclei**.

The Cochlear Nuclei / Vestibulocochlear Nuclei Sub-Container Boundary
---------------------------------------------------------------------
This is the **sub-container vs. sub-container child** boundary:

*   **Cochlear nuclei** (this module) — a **sub-container child** of the
    **vestibulocochlear_nuclei** sub-container.

*   **Vestibulocochlear nuclei** (``.../vestibulocochlear_nuclei/``) —
    the **CN VIII special sensory sub-container**, with **two structural
    children** (the **cochlear nuclei** and the **vestibular nuclei**).

**The cochlear nuclei are a sub-container child of the
vestibulocochlear_nuclei.** Consumers must **not** conflate the cochlear
nuclei with the **vestibulocochlear_nuclei** sub-container or the
**cranial_nerve_nuclei** container.

The Cochlear Nuclei / Right Cochlear Nuclei Boundary
----------------------------------------------------
This is the **strict-mirror** boundary:

*   **Left cochlear nuclei** (this module) — the **left-side** auditory
    special sensory nuclei for **left hearing**.

*   **Right cochlear nuclei**
    (``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/``)
    — the **structurally identical** right-side auditory special
    sensory nuclei for **right hearing**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same three prose
subdivisions (AVCN, PVCN, DCN), same auditory special sensory function,
same bilateral framing. **Auditory laterality facts are documented in
the Lateralization Notes below, not imported from elsewhere** — the
structural connectivity facts (ipsilateral cochlear input up to the
superior olivary complex, then bilateral projections from the superior
olivary complex onward) are **structural** and **not warnings**.
Consumers must **not** import a lateralization warning into the left
cochlear nuclei — there is **none at the sub-container level**.

The Cochlear Nuclei / SLEA Boundary
-----------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cochlear nuclei** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The cochlear nuclei are NOT part of the SLEA continuum.** They are
**auditory special sensory brainstem nuclei**, and they carry **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
cochlear nuclei.

Function in the Human Brain
---------------------------
The cochlear nuclei's functions are **the first central relay for left
hearing** — **NOT a single unified function**:

*   **Auditory Relay (First-Order):** The **cochlear nuclei**
    **receive** the **primary auditory axons** from the **left spiral
    ganglion** (via the **left cochlear nerve**) and **project** to the
    **superior olivary complex**, the **inferior colliculus**, and the
    **medial geniculate body** — the **ascending auditory pathway**.
    They are the **first central relay** for **hearing**.

*   **Sound Localization (Interaural Time and Intensity Differences):**
    The **AVCN** (via its **spherical bushy cells** and **globular
    bushy cells**) **projects** to the **superior olivary complex** —
    via the **trapezoid body** — to **compute** the **interaural time
    differences** (ITD) and **interaural intensity differences** (IID)
    that underlie **sound localization**. The **AVCN is the principal
    substrate** of the **neural computation** of **sound source
    location**.

*   **Temporal Onset Detection and Speech Processing:** The **PVCN**
    (via its **octopus cells**) **detects** the **temporal onsets** and
    **rapid temporal transients** that are **critical for speech
    perception** — the **octopus cells** are **exquisitely tuned** to
    **broadband transients** and **preserve temporal precision** that
    is **essential** for **speech intelligibility**.

*   **Spectral Cue Processing and Vertical Sound Localization:** The
    **DCN** (via its **fusiform cells** and **cartwheel cells**)
    **processes** the **spectral cues** and **complex sound features**
    (including the **spectral notches** produced by the **pinna** and
    **head-related transfer functions**) that underlie **vertical
    sound localization** — the **DCN** is the **primary substrate** of
    **spectral cue processing** for **elevation** and **front-back
    discrimination**.

*   **NOT a neural processor in the classical sense.** The cochlear
    nuclei are **first-order central sensory relays** — they **receive**
    the primary auditory afferents and **project** them upward. The
    **processing** of auditory signals is **distributed** across the
    **cochlear nuclei** (first central relay), the **superior olivary
    complex** and **inferior colliculus** (auditory brainstem
    processing), the **medial geniculate body** (thalamic relay), and
    the **primary auditory cortex** (cortical processing). The
    **cochlear nuclei** are the **first central relay** — the
    **brainstem entry point** for audition.

**The unifying theme:** the cochlear nuclei are the **first central
sensory relay** for the **left auditory system** — the **sole central
target** of the **left cochlear nerve**. They are **special sensory**
(hearing), **three-population** (AVCN for sound localization; PVCN for
temporal onset; DCN for spectral cues), **SLEA-free**, and **NOT the
cochlear nerve** — the **nerve** is the **white-matter axon bundle**;
the **nuclei** are the **grey-matter neuron clusters** that **receive**
its axons.

Associated Disorders
--------------------
The cochlear nuclei have **no named "cochlear nuclei syndrome"** — their
clinical associations are **nucleus-specific**, and they are
**distinguishable from nerve-level, peripheral-receptor-level, and
downstream auditory pathway lesions**:

*   **Cochlear Nuclei Lesion — Ipsilateral Sensorineural Hearing Loss:**
    A lesion of the **left cochlear nuclei** causes **left
    sensorineural hearing loss** — **unilateral deafness** (if the
    lesion is complete) or **impaired hearing** (if partial). Because
    the **auditory pathway** is **bilateral from the superior olivary
    complex onward**, a **cochlear nuclei lesion** is one of the **few
    lesions** that causes **unilateral** hearing loss — the **cortical
    auditory cortex** receives **bilateral** input, so a **cortical**
    lesion does **not** cause unilateral deafness. **This is a critical
    clinical distinction** — **cochlear nuclei lesions** cause
    **ipsilateral deafness**; **cortical auditory lesions** do **not**.

*   **Cochlear Nerve Lesion — Ipsilateral Sensorineural Hearing Loss
    (Acoustic Neuroma, Vestibular Schwannoma):** A lesion of the **left
    cochlear nerve** (e.g. **acoustic neuroma** / vestibular
    schwannoma, or **cochlear nerve aplasia**) causes **left
    sensorineural hearing loss** — **clinically identical** to a
    **cochlear nuclei lesion** in its effect on hearing. **The
    distinction from a cochlear nuclei lesion** is often made by
    **associated brainstem signs** — a **cochlear nuclei lesion** may be
    accompanied by **ipsilateral vestibular signs** (vestibular nuclei
    involvement) or **contralateral body sensory signs** (brainstem
    involvement); a **cochlear nerve lesion** is usually **isolated
    hearing loss** (with or without **vestibular nerve involvement** in
    acoustic neuroma). **The cochlear nuclei themselves are spared** in
    a **nerve lesion** — the lesion is at the **nerve** level.

*   **Cortical Auditory Lesion — Contralateral or Bilateral Hearing
    Deficits (NOT Unilateral Deafness):** A lesion of the **left
    primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
    42) causes **contralateral or bilateral hearing deficits** — NOT
    **unilateral deafness** — because the **auditory pathway** is
    **bilateral from the superior olivary complex onward**. **This is
    the critical contrast with cochlear nuclei lesions** — **cochlear
    nuclei lesions** cause **unilateral deafness**; **cortical
    auditory lesions** do **not**. Consumers must **not** conflate a
    **cochlear nuclei lesion** with a **cortical auditory lesion**.

*   **Auditory Neuropathy Spectrum Disorder (ANSD) — Cochlear Nerve or
    Hair Cell Lesion:** **Auditory neuropathy spectrum disorder** is a
    **hearing disorder** in which the **outer hair cell function** is
    **preserved** (otoacoustic emissions are present) but the
    **auditory nerve response** is **disrupted** (auditory brainstem
    response is abnormal or absent). It is caused by **lesions at the
    cochlear nerve level** (or **inner hair cell level**, or
    **synaptic level**) — **NOT** at the **cochlear nuclei level**.
    Consumers must **not** conflate **ANSD** with a **cochlear nuclei**
    lesion.

*   **Central Auditory Processing Disorder (CAPD) — Cortical or
    Brainstem Auditory Pathway Lesion:** **Central auditory processing
    disorder** is a **heterogeneous group** of **auditory processing
    deficits** — **difficulty understanding speech in noise**,
    **difficulty localizing sound**, **difficulty discriminating
    similar sounds** — caused by **lesions or dysfunctions** at various
    levels of the **central auditory pathway** (including the **cochlear
    nuclei**, **superior olivary complex**, **inferior colliculus**,
    **medial geniculate body**, and **auditory cortex**). **CAPD is
    not specific to the cochlear nuclei** — it is a **functional
    diagnosis** that may involve the **cochlear nuclei** as **one
    component**. Consumers must **not** conflate **CAPD** with a
    **cochlear nuclei** lesion specifically.

*   **Lateral Pontine Syndrome (Marie-Foix) — Cochlear Nuclei
    Sparing:** **Marie-Foix syndrome** (lateral pontine tegmentum
    lesion) **typically spares the cochlear nuclei** — the classic
    Marie-Foix lesion is **ventromedial** to the cochlear nuclei, which
    sit on the **dorsolateral surface** of the inferior cerebellar
    peduncle. **This is a useful anatomical distinction** — **hearing
    loss** suggests a **more lateral** pontine lesion that reaches the
    cochlear nuclei (or a **nerve-level** lesion), while **spared
    hearing** is consistent with the classic **Marie-Foix** pattern.

*   **Lateral Medullary Syndrome (Wallenberg) — Cochlear Nuclei
    Sparing:** **Wallenberg syndrome** (lateral medullary lesion)
    **typically spares the cochlear nuclei** — they are **pontine**
    structures, above the medullary level of the Wallenberg lesion.
    **Hearing loss** is **not** a classic Wallenberg feature.
    Consumers must **not** conflate the **cochlear nuclei** with the
    **medullary structures** involved in Wallenberg syndrome.

*   **No Named "Cochlear Nuclei Syndrome":** The cochlear nuclei are a
    **three-population complex** — they have **no named clinical
    syndrome**. Their clinical relevance is **nucleus-specific** —
    **ipsilateral sensorineural hearing loss** (which is **the same
    symptom** as a **cochlear nerve lesion** or a **cochlear/cochlear
    hair cell lesion**, distinguishable only by **associated signs**
    and **imaging**).

**What is NOT here:** The cochlear nuclei are **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN
VIII nerve), **auditory neuropathy spectrum disorder** (cochlear nerve
or hair cell), or **central auditory processing disorder** (a
**heterogeneous functional diagnosis** involving multiple levels of the
auditory pathway). Their clinical relevance is **auditory-specific**,
via the **left cochlear nuclei** (hearing). **No named cochlear nuclei
syndrome exists.**

Lateralization Notes
--------------------
This is the **left** cochlear nuclei module. The cochlear nuclei are
**bilaterally symmetric** with the right cochlear nuclei and **strictly
mirrored** — and they carry **NO warning at the sub-container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right** cochlear
    nuclei are **structurally identical** — same three prose
    subdivisions (AVCN, PVCN, DCN), same auditory special sensory
    function, same bilateral framing. The bilateral symmetry is
    **strict**.

*   **Ipsilateral Cochlear Input (Structural Fact, NOT a Lateralization
    Warning):** The **left cochlear nuclei** receive **primary auditory
    axons from the left cochlea** (via the left spiral ganglion and
    left cochlear nerve) — **ipsilateral input**. The **right cochlear
    nuclei** receive input from the right cochlea. This **ipsilateral
    input** is a **structural fact** of the **auditory system** — the
    auditory pathway is **ipsilateral up to the superior olivary
    complex**, where **bilateral convergence** begins. It is **not** a
    functional lateralization. It is the **neural substrate** of
    **ipsilateral sensorineural hearing loss** in **cochlear nuclei**
    or **cochlear nerve** lesions.

*   **Contralateral Auditory Projections from Superior Olivary Complex
    Onward (Structural Fact, NOT a Lateralization Warning):** From the
    **superior olivary complex** onward, the **ascending auditory
    pathway** is **bilateral** — the **left cochlear nuclei** project
    **contralaterally** to the **right superior olivary complex** (via
    the **right trapezoid body**) and **ipsilaterally** to the **left
    superior olivary complex**. This is why **cortical auditory
    lesions** do **not** cause unilateral deafness — the **auditory
    cortex** receives **bilateral** input. **This is a structural fact
    of the auditory system**, not a functional lateralization.

*   **Bilateral Ears — Unilateral Deafness Is Localized to the Cochlea,
    Cochlear Nerve, or Cochlear Nuclei:** Because the **auditory
    pathway** is **bilateral from the superior olivary complex
    onward**, **unilateral deafness** is **only** caused by lesions at
    the level of the **cochlea**, the **cochlear nerve**, or the
    **cochlear nuclei**. **This is a structural fact of the auditory
    system** — it is **not** a functional lateralization, and it is
    **not** a warning. It is the **neural substrate** of the **clinical
    rule** that **unilateral deafness localizes to the peripheral or
    first-order central auditory pathway**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The cochlear
    nuclei are **SLEA-free** — they are **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the cochlear nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the cochlear
    nuclei are SPECIAL SENSORY AUDITORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The cochlear nuclei are
    **auditory special sensory brainstem nuclei** — consumers must
    **not** conflate them with the **amygdala** or with the **fear
    circuit**.

**A consumer that assumes "left cochlear nuclei = right cochlear
nuclei" will be structurally correct** — the two sides are **strictly
symmetric** (the ipsilateral input and bilateral projections are
structural facts, not lateralizations). The cochlear nuclei are a
**strict-mirror pair with NO warning at the sub-container level** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cranial_nerve_nuclei/right/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../metencephalon/cerebellum/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    cochlear nuclei's relationships to the **cochlear nerve**, the
    **cochlea**, the **spiral ganglion**, the **superior olivary
    complex**, the **inferior colliculus**, the **medial geniculate
    body**, the **primary auditory cortex**, the **trapezoid body**,
    the **lateral lemniscus**, the **inferior cerebellar peduncle**,
    the **cerebellum**, and the **CN V, VI, VII siblings** are
    documented as **prose and boundary data**, not as structural parents
    or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf at tree level — conceptual sub-container of THREE PROSE
    SUBDIVISIONS.** The **AVCN**, **PVCN**, and **DCN** are documented
    as **prose**, not as structural children. Consumers must not assume
    any exist as structural children; resolve sub-nucleus-level detail
    through the references.
*   **SPECIAL SENSORY AUDITORY — NOT general sensory.** The **cochlear
    nuclei** are **auditory special sensory** (hearing); they are **not**
    general sensory nuclei. Consumers must **not** conflate the cochlear
    nuclei with the **chief sensory trigeminal nucleus** or any other
    general sensory nucleus.
*   **NOT the vestibular nuclei — that is the OTHER sub-container.** The
    **cochlear nuclei** (auditory) and the **vestibular nuclei**
    (balance) are **different structures** — different sensory
    modalities, different peripheral receptors, different ascending
    pathways. Consumers must **not** conflate the two.
*   **GREY-MATTER NUCLEI — NOT the cochlear NERVE.** The **cochlear
    nuclei** are the **grey-matter neuron clusters**; the **cochlear
    nerve** is the **white-matter axon bundle**. Consumers must **not**
    conflate the two.
*   **NOT the cochlea or spiral ganglion — those are PERIPHERAL.** The
    **nuclei** are central; the **cochlea** and **spiral ganglion** are
    peripheral. Consumers must **not** conflate the two.
*   **NOT the vestibulocochlear nerve — that is the WHOLE CN VIII.** The
    **cochlear nuclei** receive the axons of the **cochlear division
    only**; the **vestibulocochlear nerve** carries both divisions.
    Consumers must **not** conflate the two.
*   **NOT the superior olivary complex, inferior colliculus, medial
    geniculate body, or primary auditory cortex — those are DOWNSTREAM.**
    The **cochlear nuclei** are the **first central auditory relay**.
    Consumers must **not** conflate them with any downstream auditory
    structure.
*   **NOT the trapezoid body or the lateral lemniscus — those are
    WHITE-MATTER TRACTS.** The **nuclei** are grey matter; the **tracts**
    are white matter. Consumers must **not** conflate the two.
*   **NOT the inferior cerebellar peduncle — that is the WHITE-MATTER
    TRACT the nuclei SIT ON.** The **nuclei** are grey matter; the
    **peduncle** is white matter. The **anatomical juxtaposition** is a
    **classic source of confusion** — consumers must **not** conflate
    the two.
*   **NOT the cerebellum — that is the metencephalic SIBLING the
    peduncle connects to.** The **cochlear nuclei** are the **auditory
    brainstem relay**; the **cerebellum** is the **metencephalic
    cerebellar half**. Consumers must **not** conflate the two.
*   **NOT the CN V, VI, VII sibling nuclei.** The **chief sensory
    trigeminal nucleus**, **motor trigeminal nucleus**, **abducens
    nucleus**, **facial nerve nucleus**, and **superior salivatory
    nucleus** are **different structures** for **different cranial
    nerves and different functional systems**. Consumers must **not**
    conflate the cochlear nuclei with any of them.
*   **THREE FUNCTIONALLY DISTINCT PROSE SUBDIVISIONS — AVCN vs. PVCN
    vs. DCN.** The **AVCN** (sound localization), **PVCN** (temporal
    onset and speech), and **DCN** (spectral cues and vertical
    localization) are **prose**, not structural children. Consumers must
    **not** treat the cochlear nuclei as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The cochlear
    nuclei are **not** an extended-amygdala component, and they carry
    **no SLEA warning**.
*   **NOT the fear-output — the cochlear nuclei are SPECIAL SENSORY
    AUDITORY.** The **fear-output** structure is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **cochlear nuclei** are **auditory special sensory
    brainstem nuclei** — they are **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The cochlear nuclei are a local leaf under
    the vestibulocochlear_nuclei sub-container, not a cross-listed leaf.
*   **No nested cross-listing.** The cochlear nuclei have no nested
    dual-framing module. They are a single leaf (at the tree level) with
    three prose subdivisions.
*   **Structural parity with right cochlear nuclei — strict mirror with
    NO warning.** Left and right cochlear nuclei modules are
    **structurally identical** — same leaf status, same **auditory
    special sensory** framing, same **three prose subdivisions**
    (AVCN, PVCN, DCN), same **SLEA-free** status, same **no warning** at
    the sub-container level.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei import cochlear_nuclei

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.left."
        "vestibulocochlear_nuclei.cochlear_nuclei"
    )

**Do not** assume the cochlear nuclei are a **structural container**. They
are a **leaf at the tree level** — with **three conceptual prose
subdivisions** (AVCN, PVCN, DCN) that are **not** structural children.

**Do not** assume the cochlear nuclei are the **cochlear nerve**. The
**cochlear nerve** is the **white-matter axon bundle**; the **cochlear
nuclei** are the **grey-matter neuron clusters**. They are **different
structures**.

**Do not** assume the cochlear nuclei are the **cochlea** or the
**spiral ganglion**. Those are **peripheral** structures; the **cochlear
nuclei** are **central**.

**Do not** assume the cochlear nuclei are the **vestibular nuclei**. The
**vestibular nuclei** are the **other sub-container** of the
vestibulocochlear nuclei — they subserve **balance and spatial
orientation**; the **cochlear nuclei** subserve **hearing**.

**Do not** assume the cochlear nuclei are the **superior olivary
complex**, **inferior colliculus**, **medial geniculate body**, or
**primary auditory cortex**. Those are **downstream** auditory
structures — the **cochlear nuclei** are the **first central auditory
relay**.

**Do not** assume the cochlear nuclei are the **trapezoid body** or the
**lateral lemniscus**. Those are **white-matter tracts** that **carry**
the cochlear nuclei projections — the **nuclei** are the **grey-matter
neuron clusters** that **give rise to** them.

**Do not** assume the cochlear nuclei are the **inferior cerebellar
peduncle** or the **cerebellum**. The **nuclei** sit **on** the
**inferior cerebellar peduncle** (a **white-matter tract** that connects
to the **cerebellum**), but the **nuclei**, the **peduncle**, and the
**cerebellum** are **different structures**.

**Do not** assume the cochlear nuclei are the **CN V, VI, or VII sibling
nuclei**. The **chief sensory trigeminal nucleus**, **motor trigeminal
nucleus**, **abducens nucleus**, **facial nerve nucleus**, and
**superior salivatory nucleus** are **different structures** for
**different cranial nerves and functional systems**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the cochlear nuclei. **The cochlear nuclei are SLEA-FREE**
— they are **not** an extended-amygdala component, and they are **NOT
part of the fear circuit**.

Iterating the cochlear nuclei's (empty) structural children (recommended
consumer pattern)::

    COCHLEAR_NUCLEI_CHILDREN = ()
    # The cochlear nuclei are a leaf at the tree level. The AVCN, PVCN,
    # and DCN are prose subdivisions, not structural children.

Reaching the cochlear nerve (recommended consumer pattern — the
white-matter axon bundle)::

    # The cochlear nerve (the cochlear division of left CN VIII) is the
    # WHITE-MATTER axon bundle:
    #
    #   peripheral: left cochlea -> left spiral ganglion -> left
    #               cochlear nerve (CN VIII cochlear division)
    #
    # The nuclei are the CENTRAL sensory relays; the nerve is the
    # PERIPHERAL conduction infrastructure.

Reaching the spiral ganglion (recommended consumer pattern — the
peripheral sensory ganglion)::

    # The spiral ganglion (cochlear ganglion) is the PERIPHERAL sensory
    # ganglion containing the primary auditory neuron cell bodies:
    #
    #   peripheral: left spiral ganglion
    #
    # The nuclei are CENTRAL; the ganglion is PERIPHERAL.

Reaching the vestibular nuclei (recommended consumer pattern — the OTHER
sub-container of the vestibulocochlear nuclei)::

    # The vestibular nuclei are the VESTIBULAR sub-container of the
    # vestibulocochlear nuclei:
    #
    #   .../vestibulocochlear_nuclei/vestibular_nuclei/
    #
    # The cochlear nuclei (auditory) and the vestibular nuclei (balance)
    # are FUNCTIONALLY DISTINCT — different sensory modalities, different
    # peripheral receptors, different ascending pathways.

Reaching the superior olivary complex (recommended consumer pattern —
the downstream auditory relay)::

    # The superior olivary complex is the DOWNSTREAM auditory relay:
    #
    #   .../pons/superior_olivary_complex/left/
    #
    # The cochlear nuclei PROJECT TO the superior olivary complex (via
    # the trapezoid body); the superior olivary complex is DOWNSTREAM of
    # the cochlear nuclei.

Reaching the inferior colliculus (recommended consumer pattern — the
downstream midbrain auditory relay)::

    # The inferior colliculus is the DOWNSTREAM midbrain auditory relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/
    #
    # The cochlear nuclei are UPSTREAM of the inferior colliculus; the
    # inferior colliculus is DOWNSTREAM of the cochlear nuclei.

Reaching the medial geniculate body (recommended consumer pattern — the
downstream thalamic auditory relay)::

    # The medial geniculate body is the DOWNSTREAM thalamic auditory
    # relay:
    #
    #   .../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/
    #
    # The cochlear nuclei are UPSTREAM of the medial geniculate body; the
    # medial geniculate body is DOWNSTREAM of the cochlear nuclei.

Reaching the primary auditory cortex (recommended consumer pattern — the
downstream cortical auditory target)::

    # The primary auditory cortex (Heschl's gyrus, Brodmann areas 41 and
    # 42) is the DOWNSTREAM cortical auditory target:
    #
    #   .../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/
    #
    # The cochlear nuclei are UPSTREAM of the primary auditory cortex;
    # the primary auditory cortex is DOWNSTREAM of the cochlear nuclei.

Reaching the trapezoid body (recommended consumer pattern — the
white-matter decussating tract)::

    # The trapezoid body is the WHITE-MATTER decussating tract:
    #
    #   .../white_matter/.../trapezoid_body/  (or equivalent path)
    #
    # The cochlear nuclei GIVE RISE TO the trapezoid body axons; the
    # trapezoid body CARRIES them to the CONTRALATERAL superior olivary
    # complex.

Reaching the inferior cerebellar peduncle (recommended consumer pattern —
the white-matter tract the nuclei SIT ON)::

    # The inferior cerebellar peduncle is the WHITE-MATTER tract on whose
    # dorsolateral surface the cochlear nuclei are anatomically located:
    #
    #   .../white_matter/.../inferior_cerebellar_peduncle/  (or equivalent path)
    #
    # The cochlear nuclei are GREY MATTER that sit ON the peduncle; the
    # peduncle is WHITE MATTER that connects to the cerebellum. They are
    # DIFFERENT STRUCTURES — the anatomical juxtaposition is a classic
    # source of confusion.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
            f"{side}.vestibulocochlear_nuclei.cochlear_nuclei"
        )
        # resolve cn_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The cochlear nuclei's three prose subdivisions are prose, not
    # modules:
    #   AVCN (anterior ventral cochlear nucleus) -> spherical and
    #       globular bushy cells; interaural time and intensity
    #       difference processing; principal output to superior olivary
    #       complex via trapezoid body; SOUND LOCALIZATION
    #   PVCN (posterior ventral cochlear nucleus) -> octopus cells;
    #       temporal onset and rapid transient detection; critical for
    #       SPEECH PERCEPTION; projects via intermediate acoustic stria
    #       to inferior colliculus and contralateral cochlear nuclei
    #   DCN (dorsal cochlear nucleus) -> fusiform and cartwheel cells;
    #       cerebellum-like cortical structure; spectral cue processing
    #       and complex sound feature extraction; SPECTRAL CUES for
    #       VERTICAL SOUND LOCALIZATION
    #
    # Do not attempt to resolve these as sub-paths of the cochlear
    # nuclei — resolve them at the prose subdivision level through the
    # references.

References
----------
*   **Canonical auditory anatomy:** Pickles, J.O. (2015). *An
    Introduction to the Physiology of Hearing*, 4th ed. (Cochlear nuclei
    and the ascending auditory pathway — definitive.)
*   **Auditory brainstem — review:** Cant, N.B., Benson, C.G. (2003).
    "Parallel auditory pathways: projection patterns of the different
    neuronal populations in the cochlear nuclei." *Brain Research
    Bulletin* 60:457–474. (Cochlear nuclei subdivisions and projections
    to the superior olivary complex.)
*   **Cochlear nuclei cell types:** Osen, K.K. (1969). "Cytoarchitecture
    of the cochlear nuclei in the cat." *Journal of Comparative
    Neurology* 136:453–484. (Cytoarchitectonic subdivisions of the
    cochlear nuclei — AVCN, PVCN, DCN and their cell types.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Cochlear nuclei in
    overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An Atlas
    of Structures, Sections, and Systems*, 8th ed. (Cochlear nuclei and
    the pontomedullary junction.)
*   **Sound localization:** Grothe, B., Pecka, M., McAlpine, D. (2010).
    "Mechanisms of sound localization and coding in mammals."
    *Physiological Reviews* 90:983–1012. (AVCN and superior olivary
    complex — interaural time and intensity difference processing.)
*   **Temporal processing and speech:** Oertel, D., Bal, R., Gardner,
    S.M., Smith, P.H., Joris, P.X. (2000). "Detection of synchrony in
    the activity of auditory nerve fibers from the cat." *Journal of
    Neurophysiology* 83:2856–2869. (PVCN octopus cells and temporal
    onset detection.)
*   **DCN spectral processing:** Young, E.D., Davis, K.A. (2002).
    "Circuitry and function of the dorsal cochlear nucleus." In
    *Integrative Functions in the Mammalian Auditory Pathway*. (DCN
    fusiform cells and spectral cue processing for vertical sound
    localization.)
*   **Acoustic neuroma (contrast — the CN VIII nerve, not the nuclei):**
    Matthies, C., Samii, M. (1997). "Management of 1000 vestibular
    schwannomas (acoustic neuromas): clinical presentation."
    *Neurosurgery* 40:1–10. (Acoustic neuroma — vestibular schwannoma of
    the CN VIII nerve; distinct from the cochlear nuclei.)
*   **Cortical auditory lesions (contrast — NOT unilateral deafness):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Cortical auditory lesions do not cause unilateral
    deafness — bilateral auditory pathway from the superior olivary
    complex onward.)
*   **Auditory neuropathy spectrum disorder (contrast — cochlear nerve or
    hair cell lesion):** Starr, A., Picton, T.W., Sininger, Y., Hood,
    L.J., Berlin, C.I. (1996). "Auditory neuropathy." *Brain*
    119:741–753. (Auditory neuropathy — cochlear nerve or hair cell
    lesion; distinct from the cochlear nuclei.)
*   **Central auditory processing disorder (contrast — heterogeneous
    functional diagnosis):** American Speech-Language-Hearing
    Association (2005). *(Central) Auditory Processing Disorders*.
    (CAPD — heterogeneous functional diagnosis involving multiple levels
    of the auditory pathway; not specific to the cochlear nuclei.)
*   **Lateral pontine syndrome (contrast — cochlear nuclei typically
    spared):** Marie, P., Foix, C. (1913). "Les lésions des artères du
    cervelet." *Revue Neurologique* 25:177–190. (Lateral pontine
    syndrome — ventromedial pontine tegmentum lesion; cochlear nuclei
    typically spared.)
*   **Wallenberg syndrome (contrast — cochlear nuclei typically
    spared):** Wallenberg, A. (1901). "Acute bulbar paralysis (embolic
    obstruction of the posterior inferior cerebellar artery)." *Archiv
    für Psychiatrie und Nervenkrankheiten* 34:923–959. (Lateral medullary
    syndrome — medullary lesion; cochlear nuclei typically spared.)
*   **Superior olivary complex (contrast — downstream auditory relay):**
    Grothe, B., Pecka, M., McAlpine, D. (2010). "Mechanisms of sound
    localization and coding in mammals." *Physiological Reviews*
    90:983–1012. (Superior olivary complex — downstream of the cochlear
    nuclei.)
*   **Inferior colliculus (contrast — downstream midbrain auditory
    relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002). "The
    inferior colliculus: a hub for the central auditory system." In
    *Integrative Functions in the Mammalian Auditory Pathway*. (Inferior
    colliculus — downstream of the cochlear nuclei.)
*   **Medial geniculate body (contrast — downstream thalamic auditory
    relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The Inferior
    Colliculus: A Hub for the Central Auditory System*. (Medial
    geniculate body — downstream of the cochlear nuclei.)
*   **Primary auditory cortex (contrast — downstream cortical auditory
    target):** Pickles, J.O. (2015). *An Introduction to the Physiology
    of Hearing*, 4th ed. (Primary auditory cortex — downstream of the
    cochlear nuclei.)
*   **Inferior cerebellar peduncle (contrast — the white-matter tract the
    nuclei SIT ON):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Inferior cerebellar peduncle and
    the cochlear nuclei — the nuclei sit on the dorsolateral surface of
    the peduncle.)
*   **Vestibular nuclei (contrast — the OTHER sub-container of the
    vestibulocochlear nuclei):** Goldberg, J.M., et al. (2012). *The
    Vestibular System: A Sixth Sense*. (Vestibular nuclei — balance and
    spatial orientation; distinct from the cochlear nuclei.)
*   **SLEA (contrast — the cochlear nuclei are not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the cochlear nuclei.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the cochlear nuclei.)
*   NeuroNames — Cochlear nuclei (left); FMA — Cochlear nuclei (left
    member).
"""