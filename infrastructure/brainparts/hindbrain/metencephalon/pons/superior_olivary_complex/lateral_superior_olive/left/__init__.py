"""
infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.lateral_superior_olive.left
==========================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── superior_olivary_complex
                └── lateral_superior_olive
                    └── left   <-- THIS MODULE

**Primary synonym:** Left lateral superior olive; left LSO; left lateral
superior olivary nucleus; "the left interaural level difference (ILD)
processor."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nucleus** — an **anatomically delimited
grey-matter nucleus** in the **left lateral superior olivary complex**,
the **principal substrate** of **interaural level difference (ILD)
processing** for **high-frequency horizontal sound localization**.
**Part of:** The **lateral_superior_olive** container — specifically,
the **left half** of the **bilateral LSO**. The **lateral_superior_olive**
container is the **ILD processor** of the **superior olivary complex**;
the **left** sub-container is its **left-side structural child**.
**Structural parent:** ``.../lateral_superior_olive/`` → **direct child**
of the lateral_superior_olive container.
**Structural children:** **None.** This is a **leaf** module. The
**excitatory (glutamatergic) principal output neurons** and the
**inhibitory (glycinergic) input-receiving neurons** are documented as
**prose**, not as structural children.
**Boundary status (LEAF — NOT a container):** **Boundary case — the left
lateral superior olive is a LEAF, not a container.** It has **no
structural children**. The **excitatory and inhibitory neuron
populations** are **prose** populations, not structural children.
Consumers must **not** treat the left lateral superior olive as a
container, and must **not** assume the neuron populations exist as
sub-modules.
**Boundary status (LEFT HALF — NOT the whole lateral_superior_olive
container):** **Boundary case — the left lateral superior olive is the
LEFT HALF of the lateral_superior_olive container, NOT the whole
container.** The **lateral_superior_olive** container
(``.../lateral_superior_olive/``) has **two structural children** —
``left`` and ``right``. The **left** sub-container (here) is the
**left-side** half only. Consumers must **not** conflate the left LSO
with the **whole LSO** — the right side is a **separate structural
sibling**.
**Boundary status (NOT the right lateral superior olive — strict mirror,
no warning):** **Boundary case — the left lateral superior olive is NOT
the right lateral superior olive; the two are a STRICT MIRROR PAIR with
NO warning at the sub-container level.** The **right lateral superior
olive** (``.../lateral_superior_olive/right/``) is the **structurally
identical** right-side counterpart — same neuron populations, same
functional system (ILD processing), same bilateral framing. The two
sides are **strictly mirrored** — any lateralization is documented
**here, in the Lateralization Notes**, not imported from elsewhere.
Consumers must **not** import a lateralization warning into the left LSO
— there is **none at the sub-container level** beyond the
**excitation-inhibition asymmetry** documented below.
**Boundary status (ILD PROCESSOR — NOT the ITD processor):** **Boundary
case — the left lateral superior olive is the ILD PROCESSOR, NOT the ITD
processor.** The **left LSO** processes **interaural level differences**
(ILD) for **high-frequency horizontal sound localization**. The **medial
superior olive (MSO)**
(``.../superior_olivary_complex/medial_superior_olive/left/``) is the
**ITD processor** for **low-frequency horizontal sound localization**.
They are **DIFFERENT STRUCTURES** — different binaural cues (ILD vs.
ITD), different frequency ranges (high vs. low), different neural
mechanisms (excitation-inhibition comparator for ILD vs. coincidence
detector for ITD). **This distinction is functionally load-bearing** —
the two binaural cues dominate at different frequency ranges (ILD above
~1.5 kHz; ITD below ~1.5 kHz in humans). Consumers must **not** conflate
the left LSO with the left MSO.
**Boundary status (NOT the left medial nucleus of the trapezoid body —
that is the INHIBITORY RELAY):** **Boundary case — the left lateral
superior olive is NOT the left medial nucleus of the trapezoid body
(MNTB).** The **left MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/``)
is the **inhibitory relay** that **receives** the **right cochlear
nuclei** globular bushy cell projections (via the **trapezoid body**)
and **projects** an **inhibitory (glycinergic)** input to the **left
LSO**. The **left LSO** (here) is the **ILD processor** that **receives**
the **excitatory left cochlear nuclei** input and the **inhibitory left
MNTB** input. They are **DIFFERENT STRUCTURES** — different functional
roles (ILD processing vs. inhibitory relay). **They are functionally
coupled** — the left MNTB **projects to** the left LSO. Consumers must
**not** conflate the left LSO with the left MNTB.
**Boundary status (NOT the right MNTB — that projects to the RIGHT
LSO):** **Boundary case — the left lateral superior olive is NOT the
right medial nucleus of the trapezoid body.** The **right MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/right/``)
**receives** the **left cochlear nuclei** input (via the **trapezoid
body**) and **projects** an **inhibitory (glycinergic)** input to the
**right LSO** — **not** the left LSO. The **left LSO** (here) is the
**ILD processor** that **receives** the **inhibitory left MNTB** input
(not the right MNTB input). They are **DIFFERENT STRUCTURES** — different
targets (right LSO vs. left LSO). Consumers must **not** conflate the
left LSO with the right MNTB.
**Boundary status (TWO-INPUT COMPARATOR — excitatory ipsilateral and
inhibitory contralateral):** **Boundary case — the left lateral
superior olive is a TWO-INPUT COMPARATOR — it receives EXCITATORY input
from the LEFT cochlear nuclei (ipsilateral) and INHIBITORY input from
the LEFT MNTB (which itself receives RIGHT cochlear nuclei input).** This
**excitation-inhibition** arrangement is the **neural substrate** of
**ILD processing** — the **left LSO neuron** **fires maximally** when
the **left-ear sound level** is **higher** than the **right-ear sound
level** (because the **excitatory** left-ear drive **exceeds** the
**inhibitory** right-ear drive via the left MNTB). **This
ipsilateral-excitatory and contralateral-inhibitory arrangement** is a
**structural fact** of the **left LSO** — it is **not** a
lateralization warning. Consumers must **not** treat the left LSO as a
single-input relay — it is a **two-input comparator** with **distinct
excitatory and inhibitory inputs**.
**Boundary status (NOT the left cochlear nuclei — those are the UPSTREAM
MONAURAL FIRST-ORDER RELAY):** **Boundary case — the left lateral
superior olive is NOT the left cochlear nuclei.** The **left cochlear
nuclei**
(``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``)
are the **monaural first-order relay** that **receive** the **monaural**
auditory input from the **left cochlea** and **project** to the **left
LSO** (via the **trapezoid body**). The **left LSO** (here) is the
**binaural second-order relay** that **receives** the **excitatory left
cochlear nuclei** projection and the **inhibitory left MNTB** projection
(which itself receives **right cochlear nuclei** input) and **performs**
the **ILD computation**. They are **DIFFERENT STRUCTURES** — the
**cochlear nuclei** are **monaural first-order**; the **left LSO** is
**binaural second-order**. **This distinction is clinically
load-bearing** — a **left cochlear nuclei lesion** causes **left
sensorineural hearing loss**; a **left LSO lesion** causes **impaired
ILD-based sound localization** (specifically, **impaired localization of
high-frequency sounds on the left side**) with **preserved pure-tone
thresholds**. Consumers must **not** conflate the left LSO with the left
cochlear nuclei.
**Boundary status (NOT the trapezoid body — that is the WHITE-MATTER
AFFERENT TRACT):** **Boundary case — the left lateral superior olive is
NOT the trapezoid body.** The **trapezoid body** is the **white-matter
decussating tract** that **carries** the **bilateral auditory axons**
from the **cochlear nuclei** to the **superior olivary complex** —
the **afferent limb** of the **binaural sound-localization pathway**.
The **left LSO** (here) is the **grey-matter neuron cluster** that
**receives** the trapezoid-body axons (via **excitatory** input from the
**left cochlear nuclei** and **inhibitory** input from the **left
MNTB**, which itself receives **right cochlear nuclei** input via the
**trapezoid body**). They are **DIFFERENT STRUCTURES** — the **LSO** is
grey matter; the **trapezoid body** is white matter. Consumers must
**not** conflate the left LSO with the trapezoid body.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
EFFERENT TRACT):** **Boundary case — the left lateral superior olive is
NOT the lateral lemniscus.** The **lateral lemniscus** is the
**white-matter ascending tract** that **carries** the **efferent axons**
from the **superior olivary complex** (including the **left LSO**) to the
**inferior colliculus** (primarily the **left inferior colliculus**, with
**contralateral** projections to the **right inferior colliculus**). The
**left LSO** (here) is the **grey-matter neuron cluster** that **gives
rise to** the lateral lemniscus axons. They are **DIFFERENT
STRUCTURES** — the **LSO** is grey matter; the **lateral lemniscus** is
white matter. Consumers must **not** conflate the left LSO with the
lateral lemniscus.
**Boundary status (NOT the left inferior colliculus — that is the
MIDBRAIN DOWNSTREAM AUDITORY RELAY):** **Boundary case — the left
lateral superior olive is NOT the left inferior colliculus.** The **left
inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
is the **midbrain auditory relay** that **receives** the **ascending
auditory projections** from the **superior olivary complex** (including
the **left LSO**) and **projects** to the **left medial geniculate
body**. The **left LSO** (here) is the **pontine ILD processor** — it is
**upstream** of the left inferior colliculus. They are **DIFFERENT
STRUCTURES** — the **left LSO** is **pontine** and **upstream**; the
**left inferior colliculus** is **midbrain** and **downstream**.
Consumers must **not** conflate the left LSO with the left inferior
colliculus.
**Boundary status (NOT the left medial geniculate body — that is the
THALAMIC DOWNSTREAM AUDITORY RELAY):** **Boundary case — the left
lateral superior olive is NOT the left medial geniculate body.** The
**left medial geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
is the **thalamic auditory relay** that **receives** the **ascending
auditory projections** from the **left inferior colliculus** and
**projects** to the **left primary auditory cortex**. The **left LSO**
(here) is the **pontine ILD processor** — it is **upstream** of the left
medial geniculate body. They are **DIFFERENT STRUCTURES** — the **left
LSO** is **pontine** and **upstream**; the **left medial geniculate
body** is **diencephalic** and **downstream**. Consumers must **not**
conflate the left LSO with the left medial geniculate body.
**Boundary status (NOT the left primary auditory cortex — that is the
CORTICAL DOWNSTREAM AUDITORY TARGET):** **Boundary case — the left
lateral superior olive is NOT the left primary auditory cortex.** The
**left primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
is the **cortical target** of the **ascending auditory pathway**. The
**left LSO** (here) is the **pontine ILD processor** — it is **upstream**
of the left primary auditory cortex. They are **DIFFERENT STRUCTURES** —
the **left LSO** is **pontine** and **upstream**; the **left primary
auditory cortex** is **cortical** and **downstream**. Consumers must
**not** conflate the left LSO with the left primary auditory cortex.
**Boundary status (NOT the left facial nerve nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the left lateral
superior olive is NOT the left facial nerve nucleus.** The **left facial
nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) is the
**branchial motor** nucleus for the **left muscles of facial
expression**. The **left LSO** (here) is the **binaural ILD processor**.
They are **DIFFERENT STRUCTURES** — different functional systems
(branchial motor vs. binaural ILD processing). They are **anatomically
adjacent** (both are in the **left ventral pontine tegmentum**) — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the left LSO with the left facial nerve nucleus.
**Boundary status (NOT the left abducens nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the left lateral
superior olive is NOT the left abducens nucleus.** The **left abducens
nucleus** (``.../cranial_nerve_nuclei/left/abducens_nucleus/``) is the
**somatic motor** nucleus for the **left lateral rectus**. The **left
LSO** (here) is the **binaural ILD processor**. They are **DIFFERENT
STRUCTURES** — different functional systems (somatic motor vs. binaural
ILD processing). They are **anatomically adjacent** — the **left LSO** is
**near the genu of the left facial nerve** and the **left abducens
nucleus**; this proximity is a **classic source of confusion** —
consumers must **not** conflate the left LSO with the left abducens
nucleus.
**Boundary status (NOT the left cochlear nerve or the left
vestibulocochlear nerve — those are the PERIPHERAL AUDITORY CONDUCTION
INFRASTRUCTURE):** **Boundary case — the left lateral superior olive is
NOT the left cochlear nerve or the left vestibulocochlear nerve.** The
**left cochlear nerve** (the cochlear division of left CN VIII) and the
**left vestibulocochlear nerve** (left CN VIII) are the **white-matter
peripheral nerves** that **carry** the **primary auditory axons** from
the **left spiral ganglion** to the **left cochlear nuclei**. The **left
LSO** (here) is the **central grey-matter binaural ILD processor**.
They are **DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **left LSO** is **central grey matter**. Consumers
must **not** conflate the left LSO with the left cochlear or left
vestibulocochlear nerve.
**Boundary status (NOT the whole lateral_superior_olive container — that
is the PARENT):** **Boundary case — the left lateral superior olive is
NOT the whole lateral_superior_olive container; the
lateral_superior_olive container is the PARENT.** The
**lateral_superior_olive** container (``.../lateral_superior_olive/``)
is the **bilateral ILD processor** — it **contains** the **left LSO**
(here) and the **right LSO**. The **left LSO** is the **left half** of
the lateral_superior_olive container. Consumers must **not** conflate
the left LSO with the **whole LSO**.
**Boundary status (NOT the whole superior_olivary_complex container —
that is the GRANDPARENT):** **Boundary case — the left lateral superior
olive is NOT the whole superior_olivary_complex container; the
superior_olivary_complex container is the GRANDPARENT.** The
**superior_olivary_complex** container
(``.../superior_olivary_complex/``) is the **pontine binaural
sound-localization relay** — it **contains** the **LSO**, the **MSO**,
and the **MNTB**. The **left LSO** is **one of the sub-nuclei** of the
superior olivary complex. Consumers must **not** conflate the left LSO
with the **whole superior olivary complex**.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
functionally distinct populations):** **Boundary case — the left lateral
superior olive is NOT a single uniform neuron population; it contains
MULTIPLE functionally distinct populations.** The **principal output
neurons** — the **excitatory (glutamatergic)** projection neurons that
**receive** the **excitatory left cochlear nuclei** input and the
**inhibitory left MNTB** input, and **project** to the **left inferior
colliculus** (via the **lateral lemniscus**) — they are the **ILD
computation** output. The **inhibitory interneurons** — the **local
circuit neurons** that **modulate** the **principal output neurons**.
**These populations are prose, not structural children.** Consumers must
**not** treat the left LSO as a single uniform population — it is a
**functionally heterogeneous nucleus** with **distinct** sub-circuits.
**Boundary status (SLEA-FREE — the left lateral superior olive is NOT an
extended-amygdala component):** **Boundary case — the left lateral
superior olive is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala) and to
the **BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **left LSO** is a **binaural auditory ILD processor** —
it is **NOT** an extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into the left
LSO — it is **SLEA-free**.

Overview
--------
The left lateral superior olive is the **left half** of the **bilateral
LSO** — the **left grey-matter neuron cluster** in the **left superior
olivary complex** that is the **principal substrate** of **interaural
level difference (ILD) processing** for **high-frequency horizontal
sound localization**. It is a **leaf** module under the ``left``
sub-container of the lateral_superior_olive container, and it is the
**left ILD processor** — the **left LSO** that **compares** the
**left-ear sound level** (excitatory input) with the **right-ear sound
level** (inhibitory input via the left MNTB).

**The left lateral superior olive is a LEAF, not a container.** It has
**no structural children**. The **excitatory and inhibitory neuron
populations** are **prose populations**, not structural children.

**The left lateral superior olive is the LEFT HALF of the
lateral_superior_olive container, NOT the whole container.** The
**lateral_superior_olive** container has **two structural children** —
``left`` and ``right``. The **left** sub-container (here) is the
**left-side** half only.

**The left lateral superior olive and the right lateral superior olive
are a STRICT MIRROR PAIR with NO warning at the sub-container level.**
The two sides are **structurally identical** — same neuron populations,
same functional system (ILD processing), same bilateral framing.

**The left lateral superior olive is the ILD PROCESSOR, not the ITD
processor.** The **left LSO** processes **interaural level differences**
for **high-frequency horizontal sound localization**. The **left MSO**
processes **interaural time differences** for **low-frequency horizontal
sound localization**.

**The left lateral superior olive is a TWO-INPUT COMPARATOR.** It
receives **excitatory** input from the **left cochlear nuclei** and
**inhibitory** input from the **left MNTB** (which itself receives
**right cochlear nuclei** input). The **left LSO** **fires maximally**
when the **left-ear sound level** is **higher** than the **right-ear
sound level** — it signals **"sound on the left."**

**The left lateral superior olive is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The left lateral superior olive contains **multiple functionally
distinct neuron populations** — documented as **prose**, not as
structural children:

*   **Principal output neurons** — the **excitatory (glutamatergic)**
    projection neurons that **receive** the **excitatory left cochlear
    nuclei** input (via the **trapezoid body**) and the **inhibitory
    left MNTB** input (via the **glycinergic** projection from the
    **left MNTB**, which itself receives **right cochlear nuclei** input
    via the **trapezoid body**). They **project** to the **left
    inferior colliculus** (primarily, via the **lateral lemniscus**)
    and to the **right inferior colliculus** (contralaterally, to a
    lesser extent). They are the **ILD computation** output — they
    **fire maximally** when the **left-ear sound level** is **higher**
    than the **right-ear sound level** (because the **excitatory**
    left-ear drive **exceeds** the **inhibitory** right-ear drive).

*   **Inhibitory interneurons** — the **local circuit neurons** that
    **modulate** the **principal output neurons** within the left LSO.
    They are **prose** populations, not structural children.

**These populations are prose, not structural children.** The tree wires
the **left lateral superior olive** as a **single leaf** under the
``left`` sub-container of the lateral_superior_olive container — the
**excitatory and inhibitory neuron populations** are **prose**, not
structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Left LSO / Right LSO Boundary
---------------------------------
This is the **strict-mirror** boundary:

*   **Left lateral superior olive** (this module) — the **left-side** LSO
    — the **left ILD processor**.

*   **Right lateral superior olive**
    (``.../lateral_superior_olive/right/``) — the **structurally
    identical** right-side LSO — the **right ILD processor**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same neuron
populations, same functional system (ILD processing), same bilateral
framing. Any lateralization is documented **here, in the Lateralization
Notes**, not imported from elsewhere. Consumers must **not** import a
lateralization warning into the left LSO — there is **none at the
sub-container level** beyond the **excitation-inhibition asymmetry**
documented below.

The Left LSO / Lateral Superior Olive Container Boundary
--------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Left lateral superior olive** (this module) — the **left-side**
    half of the bilateral LSO.

*   **Lateral superior olive container** (``.../lateral_superior_olive/``)
    — the **whole bilateral LSO**, with **two structural children**
    (``left`` and ``right``).

**The left lateral superior olive is a child of the lateral_superior_olive
container.** Consumers must **not** conflate the left half with the
**whole LSO** — the right side is a **separate structural sibling**.

The Left LSO / Left MSO Boundary
--------------------------------
This is the **sibling** boundary — **ILD processor vs. ITD processor**:

*   **Left lateral superior olive** (this module) — the **left ILD
    processor** for **high-frequency horizontal sound localization**.

*   **Left medial superior olive (MSO)**
    (``.../superior_olivary_complex/medial_superior_olive/left/``) — the
    **left ITD processor** for **low-frequency horizontal sound
    localization**.

**They are DIFFERENT STRUCTURES** — different binaural cues (ILD vs.
ITD), different frequency ranges (high vs. low), different neural
mechanisms (excitation-inhibition for ILD vs. coincidence detection for
ITD). Consumers must **not** conflate the left LSO with the left MSO.

The Left LSO / Left MNTB Boundary
---------------------------------
This is the **sibling** boundary — **ILD processor vs. inhibitory
relay**:

*   **Left lateral superior olive** (this module) — the **left ILD
    processor** that **receives** the **inhibitory left MNTB** input.

*   **Left medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/``)
    — the **left inhibitory relay** that **receives** the **right
    cochlear nuclei** input and **projects** the **inhibitory
    (glycinergic)** input to the **left LSO**.

**They are DIFFERENT STRUCTURES** — different functional roles (ILD
processing vs. inhibitory relay). **They are functionally coupled** —
the left MNTB **projects to** the left LSO. Consumers must **not**
conflate the left LSO with the left MNTB.

The Left LSO / Right MNTB Boundary
----------------------------------
This is the **wrong-target** boundary:

*   **Left lateral superior olive** (this module) — the **left ILD
    processor** that **receives** the **inhibitory left MNTB** input
    (not the right MNTB input).

*   **Right medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/right/``)
    — the **right inhibitory relay** that **projects** to the **right
    LSO** — **not** the left LSO.

**They are DIFFERENT STRUCTURES** — different targets (right LSO vs.
left LSO). Consumers must **not** conflate the left LSO with the right
MNTB.

The Left LSO / Left Cochlear Nuclei Boundary
--------------------------------------------
This is the **binaural second-order vs. monaural first-order** boundary:

*   **Left lateral superior olive** (this module) — the **left binaural
    second-order relay** that **receives** the **excitatory left
    cochlear nuclei** input and the **inhibitory left MNTB** input and
    **performs** the **ILD computation**.

*   **Left cochlear nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``)
    — the **left monaural first-order relay** that **receives** the
    **monaural** auditory input from the **left cochlea** and
    **projects** to the **left LSO** (via the **trapezoid body**).

**They are DIFFERENT STRUCTURES** — the **left cochlear nuclei** are
**monaural first-order**; the **left LSO** is **binaural second-order**.
**This distinction is clinically load-bearing** — a **left cochlear
nuclei lesion** causes **left sensorineural hearing loss**; a **left LSO
lesion** causes **impaired ILD-based sound localization** (specifically,
**impaired localization of high-frequency sounds on the left side**)
with **preserved pure-tone thresholds**. Consumers must **not** conflate
the left LSO with the left cochlear nuclei.

The Left LSO / Trapezoid Body Boundary
--------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Left lateral superior olive** (this module) — the **grey-matter
    neuron cluster** that **receives** the trapezoid-body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the **bilateral auditory axons** from the **cochlear
    nuclei** to the **superior olivary complex** (including the left
    LSO).

**They are DIFFERENT STRUCTURES** — the **LSO** is grey matter; the
**trapezoid body** is white matter. Consumers must **not** conflate the
left LSO with the trapezoid body.

The Left LSO / Lateral Lemniscus Boundary
-----------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Left lateral superior olive** (this module) — the **grey-matter
    neuron cluster** that **gives rise to** the lateral lemniscus axons.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the **efferent axons** from the **superior olivary
    complex** (including the left LSO) to the **inferior colliculus**.

**They are DIFFERENT STRUCTURES** — the **LSO** is grey matter; the
**lateral lemniscus** is white matter. Consumers must **not** conflate
the left LSO with the lateral lemniscus.

The Left LSO / Left Inferior Colliculus Boundary
------------------------------------------------
This is the **pontine ILD processor vs. midbrain downstream relay**
boundary:

*   **Left lateral superior olive** (this module) — the **left pontine
    ILD processor**.

*   **Left inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``)
    — the **left midbrain auditory relay** that **receives** the
    **ascending auditory projections** from the **superior olivary
    complex** (including the left LSO) and **projects** to the **left
    medial geniculate body**.

**They are DIFFERENT STRUCTURES** — the **left LSO** is **pontine** and
**upstream**; the **left inferior colliculus** is **midbrain** and
**downstream**. Consumers must **not** conflate the left LSO with the
left inferior colliculus.

The Left LSO / Left Medial Geniculate Body Boundary
---------------------------------------------------
This is the **pontine ILD processor vs. thalamic downstream relay**
boundary:

*   **Left lateral superior olive** (this module) — the **left pontine
    ILD processor**.

*   **Left medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``)
    — the **left thalamic auditory relay** that **receives** the
    **ascending auditory projections** from the **left inferior
    colliculus** and **projects** to the **left primary auditory
    cortex**.

**They are DIFFERENT STRUCTURES** — the **left LSO** is **pontine** and
**upstream**; the **left medial geniculate body** is **diencephalic** and
**downstream**. Consumers must **not** conflate the left LSO with the
left medial geniculate body.

The Left LSO / Left Primary Auditory Cortex Boundary
----------------------------------------------------
This is the **pontine ILD processor vs. cortical downstream target**
boundary:

*   **Left lateral superior olive** (this module) — the **left pontine
    ILD processor**.

*   **Left primary auditory cortex** (Heschl's gyrus, Brodmann areas 41
    and 42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``)
    — the **left cortical target** of the **ascending auditory
    pathway**.

**They are DIFFERENT STRUCTURES** — the **left LSO** is **pontine** and
**upstream**; the **left primary auditory cortex** is **cortical** and
**downstream**. Consumers must **not** conflate the left LSO with the
left primary auditory cortex.

The Left LSO / Left Facial Nerve Nucleus Boundary
-------------------------------------------------
This is the **auditory binaural relay vs. branchial motor** boundary:

*   **Left lateral superior olive** (this module) — the **left binaural
    ILD processor**.

*   **Left facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) — the
    **branchial motor** nucleus for the **left muscles of facial
    expression**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. branchial motor). They are
**anatomically adjacent** — consumers must **not** conflate the left LSO
with the left facial nerve nucleus.

The Left LSO / Left Abducens Nucleus Boundary
---------------------------------------------
This is the **auditory binaural relay vs. somatic motor** boundary:

*   **Left lateral superior olive** (this module) — the **left binaural
    ILD processor**.

*   **Left abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/``) — the
    **somatic motor** nucleus for the **left lateral rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. somatic motor). They are
**anatomically adjacent** — consumers must **not** conflate the left LSO
with the left abducens nucleus.

The Left LSO / Left Cochlear and Vestibulocochlear Nerves Boundary
------------------------------------------------------------------
This is the **central grey matter vs. peripheral white matter** boundary:

*   **Left lateral superior olive** (this module) — the **central
    grey-matter binaural ILD processor**.

*   **Left cochlear nerve** (the cochlear division of left CN VIII) and
    **left vestibulocochlear nerve** (left CN VIII) — the **peripheral
    white-matter nerves** that **carry** the **primary auditory axons**
    from the **left spiral ganglion** to the **left cochlear nuclei**.

**They are DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **left LSO** is **central grey matter**. Consumers
must **not** conflate the left LSO with the left cochlear or left
vestibulocochlear nerve.

The Left LSO / Whole Lateral Superior Olive Container Boundary
--------------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Left lateral superior olive** (this module) — the **left-side**
    half of the lateral_superior_olive container.

*   **Lateral superior olive container** (``.../lateral_superior_olive/``)
    — the **whole bilateral LSO**, with **two structural children**
    (``left`` and ``right``).

**The left lateral superior olive is a child of the
lateral_superior_olive container.** Consumers must **not** conflate the
left LSO with the **whole LSO**.

The Left LSO / Whole Superior Olivary Complex Container Boundary
----------------------------------------------------------------
This is the **sub-nucleus vs. grandparent** boundary:

*   **Left lateral superior olive** (this module) — the **left LSO** —
    one of the sub-nuclei of the superior olivary complex.

*   **Superior olivary complex container**
    (``.../superior_olivary_complex/``) — the **pontine binaural
    sound-localization relay** that **contains** the **LSO**, the
    **MSO**, and the **MNTB**.

**The left LSO is a great-grandchild of the superior olivary complex**
(via the lateral_superior_olive container). Consumers must **not**
conflate the left LSO with the **whole superior olivary complex**.

The Left LSO / SLEA Boundary
----------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Left lateral superior olive** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The left lateral superior olive is NOT part of the SLEA continuum.** It
is a **binaural auditory ILD processor**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the left
LSO.

Function in the Human Brain
---------------------------
The left lateral superior olive's functions are **interaural level
difference (ILD) processing** for **high-frequency horizontal sound
localization** — **NOT a single unified function**:

*   **ILD Computation (Excitation-Inhibition Comparator):** The **left
    LSO** is the **two-input comparator** for **ILD processing**. It
    **receives** the **excitatory left cochlear nuclei** input (via the
    **trapezoid body**) and the **inhibitory left MNTB** input (which
    itself receives **right cochlear nuclei** input via the **trapezoid
    body**). The **excitation-inhibition** arrangement means the **left
    LSO neuron** **fires maximally** when the **left-ear sound level** is
    **higher** than the **right-ear sound level** — the **left LSO
    neuron** is a **comparator** of the **left-ear level** (excitation)
    against the **right-ear level** (inhibition).

*   **Left-Sided High-Frequency Horizontal Sound Localization:** The
    **left LSO** is the **dominant binaural cue** for **high-frequency
    sound localization** (> ~1.5 kHz in humans) of **sound sources on
    the left side** — because **high-frequency sounds** are **shadowed**
    by the **head** (the **head shadow effect**), the **left-ear sound
    level** is **higher** than the **right-ear sound level** when the
    sound source is on the **left side**, and the **left LSO** is
    **maximally excited** — it signals **"sound on the left."**

*   **Human LSO Smaller than MSO (But Retains ILD Function):** In
    **humans**, the **LSO** is **smaller** than in many other mammals
    (especially in **echo-locating bats and rodents**), and the **human
    MSO** is the **dominant binaural sound-localization nucleus** (MSO
    dominates for **ITD** — **low-frequency** sound localization). The
    **human LSO** nevertheless **retains ILD-related function** — it
    **contributes** to **high-frequency horizontal sound
    localization** and to **binaural unmasking** (the ability to detect
    a signal in noise by comparing the two ears).

*   **NOT a neural processor in the classical sense.** The **left LSO**
    is a **binaural relay** — it **receives** the **excitatory** and
    **inhibitory** auditory inputs and **performs** the **ILD
    computation** — it **projects** the **binaural representation** to
    the **left inferior colliculus** (primarily, via the **lateral
    lemniscus**) and to the **right inferior colliculus**
    (contralaterally, to a lesser extent). The **processing** of
    **binaural sound localization** is **distributed** across the
    **cochlear nuclei** (monaural auditory processing), the **left LSO**
    (ILD processing), the **left MSO** (ITD processing), the **inferior
    colliculus** (integration of binaural and spectral cues and auditory
    space map), the **medial geniculate body** (thalamic relay), and the
    **primary auditory cortex** (cortical processing). The **left LSO**
    is the **left ILD processor** — the **brainstem substrate** of
    **left-sided high-frequency horizontal sound localization**.

**The unifying theme:** the left lateral superior olive is the **left
binaural ILD processor** — the **excitation-inhibition comparator** that
**computes** the **interaural level difference** for **high-frequency
horizontal sound localization** on the **left side**. It is a **leaf
module** under the ``left`` sub-container of the lateral_superior_olive
container, **two-input (excitatory-inhibitory)**, **SLEA-free**, and
**NOT the left MNTB** (the **left MNTB** is the **inhibitory relay** that
**projects to** the left LSO).

Associated Disorders
--------------------
The left lateral superior olive has **no named "left lateral superior
olive syndrome"** — its clinical associations are **binaural-specific**:

*   **Left LSO Lesion — Impaired ILD-Based Sound Localization on the
    Left with Preserved Pure-Tone Thresholds:** A lesion of the **left
    lateral superior olive** (e.g. **pontine stroke**, **tumor**,
    **demyelination**) causes **impaired ILD-based sound localization**
    — specifically, **impaired localization of high-frequency sounds on
    the left side** — with **preserved pure-tone thresholds** (because
    the **monaural auditory pathway** — the **cochlear nuclei** and the
    **ascending auditory pathway** — is intact). **The ILD-specific
    pattern** is the **substrate** of the **left LSO** function — this
    is the **"left ILD-specific binaural deficit"** that **distinguishes**
    a **left LSO lesion** from a **left cochlear nuclei lesion** (which
    causes **left sensorineural hearing loss**) or a **left MSO lesion**
    (which causes **left ITD-specific binaural deficit**).

*   **High-Frequency Left-Sided Sound Localization Deficit — Left LSO
    Involvement:** **High-frequency horizontal sound localization** on
    the **left side** depends on **ILD processing**, which is
    **subserved** by the **left LSO**. **The left LSO** is **one of the
    neural substrates** of **left ILD-based sound localization**, and
    its dysfunction may **contribute** to **high-frequency left-sided
    sound localization deficits** — especially in **patients with left
    pontine lesions** or **age-related hearing loss** (presbycusis).

*   **Presbycusis — Left LSO Involvement:** **Presbycusis** (age-related
    hearing loss) is characterized by **peripheral auditory dysfunction**
    (cochlear hair cell loss) **and central auditory dysfunction**
    (including **left LSO** dysfunction — **reduced neuron number**,
    **reduced synaptic density**, and **reduced ILD processing**). The
    **left LSO** may show **age-related changes** — contributing to
    **impaired left-sided high-frequency horizontal sound localization**
    and **impaired speech understanding in noise** in **older adults**.

*   **Multiple Sclerosis — Left LSO Involvement:** **Multiple sclerosis**
    can affect the **left LSO** (as a **left brainstem demyelinating
    lesion**), contributing to **impaired left ILD-based sound
    localization** and **left binaural hearing deficits**.

*   **Left Pontine Stroke — Left LSO Involvement:** A **left pontine
    stroke** (e.g. **basilar artery** perforator territory) involving
    the **left LSO** causes **impaired left ILD-based sound
    localization** — often accompanied by **other left pontine signs**
    (**right hemiparesis**, **left facial palsy**, **left abducens
    palsy**, **right cerebellar ataxia**).

*   **Binaural Hearing Deficit — Left LSO Involvement:** **Binaural
    hearing** is the **ability to use** the **differences** between the
    **two ears** to **localize sound** and to **understand speech in
    noise**. **The left LSO** is **one of the neural substrates** of
    **binaural hearing** (specifically **left ILD-based binaural
    processing**), and its dysfunction may **contribute** to **left
    binaural hearing deficits**.

*   **No Named "Left LSO Syndrome":** The left LSO is a **single
    bilateral sub-nucleus** — it has **no named clinical syndrome** of
    its own. Its clinical relevance is **ILD-specific** — **impaired
    left ILD-based sound localization**, **impaired left-sided
    high-frequency horizontal sound localization**, and **impaired left
    binaural hearing**.

**What is NOT here:** The left LSO is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **vestibular neuritis** (vestibular nerve), **labyrinthitis**
(inner ear), or **auditory neuropathy spectrum disorder** (cochlear nerve
or hair cell). Its clinical relevance is **ILD-specific**, via the
**interaural level difference (ILD) processing** it subserves on the
**left side**. **No named left LSO syndrome exists.**

Lateralization Notes
--------------------
This is the **left** lateral superior olive module. The left LSO is
**bilaterally symmetric** with the right LSO and **strictly mirrored** —
and it carries **NO warning at the sub-container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right** LSO are
    **structurally identical** — same neuron populations, same functional
    system (ILD processing), same bilateral framing. The bilateral
    symmetry is **strict**.

*   **Ipsilateral Excitatory and Contralateral Inhibitory Inputs
    (Structural Fact, NOT a Lateralization Warning):** The **left LSO**
    receives **excitatory input** from the **left cochlear nuclei** (via
    the **trapezoid body**) and **inhibitory input** from the **left
    MNTB** (which itself receives **right cochlear nuclei** input via
    the **trapezoid body**). **This ipsilateral excitatory and
    contralateral inhibitory input** is a **structural fact** of the
    **ILD-processing system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **ILD
    computation** in the **left LSO** — the **left LSO** **compares**
    the **left-ear sound level** (excitation) with the **right-ear
    sound level** (inhibition via the left MNTB).

*   **Left-Sided ILD Computation (Structural Fact, NOT a Lateralization
    Warning):** The **left LSO neuron** **fires maximally** when the
    **left-ear sound level** is **higher** than the **right-ear sound
    level** — because the **excitatory** left-ear drive **exceeds** the
    **inhibitory** right-ear drive. **This ILD computation** is a
    **structural fact** of the **binaural sound-localization system** —
    it is **not** a functional lateralization. It is the **neural
    substrate** of **left-sided high-frequency horizontal sound
    localization** in the human brain.

*   **Ipsilateral and Contralateral Inferior Colliculus Projections
    (Structural Fact, NOT a Lateralization Warning):** The **left LSO**
    **projects** to the **left inferior colliculus** (ipsilateral,
    primarily, via the **lateral lemniscus**) and to the **right
    inferior colliculus** (contralaterally, to a lesser extent). **This
    ipsilateral and contralateral projection** is a **structural fact**
    of the **ascending auditory system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **bilateral
    inferior colliculus representation** of **left-sided sound-source
    location**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The left LSO is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the left LSO.

*   **NO Amygdala-Lateralization Warning of their own (the left LSO is
    BINAURAL AUDITORY, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The left LSO is a **binaural auditory ILD
    processor** — consumers must **not** conflate it with the
    **amygdala** or with the **fear circuit**.

**A consumer that assumes "left LSO = right LSO" will be structurally
correct** — the two sides are **strictly symmetric** (the ipsilateral
excitatory and contralateral inhibitory inputs and the left-sided ILD
computation are structural facts, not lateralizations). The left LSO is
a **strict-mirror pair with NO warning at the sub-container level** —
**no SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left sub-container is the
    **left half**; it does **not** import the right sub-container at
    module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../lateral_superior_olive/right/``,
    ``.../superior_olivary_complex/medial_superior_olive/``,
    ``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``,
    ``.../superior_olivary_complex/``, ``.../pons/tegmentum/``,
    ``.../pons/cranial_nerve_nuclei/``, ``.../midbrain/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    left LSO's relationships to the **left MNTB**, the **right MNTB**,
    the **left MSO**, the **left cochlear nuclei**, the **trapezoid
    body**, the **lateral lemniscus**, the **left inferior colliculus**,
    the **left medial geniculate body**, the **left primary auditory
    cortex**, the **left facial nerve nucleus**, the **left abducens
    nucleus**, the **left cochlear** and **left vestibulocochlear
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
*   **LEFT HALF — NOT the whole lateral_superior_olive container.** The
    **lateral_superior_olive** container has **two structural children**
    — ``left`` and ``right``. The **left** sub-container (here) is the
    **left-side** half only.
*   **STRICT MIRROR with the right LSO — NO warning at the sub-container
    level.** The **left** and **right** LSO are **structurally
    identical**. Any lateralization is documented **here, in the
    Lateralization Notes**.
*   **ILD PROCESSOR — NOT the ITD processor (MSO).** The **left LSO**
    processes **interaural level differences**; the **left MSO**
    processes **interaural time differences**. Consumers must **not**
    conflate the two.
*   **NOT the left MNTB — that is the INHIBITORY RELAY.** The **left
    MNTB** **projects to** the left LSO. Consumers must **not** conflate
    the two.
*   **NOT the right MNTB — that projects to the RIGHT LSO.** Consumers
    must **not** conflate the left LSO with the right MNTB.
*   **NOT the left cochlear nuclei — those are the UPSTREAM MONAURAL
    FIRST-ORDER RELAY.** Consumers must **not** conflate the left LSO
    with the left cochlear nuclei.
*   **NOT the trapezoid body or the lateral lemniscus — those are the
    WHITE-MATTER TRACTS.** Consumers must **not** conflate the left LSO
    with either tract.
*   **NOT the left inferior colliculus, the left medial geniculate body,
    or the left primary auditory cortex — those are DOWNSTREAM AUDITORY
    STRUCTURES.** Consumers must **not** conflate the left LSO with any
    of them.
*   **NOT the left facial nerve nucleus or the left abducens nucleus —
    those are ANATOMICALLY ADJACENT SIBLINGS.** Consumers must **not**
    conflate the left LSO with either of them.
*   **NOT the left cochlear or left vestibulocochlear nerve — those are
    the PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE.** Consumers must
    **not** conflate the left LSO with either nerve.
*   **NOT the whole lateral_superior_olive container — that is the
    PARENT.** Consumers must **not** conflate the left LSO with the
    whole LSO.
*   **NOT the whole superior_olivary_complex container — that is the
    GRANDPARENT.** Consumers must **not** conflate the left LSO with the
    whole superior olivary complex.
*   **MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — NOT a single uniform
    nucleus.** The **principal output neurons** (excitatory,
    glutamatergic) and the **inhibitory interneurons** are **prose**, not
    structural children. Consumers must **not** treat the left LSO as a
    single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The left LSO is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.
*   **NOT the fear-output — the left LSO is BINAURAL AUDITORY.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **left LSO** is a **binaural auditory ILD processor**
    — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The left LSO is a local leaf under the
    ``left`` sub-container of the lateral_superior_olive container, not
    a cross-listed leaf.
*   **No nested cross-listing.** The left LSO has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.lateral_superior_olive import left

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex."
        "lateral_superior_olive.left"
    )

**Do not** assume the left LSO is a **container**. It is a **leaf** —
the **excitatory and inhibitory neuron populations** are **prose**, not
structural children.

**Do not** assume the left LSO is the **whole lateral_superior_olive
container**. It is the **left-side half only** — the right side is a
**separate structural sibling**.

**Do not** assume the left LSO is the **right LSO**. The two are a
**strict mirror pair with NO warning at the sub-container level** — any
lateralization is documented **here, in the Lateralization Notes**.

**Do not** assume the left LSO is the **left MNTB** or the **right
MNTB**. The **left MNTB** is the **inhibitory relay** that **projects
to** the left LSO; the **right MNTB** projects to the **right LSO**.
They are **different structures**.

**Do not** assume the left LSO is the **left MSO**. The **left MSO** is
the **ITD processor**; the **left LSO** is the **ILD processor**. They
are **different structures** — different binaural cues and different
frequency ranges.

**Do not** assume the left LSO is the **left cochlear nuclei**. The
**left cochlear nuclei** are the **monaural first-order relay**; the
**left LSO** is the **binaural second-order ILD processor**.

**Do not** assume the left LSO is the **trapezoid body** or the **lateral
lemniscus**. The **trapezoid body** is the **afferent white-matter
tract**; the **lateral lemniscus** is the **efferent white-matter
tract**. The **left LSO** is the **grey-matter neuron cluster** that
receives from the trapezoid body and projects to the lateral lemniscus.

**Do not** assume the left LSO is the **left inferior colliculus**, the
**left medial geniculate body**, or the **left primary auditory
cortex**. Those are the **downstream** auditory relays — the **left
LSO** is the **pontine ILD processor**.

**Do not** assume the left LSO is the **left facial nerve nucleus** or
the **left abducens nucleus**. Those are **anatomically adjacent
siblings** — different functional systems.

**Do not** assume the left LSO is the **left cochlear nerve** or the
**left vestibulocochlear nerve**. Those are the **peripheral auditory
conduction infrastructure** — the left LSO is **central grey matter**.

**Do not** assume the left LSO is the **whole superior olivary
complex**. The **superior olivary complex** is the **grandparent** — the
**left LSO** is one of its **three sub-nuclei** (via the
lateral_superior_olive container).

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the left LSO. **The left LSO is SLEA-FREE** — it is
**not** an extended-amygdala component, and it is **NOT part of the fear
circuit**.

Iterating the left LSO's (empty) children (recommended consumer
pattern)::

    LEFT_LATERAL_SUPERIOR_OLIVE_CHILDREN = ()
    # The left LSO is a leaf. The excitatory and inhibitory neuron
    # populations are prose, not modules.

Reaching the right LSO (recommended consumer pattern — the strict
mirror)::

    # The right LSO is the structurally identical RIGHT half of the
    # lateral_superior_olive container:
    #
    #   .../lateral_superior_olive/right/
    #
    # The left and right LSO are a STRICT MIRROR PAIR with NO warning at
    # the sub-container level.

Reaching the left MNTB (recommended consumer pattern — the inhibitory
relay sibling)::

    # The left MNTB is the INHIBITORY RELAY that PROJECTS TO the left
    # LSO:
    #
    #   .../superior_olivary_complex/medial_nucleus_of_trapezoid_body/left/
    #
    # The left MNTB PROJECTS an inhibitory (glycinergic) input to the
    # left LSO — the two are FUNCTIONALLY COUPLED but STRUCTURALLY
    # DISTINCT.

Reaching the left MSO (recommended consumer pattern — the ITD processor
sibling)::

    # The left MSO is the ITD PROCESSOR:
    #
    #   .../superior_olivary_complex/medial_superior_olive/left/
    #
    # The left MSO processes INTERAURAL TIME DIFFERENCES for LOW-FREQUENCY
    # sound localization; the left LSO processes INTERAURAL LEVEL
    # DIFFERENCES for HIGH-FREQUENCY sound localization.

Reaching the left cochlear nuclei (recommended consumer pattern — the
UPSTREAM monaural first-order relay)::

    # The left cochlear nuclei are the MONAURAL FIRST-ORDER relay — they
    # project to the left LSO (via the trapezoid body):
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/
    #
    # The left cochlear nuclei are UPSTREAM (monaural first-order); the
    # left LSO is DOWNSTREAM (binaural second-order ILD processor).

Reaching the left inferior colliculus (recommended consumer pattern —
the DOWNSTREAM midbrain auditory relay)::

    # The left inferior colliculus is the DOWNSTREAM midbrain auditory
    # relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/
    #
    # The left LSO is UPSTREAM of the left inferior colliculus; the left
    # inferior colliculus is DOWNSTREAM of the left LSO.

Reaching the whole lateral superior olive container (recommended
consumer pattern — the PARENT)::

    # The lateral superior olive container is the BILATERAL ILD PROCESSOR
    # parent that CONTAINS the left LSO and the right LSO:
    #
    #   .../lateral_superior_olive/
    #
    # The left LSO is one of the TWO HALVES of the lateral superior olive
    # container.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        lso_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"lateral_superior_olive.{side}"
        )
        # resolve lso_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The left LSO's neuron populations are prose, not modules:
    #   principal output neurons (excitatory, glutamatergic) -> receive
    #       excitatory left cochlear nuclei input (via trapezoid body)
    #       and inhibitory left MNTB input; project to left inferior
    #       colliculus (primarily, via lateral lemniscus) and to right
    #       inferior colliculus (contralaterally); the ILD computation
    #       output
    #   inhibitory interneurons (local circuit neurons) -> modulate the
    #       principal output neurons within the left LSO
    #
    # Do not attempt to resolve these as sub-paths of the left LSO —
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
*   **Left pontine stroke — left LSO involvement:** Bassetti, C.,
    Bogousslavsky, J., Barth, A., Regli, F. (1996). "Isolated infarcts
    of the pontine nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Left pontine stroke — left LSO involvement;
    binaural hearing deficits.)
*   **Left MSO (contrast — the ITD processor sibling):** Yin, T.C.T.,
    Chan, J.C.K. (1990). "Interaural time sensitivity in medial superior
    olive of cat." *Journal of Neurophysiology* 64:465–488. (MSO — ITD
    processing; sibling of the LSO.)
*   **Left MNTB (contrast — the inhibitory relay sibling):** Smith,
    P.H., Joris, P.X., Yin, T.C.T. (1998). "Anatomy and physiology of
    principal cells of the medial nucleus of the trapezoid body (MNTB) of
    the cat." *Journal of Neurophysiology* 79:3127–3142. (MNTB —
    inhibitory relay; sibling of the LSO.)
*   **Right MNTB (contrast — projects to the RIGHT LSO, not the left
    LSO):** Smith, P.H., et al. (1998). "Anatomy and physiology of
    principal cells of the medial nucleus of the trapezoid body (MNTB)
    of the cat." *Journal of Neurophysiology* 79:3127–3142. (Right
    MNTB — projects to the right LSO, not the left LSO.)
*   **Left cochlear nuclei (contrast — the UPSTREAM monaural first-order
    relay):** Cant, N.B., Benson, C.G. (2003). "Parallel auditory
    pathways: projection patterns of the different neuronal populations
    in the cochlear nuclei." *Brain Research Bulletin* 60:457–474.
    (Left cochlear nuclei — monaural first-order relay; projects to the
    left LSO via the trapezoid body.)
*   **Trapezoid body (contrast — the white-matter afferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Trapezoid body — afferent white-matter tract from
    the cochlear nuclei to the LSO.)
*   **Lateral lemniscus (contrast — the white-matter efferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Lateral lemniscus — efferent white-matter tract
    from the LSO to the inferior colliculus.)
*   **Left inferior colliculus (contrast — the midbrain downstream
    auditory relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002).
    "The inferior colliculus: a hub for the central auditory system."
    In *Integrative Functions in the Mammalian Auditory Pathway*. (Left
    inferior colliculus — downstream of the left LSO.)
*   **Left medial geniculate body (contrast — the thalamic downstream
    auditory relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The
    Inferior Colliculus: A Hub for the Central Auditory System*. (Left
    medial geniculate body — downstream of the left LSO.)
*   **Left primary auditory cortex (contrast — the cortical downstream
    auditory target):** Pickles, J.O. (2015). *An Introduction to the
    Physiology of Hearing*, 4th ed. (Left primary auditory cortex —
    downstream of the left LSO.)
*   **SLEA (contrast — the left LSO is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the left LSO.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the left LSO.)
*   NeuroNames — Lateral superior olive (left); FMA — Lateral superior
    olive (left member).
"""
