"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei
========================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── left
                    └── vestibulocochlear_nuclei   <-- THIS MODULE
                        ├── cochlear_nuclei
                        └── vestibular_nuclei

**Primary synonym:** Left vestibulocochlear nuclei; left octavus nuclei;
left CN VIII nuclei; left cochlear and vestibular nuclear complex; "the
left auditory-vestibular brainstem nuclear group."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**bilateral sub-container** of **brainstem special sensory nuclei** — a
**heterogeneous collection** of **left-side special sensory nuclei** in
the **left pontomedullary junction** that **receive** the **left
vestibulocochlear nerve** (left CN VIII). It is the **sole central
target** of left CN VIII and the **brainstem relay** for **left hearing**
and **left balance**.
**Part of:** The **left** container of the **cranial_nerve_nuclei**
container — specifically, the **special sensory** component. The **left**
container is the **left-side half** of the pontine cranial-nerve nuclear
collection.
**Structural parent:** ``.../cranial_nerve_nuclei/left/`` → **direct
child** of the left container.
**Structural children:** **Two sub-containers** — ``cochlear_nuclei``
(left auditory relay) and ``vestibular_nuclei`` (left balance and spatial
orientation relay). Each is itself a **sub-container** of the
**vestibulocochlear nuclei**.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
vestibulocochlear nuclei is a CONTAINER, not a leaf.** It has **two
structural children** (``cochlear_nuclei`` and ``vestibular_nuclei``),
each of which is itself a **sub-container** with its own children.
Consumers must **not** treat the vestibulocochlear nuclei as a leaf, and
must **not** assume the cochlear and vestibular nuclei are absent — they
are its **direct structural children**.
**Boundary status (SPECIAL SENSORY — NOT a general sensory nucleus):**
**Boundary case — the vestibulocochlear nuclei is SPECIAL SENSORY, NOT
general sensory.** Unlike the **chief sensory trigeminal nucleus**
(general sensory — discriminative touch from the face), the
**vestibulocochlear nuclei** (here) are **special sensory** — they
subserve **hearing** (cochlear nuclei) and **balance and spatial
orientation** (vestibular nuclei). They are **DIFFERENT STRUCTURES** —
different sensory modalities (special vs. general), different cranial
nerves (VIII vs. V), different peripheral receptors (hair cells in the
cochlea and vestibular apparatus vs. mechanoreceptors in the face).
Consumers must **not** conflate the **vestibulocochlear nuclei** with the
**chief sensory trigeminal nucleus** or any other general sensory nucleus.
**Boundary status (GREY-MATTER NUCLEI — NOT the vestibulocochlear NERVE):**
**Boundary case — the vestibulocochlear nuclei are the GREY-MATTER
NUCLEI, NOT the vestibulocochlear nerve (CN VIII).** The **left
vestibulocochlear nerve** (left CN VIII) is the **white-matter axon
bundle** that **carries** the **primary sensory axons** from the **left
cochlea** (hearing) and the **left vestibular apparatus** (balance) to
the **left vestibulocochlear nuclei**. The **vestibulocochlear nuclei**
(here) are the **grey-matter neuron clusters** that **receive** those
axons and **relay** the auditory and vestibular signals **upward**.
They are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**nerve** is white matter. Consumers must **not** conflate the **nuclei**
with the **nerve** — the nuclei are the **central sensory relays**; the
nerve is the **peripheral conduction infrastructure**.
**Boundary status (NOT the cochlea or vestibular apparatus — those are
PERIPHERAL RECEPTORS):** **Boundary case — the vestibulocochlear nuclei
are NOT the cochlea or the vestibular apparatus.** The **left cochlea**
(hearing) and the **left vestibular apparatus** — the **semicircular
canals**, **utricle**, and **saccule** (balance and spatial
orientation) — are the **peripheral sensory receptors** whose **hair
cells** transduce sound and head motion into neural signals. The
**vestibulocochlear nuclei** (here) are the **central grey-matter
relays** that **receive** those signals. They are **DIFFERENT
STRUCTURES** — the **receptors** are peripheral sensory organs; the
**nuclei** are central nervous system. Consumers must **not** conflate
the **central nuclei** with the **peripheral receptors**.
**Boundary status (NOT the spiral ganglion or Scarpa's ganglion — those
are PERIPHERAL SENSORY GANGLIA):** **Boundary case — the
vestibulocochlear nuclei are NOT the spiral ganglion or Scarpa's
ganglion.** The **left spiral ganglion** (cochlear ganglion) is the
**peripheral sensory ganglion** that contains the **primary auditory
neuron cell bodies** for the left cochlea. **Scarpa's ganglion**
(vestibular ganglion) is the **peripheral sensory ganglion** that
contains the **primary vestibular neuron cell bodies** for the left
vestibular apparatus. The **vestibulocochlear nuclei** (here) are the
**central grey-matter nuclei** that **receive** the axons from those
ganglia. They are **DIFFERENT STRUCTURES** — the **ganglia** are
peripheral; the **nuclei** are central. Consumers must **not** conflate
the **central nuclei** with the **peripheral ganglia**.
**Boundary status (NOT the superior olivary complex — that is DOWNSTREAM
of the cochlear nuclei):** **Boundary case — the vestibulocochlear
nuclei are NOT the superior olivary complex.** The **left superior
olivary complex**
(``.../pons/superior_olivary_complex/left/``) is the **auditory
brainstem relay** that **receives** the **projections** from the **left
cochlear nuclei** (and the **right cochlear nuclei**, via the **trapezoid
body**) and **processes** **interaural time and intensity differences**
for **sound localization**. The **vestibulocochlear nuclei** (here) are
**upstream** of the superior olivary complex — they are the **first
central relay** for audition. They are **DIFFERENT STRUCTURES** — the
**cochlear nuclei** are the **first-order central auditory relay**; the
**superior olivary complex** is the **second-order binaural processing
center**. Consumers must **not** conflate the **vestibulocochlear
nuclei** with the **superior olivary complex**.
**Boundary status (NOT the inferior colliculus — that is MIDBRAIN and it
is DOWNSTREAM):** **Boundary case — the vestibulocochlear nuclei are NOT
the inferior colliculus.** The **left inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
is the **midbrain auditory relay** that **receives** the **ascending
auditory projections** from the **superior olivary complex** and the
**lateral lemniscus** and **projects** to the **medial geniculate body**
of the thalamus. The **vestibulocochlear nuclei** (here) are
**upstream** of the inferior colliculus — they are the **first central
relay**. Consumers must **not** conflate the **vestibulocochlear nuclei**
with the **inferior colliculus**.
**Boundary status (NOT the medial geniculate body — that is THALAMIC and
it is DOWNSTREAM):** **Boundary case — the vestibulocochlear nuclei are
NOT the medial geniculate body.** The **left medial geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
is the **thalamic auditory relay** that **receives** the **ascending
auditory projections** from the **inferior colliculus** and **projects**
to the **primary auditory cortex**. The **vestibulocochlear nuclei**
(here) are **upstream** of the medial geniculate body — they are the
**first central relay**. Consumers must **not** conflate the
**vestibulocochlear nuclei** with the **medial geniculate body**.
**Boundary status (NOT the primary auditory cortex — that is CORTICAL
and it is DOWNSTREAM):** **Boundary case — the vestibulocochlear nuclei
are NOT the primary auditory cortex.** The **left primary auditory
cortex** (Heschl's gyrus, Brodmann areas 41 and 42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
is the **cortical target** of the **ascending auditory pathway**. The
**vestibulocochlear nuclei** (here) are **far upstream** of the primary
auditory cortex — they are the **first central relay**. Consumers must
**not** conflate the **vestibulocochlear nuclei** with the **primary
auditory cortex**.
**Boundary status (NOT the vestibular cortex — that is CORTICAL and it
is DOWNSTREAM):** **Boundary case — the vestibulocochlear nuclei are NOT
the vestibular cortex.** The **vestibular cortex** — a **distributed
cortical network** including the **parieto-insular vestibular cortex
(PIVC)**, parts of the **parietal lobe** (area 2v, area 3a), the
**insular cortex**, and the **superior temporal gyrus** — is the
**cortical target** of the **ascending vestibular pathway**. The
**vestibulocochlear nuclei** (here) are **far upstream** of the
vestibular cortex — they are the **first central relay**. Consumers must
**not** conflate the **vestibulocochlear nuclei** with the **vestibular
cortex**.
**Boundary status (NOT the cerebellum — that is a metencephalic SIBLING,
and it receives vestibular projections):** **Boundary case — the
vestibulocochlear nuclei are NOT the cerebellum.** The **left cerebellum**
(``.../metencephalon/cerebellum/hemispheres/left/``) is the **left
metencephalic cerebellar half** — it has its **own nuclei** (left
dentate, left fastigial, left interposed: left emboliform + left
globose) and its **own cortex**. The **left vestibular nuclei** project
**directly** to the **left cerebellum** (especially the **flocculonodular
lobe** and the **fastigial nucleus**) to **drive** the
**vestibulocerebellar** pathways for **balance and gait**. This
**cerebellar projection** is a **structural fact** — but the
**cerebellum** and the **vestibulocochlear nuclei** are **DIFFERENT
STRUCTURES**. Consumers must **not** conflate the **vestibulocochlear
nuclei** with the **cerebellum**.
**Boundary status (NOT the medial longitudinal fasciculus — that is the
WHITE-MATTER TRACT that carries vestibular projections):** **Boundary
case — the vestibulocochlear nuclei are NOT the medial longitudinal
fasciculus (MLF).** The **MLF** is the **white-matter tract** that
**carries** the **ascending and descending projections** from the
**vestibular nuclei** to the **extraocular motor nuclei** (III, IV, VI),
the **abducens internuclear neurons**, the **cervical spinal cord**, and
the **contralateral vestibular nuclei**. The **vestibular nuclei** (here)
are the **grey-matter neuron clusters** that **give rise to** those
axons. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter;
the **MLF** is white matter. Consumers must **not** conflate the
**vestibulocochlear nuclei** with the **MLF**.
**Boundary status (NOT the vestibulo-ocular reflex — that is a CIRCUIT,
not a structure):** **Boundary case — the vestibulocochlear nuclei are
NOT the vestibulo-ocular reflex (VOR); the VOR is a CIRCUIT.** The
**VOR** is a **three-neuron reflex arc** whose **afferent limb** is the
**vestibular nerve** from the **semicircular canals**, whose **central
node** is the **vestibular nuclei**, and whose **efferent limb** is the
**abducens nucleus** (for horizontal VOR) or the **oculomotor/trochlear
nuclei** (for vertical VOR), via the **MLF**. The **vestibulocochlear
nuclei** are **one node** in this circuit — the **central node** — not
the circuit itself. Consumers must **not** conflate the
**vestibulocochlear nuclei** with the **VOR**.
**Boundary status (NOT the vestibulospinal tracts — those are the
WHITE-MATTER DESCENDING PATHWAYS):** **Boundary case — the
vestibulocochlear nuclei are NOT the vestibulospinal tracts.** The
**lateral vestibulospinal tract** and the **medial vestibulospinal
tract** are the **descending white-matter pathways** that **carry** the
**vestibular nuclei projections** to the **spinal cord** — they
**mediate postural adjustments** and **head stabilization**. The
**vestibular nuclei** (here) are the **grey-matter neuron clusters**
that **give rise to** those axons. They are **DIFFERENT STRUCTURES** —
the **nuclei** are grey matter; the **tracts** are white matter.
Consumers must **not** conflate the **vestibulocochlear nuclei** with
the **vestibulospinal tracts**.
**Boundary status (NOT the cochlear or vestibular NERVE — that is the
WHOLE CN VIII):** **Boundary case — the vestibulocochlear nuclei are NOT
the vestibulocochlear nerve.** The **left vestibulocochlear nerve** (left
CN VIII) is the **whole nerve** — it contains the **cochlear division**
(from the left cochlea, via the spiral ganglion) and the **vestibular
division** (from the left vestibular apparatus, via Scarpa's ganglion).
The **vestibulocochlear nuclei** (here) are the **central grey-matter
nuclei** that **receive** the axons of both divisions. They are
**DIFFERENT STRUCTURES** — the **nuclei** are central grey matter; the
**nerve** is the **whole peripheral nerve** that carries the primary
sensory axons. Consumers must **not** conflate the
**vestibulocochlear nuclei** with the **vestibulocochlear nerve**.
**Boundary status (NOT the trigeminal ganglion, geniculate ganglion, or
other sensory ganglia — those are DIFFERENT NERVES):** **Boundary case —
the vestibulocochlear nuclei are NOT the trigeminal ganglion, the
geniculate ganglion, or any other cranial-nerve sensory ganglion.** Those
ganglia are **peripheral sensory ganglia** on **different cranial nerves**
(CN V, CN VII) containing **different primary sensory neuron cell
bodies**. The **vestibulocochlear nuclei** (here) are the **central
grey-matter nuclei** for **CN VIII** — they receive axons from the
**spiral ganglion** (cochlear) and **Scarpa's ganglion** (vestibular),
**not** from the trigeminal or geniculate ganglia. Consumers must **not**
conflate the **CN VIII central nuclei** with the **peripheral sensory
ganglia of other cranial nerves**.
**Boundary status (NOT the facial nerve nucleus, superior salivatory
nucleus, abducens nucleus, chief sensory trigeminal nucleus, or motor
trigeminal nucleus — those are SIBLINGS):** **Boundary case — the
vestibulocochlear nuclei are NOT the facial nerve nucleus, superior
salivatory nucleus, abducens nucleus, chief sensory trigeminal nucleus,
or motor trigeminal nucleus.** Those are **sibling** nuclei under the
left container of the cranial_nerve_nuclei — they subserve **different
cranial nerves** (VII, VII, VI, V, V) and **different functional systems**
(branchial motor, parasympathetic, somatic motor, general sensory,
branchial motor). The **vestibulocochlear nuclei** (here) are the **CN
VIII special sensory nuclei** — **hearing** and **balance**. Consumers
must **not** conflate the **vestibulocochlear nuclei** with any of the
**CN V, CN VI, or CN VII sibling nuclei**.
**Boundary status (NOT a single uniform system — TWO functionally
distinct SUB-CONTAINERS):** **Boundary case — the vestibulocochlear
nuclei is a HETEROGENEOUS collection of TWO functionally distinct
sub-containers, not a single uniform system.** The **cochlear nuclei**
subserve **hearing** (via the **cochlear division** of CN VIII); the
**vestibular nuclei** subserve **balance and spatial orientation** (via
the **vestibular division** of CN VIII). These two sub-containers are
**structurally distinct** — each has its **own sub-children** — and
their **functional systems** are **completely different** (auditory vs.
vestibular). The tree wires them as **two structural children** of the
vestibulocochlear nuclei. Consumers must **not** treat the
vestibulocochlear nuclei as a single uniform system — it is a
**two-sub-container** collection of **functionally distinct** special
sensory nuclei.
**Boundary status (NOT the whole cranial_nerve_nuclei container — a
sub-container child of the left container):** **Boundary case — the
vestibulocochlear nuclei are a SUB-CONTAINER child of the left container,
not the container itself, and not the whole cranial_nerve_nuclei
container.** The **left** container contains the **vestibulocochlear
nuclei** and **five other children**. The **cranial_nerve_nuclei**
container contains **two structural children** (``left`` and ``right``).
Consumers must **not** conflate the vestibulocochlear nuclei with the
**left** container or the **cranial_nerve_nuclei** container.
**Boundary status (NOT the right vestibulocochlear nuclei — strict
mirror, no warning):** **Boundary case — the left vestibulocochlear
nuclei are NOT the right vestibulocochlear nuclei; the two are a STRICT
MIRROR PAIR with NO warning at the sub-container level.** The **right
vestibulocochlear nuclei**
(``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/``) is the
**structurally identical** right-side counterpart — same two
sub-containers (cochlear and vestibular nuclei), same special sensory
function, same bilateral framing. The two sides are **strictly
mirrored** — any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere. Consumers must
**not** import a lateralization warning into the left vestibulocochlear
nuclei — there is **none at the sub-container level** beyond the
**auditory and vestibular structural facts** documented below.
**Boundary status (SLEA-FREE — the vestibulocochlear nuclei are NOT an
extended-amygdala component):** **Boundary case — the
vestibulocochlear nuclei are SLEA-FREE.** The **SLEA overlap** belongs
to the **central nucleus** (the **only SLEA component** in the amygdala)
and to the **BNST**, **ventral pallidum**, and **nucleus accumbens**
(wired elsewhere). The **vestibulocochlear nuclei** are **special
sensory brainstem nuclei** — they are **NOT** an extended-amygdala
component, and they carry **NO SLEA warning**. Consumers must **not**
import the SLEA warning into the vestibulocochlear nuclei — they are
**SLEA-free**.

Overview
--------
The vestibulocochlear nuclei are the **special sensory** nuclei for
**left CN VIII** — the **sole central target** of the **left
vestibulocochlear nerve** and the **brainstem relay** for **left
hearing** and **left balance**. They are a **sub-container** under the
left container of the cranial_nerve_nuclei container, with **two
structural children** — the **cochlear nuclei** (left auditory relay)
and the **vestibular nuclei** (left balance and spatial orientation
relay).

**The vestibulocochlear nuclei are a CONTAINER, NOT a leaf.** Their
structural children are the **cochlear nuclei** and **vestibular
nuclei**, each of which is itself a **sub-container** with its own
children.

**The vestibulocochlear nuclei are SPECIAL SENSORY, NOT general
sensory.** The **cochlear nuclei** subserve **hearing** (special
auditory sense); the **vestibular nuclei** subserve **balance and
spatial orientation** (special vestibular sense). They are **DIFFERENT
STRUCTURES** from the **chief sensory trigeminal nucleus** (general
sensory — discriminative touch from the face) or any other general
sensory nucleus.

**The vestibulocochlear nuclei are the GREY-MATTER NUCLEI, NOT the
vestibulocochlear NERVE.** The **vestibulocochlear nerve** (left
CN VIII) is the **white-matter axon bundle** that **carries** the
primary sensory axons from the left cochlea and left vestibular
apparatus. The **vestibulocochlear nuclei** (here) are the **grey-matter
neuron clusters** that **receive** those axons. They are **DIFFERENT
STRUCTURES** — the **nuclei** are grey matter; the **nerve** is white
matter.

**The vestibulocochlear nuclei are a TWO-SUB-CONTAINER collection of
functionally distinct special sensory nuclei.** The **cochlear nuclei**
subserve **hearing**; the **vestibular nuclei** subserve **balance and
spatial orientation**. They are wired as **two structural children** of
the vestibulocochlear nuclei. Consumers must **not** treat the
vestibulocochlear nuclei as a single uniform system.

**The vestibulocochlear nuclei are SLEA-FREE.** They are **not** an
extended-amygdala component, and they carry **no SLEA warning**.

Sub-Container Composition (structural children, prose)
------------------------------------------------------
The vestibulocochlear nuclei contain **two sub-containers** — documented
as **structural children** (not as leaves of the vestibulocochlear
nuclei):

*   **Cochlear nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``)
    — the **left auditory relay** — the **first central relay** for
    **hearing**. They receive the **primary auditory axons** from the
    **left spiral ganglion** (via the **left cochlear nerve** — the
    cochlear division of left CN VIII) and **project** to the
    **superior olivary complex**, the **inferior colliculus**, and the
    **medial geniculate body** — the **ascending auditory pathway**.
    The **cochlear nuclei** are **subdivided** into **anterior ventral
    cochlear nucleus (AVCN)**, **posterior ventral cochlear nucleus
    (PVCN)**, and **dorsal cochlear nucleus (DCN)** — **prose
    subdivisions**, not structural children of the cochlear nuclei.
    **Hearing is the functional system** subserved by the cochlear
    nuclei.

*   **Vestibular nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **left balance and spatial orientation relay** — the **first
    central relay** for the **vestibular system**. They receive the
    **primary vestibular axons** from **Scarpa's ganglion** (via the
    **left vestibular nerve** — the vestibular division of left CN VIII)
    and **project** to the **extraocular motor nuclei** (via the **MLF**
    — the **vestibulo-ocular reflex**), the **spinal cord** (via the
    **vestibulospinal tracts** — postural adjustment), the
    **cerebellum** (via the **vestibulocerebellar** pathways —
    balance and gait), and the **thalamus** and **cortex** (via the
    **ascending vestibular pathway** — conscious perception of balance
    and spatial orientation). The **vestibular nuclei** are
    **subdivided** into **superior**, **lateral (Deiters')**,
    **medial**, and **inferior** vestibular nuclei — **prose
    subdivisions**, not structural children of the vestibular nuclei.
    **Balance and spatial orientation are the functional systems**
    subserved by the vestibular nuclei.

**These two sub-containers are structural children of the
vestibulocochlear nuclei.** The vestibulocochlear nuclei's
**structural children** are the **cochlear nuclei** and **vestibular
nuclei**; each sub-container has its own **prose subdivisions** that
are **not** structural children. Consumers resolving sub-nucleus-level
detail go **through** the cochlear nuclei or the vestibular nuclei.

The Vestibulocochlear Nuclei / Vestibulocochlear Nerve Boundary
---------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Vestibulocochlear nuclei** (this module) — the **grey-matter
    neuron clusters** in the left pontomedullary junction.

*   **Vestibulocochlear nerve** (left CN VIII) — the **white-matter axon
    bundle** that carries the primary sensory axons from the left
    cochlea and left vestibular apparatus.

**They are DIFFERENT STRUCTURES.** The **nuclei** are the **central
sensory relays**; the **nerve** is the **peripheral conduction
infrastructure**. Consumers must **not** conflate the two — the
**vestibulocochlear nuclei** are the **nuclei**; the
**vestibulocochlear nerve** is the **nerve**.

The Vestibulocochlear Nuclei / Cochlea and Vestibular Apparatus Boundary
-----------------------------------------------------------------------
This is the **central vs. peripheral** boundary:

*   **Vestibulocochlear nuclei** (this module) — the **central
    grey-matter relays**.

*   **Cochlea** and **vestibular apparatus** (semicircular canals,
    utricle, saccule) — the **peripheral sensory receptors** whose
    **hair cells** transduce sound and head motion into neural signals.

**They are DIFFERENT STRUCTURES** — the **receptors** are peripheral
sensory organs; the **nuclei** are central nervous system. Consumers must
**not** conflate the **central nuclei** with the **peripheral receptors**.

The Vestibulocochlear Nuclei / Spiral Ganglion and Scarpa's Ganglion Boundary
---------------------------------------------------------------------------
This is the **central vs. peripheral** boundary — **nuclei vs. ganglia**:

*   **Vestibulocochlear nuclei** (this module) — the **central
    grey-matter nuclei** that **receive** the primary sensory axons.

*   **Spiral ganglion** (cochlear ganglion) and **Scarpa's ganglion**
    (vestibular ganglion) — the **peripheral sensory ganglia** that
    contain the **primary auditory and vestibular neuron cell bodies**.

**They are DIFFERENT STRUCTURES** — the **ganglia** are peripheral; the
**nuclei** are central. Consumers must **not** conflate the **central
nuclei** with the **peripheral ganglia**.

The Vestibulocochlear Nuclei / Superior Olivary Complex Boundary
----------------------------------------------------------------
This is the **auditory brainstem relay** boundary — **upstream vs.
downstream**:

*   **Vestibulocochlear nuclei** (this module) — the **first central
    auditory relay** (via the **cochlear nuclei**).

*   **Superior olivary complex**
    (``.../pons/superior_olivary_complex/left/``) — the **auditory
    brainstem relay** that **receives** the cochlear nuclei
    projections (via the **trapezoid body**) and **processes**
    **interaural time and intensity differences** for **sound
    localization**.

**The vestibulocochlear nuclei are UPSTREAM** of the superior olivary
complex — the **cochlear nuclei** are the **first-order central
auditory relay**; the **superior olivary complex** is the
**second-order binaural processing center**. Consumers must **not**
conflate the **vestibulocochlear nuclei** with the **superior olivary
complex**.

The Vestibulocochlear Nuclei / Inferior Colliculus Boundary
-----------------------------------------------------------
This is the **midbrain auditory relay** boundary — **upstream vs.
downstream**:

*   **Vestibulocochlear nuclei** (this module) — the **first central
    auditory relay**.

*   **Inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
    — the **midbrain auditory relay** that receives the ascending
    auditory projections from the superior olivary complex and the
    lateral lemniscus and projects to the medial geniculate body.

**The vestibulocochlear nuclei are UPSTREAM** of the inferior
colliculus — they are the **first central auditory relay**. Consumers
must **not** conflate the **vestibulocochlear nuclei** with the
**inferior colliculus**.

The Vestibulocochlear Nuclei / Medial Geniculate Body Boundary
-------------------------------------------------------------
This is the **thalamic auditory relay** boundary — **upstream vs.
downstream**:

*   **Vestibulocochlear nuclei** (this module) — the **first central
    auditory relay**.

*   **Medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
    — the **thalamic auditory relay** that receives the ascending
    auditory projections from the inferior colliculus and projects to
    the primary auditory cortex.

**The vestibulocochlear nuclei are UPSTREAM** of the medial geniculate
body — they are the **first central auditory relay**. Consumers must
**not** conflate the **vestibulocochlear nuclei** with the **medial
geniculate body**.

The Vestibulocochlear Nuclei / Primary Auditory Cortex Boundary
--------------------------------------------------------------
This is the **cortical auditory target** boundary — **upstream vs.
downstream**:

*   **Vestibulocochlear nuclei** (this module) — the **first central
    auditory relay**.

*   **Primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
    42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
    — the **cortical target** of the ascending auditory pathway.

**The vestibulocochlear nuclei are UPSTREAM** of the primary auditory
cortex — they are the **first central auditory relay**. Consumers must
**not** conflate the **vestibulocochlear nuclei** with the **primary
auditory cortex**.

The Vestibulocochlear Nuclei / Vestibular Cortex Boundary
---------------------------------------------------------
This is the **cortical vestibular target** boundary — **upstream vs.
downstream**:

*   **Vestibulocochlear nuclei** (this module) — the **first central
    vestibular relay** (via the **vestibular nuclei**).

*   **Vestibular cortex** — a **distributed cortical network** including
    the **parieto-insular vestibular cortex (PIVC)**, parts of the
    **parietal lobe** (area 2v, area 3a), the **insular cortex**, and
    the **superior temporal gyrus** — the **cortical target** of the
    ascending vestibular pathway.

**The vestibulocochlear nuclei are UPSTREAM** of the vestibular cortex —
they are the **first central vestibular relay**. Consumers must **not**
conflate the **vestibulocochlear nuclei** with the **vestibular cortex**.

The Vestibulocochlear Nuclei / Cerebellum Boundary
--------------------------------------------------
This is the **metencephalic-sibling** boundary — the cerebellum
**receives vestibular projections**:

*   **Vestibulocochlear nuclei** (this module) — the **first central
    vestibular relay** (via the **vestibular nuclei**).

*   **Cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/left/``) — the **left
    metencephalic cerebellar half**, with its **own nuclei** (left
    dentate, left fastigial, left interposed) and its **own cortex**.

