"""
infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.lateral_superior_olive
=====================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── superior_olivary_complex
                ├── lateral_superior_olive   <-- THIS MODULE
                ├── medial_nucleus_of_trapezoid_body
                └── medial_superior_olive

**Primary synonym:** Lateral superior olive; LSO; lateral superior
olivary nucleus; "the interaural level difference (ILD) processor."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nucleus** — an **anatomically delimited
grey-matter nucleus** in the **lateral superior olivary complex**, the
**principal substrate** of **interaural level difference (ILD)
processing** for **high-frequency horizontal sound localization**.
**Part of:** The **superior_olivary_complex** container — specifically,
the **binaural ILD-processing** component. The **superior olivary
complex** is the **pontine binaural sound-localization relay** of the
**ventral pontine tegmentum**.
**Structural parent:** ``.../superior_olivary_complex/`` → **direct
child** of the superior olivary complex container.
**Structural children:** **None.** This is a **leaf** module. The
**excitatory (glutamatergic) projection neurons** and the **inhibitory
(glycinergic) input-receiving neurons** are documented as **prose**,
not as structural children.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
lateral superior olive is a LEAF, not a container.** It has **no
structural children**. The **excitatory and inhibitory neuron
populations** are **prose** populations, not structural children.
Consumers must **not** treat the lateral superior olive as a container,
and must **not** assume the neuron populations exist as sub-modules.
**Boundary status (BILATERAL SINGLE MODULE — NOT split into left/right
at the tree level):** **Boundary case — the lateral superior olive is a
BILATERAL SINGLE MODULE at the tree level, even though the LSO is
BILATERAL in real anatomy.** The module represents the **bilateral
LSO** — the **left LSO** and the **right LSO** — as a **single module**.
Unlike the **superior_olivary_complex** container (which has ``left``
and ``right`` structural children in the tree), the **LSO module** (here)
is a **single, bilateral representation** — it does **not** split into
left/right at the tree level. Consumers must **not** assume a left/right
split exists at the tree level — the module is a **single, bilateral
representation**. Any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere.
**Boundary status (NOT the medial nucleus of the trapezoid body — that
is a SIBLING under the superior olivary complex):** **Boundary case —
the lateral superior olive is NOT the medial nucleus of the trapezoid
body (MNTB); the MNTB is a SIBLING under the superior olivary complex.**
The **MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``) is
the **inhibitory relay** that **projects** an **inhibitory
(glycinergic)** input to the **ipsilateral LSO** — it is the **neural
substrate** of **contralateral inhibition** that is **essential** for
**ILD processing**. The **LSO** (here) is the **ILD processor** that
**receives** the **excitatory** ipsilateral cochlear nuclei input and
the **inhibitory** MNTB input. They are **DIFFERENT STRUCTURES** —
different functional roles (ILD processing vs. inhibitory relay).
They are **functionally coupled** — the MNTB **projects to** the LSO
— but they are **not the same structure**. Consumers must **not**
conflate the lateral superior olive with the medial nucleus of the
trapezoid body.
**Boundary status (NOT the medial superior olive — that is a SIBLING
under the superior olivary complex):** **Boundary case — the lateral
superior olive is NOT the medial superior olive (MSO); the MSO is a
SIBLING under the superior olivary complex.** The **MSO**
(``.../superior_olivary_complex/medial_superior_olive/``) is the
**ITD processor** — the **principal substrate** of **interaural time
difference (ITD) processing** for **low-frequency horizontal sound
localization**. The **LSO** (here) is the **ILD processor** — the
**principal substrate** of **interaural level difference (ILD)
processing** for **high-frequency horizontal sound localization**. They
are **DIFFERENT STRUCTURES** — different binaural cues (ILD vs. ITD),
different frequency ranges (high vs. low), different neural mechanisms
(coincidence detection for ITD vs. excitation-inhibition for ILD).
Consumers must **not** conflate the lateral superior olive with the
medial superior olive.
**Boundary status (NOT the cochlear nuclei — those are the UPSTREAM
MONAURAL FIRST-ORDER RELAY):** **Boundary case — the lateral superior
olive is NOT the cochlear nuclei.** The **cochlear nuclei**
(``.../vestibulocochlear_nuclei/cochlear_nuclei/``) are the **first
central auditory relay** — they **receive** the **monaural** auditory
input from the **ipsilateral cochlea** and **project** to the **LSO**
(via the **trapezoid body**). The **LSO** (here) is the **binaural
second-order relay** that **receives** the **ipsilateral excitatory**
cochlear nuclei projection and the **MNTB inhibitory** projection (which
itself receives **contralateral cochlear nuclei** input) and **performs**
the **ILD computation**. They are **DIFFERENT STRUCTURES** — the
**cochlear nuclei** are **monaural first-order**; the **LSO** is
**binaural second-order**. Consumers must **not** conflate the lateral
superior olive with the cochlear nuclei.
**Boundary status (NOT the trapezoid body — that is the WHITE-MATTER
AFFERENT TRACT):** **Boundary case — the lateral superior olive is NOT
the trapezoid body.** The **trapezoid body** is the **white-matter
decussating tract** that **carries** the **bilateral auditory axons**
from the **cochlear nuclei** to the **superior olivary complex** — the
**afferent limb** of the **binaural sound-localization pathway**. The
**LSO** (here) is the **grey-matter neuron cluster** that **receives**
the trapezoid-body axons (via **excitatory** input from the
**ipsilateral cochlear nuclei** and **inhibitory** input from the
**ipsilateral MNTB**). They are **DIFFERENT STRUCTURES** — the **LSO**
is grey matter; the **trapezoid body** is white matter. Consumers must
**not** conflate the lateral superior olive with the trapezoid body.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
EFFERENT TRACT):** **Boundary case — the lateral superior olive is NOT
the lateral lemniscus.** The **lateral lemniscus** is the **white-matter
ascending tract** that **carries** the **efferent axons** from the
**superior olivary complex** (including the **LSO**) to the **inferior
colliculus**. The **LSO** (here) is the **grey-matter neuron cluster**
that **gives rise to** the lateral lemniscus axons. They are **DIFFERENT
STRUCTURES** — the **LSO** is grey matter; the **lateral lemniscus** is
white matter. Consumers must **not** conflate the lateral superior olive
with the lateral lemniscus.
**Boundary status (NOT the inferior colliculus — that is the MIDBRAIN
DOWNSTREAM AUDITORY RELAY):** **Boundary case — the lateral superior
olive is NOT the inferior colliculus.** The **inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
and ``.../right/``) is the **midbrain auditory relay** that **receives**
the **ascending auditory projections** from the **superior olivary
complex** (including the **LSO**) and **projects** to the **medial
geniculate body**. The **LSO** (here) is the **pontine ILD processor**
— it is **upstream** of the inferior colliculus. They are **DIFFERENT
STRUCTURES** — the **LSO** is **pontine** and **upstream**; the
**inferior colliculus** is **midbrain** and **downstream**. Consumers
must **not** conflate the lateral superior olive with the inferior
colliculus.
**Boundary status (NOT the medial geniculate body — that is the
THALAMIC DOWNSTREAM AUDITORY RELAY):** **Boundary case — the lateral
superior olive is NOT the medial geniculate body.** The **medial
geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
and ``.../right/``) is the **thalamic auditory relay** that **receives**
the **ascending auditory projections** from the **inferior colliculus**
and **projects** to the **primary auditory cortex**. The **LSO** (here)
is the **pontine ILD processor** — it is **upstream** of the medial
geniculate body. They are **DIFFERENT STRUCTURES** — the **LSO** is
**pontine** and **upstream**; the **medial geniculate body** is
**diencephalic** and **downstream**. Consumers must **not** conflate the
lateral superior olive with the medial geniculate body.
**Boundary status (NOT the primary auditory cortex — that is the CORTICAL
DOWNSTREAM AUDITORY TARGET):** **Boundary case — the lateral superior
olive is NOT the primary auditory cortex.** The **primary auditory
cortex** (Heschl's gyrus, Brodmann areas 41 and 42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
and ``.../right/``) is the **cortical target** of the **ascending
auditory pathway**. The **LSO** (here) is the **pontine ILD processor**
— it is **upstream** of the primary auditory cortex. They are
**DIFFERENT STRUCTURES** — the **LSO** is **pontine** and **upstream**;
the **primary auditory cortex** is **cortical** and **downstream**.
Consumers must **not** conflate the lateral superior olive with the
primary auditory cortex.
**Boundary status (NOT the facial nerve nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the lateral superior
olive is NOT the facial nerve nucleus.** The **facial nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
``.../right/``) is the **branchial motor** nucleus for the **muscles of
facial expression**. The **LSO** (here) is the **binaural ILD
processor**. They are **DIFFERENT STRUCTURES** — different functional
systems (branchial motor vs. binaural ILD processing). They are
**anatomically adjacent** (both are in the **ventral pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the lateral superior olive with the
facial nerve nucleus.
**Boundary status (NOT the abducens nucleus — that is an ANATOMICALLY
ADJACENT SIBLING):** **Boundary case — the lateral superior olive is
NOT the abducens nucleus.** The **abducens nucleus**
(``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and ``.../right/``)
is the **somatic motor** nucleus for the **lateral rectus**. The **LSO**
(here) is the **binaural ILD processor**. They are **DIFFERENT
STRUCTURES** — different functional systems (somatic motor vs. binaural
ILD processing). They are **anatomically adjacent** — the **LSO** is
**near the genu of the facial nerve** and the **abducens nucleus**;
this proximity is a **classic source of confusion** — consumers must
**not** conflate the lateral superior olive with the abducens nucleus.
**Boundary status (NOT the cochlear or vestibulocochlear nerve — those
are the PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE):** **Boundary
case — the lateral superior olive is NOT the cochlear or
vestibulocochlear nerve.** The **cochlear nerve** (the cochlear division
of CN VIII) and the **vestibulocochlear nerve** (CN VIII) are the
**white-matter peripheral nerves** that **carry** the **primary auditory
axons** from the **spiral ganglion** to the **cochlear nuclei**. The
**LSO** (here) is the **central grey-matter binaural ILD processor**.
They are **DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **LSO** is **central grey matter**. Consumers must
**not** conflate the lateral superior olive with the cochlear or
vestibulocochlear nerve.
**Boundary status (NOT the whole superior olivary complex — that is the
PARENT):** **Boundary case — the lateral superior olive is NOT the whole
superior olivary complex; the superior olivary complex is the PARENT.**
The **superior olivary complex**
(``.../superior_olivary_complex/``) is the **pontine binaural
sound-localization relay** — it **contains** the **LSO**, the **MSO**,
and the **MNTB**. The **LSO** (here) is the **ILD processor** — one of
the **three sub-nuclei** of the superior olivary complex. Consumers must
**not** conflate the lateral superior olive with the **whole superior
olivary complex**.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
functionally distinct populations):** **Boundary case — the lateral
superior olive is NOT a single uniform neuron population; it contains
MULTIPLE functionally distinct populations.** The **principal output
neurons** — the **excitatory (glutamatergic)** projection neurons that
**receive** the **excitatory ipsilateral cochlear nuclei** input and the
**inhibitory MNTB** input, and **project** to the **inferior
colliculus** (via the **lateral lemniscus**) — they are the **ILD
computation** output. The **inhibitory interneurons** — the **local
circuit neurons** that **modulate** the **principal output neurons**.
**These populations are prose, not structural children.** Consumers must
**not** treat the lateral superior olive as a single uniform population
— it is a **functionally heterogeneous nucleus** with **distinct**
sub-circuits.
**Boundary status (SLEA-FREE — the lateral superior olive is NOT an
extended-amygdala component):** **Boundary case — the lateral superior
olive is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **LSO** is a **binaural auditory ILD processor** — it is
**NOT** an extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into the
lateral superior olive — it is **SLEA-free**.

Overview
--------
The lateral superior olive is the **principal substrate of interaural
level difference (ILD) processing** for **high-frequency horizontal
sound localization**. It is a **leaf** module under the
superior_olivary_complex container — the **bilateral single module**
representing the **left LSO** and the **right LSO** as a **single
bilateral representation**.

**The lateral superior olive is a LEAF, not a container.** It has **no
structural children**. The **excitatory and inhibitory neuron
populations** are **prose populations**, not structural children.

**The lateral superior olive is a BILATERAL SINGLE MODULE at the tree
level.** Unlike the **superior_olivary_complex** container (which has
``left`` and ``right`` structural children in the tree), the **LSO
module** (here) is a **single, bilateral representation** — it does
**not** split into left/right at the tree level.

**The lateral superior olive is NOT the MNTB or the MSO.** The **MNTB**
is the **inhibitory relay** that **projects to** the LSO (essential for
ILD processing). The **MSO** is the **ITD processor** (low-frequency
horizontal sound localization). They are **siblings** under the superior
olivary complex — **functionally distinct** binaural sub-nuclei.

**The lateral superior olive is the ILD PROCESSOR, not the ITD
processor.** The **LSO** processes **interaural level differences**
(ILD) for **high-frequency** sound localization. The **MSO** processes
**interaural time differences** (ITD) for **low-frequency** sound
localization. **This distinction is functionally load-bearing** — the
two binaural cues dominate at different frequency ranges (ILD above
~1.5 kHz; ITD below ~1.5 kHz in humans).

**The lateral superior olive is a TWO-INPUT coincidence comparator.**
The **LSO** receives **excitatory** input from the **ipsilateral
cochlear nuclei** (via the **trapezoid body**) and **inhibitory** input
from the **ipsilateral MNTB** (which itself receives **contralateral
cochlear nuclei** input via the **trapezoid body**). The **excitation-
inhibition** arrangement is the **neural substrate** of **ILD
processing** — the **LSO** neuron **compares** the **ipsilateral sound
level** (excitation) with the **contralateral sound level**
(inhibition).

**The lateral superior olive is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Composition (neuron populations, not structural children)
--------------------------------------------------------------
The lateral superior olive contains **multiple functionally distinct
neuron populations** — documented as **prose**, not as structural
children:

*   **Principal output neurons** — the **excitatory (glutamatergic)**
    projection neurons that **receive** the **excitatory ipsilateral
    cochlear nuclei** input (via the **trapezoid body**) and the
    **inhibitory MNTB** input (via the **glycinergic** projection from
    the **ipsilateral MNTB**, which itself receives **contralateral
    cochlear nuclei** input). They **project** to the **inferior
    colliculus** (via the **lateral lemniscus**). They are the **ILD
    computation** output — they **fire maximally** when the
    **ipsilateral sound level** is **higher** than the **contralateral
    sound level** (because the **excitatory** ipsilateral drive
    **exceeds** the **inhibitory** contralateral drive).

*   **Inhibitory interneurons** — the **local circuit neurons** that
    **modulate** the **principal output neurons** within the LSO. They
    are **prose** populations, not structural children.

**These populations are prose, not structural children.** The tree wires
the **lateral superior olive** as a **single leaf** under the
superior_olivary_complex container — the **excitatory and inhibitory
neuron populations** are **prose**, not structural children. Consumers
that need **neuron-population-level** resolution should consult the
references, not the tree.

The Lateral Superior Olive / Medial Nucleus of the Trapezoid Body Boundary
--------------------------------------------------------------------------
This is the **sibling** boundary — **ILD processor vs. inhibitory relay**:

*   **Lateral superior olive** (this module) — the **ILD processor** that
    **receives** the **excitatory ipsilateral cochlear nuclei** input
    and the **inhibitory MNTB** input.

*   **Medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``)
    — the **inhibitory relay** that **receives** the **contralateral
    cochlear nuclei** globular bushy cell projections (via the
    **trapezoid body**) and **projects** an **inhibitory (glycinergic)**
    input to the **ipsilateral LSO**.

**They are DIFFERENT STRUCTURES** — different functional roles (ILD
processing vs. inhibitory relay). **They are functionally coupled** —
the MNTB **projects to** the LSO. Consumers must **not** conflate the
lateral superior olive with the medial nucleus of the trapezoid body.

The Lateral Superior Olive / Medial Superior Olive Boundary
-----------------------------------------------------------
This is the **sibling** boundary — **ILD processor vs. ITD processor**:

*   **Lateral superior olive** (this module) — the **ILD processor** for
    **high-frequency horizontal sound localization**.

*   **Medial superior olive (MSO)**
    (``.../superior_olivary_complex/medial_superior_olive/``) — the
    **ITD processor** for **low-frequency horizontal sound
    localization**.

**They are DIFFERENT STRUCTURES** — different binaural cues (ILD vs.
ITD), different frequency ranges (high vs. low), different neural
mechanisms (excitation-inhibition for ILD vs. coincidence detection for
ITD). Consumers must **not** conflate the lateral superior olive with the
medial superior olive.

The Lateral Superior Olive / Cochlear Nuclei Boundary
-----------------------------------------------------
This is the **binaural second-order vs. monaural first-order** boundary:

*   **Lateral superior olive** (this module) — the **binaural second-order
    relay** that **receives** the **ipsilateral excitatory cochlear
    nuclei** input and the **MNTB inhibitory** input and **performs**
    the **ILD computation**.

*   **Cochlear nuclei**
    (``.../vestibulocochlear_nuclei/cochlear_nuclei/``) — the **monaural
    first-order relay** that **receives** the **monaural** auditory
    input from the **ipsilateral cochlea** and **projects** to the
    **LSO** (via the **trapezoid body**).

**They are DIFFERENT STRUCTURES** — the **cochlear nuclei** are
**monaural first-order**; the **LSO** is **binaural second-order**.
Consumers must **not** conflate the lateral superior olive with the
cochlear nuclei.

The Lateral Superior Olive / Trapezoid Body Boundary
----------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Lateral superior olive** (this module) — the **grey-matter neuron
    cluster** that **receives** the trapezoid-body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the **bilateral auditory axons** from the **cochlear
    nuclei** to the **superior olivary complex** (including the LSO).

**They are DIFFERENT STRUCTURES** — the **LSO** is grey matter; the
**trapezoid body** is white matter. Consumers must **not** conflate the
lateral superior olive with the trapezoid body.

The Lateral Superior Olive / Lateral Lemniscus Boundary
-------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Lateral superior olive** (this module) — the **grey-matter neuron
    cluster** that **gives rise to** the lateral lemniscus axons.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the **efferent axons** from the **superior olivary
    complex** (including the LSO) to the **inferior colliculus**.

**They are DIFFERENT STRUCTURES** — the **LSO** is grey matter; the
**lateral lemniscus** is white matter. Consumers must **not** conflate
the lateral superior olive with the lateral lemniscus.

The Lateral Superior Olive / Inferior Colliculus Boundary
---------------------------------------------------------
This is the **pontine binaural relay vs. midbrain downstream relay**
boundary:

*   **Lateral superior olive** (this module) — the **pontine ILD
    processor**.

*   **Inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
    and ``.../right/``) — the **midbrain auditory relay** that
    **receives** the **ascending auditory projections** from the
    **superior olivary complex** (including the LSO) and **projects** to
    the **medial geniculate body**.

**They are DIFFERENT STRUCTURES** — the **LSO** is **pontine** and
**upstream**; the **inferior colliculus** is **midbrain** and
**downstream**. Consumers must **not** conflate the lateral superior
olive with the inferior colliculus.

The Lateral Superior Olive / Medial Geniculate Body Boundary
------------------------------------------------------------
This is the **pontine binaural relay vs. thalamic downstream relay**
boundary:

*   **Lateral superior olive** (this module) — the **pontine ILD
    processor**.

*   **Medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
    and ``.../right/``) — the **thalamic auditory relay** that
    **receives** the **ascending auditory projections** from the
    **inferior colliculus** and **projects** to the **primary auditory
    cortex**.

**They are DIFFERENT STRUCTURES** — the **LSO** is **pontine** and
**upstream**; the **medial geniculate body** is **diencephalic** and
**downstream**. Consumers must **not** conflate the lateral superior
olive with the medial geniculate body.

The Lateral Superior Olive / Primary Auditory Cortex Boundary
-------------------------------------------------------------
This is the **pontine binaural relay vs. cortical downstream target**
boundary:

*   **Lateral superior olive** (this module) — the **pontine ILD
    processor**.

*   **Primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
    42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
    and ``.../right/``) — the **cortical target** of the **ascending
    auditory pathway**.

**They are DIFFERENT STRUCTURES** — the **LSO** is **pontine** and
**upstream**; the **primary auditory cortex** is **cortical** and
**downstream**. Consumers must **not** conflate the lateral superior
olive with the primary auditory cortex.

The Lateral Superior Olive / Facial Nerve Nucleus Boundary
-----------------------------------------------------------
This is the **auditory binaural relay vs. branchial motor** boundary:

*   **Lateral superior olive** (this module) — the **binaural ILD
    processor**.

*   **Facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
    ``.../right/``) — the **branchial motor** nucleus for the **muscles
    of facial expression**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. branchial motor). They are
**anatomically adjacent** — consumers must **not** conflate the lateral
superior olive with the facial nerve nucleus.

The Lateral Superior Olive / Abducens Nucleus Boundary
-------------------------------------------------------
This is the **auditory binaural relay vs. somatic motor** boundary:

*   **Lateral superior olive** (this module) — the **binaural ILD
    processor**.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and
    ``.../right/``) — the **somatic motor** nucleus for the **lateral
    rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. somatic motor). They are
**anatomically adjacent** — consumers must **not** conflate the lateral
superior olive with the abducens nucleus.

The Lateral Superior Olive / Cochlear and Vestibulocochlear Nerves Boundary
---------------------------------------------------------------------------
This is the **central grey matter vs. peripheral white matter** boundary:

*   **Lateral superior olive** (this module) — the **central grey-matter
    binaural ILD processor**.

*   **Cochlear nerve** (the cochlear division of CN VIII) and
    **vestibulocochlear nerve** (CN VIII) — the **peripheral white-matter
    nerves** that **carry** the **primary auditory axons** from the
    **spiral ganglion** to the **cochlear nuclei**.

**They are DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **LSO** is **central grey matter**. Consumers must
**not** conflate the lateral superior olive with the cochlear or
vestibulocochlear nerve.

The Lateral Superior Olive / Whole Superior Olivary Complex Boundary
--------------------------------------------------------------------
This is the **sub-nucleus vs. parent** boundary:

*   **Lateral superior olive** (this module) — the **ILD processor** — one
    of the **three sub-nuclei** of the superior olivary complex.

*   **Superior olivary complex** (``.../superior_olivary_complex/``) —
    the **pontine binaural sound-localization relay** that **contains**
    the **LSO**, the **MSO**, and the **MNTB**.

**The lateral superior olive is a child of the superior olivary
complex.** Consumers must **not** conflate the lateral superior olive
with the **whole superior olivary complex**.

The Lateral Superior Olive / SLEA Boundary
------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Lateral superior olive** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The lateral superior olive is NOT part of the SLEA continuum.** It is a
**binaural auditory ILD processor**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the lateral superior
olive.

Function in the Human Brain
---------------------------
The lateral superior olive's functions are **interaural level difference
(ILD) processing** for **high-frequency horizontal sound localization** —
**NOT a single unified function**:

*   **ILD Computation (Excitation-Inhibition Comparator):** The **LSO**
    is the **two-input coincidence comparator** for **ILD processing**.
    It **receives** the **excitatory ipsilateral cochlear nuclei** input
    (via the **trapezoid body**) and the **inhibitory MNTB** input
    (which itself receives **contralateral cochlear nuclei** input via
    the **trapezoid body**). The **excitation-inhibition** arrangement
    means the **LSO neuron** **fires maximally** when the **ipsilateral
    sound level** is **higher** than the **contralateral sound level**
    — the **LSO neuron** is a **comparator** of the **two ear levels**.

*   **High-Frequency Horizontal Sound Localization:** The **LSO** is the
    **dominant binaural cue** for **high-frequency sound localization**
    (> ~1.5 kHz in humans), because **high-frequency sounds** are
    **shadowed** by the **head** (the **head shadow effect**) — the
    **sound level** at the **near ear** is **higher** than at the **far
    ear**. The **LSO** **computes** this **interaural level difference**
    and **encodes** the **horizontal sound-source location** in its
    **firing rate**.

*   **Human LSO Smaller than MSO (But Retains ILD Function):** In
    **humans**, the **LSO** is **smaller** than in many other mammals
    (especially in **echo-locating bats and rodents**), and the **human
    MSO** is the **dominant binaural sound-localization nucleus** (MSO
    dominates for **ITD** — **low-frequency** sound localization). The
    **human LSO** nevertheless **retains ILD-related function** — it
    **contributes** to **high-frequency horizontal sound
    localization** and to **binaural unmasking** (the ability to detect
    a signal in noise by comparing the two ears).

*   **NOT a neural processor in the classical sense.** The **LSO** is a
    **binaural relay** — it **receives** the **excitatory** and
    **inhibitory** auditory inputs and **performs** the **ILD
    computation** — it **projects** the **binaural representation** to
    the **inferior colliculus** (via the **lateral lemniscus**). The
    **processing** of **binaural sound localization** is **distributed**
    across the **cochlear nuclei** (monaural auditory processing), the
    **LSO** (ILD processing), the **MSO** (ITD processing), the
    **inferior colliculus** (integration of binaural and spectral cues
    and auditory space map), the **medial geniculate body** (thalamic
    relay), and the **primary auditory cortex** (cortical processing).
    The **LSO** is the **ILD processor** — the **brainstem substrate**
    of **high-frequency horizontal sound localization**.

**The unifying theme:** the lateral superior olive is the **binaural ILD
processor** — the **excitation-inhibition comparator** that
**computes** the **interaural level difference** for **high-frequency
horizontal sound localization**. It is a **leaf module** under the
superior_olivary_complex container, a **bilateral single module** at the
tree level, **two-input (excitatory-inhibitory)**, **SLEA-free**, and
**NOT the MNTB** (the **MNTB** is the **inhibitory relay** that
**projects to** the LSO).

Associated Disorders
--------------------
The lateral superior olive has **no named "lateral superior olive
syndrome"** — its clinical associations are **binaural-specific**:

*   **Lateral Superior Olive Lesion — Impaired ILD-Based Sound
    Localization with Preserved Pure-Tone Thresholds:** A lesion of the
    **lateral superior olive** (e.g. **pontine stroke**, **tumor**,
    **demyelination**) causes **impaired ILD-based sound localization**
    (impaired **high-frequency horizontal sound localization**) with
    **preserved pure-tone thresholds** (because the **monaural auditory
    pathway** — the **cochlear nuclei** and the **ascending auditory
    pathway** — is intact). **The ILD-specific pattern** is the
    **substrate** of the **lateral superior olive** function — this is
    the **"ILD-specific binaural deficit"** that **distinguishes** a
    **lateral superior olive lesion** from a **cochlear nuclei lesion**
    (which causes **ipsilateral sensorineural hearing loss**) or a
    **MSO lesion** (which causes **ITD-specific binaural deficit**).

*   **High-Frequency Horizontal Sound Localization Deficit — Lateral
    Superior Olive Involvement:** **High-frequency horizontal sound
    localization** depends on **ILD processing**, which is **subserved**
    by the **lateral superior olive**. **The lateral superior olive** is
    **one of the neural substrates** of **ILD-based sound localization**,
    and its dysfunction may **contribute** to **high-frequency
    horizontal sound localization deficits** — especially in **patients
    with pontine lesions** or **age-related hearing loss** (presbycusis).

*   **Presbycusis — Lateral Superior Olive Involvement:** **Presbycusis**
    (age-related hearing loss) is characterized by **peripheral auditory
    dysfunction** (cochlear hair cell loss) **and central auditory
    dysfunction** (including **lateral superior olive** dysfunction —
    **reduced neuron number**, **reduced synaptic density**, and
    **reduced ILD processing**). The **lateral superior olive** may show
    **age-related changes** — contributing to **impaired high-frequency
    horizontal sound localization** and **impaired speech understanding
    in noise** in **older adults**.

*   **Multiple Sclerosis — Lateral Superior Olive Involvement:**
    **Multiple sclerosis** can affect the **lateral superior olive** (as
    a **brainstem demyelinating lesion**), contributing to **impaired
    ILD-based sound localization** and **binaural hearing deficits**.

*   **Pontine Stroke — Lateral Superior Olive Involvement:** A **pontine
    stroke** (e.g. **basilar artery** perforator territory) involving
    the **lateral superior olive** causes **impaired ILD-based sound
    localization** — often accompanied by **other pontine signs**
    (**hemiparesis**, **facial palsy**, **abducens palsy**, **cerebellar
    ataxia**).

*   **Binaural Hearing Deficit — Lateral Superior Olive Involvement:**
    **Binaural hearing** is the **ability to use** the **differences**
    between the **two ears** to **localize sound** and to **understand
    speech in noise**. **The lateral superior olive** is **one of the
    neural substrates** of **binaural hearing** (specifically **ILD-based
    binaural processing**), and its dysfunction may **contribute** to
    **binaural hearing deficits**.

*   **No Named "Lateral Superior Olive Syndrome":** The lateral superior
    olive is a **single bilateral sub-nucleus** — it has **no named
    clinical syndrome** of its own. Its clinical relevance is
    **ILD-specific** — **impaired ILD-based sound localization**,
    **impaired high-frequency horizontal sound localization**, and
    **impaired binaural hearing**.

**What is NOT here:** The lateral superior olive is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **vestibular neuritis** (vestibular nerve), **labyrinthitis**
(inner ear), or **auditory neuropathy spectrum disorder** (cochlear nerve
or hair cell). Its clinical relevance is **ILD-specific**, via the
**interaural level difference (ILD) processing** it subserves. **No
named lateral superior olive syndrome exists.**

Lateralization Notes
--------------------
This is the **single, bilateral** lateral superior olive module. The LSO
is **bilateral in real anatomy** (left LSO and right LSO), but the tree
wires it as a **single module** — and the module carries **NO warning
at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **lateral_superior_olive** module (here) is a **single module** that
    represents the **bilateral LSO** (left LSO and right LSO). The tree
    does **not** split them into left/right at the tree level. Consumers
    must **not** assume a left/right split exists at the module level —
    the module is a **single, bilateral representation**.

*   **Ipsilateral Excitatory and Contralateral Inhibitory Inputs
    (Structural Fact, NOT a Lateralization Warning):** The **left LSO**
    receives **excitatory input** from the **left cochlear nuclei** (via
    the **trapezoid body**) and **inhibitory input** from the **left
    MNTB** (which itself receives **right cochlear nuclei** input via
    the **trapezoid body**). The **right LSO** receives the **mirror
    inputs**. **This ipsilateral excitatory and contralateral inhibitory
    input** is a **structural fact** of the **ILD-processing
    system** — it is **not** a functional lateralization. It is the
    **neural substrate** of the **ILD computation** in the human brain.

*   **ILD Computation (Structural Fact, NOT a Lateralization Warning):**
    The **LSO neuron** **fires maximally** when the **ipsilateral sound
    level** is **higher** than the **contralateral sound level** —
    because the **excitatory** ipsilateral drive **exceeds** the
    **inhibitory** contralateral drive. **This ILD computation** is a
    **structural fact** of the **binaural sound-localization system** —
    it is **not** a functional lateralization. It is the **neural
    substrate** of **high-frequency horizontal sound localization** in
    the human brain.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The lateral
    superior olive is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the lateral
    superior olive.

*   **NO Amygdala-Lateralization Warning of their own (the LSO is
    BINAURAL AUDITORY, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The lateral superior olive is a **binaural auditory
    ILD processor** — consumers must **not** conflate it with the
    **amygdala** or with the **fear circuit**.

**A consumer that sees "lateral_superior_olive" must understand that the
module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **ipsilateral excitatory and
contralateral inhibitory inputs** and the **ILD computation** are
**structural facts**, not lateralizations. The lateral superior olive is
a **strict-single module with NO warning at the module level** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** LSO as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``,
    ``.../superior_olivary_complex/medial_superior_olive/``,
    ``.../superior_olivary_complex/``, ``.../pons/tegmentum/``,
    ``.../pons/cranial_nerve_nuclei/``, ``.../midbrain/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    LSO's relationships to the **MNTB**, the **MSO**, the **cochlear
    nuclei**, the **trapezoid body**, the **lateral lemniscus**, the
    **inferior colliculus**, the **medial geniculate body**, the
    **primary auditory cortex**, the **facial nerve nucleus**, the
    **abducens nucleus**, the **cochlear** and **vestibulocochlear
    nerves**, the **whole superior olivary complex**, and the **SLEA
    continuum** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **excitatory and
    inhibitory neuron populations** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **BILATERAL SINGLE MODULE — NOT split into left/right at the tree
    level.** The **lateral superior olive** is a **single module** that
    represents the **bilateral LSO** — the tree does **not** split it
    into left/right. Consumers must **not** assume a left/right split
    exists at the module level.
*   **ILD PROCESSOR — NOT the ITD processor.** The **LSO** processes
    **interaural level differences** for **high-frequency horizontal
    sound localization**. The **MSO** processes **interaural time
    differences** for **low-frequency horizontal sound localization**.
    Consumers must **not** conflate the LSO with the MSO.
*   **NOT the MNTB — that is the INHIBITORY RELAY.** The **MNTB** is the
    **inhibitory relay** that **projects to** the LSO. Consumers must
    **not** conflate the LSO with the MNTB.
*   **NOT the cochlear nuclei — those are the UPSTREAM MONAURAL
    FIRST-ORDER RELAY.** Consumers must **not** conflate the LSO with
    the cochlear nuclei.
*   **NOT the trapezoid body or the lateral lemniscus — those are the
    WHITE-MATTER TRACTS.** The **trapezoid body** is the **afferent
    tract**; the **lateral lemniscus** is the **efferent tract**. The
    **LSO** is the **grey-matter neuron cluster** that receives from the
    trapezoid body and projects to the lateral lemniscus.
*   **NOT the inferior colliculus, the medial geniculate body, or the
    primary auditory cortex — those are DOWNSTREAM AUDITORY STRUCTURES.**
    Consumers must **not** conflate the LSO with any of them.
*   **NOT the facial nerve nucleus or the abducens nucleus — those are
    ANATOMICALLY ADJACENT SIBLINGS.** Consumers must **not** conflate the
    LSO with either of them.
*   **NOT the cochlear or vestibulocochlear nerve — those are the
    PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE.** Consumers must
    **not** conflate the LSO with either nerve.
*   **NOT the whole superior olivary complex — that is the PARENT.**
    Consumers must **not** conflate the LSO with the whole superior
    olivary complex.
*   **MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — NOT a single uniform
    nucleus.** The **principal output neurons** (excitatory,
    glutamatergic) and the **inhibitory interneurons** are **prose**, not
    structural children. Consumers must **not** treat the LSO as a
    single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The lateral
    superior olive is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output — the LSO is BINAURAL AUDITORY.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **LSO** is a **binaural auditory ILD processor** — it
    is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The LSO is a local leaf under the
    superior_olivary_complex container, not a cross-listed leaf.
*   **No nested cross-listing.** The LSO has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex import lateral_superior_olive

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex."
        "lateral_superior_olive"
    )

**Do not** assume the lateral superior olive is a **container**. It is a
**leaf** — the **excitatory and inhibitory neuron populations** are
**prose**, not structural children.

**Do not** assume the lateral superior olive is **split into left/right
at the tree level**. The LSO is **bilateral in real anatomy**, but the
tree wires it as a **single module** — there is **no left/right split at
the module level**.

**Do not** assume the lateral superior olive is the **MNTB** or the
**MSO**. The **MNTB** is the **inhibitory relay** (projects to the LSO);
the **MSO** is the **ITD processor**. They are **different structures**.

**Do not** assume the lateral superior olive is the **cochlear nuclei**.
The **cochlear nuclei** are the **monaural first-order relay**; the
**LSO** is the **binaural second-order ILD processor**.

**Do not** assume the lateral superior olive is the **trapezoid body** or
the **lateral lemniscus**. The **trapezoid body** is the **afferent
white-matter tract**; the **lateral lemniscus** is the **efferent
white-matter tract**. The **LSO** is the **grey-matter neuron cluster**
that receives from the trapezoid body and projects to the lateral
lemniscus.

**Do not** assume the lateral superior olive is the **inferior
colliculus**, the **medial geniculate body**, or the **primary auditory
cortex**. Those are the **downstream** auditory relays — the **LSO** is
the **pontine ILD processor**.

**Do not** assume the lateral superior olive is the **facial nerve
nucleus** or the **abducens nucleus**. Those are **anatomically
adjacent siblings** — different functional systems.

**Do not** assume the lateral superior olive is the **cochlear nerve** or
the **vestibulocochlear nerve**. Those are the **peripheral auditory
conduction infrastructure** — the LSO is **central grey matter**.

**Do not** assume the lateral superior olive is the **whole superior
olivary complex**. The **superior olivary complex** is the **parent** —
the **LSO** is one of its **three sub-nuclei**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the lateral superior olive. **The lateral superior olive
is SLEA-FREE** — it is **not** an extended-amygdala component, and it is
**NOT part of the fear circuit**.

Iterating the lateral superior olive's (empty) children (recommended
consumer pattern)::

    LATERAL_SUPERIOR_OLIVE_CHILDREN = ()
    # The lateral superior olive is a leaf. The excitatory and inhibitory
    # neuron populations are prose, not modules.

Reaching the MNTB (recommended consumer pattern — the inhibitory relay
sibling)::

    # The MNTB is the INHIBITORY RELAY sibling under the
    # superior_olivary_complex container:
    #
    #   .../superior_olivary_complex/medial_nucleus_of_trapezoid_body/
    #
    # The MNTB PROJECTS an inhibitory (glycinergic) input to the LSO —
    # the two are FUNCTIONALLY COUPLED but STRUCTURALLY DISTINCT.

Reaching the MSO (recommended consumer pattern — the ITD processor
sibling)::

    # The MSO is the ITD PROCESSOR sibling under the
    # superior_olivary_complex container:
    #
    #   .../superior_olivary_complex/medial_superior_olive/
    #
    # The MSO processes INTERAURAL TIME DIFFERENCES for LOW-FREQUENCY
    # sound localization; the LSO processes INTERAURAL LEVEL DIFFERENCES
    # for HIGH-FREQUENCY sound localization. They are DIFFERENT
    # STRUCTURES with DIFFERENT binaural cues.

Reaching the cochlear nuclei (recommended consumer pattern — the
UPSTREAM monaural first-order relay)::

    # The cochlear nuclei are the MONAURAL FIRST-ORDER relay — they
    # project to the LSO (via the trapezoid body):
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/  (and right/)
    #
    # The cochlear nuclei are UPSTREAM (monaural first-order); the LSO
    # is DOWNSTREAM (binaural second-order ILD processor).

Reaching the trapezoid body (recommended consumer pattern — the
white-matter afferent tract)::

    # The trapezoid body is the WHITE-MATTER afferent tract from the
    # cochlear nuclei to the LSO:
    #
    #   .../white_matter/.../trapezoid_body/  (or equivalent path)
    #
    # The LSO RECEIVES the trapezoid body axons; the trapezoid body is
    # the AFFERENT limb of the ILD-processing pathway.

Reaching the lateral lemniscus (recommended consumer pattern — the
white-matter efferent tract)::

    # The lateral lemniscus is the WHITE-MATTER efferent tract from the
    # LSO to the inferior colliculus:
    #
    #   .../white_matter/.../lateral_lemniscus/  (or equivalent path)
    #
    # The LSO GIVES RISE TO the lateral lemniscus axons; the lateral
    # lemniscus is the EFFERENT limb of the ILD-processing pathway.

Reaching the inferior colliculus (recommended consumer pattern — the
DOWNSTREAM midbrain auditory relay)::

    # The inferior colliculus is the DOWNSTREAM midbrain auditory relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/  (and right/)
    #
    # The LSO is UPSTREAM of the inferior colliculus; the inferior
    # colliculus is DOWNSTREAM of the LSO.

Reaching the whole superior olivary complex (recommended consumer
pattern — the PARENT)::

    # The superior olivary complex is the PONTINE BINAURAL
    # SOUND-LOCALIZATION RELAY parent that CONTAINS the LSO, the MSO,
    # and the MNTB:
    #
    #   .../superior_olivary_complex/
    #
    # The LSO is one of the THREE SUB-NUCLEI of the superior olivary
    # complex.

Bilateral iteration (recommended consumer pattern)::

    # The LSO is a SINGLE module (not split into left/right at the tree
    # level). The module represents the BILATERAL LSO. Any lateralization
    # is a STRUCTURAL FACT (ipsilateral excitatory and contralateral
    # inhibitory inputs), not a lateralization warning.
    lso_path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex."
        "lateral_superior_olive"
    )
    # resolve lso_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The LSO's neuron populations are prose, not modules:
    #   principal output neurons (excitatory, glutamatergic) -> receive
    #       excitatory ipsilateral cochlear nuclei input (via trapezoid
    #       body) and inhibitory MNTB input; project to inferior
    #       colliculus (via lateral lemniscus); the ILD computation
    #       output
    #   inhibitory interneurons (local circuit neurons) -> modulate the
    #       principal output neurons within the LSO
    #
    # Do not attempt to resolve these as sub-paths of the LSO — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical LSO anatomy:** Pickles, J.O. (2015). *An Introduction
    to the Physiology of Hearing*, 4th ed. (Lateral superior olive and
    ILD processing — definitive.)
*   **LSO — ILD processing:** Tollin, D.J. (2003). "The lateral superior
    olive as a source of ascending and descending auditory pathways."
    *Journal of the Association for Research in Otolaryngology*
    4:311–327. (LSO — ILD processing; MNTB inhibition.)
*   **LSO and MNTB — excitation-inhibition:** Smith, P.H., Joris, P.X.,
    Yin, T.C.T. (1998). "Anatomy and physiology of principal cells of
    the medial nucleus of the trapezoid body (MNTB) of the cat."
    *Journal of Neurophysiology* 79:3127–3142. (MNTB — inhibitory relay
    for ILD processing; projects to the LSO.)
*   **Human LSO:** Middlebrooks, J.C. (2015). "Sound localization." In
    *The Auditory System*. (Human LSO — smaller than in other mammals
    but retains ILD function.)
*   **Binaural sound localization — review:** Grothe, B., Pecka, M.,
    McAlpine, D. (2010). "Mechanisms of sound localization and coding
    in mammals." *Physiological Reviews* 90:983–1012. (LSO and MSO —
    ILD and ITD processing.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Lateral superior olive in
    overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An
    Atlas of Structures, Sections, and Systems*, 8th ed. (Lateral
    superior olive and the pontomedullary junction.)
*   **Binaural hearing deficits:** Middlebrooks, J.C., Green, D.M.
    (1991). "Sound localization by human listeners." *Annual Review of
    Psychology* 42:135–159. (Binaural hearing deficits — impaired sound
    localization.)
*   **Presbycusis — LSO involvement:** Frisina, R.D., Walton, J.P.
    (2006). "Age-related structural and functional changes in the
    auditory system." In *Handbook of the Biology of Aging*.
    (Presbycusis — LSO age-related changes.)
*   **Multiple sclerosis — LSO involvement:** Furst, M., Aharonson,
    V., Levine, R.A., et al. (2000). "Sound lateralization in patients
    with unilateral or bilateral multiple sclerosis." *Annals of
    Neurology* 47:389–393. (Multiple sclerosis — LSO involvement;
    binaural hearing deficits.)
*   **Pontine stroke — LSO involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — LSO involvement; binaural hearing
    deficits.)
*   **MSO (contrast — the ITD processor sibling):** Yin, T.C.T., Chan,
    J.C.K. (1990). "Interaural time sensitivity in medial superior
    olive of cat." *Journal of Neurophysiology* 64:465–488. (MSO — ITD
    processing; sibling of the LSO.)
*   **MNTB (contrast — the inhibitory relay sibling):** Smith, P.H.,
    Joris, P.X., Yin, T.C.T. (1998). "Anatomy and physiology of
    principal cells of the medial nucleus of the trapezoid body (MNTB)
    of the cat." *Journal of Neurophysiology* 79:3127–3142. (MNTB —
    inhibitory relay; sibling of the LSO.)
*   **Cochlear nuclei (contrast — the UPSTREAM monaural first-order
    relay):** Cant, N.B., Benson, C.G. (2003). "Parallel auditory
    pathways: projection patterns of the different neuronal populations
    in the cochlear nuclei." *Brain Research Bulletin* 60:457–474.
    (Cochlear nuclei — monaural first-order relay; projects to the
    LSO via the trapezoid body.)
*   **Trapezoid body (contrast — the white-matter afferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Trapezoid body — afferent white-matter tract
    from the cochlear nuclei to the LSO.)
*   **Lateral lemniscus (contrast — the white-matter efferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Lateral lemniscus — efferent white-matter tract
    from the LSO to the inferior colliculus.)
*   **Inferior colliculus (contrast — the midbrain downstream auditory
    relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002). "The
    inferior colliculus: a hub for the central auditory system." In
    *Integrative Functions in the Mammalian Auditory Pathway*. (Inferior
    colliculus — downstream of the LSO.)
*   **Medial geniculate body (contrast — the thalamic downstream
    auditory relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The
    Inferior Colliculus: A Hub for the Central Auditory System*. (Medial
    geniculate body — downstream of the LSO.)
*   **Primary auditory cortex (contrast — the cortical downstream
    auditory target):** Pickles, J.O. (2015). *An Introduction to the
    Physiology of Hearing*, 4th ed. (Primary auditory cortex —
    downstream of the LSO.)
*   **SLEA (contrast — the LSO is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the LSO.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the LSO.)
*   NeuroNames — Lateral superior olive; FMA — Lateral superior olive.
"""
