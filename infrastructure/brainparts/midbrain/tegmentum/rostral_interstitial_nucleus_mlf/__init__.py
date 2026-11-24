"""
infrastructure.brainparts.midbrain.tegmentum.rostral_interstitial_nucleus_mlf
=============================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        ├── caudal_linear_nucleus        (midline leaf)
        ├── dorsal_raphe_nucleus         (midline leaf)
        ├── interpeduncular_nucleus      (midline leaf)
        ├── midbrain_reticular_formation (diffuse bilateral leaf)
        ├── periaqueductal_gray          (diffuse bilateral leaf)
        ├── red_nucleus                  (structure container — paired
        │                                 substantive leaves)
        └── rostral_interstitial_nucleus_mlf   <-- THIS MODULE
            ├── left                     (STRUCTURE CONTAINER —
            │   └── ...                    PAIRED — substantive
            └── right                    paired leaves — the
                └── ...                  riMLF, the vertical
                                         saccade generator)

**Primary synonym:** Rostral interstitial nucleus of the medial
longitudinal fasciculus; **riMLF**; **rostral iMLF**; **RI** (older
term); **nucleus interstitialis rostralis fasciculi longitudinalis
medialis** (Latin).
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). **Not a classical Nissl-defined nucleus.** A
**functionally-defined region** of the **rostral midbrain
tegmentum** — a **collection of neurons embedded within (and
adjacent to) the fibers of the medial longitudinal fasciculus
(MLF)** — **paired** (a left riMLF and a right riMLF). It is
**defined by its function** — the **vertical saccade generator** —
and by its **position** (at the **rostral end** of the MLF, at the
**diencephalon-midbrain junction**), **not by a sharp
cytoarchitectonic border**. **This is the same class of structure
as the pre-Bötzinger complex** (the respiratory rhythm kernel) —
**functionally defined, not cytoarchitectonic**.
**Container status:** **This module is a STRUCTURE CONTAINER, not a
leaf.** It holds the **left riMLF** and the **right riMLF** as
**substantive paired leaves** — each is a **functionally-defined
region** (the vertical saccade generator on its side). **The riMLF
is a GENUINELY PAIRED structure** — the left and right are **two
real anatomical regions** — **and it follows the substantive-
paired-leaf pattern** established by the **red nucleus**. **The
structure container holds the left and right leaves; the leaves
carry the substantive anatomy.**
**Part of:** The **tegmentum** region container — as a **structure
container** for a **paired** structure. **The riMLF is NOT a
cranial nerve nucleus** and is **NOT cross-listed** with
``cranial_nerve_nuclei/``.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — as a **structure container**
for a **paired** structure.
**Structural children (expected — the tree is authoritative):**
*   ``left/`` — the **left riMLF** — a **substantive paired
    leaf** — the **left vertical saccade generator**.
*   ``right/`` — the **right riMLF** — a **substantive paired
    leaf** — the **right vertical saccade generator** — the
    **mirror** of the left.
**Boundary status (STRUCTURE CONTAINER — the SECOND paired tegmentum
structure represented as a structure container, after the red
nucleus):** **Boundary case — the riMLF is a STRUCTURE CONTAINER.**
It holds the **left riMLF** and the **right riMLF** as
**substantive paired leaves** — each is a **functionally-defined
region** (the vertical saccade generator on its side). **The riMLF
is the SECOND paired tegmentum structure to be represented as a
structure container** — after the **red nucleus**. **The structure-
container pattern is the SAME:** one "home" at
``tegmentum/rostral_interstitial_nucleus_mlf/``, with ``left/``
and ``right/`` as **substantive paired leaves**. **The substantive-
paired-leaf pattern is the SAME:** the **left** and **right**
leaves are **substantive anatomical content**, not thin side
containers.
**Boundary status (FUNCTIONALLY-DEFINED REGION — NOT a classical
Nissl-defined nucleus — the SAME class as the pre-Bötzinger
complex):** **Boundary case — the riMLF is a FUNCTIONALLY-DEFINED
REGION, NOT a classical Nissl-defined nucleus.** It is a
**collection of neurons embedded within (and adjacent to) the
fibers of the MLF** — defined by **its function** (the **vertical
saccade generator**) and by **its position** (at the **rostral end
of the MLF**, at the **diencephalon-midbrain junction**) — **not by
a sharp cytoarchitectonic border**. **This is the SAME class of
structure as the pre-Bötzinger complex** (the **respiratory rhythm
kernel** — **functionally defined, not cytoarchitectonic**). **The
pre-Bötzinger complex is a functionally-defined REGION** — **the
riMLF is a functionally-defined REGION** — **both are the same
structural class** (functionally-defined, not Nissl-defined).
**The riMLF is NOT a classical nucleus** (unlike the **red
nucleus**, the **substantia nigra**, the **CN nuclei**, etc. — all
Nissl-defined nuclei) — **it is a functionally-defined region**
like the **preBötC**, the **pretectum**, and the **PAG** (all
functionally-defined regions in the family). Consumers must **not**
treat the riMLF as a **sharply bounded Nissl nucleus** — it is a
**functionally-defined region**.
**Boundary status (PREMOTOR SACCADE GENERATOR — the VERTICAL
saccade generator — the counterpart of the PPRF's HORIZONTAL
saccade generator):** **Boundary case — the riMLF is a PREMOTOR
SACCADE GENERATOR** — specifically, the **vertical saccade
generator**. In the family's **structure-class taxonomy**, it is a
**premotor saccade generator** — the **SAME class** as the **PPRF**
(pontine — **horizontal** saccade generator) — **but for
VERTICAL saccades** rather than horizontal. **The PPRF and the
riMLF are the TWO PREMOTOR SACCADE GENERATORS of the brainstem**
— the **PPRF for horizontal**, the **riMLF for vertical** — and
**both sit between the SC (command level) and the CN III/IV/VI
nuclei (motor level)** in the **saccade hierarchy**. **The riMLF
is the VERTICAL PREMOTOR SACCADE GENERATOR** — the **PPRF is the
HORIZONTAL PREMOTOR SACCADE GENERATOR**. **Premotor saccade
generators carry NO coupling warning** — same rule as motor
nuclei, premotor motor relays (the **red nucleus**), sensor nuclei,
relay nuclei, neuromodulatory nuclei, limbic relays, diffuse
reticular regions, and conduction pathways. **The riMLF is a
PREMOTOR SACCADE GENERATOR — NOT an oscillator, NOT a motor
nucleus, NOT a command generator (the SC is the command
generator).** See *Function in the Human Brain* and *The Saccade
Hierarchy*.
**Boundary status (BILATERAL COORDINATION VIA THE POSTERIOR
COMMISSURE — NOT intrinsic coupling — NO coupling warning):**
**Boundary case — the left and right riMLF are BILATERALLY
COORDINATED via the POSTERIOR COMMISSURE** — a **conduction
pathway** — **NOT via intrinsic coupling**. **The two riMLF must
fire together to produce conjugate vertical saccades** — **the
left riMLF and the right riMLF project to the CN III/IV nuclei on
both sides** (via the **crossed** and **uncrossed** components of
the **posterior commissure**) — **and the coordination is
provided by the posterior commissure** (a **conduction pathway**),
**not by intrinsic riMLF-to-riMLF coupling**. **This is a
DIFFERENT kind of two-sided coordination than both:**
*   **The oscillators (the pre-Bötzinger complex, the Bötzinger
    complex, the pFRG)** — **two sides that must synchronize to
    produce a single rhythm** — **the synchronization is INTRINSIC
    to the oscillator** — **the coupling warning attaches to the
    oscillator**.
*   **The red nucleus** — **two independent nuclei** — **each
    controls its own (contralateral) spinal cord side** — **no
    intrinsic coupling; the two sides are coordinated via their
    own projections** (cerebellar and cortical inputs).
*   **The riMLF** — **two functionally-defined regions that
    must fire together to produce conjugate vertical saccades**
    — **the coordination is provided by the POSTERIOR
    COMMISSURE** (a **conduction pathway**) — **NOT intrinsic
    coupling** — **the two sides are coordinated via a
    CONDUCTION PATHWAY, not via intrinsic riMLF-to-riMLF
    coupling**.
**The riMLF is the FIRST premotor saccade generator in the family
with EXPLICIT bilateral coordination via a conduction pathway**
— the **posterior commissure**. **The two sides are NOT
independent** (unlike the red nucleus) — **and NOT intrinsically
coupled** (unlike the oscillators) — **they are coordinated via
a conduction pathway** (the **posterior commissure**). **The
posterior commissure is the CONDUCTION PATHWAY that provides
the coordination** — **the riMLF's two sides are coordinated
EXTRINSICALLY, via a conduction pathway, not INTRINSICALLY, via
intrinsic coupling**. **NO coupling warning** — the coordination
is via a **conduction pathway**, not an **intrinsic oscillator
coupling** — same rule as every non-oscillator class.
**Boundary status (CONTRALATERAL POSTERIOR COMMISSURE — the
POSTERIOR COMMISSURE CARRIES the riMLF FIBERS ACROSS the
midline):** **Boundary case — the riMLF fibers CROSS the midline
in the POSTERIOR COMMISSURE.** The **posterior commissure** — a
**conduction pathway** at the **diencephalon-midbrain junction**
— **carries the riMLF fibers** from the **left riMLF** to the
**right CN III/IV nuclei** (for the **upward** vertical
saccades) and from the **right riMLF** to the **left CN III/IV
nuclei** (for the **downward** vertical saccades) — **the
posterior commissure is the CONDUCTION PATHWAY that carries the
riMLF fibers across the midline**. **The riMLF is the NUCLEUS**
— **the posterior commissure is the CONDUCTION PATHWAY**.
**They are DIFFERENT STRUCTURES** — the **riMLF** is the
**functionally-defined region** (the premotor saccade
generator); the **posterior commissure** is the **conduction
pathway** (the fibers). Consumers must **not** conflate the
riMLF with the posterior commissure — the **riMLF is the
nucleus, the posterior commissure is the fibers that cross in
it**.
**Boundary status (NOT the MLF itself — the MLF is the
LONGITUDINAL FASCICULUS that the riMLF is EMBEDDED WITHIN):**
**Boundary case — the riMLF is NOT the MLF itself.** The **medial
longitudinal fasciculus (MLF)** is a **longitudinal fiber tract**
— a **conduction pathway** — that **coordinates the CN III, IV,
and VI nuclei for conjugate gaze**. **The riMLF is a collection of
NEURONS EMBEDDED WITHIN (and adjacent to) the MLF fibers** — at
the **rostral end** of the MLF — the **"rostral interstitial
nucleus OF the MLF"** — the **"nucleus"** is **embedded within
the "fasciculus"**. **They are DIFFERENT STRUCTURES** — the
**MLF** is a **conduction pathway** (the **fiber bundle**); the
**riMLF** is a **functionally-defined region** (the **neurons
embedded within and adjacent to the fiber bundle**). Consumers
must **not** conflate the riMLF with the MLF — the **MLF is the
tract, the riMLF is the nucleus embedded within it**.
**Boundary status (NOT the PPRF — the PPRF is the HORIZONTAL
saccade generator, in the PONS):** **Boundary case — the riMLF is
NOT the PPRF.** The **PPRF** (paramedian pontine reticular
formation) is the **HORIZONTAL saccade generator** — in the
**pons**. **The riMLF is the VERTICAL saccade generator** — in
the **midbrain**. **They are DIFFERENT STRUCTURES at DIFFERENT
levels** — the **PPRF** is **pons** (horizontal); the **riMLF** is
**midbrain** (vertical). **The two together are the premotor
saccade generators of the brainstem** — the **PPRF for
horizontal**, the **riMLF for vertical** — **both between the SC
(command) and the CN nuclei (motor)**. Consumers must **not**
conflate the riMLF with the PPRF.
**Boundary status (NOT the interstitial nucleus of Cajal — the
interstitial nucleus of Cajal is the VERTICAL GAZE HOLDING
structure):** **Boundary case — the riMLF is NOT the interstitial
nucleus of Cajal.** The **interstitial nucleus of Cajal** is a
**separate midbrain tegmentum structure** — the **vertical gaze
HOLDING** structure (the **neural integrator** for vertical
gaze). **The riMLF is the vertical gaze GENERATOR** (the **premotor
saccade generator** for vertical saccades). **They are DIFFERENT
STRUCTURES** — the **riMLF** is the **saccade generator** (the
"where to look" — the **velocity command**); the **interstitial
nucleus of Cajal** is the **gaze holder** (the "where the eye is"
— the **position integrator**). **Both are midbrain, both are
vertical gaze-related, but different functions.** Consumers must
**not** conflate the riMLF with the interstitial nucleus of Cajal.
**Boundary status (NOT the superior colliculus — the SC is the
COMMAND level, the riMLF is the PREMOTOR level):** **Boundary
case — the riMLF is NOT the superior colliculus.** The **SC** is
the **saccade command generator** — the **top level** of the
**saccade hierarchy**. **The riMLF is the premotor saccade
generator** — the **second level** — **between the SC and the CN
nuclei**. **The SC DECIDES where to look** (in the **motor
map**); **the riMLF EXECUTES** (transforms the SC command into the
premotor saccade signal that drives the CN nuclei). **They are
DIFFERENT STRUCTURES at DIFFERENT levels** of the saccade
hierarchy. Consumers must **not** conflate the riMLF with the
SC.
**Boundary status (NOT the CN III/IV nuclei — those are the MOTOR
level):** **Boundary case — the riMLF is NOT the CN III/IV
nuclei.** The **oculomotor nucleus** (CN III) and the **trochlear
nucleus** (CN IV) are the **motor nuclei** that **execute** the
vertical saccade by driving the **extraocular muscles** — the
**motor level** of the saccade hierarchy. **The riMLF is the
premotor saccade generator** — the **premotor level** — **UPSTREAM
of the CN nuclei**. **They are DIFFERENT STRUCTURES at DIFFERENT
levels**. Consumers must **not** conflate the riMLF with the CN
III/IV nuclei.
**Boundary status (NOT the posterior commissure — the posterior
commissure is the CONDUCTION PATHWAY):** **Boundary case — the
riMLF is NOT the posterior commissure.** The **posterior
commissure** — a **conduction pathway** at the **diencephalon-
midbrain junction** — **carries the riMLF fibers across the
midline** (from the **left riMLF** to the **right CN III/IV
nuclei**, and from the **right riMLF** to the **left CN III/IV
nuclei**) — the **conduction pathway** that **coordinates** the
two riMLF. **The riMLF is the NUCLEUS** (the **functionally-
defined region**); the **posterior commissure** is the
**conduction pathway** (the **fibers**). **They are DIFFERENT
STRUCTURES** — the **riMLF** is the **nucleus**; the **posterior
commissure** is the **conduction pathway**. Consumers must **not**
conflate the riMLF with the posterior commissure.
**Boundary status (NOT the pretectum — the pretectum is a
SEPARATE REGION at the DIENCEPHALON-MIDBRAIN JUNCTION, ROSTRAL to
the SC):** **Boundary case — the riMLF is NOT the pretectum.** The
**pretectum** (``.../midbrain/pretectum/``) is a **separate
region** at the **diencephalon-midbrain junction** — the
**pupillary and optokinetic** region — **rostral** to the SC.
**The riMLF is a part of the midbrain tegmentum** — the
**vertical saccade generator** — **not the pretectum**. **They are
DIFFERENT REGIONS in DIFFERENT functional systems** — the
**pretectum** is **pupillary and optokinetic**; the **riMLF** is
**vertical saccadic**. Consumers must **not** conflate the riMLF
with the pretectum.
**Boundary status (NOT the red nucleus — the red nucleus is the
LIMB-MOTOR premotor relay, in the rostral midbrain tegmentum
nearby):** **Boundary case — the riMLF is NOT the red nucleus.**
The **red nucleus** (``.../tegmentum/red_nucleus/``) is the
**limb-motor premotor relay** — the **rubrospinal motor
coordination** — **ventral and rostral** to the riMLF. **The riMLF
is the vertical saccade generator** — **dorsomedial** to the red
nucleus. **They are DIFFERENT STRUCTURES** — both **premotor
relays** — **the red nucleus for LIMB motor control**, **the
riMLF for VERTICAL SACCADES** — **different functional
subsystems**. Consumers must **not** conflate the riMLF with the
red nucleus.
**Boundary status (PREMOTOR SACCADE GENERATOR — NO coupling
warning — the bilateral coordination is via the POSTERIOR
COMMISSURE, a conduction pathway, NOT intrinsic coupling):**
**Boundary case — the riMLF carries NO coupling warning.** The
**coupling warning** attaches to **OSCILLATORS** (the
pre-Bötzinger complex, the Bötzinger complex, the pFRG) — and the
**riMLF is not an oscillator**. **It is a premotor saccade
generator** — the **vertical saccade generator** — **its two
sides are coordinated via the POSTERIOR COMMISSURE** (a
**conduction pathway**), **not via intrinsic coupling**. **Premotor
saccade generators carry NO coupling warning** — same rule as
every non-oscillator class. **The riMLF is a premotor saccade
generator** — **no coupling warning**.

Overview
--------
The riMLF is the **vertical saccade generator** — a
**functionally-defined region** of the **rostral midbrain
tegmentum**, at the **diencephalon-midbrain junction** — a
**collection of neurons embedded within (and adjacent to) the
fibers of the MLF** — **paired** (a **left riMLF** and a **right
riMLF**). It is **defined by its function** (the **vertical
saccade generator**) and by its **position** (the **rostral end**
of the MLF) — **not by a sharp cytoarchitectonic border** — **the
same class of structure as the pre-Bötzinger complex**
(**functionally defined, not Nissl-defined**). It is the
**premotor saccade generator** for **vertical saccades** — the
**counterpart of the PPRF** (the **horizontal** saccade
generator, in the **pons**) — and it sits **between the superior
colliculus (command) and the CN III/IV nuclei (motor)** in the
**saccade hierarchy**. **The riMLF is the SECOND paired tegmentum
structure represented as a structure container** — after the **red
nucleus** — and it **follows the same substantive-paired-leaf
pattern** (the **left** and **right** leaves carry the
substantive anatomy). **The two sides are coordinated via the
POSTERIOR COMMISSURE** — a **conduction pathway** — **not via
intrinsic coupling**.

**The riMLF is a FUNCTIONALLY-DEFINED REGION — NOT a classical
Nissl-defined nucleus.** It is a **collection of neurons embedded
within the MLF fibers** — **the same class of structure as the
pre-Bötzinger complex**.

**The riMLF is a PREMOTOR SACCADE GENERATOR — the VERTICAL
saccade generator.** It is the **same class** as the **PPRF** (the
**horizontal** saccade generator) — **but for vertical saccades
rather than horizontal**. **The PPRF and the riMLF are the TWO
PREMOTOR SACCADE GENERATORS of the brainstem.**

**The two riMLF sides are coordinated via the POSTERIOR
COMMISSURE** — a **conduction pathway** — **not via intrinsic
coupling**. **The riMLF is the FIRST premotor saccade generator in
the family with explicit bilateral coordination via a conduction
pathway.** **NO coupling warning** — the coordination is via a
**conduction pathway** (the posterior commissure), not an
**intrinsic oscillator coupling**.

**The riMLF is the anatomical substrate for TWO named clinical
syndromes** — **progressive supranuclear palsy (PSP)** (with the
**SNr** — the **vertical gaze palsy** of PSP) and **Parinaud
syndrome** (with the **posterior commissure** — the **upgaze
palsy** of Parinaud) — the **first paired structure in the
tegmentum to carry named clinical syndromes directly**. See
*Associated Disorders*.

**The riMLF is NOT a CN nucleus.** It is **not** cross-listed with
``cranial_nerve_nuclei/`` — it has **one path only**:
``.../tegmentum/rostral_interstitial_nucleus_mlf/`` (as a structure
container) with ``left/`` and ``right/`` children.

The Structure-Container Pattern — the SECOND Paired Structure
-------------------------------------------------------------
**The riMLF is the SECOND paired tegmentum structure represented as
a structure container** — after the **red nucleus**. **The
structure-container pattern is the SAME:** one "home" at
``tegmentum/rostral_interstitial_nucleus_mlf/``, with ``left/`` and
``right/`` as **substantive paired leaves**. **The substantive-
paired-leaf pattern is the SAME:** the **left** and **right**
leaves are **substantive anatomical content**, not thin side
containers.

**The two patterns are consistent** — the **red nucleus** and the
**riMLF** are **both genuinely paired structures** — **and both
follow the substantive-paired-leaf pattern**. **The structure
container** holds the **left** and **right** leaves; **the leaves**
carry the **substantive anatomy**.

**The riMLF is the FIRST functionally-defined paired structure
represented as a structure container** — the **red nucleus is the
first Nissl-defined paired structure**. **The class distinction**
(functionally-defined vs. Nissl-defined) is **orthogonal** to the
**laterality** (paired vs. non-paired) — the **riMLF** is
**functionally-defined AND paired**; the **red nucleus** is
**Nissl-defined AND paired**; the **CLi** is **Nissl-defined AND
midline**; the **MRF** is **functionally-defined AND diffuse
bilateral**. **The structural taxonomy now has ALL COMBINATIONS
of (defined-by × laterality)**: Nissl × paired (red nucleus), Nissl
× midline (CLi, DR, IPN), Nissl × diffuse bilateral (none yet),
functionally-defined × paired (riMLF), functionally-defined ×
midline (none yet), functionally-defined × diffuse bilateral (MRF,
PAG). **The structural taxonomy is more fully exercised.**

The Saccade Hierarchy
---------------------
The **saccade hierarchy** is the **functional context** for the
riMLF. It is a **hierarchy** with the **riMLF** at the **premotor
level**:

*   **SC (command level)** — the **superior colliculus** —
    **sensorimotor integration** — receives **visual, auditory,
    and somatosensory** input and generates **saccade commands**
    in a **motor map**. **The SC is at the TOP of the saccade
    hierarchy.**

*   **PPRF (horizontal premotor level)** — the **paramedian
    pontine reticular formation** — **pons** — the **horizontal
    saccade generator** — **transforms** the SC's **horizontal**
    saccade command into the **premotor saccade signal** for the
    **horizontal** component.

*   **riMLF (vertical premotor level)** — **THIS STRUCTURE** —
    **midbrain** — the **vertical saccade generator** —
    **transforms** the SC's **vertical** saccade command into the
    **premotor saccade signal** for the **vertical** component.

*   **CN III / IV / VI nuclei (motor level)** — the **oculomotor
    nucleus** (CN III), the **trochlear nucleus** (CN IV), and
    the **abducens nucleus** (CN VI) — **motor nuclei** — they
    **execute** the saccade by driving the **extraocular
    muscles**.

*   **Extraocular muscles (effector level)** — the **six
    extraocular muscles** per eye — **the effectors** of the
    saccade.

**The riMLF is the VERTICAL premotor saccade generator** — **between
the SC (command) and the CN III/IV nuclei (motor)** — the
**midbrain premotor level**. **The PPRF is the HORIZONTAL premotor
saccade generator** — **between the SC (command) and the CN VI/III
nuclei (motor)** — the **pontine premotor level**. **The two
together** — the **PPRF** (horizontal) and the **riMLF**
(vertical) — are the **premotor saccade generators of the
brainstem** — **both between the SC and the CN nuclei**.

**The riMLF is NOT the PPRF, NOT the SC, NOT the CN nuclei, and
NOT the extraocular muscles** — it is the **vertical premotor
saccade generator** — a **distinct level** of the saccade
hierarchy.

The Posterior Commissure — the Bilateral Coordination Pathway
-------------------------------------------------------------
The **posterior commissure** — a **conduction pathway** at the
**diencephalon-midbrain junction** — **carries the riMLF fibers
across the midline** — **the left riMLF fibers** (for the
**upward** vertical saccades) **cross to the RIGHT CN III/IV
nuclei** — **the right riMLF fibers** (for the **downward**
vertical saccades) **cross to the LEFT CN III/IV nuclei** — **the
posterior commissure is the CONDUCTION PATHWAY that carries the
riMLF fibers across the midline**.

**The riMLF and the posterior commissure are DIFFERENT
STRUCTURES:**
*   **The riMLF** — the **functionally-defined region** — the
    **premotor saccade generator** — the **NUCLEUS**.
*   **The posterior commissure** — the **conduction pathway** —
    the **fibers** that cross the midline.

**The bilateral coordination of the two riMLF is via the posterior
commissure** — a **conduction pathway** — **not via intrinsic
coupling**. **The two riMLF are coordinated EXTRINSICALLY, via a
conduction pathway** — **not INTRINSICALLY, via intrinsic
oscillator coupling**. **This is a DIFFERENT kind of two-sided
coordination than the oscillators' intrinsic synchronization**
(the **pre-Bötzinger complex** — **intrinsic**; **NO conduction
pathway** is required for the bilateral synchrony — the
**oscillators must fire together because of intrinsic coupling**)
— **the riMLF's two sides are coordinated via the posterior
commissure** — a **conduction pathway** — **not via intrinsic
coupling**. **NO coupling warning** — the coordination is via a
**conduction pathway**, not an **intrinsic oscillator coupling**.

**The posterior commissure is the CONDUCTION PATHWAY that the
riMLF fibers cross in** — **the riMLF is the NUCLEUS, the
posterior commissure is the fibers**. **They are DIFFERENT
STRUCTURES** — **the riMLF** is the **premotor saccade
generator**; the **posterior commissure** is the **conduction
pathway**. **Consumers must not conflate the riMLF with the
posterior commissure.**

Function in the Human Brain
---------------------------
The riMLF's function is **vertical saccade generation** — the
**premotor level** of the **vertical saccade hierarchy** —
**NOT** a sensory relay, **NOT** a modulatory nucleus, **NOT** a
motor nucleus, **NOT** a command generator (the **SC** is the
command generator), **NOT** an oscillator:

*   **Vertical Saccade Generation (the riMLF's primary function):**
    The riMLF **transforms** the **superior colliculus's vertical
    saccade command** into the **premotor saccade signal** that
    **drives the CN III/IV nuclei** — **the vertical saccade
    generator** — **the premotor level** of the **vertical saccade
    hierarchy**. **The riMLF is the VERTICAL PREMOTOR SACCADE
    GENERATOR** — the **counterpart of the PPRF** (the
    **horizontal** premotor saccade generator).

*   **Bilateral Coordination via the Posterior Commissure:** The
    **left riMLF** and the **right riMLF** **must fire together**
    to produce **conjugate vertical saccades** — **the left
    riMLF** drives the **upward** vertical saccades (via the
    **posterior commissure** to the **right CN III/IV nuclei**);
    **the right riMLF** drives the **downward** vertical
    saccades (via the **posterior commissure** to the **left
    CN III/IV nuclei**) — **the posterior commissure is the
    CONDUCTION PATHWAY that provides the coordination** — **NOT
    intrinsic coupling**.

*   **Vertical Gaze Holding (via the interstitial nucleus of
    Cajal — NOT the riMLF):** The **vertical gaze holding**
    (the **neural integrator** for vertical gaze — the "where
    the eye is") is mediated by the **interstitial nucleus of
    Cajal** — a **separate midbrain tegmentum structure** —
    **NOT the riMLF**. **The riMLF generates the vertical
    saccades** (the "where to look"); **the interstitial
    nucleus of Cajal holds the vertical gaze** (the "where the
    eye is"). **They are DIFFERENT structures with
    complementary functions** — **both vertical-gaze related,
    both midbrain, but different.**

*   **NOT a sensory relay.** The riMLF does **not** transduce or
    relay a specific sensory modality.

*   **NOT a modulatory nucleus.** The riMLF does **not** broadcast
    a single neuromodulator via volume transmission — it is a
    **premotor saccade generator**.

*   **NOT a motor nucleus.** The riMLF does **not** drive muscle
    directly — it **relays** to the **CN III/IV nuclei** via the
    **posterior commissure**. **The CN III/IV nuclei are the
    motor nuclei**; the **riMLF is a premotor saccade generator**.

*   **NOT the command generator.** The **superior colliculus**
    is the **command generator** — the **SC DECIDES where to
    look**; the **riMLF EXECUTES** (transforms the SC command
    into the premotor saccade signal). **Different levels of the
    saccade hierarchy.**

*   **NOT an oscillator.** The riMLF is a **premotor saccade
    generator** — it does **not** generate a rhythm. **Premotor
    saccade generators carry NO coupling warning** — same rule
    as every non-oscillator class.

**The unifying theme:** the riMLF is the **vertical saccade
generator** — a **functionally-defined region** of the **rostral
midbrain tegmentum** — the **premotor level** of the **vertical
saccade hierarchy** — **between the superior colliculus (command)
and the CN III/IV nuclei (motor)**. It is the **counterpart of
the PPRF** (the **horizontal** premotor saccade generator) — **the
two together are the premotor saccade generators of the
brainstem**. **The two riMLF sides are coordinated via the
POSTERIOR COMMISSURE** — a **conduction pathway** — **not via
intrinsic coupling** — **NO coupling warning**. **The riMLF is the
SECOND paired tegmentum structure represented as a structure
container** — after the **red nucleus** — and it **follows the
same substantive-paired-leaf pattern**.

Associated Disorders
--------------------
The riMLF is the **anatomical substrate** for two **named clinical
syndromes** — the **first paired structure in the tegmentum to
carry named clinical syndromes directly**:

*   **Progressive Supranuclear Palsy (PSP — DIRECT — the riMLF is
    one of two primary substrates; the other is the SNr):** **PSP**
    — **vertical gaze palsy** (especially **downward**),
    **postural instability**, **parkinsonism**, **cognitive
    impairment** — is a **tauopathy** that involves the
    **midbrain tegmentum** — **the riMLF** (the **vertical
    saccade generator** — the **loss of vertical saccades**)
    and the **SNr** (the **inhibitory gate on the SC** — the
    **loss of saccade inhibition** — **slow saccades**, **saccade
    hypometria**). **The riMLF IS ONE OF THE TWO primary
    substrates** — the **vertical saccade palsy** is the **riMLF**
    contribution. **The "supranuclear" in PSP means "above the
    CN nuclei"** — **the lesion is in the PREMOTOR saccade
    generators** (the **riMLF** for vertical, the **PPRF** for
    horizontal) **and the basal ganglia inhibitory gate** (the
    **SNr**) — **NOT in the CN III/IV/VI nuclei themselves**.
    **The riMLF is the VERTICAL premotor saccade generator** —
    **the PSP vertical gaze palsy is the riMLF (and SNr)
    contribution**.

*   **Parinaud Syndrome (Dorsal Midbrain Syndrome — DIRECT — the
    riMLF fibers are interrupted in the posterior commissure; the
    posterior commissure is the lesion site):** **Parinaud
    syndrome** — **upgaze palsy**, **convergence-retraction
    nystagmus**, **light-near dissociation**, **Collier sign**
    (eyelid retraction) — is a **dorsal midbrain syndrome**
    caused by a **dorsal midbrain lesion** (e.g., **pineal
    region tumor**, **tectal glioma**, **hydrocephalus**). **The
    upgaze palsy** of Parinaud syndrome is caused by the **lesion
    interrupting the riMLF fibers in the posterior commissure**
    — **the riMLF fibers (for upward vertical saccades) cross
    in the posterior commissure** — **a posterior commissure
    lesion interrupts the bilateral riMLF projection** —
    **producing upgaze palsy**. **The riMLF is the anatomical
    substrate for the upgaze palsy** — **the posterior
    commissure is the lesion site** (the **fibers crossing in
    it**). **The riMLF fibers are interrupted; the riMLF nucleus
    itself may be spared.** **The distinction is critical:**
    **the posterior commissure is the CONDUCTION PATHWAY**;
    **the riMLF is the NUCLEUS** — **a Parinaud syndrome lesion
    in the posterior commissure is a CONDUCTION PATHWAY lesion,
    not a riMLF nucleus lesion** — **but the riMLF's FUNCTION is
    disrupted** (the fibers are interrupted).

*   **Unilateral riMLF Lesion (INDIRECT — asymmetric vertical gaze
    palsy):** A **focal lesion** of the **left or right riMLF** —
    from **small infarction**, **demyelination**, or **tumor** —
    produces **asymmetric vertical gaze palsy** — **typically
    worse in one vertical direction** (the **riMLF's up/down
    specific fibers**) — **but the bilateral coordination via
    the posterior commissure means that a unilateral riMLF lesion
    often produces incomplete or asymmetric vertical gaze palsy
    rather than complete palsy of one direction**. **The riMLF
    is a contributor** — **the posterior commissure provides the
    bilateral coordination**.

*   **No Named "riMLF Syndrome" per se — but PSP and Parinaud
    syndrome are the named syndromes:** The riMLF is **one of the
    two primary substrates** for **PSP** (the **vertical gaze
    palsy**) — **the SNr is the other** — and it is the
    **anatomical substrate** (via its **fibers crossing in the
    posterior commissure**) for the **upgaze palsy of Parinaud
    syndrome** — **the posterior commissure is the lesion site,
    not the riMLF nucleus**. **The riMLF has no named syndrome
    of its own** — **PSP and Parinaud syndrome are the named
    syndromes** — **the riMLF is a substrate for both**.

**What is NOT here:** The riMLF is **not** the substrate for
**horizontal gaze palsy** (the **PPRF** — the **horizontal**
saccade generator — **NOT** the riMLF), **horizontal saccade
deficits** (the **PPRF** — **NOT** the riMLF), **internuclear
ophthalmoplegia** (the **MLF** — **NOT** the riMLF),
**Weber syndrome** (the **cerebral peduncle** — **NOT** the
riMLF), **Benedikt / Claude syndromes** (the **red nucleus** +
the **CN III fascicles** — **NOT** the riMLF),
**Nothnagel syndrome** (the **tectum** / **superior cerebellar
peduncle** — **NOT** the riMLF), **Parinaud syndrome as a
riMLF-NUCLEUS syndrome** (the **posterior commissure is the
lesion site** — the **riMLF's FIBERS are interrupted** — the
**riMLF nucleus itself may be spared** — **the riMLF is the
anatomical substrate, the posterior commissure is the lesion
site**), **progressive supranuclear palsy as a riMLF-EXCLUSIVE
syndrome** (the **SNr is the other primary substrate** — **both
the riMLF and the SNr are involved**), **Parkinson's disease**
(the **substantia nigra pars compacta** — **NOT** the riMLF),
**Huntington's disease** (the **striatum** — **NOT** the
riMLF), **ALS** (the **corticospinal tract** and the
**anterior horn cells** — **NOT** the riMLF), **pupillary
light reflex deficits** (the **pretectum** and the **EW
nucleus** — **NOT** the riMLF), **oculomotor palsy** (the
**CN III nucleus** — **NOT** the riMLF), **trochlear palsy**
(the **CN IV nucleus** — **NOT** the riMLF), **trigeminal
sensory deficits** (the **trigeminal ganglion**, the **main
sensory**, and the **spinal trigeminal nucleus** — **NOT** the
riMLF), **CCHS** (RTN), **OIRD** (pre-Bötzinger complex —
NK1R neurons), **Rett syndrome** (pre-Bötzinger complex),
**SIDS** (proposed — pre-Bötzinger complex + arcuate nucleus),
**essential hypertension / sympathetic overactivity** (C1 group
/ RVLM), or **Kluver-Bucy syndrome** (amygdala). Its clinical
relevance is **direct** for **PSP** (with the **SNr**) and
**Parinaud syndrome** (via the **posterior commissure**) — but
the **riMLF is one substrate** in each, not the sole
substrate. **The riMLF has no named syndrome of its own —
PSP and Parinaud syndrome are the named syndromes.**

Lateralization Notes
--------------------
This is the **rostral_interstitial_nucleus_mlf** structure
container — its structural children are the **left riMLF** and
the **right riMLF** (substantive paired leaves). **The two sides
are BILATERALLY SYMMETRIC paired functionally-defined regions** —
each is an **independent vertical saccade generator** on its
side — **but their clinical patterns are BILATERAL** because the
**two sides are coordinated via the POSTERIOR COMMISSURE**.

*   **Paired Structure — Two Independent Regions:** Each side is
    an **independent riMLF** — the **left riMLF** and the
    **right riMLF** — each is a **functionally-defined region**
    (the **vertical saccade generator** on its side). **The two
    sides are structurally symmetric** — same position (at the
    **rostral end of the MLF**), same function (the **vertical
    saccade generator**).

*   **BILATERAL Coordination via the POSTERIOR COMMISSURE — NOT
    intrinsic coupling:** The **left and right riMLF** are
    **BILATERALLY COORDINATED via the POSTERIOR COMMISSURE** —
    a **conduction pathway** — **NOT via intrinsic coupling**.
    **The two riMLF must fire together to produce conjugate
    vertical saccades** — the **left riMLF** drives the
    **upward** vertical saccades (via the **posterior
    commissure** to the **right CN III/IV nuclei**); the
    **right riMLF** drives the **downward** vertical saccades
    (via the **posterior commissure** to the **left CN III/IV
    nuclei**) — **the posterior commissure is the CONDUCTION
    PATHWAY that provides the coordination** — **NOT intrinsic
    riMLF-to-riMLF coupling**.

*   **NO Coupling Warning — the riMLF is a PREMOTOR SACCADE
    GENERATOR:** The **pre-Bötzinger complex** carries a
    **coupling warning** because it is an **oscillator** whose
    two sides must synchronize to produce a single rhythm — the
    **synchronization is INTRINSIC** to the oscillator. The
    **riMLF** is a **premotor saccade generator** — its two
    sides are coordinated via the **posterior commissure** (a
    **conduction pathway**) — **NOT via intrinsic coupling**.
    **Premotor saccade generators carry NO coupling warning** —
    same rule as every non-oscillator class. **The riMLF is the
    FIRST premotor saccade generator in the family with explicit
    bilateral coordination via a conduction pathway** — **the
    coordination is via the POSTERIOR COMMISSURE, NOT via
    intrinsic coupling** — **NO coupling warning**.

*   **Bilateral Clinical Pattern — NOT Contralateral:** Unlike the
    **red nucleus** (which has a **contralateral** clinical
    pattern — a left red nucleus lesion produces right-sided
    motor deficits, because the **rubrospinal tract decussates**),
    the **riMLF** has a **BILATERAL** clinical pattern — a
    **unilateral riMLF lesion** produces **asymmetric vertical
    gaze palsy** (because the **posterior commissure provides
    the bilateral coordination** — **the other side's riMLF
    contributes to the vertical saccades via the crossed
    posterior commissure fibers**). **The riMLF's clinical
    pattern is BILATERAL** — **not contralateral** — **because
    the two sides are coordinated via the posterior commissure,
    not independent.** **This is the FIRST premotor saccade
    generator in the family with a BILATERAL clinical pattern**
    — **distinct from the red nucleus's CONTRALATERAL pattern**
    — **distinct from the oscillators' RHYTHM-COUPLING pattern**.

*   **No SLEA Warning:** The riMLF is **SLEA-free** — it is
    **not** an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The riMLF is **not**
    part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The riMLF is **not** a
    rhinencephalon structure.

**The riMLF is a strict mirror pair** — the **left riMLF** and
the **right riMLF** are **structurally identical** — **and their
clinical patterns are BILATERAL** — **not contralateral** —
because the **two sides are coordinated via the posterior
commissure**. **The riMLF's clinical pattern is a NEW pattern in
the family** — **BILATERAL** — **distinct from the red nucleus's
CONTRALATERAL pattern** — **distinct from the oscillators'
RHYTHM-COUPLING pattern**. **The bilateral pattern is the
structural expression of the riMLF's function:** the **two
riMLF must fire together to produce conjugate vertical saccades**
— **the coordination is via the posterior commissure** —
**not via intrinsic coupling** — **the bilateral clinical pattern
reflects the extrinsic coordination**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** This structure container
    does **not** import from ``.../left/`` or ``.../right/`` at
    the container level — the container's `__init__.py` is
    **namespace only**. The **left** and **right** leaves are
    **side-scoped leaves** — each carries its **own**
    cross-hemisphere rules (the left leaf does not import from
    the right, and vice versa).
*   **No cross-lobe imports.** This module does **not** import
    from the **superior colliculus**, the **PPRF**, the **CN
    III/IV nuclei**, the **posterior commissure**, the **MLF**,
    the **interstitial nucleus of Cajal**, the **pretectum**, the
    **red nucleus**, the **SNr**, the **basal ganglia**, or any
    other container. The riMLF's relationships to the SC, the
    PPRF, the CN III/IV nuclei, the posterior commissure, the
    MLF, the interstitial nucleus of Cajal, the pretectum, the
    red nucleus, the SNr, and the basal ganglia are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The riMLF's
    transmitter phenotypes (glutamatergic, GABAergic, etc.) are
    **``chemicals_hormones``-layer facts** — documented as
    **prose**, **never imported**.
*   **STRUCTURE CONTAINER — the SECOND paired tegmentum structure
    represented as a structure container, after the red nucleus.**
    The riMLF is a **structure container** at
    ``tegmentum/rostral_interstitial_nucleus_mlf/`` — holding the
    **left riMLF** and the **right riMLF** as **substantive
    paired leaves**. **This follows the SAME structure-container
    pattern as the red nucleus.**
*   **THE STRUCTURE-CONTAINER PATTERN — consistent with the red
    nucleus.** Every paired structure is a **structure container**
    with **substantive paired leaves** — the **red nucleus**
    (Nissl-defined) and the **riMLF** (functionally-defined) —
    **both follow the pattern**. **The structure-container
    pattern is consistent** — the **structure decides its own
    internal representation** — **paired leaves for paired
    structures**.
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER.** The tegmentum
    container's **paired-leaf rule** — *"each tegmentum nucleus
    is a paired structure (a ``left/`` leaf and a ``right/``
    leaf)"* — should be **AMENDED** to acknowledge the
    **structure-container pattern**: **paired structures are
    structure containers holding ``left/`` and ``right/``** —
    **not leaves directly under ``tegmentum/left/`` and
    ``tegmentum/right/``**. **The red nucleus** and the
    **riMLF** are the **two structure-container pattern
    examples**. The amendment should also acknowledge the
    **midline leaf** pattern (the **CLi**, **DR**, **IPN** —
    **pending** the joint Resolution B) and the **diffuse
    bilateral leaf** pattern (the **MRF**, **PAG** — **the PAG
    is the actual clean case**). **The tegmentum container
    amendment is now more fully evidenced** — **the paired
    structure-container pattern** (red nucleus + riMLF), **the
    diffuse bilateral leaf pattern** (PAG), and **the midline
    leaf pattern** (pending the joint Resolution B for the CLi,
    DR, and IPN).
*   **FUNCTIONALLY-DEFINED REGION — NOT a classical Nissl-defined
    nucleus.** The riMLF is a **collection of neurons embedded
    within the MLF fibers** — the **same class of structure as
    the pre-Bötzinger complex** — **functionally defined, not
    Nissl-defined**.
*   **PREMOTOR SACCADE GENERATOR — the VERTICAL saccade
    generator.** The riMLF is a **premotor saccade generator**
    — the **same class** as the **PPRF** (the **horizontal**
    saccade generator) — **but for vertical saccades**.
    **Premotor saccade generators carry NO coupling warning** —
    same rule as every non-oscillator class.
*   **BILATERAL COORDINATION VIA THE POSTERIOR COMMISSURE — NOT
    intrinsic coupling.** The **two riMLF sides** are
    **coordinated via the posterior commissure** — a
    **conduction pathway** — **not via intrinsic coupling**.
    **NO coupling warning** — the coordination is via a
    **conduction pathway**, not an **intrinsic oscillator
    coupling**.
*   **BILATERAL clinical pattern — NOT contralateral.** The
    riMLF has a **bilateral** clinical pattern (a unilateral
    lesion produces **asymmetric** vertical gaze palsy — **the
    posterior commissure provides the bilateral coordination**)
    — **distinct from the red nucleus's CONTRALATERAL pattern**
    — **distinct from the oscillators' RHYTHM-COUPLING pattern**.
*   **NOT A CN NUCLEUS.** The riMLF is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. It has **one path only** (as a
    structure container).
*   **NOT a motor nucleus — a PREMOTOR SACCADE GENERATOR.** The
    **CN III/IV nuclei** are the motor nuclei; the **riMLF** is
    a premotor saccade generator.
*   **NOT the command generator — the SC is the command
    generator.** The **riMLF EXECUTES** the SC's vertical
    saccade command.
*   **NOT the PPRF — the PPRF is the HORIZONTAL saccade
    generator, in the PONS.**
*   **NOT the interstitial nucleus of Cajal — that is the
    VERTICAL GAZE HOLDING structure.**
*   **NOT the MLF itself — the MLF is the LONGITUDINAL FASCICULUS
    that the riMLF is EMBEDDED WITHIN.**
*   **NOT the posterior commissure — that is the CONDUCTION
    PATHWAY.**
*   **NOT the pretectum — that is a SEPARATE REGION at the
    DIENCEPHALON-MIDBRAIN JUNCTION.**
*   **NOT the red nucleus — that is the LIMB-MOTOR premotor
    relay.**
*   **CHEMICALS-LAYER DISCIPLINE.** The riMLF's transmitter
    phenotypes are **``chemicals_hormones``-layer facts** —
    documented as **prose**, **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The riMLF is a
    **local structure container** under the tegmentum — no
    cross-listing.
*   **No nested cross-listing** at the container level. The
    riMLF container's **structural children are the left and
    right leaves** — **not** cross-listed with any other
    container.
*   **The on-disk tree is authoritative.** If the tree has
    ``.../tegmentum/rostral_interstitial_nucleus_mlf/left/`` and
    ``.../tegmentum/rostral_interstitial_nucleus_mlf/right/``,
    the **structure-container** representation is authoritative.

Usage
-----
Resolve the structure container by path::

    from infrastructure.brainparts.midbrain.tegmentum import rostral_interstitial_nucleus_mlf

Resolve a side-scoped leaf by path::

    from infrastructure.brainparts.midbrain.tegmentum.rostral_interstitial_nucleus_mlf.left import (
        ROSTRAL_INTERSTITIAL_NUCLEUS_MLF_LEFT_CHILDREN,
    )
    from infrastructure.brainparts.midbrain.tegmentum.rostral_interstitial_nucleus_mlf.right import (
        ROSTRAL_INTERSTITIAL_NUCLEUS_MLF_RIGHT_CHILDREN,
    )

Or by fully-qualified path string (leaves, not the container)::

    left_path = "midbrain.tegmentum.rostral_interstitial_nucleus_mlf.left"
    right_path = "midbrain.tegmentum.rostral_interstitial_nucleus_mlf.right"

**Do not** assume the riMLF is a **leaf** — it is a **structure
container** — it holds the **left riMLF** and the **right riMLF**
as **substantive paired leaves**.

**Do not** assume the riMLF is a **midline nucleus** or a
**diffuse bilateral region** — it is a **paired
functionally-defined region** — the **same class of structure
as the pre-Bötzinger complex** — **functionally defined, not
Nissl-defined**.

**Do not** assume the riMLF is a **cranial nerve nucleus** — it
is **not** and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the riMLF is a **motor nucleus** — it is a
**premotor saccade generator** — the **CN III/IV nuclei** are
the motor nuclei; the **riMLF** relays via the **posterior
commissure**.

**Do not** assume the riMLF is the **command generator** — the
**SC** is the command generator; the **riMLF EXECUTES**.

**Do not** assume the riMLF is the **PPRF** — the **PPRF** is
the **horizontal** saccade generator, in the **pons**; the
**riMLF** is the **vertical** saccade generator, in the
**midbrain**.

**Do not** assume the riMLF is the **interstitial nucleus of
Cajal** — that is the **vertical gaze HOLDING** structure; the
**riMLF** is the **vertical saccade GENERATOR**.

**Do not** assume the riMLF is the **MLF itself** — the **MLF**
is the **longitudinal fasciculus** that the riMLF is
**embedded within** — the **MLF** is a **conduction pathway**;
the **riMLF** is a **functionally-defined region** (the
**nucleus**).

**Do not** assume the riMLF is the **posterior commissure** —
the **posterior commissure** is the **conduction pathway** that
carries the riMLF fibers across the midline — **the riMLF is
the nucleus, the posterior commissure is the fibers**.

**Do not** assume the riMLF is the **pretectum** — the
**pretectum** is a **separate region** at the diencephalon-
midbrain junction. **The riMLF is a part of the midbrain
tegmentum** — the **vertical saccade generator**.

**Do not** assume the riMLF is the **red nucleus** — the **red
nucleus** is the **limb-motor premotor relay**; the **riMLF**
is the **vertical saccade generator** — **different functional
subsystems**.

**Do not** import a **coupling warning** into the riMLF —
**premotor saccade generators carry NO coupling warning** —
same rule as every non-oscillator class. **The two sides are
coordinated via the posterior commissure** (a **conduction
pathway**), **not via intrinsic coupling**.

**Do not** assume the riMLF's clinical pattern is
**contralateral** — it is **bilateral** — a **unilateral** riMLF
lesion produces **asymmetric** vertical gaze palsy (because the
**posterior commissure provides the bilateral coordination**).
**The bilateral clinical pattern is distinct from the red
nucleus's CONTRALATERAL pattern** — **distinct from the
oscillators' RHYTHM-COUPLING pattern**.

Iterating the riMLF structure container's children (recommended
consumer pattern)::

    import pkgutil
    import infrastructure.brainparts.midbrain.tegmentum.rostral_interstitial_nucleus_mlf as rimlf_pkg

    ROSTRAL_INTERSTITIAL_NUCLEUS_MLF_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(rimlf_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("left", "right")
    #
    # Each side is a functionally-defined region — the left riMLF
    # and the right riMLF — the vertical saccade generators on
    # each side.

Reaching the left riMLF (recommended consumer pattern — the LEFT
leaf)::

    # The left riMLF — the LEFT vertical saccade generator — at
    # the rostral end of the MLF, in the left midbrain tegmentum:
    #
    #   brainparts.midbrain.tegmentum.rostral_interstitial_nucleus_mlf.left
    #
    # The left riMLF and the right riMLF are BILATERALLY
    # COORDINATED via the POSTERIOR COMMISSURE (a conduction
    # pathway) — NOT via intrinsic coupling.

Reaching the right riMLF (recommended consumer pattern — the
RIGHT leaf)::

    # The right riMLF — the RIGHT vertical saccade generator — at
    # the rostral end of the MLF, in the right midbrain tegmentum:
    #
    #   brainparts.midbrain.tegmentum.rostral_interstitial_nucleus_mlf.right
    #
    # The right riMLF and the left riMLF are BILATERALLY
    # COORDINATED via the POSTERIOR COMMISSURE (a conduction
    # pathway) — NOT via intrinsic coupling.

Reaching the red nucleus (recommended consumer pattern — the
OTHER structure container)::

    # The red nucleus is the FIRST paired structure container —
    # the limb-motor premotor relay:
    #
    #   brainparts.midbrain.tegmentum.red_nucleus
    #
    # The red nucleus is the FIRST structure container (Nissl-
    # defined, paired, substantive paired leaves). The riMLF is
    # the SECOND structure container (functionally-defined,
    # paired, substantive paired leaves). Both follow the same
    # structure-container pattern.

Reaching the PPRF (recommended consumer pattern — the HORIZONTAL
premotor saccade generator, in the PONS)::

    # The PPRF is the HORIZONTAL premotor saccade generator — in
    # the PONS:
    #
    #   brainparts.hindbrain.metencephalon.pons.pprf
    #
    # The PPRF (horizontal) and the riMLF (vertical) are the TWO
    # premotor saccade generators of the brainstem — both between
    # the SC (command) and the CN nuclei (motor).

Reaching the superior colliculus (recommended consumer pattern —
the COMMAND level)::

    # The superior colliculus is the saccade COMMAND GENERATOR —
    # the TOP of the saccade hierarchy:
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #   (OR: brainparts.midbrain.tectum.corpora_quadrigemina.left.superior_colliculus)
    #
    # The SC DECIDES where to look (the command); the riMLF
    # EXECUTES (the premotor level).

Reaching the CN III/IV nuclei (recommended consumer pattern —
the MOTOR level)::

    # The CN III/IV nuclei are the MOTOR nuclei that execute the
    # vertical saccade — DOWNSTREAM of the riMLF:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #
    # The riMLF is the PREMOTOR saccade generator; the CN III/IV
    # nuclei are the MOTOR nuclei. Different levels.

Reaching the posterior commissure (recommended consumer pattern —
the CONDUCTION PATHWAY that coordinates the two sides)::

    # The posterior commissure is the CONDUCTION PATHWAY that
    # carries the riMLF fibers across the midline — the
    # coordination of the two riMLF:
    #
    #   brainparts.midbrain.posterior_commissure
    #   (OR: brainparts.forebrain.diencephalon.posterior_commissure
    #    — depending on the on-disk tree)
    #
    # The posterior commissure is a CONDUCTION PATHWAY; the riMLF
    # is a NUCLEUS. The two riMLF are BILATERALLY COORDINATED via
    # the posterior commissure — NOT via intrinsic coupling.

Reaching the MLF (recommended consumer pattern — the
LONGITUDINAL FASCICULUS that the riMLF is EMBEDDED WITHIN)::

    # The MLF is the LONGITUDINAL FASCICULUS that the riMLF is
    # EMBEDDED WITHIN — the "rostral interstitial nucleus OF the
    # MLF" — the nucleus embedded within the tract:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.medial_longitudinal_fasciculus
    #
    # The MLF is a CONDUCTION PATHWAY; the riMLF is a
    # FUNCTIONALLY-DEFINED REGION (the nucleus embedded within
    # the tract). They are DIFFERENT structures.

Reaching the interstitial nucleus of Cajal (recommended consumer
pattern — the VERTICAL GAZE HOLDING structure, NOT the vertical
saccade generator)::

    # The interstitial nucleus of Cajal is the VERTICAL GAZE
    # HOLDING structure — the neural integrator for vertical gaze
    # (the "where the eye is"):
    #
    #   brainparts.midbrain.tegmentum.interstitial_nucleus_of_cajal
    #
    # The interstitial nucleus of Cajal HOLDS the vertical gaze
    # (the integrator); the riMLF GENERATES the vertical saccades
    # (the velocity command). Complementary but different.

Reaching the pretectum (recommended consumer pattern — the
SEPARATE REGION at the DIENCEPHALON-MIDBRAIN JUNCTION)::

    # The pretectum is a SEPARATE REGION at the diencephalon-
    # midbrain junction — the pupillary and optokinetic region:
    #
    #   brainparts.midbrain.pretectum
    #
    # The pretectum is PUPILLARY AND OPTOKINETIC; the riMLF is
    # VERTICAL SACCADIC. Different regions, different functional
    # systems.

Reaching the SNr (recommended consumer pattern — the co-substrate
of PSP with the riMLF)::

    # The substantia nigra pars reticulata (SNr) is the co-substrate
    # of PSP with the riMLF — the inhibitory gate on the SC:
    #
    #   brainparts.midbrain.tegmentum.left.substantia_nigra.pars_reticulata
    #   (OR: brainparts.midbrain.tegmentum.right.substantia_nigra.pars_reticulata)
    #
    # PSP vertical gaze palsy: the riMLF (vertical saccade
    # generator — loss of vertical saccades) + the SNr (inhibitory
    # gate on the SC — loss of saccade inhibition — slow saccades,
    # saccade hypometria). Both are midbrain substrates.

The saccade hierarchy — detail (not wired — consult references)::

    # The saccade hierarchy — the riMLF is the VERTICAL premotor
    # level:
    #
    #   SUPERIOR COLLICULUS (command level) — sensorimotor
    #     integration; receives visual, auditory, somatosensory
    #     input; generates saccade commands in a motor map
    #         |
    #         v
    #   PPRF (horizontal premotor level) / riMLF (vertical premotor
    #   level) — the TWO premotor saccade generators — transform
    #   the SC's saccade command into the premotor saccade signal
    #         |
    #         v
    #   CN III / IV / VI nuclei (motor level) — motor nuclei;
    #     execute the saccade by driving the extraocular muscles
    #         |
    #         v
    #   Extraocular muscles (effector level) — the effectors
    #
    # The riMLF is the VERTICAL premotor saccade generator —
    # BETWEEN the SC (command) and the CN III/IV nuclei (motor).
    # The PPRF is the HORIZONTAL premotor saccade generator —
    # BETWEEN the SC (command) and the CN VI/III nuclei (motor).
    #
    # Do not attempt to resolve the PPRF, the SC, or the CN nuclei
    # as sub-paths of the riMLF — they are DIFFERENT structures at
    # DIFFERENT levels of the saccade hierarchy.

The posterior commissure coordination — detail (not wired —
consult references)::

    # The POSTERIOR COMMISSURE — the bilateral coordination
    # pathway:
    #
    #   LEFT riMLF (upward vertical saccade generator)
    #     -> LEFT riMLF fibers
    #     -> CROSS the midline in the POSTERIOR COMMISSURE
    #     -> RIGHT CN III/IV nuclei
    #     -> UPWARD vertical saccade
    #
    #   RIGHT riMLF (downward vertical saccade generator)
    #     -> RIGHT riMLF fibers
    #     -> CROSS the midline in the POSTERIOR COMMISSURE
    #     -> LEFT CN III/IV nuclei
    #     -> DOWNWARD vertical saccade
    #
    # THE TWO riMLF ARE BILATERALLY COORDINATED VIA THE POSTERIOR
    # COMMISSURE — a CONDUCTION PATHWAY. NOT via intrinsic
    # coupling. The posterior commissure is the CONDUCTION
    # PATHWAY; the riMLF is the NUCLEUS.
    #
    # The bilateral coordination is EXTRINSIC (via a conduction
    # pathway) — NOT INTRINSIC (via intrinsic oscillator
    # coupling). NO coupling warning — the coordination is via
    # the posterior commissure, not an intrinsic oscillator
    # coupling.
    #
    # Do not attempt to resolve the posterior commissure as a
    # sub-path of the riMLF — it is a DIFFERENT structure (a
    # conduction pathway).

Clinical-pattern detail (not wired — consult references)::

    # The riMLF is the ANATOMICAL SUBSTRATE for TWO NAMED CLINICAL
    # SYNDROMES — the first paired structure in the tegmentum to
    # carry named clinical syndromes directly:
    #
    #   PROGRESSIVE SUPRANUCLEAR  -> DIRECT — the riMLF is ONE OF
    #     PALSY (PSP) —             THE TWO primary substrates
    #     vertical gaze palsy,      (the SNr is the other) — the
    #     postural instability,     vertical saccade loss is the
    #     parkinsonism              riMLF contribution; the loss of
    #                               saccade inhibition is the SNr
    #                               contribution. The "supranuclear"
    #                               in PSP = "above the CN nuclei"
    #                               = in the premotor saccade
    #                               generators (riMLF, PPRF) and the
    #                               basal ganglia inhibitory gate
    #                               (SNr).
    #   PARINAUD SYNDROME        -> DIRECT — the riMLF's FIBERS are
    #     (dorsal midbrain           interrupted in the posterior
    #      syndrome) — upgaze        commissure (the lesion site).
    #      palsy, convergence-       The riMLF nucleus itself may be
    #      retraction nystagmus,     spared — the FIBERS are
    #      light-near dissociation,  interrupted. The riMLF is the
    #      Collier sign              ANATOMICAL SUBSTRATE; the
    #                               posterior commissure is the
    #                               LESION SITE (the fibers).
    #   UNILATERAL riMLF LESION  -> INDIRECT — asymmetric vertical
    #                               gaze palsy (the posterior
    #                               commissure provides the bilateral
    #                               coordination; a unilateral
    #                               lesion produces incomplete
    #                               asymmetric vertical gaze palsy).
    #
    # No named "riMLF syndrome" per se — PSP and Parinaud syndrome
    # are the named syndromes. The riMLF is a substrate for both.
    #
    # Do not conflate these patterns — they localize to the riMLF
    # plus its co-substrates (the SNr for PSP; the posterior
    # commissure for Parinaud syndrome) — not to the riMLF alone.

References
----------
*   **Canonical riMLF anatomy:** Büttner-Ennever, J.A., Büttner,
    U. (1988). "The reticular formation." In *Neuroanatomy of the
    Oculomotor System* (Büttner-Ennever, ed.). (The riMLF — its
    location at the rostral end of the MLF, at the diencephalon-
    midbrain junction; its function as the vertical saccade
    generator; its coordination via the posterior commissure.)
*   **riMLF — vertical saccade generation:** Büttner-Ennever, J.A.,
    Büttner, U., Cohen, B., Baumgartner, G. (1982). "Vertical
    gaze paralysis in the monkey after discrete unilateral
    lesions of the mesencephalic reticular formation." *Brain*
    105:549–570. (The riMLF as the vertical saccade generator —
    the vertical gaze paralysis after riMLF lesions.)
*   **riMLF — saccade generation review:** Moschovakis, A.K.,
    Scudder, C.A., Highstein, S.M. (1996). "The microscopic
    anatomy and physiology of the primate interstitial nucleus of
    Cajal I. Efferent projections." *Journal of Neurophysiology*
    75:725–739. (The riMLF and the interstitial nucleus of Cajal
    — the vertical saccade generator and the vertical gaze
    holder — complementary functions.)
*   **PPRF — the horizontal saccade generator (contrast):** Cohen,
    B., Komatsuzaki, A. (1972). "Eye movements induced by
    stimulation of the pontine reticular formation: evidence for
    integration in oculomotor pathways." *Experimental Neurology*
    36:101–117. (The PPRF as the horizontal saccade generator —
    the counterpart of the riMLF.)
*   **Posterior commissure:** Carpenter, M.B., Sutin, J. (1983).
    *Human Neuroanatomy*, 8th ed. (The posterior commissure — the
    conduction pathway at the diencephalon-midbrain junction —
    carrying the riMLF fibers across the midline.)
*   **PSP — riMLF and SNr involvement:** Steele, J.C., Richardson,
    J.C., Olszewski, J. (1964). "Progressive supranuclear palsy."
    *Archives of Neurology* 10:333–359. (PSP — the riMLF and the
    SNr as the two primary substrates for the vertical gaze
    palsy and the loss of saccade inhibition.)
*   **PSP — vertical gaze palsy review:** Bhidayasiri, R., Plant,
    G.T., Leigh, R.J. (2001). "Progressive supranuclear palsy:
    clinical, genetic and pathological aspects." *Journal of the
    Neurological Sciences* 186:1–11. (The PSP vertical gaze palsy
    — the riMLF contribution.)
*   **Parinaud syndrome — posterior commissure lesion:** Parinaud,
    H. (1883). "Paralysie des mouvements associés des yeux."
    *Annales d'Oculistique* 90:1–21. (Parinaud syndrome — the
    dorsal midbrain syndrome — the upgaze palsy caused by the
    posterior commissure lesion interrupting the riMLF fibers.)
*   **Parinaud syndrome — modern review:** Baloh, R.W., Furman,
    J.M., Halmagyi, G.M. (2010). "Parinaud syndrome." In
    *Oxford Textbook of Vertigo and Imbalance*. (The Parinaud
    syndrome — the posterior commissure lesion as the anatomical
    substrate.)
*   **Interstitial nucleus of Cajal — the vertical gaze holder
    (contrast):** Fukushima, K., Kaneko, C.R., Fuchs, A.F. (1992).
    "The neuronal substrate of integration in the oculomotor
    system." *Progress in Neurobiology* 39:609–639. (The
    interstitial nucleus of Cajal — the neural integrator for
    vertical gaze — the complementary function to the riMLF.)
*   **Saccade hierarchy:** Leigh, R.J., Zee, D.S. (2015). *The
    Neurology of Eye Movements*, 6th ed. (The saccade hierarchy —
    the SC (command) → the PPRF / riMLF (premotor) → the CN
    nuclei (motor) → the extraocular muscles (effector).)
*   **MLF — the longitudinal fasciculus (contrast):** Frohman,
    T.C., Galetta, S.L., Fox, R.J., Solomon, D., Straumann, D.,
    Filippi, M., Zee, D.S., Frohman, E.M. (2008). "Pearls &
    Oy-sters: The medial longitudinal fasciculus in ocular motor
    physiology." *Neurology* 70:e57–e67. (The MLF — the
    longitudinal fasciculus that the riMLF is embedded within.)
*   **Superior colliculus (contrast — the command level):**
    Sparks, D.L. (2002). "The brainstem control of saccadic eye
    movements." *Nature Reviews Neuroscience* 3:952–964. (The
    superior colliculus — the saccade command generator — the
    top of the saccade hierarchy, upstream of the riMLF.)
*   **Red nucleus (contrast — the first structure container):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (The red nucleus — the first paired
    structure container — the limb-motor premotor relay — a
    different functional subsystem from the riMLF.)
*   **SLEA (contrast — the riMLF is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the riMLF.)
*   NeuroNames — Rostral interstitial nucleus of the medial
    longitudinal fasciculus; FMA — Rostral interstitial nucleus
    of the MLF. **The riMLF is a paired functionally-defined
    region — the vertical saccade generator.**
"""