**The left vestibular nuclei project directly to the left cerebellum**
(especially the **flocculonodular lobe** and the **fastigial nucleus**)
to drive the **vestibulocerebellar** pathways for **balance and gait**.
**This cerebellar projection is a structural fact** — but the
**cerebellum** and the **vestibulocochlear nuclei** are **DIFFERENT
STRUCTURES**. Consumers must **not** conflate the **vestibulocochlear
nuclei** with the **cerebellum**.

The Vestibulocochlear Nuclei / Medial Longitudinal Fasciculus Boundary
----------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Vestibulocochlear nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the MLF-projecting axons (via the
    vestibular nuclei).

*   **Medial longitudinal fasciculus (MLF)** — the **white-matter tract**
    that **carries** the ascending and descending projections from the
    vestibular nuclei to the extraocular motor nuclei (III, IV, VI), the
    abducens internuclear neurons, the cervical spinal cord, and the
    contralateral vestibular nuclei.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**MLF** is white matter. Consumers must **not** conflate the
**vestibulocochlear nuclei** with the **MLF**.

The Vestibulocochlear Nuclei / Vestibulo-Ocular Reflex Boundary
--------------------------------------------------------------
This is the **structure vs. circuit** boundary:

*   **Vestibulocochlear nuclei** (this module) — **one node** in the VOR
    — the **central node**.

