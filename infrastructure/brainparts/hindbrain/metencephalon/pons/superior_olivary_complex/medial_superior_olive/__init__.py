"""
infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.medial_superior_olive
====================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── superior_olivary_complex
                └── medial_superior_olive   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Medial superior olive; MSO; medial superior olivary
nucleus; "the interaural time difference (ITD) coincidence detector."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nucleus** — a **bilateral collection of
anatomically delimited auditory coincidence-detector neurons** in the
**medial superior olivary complex**, the **principal substrate** of
**interaural time difference (ITD) processing** for **low-frequency
horizontal sound localization**. In **humans**, the **MSO** is the
**dominant binaural sound-localization nucleus** — it is **larger** than
the LSO and **dominates** ITD-based localization.
**Part of:** The **superior_olivary_complex** container — specifically,
the **binaural ITD-processing** component. The **superior olivary
complex** is the **pontine binaural sound-localization relay** of the
**ventral pontine tegmentum**.
**Structural parent:** ``.../superior_olivary_complex/`` → **direct
child** of the superior olivary complex container.
**Structural children:** **Two sub-containers** — ``left`` and ``right``
— the **bilateral halves** of the medial superior olive. Each of
``left`` and ``right`` is a **sub-container** (a **leaf** at the tree
level) whose **principal coincidence-detector neurons** and **local
circuit interneurons** are documented as **prose**, not as structural
children.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
medial superior olive is a CONTAINER, not a leaf.** It has **two
structural children** (``left`` and ``right``), each of which is a
**leaf** at the tree level. Consumers must **not** treat the medial
superior olive as a leaf, and must **not** assume the left and right
sub-containers are absent — they are the **direct structural children**
of the medial superior olive.
**Boundary status (BILATERAL CONTAINER — left and right are STRUCTURALLY
SYMMETRIC):** **Boundary case — the medial superior olive is a
BILATERAL container.** The **left** and **right** sub-containers are
**structurally symmetric** — same neuron populations (principal
coincidence-detector neurons; local circuit interneurons), same
functional system (ITD processing via coincidence detection), same
bilateral framing. The bilateral symmetry is **strict**. Consumers must
**not** assume a left/right asymmetry at the container level — the
container is a **strict mirror pair**. Any lateralization is documented
**inside the left and right sub-containers** and in the **Lateralization
Notes** below, not imported from elsewhere.
**Boundary status (EXCITATORY COINCIDENCE DETECTOR — NOT an inhibitory
relay):** **Boundary case — the medial superior olive is an EXCITATORY
COINCIDENCE DETECTOR, NOT an inhibitory relay.** The **MSO** principal
neurons are **excitatory (glutamatergic)** — they **receive bilateral
excitatory** input from the **ipsilateral cochlear nuclei** and the
**contralateral cochlear nuclei** (via the **trapezoid body**) and
**fire maximally** when the **ipsilateral** and **contralateral** inputs
arrive **simultaneously** (the **Jeffress coincidence-detection model**).
This is the **opposite** of the **glycinergic inhibitory relay** of the
**MNTB** (which converts the **excitatory** contralateral cochlear
nuclei input into an **inhibitory** input to the ipsilateral LSO).
**This distinction is functionally load-bearing** — the **MSO** is the
**neural substrate** of **ITD processing** (via **excitatory coincidence
detection**), whereas the **MNTB** is the **neural substrate** of
**contralateral inhibition** for **ILD processing**. Consumers must
**not** conflate the medial superior olive with an **inhibitory relay**
— it is the **excitatory coincidence-detector relay** of the superior
olivary complex.
**Boundary status (ITD PROCESSOR — NOT the ILD processor):** **Boundary
case — the medial superior olive is the ITD PROCESSOR, NOT the ILD
processor.** The **MSO** processes **interaural time differences**
(ITD) for **low-frequency horizontal sound localization** (< ~1.5 kHz
in humans). The **lateral superior olive (LSO)**
(``.../superior_olivary_complex/lateral_superior_olive/``) is the
**ILD processor** for **high-frequency horizontal sound localization**
(> ~1.5 kHz in humans). They are **DIFFERENT STRUCTURES** — different
binaural cues (ITD vs. ILD), different frequency ranges (low vs. high),
different neural mechanisms (coincidence detection for ITD vs.
excitation-inhibition for ILD). **This distinction is functionally
load-bearing** — the two binaural cues dominate at different frequency
ranges, and the **human MSO is the dominant binaural sound-localization
nucleus** (unlike in many other mammals). Consumers must **not** conflate
the medial superior olive with the lateral superior olive.
**Boundary status (NOT the MNTB — that is the INHIBITORY RELAY for ILD
processing):** **Boundary case — the medial superior olive is NOT the
medial nucleus of the trapezoid body (MNTB).** The **MNTB**
(``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``) is
the **glycinergic inhibitory relay** that **receives** the
**contralateral cochlear nuclei** input (via the **calyx of Held** in the
**trapezoid body**) and **projects** an **inhibitory (glycinergic)**
input to the **ipsilateral LSO** — it is the **inhibitory relay** for
**ILD processing**. The **MSO** (here) is the **excitatory coincidence
detector** for **ITD processing** — it **receives bilateral excitatory**
input and **performs** the **ITD computation** directly. They are
**DIFFERENT STRUCTURES** — different binaural cues (ITD vs. ILD),
different neural mechanisms (coincidence detection vs. inhibitory
relay). Consumers must **not** conflate the medial superior olive with
the medial nucleus of the trapezoid body.
**Boundary status (NOT the cochlear nuclei — those are the UPSTREAM
MONAURAL FIRST-ORDER RELAY):** **Boundary case — the medial superior
olive is NOT the cochlear nuclei.** The **cochlear nuclei**
(``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``
and ``.../right/``) are the **monaural first-order relay** that
**receive** the **monaural** auditory input from the **ipsilateral
cochlea**. The **bilateral cochlear nuclei** — especially the
**spherical bushy cells** in the **anterior ventral cochlear nucleus
(AVCN)** — **project** to the **MSO** via the **trapezoid body**
(ipsilaterally and contralaterally). The **MSO** (here) is the
**binaural second-order relay** that **receives bilateral excitatory**
cochlear nuclei input and **performs** the **ITD computation**. They are
**DIFFERENT STRUCTURES** — the **cochlear nuclei** are **monaural
first-order**; the **MSO** is **binaural second-order**. **This
distinction is clinically load-bearing** — a **cochlear nuclei lesion**
causes **ipsilateral sensorineural hearing loss**; an **MSO lesion**
causes **impaired ITD-based sound localization** (impaired
**low-frequency horizontal sound localization**) with **preserved
pure-tone thresholds**. Consumers must **not** conflate the medial
superior olive with the cochlear nuclei.
**Boundary status (NOT the trapezoid body — that is the WHITE-MATTER
AFFERENT TRACT):** **Boundary case — the medial superior olive is NOT
the trapezoid body.** The **trapezoid body** is the **white-matter
decussating tract** that **carries** the **bilateral auditory axons**
from the **cochlear nuclei** to the **superior olivary complex** —
including the **bilateral cochlear nuclei** projections to the **MSO**
(the **ipsilateral** and **contralateral** excitatory inputs). The
**MSO** (here) is the **grey-matter neuron cluster** that **receives**
the trapezoid-body axons. They are **DIFFERENT STRUCTURES** — the
**MSO** is grey matter; the **trapezoid body** is white matter.
Consumers must **not** conflate the medial superior olive with the
trapezoid body.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
EFFERENT TRACT):** **Boundary case — the medial superior olive is NOT
the lateral lemniscus.** The **lateral lemniscus** is the **white-matter
ascending tract** that **carries** the **efferent axons** from the
**superior olivary complex** (including the **MSO**) to the **inferior
colliculus**. The **MSO** (here) is the **grey-matter neuron cluster**
that **gives rise to** the lateral lemniscus axons. They are **DIFFERENT
STRUCTURES** — the **MSO** is grey matter; the **lateral lemniscus** is
white matter. Consumers must **not** conflate the medial superior olive
with the lateral lemniscus.
**Boundary status (NOT the inferior colliculus — that is the MIDBRAIN
DOWNSTREAM AUDITORY RELAY):** **Boundary case — the medial superior
olive is NOT the inferior colliculus.** The **inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
and ``.../right/``) is the **midbrain auditory relay** that **receives**
the **ascending auditory projections** from the **superior olivary
complex** (including the **MSO**, via the **lateral lemniscus**) and
**projects** to the **medial geniculate body**. The **MSO** (here) is
the **pontine ITD processor** — it is **upstream** of the inferior
colliculus. They are **DIFFERENT STRUCTURES** — the **MSO** is
**pontine** and **upstream**; the **inferior colliculus** is **midbrain**
and **downstream**. Consumers must **not** conflate the medial superior
olive with the inferior colliculus.
**Boundary status (NOT the medial geniculate body — that is the THALAMIC
DOWNSTREAM AUDITORY RELAY):** **Boundary case — the medial superior
olive is NOT the medial geniculate body.** The **medial geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
and ``.../right/``) is the **thalamic auditory relay** that **receives**
the **ascending auditory projections** from the **inferior colliculus**
and **projects** to the **primary auditory cortex**. The **MSO** (here)
is the **pontine ITD processor** — it is **upstream** of the medial
geniculate body. They are **DIFFERENT STRUCTURES** — the **MSO** is
**pontine** and **upstream**; the **medial geniculate body** is
**diencephalic** and **downstream**. Consumers must **not** conflate the
medial superior olive with the medial geniculate body.
**Boundary status (NOT the primary auditory cortex — that is the CORTICAL
DOWNSTREAM AUDITORY TARGET):** **Boundary case — the medial superior
olive is NOT the primary auditory cortex.** The **primary auditory
cortex** (Heschl's gyrus, Brodmann areas 41 and 42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
and ``.../right/``) is the **cortical target** of the **ascending
auditory pathway**. The **MSO** (here) is the **pontine ITD processor**
— it is **upstream** of the primary auditory cortex. They are
**DIFFERENT STRUCTURES** — the **MSO** is **pontine** and **upstream**;
the **primary auditory cortex** is **cortical** and **downstream**.
Consumers must **not** conflate the medial superior olive with the
primary auditory cortex.
**Boundary status (NOT the facial nerve nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the medial superior
olive is NOT the facial nerve nucleus.** The **facial nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
``.../right/``) is the **branchial motor** nucleus for the **muscles of
facial expression**. The **MSO** (here) is the **excitatory ITD
coincidence detector**. They are **DIFFERENT STRUCTURES** — different
functional systems (branchial motor vs. binaural ITD processing). They
are **anatomically adjacent** (both are in the **ventral pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the medial superior olive with the
facial nerve nucleus.
**Boundary status (NOT the abducens nucleus — that is an ANATOMICALLY
ADJACENT SIBLING):** **Boundary case — the medial superior olive is NOT
the abducens nucleus.** The **abducens nucleus**
(``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and ``.../right/``)
is the **somatic motor** nucleus for the **lateral rectus**. The **MSO**
(here) is the **excitatory ITD coincidence detector**. They are
**DIFFERENT STRUCTURES** — different functional systems (somatic motor
vs. binaural ITD processing). They are **anatomically adjacent** — the
**MSO** is **near the genu of the facial nerve** and the **abducens
nucleus**; this proximity is a **classic source of confusion** —
consumers must **not** conflate the medial superior olive with the
abducens nucleus.
**Boundary status (NOT the cochlear or vestibulocochlear nerve — those
are the PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE):** **Boundary
case — the medial superior olive is NOT the cochlear or
vestibulocochlear nerve.** The **cochlear nerve** (the cochlear
division of CN VIII) and the **vestibulocochlear nerve** (CN VIII) are
the **white-matter peripheral nerves** that **carry** the **primary
auditory axons** from the **spiral ganglion** to the **cochlear nuclei**.
The **MSO** (here) is the **central grey-matter binaural ITD processor**.
They are **DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **MSO** is **central grey matter**. Consumers must
**not** conflate the medial superior olive with the cochlear or
vestibulocochlear nerve.
**Boundary status (NOT the pons or the pontine tegmentum — those are the
GRANDPARENT and its tegmentum):** **Boundary case — the medial superior
olive is NOT the pons or the pontine tegmentum.** The **pons**
(``.../pons/``) is the **whole metencephalic brainstem segment**; the
**pontine tegmentum** is the **dorsal pontine grey-matter region**. The
**MSO** (here) is a **specific bilateral auditory coincidence-detector
nucleus** in the **ventral pontine tegmentum**. Consumers must **not**
conflate the medial superior olive with the **whole pons** or with the
**whole pontine tegmentum**.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
functionally distinct populations):** **Boundary case — the medial
superior olive is NOT a single uniform neuron population; it contains
MULTIPLE functionally distinct populations.** The **principal
coincidence-detector neurons** — the **excitatory (glutamatergic)**
bipolar neurons that **receive bilateral excitatory** input from the
**ipsilateral cochlear nuclei** and the **contralateral cochlear nuclei**
(via the **trapezoid body**) and **fire maximally** when the two inputs
arrive **simultaneously** (the **Jeffress coincidence-detection
model**) — they are the **ITD computation** output. The **local circuit
interneurons** — the **local neurons** that **modulate** the **principal
neurons**. **These populations are prose, not structural children.**
Consumers must **not** treat the medial superior olive as a single
uniform population — it is a **functionally heterogeneous nucleus** with
**distinct** sub-circuits.
**Boundary status (SLEA-FREE — the medial superior olive is NOT an
extended-amygdala component):** **Boundary case — the medial superior
olive is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **MSO** is a **binaural auditory ITD coincidence
detector** — it is **NOT** an extended-amygdala component, and it
carries **NO SLEA warning**. Consumers must **not** import the SLEA
warning into the medial superior olive — it is **SLEA-free**.

Overview
--------
The medial superior olive is the **excitatory coincidence detector** for
**interaural time difference (ITD) processing** — the **bilateral
collection** of **excitatory (glutamatergic) bipolar neurons** that
**receive bilateral excitatory** input from the **ipsilateral cochlear
nuclei** and the **contralateral cochlear nuclei** (via the **trapezoid
body**) and **fire maximally** when the two inputs arrive
**simultaneously** (the **Jeffress coincidence-detection model**) — the
**neural substrate** of **ITD processing** for **low-frequency
horizontal sound localization**. In **humans**, the **MSO** is the
**dominant binaural sound-localization nucleus** — it is **larger**
than the LSO and **dominates** ITD-based localization. It is a
**container** under the superior olivary complex container, with **two
structural children** (``left`` and ``right``) — the **bilateral halves**
of the MSO — each of which is a **leaf** at the tree level with **prose
neuron populations**.

**The medial superior olive is a CONTAINER, NOT a leaf.** Its structural
children are ``left`` and ``right`` — the **bilateral sub-containers**.

**The medial superior olive is a BILATERAL CONTAINER.** The ``left`` and
``right`` sub-containers are **structurally symmetric** — same neuron
populations, same functional system (ITD processing via coincidence
detection), same bilateral framing. The bilateral symmetry is **strict**.

**The medial superior olive is an EXCITATORY COINCIDENCE DETECTOR.** The
**MSO** principal neurons are **excitatory (glutamatergic)** — they
**fire maximally** when the **ipsilateral** and **contralateral** inputs
arrive **simultaneously**. This is the **neural substrate** of **ITD
processing** for **low-frequency horizontal sound localization**. **This
is the opposite of the glycinergic inhibitory relay of the MNTB** — the
MNTB **converts** the **excitatory** contralateral cochlear nuclei input
into an **inhibitory** input to the ipsilateral LSO, whereas the **MSO**
**uses** the **bilateral excitatory** cochlear nuclei input **directly**
to compute the **ITD**.

**The medial superior olive is the ITD PROCESSOR, not the ILD
processor.** The **MSO** processes **interaural time differences** for
**low-frequency horizontal sound localization**. The **LSO** processes
**interaural level differences** for **high-frequency horizontal sound
localization**. **This distinction is functionally load-bearing** — the
**human MSO** is the **dominant binaural sound-localization nucleus**
(the human LSO is smaller than in many other mammals).

**The medial superior olive is NOT the LSO, the MNTB, the cochlear
nuclei, the trapezoid body, the lateral lemniscus, the inferior
colliculus, the medial geniculate body, or the primary auditory
cortex.** Those are **different auditory structures** — the **LSO**
(ILD processor), the **MNTB** (inhibitory relay for ILD processing),
the **cochlear nuclei** (upstream monaural first-order relay), the
**trapezoid body** (afferent white-matter tract), the **lateral
lemniscus** (efferent white-matter tract), and the **downstream**
midbrain/thalamic/cortical auditory relays. The **MSO** is the
**excitatory coincidence detector** — the **intrinsic superior olivary
complex node** that makes **ITD processing possible**.

**The medial superior olive is a TWO-POPULATION complex.** The
**principal coincidence-detector neurons** (excitatory bipolar neurons
receiving bilateral cochlear nuclei input) and the **local circuit
interneurons** are **prose**, not structural children.

**The medial superior olive is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Sub-Container and Neuron Population Composition (structural children
and prose, not structural grandchildren)
----------------------------------------
The medial superior olive contains **two structural children** — the
``left`` and ``right`` sub-containers — each of which is a **leaf** at
the tree level with **prose neuron populations**:

*   **Left medial superior olive**
    (``.../medial_superior_olive/left/``) — the **left excitatory
    coincidence detector**. It **receives bilateral excitatory** input
    from the **left cochlear nuclei** (ipsilateral) and the **right
    cochlear nuclei** (contralateral, via the **right trapezoid
    body**) and **fires maximally** when the two inputs arrive
    **simultaneously** — it **encodes** the **ITD** for **sound sources
    on the left side** and the **midline** (depending on the ITD). The
    **left MSO** is the **neural substrate** of **left-sided ITD
    processing** — the **excitatory coincidence detector** that
    **enables** the **left MSO neuron** to **encode** the **horizontal
    sound-source location** on the **left side** and the **midline**
    (for **low-frequency sounds**).

*   **Right medial superior olive**
    (``.../medial_superior_olive/right/``) — the **right excitatory
    coincidence detector**. It **receives bilateral excitatory** input
    from the **right cochlear nuclei** (ipsilateral) and the **left
    cochlear nuclei** (contralateral, via the **left trapezoid body**)
    and **fires maximally** when the two inputs arrive
    **simultaneously** — it **encodes** the **ITD** for **sound sources
    on the right side** and the **midline** (depending on the ITD). The
    **right MSO** is the **neural substrate** of **right-sided ITD
    processing** — the **excitatory coincidence detector** that
    **enables** the **right MSO neuron** to **encode** the **horizontal
    sound-source location** on the **right side** and the **midline**
    (for **low-frequency sounds**).

**Each of the left and right sub-containers contains two prose neuron
populations** — the **principal coincidence-detector neurons**
(excitatory bipolar neurons receiving bilateral cochlear nuclei input)
and the **local circuit interneurons**. **These populations are prose,
not structural children** — the ``left`` and ``right`` sub-containers
are **leaves** at the tree level.

The MSO / LSO Boundary
----------------------
This is the **sibling** boundary — **ITD processor vs. ILD processor**:

*   **Medial superior olive** (this module) — the **ITD processor** for
    **low-frequency horizontal sound localization**.

*   **Lateral superior olive (LSO)**
    (``.../superior_olivary_complex/lateral_superior_olive/``) — the
    **ILD processor** for **high-frequency horizontal sound
    localization**.

**They are DIFFERENT STRUCTURES** — different binaural cues (ITD vs.
ILD), different frequency ranges (low vs. high), different neural
mechanisms (coincidence detection for ITD vs. excitation-inhibition for
ILD). **This distinction is functionally load-bearing** — the **human
MSO is the dominant binaural sound-localization nucleus**. Consumers
must **not** conflate the medial superior olive with the lateral
superior olive.

The MSO / MNTB Boundary
-----------------------
This is the **sibling** boundary — **ITD processor vs. inhibitory
relay**:

*   **Medial superior olive** (this module) — the **excitatory ITD
    coincidence detector**.

*   **Medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``)
    — the **glycinergic inhibitory relay** for **ILD processing** — it
    **receives** the **contralateral cochlear nuclei** input and
    **projects** an **inhibitory input** to the **ipsilateral LSO**.

**They are DIFFERENT STRUCTURES** — different functional roles
(excitatory coincidence detector vs. inhibitory relay), different
binaural cues (ITD vs. ILD). Consumers must **not** conflate the medial
superior olive with the medial nucleus of the trapezoid body.

The MSO / Cochlear Nuclei Boundary
----------------------------------
This is the **binaural second-order vs. monaural first-order** boundary:

*   **Medial superior olive** (this module) — the **binaural
    second-order relay** that **receives bilateral excitatory** cochlear
    nuclei input and **performs** the **ITD computation**.

*   **Cochlear nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``
    and ``.../right/``) — the **monaural first-order relay** that
    **receive** the **monaural** auditory input from the **ipsilateral
    cochlea** — the **bilateral spherical bushy cells** in the **AVCN**
    **project** to the **MSO** via the **trapezoid body**
    (ipsilaterally and contralaterally).

**They are DIFFERENT STRUCTURES** — the **cochlear nuclei** are
**monaural first-order**; the **MSO** is **binaural second-order**.
**This distinction is clinically load-bearing** — a **cochlear nuclei
lesion** causes **ipsilateral sensorineural hearing loss**; an **MSO
lesion** causes **impaired ITD-based sound localization** (impaired
**low-frequency horizontal sound localization**) with **preserved
pure-tone thresholds**. Consumers must **not** conflate the medial
superior olive with the cochlear nuclei.

The MSO / Trapezoid Body Boundary
---------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Medial superior olive** (this module) — the **grey-matter neuron
    cluster** that **receives** the trapezoid-body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the **bilateral auditory axons** from the **cochlear
    nuclei** to the **superior olivary complex** (including the
    **bilateral cochlear nuclei** projections to the **MSO**).

**They are DIFFERENT STRUCTURES** — the **MSO** is grey matter; the
**trapezoid body** is white matter. Consumers must **not** conflate the
medial superior olive with the trapezoid body.

The MSO / Lateral Lemniscus Boundary
------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Medial superior olive** (this module) — the **grey-matter neuron
    cluster** that **gives rise to** the lateral lemniscus axons.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the **efferent axons** from the **superior olivary
    complex** (including the **MSO**) to the **inferior colliculus**.

**They are DIFFERENT STRUCTURES** — the **MSO** is grey matter; the
**lateral lemniscus** is white matter. Consumers must **not** conflate
the medial superior olive with the lateral lemniscus.

The MSO / Inferior Colliculus Boundary
--------------------------------------
This is the **pontine ITD processor vs. midbrain downstream relay**
boundary:

*   **Medial superior olive** (this module) — the **pontine ITD
    processor**.

*   **Inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
    and ``.../right/``) — the **midbrain auditory relay** that
    **receives** the **ascending auditory projections** from the
    **superior olivary complex** (including the **MSO**, via the
    **lateral lemniscus**) and **projects** to the **medial geniculate
    body**.

**They are DIFFERENT STRUCTURES** — the **MSO** is **pontine** and
**upstream**; the **inferior colliculus** is **midbrain** and
**downstream**. Consumers must **not** conflate the medial superior
olive with the inferior colliculus.

The MSO / Medial Geniculate Body Boundary
-----------------------------------------
This is the **pontine ITD processor vs. thalamic downstream relay**
boundary:

*   **Medial superior olive** (this module) — the **pontine ITD
    processor**.

*   **Medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
    and ``.../right/``) — the **thalamic auditory relay** that
    **receives** the **ascending auditory projections** from the
    **inferior colliculus** and **projects** to the **primary auditory
    cortex**.

**They are DIFFERENT STRUCTURES** — the **MSO** is **pontine** and
**upstream**; the **medial geniculate body** is **diencephalic** and
**downstream**. Consumers must **not** conflate the medial superior
olive with the medial geniculate body.

The MSO / Primary Auditory Cortex Boundary
------------------------------------------
This is the **pontine ITD processor vs. cortical downstream target**
boundary:

*   **Medial superior olive** (this module) — the **pontine ITD
    processor**.

*   **Primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
    42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
    and ``.../right/``) — the **cortical target** of the **ascending
    auditory pathway**.

**They are DIFFERENT STRUCTURES** — the **MSO** is **pontine** and
**upstream**; the **primary auditory cortex** is **cortical** and
**downstream**. Consumers must **not** conflate the medial superior
olive with the primary auditory cortex.

The MSO / Facial Nerve Nucleus Boundary
---------------------------------------
This is the **auditory binaural relay vs. branchial motor** boundary:

*   **Medial superior olive** (this module) — the **excitatory ITD
    coincidence detector**.

*   **Facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
    ``.../right/``) — the **branchial motor** nucleus for the **muscles
    of facial expression**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. branchial motor). They are
**anatomically adjacent** — consumers must **not** conflate the medial
superior olive with the facial nerve nucleus.

The MSO / Abducens Nucleus Boundary
-----------------------------------
This is the **auditory binaural relay vs. somatic motor** boundary:

*   **Medial superior olive** (this module) — the **excitatory ITD
    coincidence detector**.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and
    ``.../right/``) — the **somatic motor** nucleus for the **lateral
    rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. somatic motor). They are
**anatomically adjacent** — consumers must **not** conflate the medial
superior olive with the abducens nucleus.

The MSO / Cochlear and Vestibulocochlear Nerves Boundary
--------------------------------------------------------
This is the **central grey matter vs. peripheral white matter** boundary:

*   **Medial superior olive** (this module) — the **central grey-matter
    binaural ITD processor**.

*   **Cochlear nerve** (the cochlear division of CN VIII) and
    **vestibulocochlear nerve** (CN VIII) — the **peripheral white-matter
    nerves** that **carry** the **primary auditory axons** from the
    **spiral ganglion** to the **cochlear nuclei**.

**They are DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **MSO** is **central grey matter**. Consumers must
**not** conflate the medial superior olive with the cochlear or
vestibulocochlear nerve.

The MSO / Superior Olivary Complex Container Boundary
-----------------------------------------------------
This is the **sub-container vs. parent** boundary:

*   **Medial superior olive** (this module) — the **excitatory ITD
    coincidence detector** — one of the **three sub-nuclei** of the
    superior olivary complex.

*   **Superior olivary complex container**
    (``.../superior_olivary_complex/``) — the **pontine binaural
    sound-localization relay** that **contains** the **LSO**, the
    **MSO**, and the **MNTB**.

**The medial superior olive is a child of the superior olivary
complex.** Consumers must **not** conflate the medial superior olive
with the **whole superior olivary complex**.

The MSO / SLEA Boundary
-----------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Medial superior olive** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The medial superior olive is NOT part of the SLEA continuum.** It is a
**binaural auditory ITD processor**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the medial superior
olive.

Function in the Human Brain
---------------------------
The medial superior olive's functions are **interaural time difference
(ITD) processing** for **low-frequency horizontal sound localization** —
**NOT a single unified function**:

*   **ITD Computation (Excitatory Coincidence Detection):** The **MSO**
    is the **excitatory coincidence detector** for **ITD processing**.
    It **receives bilateral excitatory** input from the **ipsilateral
    cochlear nuclei** and the **contralateral cochlear nuclei** (via the
    **trapezoid body**) and **fires maximally** when the two inputs
    arrive **simultaneously** (the **Jeffress coincidence-detection
    model**). **The MSO neuron** is a **coincidence detector** — it
    **encodes** the **ITD** (the **difference in arrival time** of a
    sound at the two ears) in its **firing rate**. **ITD** is the
    **dominant cue** for **horizontal sound localization** of
    **low-frequency sounds** (< ~1.5 kHz in humans) — because
    **low-frequency sounds** are **not shadowed** by the **head** (the
    **head shadow effect** is **negligible** at low frequencies), the
    **level difference** between the two ears is **small**, and the
    **time difference** is the **dominant binaural cue**.

*   **Low-Frequency Horizontal Sound Localization:** The **MSO** is the
    **dominant binaural cue** for **low-frequency sound localization**
    (< ~1.5 kHz in humans) of **sound sources** across the
    **horizontal plane** — because **low-frequency sounds** have
    **long wavelengths** that **diffract around the head**, so the
    **sound level** at the two ears is **nearly the same**, and the
    **time of arrival** is the **dominant binaural cue**. The **MSO**
    **computes** the **interaural time difference** and **encodes** the
    **horizontal sound-source location** in its **firing rate**.

*   **Human MSO Dominance:** In **humans**, the **MSO** is the
    **dominant binaural sound-localization nucleus** — it is **larger**
    than the LSO, and it **dominates ITD-based localization** for
    **low-frequency sounds** (the **LSO** is **smaller** in humans than
    in many other mammals, and its **ILD-based function** is
    **secondary** to the **MSO's ITD-based function**). The **human
    MSO** is the **primary neural substrate** of **low-frequency
    horizontal sound localization**.

*   **NOT a neural processor in the classical sense.** The **MSO** is a
    **binaural coincidence detector** — it **receives** the
    **bilateral excitatory** auditory inputs and **performs** the **ITD
    computation** — it **projects** the **binaural representation** to
    the **inferior colliculus** (via the **lateral lemniscus**). The
    **processing** of **binaural sound localization** is **distributed**
    across the **cochlear nuclei** (monaural auditory processing), the
    **MSO** (ITD processing), the **LSO** (ILD processing), the
    **inferior colliculus** (integration of binaural and spectral cues
    and auditory space map), the **medial geniculate body** (thalamic
    relay), and the **primary auditory cortex** (cortical processing).
    The **MSO** is the **ITD processor** — the **brainstem substrate**
    of **low-frequency horizontal sound localization**.

**The unifying theme:** the medial superior olive is the **binaural ITD
processor** — the **excitatory coincidence detector** that **computes**
the **interaural time difference** for **low-frequency horizontal sound
localization**. It is a **bilateral container** (left and right
sub-containers), **two-population** (principal coincidence-detector
neurons; local circuit interneurons), **excitatory (glutamatergic)**,
**SLEA-free**, and **NOT the LSO** (the **LSO** is the **ILD processor**
for **high-frequency** sound localization) — the **MSO** is the **ITD
processor** for **low-frequency** sound localization.

Associated Disorders
--------------------
The medial superior olive has **no named "medial superior olive
syndrome"** — its clinical associations are **binaural-specific**:

*   **MSO Lesion — Impaired ITD-Based Sound Localization with Preserved
    Pure-Tone Thresholds:** A lesion of the **medial superior olive**
    (e.g. **pontine stroke**, **tumor**, **demyelination**) causes
    **impaired ITD-based sound localization** (impaired **low-frequency
    horizontal sound localization**) with **preserved pure-tone
    thresholds** (because the **monaural auditory pathway** — the
    **cochlear nuclei** and the **ascending auditory pathway** — is
    intact). **The ITD-specific pattern** is the **substrate** of the
    **MSO** function — this is the **"ITD-specific binaural deficit"**
    that **distinguishes** an **MSO lesion** from a **cochlear nuclei
    lesion** (which causes **sensorineural hearing loss**) or an
    **LSO lesion** (which causes **ILD-specific binaural deficit**).

*   **Low-Frequency Horizontal Sound Localization Deficit — MSO
    Involvement:** **Low-frequency horizontal sound localization**
    depends on **ITD processing**, which is **subserved** by the **MSO**.
    **The MSO** is **one of the neural substrates** of **ITD-based
    sound localization**, and its dysfunction may **contribute** to
    **low-frequency horizontal sound localization deficits** —
    especially in **patients with pontine lesions** or **age-related
    hearing loss** (presbycusis).

*   **Presbycusis — MSO Involvement:** **Presbycusis** (age-related
    hearing loss) is characterized by **peripheral auditory dysfunction**
    (cochlear hair cell loss) **and central auditory dysfunction**
    (including **MSO** dysfunction — **reduced neuron number**,
    **reduced synaptic density**, and **reduced ITD processing**). The
    **MSO** may show **age-related changes** — contributing to
    **impaired low-frequency horizontal sound localization** and
    **impaired speech understanding in noise** in **older adults**.

*   **Multiple Sclerosis — MSO Involvement:** **Multiple sclerosis** can
    affect the **MSO** (as a **brainstem demyelinating lesion**),
    contributing to **impaired ITD-based sound localization** and
    **binaural hearing deficits**.

*   **Pontine Stroke — MSO Involvement:** A **pontine stroke** (e.g.
    **basilar artery** perforator territory) involving the **MSO** causes
    **impaired ITD-based sound localization** — often accompanied by
    **other pontine signs** (**hemiparesis**, **facial palsy**,
    **abducens palsy**, **cerebellar ataxia**).

*   **Binaural Hearing Deficit — MSO Involvement:** **Binaural hearing**
    is the **ability to use** the **differences** between the **two
    ears** to **localize sound** and to **understand speech in noise**
    (the **binaural squelch effect** and the **binaural summation
    effect**). **The MSO** is **one of the neural substrates** of
    **binaural hearing** (specifically **ITD-based binaural processing**
    — the **dominant** binaural cue for **low-frequency sound
    localization** in humans), and its dysfunction may **contribute** to
    **binaural hearing deficits** — **impaired sound localization**,
    **impaired speech understanding in noise**, and **impaired binaural
    unmasking**.

*   **No Named "MSO Syndrome":** The medial superior olive is a
    **bilateral container** of **two functionally distinct neuron
    populations** — it has **no named clinical syndrome** of its own.
    Its clinical relevance is **ITD-specific** — **impaired ITD-based
    sound localization**, **impaired low-frequency horizontal sound
    localization**, and **impaired binaural hearing**.

**What is NOT here:** The medial superior olive is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **vestibular neuritis** (vestibular nerve), **labyrinthitis**
(inner ear), or **auditory neuropathy spectrum disorder** (cochlear nerve
or hair cell). Its clinical relevance is **ITD-specific**, via the
**interaural time difference (ITD) processing** it subserves. **No named
MSO syndrome exists.**

Lateralization Notes
--------------------
This is the **bilateral** medial superior olive container. The MSO is
**bilaterally symmetric** with the **left** and **right**
sub-containers **strictly mirrored** — and it carries **NO warning at
the container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right**
    sub-containers are **structurally identical** — same neuron
    populations (principal coincidence-detector neurons; local circuit
    interneurons), same functional system (ITD processing via
    coincidence detection), same bilateral framing. The bilateral
    symmetry is **strict**.

*   **Bilateral Excitatory Input (Structural Fact, NOT a Lateralization
    Warning):** The **left MSO** receives **bilateral excitatory** input
    from the **left cochlear nuclei** (ipsilateral) and the **right
    cochlear nuclei** (contralateral, via the **right trapezoid
    body**). The **right MSO** receives **bilateral excitatory** input
    from the **right cochlear nuclei** (ipsilateral) and the **left
    cochlear nuclei** (contralateral, via the **left trapezoid body**).
    **This bilateral excitatory input** is a **structural fact** of the
    **MSO** — it is **not** a functional lateralization. It is the
    **neural substrate** of the **MSO's role as the coincidence
    detector** for **ITD processing** — the **MSO neuron** **fires
    maximally** when the **ipsilateral** and **contralateral** inputs
    arrive **simultaneously** (the **Jeffress coincidence-detection
    model**).

*   **ITD Computation Across the Horizontal Plane (Structural Fact, NOT
    a Lateralization Warning):** The **MSO** population (left and right
    MSO **together**) **encodes** the **ITD** for **sound sources**
    across the **entire horizontal plane** — the **left MSO** encodes
    **left-sided** and **midline** sound sources (via the **left
    MSO's** coincidence detection of **left-ear** and **right-ear**
    inputs), and the **right MSO** encodes **right-sided** and
    **midline** sound sources. **This ITD computation** is a
    **structural fact** of the **binaural sound-localization system**
    — it is **not** a functional lateralization. It is the **neural
    substrate** of the **human ITD-based horizontal sound-localization
    ability**.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The MSO is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the MSO.

*   **NO Amygdala-Lateralization Warning of their own (the MSO is
    BINAURAL AUDITORY, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The MSO is a **binaural auditory ITD coincidence
    detector** — consumers must **not** conflate it with the
    **amygdala** or with the **fear circuit**.

**A consumer that assumes "left MSO = right MSO" will be structurally
correct** — the two sides are **strictly symmetric** (the bilateral
excitatory input and the ITD computation across the horizontal plane are
structural facts, not lateralizations). The MSO is a **strict-mirror
pair with NO warning at the container level** — **no SLEA warning**,
**no amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The container is **bilateral**, but
    it does **not** import ``left`` or ``right`` at module level — it
    exposes them as **structural children** and lets consumers resolve
    them through the memory/recall layer.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../superior_olivary_complex/lateral_superior_olive/``,
    ``.../superior_olivary_complex/medial_nucleus_of_trapezoid_body/``,
    ``.../superior_olivary_complex/``, ``.../pons/tegmentum/``,
    ``.../pons/cranial_nerve_nuclei/``, ``.../midbrain/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    MSO's relationships to the **LSO**, the **MNTB**, the **cochlear
    nuclei**, the **trapezoid body**, the **lateral lemniscus**, the
    **inferior colliculus**, the **medial geniculate body**, the
    **primary auditory cortex**, the **facial nerve nucleus**, the
    **abducens nucleus**, the **cochlear** and **vestibulocochlear
    nerves**, the **whole superior olivary complex**, and the **SLEA
    continuum** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children `left` and `right`, each a
    leaf at the tree level with prose neuron populations.** The **left**
    and **right** sub-containers are **leaves** at the tree level — they
    have **no structural children**, but they contain **prose neuron
    populations** (principal coincidence-detector neurons; local circuit
    interneurons). Consumers must not conflate the container with its
    children.
*   **BILATERAL CONTAINER — left and right are STRUCTURALLY SYMMETRIC.**
    The **left** and **right** sub-containers are a **strict-mirror
    pair** with **no warning at the container level**. Any
    lateralization is documented **inside the left and right
    sub-containers** and in the **Lateralization Notes**.
*   **EXCITATORY COINCIDENCE DETECTOR — NOT an inhibitory relay.** The
    **MSO** neurons are **excitatory (glutamatergic)** — they **fire
    maximally** when the **ipsilateral** and **contralateral** inputs
    arrive **simultaneously** (the **Jeffress coincidence-detection
    model**). This is the **opposite** of the **glycinergic inhibitory
    relay** of the **MNTB**. Consumers must **not** conflate the MSO
    with an **inhibitory relay**.
*   **ITD PROCESSOR — NOT the ILD processor (LSO).** The **MSO**
    processes **interaural time differences** for **low-frequency
    horizontal sound localization**; the **LSO** processes **interaural
    level differences** for **high-frequency horizontal sound
    localization**. Consumers must **not** conflate the MSO with the
    LSO.
*   **NOT the MNTB — that is the INHIBITORY RELAY for ILD processing.**
    Consumers must **not** conflate the MSO with the MNTB.
*   **NOT the cochlear nuclei — those are the UPSTREAM monaural
    first-order relay.** Consumers must **not** conflate the MSO with
    the cochlear nuclei.
*   **NOT the trapezoid body or the lateral lemniscus — those are the
    WHITE-MATTER TRACTS.** Consumers must **not** conflate the MSO with
    either tract.
*   **NOT the inferior colliculus, the medial geniculate body, or the
    primary auditory cortex — those are DOWNSTREAM AUDITORY
    STRUCTURES.** Consumers must **not** conflate the MSO with any of
    them.
*   **NOT the facial nerve nucleus or the abducens nucleus — those are
    ANATOMICALLY ADJACENT SIBLINGS.** Consumers must **not** conflate
    the MSO with either of them.
*   **NOT the cochlear or vestibulocochlear nerve — those are the
    PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE.** Consumers must
    **not** conflate the MSO with either nerve.
*   **NOT the whole superior olivary complex — that is the PARENT.**
    Consumers must **not** conflate the MSO with the whole superior
    olivary complex.
*   **MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — NOT a single uniform
    nucleus.** The **principal coincidence-detector neurons**
    (excitatory bipolar neurons) and the **local circuit interneurons**
    are **prose**, not structural children. Consumers must **not** treat
    the MSO as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The MSO is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the MSO is BINAURAL AUDITORY.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **MSO** is a **binaural auditory ITD processor** — it
    is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The MSO is a local container under the
    superior_olivary_complex container, not a cross-listed container.
*   **No nested cross-listing.** The MSO has no nested dual-framing
    module. It is a single bilateral container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex import medial_superior_olive

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex."
        "medial_superior_olive"
    )

**Do not** assume the MSO is a **leaf**. It is a **container** — its
structural children are ``left`` and ``right``, each of which is a
**leaf** at the tree level with **prose neuron populations**.

**Do not** assume the MSO is an **inhibitory relay**. The **MSO**
neurons are **excitatory (glutamatergic)** — they **fire maximally**
when the **ipsilateral** and **contralateral** inputs arrive
**simultaneously**.

**Do not** assume the MSO is the **LSO** (the **ILD processor** for
**high-frequency** sound localization) or the **MNTB** (the **inhibitory
relay** for **ILD processing**). The **MSO** is the **ITD processor**
for **low-frequency** sound localization.

**Do not** assume the MSO is the **cochlear nuclei**, the **trapezoid
body**, the **lateral lemniscus**, the **inferior colliculus**, the
**medial geniculate body**, or the **primary auditory cortex**. Those are
**different auditory structures** — the **cochlear nuclei** (upstream
monaural first-order relay), the **trapezoid body** (afferent
white-matter tract), the **lateral lemniscus** (efferent white-matter
tract), and the **downstream** midbrain/thalamic/cortical auditory
relays.

**Do not** assume the MSO is the **facial nerve nucleus** or the
**abducens nucleus**. Those are **anatomically adjacent siblings** —
different functional systems.

**Do not** assume the MSO is the **cochlear nerve** or the
**vestibulocochlear nerve**. Those are the **peripheral auditory
conduction infrastructure** — the MSO is **central grey matter**.

**Do not** assume the MSO is the **whole superior olivary complex**. The
**superior olivary complex** is the **parent** — the **MSO** is one of
its **three sub-nuclei**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the MSO. **The MSO is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the MSO's structural children (recommended consumer pattern)::

    MEDIAL_SUPERIOR_OLIVE_CHILDREN = ("left", "right")
    # The container is bilateral. The left and right sub-containers are
    # LEAVES at the tree level, with prose neuron populations (principal
    # coincidence-detector neurons; local circuit interneurons).

Iterating the MSO's left and right sub-containers (recommended consumer
pattern)::

    for side in ("left", "right"):
        mso_side_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"medial_superior_olive.{side}"
        )
        # resolve mso_side_path through the memory/recall layer

Reaching the LSO (recommended consumer pattern — the ILD processor
sibling)::

    # The LSO is the ILD PROCESSOR sibling under the
    # superior_olivary_complex container:
    #
    #   .../superior_olivary_complex/lateral_superior_olive/
    #
    # The LSO processes INTERAURAL LEVEL DIFFERENCES for HIGH-FREQUENCY
    # sound localization; the MSO processes INTERAURAL TIME DIFFERENCES
    # for LOW-FREQUENCY sound localization.

Reaching the MNTB (recommended consumer pattern — the inhibitory relay
sibling for ILD processing)::

    # The MNTB is the INHIBITORY RELAY sibling under the
    # superior_olivary_complex container:
    #
    #   .../superior_olivary_complex/medial_nucleus_of_trapezoid_body/
    #
    # The MNTB is the GLYCINERGIC INHIBITORY RELAY for ILD processing
    # (it converts excitatory contralateral cochlear nuclei input into
    # inhibitory input to the ipsilateral LSO); the MSO is the EXCITATORY
    # COINCIDENCE DETECTOR for ITD processing. They are DIFFERENT
    # STRUCTURES with DIFFERENT binaural cues.

Reaching the cochlear nuclei (recommended consumer pattern — the
UPSTREAM MONAURAL FIRST-ORDER RELAY)::

    # The cochlear nuclei are the UPSTREAM MONAURAL FIRST-ORDER relay —
    # the bilateral cochlear nuclei (specifically the spherical bushy
    # cells in the AVCN) project to the MSO via the trapezoid body:
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/  (and right/)
    #
    # The cochlear nuclei are UPSTREAM (monaural first-order); the MSO is
    # DOWNSTREAM (binaural second-order excitatory coincidence detector).

Reaching the trapezoid body (recommended consumer pattern — the
white-matter afferent tract)::

    # The trapezoid body is the WHITE-MATTER afferent tract that carries
    # the bilateral cochlear nuclei axons to the MSO:
    #
    #   .../white_matter/.../trapezoid_body/  (or equivalent path)
    #
    # The MSO RECEIVES the trapezoid body axons; the trapezoid body is
    # the AFFERENT limb of the ITD-processing pathway.

Reaching the lateral lemniscus (recommended consumer pattern — the
white-matter efferent tract)::

    # The lateral lemniscus is the WHITE-MATTER efferent tract from the
    # MSO (and the LSO) to the inferior colliculus:
    #
    #   .../white_matter/.../lateral_lemniscus/  (or equivalent path)
    #
    # The MSO GIVES RISE TO the lateral lemniscus axons; the lateral
    # lemniscus is the EFFERENT limb of the ITD-processing pathway.

Reaching the inferior colliculus (recommended consumer pattern — the
DOWNSTREAM midbrain auditory relay)::

    # The inferior colliculus is the DOWNSTREAM midbrain auditory relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/  (and right/)
    #
    # The MSO is UPSTREAM of the inferior colliculus; the inferior
    # colliculus is DOWNSTREAM of the MSO.

Reaching the whole superior olivary complex container (recommended
consumer pattern — the PARENT)::

    # The superior olivary complex container is the PONTINE BINAURAL
    # SOUND-LOCALIZATION RELAY parent that CONTAINS the LSO, the MSO,
    # and the MNTB:
    #
    #   .../superior_olivary_complex/
    #
    # The MSO is one of the THREE SUB-NUCLEI of the superior olivary
    # complex.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mso_side_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"medial_superior_olive.{side}"
        )
        # resolve mso_side_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The MSO's neuron populations are prose, not modules:
    #   principal coincidence-detector neurons (excitatory, glutamatergic
    #       bipolar neurons) -> receive bilateral excitatory cochlear
    #       nuclei input (via trapezoid body); fire maximally when
    #       ipsilateral and contralateral inputs arrive simultaneously
    #       (Jeffress coincidence-detection model); the ITD computation
    #       output
    #   local circuit interneurons -> modulate the principal neurons
    #       within the MSO
    #
    # Do not attempt to resolve these as sub-paths of the MSO — resolve
    # them at the neuron-population level through the references.

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
*   **Pontine stroke — MSO involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — MSO involvement; binaural hearing
    deficits.)
*   **LSO (contrast — the ILD processor sibling):** Tollin, D.J. (2003).
    "The lateral superior olive as a source of ascending and descending
    auditory pathways." *Journal of the Association for Research in
    Otolaryngology* 4:311–327. (LSO — ILD processing; sibling of the
    MSO.)
*   **MNTB (contrast — the inhibitory relay sibling for ILD
    processing):** Smith, P.H., Joris, P.X., Yin, T.C.T. (1998).
    "Anatomy and physiology of principal cells of the medial nucleus of
    the trapezoid body (MNTB) of the cat." *Journal of Neurophysiology*
    79:3127–3142. (MNTB — glycinergic inhibitory relay for ILD
    processing; sibling of the MSO.)
*   **Cochlear nuclei (contrast — the UPSTREAM monaural first-order
    relay):** Cant, N.B., Benson, C.G. (2003). "Parallel auditory
    pathways: projection patterns of the different neuronal populations
    in the cochlear nuclei." *Brain Research Bulletin* 60:457–474.
    (Cochlear nuclei — monaural first-order relay; projects to the MSO
    via the trapezoid body.)
*   **Trapezoid body (contrast — the white-matter afferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Trapezoid body — afferent white-matter tract
    from the cochlear nuclei to the MSO.)
*   **Lateral lemniscus (contrast — the white-matter efferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Lateral lemniscus — efferent white-matter tract
    from the MSO to the inferior colliculus.)
*   **Inferior colliculus (contrast — the midbrain downstream auditory
    relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002). "The
    inferior colliculus: a hub for the central auditory system." In
    *Integrative Functions in the Mammalian Auditory Pathway*. (Inferior
    colliculus — downstream of the MSO.)
*   **Medial geniculate body (contrast — the thalamic downstream
    auditory relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The
    Inferior Colliculus: A Hub for the Central Auditory System*. (Medial
    geniculate body — downstream of the MSO.)
*   **Primary auditory cortex (contrast — the cortical downstream
    auditory target):** Pickles, J.O. (2015). *An Introduction to the
    Physiology of Hearing*, 4th ed. (Primary auditory cortex —
    downstream of the MSO.)
*   **Facial nerve nucleus (contrast — the adjacent branchial motor
    nucleus):** May, M., Schaitkin, B.M. (2000). *The Facial Nerve*, 2nd
    ed. (Facial nerve nucleus — anatomically adjacent to the MSO;
    functionally distinct.)
*   **Abducens nucleus (contrast — the adjacent somatic motor
    nucleus):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye
    Movements*, 5th ed. (Abducens nucleus — anatomically adjacent to the
    MSO; functionally distinct.)
*   **SLEA (contrast — the MSO is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the MSO.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the MSO.)
*   NeuroNames — Medial superior olive; FMA — Medial superior olive.
"""
