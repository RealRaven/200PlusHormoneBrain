"""
infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.lateral_superior_olive.right
===========================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── superior_olivary_complex
                └── lateral_superior_olive
                    └── right   <-- THIS MODULE

**Primary synonym:** Right lateral superior olive; right LSO; right
lateral superior olivary nucleus; "the right interaural level difference
(ILD) processor."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nucleus** — an **anatomically delimited
grey-matter nucleus** in the **right lateral superior olivary complex**,
the **principal substrate** of **interaural level difference (ILD)
processing** for **high-frequency horizontal sound localization**.
**Part of:** The **lateral_superior_olive** container — specifically,
the **right half** of the **bilateral LSO**. The
**lateral_superior_olive** container is the **ILD processor** of the
**superior olivary complex**; the **right** sub-container is its
**right-side structural child**.
**Structural parent:** ``.../lateral_superior_olive/`` → **direct child**
of the lateral_superior_olive container.
**Structural children:** **None.** This is a **leaf** module. The
**excitatory (glutamatergic) principal output neurons** and the
**inhibitory (glycinergic) input-receiving neurons** are documented as
**prose**, not as structural children.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
right lateral superior olive is a LEAF, not a container.** It has **no
structural children**. The **excitatory and inhibitory neuron
populations** are **prose** populations, not structural children.
Consumers must **not** treat the right lateral superior olive as a
container, and must **not** assume the neuron populations exist as
sub-modules.
**Boundary status (RIGHT HALF — NOT the whole lateral_superior_olive
container):** **Boundary case — the right lateral superior olive is the
RIGHT HALF of the lateral_superior_olive container, NOT the whole
container.** The **lateral_superior_olive** container
(``.../lateral_superior_olive/``) has **two structural children** —
``left`` and ``right``. The **right** sub-container (here) is the
**right-side** half only. Consumers must **not** conflate the right LSO
with the **whole LSO** — the left side is a **separate structural
sibling**.
**Boundary status (NOT the left lateral superior olive — strict mirror,
no warning):** **Boundary case — the right lateral superior olive is NOT
the left lateral superior olive; the two are a STRICT MIRROR PAIR with
NO warning at the sub-container level.** The **left lateral superior
olive** (``.../lateral_superior_olive/left/``) is the **structurally
identical** left-side counterpart — same neuron populations, same
functional system (ILD processing), same bilateral framing. The two
sides are **strictly mirrored** — any lateralization is documented
**here, in the Lateralization Notes**, not imported from elsewhere.
Consumers must **not** import a lateralization warning into the right
LSO — there is **none at the sub-container level** beyond the
**excitation-inhibition asymmetry** documented below.
**Boundary status (ILD PROCESSOR — NOT the ITD processor):** **Boundary
case — the right lateral superior olive is the ILD PROCESSOR, NOT the
ITD processor.** The **right LSO** processes **interaural level
differences** (ILD) for **high-frequency horizontal sound localization**.
The **medial superior olive (MSO)**
(``.../superior_olivary_complex/medial_superior_olive/right/``) is the
**ITD processor** for **low-frequency horizontal sound localization**.
They are **DIFFERENT STRUCTURES** — different binaural cues (ILD vs.
ITD), different frequency ranges (high vs. low), different neural
mechanisms (excitation-inhibition comparator for ILD vs. coincidence
detector for ITD). **This distinction is functionally load-bearing** —
the two binaural cues dominate at different frequency ranges (ILD above
~1.5 kHz; ITD below ~1.5 kHz in humans). Consumers must **not** conflate
the right LSO with the right MSO.
**Boundary status (NOT the right medial nucleus of the trapezoid body —
that is the INHIBITORY RELAY):** **Boundary case — the right lateral
superior olive is NOT the right medial nucleus of the trapezoid body
(MNTB).** The **right MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/right/``)
is the **inhibitory relay** that **receives** the **left cochlear
nuclei** globular bushy cell projections (via the **trapezoid body**)
and **projects** an **inhibitory (glycinergic)** input to the **right
LSO**. The **right LSO** (here) is the **ILD processor** that
**receives** the **excitatory right cochlear nuclei** input and the
**inhibitory right MNTB** input. They are **DIFFERENT STRUCTURES** —
different functional roles (ILD processing vs. inhibitory relay). **They
are functionally coupled** — the right MNTB **projects to** the right
LSO. Consumers must **not** conflate the right LSO with the right MNTB.
**Boundary status (NOT the left MNTB — that projects to the LEFT LSO):**
**Boundary case — the right lateral superior olive is NOT the left
medial nucleus of the trapezoid body.** The **left MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/``)
**receives** the **right cochlear nuclei** input (via the **trapezoid
body**) and **projects** an **inhibitory (glycinergic)** input to the
**left LSO** — **not** the right LSO. The **right LSO** (here) is the
**ILD processor** that **receives** the **inhibitory right MNTB** input
(not the left MNTB input). They are **DIFFERENT STRUCTURES** — different
targets (left LSO vs. right LSO). Consumers must **not** conflate the
right LSO with the left MNTB.
**Boundary status (TWO-INPUT COMPARATOR — excitatory ipsilateral and
inhibitory contralateral):** **Boundary case — the right lateral
superior olive is a TWO-INPUT COMPARATOR — it receives EXCITATORY input
from the RIGHT cochlear nuclei (ipsilateral) and INHIBITORY input from
the RIGHT MNTB (which itself receives LEFT cochlear nuclei input).** This
**excitation-inhibition** arrangement is the **neural substrate** of
**ILD processing** — the **right LSO neuron** **fires maximally** when
the **right-ear sound level** is **higher** than the **left-ear sound
level** (because the **excitatory** right-ear drive **exceeds** the
**inhibitory** left-ear drive via the right MNTB). **This
ipsilateral-excitatory and contralateral-inhibitory arrangement** is a
**structural fact** of the **right LSO** — it is **not** a
lateralization warning. Consumers must **not** treat the right LSO as a
single-input relay — it is a **two-input comparator** with **distinct
excitatory and inhibitory inputs**.
**Boundary status (NOT the right cochlear nuclei — those are the UPSTREAM
MONAURAL FIRST-ORDER RELAY):** **Boundary case — the right lateral
superior olive is NOT the right cochlear nuclei.** The **right cochlear
nuclei**
(``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/``)
are the **monaural first-order relay** that **receive** the **monaural**
auditory input from the **right cochlea** and **project** to the **right
LSO** (via the **trapezoid body**). The **right LSO** (here) is the
**binaural second-order relay** that **receives** the **excitatory right
cochlear nuclei** projection and the **inhibitory right MNTB**
projection (which itself receives **left cochlear nuclei** input) and
**performs** the **ILD computation**. They are **DIFFERENT STRUCTURES**
— the **cochlear nuclei** are **monaural first-order**; the **right
LSO** is **binaural second-order**. **This distinction is clinically
load-bearing** — a **right cochlear nuclei lesion** causes **right
sensorineural hearing loss**; a **right LSO lesion** causes **impaired
ILD-based sound localization** (specifically, **impaired localization of
high-frequency sounds on the right side**) with **preserved pure-tone
thresholds**. Consumers must **not** conflate the right LSO with the
right cochlear nuclei.
**Boundary status (NOT the trapezoid body — that is the WHITE-MATTER
AFFERENT TRACT):** **Boundary case — the right lateral superior olive is
NOT the trapezoid body.** The **trapezoid body** is the **white-matter
decussating tract** that **carries** the **bilateral auditory axons**
from the **cochlear nuclei** to the **superior olivary complex** — the
**afferent limb** of the **binaural sound-localization pathway**. The
**right LSO** (here) is the **grey-matter neuron cluster** that
**receives** the trapezoid-body axons (via **excitatory** input from the
**right cochlear nuclei** and **inhibitory** input from the **right
MNTB**, which itself receives **left cochlear nuclei** input via the
**trapezoid body**). They are **DIFFERENT STRUCTURES** — the **LSO** is
grey matter; the **trapezoid body** is white matter. Consumers must
**not** conflate the right LSO with the trapezoid body.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
EFFERENT TRACT):** **Boundary case — the right lateral superior olive is
NOT the lateral lemniscus.** The **lateral lemniscus** is the
**white-matter ascending tract** that **carries** the **efferent axons**
from the **superior olivary complex** (including the **right LSO**) to
the **inferior colliculus** (primarily the **right inferior colliculus**,
with **contralateral** projections to the **left inferior colliculus**).
The **right LSO** (here) is the **grey-matter neuron cluster** that
**gives rise to** the lateral lemniscus axons. They are **DIFFERENT
STRUCTURES** — the **LSO** is grey matter; the **lateral lemniscus** is
white matter. Consumers must **not** conflate the right LSO with the
lateral lemniscus.
**Boundary status (NOT the right inferior colliculus — that is the
MIDBRAIN DOWNSTREAM AUDITORY RELAY):** **Boundary case — the right
lateral superior olive is NOT the right inferior colliculus.** The
**right inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/right/inferior_colliculus/``)
is the **midbrain auditory relay** that **receives** the **ascending
auditory projections** from the **superior olivary complex** (including
the **right LSO**) and **projects** to the **right medial geniculate
body**. The **right LSO** (here) is the **pontine ILD processor** — it
is **upstream** of the right inferior colliculus. They are **DIFFERENT
STRUCTURES** — the **right LSO** is **pontine** and **upstream**; the
**right inferior colliculus** is **midbrain** and **downstream**.
Consumers must **not** conflate the right LSO with the right inferior
colliculus.
**Boundary status (NOT the right medial geniculate body — that is the
THALAMIC DOWNSTREAM AUDITORY RELAY):** **Boundary case — the right
lateral superior olive is NOT the right medial geniculate body.** The
**right medial geniculate body**
(``.../diencephalon/thalamus/right/metathalamus/medial_geniculate_body/``)
is the **thalamic auditory relay** that **receives** the **ascending
auditory projections** from the **right inferior colliculus** and
**projects** to the **right primary auditory cortex**. The **right LSO**
(here) is the **pontine ILD processor** — it is **upstream** of the
right medial geniculate body. They are **DIFFERENT STRUCTURES** — the
**right LSO** is **pontine** and **upstream**; the **right medial
geniculate body** is **diencephalic** and **downstream**. Consumers must
**not** conflate the right LSO with the right medial geniculate body.
**Boundary status (NOT the right primary auditory cortex — that is the
CORTICAL DOWNSTREAM AUDITORY TARGET):** **Boundary case — the right
lateral superior olive is NOT the right primary auditory cortex.** The
**right primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
42)
(``.../cerebral_hemispheres/right/cortex/temporal/cortex/primary_auditory_cortex/``)
is the **cortical target** of the **ascending auditory pathway**. The
**right LSO** (here) is the **pontine ILD processor** — it is
**upstream** of the right primary auditory cortex. They are **DIFFERENT
STRUCTURES** — the **right LSO** is **pontine** and **upstream**; the
**right primary auditory cortex** is **cortical** and **downstream**.
Consumers must **not** conflate the right LSO with the right primary
auditory cortex.
**Boundary status (NOT the right facial nerve nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the right lateral
superior olive is NOT the right facial nerve nucleus.** The **right
facial nerve nucleus**
(``.../cranial_nerve_nuclei/right/facial_nerve_nucleus/``) is the
**branchial motor** nucleus for the **right muscles of facial
expression**. The **right LSO** (here) is the **binaural ILD processor**.
They are **DIFFERENT STRUCTURES** — different functional systems
(branchial motor vs. binaural ILD processing). They are **anatomically
adjacent** (both are in the **right ventral pontine tegmentum**) — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the right LSO with the right facial nerve nucleus.
**Boundary status (NOT the right abducens nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the right lateral
superior olive is NOT the right abducens nucleus.** The **right abducens
nucleus** (``.../cranial_nerve_nuclei/right/abducens_nucleus/``) is the
**somatic motor** nucleus for the **right lateral rectus**. The **right
LSO** (here) is the **binaural ILD processor**. They are **DIFFERENT
STRUCTURES** — different functional systems (somatic motor vs. binaural
ILD processing). They are **anatomically adjacent** — the **right LSO**
is **near the genu of the right facial nerve** and the **right abducens
nucleus**; this proximity is a **classic source of confusion** —
consumers must **not** conflate the right LSO with the right abducens
nucleus.
**Boundary status (NOT the right cochlear nerve or the right
vestibulocochlear nerve — those are the PERIPHERAL AUDITORY CONDUCTION
INFRASTRUCTURE):** **Boundary case — the right lateral superior olive is
NOT the right cochlear nerve or the right vestibulocochlear nerve.** The
**right cochlear nerve** (the cochlear division of right CN VIII) and
the **right vestibulocochlear nerve** (right CN VIII) are the
**white-matter peripheral nerves** that **carry** the **primary auditory
axons** from the **right spiral ganglion** to the **right cochlear
nuclei**. The **right LSO** (here) is the **central grey-matter binaural
ILD processor**. They are **DIFFERENT STRUCTURES** — the **nerves** are
**peripheral white matter**; the **right LSO** is **central grey
matter**. Consumers must **not** conflate the right LSO with the right
cochlear or right vestibulocochlear nerve.
**Boundary status (NOT the whole lateral_superior_olive container — that
is the PARENT):** **Boundary case — the right lateral superior olive is
NOT the whole lateral_superior_olive container; the
lateral_superior_olive container is the PARENT.** The
**lateral_superior_olive** container (``.../lateral_superior_olive/``)
is the **bilateral ILD processor** — it **contains** the **right LSO**
(here) and the **left LSO**. The **right LSO** is the **right half** of
the lateral_superior_olive container. Consumers must **not** conflate
the right LSO with the **whole LSO**.
**Boundary status (NOT the whole superior_olivary_complex container —
that is the GRANDPARENT):** **Boundary case — the right lateral superior
olive is NOT the whole superior_olivary_complex container; the
superior_olivary_complex container is the GRANDPARENT.** The
**superior_olivary_complex** container
(``.../superior_olivary_complex/``) is the **pontine binaural
sound-localization relay** — it **contains** the **LSO**, the **MSO**,
and the **MNTB**. The **right LSO** is **one of the sub-nuclei** of the
superior olivary complex. Consumers must **not** conflate the right LSO
with the **whole superior olivary complex**.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
functionally distinct populations):** **Boundary case — the right
lateral superior olive is NOT a single uniform neuron population; it
contains MULTIPLE functionally distinct populations.** The **principal
output neurons** — the **excitatory (glutamatergic)** projection neurons
that **receive** the **excitatory right cochlear nuclei** input and the
**inhibitory right MNTB** input, and **project** to the **right inferior
colliculus** (via the **lateral lemniscus**) — they are the **ILD
computation** output. The **inhibitory interneurons** — the **local
circuit neurons** that **modulate** the **principal output neurons**.
**These populations are prose, not structural children.** Consumers must
**not** treat the right LSO as a single uniform population — it is a
**functionally heterogeneous nucleus** with **distinct** sub-circuits.
**Boundary status (SLEA-FREE — the right lateral superior olive is NOT an
extended-amygdala component):** **Boundary case — the right lateral
superior olive is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala) and to
the **BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **right LSO** is a **binaural auditory ILD processor** —
it is **NOT** an extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into the right
LSO — it is **SLEA-free**.

Overview
--------
The right lateral superior olive is the **right half** of the **bilateral
LSO** — the **right grey-matter neuron cluster** in the **right superior
olivary complex** that is the **principal substrate** of **interaural
level difference (ILD) processing** for **high-frequency horizontal
sound localization**. It is a **leaf** module under the ``right``
sub-container of the lateral_superior_olive container, and it is the
**right ILD processor** — the **right LSO** that **compares** the
**right-ear sound level** (excitatory input) with the **left-ear sound
level** (inhibitory input via the right MNTB).

**The right lateral superior olive is a LEAF, not a container.** It has
**no structural children**. The **excitatory and inhibitory neuron
populations** are **prose populations**, not structural children.

**The right lateral superior olive is the RIGHT HALF of the
lateral_superior_olive container, NOT the whole container.** The
**lateral_superior_olive** container has **two structural children** —
``left`` and ``right``. The **right** sub-container (here) is the
**right-side** half only.

**The right lateral superior olive and the left lateral superior olive
are a STRICT MIRROR PAIR with NO warning at the sub-container level.**
The two sides are **structurally identical** — same neuron populations,
same functional system (ILD processing), same bilateral framing.

**The right lateral superior olive is the ILD PROCESSOR, not the ITD
processor.** The **right LSO** processes **interaural level differences**
for **high-frequency horizontal sound localization**. The **right MSO**
processes **interaural time differences** for **low-frequency horizontal
sound localization**.

**The right lateral superior olive is a TWO-INPUT COMPARATOR.** It
receives **excitatory** input from the **right cochlear nuclei** and
**inhibitory** input from the **right MNTB** (which itself receives
**left cochlear nuclei** input). The **right LSO** **fires maximally**
when the **right-ear sound level** is **higher** than the **left-ear
sound level** — it signals **"sound on the right."**

**The right lateral superior olive is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The right lateral superior olive contains **multiple functionally
distinct neuron populations** — documented as **prose**, not as
structural children:

*   **Principal output neurons** — the **excitatory (glutamatergic)**
    projection neurons that **receive** the **excitatory right cochlear
    nuclei** input (via the **trapezoid body**) and the **inhibitory
    right MNTB** input (via the **glycinergic** projection from the
    **right MNTB**, which itself receives **left cochlear nuclei** input
    via the **trapezoid body**). They **project** to the **right
    inferior colliculus** (primarily, via the **lateral lemniscus**)
    and to the **left inferior colliculus** (contralaterally, to a
    lesser extent). They are the **ILD computation** output — they
    **fire maximally** when the **right-ear sound level** is **higher**
    than the **left-ear sound level** (because the **excitatory**
    right-ear drive **exceeds** the **inhibitory** left-ear drive).

*   **Inhibitory interneurons** — the **local circuit neurons** that
    **modulate** the **principal output neurons** within the right LSO.
    They are **prose** populations, not structural children.

**These populations are prose, not structural children.** The tree wires
the **right lateral superior olive** as a **single leaf** under the
``right`` sub-container of the lateral_superior_olive container — the
**excitatory and inhibitory neuron populations** are **prose**, not
structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Right LSO / Left LSO Boundary
---------------------------------
This is the **strict-mirror** boundary:

*   **Right lateral superior olive** (this module) — the **right-side**
    LSO — the **right ILD processor**.

*   **Left lateral superior olive**
    (``.../lateral_superior_olive/left/``) — the **structurally
    identical** left-side LSO — the **left ILD processor**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same neuron
populations, same functional system (ILD processing), same bilateral
framing. Any lateralization is documented **here, in the Lateralization
Notes**, not imported from elsewhere. Consumers must **not** import a
lateralization warning into the right LSO — there is **none at the
sub-container level** beyond the **excitation-inhibition asymmetry**
documented below.

The Right LSO / Lateral Superior Olive Container Boundary
---------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Right lateral superior olive** (this module) — the **right-side**
    half of the bilateral LSO.

*   **Lateral superior olive container** (``.../lateral_superior_olive/``)
    — the **whole bilateral LSO**, with **two structural children**
    (``left`` and ``right``).

**The right lateral superior olive is a child of the
lateral_superior_olive container.** Consumers must **not** conflate the
right half with the **whole LSO** — the left side is a **separate
structural sibling**.

The Right LSO / Right MSO Boundary
----------------------------------
This is the **sibling** boundary — **ILD processor vs. ITD processor**:

*   **Right lateral superior olive** (this module) — the **right ILD
    processor** for **high-frequency horizontal sound localization**.

*   **Right medial superior olive (MSO)**
    (``.../superior_olivary_complex/medial_superior_olive/right/``) — the
    **right ITD processor** for **low-frequency horizontal sound
    localization**.

**They are DIFFERENT STRUCTURES** — different binaural cues (ILD vs.
ITD), different frequency ranges (high vs. low), different neural
mechanisms (excitation-inhibition for ILD vs. coincidence detection for
ITD). Consumers must **not** conflate the right LSO with the right MSO.

The Right LSO / Right MNTB Boundary
-----------------------------------
This is the **sibling** boundary — **ILD processor vs. inhibitory
relay**:

*   **Right lateral superior olive** (this module) — the **right ILD
    processor** that **receives** the **inhibitory right MNTB** input.

*   **Right medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/right/``)
    — the **right inhibitory relay** that **receives** the **left
    cochlear nuclei** input and **projects** the **inhibitory
    (glycinergic)** input to the **right LSO**.

**They are DIFFERENT STRUCTURES** — different functional roles (ILD
processing vs. inhibitory relay). **They are functionally coupled** —
the right MNTB **projects to** the right LSO. Consumers must **not**
conflate the right LSO with the right MNTB.

The Right LSO / Left MNTB Boundary
----------------------------------
This is the **wrong-target** boundary:

*   **Right lateral superior olive** (this module) — the **right ILD
    processor** that **receives** the **inhibitory right MNTB** input
    (not the left MNTB input).

*   **Left medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/``)
    — the **left inhibitory relay** that **projects** to the **left
    LSO** — **not** the right LSO.

**They are DIFFERENT STRUCTURES** — different targets (left LSO vs.
right LSO). Consumers must **not** conflate the right LSO with the left
MNTB.

The Right LSO / Right Cochlear Nuclei Boundary
----------------------------------------------
This is the **binaural second-order vs. monaural first-order** boundary:

*   **Right lateral superior olive** (this module) — the **right binaural
    second-order relay** that **receives** the **excitatory right
    cochlear nuclei** input and the **inhibitory right MNTB** input and
    **performs** the **ILD computation**.

*   **Right cochlear nuclei**
    (``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/``)
    — the **right monaural first-order relay** that **receives** the
    **monaural** auditory input from the **right cochlea** and
    **projects** to the **right LSO** (via the **trapezoid body**).

**They are DIFFERENT STRUCTURES** — the **right cochlear nuclei** are
**monaural first-order**; the **right LSO** is **binaural second-order**.
**This distinction is clinically load-bearing** — a **right cochlear
nuclei lesion** causes **right sensorineural hearing loss**; a **right
LSO lesion** causes **impaired ILD-based sound localization**
(specifically, **impaired localization of high-frequency sounds on the
right side**) with **preserved pure-tone thresholds**. Consumers must
**not** conflate the right LSO with the right cochlear nuclei.

The Right LSO / Trapezoid Body Boundary
---------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Right lateral superior olive** (this module) — the **grey-matter
    neuron cluster** that **receives** the trapezoid-body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the **bilateral auditory axons** from the **cochlear
    nuclei** to the **superior olivary complex** (including the right
    LSO).

**They are DIFFERENT STRUCTURES** — the **LSO** is grey matter; the
**trapezoid body** is white matter. Consumers must **not** conflate the
right LSO with the trapezoid body.

The Right LSO / Lateral Lemniscus Boundary
------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Right lateral superior olive** (this module) — the **grey-matter
    neuron cluster** that **gives rise to** the lateral lemniscus axons.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the **efferent axons** from the **superior olivary
    complex** (including the right LSO) to the **inferior colliculus**.

**They are DIFFERENT STRUCTURES** — the **LSO** is grey matter; the
**lateral lemniscus** is white matter. Consumers must **not** conflate
the right LSO with the lateral lemniscus.

The Right LSO / Right Inferior Colliculus Boundary
--------------------------------------------------
This is the **pontine ILD processor vs. midbrain downstream relay**
boundary:

*   **Right lateral superior olive** (this module) — the **right pontine
    ILD processor**.

*   **Right inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/right/inferior_colliculus/``)
    — the **right midbrain auditory relay** that **receives** the
    **ascending auditory projections** from the **superior olivary
    complex** (including the right LSO) and **projects** to the **right
    medial geniculate body**.

**They are DIFFERENT STRUCTURES** — the **right LSO** is **pontine** and
**upstream**; the **right inferior colliculus** is **midbrain** and
**downstream**. Consumers must **not** conflate the right LSO with the
right inferior colliculus.

The Right LSO / Right Medial Geniculate Body Boundary
-----------------------------------------------------
This is the **pontine ILD processor vs. thalamic downstream relay**
boundary:

*   **Right lateral superior olive** (this module) — the **right pontine
    ILD processor**.

*   **Right medial geniculate body**
    (``.../diencephalon/thalamus/right/metathalamus/medial_geniculate_body/``)
    — the **right thalamic auditory relay** that **receives** the
    **ascending auditory projections** from the **right inferior
    colliculus** and **projects** to the **right primary auditory
    cortex**.

**They are DIFFERENT STRUCTURES** — the **right LSO** is **pontine** and
**upstream**; the **right medial geniculate body** is **diencephalic**
and **downstream**. Consumers must **not** conflate the right LSO with
the right medial geniculate body.

The Right LSO / Right Primary Auditory Cortex Boundary
------------------------------------------------------
This is the **pontine ILD processor vs. cortical downstream target**
boundary:

*   **Right lateral superior olive** (this module) — the **right pontine
    ILD processor**.

*   **Right primary auditory cortex** (Heschl's gyrus, Brodmann areas 41
    and 42)
    (``.../cerebral_hemispheres/right/cortex/temporal/cortex/primary_auditory_cortex/``)
    — the **right cortical target** of the **ascending auditory
    pathway**.

**They are DIFFERENT STRUCTURES** — the **right LSO** is **pontine** and
**upstream**; the **right primary auditory cortex** is **cortical** and
**downstream**. Consumers must **not** conflate the right LSO with the
right primary auditory cortex.

The Right LSO / Right Facial Nerve Nucleus Boundary
---------------------------------------------------
This is the **auditory binaural relay vs. branchial motor** boundary:

*   **Right lateral superior olive** (this module) — the **right binaural
    ILD processor**.

*   **Right facial nerve nucleus**
    (``.../cranial_nerve_nuclei/right/facial_nerve_nucleus/``) — the
    **branchial motor** nucleus for the **right muscles of facial
    expression**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. branchial motor). They are
**anatomically adjacent** — consumers must **not** conflate the right
LSO with the right facial nerve nucleus.

The Right LSO / Right Abducens Nucleus Boundary
-----------------------------------------------
This is the **auditory binaural relay vs. somatic motor** boundary:

*   **Right lateral superior olive** (this module) — the **right binaural
    ILD processor**.

*   **Right abducens nucleus**
    (``.../cranial_nerve_nuclei/right/abducens_nucleus/``) — the
    **somatic motor** nucleus for the **right lateral rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. somatic motor). They are
**anatomically adjacent** — consumers must **not** conflate the right
LSO with the right abducens nucleus.

The Right LSO / Right Cochlear and Vestibulocochlear Nerves Boundary
--------------------------------------------------------------------
This is the **central grey matter vs. peripheral white matter** boundary:

*   **Right lateral superior olive** (this module) — the **central
    grey-matter binaural ILD processor**.

*   **Right cochlear nerve** (the cochlear division of right CN VIII) and
    **right vestibulocochlear nerve** (right CN VIII) — the **peripheral
    white-matter nerves** that **carry** the **primary auditory axons**
    from the **right spiral ganglion** to the **right cochlear nuclei**.

**They are DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **right LSO** is **central grey matter**. Consumers
must **not** conflate the right LSO with the right cochlear or right
vestibulocochlear nerve.

The Right LSO / Whole Lateral Superior Olive Container Boundary
---------------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Right lateral superior olive** (this module) — the **right-side**
    half of the lateral_superior_olive container.

*   **Lateral superior olive container** (``.../lateral_superior_olive/``)
    — the **whole bilateral LSO**, with **two structural children**
    (``left`` and ``right``).

**The right lateral superior olive is a child of the
lateral_superior_olive container.** Consumers must **not** conflate the
right LSO with the **whole LSO**.

The Right LSO / Whole Superior Olivary Complex Container Boundary
-----------------------------------------------------------------
This is the **sub-nucleus vs. grandparent** boundary:

*   **Right lateral superior olive** (this module) — the **right LSO** —
    one of the sub-nuclei of the superior olivary complex.

*   **Superior olivary complex container**
    (``.../superior_olivary_complex/``) — the **pontine binaural
    sound-localization relay** that **contains** the **LSO**, the
    **MSO**, and the **MNTB**.

**The right LSO is a great-grandchild of the superior olivary complex**
(via the lateral_superior_olive container). Consumers must **not**
conflate the right LSO with the **whole superior olivary complex**.

The Right LSO / SLEA Boundary
-----------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Right lateral superior olive** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The right lateral superior olive is NOT part of the SLEA continuum.**
It is a **binaural auditory ILD processor**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the right
LSO.

Function in the Human Brain
---------------------------
The right lateral superior olive's functions are **interaural level
difference (ILD) processing** for **high-frequency horizontal sound
localization** — **NOT a single unified function**:

*   **ILD Computation (Excitation-Inhibition Comparator):** The **right
    LSO** is the **two-input comparator** for **ILD processing**. It
    **receives** the **excitatory right cochlear nuclei** input (via the
    **trapezoid body**) and the **inhibitory right MNTB** input (which
    itself receives **left cochlear nuclei** input via the **trapezoid
    body**). The **excitation-inhibition** arrangement means the
    **right LSO neuron** **fires maximally** when the **right-ear sound
    level** is **higher** than the **left-ear sound level** — the
    **right LSO neuron** is a **comparator** of the **right-ear level**
    (excitation) against the **left-ear level** (inhibition).

*   **Right-Sided High-Frequency Horizontal Sound Localization:** The
    **right LSO** is the **dominant binaural cue** for **high-frequency
    sound localization** (> ~1.5 kHz in humans) of **sound sources on
    the right side** — because **high-frequency sounds** are **shadowed**
    by the **head** (the **head shadow effect**), the **right-ear sound
    level** is **higher** than the **left-ear sound level** when the
    sound source is on the **right side**, and the **right LSO** is
    **maximally excited** — it signals **"sound on the right."**

*   **Human LSO Smaller than MSO (But Retains ILD Function):** In
    **humans**, the **LSO** is **smaller** than in many other mammals
    (especially in **echo-locating bats and rodents**), and the **human
    MSO** is the **dominant binaural sound-localization nucleus** (MSO
    dominates for **ITD** — **low-frequency** sound localization). The
    **human LSO** nevertheless **retains ILD-related function** — it
    **contributes** to **high-frequency horizontal sound
    localization** and to **binaural unmasking** (the ability to detect
    a signal in noise by comparing the two ears).

*   **NOT a neural processor in the classical sense.** The **right LSO**
    is a **binaural relay** — it **receives** the **excitatory** and
    **inhibitory** auditory inputs and **performs** the **ILD
    computation** — it **projects** the **binaural representation** to
    the **right inferior colliculus** (primarily, via the **lateral
    lemniscus**) and to the **left inferior colliculus**
    (contralaterally, to a lesser extent). The **processing** of
    **binaural sound localization** is **distributed** across the
    **cochlear nuclei** (monaural auditory processing), the **right
    LSO** (ILD processing), the **right MSO** (ITD processing), the
    **inferior colliculus** (integration of binaural and spectral cues
    and auditory space map), the **medial geniculate body** (thalamic
    relay), and the **primary auditory cortex** (cortical processing).
    The **right LSO** is the **right ILD processor** — the **brainstem
    substrate** of **right-sided high-frequency horizontal sound
    localization**.

**The unifying theme:** the right lateral superior olive is the **right
binaural ILD processor** — the **excitation-inhibition comparator** that
**computes** the **interaural level difference** for **high-frequency
horizontal sound localization** on the **right side**. It is a **leaf
module** under the ``right`` sub-container of the
lateral_superior_olive container, **two-input (excitatory-inhibitory)**,
**SLEA-free**, and **NOT the right MNTB** (the **right MNTB** is the
**inhibitory relay** that **projects to** the right LSO).

Associated Disorders
--------------------
The right lateral superior olive has **no named "right lateral superior
olive syndrome"** — its clinical associations are **binaural-specific**:

*   **Right LSO Lesion — Impaired ILD-Based Sound Localization on the
    Right with Preserved Pure-Tone Thresholds:** A lesion of the **right
    lateral superior olive** (e.g. **pontine stroke**, **tumor**,
    **demyelination**) causes **impaired ILD-based sound localization**
    — specifically, **impaired localization of high-frequency sounds on
    the right side** — with **preserved pure-tone thresholds** (because
    the **monaural auditory pathway** — the **cochlear nuclei** and the
    **ascending auditory pathway** — is intact). **The ILD-specific
    pattern** is the **substrate** of the **right LSO** function — this
    is the **"right ILD-specific binaural deficit"** that
    **distinguishes** a **right LSO lesion** from a **right cochlear
    nuclei lesion** (which causes **right sensorineural hearing loss**)
    or a **right MSO lesion** (which causes **right ITD-specific
    binaural deficit**).

*   **High-Frequency Right-Sided Sound Localization Deficit — Right LSO
    Involvement:** **High-frequency horizontal sound localization** on
    the **right side** depends on **ILD processing**, which is
    **subserved** by the **right LSO**. **The right LSO** is **one of
    the neural substrates** of **right ILD-based sound localization**,
    and its dysfunction may **contribute** to **high-frequency
    right-sided sound localization deficits** — especially in **patients
    with right pontine lesions** or **age-related hearing loss**
    (presbycusis).

*   **Presbycusis — Right LSO Involvement:** **Presbycusis** (age-related
    hearing loss) is characterized by **peripheral auditory dysfunction**
    (cochlear hair cell loss) **and central auditory dysfunction**
    (including **right LSO** dysfunction — **reduced neuron number**,
    **reduced synaptic density**, and **reduced ILD processing**). The
    **right LSO** may show **age-related changes** — contributing to
    **impaired right-sided high-frequency horizontal sound localization**
    and **impaired speech understanding in noise** in **older adults**.

*   **Multiple Sclerosis — Right LSO Involvement:** **Multiple
    sclerosis** can affect the **right LSO** (as a **right brainstem
    demyelinating lesion**), contributing to **impaired right ILD-based
    sound localization** and **right binaural hearing deficits**.

*   **Right Pontine Stroke — Right LSO Involvement:** A **right pontine
    stroke** (e.g. **basilar artery** perforator territory) involving
    the **right LSO** causes **impaired right ILD-based sound
    localization** — often accompanied by **other right pontine signs**
    (**left hemiparesis**, **right facial palsy**, **right abducens
    palsy**, **left cerebellar ataxia**).

*   **Binaural Hearing Deficit — Right LSO Involvement:** **Binaural
    hearing** is the **ability to use** the **differences** between the
    **two ears** to **localize sound** and to **understand speech in
    noise**. **The right LSO** is **one of the neural substrates** of
    **binaural hearing** (specifically **right ILD-based binaural
    processing**), and its dysfunction may **contribute** to **right
    binaural hearing deficits**.

*   **No Named "Right LSO Syndrome":** The right LSO is a **single
    bilateral sub-nucleus** — it has **no named clinical syndrome** of
    its own. Its clinical relevance is **ILD-specific** — **impaired
    right ILD-based sound localization**, **impaired right-sided
    high-frequency horizontal sound localization**, and **impaired right
    binaural hearing**.

**What is NOT here:** The right LSO is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **vestibular neuritis** (vestibular nerve), **labyrinthitis**
(inner ear), or **auditory neuropathy spectrum disorder** (cochlear nerve
or hair cell). Its clinical relevance is **ILD-specific**, via the
**interaural level difference (ILD) processing** it subserves on the
**right side**. **No named right LSO syndrome exists.**

Lateralization Notes
--------------------
This is the **right** lateral superior olive module. The right LSO is
**bilaterally symmetric** with the left LSO and **strictly mirrored** —
and it carries **NO warning at the sub-container level**:

*   **Strict Bilateral Symmetry:** The **right** and **left** LSO are
    **structurally identical** — same neuron populations, same functional
    system (ILD processing), same bilateral framing. The bilateral
    symmetry is **strict**.

*   **Ipsilateral Excitatory and Contralateral Inhibitory Inputs
    (Structural Fact, NOT a Lateralization Warning):** The **right LSO**
    receives **excitatory input** from the **right cochlear nuclei** (via
    the **trapezoid body**) and **inhibitory input** from the **right
    MNTB** (which itself receives **left cochlear nuclei** input via the
    **trapezoid body**). **This ipsilateral excitatory and contralateral
    inhibitory input** is a **structural fact** of the **ILD-processing
    system** — it is **not** a functional lateralization. It is the
    **neural substrate** of the **ILD computation** in the **right
    LSO** — the **right LSO** **compares** the **right-ear sound level**
    (excitation) with the **left-ear sound level** (inhibition via the
    right MNTB).

*   **Right-Sided ILD Computation (Structural Fact, NOT a
    Lateralization Warning):** The **right LSO neuron** **fires
    maximally** when the **right-ear sound level** is **higher** than the
    **left-ear sound level** — because the **excitatory** right-ear
    drive **exceeds** the **inhibitory** left-ear drive. **This ILD
    computation** is a **structural fact** of the **binaural
    sound-localization system** — it is **not** a functional
    lateralization. It is the **neural substrate** of **right-sided
    high-frequency horizontal sound localization** in the human brain.

*   **Ipsilateral and Contralateral Inferior Colliculus Projections
    (Structural Fact, NOT a Lateralization Warning):** The **right LSO**
    **projects** to the **right inferior colliculus** (ipsilateral,
    primarily, via the **lateral lemniscus**) and to the **left inferior
    colliculus** (contralaterally, to a lesser extent). **This
    ipsilateral and contralateral projection** is a **structural fact**
    of the **ascending auditory system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **bilateral
    inferior colliculus representation** of **right-sided sound-source
    location**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The right LSO is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the right LSO.

*   **NO Amygdala-Lateralization Warning of their own (the right LSO is
    BINAURAL AUDITORY, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The right LSO is a **binaural auditory ILD
    processor** — consumers must **not** conflate it with the
    **amygdala** or with the **fear circuit**. **Note**: the
    "right-amygdala" lateralization is about the **amygdala**, not about
    this right pontine auditory nucleus — do not import it.

**A consumer that assumes "right LSO = left LSO" will be structurally
correct** — the two sides are **strictly symmetric** (the ipsilateral
excitatory and contralateral inhibitory inputs and the right-sided ILD
computation are structural facts, not lateralizations). The right LSO is
a **strict-mirror pair with NO warning at the sub-container level** —
**no SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right sub-container is the
    **right half**; it does **not** import the left sub-container at
    module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../lateral_superior_olive/left/``,
    ``.../superior_olivary_complex/medial_superior_olive/``,
    ``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``,
    ``.../superior_olivary_complex/``, ``.../pons/tegmentum/``,
    ``.../pons/cranial_nerve_nuclei/``, ``.../midbrain/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    right LSO's relationships to the **right MNTB**, the **left MNTB**,
    the **right MSO**, the **right cochlear nuclei**, the **trapezoid
    body**, the **lateral lemniscus**, the **right inferior colliculus**,
    the **right medial geniculate body**, the **right primary auditory
    cortex**, the **right facial nerve nucleus**, the **right abducens
    nucleus**, the **right cochlear** and **right vestibulocochlear
    nerves**, the **whole lateral superior olive container**, the
    **whole superior olivary complex container**, and the **SLEA
    continuum** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **excitatory and
    inhibitory neuron populations** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **RIGHT HALF — NOT the whole lateral_superior_olive container.** The
    **lateral_superior_olive** container has **two structural children**
    — ``left`` and ``right``. The **right** sub-container (here) is the
    **right-side** half only.
*   **STRICT MIRROR with the left LSO — NO warning at the sub-container
    level.** The **right** and **left** LSO are **structurally
    identical**. Any lateralization is documented **here, in the
    Lateralization Notes**.
*   **ILD PROCESSOR — NOT the ITD processor (MSO).** The **right LSO**
    processes **interaural level differences**; the **right MSO**
    processes **interaural time differences**. Consumers must **not**
    conflate the two.
*   **NOT the right MNTB — that is the INHIBITORY RELAY.** The **right
    MNTB** **projects to** the right LSO. Consumers must **not** conflate
    the two.
*   **NOT the left MNTB — that projects to the LEFT LSO.** Consumers must
    **not** conflate the right LSO with the left MNTB.
*   **NOT the right cochlear nuclei — those are the UPSTREAM MONAURAL
    FIRST-ORDER RELAY.** Consumers must **not** conflate the right LSO
    with the right cochlear nuclei.
*   **NOT the trapezoid body or the lateral lemniscus — those are the
    WHITE-MATTER TRACTS.** Consumers must **not** conflate the right LSO
    with either tract.
*   **NOT the right inferior colliculus, the right medial geniculate
    body, or the right primary auditory cortex — those are DOWNSTREAM
    AUDITORY STRUCTURES.** Consumers must **not** conflate the right LSO
    with any of them.
*   **NOT the right facial nerve nucleus or the right abducens nucleus —
    those are ANATOMICALLY ADJACENT SIBLINGS.** Consumers must **not**
    conflate the right LSO with either of them.
*   **NOT the right cochlear or right vestibulocochlear nerve — those are
    the PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE.** Consumers must
    **not** conflate the right LSO with either nerve.
*   **NOT the whole lateral_superior_olive container — that is the
    PARENT.** Consumers must **not** conflate the right LSO with the
    whole LSO.
*   **NOT the whole superior_olivary_complex container — that is the
    GRANDPARENT.** Consumers must **not** conflate the right LSO with the
    whole superior olivary complex.
*   **MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — NOT a single uniform
    nucleus.** The **principal output neurons** (excitatory,
    glutamatergic) and the **inhibitory interneurons** are **prose**, not
    structural children. Consumers must **not** treat the right LSO as a
    single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The right LSO is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.
*   **NOT the fear-output — the right LSO is BINAURAL AUDITORY.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **right LSO** is a **binaural auditory ILD processor**
    — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The right LSO is a local leaf under the
    ``right`` sub-container of the lateral_superior_olive container, not
    a cross-listed leaf.
*   **No nested cross-listing.** The right LSO has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.lateral_superior_olive import right

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex."
        "lateral_superior_olive.right"
    )

**Do not** assume the right LSO is a **container**. It is a **leaf** —
the **excitatory and inhibitory neuron populations** are **prose**, not
structural children.

**Do not** assume the right LSO is the **whole lateral_superior_olive
container**. It is the **right-side half only** — the left side is a
**separate structural sibling**.

**Do not** assume the right LSO is the **left LSO**. The two are a
**strict mirror pair with NO warning at the sub-container level** — any
lateralization is documented **here, in the Lateralization Notes**.

**Do not** assume the right LSO is the **right MNTB** or the **left
MNTB**. The **right MNTB** is the **inhibitory relay** that **projects
to** the right LSO; the **left MNTB** projects to the **left LSO**.
They are **different structures**.

**Do not** assume the right LSO is the **right MSO**. The **right MSO**
is the **ITD processor**; the **right LSO** is the **ILD processor**.
They are **different structures** — different binaural cues and
different frequency ranges.

**Do not** assume the right LSO is the **right cochlear nuclei**. The
**right cochlear nuclei** are the **monaural first-order relay**; the
**right LSO** is the **binaural second-order ILD processor**.

**Do not** assume the right LSO is the **trapezoid body** or the
**lateral lemniscus**. The **trapezoid body** is the **afferent
white-matter tract**; the **lateral lemniscus** is the **efferent
white-matter tract**. The **right LSO** is the **grey-matter neuron
cluster** that receives from the trapezoid body and projects to the
lateral lemniscus.

**Do not** assume the right LSO is the **right inferior colliculus**, the
**right medial geniculate body**, or the **right primary auditory
cortex**. Those are the **downstream** auditory relays — the **right
LSO** is the **pontine ILD processor**.

**Do not** assume the right LSO is the **right facial nerve nucleus** or
the **right abducens nucleus**. Those are **anatomically adjacent
siblings** — different functional systems.

**Do not** assume the right LSO is the **right cochlear nerve** or the
**right vestibulocochlear nerve**. Those are the **peripheral auditory
conduction infrastructure** — the right LSO is **central grey matter**.

**Do not** assume the right LSO is the **whole superior olivary
complex**. The **superior olivary complex** is the **grandparent** — the
**right LSO** is one of its **three sub-nuclei** (via the
lateral_superior_olive container).

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the right LSO. **The right LSO is SLEA-FREE** — it is
**not** an extended-amygdala component, and it is **NOT part of the fear
circuit**. **Note**: the "right-amygdala" lateralization is about the
**amygdala**, not about this right pontine auditory nucleus — do not
import it.

Iterating the right LSO's (empty) children (recommended consumer
pattern)::

    RIGHT_LATERAL_SUPERIOR_OLIVE_CHILDREN = ()
    # The right LSO is a leaf. The excitatory and inhibitory neuron
    # populations are prose, not modules.

Reaching the left LSO (recommended consumer pattern — the strict
mirror)::

    # The left LSO is the structurally identical LEFT half of the
    # lateral_superior_olive container:
    #
    #   .../lateral_superior_olive/left/
    #
    # The right and left LSO are a STRICT MIRROR PAIR with NO warning at
    # the sub-container level.

Reaching the right MNTB (recommended consumer pattern — the inhibitory
relay sibling)::

    # The right MNTB is the INHIBITORY RELAY that PROJECTS TO the right
    # LSO:
    #
    #   .../superior_olivary_complex/medial_nucleus_of_trapezoid_body/right/
    #
    # The right MNTB PROJECTS an inhibitory (glycinergic) input to the
    # right LSO — the two are FUNCTIONALLY COUPLED but STRUCTURALLY
    # DISTINCT.

Reaching the right MSO (recommended consumer pattern — the ITD processor
sibling)::

    # The right MSO is the ITD PROCESSOR:
    #
    #   .../superior_olivary_complex/medial_superior_olive/right/
    #
    # The right MSO processes INTERAURAL TIME DIFFERENCES for LOW-FREQUENCY
    # sound localization; the right LSO processes INTERAURAL LEVEL
    # DIFFERENCES for HIGH-FREQUENCY sound localization.

Reaching the right cochlear nuclei (recommended consumer pattern — the
UPSTREAM monaural first-order relay)::

    # The right cochlear nuclei are the MONAURAL FIRST-ORDER relay — they
    # project to the right LSO (via the trapezoid body):
    #
    #   .../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/cochlear_nuclei/
    #
    # The right cochlear nuclei are UPSTREAM (monaural first-order); the
    # right LSO is DOWNSTREAM (binaural second-order ILD processor).

Reaching the right inferior colliculus (recommended consumer pattern —
the DOWNSTREAM midbrain auditory relay)::

    # The right inferior colliculus is the DOWNSTREAM midbrain auditory
    # relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/right/inferior_colliculus/
    #
    # The right LSO is UPSTREAM of the right inferior colliculus; the
    # right inferior colliculus is DOWNSTREAM of the right LSO.

Reaching the whole lateral superior olive container (recommended
consumer pattern — the PARENT)::

    # The lateral superior olive container is the BILATERAL ILD PROCESSOR
    # parent that CONTAINS the right LSO and the left LSO:
    #
    #   .../lateral_superior_olive/
    #
    # The right LSO is one of the TWO HALVES of the lateral superior olive
    # container.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        lso_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"lateral_superior_olive.{side}"
        )
        # resolve lso_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The right LSO's neuron populations are prose, not modules:
    #   principal output neurons (excitatory, glutamatergic) -> receive
    #       excitatory right cochlear nuclei input (via trapezoid body)
    #       and inhibitory right MNTB input; project to right inferior
    #       colliculus (primarily, via lateral lemniscus) and to left
    #       inferior colliculus (contralaterally); the ILD computation
    #       output
    #   inhibitory interneurons (local circuit neurons) -> modulate the
    #       principal output neurons within the right LSO
    #
    # Do not attempt to resolve these as sub-paths of the right LSO —
    # resolve them at the neuron-population level through the references.

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
*   **Right pontine stroke — right LSO involvement:** Bassetti, C.,
    Bogousslavsky, J., Barth, A., Regli, F. (1996). "Isolated infarcts
    of the pontine nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Right pontine stroke — right LSO involvement;
    binaural hearing deficits.)
*   **Right MSO (contrast — the ITD processor sibling):** Yin, T.C.T.,
    Chan, J.C.K. (1990). "Interaural time sensitivity in medial superior
    olive of cat." *Journal of Neurophysiology* 64:465–488. (MSO — ITD
    processing; sibling of the LSO.)
*   **Right MNTB (contrast — the inhibitory relay sibling):** Smith,
    P.H., Joris, P.X., Yin, T.C.T. (1998). "Anatomy and physiology of
    principal cells of the medial nucleus of the trapezoid body (MNTB) of
    the cat." *Journal of Neurophysiology* 79:3127–3142. (MNTB —
    inhibitory relay; sibling of the LSO.)
*   **Left MNTB (contrast — projects to the LEFT LSO, not the right
    LSO):** Smith, P.H., et al. (1998). "Anatomy and physiology of
    principal cells of the medial nucleus of the trapezoid body (MNTB)
    of the cat." *Journal of Neurophysiology* 79:3127–3142. (Left
    MNTB — projects to the left LSO, not the right LSO.)
*   **Right cochlear nuclei (contrast — the UPSTREAM monaural first-order
    relay):** Cant, N.B., Benson, C.G. (2003). "Parallel auditory
    pathways: projection patterns of the different neuronal populations
    in the cochlear nuclei." *Brain Research Bulletin* 60:457–474.
    (Right cochlear nuclei — monaural first-order relay; projects to the
    right LSO via the trapezoid body.)
*   **Trapezoid body (contrast — the white-matter afferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Trapezoid body — afferent white-matter tract from
    the cochlear nuclei to the LSO.)
*   **Lateral lemniscus (contrast — the white-matter efferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Lateral lemniscus — efferent white-matter tract
    from the LSO to the inferior colliculus.)
*   **Right inferior colliculus (contrast — the midbrain downstream
    auditory relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002).
    "The inferior colliculus: a hub for the central auditory system."
    In *Integrative Functions in the Mammalian Auditory Pathway*. (Right
    inferior colliculus — downstream of the right LSO.)
*   **Right medial geniculate body (contrast — the thalamic downstream
    auditory relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The
    Inferior Colliculus: A Hub for the Central Auditory System*. (Right
    medial geniculate body — downstream of the right LSO.)
*   **Right primary auditory cortex (contrast — the cortical downstream
    auditory target):** Pickles, J.O. (2015). *An Introduction to the
    Physiology of Hearing*, 4th ed. (Right primary auditory cortex —
    downstream of the right LSO.)
*   **SLEA (contrast — the right LSO is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the right LSO.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the right LSO. **Note**: the
    "right-amygdala" lateralization is about the **amygdala**, not about
    this right pontine auditory nucleus.)
*   NeuroNames — Lateral superior olive (right); FMA — Lateral superior
    olive (right member).
"""