*   **Vestibulo-ocular reflex (VOR)** — the **three-neuron reflex arc**
    whose **afferent limb** is the **vestibular nerve**, whose **central
    node** is the **vestibular nuclei**, and whose **efferent limb** is
    the **abducens nucleus** (horizontal VOR) or the **oculomotor/
    trochlear nuclei** (vertical VOR), via the **MLF**.

**They are DIFFERENT CONCEPTS** — the **vestibulocochlear nuclei** are
**structures**; the **VOR** is a **circuit**. Consumers must **not**
conflate the **vestibulocochlear nuclei** with the **VOR**.

The Vestibulocochlear Nuclei / Vestibulospinal Tracts Boundary
--------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the
**descending pathways**:

*   **Vestibulocochlear nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the vestibulospinal axons (via the
    vestibular nuclei).

*   **Lateral vestibulospinal tract** and **medial vestibulospinal
    tract** — the **descending white-matter pathways** that **carry**
    the vestibular nuclei projections to the spinal cord.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**tracts** are white matter. Consumers must **not** conflate the
**vestibulocochlear nuclei** with the **vestibulospinal tracts**.

The Vestibulocochlear Nuclei / CN V, VI, VII Sibling Nuclei Boundary
--------------------------------------------------------------------
This is the **sibling** boundary — **special sensory vs. other functional
systems**:

