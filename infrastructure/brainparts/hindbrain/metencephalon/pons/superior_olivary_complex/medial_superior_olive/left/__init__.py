"""
infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.medial_superior_olive.left
=========================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── superior_olivary_complex
                └── medial_superior_olive
                    └── left   <-- THIS MODULE

**Primary synonym:** Left medial superior olive; left MSO; left medial
superior olivary nucleus; "the left interaural time difference (ITD)
coincidence detector."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nucleus** — an **anatomically delimited
grey-matter nucleus** in the **left medial superior olivary complex**,
the **principal substrate** of **interaural time difference (ITD)
processing** for **low-frequency horizontal sound localization**. In
**humans**, the **MSO** is the **dominant binaural sound-localization
nucleus** — the **left MSO** is a **component** of this dominant human
binaural system.
**Part of:** The **medial_superior_olive** container — specifically, the
**left half** of the **bilateral MSO**. The **medial_superior_olive**
container is the **ITD processor** of the **superior olivary complex**;
the **left** sub-container is its **left-side structural child**.
**Structural parent:** ``.../medial_superior_olive/`` → **direct child**
of the medial_superior_olive container.
**Structural children:** **None.** This is a **leaf** module. The
**principal coincidence-detector neurons** (excitatory bipolar neurons
receiving bilateral cochlear nuclei input) and the **local circuit
interneurons** are documented as **prose**, not as structural children.
**Boundary status (LEAF — NOT a container):** **Boundary case — the left
medial superior olive is a LEAF, not a container.** It has **no
structural children**. The **principal coincidence-detector neurons**
and the **local circuit interneurons** are **prose** populations, not
structural children. Consumers must **not** treat the left medial
superior olive as a container, and must **not** assume the neuron
populations exist as sub-modules.
**Boundary status (LEFT HALF — NOT the whole medial_superior_olive
container):** **Boundary case — the left medial superior olive is the
LEFT HALF of the medial_superior_olive container, NOT the whole
container.** The **medial_superior_olive** container
(``.../medial_superior_olive/``) has **two structural children** —
``left`` and ``right``. The **left** sub-container (here) is the
**left-side** half only. Consumers must **not** conflate the left MSO
with the **whole MSO** — the right side is a **separate structural
sibling**.
**Boundary status (NOT the right medial superior olive — strict mirror,
no warning):** **Boundary case — the left medial superior olive is NOT
the right medial superior olive; the two are a STRICT MIRROR PAIR with
NO warning at the sub-container level.** The **right medial superior
olive** (``.../medial_superior_olive/right/``) is the **structurally
identical** right-side counterpart — same neuron populations, same
functional system (ITD processing via coincidence detection), same
bilateral framing. The two sides are **strictly mirrored** — any
lateralization is documented **here, in the Lateralization Notes**, not
imported from elsewhere. Consumers must **not** import a lateralization
warning into the left MSO — there is **none at the sub-container level**
beyond the **bilateral excitatory input arrangement** documented below.
**Boundary status (ITD PROCESSOR — NOT the ILD processor):** **Boundary
case — the left medial superior olive is the ITD PROCESSOR, NOT the ILD
processor.** The **left MSO** processes **interaural time differences**
(ITD) for **low-frequency horizontal sound localization** (< ~1.5 kHz
in humans). The **left lateral superior olive (LSO)**
(``.../superior_olivary_complex/lateral_superior_olive/left/``) is the
**ILD processor** for **high-frequency horizontal sound localization**
(> ~1.5 kHz in humans). They are **DIFFERENT STRUCTURES** — different
binaural cues (ITD vs. ILD), different frequency ranges (low vs. high),
different neural mechanisms (coincidence detection for ITD vs.
excitation-inhibition for ILD). **This distinction is functionally
load-bearing** — the two binaural cues dominate at different frequency
ranges, and the **human left MSO is a component of the dominant
binaural sound-localization system**. Consumers must **not** conflate
the left MSO with the left LSO.
**Boundary status (EXCITATORY COINCIDENCE DETECTOR — NOT an inhibitory
relay):** **Boundary case — the left medial superior olive is an
EXCITATORY COINCIDENCE DETECTOR, NOT an inhibitory relay.** The **left
MSO** principal neurons are **excitatory (glutamatergic)** — they
**receive bilateral excitatory** input from the **left cochlear nuclei**
(ipsilateral) and the **right cochlear nuclei** (contralateral, via the
**right trapezoid body**) and **fire maximally** when the two inputs
arrive **simultaneously** (the **Jeffress coincidence-detection
model**). This is the **opposite** of the **glycinergic inhibitory
relay** of the **left MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/``),
which **converts** the **excitatory right cochlear nuclei** input into
an **inhibitory** input to the **left LSO**. **This distinction is
functionally load-bearing** — the **left MSO** is the **neural
substrate** of **left ITD processing** (via **excitatory coincidence
detection**), whereas the **left MNTB** is the **neural substrate** of
**contralateral inhibition** for **ILD processing**. Consumers must
**not** conflate the left MSO with an **inhibitory relay** — it is the
**excitatory coincidence-detector relay** of the left superior olivary
complex.
**Boundary status (NOT the left MNTB — that is the INHIBITORY RELAY for
ILD processing):** **Boundary case — the left medial superior olive is
NOT the left medial nucleus of the trapezoid body (MNTB).** The **left
MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/``)
is the **glycinergic inhibitory relay** that **receives** the **right
cochlear nuclei** input (via the **calyx of Held** in the **right
trapezoid body**) and **projects** an **inhibitory (glycinergic)**
input to the **left LSO** — it is the **inhibitory relay** for **left
ILD processing**. The **left MSO** (here) is the **excitatory
coincidence detector** for **left ITD processing** — it **receives
bilateral excitatory** input and **performs** the **ITD computation**
directly. They are **DIFFERENT STRUCTURES** — different binaural cues
(ITD vs. ILD), different neural mechanisms (coincidence detection vs.
inhibitory relay). Consumers must **not** conflate the left MSO with
the left MNTB.
**Boundary status (BILATERAL EXCITATORY INPUT — NOT a single-ear
relay):** **Boundary case — the left medial superior olive is a
BILATERAL EXCITATORY COMPARATOR — it receives EXCITATORY input from
BOTH the LEFT cochlear nuclei (ipsilateral) and the RIGHT cochlear
nuclei (contralateral).** The **left MSO** is the **first brainstem
site** where the **left-ear** and **right-ear** signals **converge on
the same neuron** — it is the **neural substrate** of the **ITD
computation** via **coincidence detection**. **The left MSO neuron**
**fires maximally** when the **left-ear** and **right-ear** inputs
arrive **simultaneously** — it encodes the **ITD** for **sound sources
on the left side** and the **midline** (depending on the ITD). **This
bilateral excitatory arrangement** is a **structural fact** of the
**left MSO** — it is **not** a lateralization warning. Consumers must
**not** treat the left MSO as a **single-ear relay** — it is a
**bilateral excitatory comparator** with **distinct ipsilateral and
contralateral inputs**.
**Boundary status (NOT the left cochlear nuclei — those are the UPSTREAM
MONAURAL FIRST-ORDER RELAY):** **Boundary case — the left medial
superior olive is NOT the left cochlear nuclei.** The **left cochlear
nuclei**
(``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``)
are the **monaural first-order relay** that **receive** the **monaural**
auditory input from the **left cochlea**. The **left cochlear nuclei**
(specifically the **spherical bushy cells** in the **left AVCN**)
**project** to the **left MSO** via the **left trapezoid body**
(ipsilaterally and contralaterally). The **left MSO** (here) is the
**binaural second-order relay** that **receives bilateral excitatory**
cochlear nuclei input and **performs** the **ITD computation**. They
are **DIFFERENT STRUCTURES** — the **cochlear nuclei** are **monaural
first-order**; the **left MSO** is **binaural second-order**. **This
distinction is clinically load-bearing** — a **left cochlear nuclei
lesion** causes **left sensorineural hearing loss**; a **left MSO
lesion** causes **impaired ITD-based sound localization** (impaired
**low-frequency horizontal sound localization**) with **preserved
pure-tone thresholds**. Consumers must **not** conflate the left MSO
with the left cochlear nuclei.
**Boundary status (NOT the right cochlear nuclei — those are the
CONTRALATERAL UPSTREAM SOURCE):** **Boundary case — the left medial
superior olive is NOT the right cochlear nuclei.** The **right cochlear
nuclei**
(``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/``)
are the **monaural first-order relay** that **receive** the **monaural**
auditory input from the **right cochlea**. The **right cochlear
nuclei** (specifically the **spherical bushy cells** in the **right
AVCN**) **project** to the **left MSO** via the **right trapezoid
body** (contralaterally). The **left MSO** (here) is the **binaural
second-order relay** that **receives bilateral excitatory** cochlear
nuclei input and **performs** the **ITD computation**. Consumers must
**not** conflate the left MSO with the right cochlear nuclei.
**Boundary status (NOT the trapezoid body — that is the WHITE-MATTER
AFFERENT TRACT):** **Boundary case — the left medial superior olive is
NOT the trapezoid body.** The **trapezoid body** is the **white-matter
decussating tract** that **carries** the **bilateral auditory axons**
from the **cochlear nuclei** to the **superior olivary complex** —
including the **bilateral cochlear nuclei** projections to the **left
MSO** (the **left** and **right** excitatory inputs). The **left MSO**
(here) is the **grey-matter neuron cluster** that **receives** the
trapezoid-body axons. They are **DIFFERENT STRUCTURES** — the **left
MSO** is grey matter; the **trapezoid body** is white matter.
Consumers must **not** conflate the left MSO with the trapezoid body.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
EFFERENT TRACT):** **Boundary case — the left medial superior olive is
NOT the lateral lemniscus.** The **lateral lemniscus** is the
**white-matter ascending tract** that **carries** the **efferent axons**
from the **superior olivary complex** (including the **left MSO**) to
the **inferior colliculus** (primarily the **left inferior colliculus**,
with **contralateral** projections to the **right inferior colliculus**).
The **left MSO** (here) is the **grey-matter neuron cluster** that
**gives rise to** the lateral lemniscus axons. They are **DIFFERENT
STRUCTURES** — the **left MSO** is grey matter; the **lateral
lemniscus** is white matter. Consumers must **not** conflate the left
MSO with the lateral lemniscus.
**Boundary status (NOT the left inferior colliculus — that is the
MIDBRAIN DOWNSTREAM AUDITORY RELAY):** **Boundary case — the left
medial superior olive is NOT the left inferior colliculus.** The **left
inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
is the **midbrain auditory relay** that **receives** the **ascending
auditory projections** from the **superior olivary complex** (including
the **left MSO**) and **projects** to the **left medial geniculate
body**. The **left MSO** (here) is the **pontine ITD processor** — it
is **upstream** of the left inferior colliculus. They are **DIFFERENT
STRUCTURES** — the **left MSO** is **pontine** and **upstream**; the
**left inferior colliculus** is **midbrain** and **downstream**.
Consumers must **not** conflate the left MSO with the left inferior
colliculus.
**Boundary status (NOT the left medial geniculate body — that is the
THALAMIC DOWNSTREAM AUDITORY RELAY):** **Boundary case — the left
medial superior olive is NOT the left medial geniculate body.** The
**left medial geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
is the **thalamic auditory relay** that **receives** the **ascending
auditory projections** from the **left inferior colliculus** and
**projects** to the **left primary auditory cortex**. The **left MSO**
(here) is the **pontine ITD processor** — it is **upstream** of the
left medial geniculate body. They are **DIFFERENT STRUCTURES** — the
**left MSO** is **pontine** and **upstream**; the **left medial
geniculate body** is **diencephalic** and **downstream**. Consumers
must **not** conflate the left MSO with the left medial geniculate
body.
**Boundary status (NOT the left primary auditory cortex — that is the
CORTICAL DOWNSTREAM AUDITORY TARGET):** **Boundary case — the left
medial superior olive is NOT the left primary auditory cortex.** The
**left primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
is the **cortical target** of the **ascending auditory pathway**. The
**left MSO** (here) is the **pontine ITD processor** — it is
**upstream** of the left primary auditory cortex. They are **DIFFERENT
STRUCTURES** — the **left MSO** is **pontine** and **upstream**; the
**left primary auditory cortex** is **cortical** and **downstream**.
Consumers must **not** conflate the left MSO with the left primary
auditory cortex.
**Boundary status (NOT the left facial nerve nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the left medial
superior olive is NOT the left facial nerve nucleus.** The **left facial
nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) is the
**branchial motor** nucleus for the **left muscles of facial
expression**. The **left MSO** (here) is the **excitatory ITD
coincidence detector**. They are **DIFFERENT STRUCTURES** — different
functional systems (branchial motor vs. binaural ITD processing). They
are **anatomically adjacent** (both are in the **left ventral pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the left MSO with the left facial nerve
nucleus.
**Boundary status (NOT the left abducens nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the left medial
superior olive is NOT the left abducens nucleus.** The **left abducens
nucleus** (``.../cranial_nerve_nuclei/left/abducens_nucleus/``) is the
**somatic motor** nucleus for the **left lateral rectus**. The **left
MSO** (here) is the **excitatory ITD coincidence detector**. They are
**DIFFERENT STRUCTURES** — different functional systems (somatic motor
vs. binaural ITD processing). They are **anatomically adjacent** — the
**left MSO** is **near the genu of the left facial nerve** and the
**left abducens nucleus**; this proximity is a **classic source of
confusion** — consumers must **not** conflate the left MSO with the
left abducens nucleus.
**Boundary status (NOT the left cochlear nerve or the left
vestibulocochlear nerve — those are the PERIPHERAL AUDITORY CONDUCTION
INFRASTRUCTURE):** **Boundary case — the left medial superior olive is
NOT the left cochlear nerve or the left vestibulocochlear nerve.** The
**left cochlear nerve** (the cochlear division of left CN VIII) and the
**left vestibulocochlear nerve** (left CN VIII) are the **white-matter
peripheral nerves** that **carry** the **primary auditory axons** from
the **left spiral ganglion** to the **left cochlear nuclei**. The **left
MSO** (here) is the **central grey-matter binaural ITD processor**.
They are **DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **left MSO** is **central grey matter**. Consumers
must **not** conflate the left MSO with the left cochlear or left
vestibulocochlear nerve.
**Boundary status (NOT the whole medial_superior_olive container — that
is the PARENT):** **Boundary case — the left medial superior olive is
NOT the whole medial_superior_olive container; the
medial_superior_olive container is the PARENT.** The
**medial_superior_olive** container (``.../medial_superior_olive/``) is
the **bilateral ITD processor** — it **contains** the **left MSO**
(here) and the **right MSO**. The **left MSO** is the **left half** of
the medial_superior_olive container. Consumers must **not** conflate
the left MSO with the **whole MSO**.
**Boundary status (NOT the whole superior_olivary_complex container —
that is the GRANDPARENT):** **Boundary case — the left medial superior
olive is NOT the whole superior_olivary_complex container; the
superior_olivary_complex container is the GRANDPARENT.** The
**superior_olivary_complex** container
(``.../superior_olivary_complex/``) is the **pontine binaural
sound-localization relay** — it **contains** the **LSO**, the **MSO**,
and the **MNTB**. The **left MSO** is **one of the sub-nuclei** of the
superior olivary complex. Consumers must **not** conflate the left MSO
with the **whole superior olivary complex**.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
functionally distinct populations):** **Boundary case — the left medial
superior olive is NOT a single uniform neuron population; it contains
MULTIPLE functionally distinct populations.** The **principal
coincidence-detector neurons** — the **excitatory (glutamatergic)**
bipolar neurons that **receive bilateral excitatory** input from the
**left cochlear nuclei** (ipsilateral) and the **right cochlear nuclei**
(contralateral, via the **right trapezoid body**) and **fire
maximally** when the two inputs arrive **simultaneously** (the
**Jeffress coincidence-detection model**) — they are the **ITD
computation** output of the **left MSO**. The **local circuit
interneurons** — the **local neurons** that **modulate** the
**principal neurons**. **These populations are prose, not structural
children.** Consumers must **not** treat the left MSO as a single
uniform population — it is a **functionally heterogeneous nucleus**
with **distinct** sub-circuits.
**Boundary status (SLEA-FREE — the left medial superior olive is NOT an
extended-amygdala component):** **Boundary case — the left medial
superior olive is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala) and
to the **BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **left MSO** is a **binaural auditory ITD coincidence
detector** — it is **NOT** an extended-amygdala component, and it
carries **NO SLEA warning**. Consumers must **not** import the SLEA
warning into the left MSO — it is **SLEA-free**.

Overview
--------
The left medial superior olive is the **left half** of the **bilateral
MSO** — the **left grey-matter neuron cluster** in the **left superior
olivary complex** that is the **excitatory coincidence detector** for
**interaural time difference (ITD) processing** for **low-frequency
horizontal sound localization**. It is a **leaf** module under the
``left`` sub-container of the medial_superior_olive container, and it is
the **left ITD processor** — the **left MSO** that **fires maximally**
when the **left-ear** and **right-ear** signals arrive
**simultaneously** (the **Jeffress coincidence-detection model**).

**The left medial superior olive is a LEAF, not a container.** It has
**no structural children**. The **principal coincidence-detector
neurons** and the **local circuit interneurons** are **prose
populations**, not structural children.

**The left medial superior olive is the LEFT HALF of the
medial_superior_olive container, NOT the whole container.** The
**medial_superior_olive** container has **two structural children** —
``left`` and ``right``. The **left** sub-container (here) is the
**left-side** half only.

**The left medial superior olive and the right medial superior olive are
a STRICT MIRROR PAIR with NO warning at the sub-container level.** The
two sides are **structurally identical** — same neuron populations, same
functional system (ITD processing via coincidence detection), same
bilateral framing.

**The left medial superior olive is the ITD PROCESSOR, not the ILD
processor.** The **left MSO** processes **interaural time differences**
for **low-frequency horizontal sound localization**. The **left LSO**
processes **interaural level differences** for **high-frequency
horizontal sound localization**.

**The left medial superior olive is a BILATERAL EXCITATORY
COMPARATOR.** It receives **excitatory** input from **both** the **left
cochlear nuclei** (ipsilateral) and the **right cochlear nuclei**
(contralateral, via the **right trapezoid body**). The **left MSO
neuron** **fires maximally** when the **left-ear** and **right-ear**
inputs arrive **simultaneously** — it encodes the **ITD** for
**sound sources on the left side** and the **midline** (depending on
the ITD).

**The left medial superior olive is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The left medial superior olive contains **multiple functionally
distinct neuron populations** — documented as **prose**, not as
structural children:

*   **Principal coincidence-detector neurons** — the **excitatory
    (glutamatergic)** bipolar neurons that **receive bilateral
    excitatory** input from the **left cochlear nuclei** (ipsilateral,
    via the **left trapezoid body**) and the **right cochlear nuclei**
    (contralateral, via the **right trapezoid body**) and **fire
    maximally** when the two inputs arrive **simultaneously** (the
    **Jeffress coincidence-detection model**). They **project** to the
    **left inferior colliculus** (primarily, via the **lateral
    lemniscus**) and to the **right inferior colliculus**
    (contralaterally, to a lesser extent). They are the **ITD
    computation** output of the **left MSO** — they **encode** the
    **ITD** for **sound sources on the left side** and the **midline**
    (depending on the ITD).

*   **Local circuit interneurons** — the **local neurons** that
    **modulate** the **principal coincidence-detector neurons** within
    the left MSO. They are **prose** populations, not structural
    children.

**These populations are prose, not structural children.** The tree wires
the **left medial superior olive** as a **single leaf** under the
``left`` sub-container of the medial_superior_olive container — the
**principal coincidence-detector neurons** and the **local circuit
interneurons** are **prose**, not structural children. Consumers that
need **neuron-population-level** resolution should consult the
references, not the tree.

The Left MSO / Right MSO Boundary
---------------------------------
This is the **strict-mirror** boundary:

*   **Left medial superior olive** (this module) — the **left-side** MSO
    — the **left ITD coincidence detector**.

*   **Right medial superior olive**
    (``.../medial_superior_olive/right/``) — the **structurally
    identical** right-side MSO — the **right ITD coincidence detector**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same neuron
populations, same functional system (ITD processing via coincidence
detection), same bilateral framing. Any lateralization is documented
**here, in the Lateralization Notes**, not imported from elsewhere.
Consumers must **not** import a lateralization warning into the left MSO
— there is **none at the sub-container level** beyond the **bilateral
excitatory input arrangement** documented below.

The Left MSO / Medial Superior Olive Container Boundary
-------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Left medial superior olive** (this module) — the **left-side** half
    of the bilateral MSO.

*   **Medial superior olive container** (``.../medial_superior_olive/``)
    — the **whole bilateral MSO**, with **two structural children**
    (``left`` and ``right``).

**The left medial superior olive is a child of the
medial_superior_olive container.** Consumers must **not** conflate the
left half with the **whole MSO** — the right side is a **separate
structural sibling**.

The Left MSO / Left LSO Boundary
--------------------------------
This is the **sibling** boundary — **ITD processor vs. ILD processor**:

*   **Left medial superior olive** (this module) — the **left ITD
    processor** for **low-frequency horizontal sound localization**.

*   **Left lateral superior olive (LSO)**
    (``.../superior_olivary_complex/lateral_superior_olive/left/``) —
    the **left ILD processor** for **high-frequency horizontal sound
    localization**.

**They are DIFFERENT STRUCTURES** — different binaural cues (ITD vs.
ILD), different frequency ranges (low vs. high), different neural
mechanisms (coincidence detection for ITD vs. excitation-inhibition for
ILD). Consumers must **not** conflate the left MSO with the left LSO.

The Left MSO / Left MNTB Boundary
---------------------------------
This is the **sibling** boundary — **excitatory coincidence detector vs.
inhibitory relay**:

*   **Left medial superior olive** (this module) — the **excitatory ITD
    coincidence detector**.

*   **Left medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/``)
    — the **glycinergic inhibitory relay** for **ILD processing** — it
    **receives** the **right cochlear nuclei** input and **projects** an
    **inhibitory input** to the **left LSO**.

**They are DIFFERENT STRUCTURES** — different functional roles
(excitatory coincidence detector vs. inhibitory relay), different
binaural cues (ITD vs. ILD). Consumers must **not** conflate the left
MSO with the left MNTB.

The Left MSO / Left Cochlear Nuclei Boundary
--------------------------------------------
This is the **binaural second-order vs. monaural first-order** boundary:

*   **Left medial superior olive** (this module) — the **left binaural
    second-order relay** that **receives bilateral excitatory** cochlear
    nuclei input and **performs** the **ITD computation**.

*   **Left cochlear nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``)
    — the **left monaural first-order relay** that **receives** the
    **monaural** auditory input from the **left cochlea** — the **left
    cochlear nuclei** (specifically the **left spherical bushy cells** in
    the **left AVCN**) **project** to the **left MSO** via the **left
    trapezoid body** (ipsilaterally).

**They are DIFFERENT STRUCTURES** — the **left cochlear nuclei** are
**monaural first-order**; the **left MSO** is **binaural second-order**.
**This distinction is clinically load-bearing** — a **left cochlear
nuclei lesion** causes **left sensorineural hearing loss**; a **left MSO
lesion** causes **impaired left ITD-based sound localization** with
**preserved pure-tone thresholds**. Consumers must **not** conflate the
left MSO with the left cochlear nuclei.

The Left MSO / Right Cochlear Nuclei Boundary
---------------------------------------------
This is the **binaural second-order vs. monaural first-order
(contralateral)** boundary:

*   **Left medial superior olive** (this module) — the **left binaural
    second-order relay** that **receives** the **contralateral right
    cochlear nuclei** input and **performs** the **ITD computation**.

*   **Right cochlear nuclei**
    (``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/``)
    — the **right monaural first-order relay** that **receives** the
    **monaural** auditory input from the **right cochlea** — the **right
    cochlear nuclei** (specifically the **right spherical bushy cells**
    in the **right AVCN**) **project** to the **left MSO** via the
    **right trapezoid body** (contralaterally).

**They are DIFFERENT STRUCTURES** — the **right cochlear nuclei** are
**monaural first-order**; the **left MSO** is **binaural second-order**.
Consumers must **not** conflate the left MSO with the right cochlear
nuclei.

The Left MSO / Trapezoid Body Boundary
--------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Left medial superior olive** (this module) — the **grey-matter
    neuron cluster** that **receives** the trapezoid-body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the **bilateral auditory axons** from the **cochlear
    nuclei** to the **superior olivary complex** (including the
    **bilateral cochlear nuclei** projections to the **left MSO**).

**They are DIFFERENT STRUCTURES** — the **left MSO** is grey matter; the
**trapezoid body** is white matter. Consumers must **not** conflate the
left MSO with the trapezoid body.

The Left MSO / Lateral Lemniscus Boundary
-----------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Left medial superior olive** (this module) — the **grey-matter
    neuron cluster** that **gives rise to** the lateral lemniscus axons.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the **efferent axons** from the **superior olivary
    complex** (including the **left MSO**) to the **inferior
    colliculus**.

**They are DIFFERENT STRUCTURES** — the **left MSO** is grey matter; the
**lateral lemniscus** is white matter. Consumers must **not** conflate
the left MSO with the lateral lemniscus.

The Left MSO / Left Inferior Colliculus Boundary
------------------------------------------------
This is the **pontine ITD processor vs. midbrain downstream relay**
boundary:

*   **Left medial superior olive** (this module) — the **left pontine
    ITD processor**.

*   **Left inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
    — the **left midbrain auditory relay** that **receives** the
    **ascending auditory projections** from the **superior olivary
    complex** (including the **left MSO**) and **projects** to the
    **left medial geniculate body**.

**They are DIFFERENT STRUCTURES** — the **left MSO** is **pontine** and
**upstream**; the **left inferior colliculus** is **midbrain** and
**downstream**. Consumers must **not** conflate the left MSO with the
left inferior colliculus.

The Left MSO / Left Medial Geniculate Body Boundary
---------------------------------------------------
This is the **pontine ITD processor vs. thalamic downstream relay**
boundary:

*   **Left medial superior olive** (this module) — the **left pontine
    ITD processor**.

*   **Left medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
    — the **left thalamic auditory relay** that **receives** the
    **ascending auditory projections** from the **left inferior
    colliculus** and **projects** to the **left primary auditory
    cortex**.

**They are DIFFERENT STRUCTURES** — the **left MSO** is **pontine** and
**upstream**; the **left medial geniculate body** is **diencephalic** and
**downstream**. Consumers must **not** conflate the left MSO with the
left medial geniculate body.

The Left MSO / Left Primary Auditory Cortex Boundary
----------------------------------------------------
This is the **pontine ITD processor vs. cortical downstream target**
boundary:

*   **Left medial superior olive** (this module) — the **left pontine
    ITD processor**.

*   **Left primary auditory cortex** (Heschl's gyrus, Brodmann areas 41
    and 42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
    — the **left cortical target** of the **ascending auditory
    pathway**.

**They are DIFFERENT STRUCTURES** — the **left MSO** is **pontine** and
**upstream**; the **left primary auditory cortex** is **cortical** and
**downstream**. Consumers must **not** conflate the left MSO with the
left primary auditory cortex.

The Left MSO / Left Facial Nerve Nucleus Boundary
-------------------------------------------------
This is the **auditory binaural relay vs. branchial motor** boundary:

*   **Left medial superior olive** (this module) — the **left excitatory
    ITD coincidence detector**.

*   **Left facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) — the
    **branchial motor** nucleus for the **left muscles of facial
    expression**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. branchial motor). They are
**anatomically adjacent** — consumers must **not** conflate the left MSO
with the left facial nerve nucleus.

The Left MSO / Left Abducens Nucleus Boundary
---------------------------------------------
This is the **auditory binaural relay vs. somatic motor** boundary:

*   **Left medial superior olive** (this module) — the **left excitatory
    ITD coincidence detector**.

*   **Left abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/``) — the
    **somatic motor** nucleus for the **left lateral rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. somatic motor). They are
**anatomically adjacent** — consumers must **not** conflate the left MSO
with the left abducens nucleus.

The Left MSO / Left Cochlear and Vestibulocochlear Nerves Boundary
------------------------------------------------------------------
This is the **central grey matter vs. peripheral white matter** boundary:

*   **Left medial superior olive** (this module) — the **central
    grey-matter binaural ITD processor**.

*   **Left cochlear nerve** (the cochlear division of left CN VIII) and
    **left vestibulocochlear nerve** (left CN VIII) — the **peripheral
    white-matter nerves** that **carry** the **primary auditory axons**
    from the **left spiral ganglion** to the **left cochlear nuclei**.

**They are DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **left MSO** is **central grey matter**. Consumers
must **not** conflate the left MSO with the left cochlear or left
vestibulocochlear nerve.

The Left MSO / Whole Medial Superior Olive Container Boundary
-------------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Left medial superior olive** (this module) — the **left-side** half
    of the medial_superior_olive container.

*   **Medial superior olive container** (``.../medial_superior_olive/``)
    — the **whole bilateral MSO**, with **two structural children**
    (``left`` and ``right``).

**The left medial superior olive is a child of the
medial_superior_olive container.** Consumers must **not** conflate the
left MSO with the **whole MSO**.

The Left MSO / Whole Superior Olivary Complex Container Boundary
---------------------------------------------------------------
This is the **sub-nucleus vs. grandparent** boundary:

*   **Left medial superior olive** (this module) — the **left MSO** — one
    of the sub-nuclei of the superior olivary complex.

*   **Superior olivary complex container**
    (``.../superior_olivary_complex/``) — the **pontine binaural
    sound-localization relay** that **contains** the **LSO**, the
    **MSO**, and the **MNTB**.

**The left MSO is a great-grandchild of the superior olivary complex**
(via the medial_superior_olive container). Consumers must **not**
conflate the left MSO with the **whole superior olivary complex**.

The Left MSO / SLEA Boundary
----------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Left medial superior olive** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The left medial superior olive is NOT part of the SLEA continuum.** It
is a **binaural auditory ITD processor**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the left
MSO.

Function in the Human Brain
---------------------------
The left medial superior olive's functions are **interaural time
difference (ITD) processing** for **low-frequency horizontal sound
localization** — **NOT a single unified function**:

*   **ITD Computation (Excitatory Coincidence Detection):** The **left
    MSO** is the **excitatory coincidence detector** for **left ITD
    processing**. It **receives bilateral excitatory** input from the
    **left cochlear nuclei** (ipsilateral) and the **right cochlear
    nuclei** (contralateral, via the **right trapezoid body**) and
    **fires maximally** when the two inputs arrive **simultaneously**
    (the **Jeffress coincidence-detection model**). **The left MSO
    neuron** is a **coincidence detector** — it **encodes** the **ITD**
    (the **difference in arrival time** of a sound at the two ears) in
    its **firing rate** for **sound sources on the left side** and the
    **midline** (depending on the ITD). **ITD** is the **dominant cue**
    for **horizontal sound localization** of **low-frequency sounds**
    (< ~1.5 kHz in humans).

*   **Low-Frequency Left-Sided Horizontal Sound Localization:** The
    **left MSO** is the **dominant binaural cue** for **low-frequency
    sound localization** (< ~1.5 kHz in humans) of **sound sources on
    the left side** and the **midline** — because **low-frequency
    sounds** have **long wavelengths** that **diffract around the
    head**, so the **sound level** at the two ears is **nearly the
    same**, and the **time of arrival** is the **dominant binaural
    cue**. The **left MSO** **computes** the **interaural time
    difference** and **encodes** the **horizontal sound-source
    location** in its **firing rate**.

*   **Human MSO Dominance:** In **humans**, the **MSO** is the
    **dominant binaural sound-localization nucleus** — it is **larger**
    than the LSO, and it **dominates ITD-based localization** for
    **low-frequency sounds** (the **LSO** is **smaller** in humans than
    in many other mammals, and its **ILD-based function** is
    **secondary** to the **MSO's ITD-based function**). The **human
    left MSO** is a **component** of the **primary neural substrate** of
    **low-frequency horizontal sound localization**.

*   **NOT a neural processor in the classical sense.** The **left MSO**
    is a **binaural coincidence detector** — it **receives** the
    **bilateral excitatory** auditory inputs and **performs** the
    **ITD computation** — it **projects** the **binaural
    representation** to the **left inferior colliculus** (primarily,
    via the **lateral lemniscus**) and to the **right inferior
    colliculus** (contralaterally, to a lesser extent). The
    **processing** of **binaural sound localization** is
    **distributed** across the **cochlear nuclei** (monaural auditory
    processing), the **left MSO** (ITD processing), the **left LSO**
    (ILD processing), the **inferior colliculus** (integration of
    binaural and spectral cues), the **medial geniculate body**
    (thalamic relay), and the **primary auditory cortex** (cortical
    processing). The **left MSO** is the **left ITD processor** — the
    **brainstem substrate** of **low-frequency left-sided horizontal
    sound localization**.

**The unifying theme:** the left medial superior olive is the **left
binaural ITD processor** — the **excitatory coincidence detector** that
**computes** the **interaural time difference** for **low-frequency
horizontal sound localization** on the **left side** and the
**midline**. It is a **leaf module** under the ``left`` sub-container of
the medial_superior_olive container, **bilateral-excitatory**,
**SLEA-free**, and **NOT the left MNTB** (the **left MNTB** is the
**inhibitory relay** for ILD processing).

Associated Disorders
--------------------
The left medial superior olive has **no named "left medial superior
olive syndrome"** — its clinical associations are **binaural-specific**:

*   **Left MSO Lesion — Impaired ITD-Based Sound Localization on the
    Left with Preserved Pure-Tone Thresholds:** A lesion of the **left
    medial superior olive** (e.g. **left pontine stroke**, **tumor**,
    **demyelination**) causes **impaired ITD-based sound localization**
    — specifically, **impaired localization of low-frequency sounds on
    the left side** and the **midline** — with **preserved pure-tone
    thresholds** (because the **monaural auditory pathway** — the
    **cochlear nuclei** and the **ascending auditory pathway** — is
    intact). **The ITD-specific pattern** is the **substrate** of the
    **left MSO** function — this is the **"left ITD-specific binaural
    deficit"** that **distinguishes** a **left MSO lesion** from a
    **left cochlear nuclei lesion** (which causes **left sensorineural
    hearing loss**) or a **left LSO lesion** (which causes **left
    ILD-specific binaural deficit**).

*   **Low-Frequency Left-Sided Sound Localization Deficit — Left MSO
    Involvement:** **Low-frequency horizontal sound localization** on
    the **left side** and the **midline** depends on **ITD processing**,
    which is **subserved** by the **left MSO**. **The left MSO** is
    **one of the neural substrates** of **left ITD-based sound
    localization**, and its dysfunction may **contribute** to
    **low-frequency left-sided sound localization deficits** —
    especially in **patients with left pontine lesions** or
    **age-related hearing loss** (presbycusis).

*   **Presbycusis — Left MSO Involvement:** **Presbycusis** (age-related
    hearing loss) is characterized by **peripheral auditory dysfunction**
    (cochlear hair cell loss) **and central auditory dysfunction**
    (including **left MSO** dysfunction — **reduced neuron number**,
    **reduced synaptic density**, and **reduced ITD processing**). The
    **left MSO** may show **age-related changes** — contributing to
    **impaired low-frequency left-sided horizontal sound localization**
    and **impaired speech understanding in noise** in **older adults**.

*   **Multiple Sclerosis — Left MSO Involvement:** **Multiple sclerosis**
    can affect the **left MSO** (as a **left brainstem demyelinating
    lesion**), contributing to **impaired left ITD-based sound
    localization** and **left binaural hearing deficits**.

*   **Left Pontine Stroke — Left MSO Involvement:** A **left pontine
    stroke** (e.g. **basilar artery** perforator territory) involving
    the **left MSO** causes **impaired left ITD-based sound
    localization** — often accompanied by **other left pontine signs**
    (**right hemiparesis**, **left facial palsy**, **left abducens
    palsy**, **right cerebellar ataxia**).

*   **Binaural Hearing Deficit — Left MSO Involvement:** **Binaural
    hearing** is the **ability to use** the **differences** between the
    **two ears** to **localize sound** and to **understand speech in
    noise**. **The left MSO** is **one of the neural substrates** of
    **binaural hearing** (specifically **left ITD-based binaural
    processing** — a **dominant** binaural cue for **low-frequency
    sound localization** in humans), and its dysfunction may
    **contribute** to **left binaural hearing deficits**.

*   **No Named "Left MSO Syndrome":** The left MSO is a **single
    bilateral sub-nucleus** — it has **no named clinical syndrome** of
    its own. Its clinical relevance is **ITD-specific** — **impaired
    left ITD-based sound localization**, **impaired low-frequency
    left-sided horizontal sound localization**, and **impaired left
    binaural hearing**.

**What is NOT here:** The left MSO is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **vestibular neuritis** (vestibular nerve), **labyrinthitis**
(inner ear), or **auditory neuropathy spectrum disorder** (cochlear nerve
or hair cell). Its clinical relevance is **ITD-specific**, via the
**interaural time difference (ITD) processing** it subserves on the
**left side** and the **midline**. **No named left MSO syndrome
exists.**

Lateralization Notes
--------------------
This is the **left** medial superior olive module. The left MSO is
**bilaterally symmetric** with the right MSO and **strictly mirrored** —
and it carries **NO warning at the sub-container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right** MSO are
    **structurally identical** — same neuron populations, same functional
    system (ITD processing via coincidence detection), same bilateral
    framing. The bilateral symmetry is **strict**.

*   **Bilateral Excitatory Input (Structural Fact, NOT a Lateralization
    Warning):** The **left MSO** receives **bilateral excitatory** input
    from the **left cochlear nuclei** (ipsilateral, via the **left
    trapezoid body**) and the **right cochlear nuclei** (contralateral,
    via the **right trapezoid body**). **This bilateral excitatory
    input** is a **structural fact** of the **MSO** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **MSO's role as the coincidence detector** for **ITD processing** —
    the **left MSO neuron** **fires maximally** when the **ipsilateral
    (left-ear)** and **contralateral (right-ear)** inputs arrive
    **simultaneously** (the **Jeffress coincidence-detection model**).

*   **Left ITD Computation (Structural Fact, NOT a Lateralization
    Warning):** The **left MSO neuron** **fires maximally** when the
    **left-ear sound arrives earlier** than the **right-ear sound** (for
    **sound sources on the left side**) or when they arrive
    **simultaneously** (for **sound sources on the midline**) —
    depending on the **specific ITD tuning** of the **left MSO neuron**.
    **This ITD computation** is a **structural fact** of the **binaural
    sound-localization system** — it is **not** a functional
    lateralization. It is the **neural substrate** of **left-sided
    ITD-based horizontal sound localization** in the human brain.

*   **Ipsilateral and Contralateral Inferior Colliculus Projections
    (Structural Fact, NOT a Lateralization Warning):** The **left MSO**
    **projects** to the **left inferior colliculus** (ipsilateral,
    primarily, via the **lateral lemniscus**) and to the **right
    inferior colliculus** (contralaterally, to a lesser extent). **This
    ipsilateral and contralateral projection** is a **structural fact**
    of the **ascending auditory system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **bilateral
    inferior colliculus representation** of **left-sided sound-source
    location**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The left MSO is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the left MSO.

*   **NO Amygdala-Lateralization Warning of their own (the left MSO is
    BINAURAL AUDITORY, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The left MSO is a **binaural auditory ITD
    coincidence detector** — consumers must **not** conflate it with the
    **amygdala** or with the **fear circuit**.

**A consumer that assumes "left MSO = right MSO" will be structurally
correct** — the two sides are **strictly symmetric** (the bilateral
excitatory input and the left-sided ITD computation are structural
facts, not lateralizations). The left MSO is a **strict-mirror pair with
NO warning at the sub-container level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left sub-container is the
    **left half**; it does **not** import the right sub-container at
    module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../medial_superior_olive/right/``,
    ``.../superior_olivary_complex/lateral_superior_olive/``,
    ``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``,
    ``.../superior_olivary_complex/``, ``.../pons/tegmentum/``,
    ``.../pons/cranial_nerve_nuclei/``, ``.../midbrain/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    left MSO's relationships to the **left LSO**, the **left MNTB**, the
    **left cochlear nuclei**, the **right cochlear nuclei**, the
    **trapezoid body**, the **lateral lemniscus**, the **left inferior
    colliculus**, the **left medial geniculate body**, the **left
    primary auditory cortex**, the **left facial nerve nucleus**, the
    **left abducens nucleus**, the **left cochlear** and **left
    vestibulocochlear nerves**, the **whole medial superior olive
    container**, the **whole superior olivary complex container**, and
    the **SLEA continuum** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **principal
    coincidence-detector neurons** and the **local circuit interneurons**
    are documented as **prose**, not as sub-modules. Consumers must not
    assume any exist as children; resolve neuron-population-level detail
    through the references.
*   **LEFT HALF — NOT the whole medial_superior_olive container.** The
    **medial_superior_olive** container has **two structural children** —
    ``left`` and ``right``. The **left** sub-container (here) is the
    **left-side** half only.
*   **STRICT MIRROR with the right MSO — NO warning at the sub-container
    level.** The **left** and **right** MSO are **structurally
    identical**. Any lateralization is documented **here, in the
    Lateralization Notes**.
*   **ITD PROCESSOR — NOT the ILD processor (LSO).** The **left MSO**
    processes **interaural time differences**; the **left LSO** processes
    **interaural level differences**. Consumers must **not** conflate the
    two.
*   **NOT the left MNTB — that is the INHIBITORY RELAY for ILD
    processing.** The **left MNTB** is the **glycinergic inhibitory
    relay** that **projects to** the left LSO. Consumers must **not**
    conflate the left MSO with the left MNTB.
*   **EXCITATORY COINCIDENCE DETECTOR — NOT an inhibitory relay.** The
    **left MSO** principal neurons are **excitatory (glutamatergic)** —
    they **fire maximally** when the **ipsilateral** and
    **contralateral** inputs arrive **simultaneously**. Consumers must
    **not** conflate the left MSO with an **inhibitory relay**.
*   **NOT the left cochlear nuclei or the right cochlear nuclei — those
    are the UPSTREAM MONAURAL FIRST-ORDER RELAYS.** Consumers must
    **not** conflate the left MSO with either cochlear nuclei.
*   **NOT the trapezoid body or the lateral lemniscus — those are the
    WHITE-MATTER TRACTS.** Consumers must **not** conflate the left MSO
    with either tract.
*   **NOT the left inferior colliculus, the left medial geniculate body,
    or the left primary auditory cortex — those are DOWNSTREAM AUDITORY
    STRUCTURES.** Consumers must **not** conflate the left MSO with any
    of them.
*   **NOT the left facial nerve nucleus or the left abducens nucleus —
    those are ANATOMICALLY ADJACENT SIBLINGS.** Consumers must **not**
    conflate the left MSO with either of them.
*   **NOT the left cochlear or left vestibulocochlear nerve — those are
    the PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE.** Consumers must
    **not** conflate the left MSO with either nerve.
*   **NOT the whole medial_superior_olive container — that is the
    PARENT.** Consumers must **not** conflate the left MSO with the whole
    MSO.
*   **NOT the whole superior_olivary_complex container — that is the
    GRANDPARENT.** Consumers must **not** conflate the left MSO with the
    whole superior olivary complex.
*   **MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — NOT a single uniform
    nucleus.** The **principal coincidence-detector neurons**
    (excitatory bipolar neurons) and the **local circuit interneurons**
    are **prose**, not structural children. Consumers must **not** treat
    the left MSO as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The left MSO is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.
*   **NOT the fear-output — the left MSO is BINAURAL AUDITORY.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **left MSO** is a **binaural auditory ITD processor**
    — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The left MSO is a local leaf under the
    ``left`` sub-container of the medial_superior_olive container, not a
    cross-listed leaf.
*   **No nested cross-listing.** The left MSO has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.medial_superior_olive import left

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex."
        "medial_superior_olive.left"
    )

**Do not** assume the left MSO is a **container**. It is a **leaf** —
the **principal coincidence-detector neurons** and the **local circuit
interneurons** are **prose**, not structural children.

**Do not** assume the left MSO is the **whole medial_superior_olive
container**. It is the **left-side half only** — the right side is a
**separate structural sibling**.

**Do not** assume the left MSO is the **right MSO**. The two are a
**strict mirror pair with NO warning at the sub-container level** — any
lateralization is documented **here, in the Lateralization Notes**.

**Do not** assume the left MSO is the **left LSO** or the **left MNTB**.
The **left LSO** is the **ILD processor**; the **left MNTB** is the
**inhibitory relay** for ILD processing. The **left MSO** is the **ITD
processor** — the **excitatory coincidence detector**. They are
**different structures** — different binaural cues and different neural
mechanisms.

**Do not** assume the left MSO is the **left cochlear nuclei** or the
**right cochlear nuclei**. Those are the **monaural first-order
relays**; the **left MSO** is the **binaural second-order ITD
processor**.

**Do not** assume the left MSO is the **trapezoid body** or the **lateral
lemniscus**. The **trapezoid body** is the **afferent white-matter
tract**; the **lateral lemniscus** is the **efferent white-matter
tract**. The **left MSO** is the **grey-matter neuron cluster** that
receives from the trapezoid body and projects to the lateral lemniscus.

**Do not** assume the left MSO is the **left inferior colliculus**, the
**left medial geniculate body**, or the **left primary auditory
cortex**. Those are the **downstream** auditory relays — the **left
MSO** is the **pontine ITD processor**.

**Do not** assume the left MSO is the **left facial nerve nucleus** or
the **left abducens nucleus**. Those are **anatomically adjacent
siblings** — different functional systems.

**Do not** assume the left MSO is the **left cochlear nerve** or the
**left vestibulocochlear nerve**. Those are the **peripheral auditory
conduction infrastructure** — the left MSO is **central grey matter**.

**Do not** assume the left MSO is the **whole superior olivary
complex**. The **superior olivary complex** is the **grandparent** — the
**left MSO** is one of its **three sub-nuclei** (via the
medial_superior_olive container).

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the left MSO. **The left MSO is SLEA-FREE** — it is
**not** an extended-amygdala component, and it is **NOT part of the fear
circuit**.

Iterating the left MSO's (empty) children (recommended consumer
pattern)::

    LEFT_MEDIAL_SUPERIOR_OLIVE_CHILDREN = ()
    # The left MSO is a leaf. The principal coincidence-detector neurons
    # and the local circuit interneurons are prose, not modules.

Reaching the right MSO (recommended consumer pattern — the strict
mirror)::

    # The right MSO is the structurally identical RIGHT half of the
    # medial_superior_olive container:
    #
    #   .../medial_superior_olive/right/
    #
    # The left and right MSO are a STRICT MIRROR PAIR with NO warning at
    # the sub-container level.

Reaching the left LSO (recommended consumer pattern — the ILD processor
sibling)::

    # The left LSO is the ILD PROCESSOR:
    #
    #   .../superior_olivary_complex/lateral_superior_olive/left/
    #
    # The left LSO processes INTERAURAL LEVEL DIFFERENCES for
    # HIGH-FREQUENCY sound localization; the left MSO processes
    # INTERAURAL TIME DIFFERENCES for LOW-FREQUENCY sound localization.

Reaching the left MNTB (recommended consumer pattern — the inhibitory
relay sibling for ILD processing)::

    # The left MNTB is the INHIBITORY RELAY for ILD processing:
    #
    #   .../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/
    #
    # The left MNTB is the GLYCINERGIC INHIBITORY RELAY (it converts
    # excitatory right cochlear nuclei input into inhibitory input to
    # the left LSO); the left MSO is the EXCITATORY COINCIDENCE DETECTOR
    # for ITD processing.

Reaching the left cochlear nuclei (recommended consumer pattern — the
IPSILATERAL UPSTREAM source)::

    # The left cochlear nuclei are the IPSILATERAL UPSTREAM MONAURAL
    # FIRST-ORDER relay — they project to the left MSO (via the left
    # trapezoid body):
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/
    #
    # The left cochlear nuclei are UPSTREAM (monaural first-order); the
    # left MSO is DOWNSTREAM (binaural second-order excitatory
    # coincidence detector).

Reaching the right cochlear nuclei (recommended consumer pattern — the
CONTRALATERAL UPSTREAM source)::

    # The right cochlear nuclei are the CONTRALATERAL UPSTREAM MONAURAL
    # FIRST-ORDER relay — they project to the left MSO (via the right
    # trapezoid body):
    #
    #   .../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/
    #
    # The right cochlear nuclei are the contralateral upstream source for
    # the left MSO's bilateral excitatory input.

Reaching the left inferior colliculus (recommended consumer pattern —
the DOWNSTREAM midbrain auditory relay)::

    # The left inferior colliculus is the DOWNSTREAM midbrain auditory
    # relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/
    #
    # The left MSO is UPSTREAM of the left inferior colliculus; the left
    # inferior colliculus is DOWNSTREAM of the left MSO.

Reaching the whole medial superior olive container (recommended
consumer pattern — the PARENT)::

    # The medial superior olive container is the BILATERAL ITD PROCESSOR
    # parent that CONTAINS the left MSO and the right MSO:
    #
    #   .../medial_superior_olive/
    #
    # The left MSO is one of the TWO HALVES of the medial superior olive
    # container.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mso_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"medial_superior_olive.{side}"
        )
        # resolve mso_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The left MSO's neuron populations are prose, not modules:
    #   principal coincidence-detector neurons (excitatory, glutamatergic
    #       bipolar neurons) -> receive bilateral excitatory cochlear
    #       nuclei input (via trapezoid body); fire maximally when
    #       ipsilateral and contralateral inputs arrive simultaneously
    #       (Jeffress coincidence-detection model); project to the left
    #       inferior colliculus (primarily, via lateral lemniscus) and to
    #       the right inferior colliculus (contralaterally); the left ITD
    #       computation output
    #   local circuit interneurons -> modulate the principal neurons
    #       within the left MSO
    #
    # Do not attempt to resolve these as sub-paths of the left MSO —
    # resolve them at the neuron-population level through the references.

References
----------
*   **Canonical MSO anatomy:** Pickles, J.O. (2015). *An Introduction
    to the Physiology of Hearing*, 4th ed. (Medial superior olive and
    ITD processing — definitive.)
*   **MSO and ITD processing:** Yin, T.C.T., Chan, J.C.K. (1990).
    "Interaural time sensitivity in medial superior olive of cat."
    *Journal of Neurophysiology* 64:465–488. (MSO — ITD processing;
    coincidence detection.)
*   **Jeffress coincidence-detection model:** Jeffress, L.A. (1948). "A
    place theory of sound localization." *Journal of Comparative and
    Physiological Psychology* 41:35–39. (Original Jeffress model —
    coincidence detection for ITD processing.)
*   **Binaural sound localization — review:** Grothe, B., Pecka, M.,
    McAlpine, D. (2010). "Mechanisms of sound localization and coding
    in mammals." *Physiological Reviews* 90:983–1012. (MSO and LSO —
    ITD and ILD processing; MSO coincidence detection.)
*   **MSO — modern review:** Golding, N.L., Oertel, D. (2012). "Synaptic
    integration in the avian cochlear nucleus." *Progress in
    Neurobiology* 98:1–17. (MSO — coincidence detection; synaptic
    integration.)
*   **Human MSO:** Middlebrooks, J.C. (2015). "Sound localization." In
    *The Auditory System*. (Human MSO — larger than the LSO; dominant
    binaural sound-localization nucleus.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Medial superior olive in
    overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An
    Atlas of Structures, Sections, and Systems*, 8th ed. (Medial
    superior olive and the pontomedullary junction.)
*   **Binaural hearing deficits:** Middlebrooks, J.C., Green, D.M.
    (1991). "Sound localization by human listeners." *Annual Review of
    Psychology* 42:135–159. (Binaural hearing deficits — impaired sound
    localization.)
*   **Presbycusis — MSO involvement:** Frisina, R.D., Walton, J.P.
    (2006). "Age-related structural and functional changes in the
    auditory system." In *Handbook of the Biology of Aging*.
    (Presbycusis — MSO age-related changes.)
*   **Multiple sclerosis — MSO involvement:** Furst, M., Aharonson,
    V., Levine, R.A., et al. (2000). "Sound lateralization in patients
    with unilateral or bilateral multiple sclerosis." *Annals of
    Neurology* 47:389–393. (Multiple sclerosis — MSO involvement;
    binaural hearing deficits.)
*   **Left pontine stroke — left MSO involvement:** Bassetti, C.,
    Bogousslavsky, J., Barth, A., Regli, F. (1996). "Isolated infarcts
    of the pontine nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Left pontine stroke — left MSO involvement;
    binaural hearing deficits.)
*   **Left LSO (contrast — the ILD processor sibling):** Tollin, D.J.
    (2003). "The lateral superior olive as a source of ascending and
    descending auditory pathways." *Journal of the Association for
    Research in Otolaryngology* 4:311–327. (LSO — ILD processing;
    sibling of the MSO.)
*   **Left MNTB (contrast — the inhibitory relay sibling for ILD
    processing):** Smith, P.H., Joris, P.X., Yin, T.C.T. (1998).
    "Anatomy and physiology of principal cells of the medial nucleus of
    the trapezoid body (MNTB) of the cat." *Journal of Neurophysiology*
    79:3127–3142. (MNTB — glycinergic inhibitory relay for ILD
    processing; sibling of the MSO.)
*   **Left cochlear nuclei (contrast — the IPSILATERAL UPSTREAM monaural
    first-order relay):** Cant, N.B., Benson, C.G. (2003). "Parallel
    auditory pathways: projection patterns of the different neuronal
    populations in the cochlear nuclei." *Brain Research Bulletin*
    60:457–474. (Left cochlear nuclei — monaural first-order relay;
    projects to the left MSO via the left trapezoid body.)
*   **Right cochlear nuclei (contrast — the CONTRALATERAL UPSTREAM
    monaural first-order relay):** Cant, N.B., Benson, C.G. (2003).
    "Parallel auditory pathways: projection patterns of the different
    neuronal populations in the cochlear nuclei." *Brain Research
    Bulletin* 60:457–474. (Right cochlear nuclei — monaural first-order
    relay; projects to the left MSO via the right trapezoid body.)
*   **Trapezoid body (contrast — the white-matter afferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Trapezoid body — afferent white-matter tract from
    the cochlear nuclei to the MSO.)
*   **Lateral lemniscus (contrast — the white-matter efferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Lateral lemniscus — efferent white-matter tract
    from the MSO to the inferior colliculus.)
*   **Left inferior colliculus (contrast — the midbrain downstream
    auditory relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002).
    "The inferior colliculus: a hub for the central auditory system."
    In *Integrative Functions in the Mammalian Auditory Pathway*. (Left
    inferior colliculus — downstream of the left MSO.)
*   **Left medial geniculate body (contrast — the thalamic downstream
    auditory relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The
    Inferior Colliculus: A Hub for the Central Auditory System*. (Left
    medial geniculate body — downstream of the left MSO.)
*   **Left primary auditory cortex (contrast — the cortical downstream
    auditory target):** Pickles, J.O. (2015). *An Introduction to the
    Physiology of Hearing*, 4th ed. (Left primary auditory cortex —
    downstream of the left MSO.)
*   **SLEA (contrast — the left MSO is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the left MSO.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the left MSO.)
*   NeuroNames — Medial superior olive (left); FMA — Medial superior
    olive (left member).
"""
