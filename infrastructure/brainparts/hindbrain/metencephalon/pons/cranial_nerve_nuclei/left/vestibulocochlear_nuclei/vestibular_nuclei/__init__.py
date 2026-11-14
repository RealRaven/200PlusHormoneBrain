"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei.vestibular_nuclei
==========================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── left
                    └── vestibulocochlear_nuclei
                        └── vestibular_nuclei   <-- THIS MODULE

**Primary synonym:** Left vestibular nuclei; left vestibular nuclear
complex; left CN VIII vestibular division nuclei; left Scarpa's ganglion
target nuclei; "the left first-order central vestibular relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nuclear complex** — a **heterogeneous
collection** of **left-side vestibular nuclei** at the **left
pontomedullary junction**, beneath the **floor of the fourth ventricle**
and lateral to the **left abducens nucleus** and **left facial
colliculus**. It is the **sole central target** of the **left vestibular
nerve** (the vestibular division of left CN VIII) and the **first-order
central vestibular relay**.
**Part of:** The **vestibulocochlear_nuclei** sub-container of the
**left** container of the **cranial_nerve_nuclei** container —
specifically, the **special sensory (vestibular)** component. The
**vestibulocochlear_nuclei** is the **left-side half** of the **CN VIII
special sensory** nuclear complex; the **vestibular_nuclei** is its
**vestibular sub-container**.
**Structural parent:** ``.../vestibulocochlear_nuclei/`` → **direct
child** of the vestibulocochlear_nuclei sub-container.
**Structural children:** **None.** This is a **leaf** module at the
**tree level** — but it is a **conceptual sub-container** of **four
prose subdivisions** (superior vestibular nucleus, lateral / Deiters'
vestibular nucleus, medial vestibular nucleus, inferior vestibular
nucleus). The **four subdivisions** are documented as **prose**, not as
structural children.
**Boundary status (LEAF at tree level — CONCEPTUAL SUB-CONTAINER of four
prose subdivisions):** **Boundary case — the vestibular nuclei are a LEAF
at the TREE level, but a CONCEPTUAL SUB-CONTAINER of FOUR PROSE
SUBDIVISIONS.** The tree wires the **vestibular nuclei** as a **single
`__init__.py`** — they have **no structural children**. The **superior
vestibular nucleus**, **lateral (Deiters') vestibular nucleus**,
**medial vestibular nucleus**, and **inferior vestibular nucleus** are
**prose subdivisions**, not structural children. Consumers must **not**
assume any of the four subdivisions exist as structural sub-modules —
they must resolve subdivision detail through the references, not the
tree.
**Boundary status (SPECIAL SENSORY — VESTIBULAR — NOT general sensory):**
**Boundary case — the vestibular nuclei are SPECIAL SENSORY (VESTIBULAR),
NOT general sensory.** Unlike the **chief sensory trigeminal nucleus**
(general sensory — discriminative touch from the face), the **vestibular
nuclei** (here) subserve **balance and spatial orientation** (the
**special vestibular sense**). They are **DIFFERENT STRUCTURES** —
different sensory modalities (special vestibular vs. general
somatosensory), different cranial nerves (VIII vs. V), different
peripheral receptors (hair cells in the semicircular canals, utricle,
and saccule vs. mechanoreceptors in the face). Consumers must **not**
conflate the **vestibular nuclei** with the **chief sensory trigeminal
nucleus** or any other general sensory nucleus.
**Boundary status (NOT the cochlear nuclei — that is the OTHER
sub-container of the vestibulocochlear nuclei):** **Boundary case — the
vestibular nuclei are NOT the cochlear nuclei.** The **left cochlear
nuclei**
(``.../vestibulocochlear_nuclei/cochlear_nuclei/``) are the **other
structural child** of the vestibulocochlear_nuclei sub-container — they
subserve **hearing** (the special auditory sense). The **left vestibular
nuclei** (here) subserve **balance and spatial orientation** (the special
vestibular sense). They are **DIFFERENT STRUCTURES** — different
functional systems (vestibular vs. auditory), different peripheral
receptors (semicircular canals, utricle, saccule vs. organ of Corti),
different ascending pathways (vestibular pathways to extraocular motor
nuclei, cerebellum, thalamus, cortex vs. auditory pathway to inferior
colliculus and medial geniculate body). They are **both under the
vestibulocochlear_nuclei sub-container**, but they are **functionally
distinct sub-containers**. Consumers must **not** conflate the
**vestibular nuclei** with the **cochlear nuclei**.
**Boundary status (GREY-MATTER NUCLEI — NOT the vestibular NERVE):**
**Boundary case — the vestibular nuclei are the GREY-MATTER NUCLEI, NOT
the vestibular nerve.** The **left vestibular nerve** (the vestibular
division of left CN VIII) is the **white-matter axon bundle** that
**carries** the **primary vestibular axons** from **Scarpa's ganglion**
to the **left vestibular nuclei**. The **vestibular nuclei** (here) are
the **grey-matter neuron clusters** that **receive** those axons and
**relay** the vestibular signal to **reflex circuits** (VOR,
vestibulospinal) and **ascending pathways** (thalamus, cortex). They
are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**nerve** is white matter. Consumers must **not** conflate the **nuclei**
with the **nerve** — the nuclei are the **central sensory relays**; the
nerve is the **peripheral conduction infrastructure**.
**Boundary status (NOT the vestibular apparatus — that is the PERIPHERAL
RECEPTOR):** **Boundary case — the vestibular nuclei are NOT the
vestibular apparatus.** The **left vestibular apparatus** — the
**semicircular canals** (anterior, posterior, horizontal — angular
acceleration), the **utricle** (horizontal linear acceleration and head
tilt), and the **saccule** (vertical linear acceleration and head
tilt) — is the **peripheral sensory apparatus** whose **hair cells**
transduce head motion and head position into neural signals. The
**vestibular nuclei** (here) are the **central grey-matter relays** that
**receive** those signals. They are **DIFFERENT STRUCTURES** — the
**apparatus** is a peripheral sensory organ; the **nuclei** are central
nervous system. Consumers must **not** conflate the **central nuclei**
with the **peripheral receptor**.
**Boundary status (NOT Scarpa's ganglion — that is a PERIPHERAL SENSORY
GANGLION):** **Boundary case — the vestibular nuclei are NOT Scarpa's
ganglion.** **Scarpa's ganglion** (the **vestibular ganglion**) is the
**peripheral sensory ganglion** that contains the **primary vestibular
neuron cell bodies** for the left vestibular apparatus. The **vestibular
nuclei** (here) are the **central grey-matter nuclei** that **receive**
the axons from Scarpa's ganglion. They are **DIFFERENT STRUCTURES** —
the **ganglion** is peripheral; the **nuclei** are central. Consumers
must **not** conflate the **central nuclei** with the **peripheral
ganglion**.
**Boundary status (NOT the vestibulocochlear nerve — that is the WHOLE
CN VIII):** **Boundary case — the vestibular nuclei are NOT the
vestibulocochlear nerve.** The **left vestibulocochlear nerve** (left
CN VIII) is the **whole nerve** — it contains the **cochlear division**
(from the left cochlea) and the **vestibular division** (from the left
vestibular apparatus). The **vestibular nuclei** (here) are the **central
grey-matter nuclei** that **receive** the axons of the **vestibular
division only**. They are **DIFFERENT STRUCTURES** — the **nuclei** are
central grey matter; the **nerve** is the **whole peripheral nerve**
that carries both divisions. Consumers must **not** conflate the
**vestibular nuclei** with the **vestibulocochlear nerve**.
**Boundary status (NOT the medial longitudinal fasciculus — that is the
WHITE-MATTER TRACT carrying vestibular projections):** **Boundary case —
the vestibular nuclei are NOT the medial longitudinal fasciculus (MLF).**
The **MLF** is the **white-matter tract** that **carries** the
**ascending and descending projections** from the **vestibular nuclei**
to the **extraocular motor nuclei** (III, IV, VI), the **abducens
internuclear neurons**, the **cervical spinal cord**, and the
**contralateral vestibular nuclei**. The **vestibular nuclei** (here)
are the **grey-matter neuron clusters** that **give rise to** those
axons. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey
matter; the **MLF** is white matter. **This distinction is clinically
load-bearing** — an **MLF** lesion causes **internuclear
ophthalmoplegia (INO)**; a **vestibular nuclei** lesion causes
**vertigo, nystagmus, imbalance, and VOR deficit**. Consumers must
**not** conflate the **vestibular nuclei** with the **MLF**.
**Boundary status (NOT the vestibulo-ocular reflex — that is a CIRCUIT,
not a structure):** **Boundary case — the vestibular nuclei are NOT the
vestibulo-ocular reflex (VOR); the VOR is a CIRCUIT.** The **VOR** is a
**three-neuron reflex arc** whose **afferent limb** is the **vestibular
nerve** from the **semicircular canals**, whose **central node** is the
**vestibular nuclei**, and whose **efferent limb** is the **abducens
nucleus** (for horizontal VOR) or the **oculomotor/trochlear nuclei**
(for vertical VOR), via the **MLF**. The **vestibular nuclei** are **one
node** in this circuit — the **central node** — not the circuit itself.
**This distinction is clinically load-bearing** — the **head impulse
test** evaluates the **VOR** (a circuit); a **vestibular nuclei** lesion
**abolishes the ipsilateral VOR** (positive head impulse test if the
lesion is central-peripheral junction-level, but typically **preserves**
it if the lesion is purely central). Consumers must **not** conflate
the **vestibular nuclei** with the **VOR**.
**Boundary status (NOT the vestibulospinal tracts — those are the
WHITE-MATTER DESCENDING PATHWAYS):** **Boundary case — the vestibular
nuclei are NOT the vestibulospinal tracts.** The **lateral
vestibulospinal tract** (from the **lateral / Deiters' vestibular
nucleus**) and the **medial vestibulospinal tract** (from the **medial
vestibular nucleus**) are the **descending white-matter pathways** that
**carry** the **vestibular nuclei projections** to the **spinal cord** —
they **mediate postural adjustments** and **head stabilization**. The
**vestibular nuclei** (here) are the **grey-matter neuron clusters**
that **give rise to** those axons. They are **DIFFERENT STRUCTURES** —
the **nuclei** are grey matter; the **tracts** are white matter.
Consumers must **not** conflate the **vestibular nuclei** with the
**vestibulospinal tracts**.
**Boundary status (NOT the vestibulocerebellar tracts — those are the
WHITE-MATTER ASCENDING PATHWAYS):** **Boundary case — the vestibular
nuclei are NOT the vestibulocerebellar tracts.** The
**vestibulocerebellar tracts** (the **direct** and **indirect**
vestibulocerebellar pathways) are the **white-matter ascending pathways**
that **carry** the **vestibular nuclei projections** to the
**cerebellum** (especially the **flocculonodular lobe** and the
**fastigial nucleus**). The **vestibular nuclei** (here) are the
**grey-matter neuron clusters** that **give rise to** those axons. They
are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**tracts** are white matter. Consumers must **not** conflate the
**vestibular nuclei** with the **vestibulocerebellar tracts**.
**Boundary status (NOT the ascending vestibular pathway — that is the
WHITE-MATTER THALAMOCORTICAL PROJECTION):** **Boundary case — the
vestibular nuclei are NOT the ascending vestibular pathway.** The
**ascending vestibular pathway** is the **white-matter projection** that
**carries** the **vestibular nuclei projections** to the **thalamus**
(the **ventral posteromedial nucleus** and the **ventral lateral
nucleus** — **prose thalamic targets**) and then to the **vestibular
cortex** (the **parieto-insular vestibular cortex**, **parietal areas
2v/3a**, the **insular cortex**, and the **superior temporal gyrus**).
The **vestibular nuclei** (here) are the **grey-matter neuron clusters**
that **give rise to** those axons. They are **DIFFERENT STRUCTURES** —
the **nuclei** are grey matter; the **pathway** is white matter.
Consumers must **not** conflate the **vestibular nuclei** with the
**ascending vestibular pathway**.
**Boundary status (NOT the cerebellum — that is the metencephalic
SIBLING that RECEIVES vestibular projections):** **Boundary case — the
vestibular nuclei are NOT the cerebellum.** The **left cerebellum**
(``.../metencephalon/cerebellum/hemispheres/left/``) is the **left
metencephalic cerebellar half** — it has its **own nuclei** (left
dentate, left fastigial, left interposed: left emboliform + left
globose) and its **own cortex**. The **left vestibular nuclei** project
**directly** to the **left cerebellum** (especially the
**flocculonodular lobe** and the **fastigial nucleus**) to **drive** the
**vestibulocerebellar** pathways for **balance and gait**. **This
cerebellar projection is a structural fact** — but the **cerebellum**
and the **vestibular nuclei** are **DIFFERENT STRUCTURES**. Consumers
must **not** conflate the **vestibular nuclei** with the **cerebellum**.
**Boundary status (NOT the thalamus or the vestibular cortex — those are
DOWNSTREAM):** **Boundary case — the vestibular nuclei are NOT the
thalamus or the vestibular cortex.** The **thalamus** (specifically the
**ventral posteromedial nucleus** and the **ventral lateral nucleus** —
**prose thalamic targets**) is the **thalamic relay** for the ascending
vestibular pathway; the **vestibular cortex** (the **parieto-insular
vestibular cortex**, **parietal areas 2v/3a**, the **insular cortex**,
and the **superior temporal gyrus**) is the **cortical target** for
conscious perception of balance and self-motion. The **vestibular
nuclei** (here) are the **first central vestibular relay** — **upstream**
of the thalamus and cortex. Consumers must **not** conflate the
**vestibular nuclei** with the **thalamus** or the **vestibular
cortex**.
**Boundary status (NOT the extraocular motor nuclei — those are the
DOWNSTREAM VOR EFFERENT NUCLEI):** **Boundary case — the vestibular
nuclei are NOT the extraocular motor nuclei.** The **oculomotor nucleus**
(midbrain — CN III), **trochlear nucleus** (midbrain — CN IV), and
**abducens nucleus** (pons — CN VI) are the **somatic motor** nuclei
that **execute** the **VOR** — they **receive** the vestibular nuclei
projections (via the **MLF**) and **drive** the **extraocular muscles**
to **stabilize the eyes** during **head movement**. The **vestibular
nuclei** (here) are the **upstream sensory relay**. They are **DIFFERENT
STRUCTURES** — the **vestibular nuclei** are **sensory**; the
**extraocular motor nuclei** are **motor**. Consumers must **not**
conflate the **vestibular nuclei** with the **extraocular motor
nuclei**.
**Boundary status (NOT the abducens nucleus — that is a SIBLING of the
cranial_nerve_nuclei container, and it is the DOWNSTREAM VOR EFFERENT
for horizontal gaze):** **Boundary case — the vestibular nuclei are NOT
the abducens nucleus.** The **left abducens nucleus**
(``.../cranial_nerve_nuclei/left/abducens_nucleus/``) is the **somatic
motor** nucleus for the **left lateral rectus** — it is the **final
common pathway** for **leftward horizontal gaze** and the **efferent
node** of the **horizontal VOR**. The **left vestibular nuclei** (here)
are the **vestibular sensory relay** — they **project** to the **right
abducens nucleus** (via the **right MLF**) and the **left abducens
nucleus** (via direct projections) for the **horizontal VOR**. They are
**DIFFERENT STRUCTURES** — the **vestibular nuclei** are **sensory
upstream**; the **abducens nucleus** is **motor downstream**. Consumers
must **not** conflate the **vestibular nuclei** with the **abducens
nucleus**.
**Boundary status (NOT a single uniform nucleus — FOUR functionally
distinct PROSE SUBDIVISIONS):** **Boundary case — the vestibular nuclei
are NOT a single uniform nucleus; they contain FOUR functionally
distinct prose subdivisions.** The **superior vestibular nucleus**
(primarily **vertical VOR** — projection to the **oculomotor and
trochlear nuclei** via the **MLF** for **vertical eye movements**). The
**lateral (Deiters') vestibular nucleus** (primarily **postural
adjustment** — origin of the **lateral vestibulospinal tract**; receives
**otolith input** from the **utricle and saccule**). The **medial
vestibular nucleus** (primarily **horizontal VOR** — projections to the
**abducens and oculomotor nuclei** via the **MLF** for **horizontal eye
movements**; origin of the **medial vestibulospinal tract**). The
**inferior vestibular nucleus** (extends into the **medulla** —
receives **otolith and canal input**; projects to the **cerebellum** and
**contralateral vestibular nuclei**; involved in **Wallenberg
syndrome**). These **prose subdivisions** are **not structural
children**. Consumers must **not** treat the vestibular nuclei as a
single uniform nucleus — they are a **four-population complex** with
**functionally distinct** sub-circuits.
**Boundary status (NOT the whole vestibulocochlear_nuclei sub-container
— a sub-container child of the vestibulocochlear_nuclei):** **Boundary
case — the vestibular nuclei are a SUB-CONTAINER child of the
vestibulocochlear_nuclei sub-container, not the sub-container itself,
and not the whole cranial_nerve_nuclei container.** The
**vestibulocochlear_nuclei** sub-container contains the **cochlear
nuclei** and the **vestibular nuclei**. The **cranial_nerve_nuclei**
container contains the **vestibulocochlear_nuclei** and **five other
children**. Consumers must **not** conflate the vestibular nuclei with
the **vestibulocochlear_nuclei** sub-container or the
**cranial_nerve_nuclei** container.
**Boundary status (NOT the right vestibular nuclei — strict mirror, no
warning):** **Boundary case — the left vestibular nuclei are NOT the
right vestibular nuclei; the two are a STRICT MIRROR PAIR with NO
warning at the sub-container level.** The **right vestibular nuclei**
(``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
are the **structurally identical** right-side counterpart — same four
prose subdivisions (superior, lateral, medial, inferior), same
vestibular special sensory function, same bilateral framing. The two
sides are **strictly mirrored** — any lateralization is documented
**here, in the Lateralization Notes**, not imported from elsewhere.
Consumers must **not** import a lateralization warning into the left
vestibular nuclei — there is **none at the sub-container level** beyond
the **vestibular structural facts** documented below.
**Boundary status (SLEA-FREE — the vestibular nuclei are NOT an
extended-amygdala component):** **Boundary case — the vestibular nuclei
are SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus**
(the **only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired elsewhere). The
**vestibular nuclei** are **vestibular special sensory brainstem
nuclei** — they are **NOT** an extended-amygdala component, and they
carry **NO SLEA warning**. Consumers must **not** import the SLEA
warning into the vestibular nuclei — they are **SLEA-free**.

Overview
--------
The vestibular nuclei are the **vestibular special sensory** nuclei for
**left CN VIII** — the **sole central target** of the **left vestibular
nerve** (the vestibular division of left CN VIII) and the **first-order
central vestibular relay**. They are a **leaf** module at the **tree
level** — with **no structural children** — but they are a
**conceptual sub-container** of **four prose subdivisions**: the
**superior vestibular nucleus**, the **lateral (Deiters') vestibular
nucleus**, the **medial vestibular nucleus**, and the **inferior
vestibular nucleus**.

**The vestibular nuclei are a LEAF at the TREE level, but a CONCEPTUAL
SUB-CONTAINER of FOUR PROSE SUBDIVISIONS.** The tree wires the
**vestibular nuclei** as a **single `__init__.py`** — they have **no
structural children**. The **superior**, **lateral (Deiters')**,
**medial**, and **inferior** vestibular nuclei are **prose
subdivisions**, not structural children. Consumers must **not** assume
any of the four subdivisions exist as structural sub-modules.

**The vestibular nuclei are SPECIAL SENSORY (VESTIBULAR), NOT general
sensory.** They subserve **balance and spatial orientation** — the
**special vestibular sense** — not general somatosensation. They are
**DIFFERENT STRUCTURES** from the **chief sensory trigeminal nucleus**
or any other general sensory nucleus.

**The vestibular nuclei are NOT the cochlear nuclei.** The **cochlear
nuclei** are the **other sub-container** of the vestibulocochlear
nuclei — they subserve **hearing**. They are **DIFFERENT STRUCTURES** —
different sensory modalities, different peripheral receptors, different
ascending pathways. They are **both under the
vestibulocochlear_nuclei sub-container**, but they are **functionally
distinct**. Consumers must **not** conflate the **vestibular nuclei**
with the **cochlear nuclei**.

**The vestibular nuclei are GREY-MATTER NUCLEI, NOT the vestibular
NERVE.** The **vestibular nerve** (the vestibular division of left
CN VIII) is the **white-matter axon bundle** that **carries** the
primary vestibular axons from Scarpa's ganglion. The **vestibular
nuclei** (here) are the **grey-matter neuron clusters** that **receive**
those axons. They are **DIFFERENT STRUCTURES** — the **nuclei** are
grey matter; the **nerve** is white matter.

**The vestibular nuclei are a FOUR-POPULATION complex.** The
**superior**, **lateral (Deiters')**, **medial**, and **inferior**
vestibular nuclei are **functionally distinct prose subdivisions**.
Consumers must **not** treat the vestibular nuclei as a single uniform
nucleus — they are a **four-population complex** with **functionally
distinct** sub-circuits.

**The vestibular nuclei are SLEA-FREE.** They are **not** an
extended-amygdala component, and they carry **no SLEA warning**.

Prose Subdivision Composition (prose, not structural children)
--------------------------------------------------------------
The vestibular nuclei contain **four prose subdivisions** — documented
as **prose**, not as structural children:

*   **Superior vestibular nucleus** — the **superior portion** of the
    vestibular nuclear complex, beneath the **floor of the fourth
    ventricle**, adjacent to the **left abducens nucleus** and **left
    facial colliculus**. The **superior vestibular nucleus** is
    primarily involved in the **vertical VOR** — it **projects** via
    the **MLF** to the **oculomotor nucleus** and the **trochlear
    nucleus** to **drive vertical eye movements** in response to
    **head pitch and roll** (from the **anterior and posterior
    semicircular canals**). It also projects to the **contralateral
    medial vestibular nucleus** via **commissural fibers** for
    **cross-coupling** of vestibular reflexes. **Vertical VOR is the
    functional system** subserved primarily by the superior vestibular
    nucleus.

*   **Lateral (Deiters') vestibular nucleus** — the **lateral portion**
    of the vestibular nuclear complex, the **largest** of the four
    subdivisions. The **lateral vestibular nucleus** is primarily
    involved in **postural adjustment** — it is the **origin** of the
    **lateral vestibulospinal tract**, which **descends ipsilaterally**
    to the **spinal cord** to **facilitate extensor muscle tone** in
    **antigravity muscles** in response to **head tilt and linear
    acceleration**. It receives **otolith input** from the **utricle
    and saccule** (linear acceleration and head tilt). It also
    **projects** to the **cerebellum** and the **contralateral
    vestibular nuclei**. **Postural adjustment and antigravity tone are
    the functional systems** subserved primarily by the lateral
    vestibular nucleus.

*   **Medial vestibular nucleus** — the **medial portion** of the
    vestibular nuclear complex, adjacent to the **floor of the fourth
    ventricle**. The **medial vestibular nucleus** is primarily involved
    in the **horizontal VOR** — it **projects** via the **MLF** to the
    **abducens nucleus** (and the **contralateral medial rectus
    subnucleus** of the **oculomotor nucleus**) to **drive horizontal
    eye movements** in response to **head rotation** (from the
    **horizontal semicircular canal**). It is also the **origin** of the
    **medial vestibulospinal tract**, which **descends bilaterally** to
    the **cervical spinal cord** to **stabilize the head** during
    **vestibular reflexes**. It projects to the **cerebellum** and to
    the **contralateral medial vestibular nucleus** via **commissural
    fibers**. **Horizontal VOR and head stabilization are the
    functional systems** subserved primarily by the medial vestibular
    nucleus.

*   **Inferior vestibular nucleus** — the **inferior portion** of the
    vestibular nuclear complex, extending **caudally into the
    medulla**. The **inferior vestibular nucleus** receives **otolith
    and canal input** and **projects** to the **cerebellum** and to the
    **contralateral vestibular nuclei**. It is the **most caudal**
    portion of the vestibular nuclear complex — it is involved in
    **Wallenberg syndrome** (lateral medullary syndrome), because the
    **inferior vestibular nucleus** extends into the **medulla** and is
    supplied by the **posterior inferior cerebellar artery (PICA)** in
    its medullary portion. **Otolith-canal integration and
    vestibulocerebellar relay are the functional systems** subserved
    primarily by the inferior vestibular nucleus.

**These subdivisions are prose, not structural children.** The tree
wires the **vestibular nuclei** as a **single leaf** — the
**superior**, **lateral (Deiters')**, **medial**, and **inferior**
vestibular nuclei are **prose**, not structural children. Consumers
that need **sub-nucleus-level** resolution should consult the
references, not the tree.

The Vestibular Nuclei / Vestibular Nerve Boundary
-------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Vestibular nuclei** (this module) — the **grey-matter neuron
    clusters** at the left pontomedullary junction.

*   **Vestibular nerve** (the vestibular division of left CN VIII) — the
    **white-matter axon bundle** that carries the primary vestibular
    axons from Scarpa's ganglion.

**They are DIFFERENT STRUCTURES.** The **nuclei** are the **central
sensory relays**; the **nerve** is the **peripheral conduction
infrastructure**. Consumers must **not** conflate the two — the
**vestibular nuclei** are the **nuclei**; the **vestibular nerve** is
the **nerve**.

The Vestibular Nuclei / Vestibular Apparatus Boundary
-----------------------------------------------------
This is the **central vs. peripheral** boundary:

*   **Vestibular nuclei** (this module) — the **central grey-matter
    relays**.

*   **Vestibular apparatus** (semicircular canals, utricle, saccule) —
    the **peripheral sensory receptors** whose **hair cells** transduce
    head motion and head position into neural signals.

**They are DIFFERENT STRUCTURES** — the **apparatus** is a peripheral
sensory organ; the **nuclei** are central nervous system. Consumers
must **not** conflate the **central nuclei** with the **peripheral
receptor**.

The Vestibular Nuclei / Scarpa's Ganglion Boundary
--------------------------------------------------
This is the **central vs. peripheral** boundary — **nuclei vs.
ganglion**:

*   **Vestibular nuclei** (this module) — the **central grey-matter
    nuclei** that **receive** the primary vestibular axons.

*   **Scarpa's ganglion** (vestibular ganglion) — the **peripheral
    sensory ganglion** that contains the **primary vestibular neuron
    cell bodies**.

**They are DIFFERENT STRUCTURES** — the **ganglion** is peripheral; the
**nuclei** are central. Consumers must **not** conflate the **central
nuclei** with the **peripheral ganglion**.

The Vestibular Nuclei / Cochlear Nuclei Boundary
------------------------------------------------
This is the **other sub-container** boundary — **vestibular vs.
auditory**, both under the vestibulocochlear nuclei:

*   **Vestibular nuclei** (this module) — the **vestibular** special
    sensory nuclei — **balance and spatial orientation**.

*   **Cochlear nuclei**
    (``.../vestibulocochlear_nuclei/cochlear_nuclei/``) — the
    **auditory** special sensory nuclei — **hearing**.

**They are DIFFERENT STRUCTURES** — different sensory modalities
(vestibular vs. auditory), different peripheral receptors, different
ascending pathways. They are **both under the vestibulocochlear_nuclei
sub-container**, but they are **functionally distinct**. Consumers must
**not** conflate the **vestibular nuclei** with the **cochlear nuclei**.

The Vestibular Nuclei / Medial Longitudinal Fasciculus Boundary
---------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Vestibular nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the MLF-projecting axons.

*   **Medial longitudinal fasciculus (MLF)** — the **white-matter tract**
    that **carries** the ascending and descending projections from the
    vestibular nuclei to the extraocular motor nuclei (III, IV, VI), the
    abducens internuclear neurons, the cervical spinal cord, and the
    contralateral vestibular nuclei.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**MLF** is white matter. **This distinction is clinically
load-bearing** — an **MLF** lesion causes **internuclear
ophthalmoplegia (INO)**; a **vestibular nuclei** lesion causes
**vertigo, nystagmus, imbalance, and VOR deficit**. Consumers must
**not** conflate the **vestibular nuclei** with the **MLF**.

The Vestibular Nuclei / Vestibulo-Ocular Reflex Boundary
--------------------------------------------------------
This is the **structure vs. circuit** boundary:

*   **Vestibular nuclei** (this module) — **one node** in the VOR — the
    **central node**.

*   **Vestibulo-ocular reflex (VOR)** — the **three-neuron reflex arc**
    whose **afferent limb** is the **vestibular nerve**, whose **central
    node** is the **vestibular nuclei**, and whose **efferent limb** is
    the **abducens nucleus** (horizontal VOR) or the **oculomotor/
    trochlear nuclei** (vertical VOR), via the **MLF**.

**They are DIFFERENT CONCEPTS** — the **vestibular nuclei** are
**structures**; the **VOR** is a **circuit**. **This distinction is
clinically load-bearing** — the **head impulse test** evaluates the
**VOR** (a circuit); a **vestibular nuclei** lesion **abolishes the
ipsilateral VOR** (though central lesions typically preserve VOR more
than peripheral lesions). Consumers must **not** conflate the
**vestibular nuclei** with the **VOR**.

The Vestibular Nuclei / Vestibulospinal Tracts Boundary
-------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the
**descending pathways**:

*   **Vestibular nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the vestibulospinal axons.

*   **Lateral vestibulospinal tract** (from the **lateral / Deiters'
    vestibular nucleus**) and **medial vestibulospinal tract** (from
    the **medial vestibular nucleus**) — the **descending white-matter
    pathways** that **carry** the vestibular nuclei projections to the
    spinal cord.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**tracts** are white matter. Consumers must **not** conflate the
**vestibular nuclei** with the **vestibulospinal tracts**.

The Vestibular Nuclei / Vestibulocerebellar Tracts Boundary
-----------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the
**ascending pathways**:

*   **Vestibular nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the vestibulocerebellar axons.

*   **Vestibulocerebellar tracts** (the **direct** and **indirect**
    vestibulocerebellar pathways) — the **white-matter ascending
    pathways** that **carry** the vestibular nuclei projections to the
    cerebellum (especially the **flocculonodular lobe** and the
    **fastigial nucleus**).

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**tracts** are white matter. Consumers must **not** conflate the
**vestibular nuclei** with the **vestibulocerebellar tracts**.

The Vestibular Nuclei / Ascending Vestibular Pathway Boundary
-------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the
**thalamocortical projection**:

*   **Vestibular nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the ascending vestibular axons.

*   **Ascending vestibular pathway** — the **white-matter projection**
    that **carries** the vestibular nuclei projections to the **thalamus**
    (the **ventral posteromedial nucleus** and the **ventral lateral
    nucleus**) and then to the **vestibular cortex**.

**They are DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the
**pathway** is white matter. Consumers must **not** conflate the
**vestibular nuclei** with the **ascending vestibular pathway**.

The Vestibular Nuclei / Cerebellum Boundary
-------------------------------------------
This is the **metencephalic-sibling** boundary — the cerebellum
**receives vestibular projections**:

*   **Vestibular nuclei** (this module) — the **first central vestibular
    relay**.

*   **Cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/left/``) — the **left
    metencephalic cerebellar half**, with its **own nuclei** (left
    dentate, left fastigial, left interposed) and its **own cortex**.

**The left vestibular nuclei project directly to the left cerebellum**
(especially the **flocculonodular lobe** and the **fastigial nucleus**)
to drive the **vestibulocerebellar** pathways for **balance and gait**.
**This cerebellar projection is a structural fact** — but the
**cerebellum** and the **vestibular nuclei** are **DIFFERENT
STRUCTURES**. Consumers must **not** conflate the **vestibular nuclei**
with the **cerebellum**.

The Vestibular Nuclei / Thalamus Boundary
-----------------------------------------
This is the **thalamic relay** boundary — **upstream vs. downstream**:

*   **Vestibular nuclei** (this module) — the **first central vestibular
    relay**.

*   **Thalamus** (specifically the **ventral posteromedial nucleus** and
    the **ventral lateral nucleus** — **prose thalamic targets**) — the
    **thalamic relay** for the ascending vestibular pathway.

**The vestibular nuclei are UPSTREAM** of the thalamus — they are the
**first central vestibular relay**. Consumers must **not** conflate the
**vestibular nuclei** with the **thalamus**.

The Vestibular Nuclei / Vestibular Cortex Boundary
--------------------------------------------------
This is the **cortical vestibular target** boundary — **upstream vs.
downstream**:

*   **Vestibular nuclei** (this module) — the **first central vestibular
    relay**.

*   **Vestibular cortex** — a **distributed cortical network** including
    the **parieto-insular vestibular cortex (PIVC)**, parts of the
    **parietal lobe** (area 2v, area 3a), the **insular cortex**, and
    the **superior temporal gyrus** — the **cortical target** of the
    ascending vestibular pathway.

**The vestibular nuclei are UPSTREAM** of the vestibular cortex — they
are the **first central vestibular relay**. Consumers must **not**
conflate the **vestibular nuclei** with the **vestibular cortex**.

The Vestibular Nuclei / Extraocular Motor Nuclei Boundary
---------------------------------------------------------
This is the **sensory vs. motor** boundary — **upstream vs. downstream**:

*   **Vestibular nuclei** (this module) — the **sensory** first central
    vestibular relay.

*   **Oculomotor nucleus** (midbrain — CN III), **trochlear nucleus**
    (midbrain — CN IV), **abducens nucleus** (pons — CN VI) — the
    **motor** extraocular nuclei that **execute** the **VOR**.

**The vestibular nuclei are UPSTREAM** of the extraocular motor nuclei
— they are the **sensory** relay that **drives** the **motor** output.
Consumers must **not** conflate the **vestibular nuclei** with the
**extraocular motor nuclei**.

The Vestibular Nuclei / Abducens Nucleus Boundary
-------------------------------------------------
This is the **sibling** boundary — **sensory vs. motor**, and **upstream
vs. downstream**:

*   **Vestibular nuclei** (this module) — the **sensory** first central
    vestibular relay.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/``) — the
    **somatic motor** nucleus for the **left lateral rectus** — the
    **efferent node** of the **horizontal VOR**.

**They are DIFFERENT STRUCTURES** — the **vestibular nuclei** are
**sensory**; the **abducens nucleus** is **motor**. They are both
involved in the **horizontal VOR** (the vestibular nuclei as the
**central node**, the abducens nucleus as the **efferent node**), but
they are **functionally distinct**. Consumers must **not** conflate the
**vestibular nuclei** with the **abducens nucleus**.

The Vestibular Nuclei / CN V, VI, VII Sibling Nuclei Boundary
-------------------------------------------------------------
This is the **sibling** boundary — **CN VIII vestibular vs. other
functional systems**:

*   **Vestibular nuclei** (this module) — the **CN VIII vestibular
    special sensory** nuclei — **balance and spatial orientation**.

*   **Chief sensory trigeminal nucleus** (CN V general sensory),
    **motor trigeminal nucleus** (CN V branchial motor), **abducens
    nucleus** (CN VI somatic motor), **facial nerve nucleus** (CN VII
    branchial motor), **superior salivatory nucleus** (CN VII
    parasympathetic) — the **sibling nuclei** under the left container
    of the cranial_nerve_nuclei.

**They are DIFFERENT STRUCTURES** — different cranial nerves, different
functional systems, different peripheral targets. Consumers must **not**
conflate the **vestibular nuclei** with any of the **CN V, CN VI, or
CN VII sibling nuclei**.

The Vestibular Nuclei / Vestibulocochlear Nuclei Sub-Container Boundary
-----------------------------------------------------------------------
This is the **sub-container vs. sub-container child** boundary:

*   **Vestibular nuclei** (this module) — a **sub-container child** of
    the **vestibulocochlear_nuclei** sub-container.

*   **Vestibulocochlear nuclei** (``.../vestibulocochlear_nuclei/``) —
    the **CN VIII special sensory sub-container**, with **two structural
    children** (the **cochlear nuclei** and the **vestibular nuclei**).

**The vestibular nuclei are a sub-container child of the
vestibulocochlear_nuclei.** Consumers must **not** conflate the
vestibular nuclei with the **vestibulocochlear_nuclei** sub-container
or the **cranial_nerve_nuclei** container.

The Vestibular Nuclei / Right Vestibular Nuclei Boundary
--------------------------------------------------------
This is the **strict-mirror** boundary:

*   **Left vestibular nuclei** (this module) — the **left-side**
    vestibular special sensory nuclei for **left balance**.

*   **Right vestibular nuclei**
    (``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **structurally identical** right-side vestibular special
    sensory nuclei for **right balance**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same four prose
subdivisions (superior, lateral, medial, inferior), same vestibular
special sensory function, same bilateral framing. **Vestibular
laterality facts are documented in the Lateralization Notes below, not
imported from elsewhere** — the structural connectivity facts
(ipsilateral vestibular input up to the thalamus, then bilateral
projections from the thalamus onward; crossed VOR projections to the
abducens nucleus) are **structural** and **not warnings**. Consumers
must **not** import a lateralization warning into the left vestibular
nuclei — there is **none at the sub-container level**.

The Vestibular Nuclei / SLEA Boundary
-------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Vestibular nuclei** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The vestibular nuclei are NOT part of the SLEA continuum.** They are
**vestibular special sensory brainstem nuclei**, and they carry **no
SLEA warning**. Consumers must **not** import the SLEA warning into the
vestibular nuclei.

Function in the Human Brain
---------------------------
The vestibular nuclei's functions are **the first central relay for left
balance and spatial orientation** — **NOT a single unified function**:

*   **Vestibulo-Ocular Reflex (VOR):** The **vestibular nuclei**
    **receive** the **primary vestibular axons** from **Scarpa's
    ganglion** (via the **left vestibular nerve**) and **project** to
    the **extraocular motor nuclei** (via the **MLF**) to **drive** the
    **vestibulo-ocular reflex (VOR)** — the **three-neuron reflex arc**
    that **stabilizes the eyes** during **head movement**. The
    **superior vestibular nucleus** drives the **vertical VOR**; the
    **medial vestibular nucleus** drives the **horizontal VOR**.

*   **Vestibulospinal Reflexes (Postural Adjustment):** The **lateral
    (Deiters') vestibular nucleus** gives rise to the **lateral
    vestibulospinal tract** — **descending ipsilaterally** to the
    **spinal cord** to **facilitate extensor muscle tone** in
    **antigravity muscles** in response to **head tilt and linear
    acceleration**. The **medial vestibular nucleus** gives rise to
    the **medial vestibulospinal tract** — **descending bilaterally**
    to the **cervical spinal cord** to **stabilize the head** during
    **vestibular reflexes**.

*   **Vestibulocerebellar Relay (Balance and Gait):** The **vestibular
    nuclei** **project** directly to the **cerebellum** (especially
    the **flocculonodular lobe** and the **fastigial nucleus**) to
    **drive** the **vestibulocerebellar** pathways for **balance and
    gait**.

*   **Ascending Vestibular Pathway (Conscious Perception):** The
    **vestibular nuclei** **project** to the **thalamus** (the
    **ventral posteromedial nucleus** and the **ventral lateral
    nucleus**) and then to the **vestibular cortex** (the
    **parieto-insular vestibular cortex**, **parietal areas 2v/3a**, the
    **insular cortex**, and the **superior temporal gyrus**) for the
    **conscious perception** of **balance**, **spatial orientation**,
    and **self-motion**.

*   **Commissural Cross-Coupling:** The **vestibular nuclei** receive
    **commissural projections** from the **contralateral vestibular
    nuclei** — this **cross-coupling** is essential for **bilateral
    coordination** of vestibular reflexes and for **central vestibular
    compensation** after unilateral vestibular loss.

*   **NOT a neural processor in the classical sense.** The **vestibular
    nuclei** are **first-order central sensory relays** — they
    **receive** the primary vestibular afferents and **project** them
    to **reflex circuits** (VOR, vestibulospinal) and **ascending
    pathways** (cerebellum, thalamus, cortex). The **processing** of
    vestibular signals is **distributed** across the **vestibular
    nuclei** (first central relay), the **VOR** and **vestibulospinal**
    circuits (reflex processing), the **cerebellum** (balance and gait),
    and the **vestibular cortex** (conscious perception). The
    **vestibular nuclei** are the **first central relay** — the
    **brainstem entry point** for the vestibular system.

**The unifying theme:** the vestibular nuclei are the **first central
sensory relay** for the **left vestibular system** — the **sole central
target** of the **left vestibular nerve**. They are **special sensory**
(balance and spatial orientation), **four-population** (superior for
vertical VOR; lateral for postural adjustment; medial for horizontal VOR
and head stabilization; inferior for otolith-canal integration and
vestibulocerebellar relay), **SLEA-free**, and **NOT the vestibular
nerve** — the **nerve** is the **white-matter axon bundle**; the
**nuclei** are the **grey-matter neuron clusters** that **receive** its
axons.

Associated Disorders
--------------------
The vestibular nuclei have **no named "vestibular nuclei syndrome"** —
their clinical associations are **nucleus-specific**, and they are
**distinguishable from nerve-level, peripheral-receptor-level, and
downstream vestibular pathway lesions**:

*   **Vestibular Nuclei Lesion — Ipsilateral Vertigo, Nystagmus, and
    Imbalance:** A lesion of the **left vestibular nuclei** causes
    **left vestibular syndrome** — **vertigo** (spinning sensation),
    **nystagmus** (usually **vertical** or **direction-changing**, with
    **no fixed fast phase** — a **central** pattern), **postural
    imbalance** (variable direction of fall — **not** consistently
    toward the lesion side), and **autonomic symptoms** (nausea,
    vomiting, pallor). **This is the classic "central vestibular"
    pattern** — distinct from the **peripheral vestibular** pattern
    (see below).

*   **Vestibular Nuclei Lesion — Ipsilateral VOR Deficit (Often
    Preserved):** A lesion of the **left vestibular nuclei** causes
    **impaired leftward vestibulo-ocular reflex (VOR)** — but the
    **head impulse test** is **often normal** in **central** vestibular
    lesions (because the **VOR** is a **reflex circuit** that can be
    **partially compensated** by **cerebellar** and **commissural**
    mechanisms). **This is a critical clinical distinction** — a
    **positive head impulse test** suggests a **peripheral** (nerve or
    labyrinth) lesion; a **normal head impulse test** with **vertigo
    and nystagmus** suggests a **central** (vestibular nuclei or
    brainstem) lesion.

*   **Lateral Pontine Syndrome (Marie-Foix) — Superior, Lateral, and
    Medial Vestibular Nuclei Involvement:** A lesion of the **left
    lateral pontine tegmentum** involving the **left superior**,
    **left lateral**, and **left medial vestibular nuclei** (and the
    **left facial nerve fibers**, **left chief sensory trigeminal
    nucleus**, **left spinal trigeminal nucleus** caudal pontine part,
    and **left middle cerebellar peduncle**) causes **Marie-Foix
    syndrome** — **ipsilateral (left) facial palsy**, **ipsilateral
    (left) facial sensory loss**, **ipsilateral (left) masticatory
    weakness**, **ipsilateral (left) vertigo/nystagmus/imbalance**,
    **ipsilateral (left) ataxia**, and **contralateral (right)
    hemiparesis**. The **vestibular nuclei** are the **substrate** of
    the **ipsilateral vestibular** component.

*   **Lateral Medullary Syndrome (Wallenberg) — Inferior Vestibular
    Nucleus Involvement:** A lesion of the **left lateral medulla**
    (PICA territory) involving the **left inferior vestibular nucleus**
    (which extends into the medulla) causes **ipsilateral (left)
    vertigo, nystagmus, and imbalance** — in addition to the **classic
    Wallenberg features** (ipsilateral facial pain/temperature loss,
    ipsilateral Horner syndrome, dysphagia, dysarthria, contralateral
    body pain/temperature loss, ipsilateral ataxia). **This is a
    useful distinction** — **Wallenberg** involves the **medullary**
    portion of the **vestibular nuclei** (the **inferior vestibular
    nucleus**); **Marie-Foix** involves the **pontine** portion
    (superior, lateral, medial vestibular nuclei).

*   **Acoustic Neuroma (Vestibular Schwannoma) — Vestibular Nerve
    Lesion:** **Acoustic neuroma** (vestibular schwannoma) is a
    **benign Schwann cell tumor** of the **vestibular division** of
    **CN VIII** — it is a **nerve-level** lesion, **not** a
    **nucleus-level** lesion. It causes **ipsilateral sensorineural
    hearing loss**, **tinnitus**, and **vestibular symptoms**
    (unsteadiness, vertigo), often with **facial nerve involvement** in
    large tumors (because the facial nerve runs adjacent to CN VIII in
    the internal auditory canal). **The vestibular nuclei themselves
    are spared** — the lesion is at the **nerve** level. Consumers
    must **not** conflate **acoustic neuroma** with a **vestibular
    nuclei** lesion.

*   **Vestibular Neuritis — Vestibular Nerve Lesion:** **Vestibular
    neuritis** is an **acute unilateral vestibular dysfunction** —
    usually **viral** or **post-viral** — affecting the **vestibular
    division of CN VIII** — it is a **nerve-level** lesion, **not** a
    **nucleus-level** lesion. It causes **acute vertigo, nystagmus, and
    imbalance** with **spared hearing** (because the **cochlear
    division** is unaffected), and a **positive head impulse test**
    (because the **VOR** is impaired). **The vestibular nuclei
    themselves are spared** — the lesion is at the **nerve** level.
    Consumers must **not** conflate **vestibular neuritis** with a
    **vestibular nuclei** lesion.

*   **Labyrinthitis — Labyrinth Lesion:** **Labyrinthitis** is an
    **acute unilateral vestibular AND auditory dysfunction** —
    affecting the **inner ear labyrinth** (both the **cochlea** and the
    **vestibular apparatus**). It causes **acute vertigo, nystagmus,
    imbalance, AND hearing loss** (unlike **vestibular neuritis**,
    which spares hearing), and a **positive head impulse test**.
    **The vestibular nuclei themselves are spared** — the lesion is at
    the **labyrinth** (peripheral receptor) level. Consumers must
    **not** conflate **labyrinthitis** with a **vestibular nuclei**
    lesion.

*   **BPPV (Benign Paroxysmal Positional Vertigo) — Otoconia in the
    Semicircular Canals:** **BPPV** is a **peripheral vestibular
    disorder** caused by **displaced otoconia** (calcium carbonate
    crystals) in the **semicircular canals** — usually the **posterior
    canal** — that **inappropriately stimulate the canal hair cells**
    during **head position changes** (rolling over in bed, looking up).
    It causes **brief (seconds), positional vertigo** triggered by
    **specific head movements**. **BPPV is a peripheral-receptor-level
    disorder** — the **vestibular nuclei themselves are spared**.
    Consumers must **not** conflate **BPPV** with a **vestibular
    nuclei** lesion.

*   **Meniere's Disease — Endolymphatic Hydrops:** **Meniere's
    disease** is a **peripheral vestibular and auditory disorder**
    caused by **endolymphatic hydrops** (increased pressure in the
    **inner ear fluid system**). It causes **episodic vertigo** (lasting
    minutes to hours), **fluctuating hearing loss**, **tinnitus**, and
    **aural fullness**. **Meniere's disease is a peripheral-receptor-
    level disorder** — the **vestibular nuclei themselves are
    spared**. Consumers must **not** conflate **Meniere's disease**
    with a **vestibular nuclei** lesion.

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
    critical clinical distinction** — the **vestibular nuclei** are
    **central**, so their lesions follow the **central** pattern; the
    **vestibular nerve** and **labyrinth** are **peripheral**, so their
    lesions follow the **peripheral** pattern.

*   **No Named "Vestibular Nuclei Syndrome":** The vestibular nuclei
    are a **four-population complex** — they have **no named clinical
    syndrome**. Their clinical relevance is **nucleus-specific** —
    **ipsilateral vertigo, nystagmus, and imbalance** (which are **the
    same symptoms** as a **vestibular nerve lesion** or a **labyrinth
    lesion**, distinguishable only by **central vs. peripheral signs**
    and **imaging**).

**What is NOT here:** The vestibular nuclei are **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN
VIII nerve), **vestibular neuritis** (CN VIII vestibular nerve),
**labyrinthitis** (inner ear), **BPPV** (otoconia in semicircular
canals), or **Meniere's disease** (endolymphatic hydrops). Their
clinical relevance is **vestibular-specific**, via the **left vestibular
nuclei** (balance). **No named vestibular nuclei syndrome exists.**

Lateralization Notes
--------------------
This is the **left** vestibular nuclei module. The vestibular nuclei are
**bilaterally symmetric** with the right vestibular nuclei and
**strictly mirrored** — and they carry **NO warning at the sub-container
level**:

*   **Strict Bilateral Symmetry:** The **left** and **right**
    vestibular nuclei are **structurally identical** — same four prose
    subdivisions (superior, lateral, medial, inferior), same vestibular
    special sensory function, same bilateral framing. The bilateral
    symmetry is **strict**.

*   **Ipsilateral Vestibular Input (Structural Fact, NOT a
    Lateralization Warning):** The **left vestibular nuclei** receive
    **primary vestibular axons from the left vestibular apparatus** (via
    Scarpa's ganglion and left vestibular nerve) — **ipsilateral
    input**. The **right vestibular nuclei** receive input from the
    right vestibular apparatus. This **ipsilateral input** is a
    **structural fact** of the **vestibular system** — the vestibular
    pathway is **ipsilateral up to the thalamus**, where **bilateral
    convergence** begins. It is **not** a functional lateralization. It
    is the **neural substrate** of **ipsilateral vestibular signs** in
    **vestibular nuclei** or **vestibular nerve** lesions.

*   **Crossed and Uncrossed VOR Projections (Structural Fact, NOT a
    Lateralization Warning):** For the **horizontal VOR**, the **left
    vestibular nuclei** project to the **right abducens nucleus** (via
    the **right MLF**) and the **left oculomotor nucleus** (via the
    **left MLF**) — this **crossed and uncrossed** projection is a
    **structural fact** of the **VOR circuit**. For the **vertical
    VOR**, the **superior vestibular nucleus** projects to the
    **oculomotor and trochlear nuclei** — also a **structural fact**,
    not a lateralization warning. The **crossed projections** are
    essential for **conjugate eye movement** during **head rotation**.

*   **Bilateral Vestibular Input to the Ascending Pathway (Structural
    Fact, NOT a Lateralization Warning):** The **vestibular nuclei**
    project to the **thalamus** (ventral posteromedial nucleus and
    ventral lateral nucleus) **bilaterally** — the **ascending
    vestibular pathway** crosses to the **contralateral thalamus** and
    ascends to the **contralateral vestibular cortex**. This is why
    **cortical vestibular lesions** do **not** cause **unilateral
    vestibular loss** — the **vestibular cortex** receives **bilateral**
    input. **This is a structural fact of the vestibular system**, not a
    functional lateralization.

*   **Ipsilateral Lateral Vestibulospinal Tract (Structural Fact, NOT a
    Lateralization Warning):** The **lateral vestibulospinal tract**
    from the **lateral (Deiters') vestibular nucleus** descends
    **ipsilaterally** to the **spinal cord** — it **facilitates
    extensor tone** in **antigravity muscles** on the **same side** as
    the vestibular nucleus. **This is a structural fact of the
    vestibulospinal system**, not a functional lateralization.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The vestibular
    nuclei are **SLEA-free** — they are **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the vestibular nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the vestibular
    nuclei are SPECIAL SENSORY VESTIBULAR, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The vestibular nuclei
    are **vestibular special sensory brainstem nuclei** — consumers must
    **not** conflate them with the **amygdala** or with the **fear
    circuit**.

**A consumer that assumes "left vestibular nuclei = right vestibular
nuclei" will be structurally correct** — the two sides are **strictly
symmetric** (the ipsilateral input and crossed/bilateral projections are
structural facts, not lateralizations). The vestibular nuclei are a
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
    vestibular nuclei's relationships to the **vestibular nerve**, the
    **vestibular apparatus**, **Scarpa's ganglion**, the **MLF**, the
    **VOR**, the **vestibulospinal tracts**, the **vestibulocerebellar
    tracts**, the **ascending vestibular pathway**, the **cerebellum**,
    the **thalamus**, the **vestibular cortex**, the **extraocular
    motor nuclei**, the **abducens nucleus**, and the **CN V, VI, VII
    siblings** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf at tree level — conceptual sub-container of FOUR PROSE
    SUBDIVISIONS.** The **superior**, **lateral (Deiters')**,
    **medial**, and **inferior** vestibular nuclei are documented as
    **prose**, not as structural children. Consumers must not assume
    any exist as structural children; resolve sub-nucleus-level detail
    through the references.
*   **SPECIAL SENSORY VESTIBULAR — NOT general sensory.** The
    **vestibular nuclei** are **vestibular special sensory** (balance
    and spatial orientation); they are **not** general sensory nuclei.
    Consumers must **not** conflate the vestibular nuclei with the
    **chief sensory trigeminal nucleus** or any other general sensory
    nucleus.
*   **NOT the cochlear nuclei — that is the OTHER sub-container.** The
    **vestibular nuclei** (balance) and the **cochlear nuclei**
    (hearing) are **different structures** — different sensory
    modalities, different peripheral receptors, different ascending
    pathways. Consumers must **not** conflate the two.
*   **GREY-MATTER NUCLEI — NOT the vestibular NERVE.** The **vestibular
    nuclei** are the **grey-matter neuron clusters**; the **vestibular
    nerve** is the **white-matter axon bundle**. Consumers must **not**
    conflate the two.
*   **NOT the vestibular apparatus or Scarpa's ganglion — those are
    PERIPHERAL.** The **nuclei** are central; the **vestibular
    apparatus** and **Scarpa's ganglion** are peripheral. Consumers must
    **not** conflate the two.
*   **NOT the vestibulocochlear nerve — that is the WHOLE CN VIII.** The
    **vestibular nuclei** receive the axons of the **vestibular division
    only**; the **vestibulocochlear nerve** carries both divisions.
    Consumers must **not** conflate the two.
*   **NOT the MLF, VOR, vestibulospinal tracts, or vestibulocerebellar
    tracts — those are circuits or white-matter tracts.** The **nuclei**
    are grey matter; the **tracts** are white matter; the **VOR** is a
    circuit. Consumers must **not** conflate the nuclei with any of
    these.
*   **NOT the cerebellum — that is the metencephalic SIBLING that
    RECEIVES vestibular projections.** The **cerebellum** and the
    **vestibular nuclei** are **different structures**. Consumers must
    **not** conflate the two.
*   **NOT the thalamus, vestibular cortex, or extraocular motor nuclei —
    those are DOWNSTREAM.** The **vestibular nuclei** are the **first
    central vestibular relay**. Consumers must **not** conflate them
    with any downstream structure.
*   **NOT the abducens nucleus — that is a SIBLING and it is the
    DOWNSTREAM VOR EFFERENT for horizontal gaze.** The **vestibular
    nuclei** are **sensory**; the **abducens nucleus** is **motor**.
    They are both involved in the **horizontal VOR**, but they are
    **functionally distinct**. Consumers must **not** conflate the two.
*   **NOT the CN V, VI, VII sibling nuclei.** The **chief sensory
    trigeminal nucleus**, **motor trigeminal nucleus**, **abducens
    nucleus**, **facial nerve nucleus**, and **superior salivatory
    nucleus** are **different structures** for **different cranial
    nerves and different functional systems**. Consumers must **not**
    conflate the vestibular nuclei with any of them.
*   **FOUR FUNCTIONALLY DISTINCT PROSE SUBDIVISIONS — SUPERIOR vs.
    LATERAL vs. MEDIAL vs. INFERIOR.** The **superior** (vertical VOR),
    **lateral** (postural adjustment), **medial** (horizontal VOR and
    head stabilization), and **inferior** (otolith-canal integration
    and vestibulocerebellar relay) vestibular nuclei are **prose**, not
    structural children. Consumers must **not** treat the vestibular
    nuclei as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The vestibular
    nuclei are **not** an extended-amygdala component, and they carry
    **no SLEA warning**.
*   **NOT the fear-output — the vestibular nuclei are SPECIAL SENSORY
    VESTIBULAR.** The **fear-output** structure is the **central
    nucleus**; the **fear-learning** structures are the **basolateral
    nuclei**; the **fear-modulatory / extinction** structures are the
    **basomedial nuclei**. The **vestibular nuclei** are **vestibular
    special sensory brainstem nuclei** — they are **not** part of the
    fear circuit.
*   **No ``AREA_PATHS`` hop.** The vestibular nuclei are a local leaf
    under the vestibulocochlear_nuclei sub-container, not a cross-listed
    leaf.
*   **No nested cross-listing.** The vestibular nuclei have no nested
    dual-framing module. They are a single leaf (at the tree level) with
    four prose subdivisions.
*   **Structural parity with right vestibular nuclei — strict mirror
    with NO warning.** Left and right vestibular nuclei modules are
    **structurally identical** — same leaf status, same **vestibular
    special sensory** framing, same **four prose subdivisions**
    (superior, lateral, medial, inferior), same **SLEA-free** status,
    same **no warning** at the sub-container level.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei import vestibular_nuclei

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.left."
        "vestibulocochlear_nuclei.vestibular_nuclei"
    )

**Do not** assume the vestibular nuclei are a **structural container**.
They are a **leaf at the tree level** — with **four conceptual prose
subdivisions** (superior, lateral, medial, inferior) that are **not**
structural children.

**Do not** assume the vestibular nuclei are the **vestibular nerve**. The
**vestibular nerve** is the **white-matter axon bundle**; the
**vestibular nuclei** are the **grey-matter neuron clusters**. They are
**different structures**.

**Do not** assume the vestibular nuclei are the **vestibular apparatus**
or **Scarpa's ganglion**. Those are **peripheral** structures; the
**vestibular nuclei** are **central**.

**Do not** assume the vestibular nuclei are the **cochlear nuclei**. The
**cochlear nuclei** are the **other sub-container** of the
vestibulocochlear nuclei — they subserve **hearing**; the **vestibular
nuclei** subserve **balance and spatial orientation**.

**Do not** assume the vestibular nuclei are the **MLF**, **VOR**,
**vestibulospinal tracts**, or **vestibulocerebellar tracts**. The
**MLF**, **vestibulospinal tracts**, and **vestibulocerebellar tracts**
are **white-matter tracts**; the **VOR** is a **circuit** — the
**vestibular nuclei** are **one node** in the VOR — the **central
node**.

**Do not** assume the vestibular nuclei are the **cerebellum**,
**thalamus**, **vestibular cortex**, or **extraocular motor nuclei**.
Those are **downstream** structures — the **vestibular nuclei** are the
**first central vestibular relay**.

**Do not** assume the vestibular nuclei are the **abducens nucleus**.
The **abducens nucleus** is the **downstream motor** nucleus for the
**horizontal VOR**; the **vestibular nuclei** are the **upstream
sensory** nucleus. They are both involved in the **horizontal VOR**, but
they are **functionally distinct**.

**Do not** assume the vestibular nuclei are the **CN V, VI, or VII
sibling nuclei**. The **chief sensory trigeminal nucleus**, **motor
trigeminal nucleus**, **abducens nucleus**, **facial nerve nucleus**,
and **superior salivatory nucleus** are **different structures** for
**different cranial nerves and functional systems**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the vestibular nuclei. **The vestibular nuclei are
SLEA-FREE** — they are **not** an extended-amygdala component, and they
are **NOT part of the fear circuit**.

Iterating the vestibular nuclei's (empty) structural children
(recommended consumer pattern)::

    VESTIBULAR_NUCLEI_CHILDREN = ()
    # The vestibular nuclei are a leaf at the tree level. The superior,
    # lateral, medial, and inferior vestibular nuclei are prose
    # subdivisions, not structural children.

Reaching the vestibular nerve (recommended consumer pattern — the
white-matter axon bundle)::

    # The vestibular nerve (the vestibular division of left CN VIII) is
    # the WHITE-MATTER axon bundle:
    #
    #   peripheral: left vestibular apparatus -> Scarpa's ganglion ->
    #               left vestibular nerve (CN VIII vestibular division)
    #
    # The nuclei are the CENTRAL sensory relays; the nerve is the
    # PERIPHERAL conduction infrastructure.

Reaching Scarpa's ganglion (recommended consumer pattern — the
peripheral sensory ganglion)::

    # Scarpa's ganglion (vestibular ganglion) is the PERIPHERAL sensory
    # ganglion containing the primary vestibular neuron cell bodies:
    #
    #   peripheral: Scarpa's ganglion (left)
    #
    # The nuclei are CENTRAL; the ganglion is PERIPHERAL.

Reaching the cochlear nuclei (recommended consumer pattern — the OTHER
sub-container of the vestibulocochlear nuclei)::

    # The cochlear nuclei are the AUDITORY sub-container of the
    # vestibulocochlear nuclei:
    #
    #   .../vestibulocochlear_nuclei/cochlear_nuclei/
    #
    # The vestibular nuclei (balance) and the cochlear nuclei (hearing)
    # are FUNCTIONALLY DISTINCT — different sensory modalities, different
    # peripheral receptors, different ascending pathways.

Reaching the MLF (recommended consumer pattern — the white-matter tract)::

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

Reaching the vestibulospinal tracts (recommended consumer pattern — the
white-matter descending pathways)::

    # The lateral and medial vestibulospinal tracts are WHITE-MATTER
    # descending pathways:
    #
    #   .../white_matter/.../vestibulospinal_tracts/  (or equivalent path)
    #
    # The vestibular nuclei GIVE RISE TO the vestibulospinal axons; the
    # vestibulospinal tracts CARRY them to the spinal cord.

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
    # is a DIFFERENT STRUCTURE from the vestibular nuclei.

Reaching the thalamus (recommended consumer pattern — the thalamic relay)::

    # The thalamus (ventral posteromedial nucleus and ventral lateral
    # nucleus) is the THALAMIC RELAY for the ascending vestibular
    # pathway:
    #
    #   .../diencephalon/thalamus/left/ventral_nuclear_group/.../  (prose thalamic target)
    #
    # The vestibular nuclei PROJECT TO the thalamus; the thalamus is
    # DOWNSTREAM of the vestibular nuclei.

Reaching the vestibular cortex (recommended consumer pattern — the
cortical vestibular target)::

    # The vestibular cortex (parieto-insular vestibular cortex, parietal
    # areas 2v/3a, insula, superior temporal gyrus) is the DOWNSTREAM
    # cortical vestibular target:
    #
    #   .../cerebral_hemispheres/left/cortex/.../  (distributed network)
    #
    # The vestibular nuclei are UPSTREAM of the vestibular cortex; the
    # vestibular cortex is DOWNSTREAM of the vestibular nuclei.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        vn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
            f"{side}.vestibulocochlear_nuclei.vestibular_nuclei"
        )
        # resolve vn_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The vestibular nuclei's four prose subdivisions are prose, not
    # modules:
    #   superior vestibular nucleus  -> vertical VOR; projects via MLF to
    #                                    oculomotor and trochlear nuclei;
    #                                    vertical eye movements
    #   lateral (Deiters') vestibular nucleus -> postural adjustment;
    #                                    origin of lateral vestibulospinal
    #                                    tract; otolith input from utricle
    #                                    and saccule; antigravity muscle
    #                                    tone
    #   medial vestibular nucleus    -> horizontal VOR; projects via MLF to
    #                                    abducens nucleus and contralateral
    #                                    medial rectus subnucleus; origin of
    #                                    medial vestibulospinal tract; head
    #                                    stabilization
    #   inferior vestibular nucleus  -> otolith-canal integration;
    #                                    vestibulocerebellar relay; extends
    #                                    into the medulla (involved in
    #                                    Wallenberg syndrome)
    #
    # Do not attempt to resolve these as sub-paths of the vestibular
    # nuclei — resolve them at the prose subdivision level through the
    # references.

References
----------
*   **Canonical vestibular anatomy:** Goldberg, J.M., Wilson, V.J.,
    Cullen, K.E., Angelaki, D.E., Broussard, D.M., Büttner-Ennever,
    J.A., Fukushima, K., Minor, L.B. (2012). *The Vestibular System: A
    Sixth Sense*. (Vestibular nuclei and the vestibular system —
    definitive.)
*   **Vestibular brainstem — review:** Highstein, S.M., Fay, R.R., Popper,
    A.N. (eds.) (2004). *The Vestibular System*. (Vestibular nuclei
    subdivisions and projections.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Vestibular nuclei in
    overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An Atlas
    of Structures, Sections, and Systems*, 8th ed. (Vestibular nuclei
    and the pontomedullary junction.)
*   **VOR — review:** Leigh, R.J., Zee, D.S. (2015). *The Neurology of
    Eye Movements*, 5th ed. (Vestibulo-ocular reflex — vestibular
    nuclei as the central node.)
*   **Vestibulospinal tracts:** Wilson, V.J., Peterson, B.W. (1981).
    "Vestibulospinal and reticulospinal systems." In *Handbook of
    Physiology*. (Lateral and medial vestibulospinal tracts — vestibular
    nuclei as the source.)
*   **Vestibulocerebellar pathways:** Manto, M., Gruol, D.L.,
    Schmahmann, J.D., Koibuchi, N., Rossi, F. (eds.) (2013). *Handbook
    of the Cerebellum and Cerebellar Disorders*. (Vestibulocerebellar
    pathways — vestibular nuclei projections to the cerebellum.)
*   **Ascending vestibular pathway:** Lopez, C., Blanke, O. (2011). "The
    thalamocortical vestibular system in health and disease." *Brain
    Research Bulletin* 85:16–22. (Ascending vestibular pathway —
    vestibular nuclei projections to thalamus and cortex.)
*   **Acoustic neuroma (contrast — the CN VIII nerve, not the nuclei):**
    Matthies, C., Samii, M. (1997). "Management of 1000 vestibular
    schwannomas (acoustic neuromas): clinical presentation."
    *Neurosurgery* 40:1–10. (Acoustic neuroma — vestibular schwannoma of
    the CN VIII nerve; distinct from the vestibular nuclei.)
*   **Vestibular neuritis (contrast — the CN VIII vestibular nerve, not
    the nuclei):** Strupp, M., Brandt, T. (2009). "Vestibular neuritis."
    *Seminars in Neurology* 29:509–519. (Vestibular neuritis —
    vestibular nerve lesion; distinct from the vestibular nuclei.)
*   **Labyrinthitis (contrast — the inner ear labyrinth, not the
    nuclei):** Baloh, R.W. (2003). "Vestibular neuritis." *New England
    Journal of Medicine* 348:1027–1032. (Labyrinthitis — inner ear
    labyrinth lesion; distinct from the vestibular nuclei.)
*   **BPPV (contrast — otoconia in the semicircular canals, not the
    nuclei):** Bhattacharyya, N., et al. (2017). "Clinical practice
    guideline: benign paroxysmal positional vertigo (update)."
    *Otolaryngology–Head and Neck Surgery* 156:S1–S47. (BPPV — otoconia
    in the semicircular canals; distinct from the vestibular nuclei.)
*   **Meniere's disease (contrast — endolymphatic hydrops, not the
    nuclei):** Sajjadi, H., Paparella, M.M. (2008). "Meniere's disease."
    *Lancet* 372:406–414. (Meniere's disease — endolymphatic hydrops;
    distinct from the vestibular nuclei.)
*   **Central vs. peripheral vestibular lesions:** Baloh, R.W., Kerber,
    K.A. (2011). *Baloh and Honrubia's Clinical Neurophysiology of the
    Vestibular System*, 5th ed. (Central vs. peripheral vestibular
    lesion patterns — vestibular nuclei are central.)
*   **Marie-Foix syndrome (contrast — pontine vestibular nuclei
    involvement):** Marie, P., Foix, C. (1913). "Les lésions des artères
    du cervelet." *Revue Neurologique* 25:177–190. (Lateral pontine
    syndrome — pontine vestibular nuclei involvement.)
*   **Wallenberg syndrome (contrast — inferior vestibular nucleus
    involvement):** Wallenberg, A. (1901). "Acute bulbar paralysis
    (embolic obstruction of the posterior inferior cerebellar artery)."
    *Archiv für Psychiatrie und Nervenkrankheiten* 34:923–959. (Lateral
    medullary syndrome — inferior vestibular nucleus involvement.)
*   **Cochlear nuclei (contrast — the OTHER sub-container of the
    vestibulocochlear nuclei):** Pickles, J.O. (2015). *An Introduction
    to the Physiology of Hearing*, 4th ed. (Cochlear nuclei — hearing;
    distinct from the vestibular nuclei.)
*   **MLF (contrast — the white-matter tract carrying vestibular
    projections):** Büttner-Ennever, J.A. (ed.) (1988). *Neuroanatomy of
    the Oculomotor System*. (MLF and the vestibulo-ocular reflex
    pathways from the vestibular nuclei.)
*   **Abducens nucleus (contrast — the downstream motor VOR efferent):**
    Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye Movements*, 5th
    ed. (Abducens nucleus — efferent node of the horizontal VOR;
    distinct from the vestibular nuclei.)
*   **SLEA (contrast — the vestibular nuclei are not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the vestibular nuclei.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the vestibular nuclei.)
*   NeuroNames — Vestibular nuclei (left); FMA — Vestibular nuclei (left
    member).
"""