*   **Vestibulocochlear nuclei** (this module) — the **CN VIII special
    sensory** nuclei — **hearing** and **balance**.

*   **Chief sensory trigeminal nucleus** (CN V general sensory),
    **motor trigeminal nucleus** (CN V branchial motor), **abducens
    nucleus** (CN VI somatic motor), **facial nerve nucleus** (CN VII
    branchial motor), **superior salivatory nucleus** (CN VII
    parasympathetic) — the **sibling nuclei** under the left container
    of the cranial_nerve_nuclei.

**They are DIFFERENT STRUCTURES** — different cranial nerves, different
functional systems, different peripheral targets. Consumers must **not**
conflate the **vestibulocochlear nuclei** with any of the **CN V, CN VI,
or CN VII sibling nuclei**.

The Vestibulocochlear Nuclei / Right Vestibulocochlear Nuclei Boundary
----------------------------------------------------------------------
This is the **strict-mirror** boundary:

*   **Left vestibulocochlear nuclei** (this module) — the **left-side**
    special sensory nuclei for **left hearing** and **left balance**.

*   **Right vestibulocochlear nuclei**
    (``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/``) — the
    **structurally identical** right-side special sensory nuclei for
    **right hearing** and **right balance**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same two
sub-containers (cochlear and vestibular nuclei), same special sensory
function, same bilateral framing. **Auditory and vestibular
laterality facts are documented in the Lateralization Notes below,
not imported from elsewhere** — the structural connectivity facts
(contralateral auditory projections from the superior olivary complex
onward, ipsilateral vestibular projections to the extraocular nuclei
for the horizontal VOR) are **structural** and **not warnings**.
Consumers must **not** import a lateralization warning into the left
vestibulocochlear nuclei — there is **none at the sub-container level**.

The Vestibulocochlear Nuclei / Cranial Nerve Nuclei Container Boundary
----------------------------------------------------------------------
This is the **sub-container vs. container** boundary:

*   **Vestibulocochlear nuclei** (this module) — a **sub-container** child
    of the **left** container.

*   **Left container** (``.../cranial_nerve_nuclei/left/``) — the
    **left-side half** of the pontine cranial-nerve nuclear collection,
    with **six structural children** (including the vestibulocochlear
    nuclei).

*   **Cranial_nerve_nuclei container** (``.../cranial_nerve_nuclei/``) —
    the **whole pontine collection**, with **two structural children**
    (``left`` and ``right``).

**The vestibulocochlear nuclei are a sub-container child of the left
container.** Consumers must **not** conflate the vestibulocochlear
nuclei with the **left** container or the **cranial_nerve_nuclei**
container.

The Vestibulocochlear Nuclei / SLEA Boundary
--------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Vestibulocochlear nuclei** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The vestibulocochlear nuclei are NOT part of the SLEA continuum.** They
are **special sensory brainstem nuclei**, and they carry **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
vestibulocochlear nuclei.

Function in the Human Brain
---------------------------
The vestibulocochlear nuclei's functions are **the first central relay
for left hearing** and **the first central relay for left balance and
spatial orientation** — **NOT a single unified function**:

*   **Auditory Relay (Cochlear Nuclei):** The **cochlear nuclei**
    **receive** the **primary auditory axons** from the **left spiral
    ganglion** (via the **left cochlear nerve**) and **project** to the
    **superior olivary complex**, the **inferior colliculus**, and the
    **medial geniculate body** — the **ascending auditory pathway**.
    They are the **first central relay** for **hearing** — the **face
    analogue** of the **dorsal column nuclei** for the body, but
    subserving **audition** rather than **somatosensation**.

*   **Vestibular Relay — VOR (Vestibular Nuclei):** The **vestibular
    nuclei** **receive** the **primary vestibular axons** from
    **Scarpa's ganglion** (via the **left vestibular nerve**) and
    **project** to the **extraocular motor nuclei** (via the **MLF**)
    to **drive** the **vestibulo-ocular reflex (VOR)** — the
    **three-neuron reflex arc** that **stabilizes the eyes** during
    **head movement**.

*   **Vestibular Relay — Postural Adjustment (Vestibular Nuclei):** The
    **vestibular nuclei** **project** to the **spinal cord** via the
    **vestibulospinal tracts** to **mediate postural adjustments** and
    **head stabilization** in response to **vestibular input**.

*   **Vestibular Relay — Cerebellar Balance (Vestibular Nuclei):** The
    **vestibular nuclei** **project** to the **cerebellum** (especially
    the **flocculonodular lobe** and the **fastigial nucleus**) to
    **drive** the **vestibulocerebellar** pathways for **balance and
    gait**.

*   **Vestibular Relay — Conscious Perception (Vestibular Nuclei):** The
    **vestibular nuclei** **project** to the **thalamus** and
    **cortex** (via the **ascending vestibular pathway**) to **mediate**
    the **conscious perception** of **balance**, **spatial
    orientation**, and **self-motion**.

*   **NOT a neural processor in the classical sense.** The
    **vestibulocochlear nuclei** are **first-order central sensory
    relays** — they **receive** the primary sensory afferents and
    **project** them upward (auditory) or to reflex circuits (vestibular).
    The **processing** of auditory and vestibular signals is
    **distributed** across the **cochlear nuclei** (first central
    relay), the **superior olivary complex** and **inferior colliculus**
    (auditory brainstem processing), the **medial geniculate body**
    (thalamic relay), and the **primary auditory cortex** (cortical
    processing); and for the vestibular system, across the **vestibular
    nuclei** (first central relay), the **VOR** and **vestibulospinal**
    circuits (reflex processing), the **cerebellum** (balance and gait),
    and the **vestibular cortex** (conscious perception). The
    **vestibulocochlear nuclei** are the **first central relay** —
    **auditory and vestibular**.

**The unifying theme:** the vestibulocochlear nuclei are the **first
central sensory relays** for the **left auditory and vestibular
systems** — the **sole central target** of the **left vestibulocochlear
nerve**. They are **two-sub-container** (cochlear nuclei for hearing;
vestibular nuclei for balance), **special sensory** (hearing and balance,
not general sensory), **SLEA-free**, and **NOT the vestibulocochlear
nerve** — the **nerve** is the **white-matter axon bundle**; the
**nuclei** are the **grey-matter neuron clusters** that **receive** its
axons.

Associated Disorders
--------------------
The vestibulocochlear nuclei have **no single named "vestibulocochlear
nuclei syndrome" as a collection** — their clinical associations are
**sub-container-specific** (cochlear vs. vestibular) and
**nucleus-specific** within each sub-container:

*   **Cochlear Nuclei Lesion — Ipsilateral Sensorineural Hearing Loss:**
    A lesion of the **left cochlear nuclei** causes **left sensorineural
    hearing loss** — **unilateral deafness** (if the lesion is complete)
    or **impaired hearing** (if partial). Because the **auditory
    pathway** is **bilateral from the superior olivary complex onward**,
    a **cochlear nuclei lesion** is one of the **few lesions** that
    causes **unilateral** hearing loss — the **cortical auditory
    cortex** receives **bilateral** input, so a **cortical** lesion does
    **not** cause unilateral deafness.

*   **Vestibular Nuclei Lesion — Ipsilateral Vertigo, Nystagmus, and
    Imbalance:** A lesion of the **left vestibular nuclei** causes
    **left vestibular syndrome** — **vertigo** (spinning sensation),
    **nystagmus** (usually **horizontal-torsional**, with the **fast
    phase away from the lesion** — i.e. toward the **right** for a
    **left** lesion), **postural imbalance** (falling **toward the
    lesion side** — **left**), and **autonomic symptoms** (nausea,
    vomiting, pallor). **This is the classic "vestibular neuritis"
    pattern** when the lesion is at the **vestibular nerve** level, or
    the **vestibular nuclei syndrome** when the lesion is at the
    **brainstem** level.

*   **Vestibular Nuclei Lesion — Ipsilateral VOR Deficit:** A lesion of
    the **left vestibular nuclei** causes **impaired leftward
    vestibulo-ocular reflex (VOR)** — the **leftward VOR** (which
    normally compensates for **rightward head rotation** by driving
    **leftward eye movement**) is **reduced or absent**. **This is
    tested clinically** with the **head impulse test** (Halmagyi-Curthoys
    test) — a **positive left head impulse test** (corrective saccade
    after leftward head thrust) suggests a **left vestibular nuclei or
    nerve lesion**.

*   **Lateral Pontine Syndrome (Marie-Foix) — Vestibular Nuclei
    Involvement:** A lesion of the **left lateral pontine tegmentum**
    involving the **left vestibular nuclei**, the **left facial nerve
    fibers**, the **left chief sensory trigeminal nucleus**, the **left
    spinal trigeminal nucleus** (caudal pontine part), and the **left
    middle cerebellar peduncle** causes **Marie-Foix syndrome** —
    **ipsilateral (left) facial palsy**, **ipsilateral (left) facial
    sensory loss**, **ipsilateral (left) masticatory weakness**,
    **ipsilateral (left) vertigo/nystagmus/imbalance**, **ipsilateral
    (left) ataxia**, and **contralateral (right) hemiparesis**. The
    **vestibular nuclei** are the **substrate** of the **ipsilateral
    vestibular** component.

*   **Lateral Medullary Syndrome (Wallenberg) — Vestibular Nuclei
    Involvement:** A lesion of the **left lateral medulla** (PICA
    territory) involving the **left vestibular nuclei** (the **inferior
    vestibular nucleus** extends into the medulla) causes **ipsilateral
    (left) vertigo, nystagmus, and imbalance** — in addition to the
    **classic Wallenberg features** (ipsilateral facial pain/temperature
    loss, ipsilateral Horner syndrome, dysphagia, dysarthria,
    contralateral body pain/temperature loss, ipsilateral ataxia).
    **This is a useful distinction** — **Wallenberg** involves the
    **medullary** portion of the **vestibular nuclei**; **Marie-Foix**
    involves the **pontine** portion.

*   **Acoustic Neuroma (Vestibular Schwannoma) — Vestibulocochlear Nerve
    Lesion:** **Acoustic neuroma** (vestibular schwannoma) is a
    **benign Schwann cell tumor** of the **vestibular division** of
    **CN VIII** — it is a **nerve-level** lesion, **not** a
    **nucleus-level** lesion. It causes **ipsilateral sensorineural
    hearing loss**, **tinnitus**, and **vestibular symptoms**
    (unsteadiness, vertigo), often with **facial nerve involvement** in
    large tumors (because the facial nerve runs adjacent to CN VIII in
    the internal auditory canal). **The vestibulocochlear nuclei
    themselves are spared** — the lesion is at the **nerve** level.
    Consumers must **not** conflate **acoustic neuroma** with a
    **vestibulocochlear nuclei** lesion.

*   **Vestibular Neuritis — Vestibular Nerve Lesion:** **Vestibular
    neuritis** is an **acute unilateral vestibular dysfunction** —
    usually **viral** or **post-viral** — affecting the **vestibular
    division of CN VIII** — it is a **nerve-level** lesion, **not** a
    **nucleus-level** lesion. It causes **acute vertigo, nystagmus, and
    imbalance** with **spared hearing** (because the **cochlear
    division** is unaffected). **The vestibulocochlear nuclei themselves
    are spared** — the lesion is at the **nerve** level. Consumers must
    **not** conflate **vestibular neuritis** with a
    **vestibulocochlear nuclei** lesion.

*   **Labyrinthitis — Labyrinth Lesion:** **Labyrinthitis** is an
    **acute unilateral vestibular AND auditory dysfunction** —
    affecting the **inner ear labyrinth** (both the **cochlea** and the
    **vestibular apparatus**). It causes **acute vertigo, nystagmus,
    imbalance, AND hearing loss** (unlike **vestibular neuritis**, which
    spares hearing). **The vestibulocochlear nuclei themselves are
    spared** — the lesion is at the **labyrinth** (peripheral receptor)
    level. Consumers must **not** conflate **labyrinthitis** with a
    **vestibulocochlear nuclei** lesion.

*   **Central vs. Peripheral Vestibular Lesions — Direction of
    Nystagmus and Other Features:** **Central vestibular lesions**
    (e.g. **vestibular nuclei** lesions) typically cause **vertical
    nystagmus** (or **direction-changing nystagmus**), **normal head
    impulse test** (because the **VOR** is preserved), and **other
    brainstem signs**. **Peripheral vestibular lesions** (e.g.
    **vestibular nerve** or **labyrinth** lesions) typically cause
    **horizontal-torsional nystagmus** (with the **fast phase away from
    the lesion**), **positive head impulse test** (because the **VOR**
    is impaired), and **no other brainstem signs**. **This is a
    critical clinical distinction** — the **vestibulocochlear nuclei**
    are **central**, so their lesions follow the **central** pattern;
    the **vestibular nerve** and **labyrinth** are **peripheral**, so
    their lesions follow the **peripheral** pattern.

*   **No Named "Vestibulocochlear Nuclei Syndrome":** The
    vestibulocochlear nuclei are a **heterogeneous collection** of two
    sub-containers — they have **no named clinical syndrome as a
    collection**. Their clinical relevance is **sub-container-specific**
    — **cochlear nuclei** → **ipsilateral sensorineural hearing loss**;
    **vestibular nuclei** → **ipsilateral vertigo, nystagmus, imbalance,
    and VOR deficit**.

**What is NOT here:** The vestibulocochlear nuclei are **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **vestibular neuritis** (CN VIII vestibular nerve), or
**labyrinthitis** (inner ear). Their clinical relevance is
**auditory-vestibular-specific**, via the **left cochlear nuclei**
(hearing) and **left vestibular nuclei** (balance). **No named
vestibulocochlear nuclei syndrome exists as a collection.**

Lateralization Notes
--------------------
This is the **left** vestibulocochlear nuclei module. The
vestibulocochlear nuclei are **bilaterally symmetric** with the right
vestibulocochlear nuclei and **strictly mirrored** — and they carry
**NO warning at the sub-container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right**
    vestibulocochlear nuclei are **structurally identical** — same two
    sub-containers (cochlear and vestibular nuclei), same special sensory
    function, same bilateral framing. The bilateral symmetry is
    **strict**.

*   **Ipsilateral Cochlear Input (Structural Fact, NOT a Lateralization
    Warning):** The **left cochlear nuclei** receive **primary auditory
    axons from the left cochlea** (via the left spiral ganglion and left
    cochlear nerve) — **ipsilateral input**. The **right cochlear
    nuclei** receive input from the right cochlea. This **ipsilateral
    input** is a **structural fact** of the **auditory system** — the
    auditory pathway is **ipsilateral up to the superior olivary
    complex**, where **bilateral convergence** begins. It is **not** a
    functional lateralization.

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

*   **Ipsilateral Vestibular Input (Structural Fact, NOT a Lateralization
    Warning):** The **left vestibular nuclei** receive **primary
    vestibular axons from the left vestibular apparatus** (via Scarpa's
    ganglion and left vestibular nerve) — **ipsilateral input**. The
    **right vestibular nuclei** receive input from the right vestibular
    apparatus. This **ipsilateral input** is a **structural fact** of
    the **vestibular system** — the vestibular pathway is **ipsilateral
    up to the thalamus**, where **bilateral convergence** begins. It is
    **not** a functional lateralization.

*   **Contralateral Vestibular Projections for the VOR (Structural Fact,
    NOT a Lateralization Warning):** For the **horizontal VOR**, the
    **left vestibular nuclei** project to the **right abducens nucleus**
    (via the **right MLF**) and the **left oculomotor nucleus** (via the
    **left MLF**) — this **crossed and uncrossed** projection is a
    **structural fact** of the **VOR circuit**. It is **not** a
    functional lateralization. For the **vertical VOR** and the
    **vestibulospinal tracts**, the **vestibular nuclei** project
    **ipsilaterally** and **contralaterally** in a **patterned
    distribution** — also a **structural fact**, not a lateralization
    warning.

*   **NO Extended-Amygdala Warning (SLEA-free sub-container):** The
    vestibulocochlear nuclei are **SLEA-free** — they are **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the
    vestibulocochlear nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the
    vestibulocochlear nuclei are SPECIAL SENSORY, not the fear-output):**
    The **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The vestibulocochlear nuclei
    are **special sensory brainstem nuclei** — consumers must **not**
    conflate them with the **amygdala** or with the **fear circuit**.

**A consumer that assumes "left vestibulocochlear nuclei = right
vestibulocochlear nuclei" will be structurally correct** — the two sides
are **strictly symmetric** (the ipsilateral input and bilateral
projections are structural facts, not lateralizations). The
vestibulocochlear nuclei are a **strict-mirror pair with NO warning at
the sub-container level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cranial_nerve_nuclei/right/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../metencephalon/cerebellum/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    vestibulocochlear nuclei's relationships to the
    **vestibulocochlear nerve**, the **cochlea**, the **vestibular
    apparatus**, the **spiral ganglion**, **Scarpa's ganglion**, the
    **superior olivary complex**, the **inferior colliculus**, the
    **medial geniculate body**, the **primary auditory cortex**, the
    **vestibular cortex**, the **cerebellum**, the **MLF**, the **VOR**,
    the **vestibulospinal tracts**, and the **CN V, VI, VII siblings**
    are documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Sub-container module — structural children are `cochlear_nuclei`
    and `vestibular_nuclei`.** Each is itself a **sub-container** with
    its own prose subdivisions (AVCN/PVCN/DCN for cochlear; superior/
    lateral/medial/inferior for vestibular) that are **not** structural
    children.
*   **SPECIAL SENSORY — NOT a general sensory nucleus.** The
    **vestibulocochlear nuclei** are **special sensory** (hearing and
    balance); they are **not** general sensory nuclei. Consumers must
    **not** conflate the vestibulocochlear nuclei with the **chief
    sensory trigeminal nucleus** or any other general sensory nucleus.
*   **GREY-MATTER NUCLEI — NOT the vestibulocochlear NERVE.** The
    **vestibulocochlear nuclei** are the **grey-matter neuron clusters**;
    the **vestibulocochlear nerve** (left CN VIII) is the **white-matter
    axon bundle**. Consumers must **not** conflate the two.
*   **NOT the cochlea or vestibular apparatus — those are PERIPHERAL
    RECEPTORS.** The **nuclei** are central; the **receptors** are
    peripheral. Consumers must **not** conflate the two.
*   **NOT the spiral ganglion or Scarpa's ganglion — those are
    PERIPHERAL SENSORY GANGLIA.** The **nuclei** are central; the
    **ganglia** are peripheral. Consumers must **not** conflate the two.
*   **NOT the superior olivary complex, inferior colliculus, medial
    geniculate body, or primary auditory cortex — those are DOWNSTREAM
    of the cochlear nuclei.** The **vestibulocochlear nuclei** are the
    **first central auditory relay**. Consumers must **not** conflate
    them with any downstream auditory structure.
*   **NOT the vestibular cortex — that is DOWNSTREAM of the vestibular
    nuclei.** The **vestibulocochlear nuclei** are the **first central
    vestibular relay**. Consumers must **not** conflate them with the
    **vestibular cortex**.
*   **NOT the cerebellum — that is a metencephalic SIBLING that RECEIVES
    vestibular projections.** The **cerebellum** and the
    **vestibulocochlear nuclei** are **different structures**.
    Consumers must **not** conflate the two.
*   **NOT the MLF — that is the WHITE-MATTER TRACT.** The **MLF** is
    white matter; the **nuclei** are grey matter. Consumers must **not**
    conflate the two.
*   **NOT the VOR — that is a CIRCUIT, not a structure.** The
    **vestibulocochlear nuclei** are **one node** in the VOR — the
    **central node**. Consumers must **not** conflate the two.
*   **NOT the vestibulospinal tracts — those are the WHITE-MATTER
    DESCENDING PATHWAYS.** The **tracts** are white matter; the
    **nuclei** are grey matter. Consumers must **not** conflate the two.
*   **NOT the CN V, VI, VII sibling nuclei.** The **chief sensory
    trigeminal nucleus**, **motor trigeminal nucleus**, **abducens
    nucleus**, **facial nerve nucleus**, and **superior salivatory
    nucleus** are **different structures** for **different cranial
    nerves and different functional systems**. Consumers must **not**
    conflate the vestibulocochlear nuclei with any of them.
*   **TWO FUNCTIONALLY DISTINCT SUB-CONTAINERS — COCHLEAR vs.
    VESTIBULAR.** The **cochlear nuclei** (hearing) and the **vestibular
    nuclei** (balance and spatial orientation) are **structurally
    distinct sub-containers**. Consumers must **not** treat the
    vestibulocochlear nuclei as a single uniform system.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    vestibulocochlear nuclei are **not** an extended-amygdala component,
    and they carry **no SLEA warning**.
*   **NOT the fear-output — the vestibulocochlear nuclei are SPECIAL
    SENSORY.** The **fear-output** structure is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **vestibulocochlear nuclei** are **special sensory
    brainstem nuclei** — they are **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The vestibulocochlear nuclei are a local
    sub-container under the left container, not a cross-listed
    sub-container.
*   **No nested cross-listing.** The vestibulocochlear nuclei have no
    nested dual-framing module. They are a single bilateral
    sub-container.
*   **Structural parity with right vestibulocochlear nuclei — strict
    mirror with NO warning.** Left and right vestibulocochlear nuclei
    modules are **structurally identical** — same sub-container status,
    same **special sensory** framing, same **two sub-containers**
    (cochlear and vestibular), same **SLEA-free** status, same **no
    warning** at the sub-container level.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left import vestibulocochlear_nuclei

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.left."
        "vestibulocochlear_nuclei"
    )

**Do not** assume the vestibulocochlear nuclei are a **leaf**. They are a
**sub-container** — their structural children are the **cochlear
nuclei** and **vestibular nuclei**.

**Do not** assume the vestibulocochlear nuclei are the **vestibulocochlear
nerve**. The **nerve** (left CN VIII) is the **white-matter axon bundle**;
the **vestibulocochlear nuclei** are the **grey-matter neuron clusters**.
They are **different structures**.

**Do not** assume the vestibulocochlear nuclei are the **cochlea**,
**vestibular apparatus**, **spiral ganglion**, or **Scarpa's ganglion**.
Those are **peripheral** structures; the **vestibulocochlear nuclei** are
**central**.

**Do not** assume the vestibulocochlear nuclei are the **superior olivary
complex**, **inferior colliculus**, **medial geniculate body**, or
**primary auditory cortex**. Those are **downstream** auditory
structures — the **cochlear nuclei** are the **first central auditory
relay**.

**Do not** assume the vestibulocochlear nuclei are the **vestibular
cortex**. That is **downstream** of the **vestibular nuclei** — the
**vestibular nuclei** are the **first central vestibular relay**.

**Do not** assume the vestibulocochlear nuclei are the **cerebellum**.
The **cerebellum** is a **metencephalic sibling** that **receives**
vestibular projections — but the **cerebellum** and the
**vestibulocochlear nuclei** are **different structures**.

**Do not** assume the vestibulocochlear nuclei are the **MLF** or the
**vestibulospinal tracts**. Those are **white-matter tracts** that
**carry** the vestibular nuclei projections — the **nuclei** are the
**grey-matter neuron clusters** that **give rise to** them.

**Do not** assume the vestibulocochlear nuclei are the **VOR**. The
**VOR** is a **circuit** — the **vestibular nuclei** are **one node** in
that circuit — the **central node**.

**Do not** assume the vestibulocochlear nuclei are the **CN V, VI, or
VII sibling nuclei**. The **chief sensory trigeminal nucleus**, **motor
trigeminal nucleus**, **abducens nucleus**, **facial nerve nucleus**,
and **superior salivatory nucleus** are **different structures** for
**different cranial nerves and functional systems**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the vestibulocochlear nuclei. **The vestibulocochlear
nuclei are SLEA-FREE** — they are **not** an extended-amygdala component,
and they are **NOT part of the fear circuit**.

Iterating the vestibulocochlear nuclei's structural children (recommended
consumer pattern)::

    VESTIBULOCOCHLEAR_NUCLEI_CHILDREN = (
        "cochlear_nuclei",
        "vestibular_nuclei",
    )
    # The vestibulocochlear nuclei are a sub-container. The cochlear
    # nuclei and vestibular nuclei are themselves sub-containers with
    # their own prose subdivisions (AVCN/PVCN/DCN for cochlear;
    # superior/lateral/medial/inferior for vestibular).

Iterating the vestibulocochlear nuclei's structural children (recommended
consumer pattern)::

    for sub in VESTIBULOCOCHLEAR_NUCLEI_CHILDREN:
        sub_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.left."
            f"vestibulocochlear_nuclei.{sub}"
        )
        # resolve sub_path through the memory/recall layer

Reaching the vestibulocochlear nerve (recommended consumer pattern — the
white-matter axon bundle)::

    # The vestibulocochlear nerve (left CN VIII) is the WHITE-MATTER axon
    # bundle:
    #
    #   peripheral: left cochlea -> left spiral ganglion -> left
    #               cochlear nerve (CN VIII cochlear division)
    #   peripheral: left vestibular apparatus -> Scarpa's ganglion ->
    #               left vestibular nerve (CN VIII vestibular division)
    #
    # The nuclei are the CENTRAL sensory relays; the nerve is the
    # PERIPHERAL conduction infrastructure.

Reaching the superior olivary complex (recommended consumer pattern —
the downstream auditory relay)::

    # The superior olivary complex is the DOWNSTREAM auditory relay:
    #
    #   .../pons/superior_olivary_complex/left/
    #
    # The cochlear nuclei PROJECT TO the superior olivary complex; the
    # superior olivary complex is DOWNSTREAM of the cochlear nuclei.

Reaching the inferior colliculus (recommended consumer pattern — the
downstream midbrain auditory relay)::

    # The inferior colliculus is the DOWNSTREAM midbrain auditory relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/
    #
    # The vestibulocochlear nuclei are UPSTREAM of the inferior
    # colliculus; the inferior colliculus is DOWNSTREAM of the cochlear
    # nuclei.

Reaching the medial geniculate body (recommended consumer pattern — the
downstream thalamic auditory relay)::

    # The medial geniculate body is the DOWNSTREAM thalamic auditory
    # relay:
    #
    #   .../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/
    #
    # The vestibulocochlear nuclei are UPSTREAM of the medial geniculate
    # body; the medial geniculate body is DOWNSTREAM of the cochlear
    # nuclei.

Reaching the primary auditory cortex (recommended consumer pattern — the
downstream cortical auditory target)::

    # The primary auditory cortex (Heschl's gyrus, Brodmann areas 41 and
    # 42) is the DOWNSTREAM cortical auditory target:
    #
    #   .../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/
    #
    # The vestibulocochlear nuclei are UPSTREAM of the primary auditory
    # cortex; the primary auditory cortex is DOWNSTREAM of the cochlear
    # nuclei.

Reaching the vestibular cortex (recommended consumer pattern — the
downstream cortical vestibular target)::

    # The vestibular cortex (parieto-insular vestibular cortex, parietal
    # areas 2v/3a, insula, superior temporal gyrus) is the DOWNSTREAM
    # cortical vestibular target:
    #
    #   .../cerebral_hemispheres/left/cortex/.../  (distributed network)
    #
    # The vestibulocochlear nuclei are UPSTREAM of the vestibular cortex;
    # the vestibular cortex is DOWNSTREAM of the vestibular nuclei.

Reaching the cerebellum (recommended consumer pattern — the metencephalic
sibling that receives vestibular projections)::

    # The cerebellum is the METENCEPHALIC SIBLING that receives direct
    # vestibular projections:
    #
    #   .../metencephalon/cerebellum/hemispheres/left/
    #
    # The vestibular nuclei PROJECT TO the cerebellum (especially the
    # flocculonodular lobe and the fastigial nucleus) to drive the
    # vestibulocerebellar pathways for balance and gait. The cerebellum
    # is a DIFFERENT STRUCTURE from the vestibulocochlear nuclei.

Reaching the MLF (recommended consumer pattern — the white-matter tract):
    
    # The MLF is the WHITE-MATTER tract carrying the vestibular
    # projections to the extraocular motor nuclei:
    #
    #   .../white_matter/.../medial_longitudinal_fasciculus/  (or equivalent path)
    #
    # The vestibular nuclei GIVE RISE TO the MLF-projecting axons; the
    # MLF CARRIES them.

Reaching the VOR circuit (recommended consumer pattern — the three-neuron
reflex arc)::

    # The vestibulo-ocular reflex (VOR) is a CIRCUIT, not a structure:
    #
    #   afferent: vestibular nerve -> vestibular nuclei
    #   central:  vestibular nuclei -> MLF
    #   efferent: abducens nucleus (horizontal VOR) / oculomotor or
    #             trochlear nuclei (vertical VOR)
    #
    # The vestibular nuclei are the CENTRAL NODE of the VOR, not the
    # circuit itself.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        vcn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
            f"{side}.vestibulocochlear_nuclei"
        )
        # resolve vcn_path through the memory/recall layer

Sub-container-level detail (not wired — consult references)::

    # The two sub-containers of the vestibulocochlear nuclei are prose,
    # not modules:
    #   cochlear_nuclei    -> hearing; subdivisions AVCN (anterior
    #                         ventral), PVCN (posterior ventral), DCN
    #                         (dorsal); projects to superior olivary
    #                         complex, inferior colliculus, medial
    #                         geniculate body
    #   vestibular_nuclei  -> balance and spatial orientation;
    #                         subdivisions superior, lateral (Deiters'),
    #                         medial, inferior; projects to extraocular
    #                         motor nuclei (via MLF, VOR), spinal cord
    #                         (vestibulospinal tracts), cerebellum
    #                         (vestibulocerebellar), thalamus/cortex
    #                         (ascending vestibular pathway)
    #
    # Do not attempt to resolve the prose subdivisions as sub-paths of
    # the vestibulocochlear nuclei — resolve them at the sub-container
    # level (cochlear_nuclei or vestibular_nuclei).

References
----------
*   **Canonical auditory anatomy:** Pickles, J.O. (2015). *An
    Introduction to the Physiology of Hearing*, 4th ed. (Cochlear nuclei
    and the ascending auditory pathway — definitive.)
*   **Canonical vestibular anatomy:** Goldberg, J.M., Wilson, V.J.,
    Cullen, K.E., Angelaki, D.E., Broussard, D.M., Büttner-Ennever,
    J.A., Fukushima, K., Minor, L.B. (2012). *The Vestibular System: A
    Sixth Sense*. (Vestibular nuclei and the vestibular system —
    definitive.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Vestibulocochlear nuclei
    in overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An Atlas
    of Structures, Sections, and Systems*, 8th ed. (Vestibulocochlear
    nuclei and the pontomedullary junction.)
*   **Auditory brainstem — review:** Cant, N.B., Benson, C.G. (2003).
    "Parallel auditory pathways: projection patterns of the different
    neuronal populations in the cochlear nuclei." *Brain Research
    Bulletin* 60:457–474. (Cochlear nuclei subdivisions and projections
    to the superior olivary complex.)
*   **Vestibular brainstem — review:** Highstein, S.M., Fay, R.R., Popper,
    A.N. (eds.) (2004). *The Vestibular System*. (Vestibular nuclei
    subdivisions and projections.)
*   **VOR — review:** Leigh, R.J., Zee, D.S. (2015). *The Neurology of
    Eye Movements*, 5th ed. (Vestibulo-ocular reflex — vestibular
    nuclei as the central node.)
*   **Vestibulospinal tracts:** Wilson, V.J., Peterson, B.W. (1981).
    "Vestibulospinal and reticulospinal systems." In *Handbook of
    Physiology*. (Lateral and medial vestibulospinal tracts — vestibular
    nuclei as the source.)
*   **Acoustic neuroma (contrast — the CN VIII nerve, not the nuclei):**
    Matthies, C., Samii, M. (1997). "Management of 1000 vestibular
    schwannomas (acoustic neuromas): clinical presentation."
    *Neurosurgery* 40:1–10. (Acoustic neuroma — vestibular schwannoma of
    the CN VIII nerve; distinct from the vestibulocochlear nuclei.)
*   **Vestibular neuritis (contrast — the CN VIII vestibular nerve, not
    the nuclei):** Strupp, M., Brandt, T. (2009). "Vestibular neuritis."
    *Seminars in Neurology* 29:509–519. (Vestibular neuritis — vestibular
    nerve lesion; distinct from the vestibulocochlear nuclei.)
*   **Labyrinthitis (contrast — the inner ear labyrinth, not the
    nuclei):** Baloh, R.W. (2003). "Vestibular neuritis." *New England
    Journal of Medicine* 348:1027–1032. (Labyrinthitis — inner ear
    labyrinth lesion; distinct from the vestibulocochlear nuclei.)
*   **Central vs. peripheral vestibular lesions:** Baloh, R.W., Kerber,
    K.A. (2011). *Baloh and Honrubia's Clinical Neurophysiology of the
    Vestibular System*, 5th ed. (Central vs. peripheral vestibular
    lesion patterns — vestibular nuclei are central.)
*   **Marie-Foix syndrome (contrast — vestibular nuclei involvement):**
    Marie, P., Foix, C. (1913). "Les lésions des artères du cervelet."
    *Revue Neurologique* 25:177–190. (Lateral pontine syndrome —
    vestibular nuclei involvement.)
*   **Wallenberg syndrome (contrast — inferior vestibular nucleus
    involvement):** Wallenberg, A. (1901). "Acute bulbar paralysis
    (embolic obstruction of the posterior inferior cerebellar artery)."
    *Archiv für Psychiatrie und Nervenkrankheiten* 34:923–959. (Lateral
    medullary syndrome — inferior vestibular nucleus involvement.)
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
*   **Vestibular cortex (contrast — downstream cortical vestibular
    target):** Lopez, C., Blanke, O. (2011). "The thalamocortical
    vestibular system in health and disease." *Brain Research Bulletin*
    85:16–22. (Vestibular cortex — downstream of the vestibular nuclei.)
*   **Cerebellum (contrast — metencephalic sibling receiving vestibular
    projections):** Manto, M., Gruol, D.L., Schmahmann, J.D., Koibuchi,
    N., Rossi, F. (eds.) (2013). *Handbook of the Cerebellum and
    Cerebellar Disorders*. (Vestibulocerebellar pathways — vestibular
    nuclei projections to the cerebellum.)
*   **MLF (contrast — the white-matter tract carrying vestibular
    projections):** Büttner-Ennever, J.A. (ed.) (1988). *Neuroanatomy of
    the Oculomotor System*. (MLF and the vestibulo-ocular reflex
    pathways from the vestibular nuclei.)
*   **SLEA (contrast — the vestibulocochlear nuclei are not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the
    vestibulocochlear nuclei.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the vestibulocochlear nuclei.)
*   NeuroNames — Vestibulocochlear nuclei (left); FMA — Vestibulocochlear
    nuclei (left member).
"""