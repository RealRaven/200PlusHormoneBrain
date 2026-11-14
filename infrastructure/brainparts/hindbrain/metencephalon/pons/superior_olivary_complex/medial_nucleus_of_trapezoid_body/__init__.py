"""
infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex.medial_nucleus_of_trapezoid_body
==============================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── superior_olivary_complex
                └── medial_nucleus_of_trapezoid_body   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Medial nucleus of the trapezoid body; MNTB; medial
trapezoid body nucleus; "the glycinergic inhibitory relay for ILD
processing."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A **brainstem
special sensory nucleus** — a **bilateral collection of anatomically
delimited glycinergic inhibitory neurons** in the **medial superior
olivary complex**, the **principal inhibitory relay** that converts the
**excitatory contralateral cochlear nuclei input** into an
**inhibitory input** to the **ipsilateral lateral superior olive (LSO)**
— the **neural substrate** of **contralateral inhibition** essential for
**interaural level difference (ILD) processing**.
**Part of:** The **superior_olivary_complex** container — specifically,
the **binaural inhibitory relay** component. The **superior olivary
complex** is the **pontine binaural sound-localization relay** of the
**ventral pontine tegmentum**.
**Structural parent:** ``.../superior_olivary_complex/`` → **direct
child** of the superior olivary complex container.
**Structural children:** **Two sub-containers** — ``left`` and ``right``
— the **bilateral halves** of the medial nucleus of the trapezoid body.
Each of ``left`` and ``right`` is a **sub-container** (a **leaf** at the
tree level) whose **principal neurons (calyx of Held-receiving
glycinergic neurons)** and **local circuit interneurons** are documented
as **prose**, not as structural children.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
medial nucleus of the trapezoid body is a CONTAINER, not a leaf.** It has
**two structural children** (``left`` and ``right``), each of which is a
**leaf** at the tree level. Consumers must **not** treat the medial
nucleus of the trapezoid body as a leaf, and must **not** assume the
left and right sub-containers are absent — they are the **direct
structural children** of the medial nucleus of the trapezoid body.
**Boundary status (BILATERAL CONTAINER — left and right are STRUCTURALLY
SYMMETRIC):** **Boundary case — the medial nucleus of the trapezoid body
is a BILATERAL container.** The **left** and **right** sub-containers
are **structurally symmetric** — same neuron populations (calyx of
Held-receiving glycinergic neurons; local circuit interneurons), same
functional system (inhibitory relay for ILD processing), same bilateral
framing. The bilateral symmetry is **strict**. Consumers must **not**
assume a left/right asymmetry at the container level — the container is
a **strict mirror pair**. Any lateralization is documented **inside the
left and right sub-containers** and in the **Lateralization Notes**
below, not imported from elsewhere.
**Boundary status (INHIBITORY RELAY — NOT an excitatory relay):**
**Boundary case — the medial nucleus of the trapezoid body is an
INHIBITORY RELAY, NOT an excitatory relay.** The **MNTB** neurons are
**glycinergic** — they release **glycine** (an **inhibitory**
neurotransmitter) at their **axonal terminals** in the **ipsilateral
LSO**. This is the **opposite** of the **excitatory (glutamatergic)**
principal neurons of the **LSO** and the **MSO**. **This distinction is
functionally load-bearing** — the **MNTB** is the **neural substrate** of
**contralateral inhibition** in the **LSO**, and its **glycinergic**
output is **essential** for the **ILD computation** (the **LSO** neuron
compares the **excitatory** ipsilateral input with the **inhibitory**
contralateral input — **without the MNTB inhibition**, the LSO could
not perform the ILD comparison). Consumers must **not** conflate the
medial nucleus of the trapezoid body with an **excitatory relay** — it
is the **glycinergic inhibitory relay** of the superior olivary complex.
**Boundary status (NOT the lateral superior olive — that is a SIBLING,
and the MNTB PROJECTS TO the LSO):** **Boundary case — the medial
nucleus of the trapezoid body is NOT the lateral superior olive (LSO);
the LSO is a SIBLING under the superior olivary complex.** The **LSO**
(``.../superior_olivary_complex/lateral_superior_olive/``) is the **ILD
processor** that **receives** the **excitatory ipsilateral cochlear
nuclei** input and the **inhibitory MNTB** input. The **MNTB** (here) is
the **inhibitory relay** that **projects** the **inhibitory
(glycinergic)** input to the **ipsilateral LSO**. They are **DIFFERENT
STRUCTURES** — different functional roles (inhibitory relay vs. ILD
processor). **They are functionally coupled** — the MNTB **projects to**
the LSO, and the two are **both essential** for **ILD processing**.
Consumers must **not** conflate the medial nucleus of the trapezoid body
with the lateral superior olive.
**Boundary status (NOT the medial superior olive — that is a SIBLING,
and it is the ITD processor):** **Boundary case — the medial nucleus of
the trapezoid body is NOT the medial superior olive (MSO); the MSO is a
SIBLING under the superior olivary complex.** The **MSO**
(``.../superior_olivary_complex/medial_superior_olive/``) is the **ITD
processor** for **low-frequency horizontal sound localization** — it
**receives bilateral excitatory** input from the **left and right
cochlear nuclei** (via the **trapezoid body**) and **performs** the
**ITD computation** (coincidence detection). The **MNTB** (here) is the
**inhibitory relay** for **ILD processing** — it **receives** the
**contralateral cochlear nuclei** input and **projects** an
**inhibitory** input to the **ipsilateral LSO**. They are **DIFFERENT
STRUCTURES** — different functional roles (inhibitory relay vs. ITD
processor), different binaural cues (ILD vs. ITD). Consumers must **not**
conflate the medial nucleus of the trapezoid body with the medial
superior olive.
**Boundary status (NOT the cochlear nuclei — those are the UPSTREAM
SOURCE):** **Boundary case — the medial nucleus of the trapezoid body is
NOT the cochlear nuclei.** The **cochlear nuclei**
(``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``
and ``.../right/``) are the **monaural first-order relay** that
**receive** the **monaural** auditory input from the **ipsilateral
cochlea**. The **contralateral cochlear nuclei** — especially the
**globular bushy cells** in the **anterior ventral cochlear nucleus
(AVCN)** — **project** to the **MNTB** via the **trapezoid body** (the
**calyx of Held** synapse). The **MNTB** (here) is the **inhibitory
relay** that **receives** the **contralateral cochlear nuclei** input
and **projects** an **inhibitory** input to the **ipsilateral LSO**.
They are **DIFFERENT STRUCTURES** — the **cochlear nuclei** are the
**upstream monaural first-order relay**; the **MNTB** is the
**downstream inhibitory relay**. Consumers must **not** conflate the
medial nucleus of the trapezoid body with the cochlear nuclei.
**Boundary status (NOT the trapezoid body — that is the WHITE-MATTER
AFFERENT TRACT):** **Boundary case — the medial nucleus of the trapezoid
body is NOT the trapezoid body.** The **trapezoid body** is the
**white-matter decussating tract** that **carries** the **bilateral
auditory axons** from the **cochlear nuclei** to the **superior olivary
complex** — including the **contralateral cochlear nuclei** projections
to the **MNTB** (via the **calyx of Held**). The **MNTB** (here) is the
**grey-matter neuron cluster** that **receives** the trapezoid-body
axons. They are **DIFFERENT STRUCTURES** — the **MNTB** is grey matter;
the **trapezoid body** is white matter. **This distinction is
functionally load-bearing** — the **MNTB** is named after the
**trapezoid body** (it is the **medial nucleus** that sits **within** the
trapezoid body), but the **MNTB** is the **grey-matter neuron cluster**,
and the **trapezoid body** is the **white-matter fiber tract**. Consumers
must **not** conflate the medial nucleus of the trapezoid body with the
trapezoid body.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
EFFERENT TRACT of the SOC, not the MNTB's own efferent):** **Boundary
case — the medial nucleus of the trapezoid body is NOT the lateral
lemniscus.** The **lateral lemniscus** is the **white-matter ascending
tract** that **carries** the **efferent axons** from the **superior
olivary complex** (including the **LSO** and the **MSO**) to the
**inferior colliculus**. The **MNTB** (here) is the **inhibitory relay**
that **projects** its **inhibitory (glycinergic)** axons **intrinsically**
to the **ipsilateral LSO** — **not** to the **lateral lemniscus**. **The
MNTB's principal efferent target is the ipsilateral LSO, not the lateral
lemniscus.** Consumers must **not** conflate the medial nucleus of the
trapezoid body with the lateral lemniscus, and must **not** assume that
the MNTB's efferent axons travel in the lateral lemniscus (they **do
not** — the MNTB is an **intrinsic superior olivary complex** relay).
**Boundary status (NOT the inferior colliculus — that is the MIDBRAIN
DOWNSTREAM AUDITORY RELAY):** **Boundary case — the medial nucleus of
the trapezoid body is NOT the inferior colliculus.** The **inferior
colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
and ``.../right/``) is the **midbrain auditory relay** that **receives**
the **ascending auditory projections** from the **superior olivary
complex** (via the **lateral lemniscus**) and **projects** to the
**medial geniculate body**. The **MNTB** (here) is the **pontine
inhibitory relay** — it is **upstream** of the inferior colliculus (and
its **output** does **not** reach the inferior colliculus directly — the
MNTB projects to the LSO, which then projects to the inferior
colliculus). They are **DIFFERENT STRUCTURES** — the **MNTB** is
**pontine** and **upstream**; the **inferior colliculus** is **midbrain**
and **downstream**. Consumers must **not** conflate the medial nucleus of
the trapezoid body with the inferior colliculus.
**Boundary status (NOT the medial geniculate body — that is the THALAMIC
DOWNSTREAM AUDITORY RELAY):** **Boundary case — the medial nucleus of
the trapezoid body is NOT the medial geniculate body.** The **medial
geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
and ``.../right/``) is the **thalamic auditory relay** that **receives**
the **ascending auditory projections** from the **inferior colliculus**
and **projects** to the **primary auditory cortex**. The **MNTB** (here)
is the **pontine inhibitory relay** — it is **upstream** of the medial
geniculate body. They are **DIFFERENT STRUCTURES** — the **MNTB** is
**pontine** and **upstream**; the **medial geniculate body** is
**diencephalic** and **downstream**. Consumers must **not** conflate the
medial nucleus of the trapezoid body with the medial geniculate body.
**Boundary status (NOT the primary auditory cortex — that is the CORTICAL
DOWNSTREAM AUDITORY TARGET):** **Boundary case — the medial nucleus of
the trapezoid body is NOT the primary auditory cortex.** The **primary
auditory cortex** (Heschl's gyrus, Brodmann areas 41 and 42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
and ``.../right/``) is the **cortical target** of the **ascending
auditory pathway**. The **MNTB** (here) is the **pontine inhibitory
relay** — it is **upstream** of the primary auditory cortex. They are
**DIFFERENT STRUCTURES** — the **MNTB** is **pontine** and **upstream**;
the **primary auditory cortex** is **cortical** and **downstream**.
Consumers must **not** conflate the medial nucleus of the trapezoid body
with the primary auditory cortex.
**Boundary status (NOT the facial nerve nucleus — that is an
ANATOMICALLY ADJACENT SIBLING):** **Boundary case — the medial nucleus
of the trapezoid body is NOT the facial nerve nucleus.** The **facial
nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
``.../right/``) is the **branchial motor** nucleus for the **muscles of
facial expression**. The **MNTB** (here) is the **glycinergic inhibitory
relay** for **ILD processing**. They are **DIFFERENT STRUCTURES** —
different functional systems (branchial motor vs. binaural inhibitory
relay). They are **anatomically adjacent** (both are in the **ventral
pontine tegmentum**) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the medial nucleus of the
trapezoid body with the facial nerve nucleus.
**Boundary status (NOT the abducens nucleus — that is an ANATOMICALLY
ADJACENT SIBLING):** **Boundary case — the medial nucleus of the
trapezoid body is NOT the abducens nucleus.** The **abducens nucleus**
(``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and ``.../right/``)
is the **somatic motor** nucleus for the **lateral rectus**. The **MNTB**
(here) is the **glycinergic inhibitory relay** for **ILD processing**.
They are **DIFFERENT STRUCTURES** — different functional systems
(somatic motor vs. binaural inhibitory relay). They are **anatomically
adjacent** — the **MNTB** is **near the genu of the facial nerve** and
the **abducens nucleus**; this proximity is a **classic source of
confusion** — consumers must **not** conflate the medial nucleus of the
trapezoid body with the abducens nucleus.
**Boundary status (NOT the cochlear or vestibulocochlear nerve — those
are the PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE):** **Boundary
case — the medial nucleus of the trapezoid body is NOT the cochlear nerve
or the vestibulocochlear nerve.** The **cochlear nerve** (the cochlear
division of CN VIII) and the **vestibulocochlear nerve** (CN VIII) are
the **white-matter peripheral nerves** that **carry** the **primary
auditory axons** from the **spiral ganglion** to the **cochlear nuclei**.
The **MNTB** (here) is the **central grey-matter inhibitory relay**.
They are **DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **MNTB** is **central grey matter**. Consumers must
**not** conflate the medial nucleus of the trapezoid body with the
cochlear or vestibulocochlear nerve.
**Boundary status (NOT the pons or the pontine tegmentum — those are the
GRANDPARENT and its tegmentum):** **Boundary case — the medial nucleus
of the trapezoid body is NOT the pons or the pontine tegmentum.** The
**pons** (``.../pons/``) is the **whole metencephalic brainstem
segment**; the **pontine tegmentum** is the **dorsal pontine grey-matter
region**. The **MNTB** (here) is a **specific bilateral glycinergic
nucleus** in the **ventral pontine tegmentum**. Consumers must **not**
conflate the medial nucleus of the trapezoid body with the **whole
pons** or with the **whole pontine tegmentum**.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
functionally distinct populations):** **Boundary case — the medial
nucleus of the trapezoid body is NOT a single uniform neuron population;
it contains MULTIPLE functionally distinct populations.** The
**principal neurons** — the **large glycinergic projection neurons**
that **receive** the **contralateral cochlear nuclei** input via the
**calyx of Held** (the **largest synapse in the mammalian brain**) and
**project** the **inhibitory (glycinergic)** input to the **ipsilateral
LSO**. The **local circuit interneurons** — the **smaller neurons** that
**modulate** the **principal neurons**. **These populations are prose,
not structural children.** Consumers must **not** treat the medial
nucleus of the trapezoid body as a single uniform population — it is a
**functionally heterogeneous nucleus** with **distinct** sub-circuits.
**Boundary status (SLEA-FREE — the medial nucleus of the trapezoid body
is NOT an extended-amygdala component):** **Boundary case — the medial
nucleus of the trapezoid body is SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **MNTB** is a **binaural inhibitory
relay** — it is **NOT** an extended-amygdala component, and it carries
**NO SLEA warning**. Consumers must **not** import the SLEA warning into
the medial nucleus of the trapezoid body — it is **SLEA-free**.

Overview
--------
The medial nucleus of the trapezoid body is the **glycinergic inhibitory
relay** of the **superior olivary complex** — the **bilateral
collection** of **glycinergic neurons** that **receives** the
**contralateral cochlear nuclei** input (via the **calyx of Held** in the
**trapezoid body**) and **projects** an **inhibitory (glycinergic)**
input to the **ipsilateral lateral superior olive (LSO)** — the
**neural substrate** of **contralateral inhibition** essential for
**interaural level difference (ILD) processing**. It is a **container**
under the superior olivary complex container, with **two structural
children** (``left`` and ``right``) — the **bilateral halves** of the
MNTB — each of which is a **leaf** at the tree level with **prose
neuron populations**.

**The medial nucleus of the trapezoid body is a CONTAINER, NOT a leaf.**
Its structural children are ``left`` and ``right`` — the **bilateral
sub-containers**.

**The medial nucleus of the trapezoid body is a BILATERAL CONTAINER.**
The ``left`` and ``right`` sub-containers are **structurally
symmetric** — same neuron populations, same functional system
(inhibitory relay for ILD processing), same bilateral framing. The
bilateral symmetry is **strict**.

**The medial nucleus of the trapezoid body is an INHIBITORY RELAY.**
The **MNTB** neurons are **glycinergic** — they release **glycine** (an
**inhibitory** neurotransmitter) at their **axonal terminals** in the
**ipsilateral LSO**. This is the **neural substrate** of
**contralateral inhibition** in the **LSO** — the **essential
ingredient** for **ILD processing**. **Without the MNTB inhibition**, the
LSO could not compare the **ipsilateral** and **contralateral** sound
levels.

**The medial nucleus of the trapezoid body is NOT the LSO, the MSO, the
cochlear nuclei, the trapezoid body, the lateral lemniscus, the
inferior colliculus, the medial geniculate body, or the primary auditory
cortex.** Those are **different auditory structures** — the **LSO** (ILD
processor), the **MSO** (ITD processor), the **cochlear nuclei**
(upstream monaural first-order relay), the **trapezoid body**
(afferent white-matter tract), the **lateral lemniscus** (efferent
white-matter tract), and the **downstream** midbrain/thalamic/cortical
auditory relays. The **MNTB** is the **glycinergic inhibitory relay** —
the **intrinsic superior olivary complex node** that makes **ILD
processing possible**.

**The medial nucleus of the trapezoid body is a TWO-POPULATION complex.**
The **principal neurons** (large glycinergic projection neurons
receiving the **calyx of Held** and projecting to the **ipsilateral
LSO**) and the **local circuit interneurons** are **prose**, not
structural children.

**The medial nucleus of the trapezoid body is SLEA-FREE.** It is **not**
an extended-amygdala component, and it carries **no SLEA warning**.

Sub-Container and Neuron Population Composition (structural children
and prose, not structural grandchildren)
----------------------------------------
The medial nucleus of the trapezoid body contains **two structural
children** — the ``left`` and ``right`` sub-containers — each of which
is a **leaf** at the tree level with **prose neuron populations**:

*   **Left medial nucleus of the trapezoid body**
    (``.../medial_nucleus_of_trapezoid_body/left/``) — the **left
    glycinergic inhibitory relay**. It **receives** the **right
    cochlear nuclei** input (specifically the **right globular bushy
    cells** in the **right AVCN**, via the **right trapezoid body** and
    the **calyx of Held** synapse) and **projects** the **inhibitory
    (glycinergic)** input to the **left LSO**. The **left MNTB** is the
    **neural substrate** of **contralateral inhibition** in the **left
    LSO** — the **inhibitory input** that **enables** the **left LSO**
    to **compare** the **left-ear sound level** (excitatory) with the
    **right-ear sound level** (inhibitory).

*   **Right medial nucleus of the trapezoid body**
    (``.../medial_nucleus_of_trapezoid_body/right/``) — the **right
    glycinergic inhibitory relay**. It **receives** the **left cochlear
    nuclei** input (specifically the **left globular bushy cells** in
    the **left AVCN**, via the **left trapezoid body** and the **calyx
    of Held** synapse) and **projects** the **inhibitory (glycinergic)**
    input to the **right LSO**. The **right MNTB** is the **neural
    substrate** of **contralateral inhibition** in the **right LSO** —
    the **inhibitory input** that **enables** the **right LSO** to
    **compare** the **right-ear sound level** (excitatory) with the
    **left-ear sound level** (inhibitory).

**Each of the left and right sub-containers contains two prose neuron
populations** — the **principal neurons** (large glycinergic projection
neurons receiving the calyx of Held and projecting to the ipsilateral
LSO) and the **local circuit interneurons**. **These populations are
prose, not structural children** — the ``left`` and ``right``
sub-containers are **leaves** at the tree level.

The MNTB / LSO Boundary
-----------------------
This is the **sibling** boundary — **inhibitory relay vs. ILD
processor**:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **glycinergic inhibitory relay** that **projects to** the ipsilateral
    LSO.

*   **Lateral superior olive (LSO)**
    (``.../superior_olivary_complex/lateral_superior_olive/``) — the
    **ILD processor** that **receives** the **excitatory ipsilateral
    cochlear nuclei** input and the **inhibitory MNTB** input.

**They are DIFFERENT STRUCTURES** — different functional roles
(inhibitory relay vs. ILD processor). **They are functionally coupled**
— the MNTB **projects to** the LSO, and the two are **both essential**
for **ILD processing**. Consumers must **not** conflate the medial
nucleus of the trapezoid body with the lateral superior olive.

The MNTB / MSO Boundary
-----------------------
This is the **sibling** boundary — **inhibitory relay vs. ITD
processor**:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **glycinergic inhibitory relay** for **ILD processing**.

*   **Medial superior olive (MSO)**
    (``.../superior_olivary_complex/medial_superior_olive/``) — the
    **ITD processor** for **low-frequency horizontal sound
    localization** — it **receives bilateral excitatory** input from the
    **left and right cochlear nuclei** and **performs** the **ITD
    computation** (coincidence detection).

**They are DIFFERENT STRUCTURES** — different functional roles
(inhibitory relay for ILD processing vs. ITD processor), different
binaural cues (ILD vs. ITD). Consumers must **not** conflate the medial
nucleus of the trapezoid body with the medial superior olive.

The MNTB / Cochlear Nuclei Boundary
-----------------------------------
This is the **inhibitory relay vs. upstream monaural first-order relay**
boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **glycinergic inhibitory relay** that **receives** the
    **contralateral cochlear nuclei** input.

*   **Cochlear nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/``
    and ``.../right/``) — the **monaural first-order relay** that
    **receive** the **monaural** auditory input from the **ipsilateral
    cochlea** — the **contralateral cochlear nuclei** (specifically the
    **globular bushy cells** in the **AVCN**) **project** to the
    **MNTB** via the **trapezoid body** (the **calyx of Held**).

**They are DIFFERENT STRUCTURES** — the **cochlear nuclei** are the
**upstream monaural first-order relay**; the **MNTB** is the
**downstream inhibitory relay**. Consumers must **not** conflate the
medial nucleus of the trapezoid body with the cochlear nuclei.

The MNTB / Trapezoid Body Boundary
----------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tract the
MNTB is NAMED AFTER**:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **grey-matter glycinergic neuron cluster** that **receives** the
    trapezoid-body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the **bilateral auditory axons** from the **cochlear
    nuclei** to the **superior olivary complex** (including the
    **contralateral cochlear nuclei** projections to the **MNTB**).

**They are DIFFERENT STRUCTURES.** The **MNTB** is grey matter; the
**trapezoid body** is white matter. **The MNTB is named after the
trapezoid body** — it is the **medial nucleus** that sits **within** the
trapezoid body — but the **MNTB** is the **grey-matter neuron cluster**,
and the **trapezoid body** is the **white-matter fiber tract**.
Consumers must **not** conflate the medial nucleus of the trapezoid body
with the trapezoid body.

The MNTB / Lateral Lemniscus Boundary
-------------------------------------
This is the **intrinsic SOC relay vs. extrinsic ascending tract**
boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **glycinergic inhibitory relay** that **projects** its **inhibitory
    (glycinergic)** axons **intrinsically** to the **ipsilateral LSO**
    — **not** to the lateral lemniscus.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the **efferent axons** from the **superior olivary
    complex** (including the **LSO** and the **MSO**) to the **inferior
    colliculus**.

**The MNTB's principal efferent target is the ipsilateral LSO, not the
lateral lemniscus.** The MNTB is an **intrinsic superior olivary
complex** relay — its **output does not reach the inferior colliculus
directly** (it reaches the inferior colliculus **indirectly**, via the
LSO). Consumers must **not** conflate the medial nucleus of the trapezoid
body with the lateral lemniscus, and must **not** assume that the MNTB's
efferent axons travel in the lateral lemniscus.

The MNTB / Inferior Colliculus Boundary
---------------------------------------
This is the **pontine inhibitory relay vs. midbrain downstream relay**
boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **pontine glycinergic inhibitory relay**.

*   **Inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
    and ``.../right/``) — the **midbrain auditory relay** that
    **receives** the **ascending auditory projections** from the
    **superior olivary complex** (including the **LSO** and **MSO**,
    via the **lateral lemniscus**) and **projects** to the **medial
    geniculate body**.

**They are DIFFERENT STRUCTURES** — the **MNTB** is **pontine** and
**upstream**; the **inferior colliculus** is **midbrain** and
**downstream**. The **MNTB does not project directly to the inferior
colliculus** — its **output reaches the inferior colliculus indirectly**,
via the **LSO**. Consumers must **not** conflate the medial nucleus of
the trapezoid body with the inferior colliculus.

The MNTB / Medial Geniculate Body Boundary
------------------------------------------
This is the **pontine inhibitory relay vs. thalamic downstream relay**
boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **pontine glycinergic inhibitory relay**.

*   **Medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
    and ``.../right/``) — the **thalamic auditory relay** that
    **receives** the **ascending auditory projections** from the
    **inferior colliculus** and **projects** to the **primary auditory
    cortex**.

**They are DIFFERENT STRUCTURES** — the **MNTB** is **pontine** and
**upstream**; the **medial geniculate body** is **diencephalic** and
**downstream**. Consumers must **not** conflate the medial nucleus of the
trapezoid body with the medial geniculate body.

The MNTB / Primary Auditory Cortex Boundary
-------------------------------------------
This is the **pontine inhibitory relay vs. cortical downstream target**
boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **pontine glycinergic inhibitory relay**.

*   **Primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
    42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
    and ``.../right/``) — the **cortical target** of the **ascending
    auditory pathway**.

**They are DIFFERENT STRUCTURES** — the **MNTB** is **pontine** and
**upstream**; the **primary auditory cortex** is **cortical** and
**downstream**. Consumers must **not** conflate the medial nucleus of the
trapezoid body with the primary auditory cortex.

The MNTB / Facial Nerve Nucleus Boundary
----------------------------------------
This is the **auditory inhibitory relay vs. branchial motor** boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **glycinergic inhibitory relay** for **ILD processing**.

*   **Facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
    ``.../right/``) — the **branchial motor** nucleus for the **muscles
    of facial expression**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory inhibitory relay vs. branchial motor). They are **anatomically
adjacent** (both are in the **ventral pontine tegmentum**) — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the medial nucleus of the trapezoid body with the facial nerve
nucleus.

The MNTB / Abducens Nucleus Boundary
------------------------------------
This is the **auditory inhibitory relay vs. somatic motor** boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **glycinergic inhibitory relay** for **ILD processing**.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and
    ``.../right/``) — the **somatic motor** nucleus for the **lateral
    rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory inhibitory relay vs. somatic motor). They are **anatomically
adjacent** — the **MNTB** is **near the genu of the facial nerve** and
the **abducens nucleus**; this proximity is a **classic source of
confusion** — consumers must **not** conflate the medial nucleus of the
trapezoid body with the abducens nucleus.

The MNTB / Cochlear and Vestibulocochlear Nerves Boundary
---------------------------------------------------------
This is the **central grey matter vs. peripheral white matter** boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **central grey-matter glycinergic inhibitory relay**.

*   **Cochlear nerve** (the cochlear division of CN VIII) and
    **vestibulocochlear nerve** (CN VIII) — the **peripheral white-matter
    nerves** that **carry** the **primary auditory axons** from the
    **spiral ganglion** to the **cochlear nuclei**.

**They are DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **MNTB** is **central grey matter**. Consumers must
**not** conflate the medial nucleus of the trapezoid body with the
cochlear or vestibulocochlear nerve.

The MNTB / Superior Olivary Complex Container Boundary
-----------------------------------------------------
This is the **sub-container vs. parent** boundary:

*   **Medial nucleus of the trapezoid body** (this module) — the
    **glycinergic inhibitory relay** — one of the **three sub-nuclei**
    of the superior olivary complex.

*   **Superior olivary complex container**
    (``.../superior_olivary_complex/``) — the **pontine binaural
    sound-localization relay** that **contains** the **LSO**, the
    **MSO**, and the **MNTB**.

**The medial nucleus of the trapezoid body is a child of the superior
olivary complex.** Consumers must **not** conflate the medial nucleus of
the trapezoid body with the **whole superior olivary complex**.

The MNTB / SLEA Boundary
------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Medial nucleus of the trapezoid body** (this module) — **SLEA-FREE**.
    It is **not** an extended-amygdala component, and it carries **no
    SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The medial nucleus of the trapezoid body is NOT part of the SLEA
continuum.** It is a **binaural inhibitory relay**, and it carries **no
SLEA warning**. Consumers must **not** import the SLEA warning into the
medial nucleus of the trapezoid body.

Function in the Human Brain
---------------------------
The medial nucleus of the trapezoid body's functions are **inhibitory
relay for interaural level difference (ILD) processing** — **NOT a single
unified function**:

*   **Contralateral Inhibition (Glycinergic Inhibitory Relay):** The
    **MNTB** is the **glycinergic inhibitory relay** that **converts**
    the **excitatory contralateral cochlear nuclei** input into an
    **inhibitory input** to the **ipsilateral LSO**. This
    **contralateral inhibition** is the **essential neural substrate**
    of **ILD processing** — the **LSO neuron** can **compare** the
    **ipsilateral sound level** (excitatory, direct from the ipsilateral
    cochlear nuclei) with the **contralateral sound level** (inhibitory,
    via the ipsilateral MNTB, which itself receives the **contralateral
    cochlear nuclei** input). **Without the MNTB inhibition**, the LSO
    would **only** receive **excitatory** input from the **ipsilateral
    cochlear nuclei** — it could **not** compare the **ipsilateral** and
    **contralateral** sound levels, and **ILD processing would be
    impossible**.

*   **Calyx of Held Synapse (Largest Synapse in the Mammalian Brain):**
    The **MNTB** principal neurons **receive** the **contralateral
    cochlear nuclei** globular bushy cell input via the **calyx of
    Held** — the **largest synapse in the mammalian brain**. The **calyx
    of Held** is a **giant presynaptic terminal** that **envelops** the
    **MNTB principal neuron soma** — it **ensures** the **fastest and
    most reliable synaptic transmission** in the mammalian brain, which
    is **essential** for the **precise timing** required for **binaural
    sound localization** (specifically, for the **MNTB's inhibitory
    output** to the **LSO** to be **precisely timed** with the
    **excitatory** input from the **ipsilateral cochlear nuclei**).

*   **ILD Processing Support (MNTB → LSO → ILD Computation):** The
    **MNTB** **projects** its **inhibitory (glycinergic)** output to the
    **ipsilateral LSO**, **enabling** the **LSO** to **perform** the
    **ILD computation** (the **LSO neuron fires maximally** when the
    **ipsilateral sound level** is **higher** than the **contralateral
    sound level** — because the **excitatory** ipsilateral drive
    **exceeds** the **inhibitory** contralateral drive via the MNTB).
    The **MNTB** is thus an **essential node** in the **ILD-processing
    circuit** — **without the MNTB**, the **LSO** could not **compute**
    the **ILD**, and **high-frequency horizontal sound localization**
    would be **impaired**.

*   **NOT a neural processor in the classical sense.** The **MNTB** is an
    **inhibitory relay** — it **receives** the **excitatory
    contralateral cochlear nuclei** input and **converts** it into an
    **inhibitory input** to the **ipsilateral LSO**. The **processing**
    of **binaural sound localization** is **distributed** across the
    **cochlear nuclei** (monaural auditory processing), the **MNTB**
    (contralateral inhibitory relay), the **LSO** (ILD processing), the
    **MSO** (ITD processing), the **inferior colliculus** (integration
    of binaural and spectral cues), the **medial geniculate body**
    (thalamic relay), and the **primary auditory cortex** (cortical
    processing). The **MNTB** is the **inhibitory relay** — the
    **brainstem node** that **converts** the **contralateral excitatory
    input** into the **inhibitory input** that makes **ILD processing
    possible**.

**The unifying theme:** the medial nucleus of the trapezoid body is the
**glycinergic inhibitory relay** of the superior olivary complex — the
**bilateral collection** of **glycinergic neurons** that **receives** the
**contralateral cochlear nuclei** input (via the **calyx of Held** in the
**trapezoid body**) and **projects** an **inhibitory (glycinergic)**
input to the **ipsilateral LSO** — the **neural substrate** of
**contralateral inhibition** essential for **ILD processing**. It is a
**bilateral container** (left and right sub-containers), **two-population**
(principal neurons receiving the calyx of Held; local circuit
interneurons), **SLEA-free**, and **NOT the trapezoid body** — the
**trapezoid body** is the **white-matter afferent tract** that the MNTB
**receives from** (and is **named after**).

Associated Disorders
--------------------
The medial nucleus of the trapezoid body has **no named "medial nucleus
of the trapezoid body syndrome"** — its clinical associations are
**binaural-specific**:

*   **MNTB Lesion — Impaired ILD-Based Sound Localization with Preserved
    Pure-Tone Thresholds:** A lesion of the **medial nucleus of the
    trapezoid body** (e.g. **pontine stroke**, **tumor**,
    **demyelination**) causes **impaired ILD-based sound localization**
    (impaired **high-frequency horizontal sound localization**) with
    **preserved pure-tone thresholds** (because the **monaural auditory
    pathway** — the **cochlear nuclei** and the **ascending auditory
    pathway** — is intact). **The ILD-specific pattern** is the
    **substrate** of the **MNTB** function — this is the **"ILD-specific
    binaural deficit"** that **distinguishes** an **MNTB lesion** from a
    **cochlear nuclei lesion** (which causes **sensorineural hearing
    loss**) or an **MSO lesion** (which causes **ITD-specific binaural
    deficit**).

*   **Binaural Hearing Deficit — MNTB Involvement:** **Binaural hearing**
    is the **ability to use** the **differences** between the **two
    ears** to **localize sound** and to **understand speech in noise**
    (the **binaural squelch effect** and the **binaural summation
    effect**). **The MNTB** is **one of the neural substrates** of
    **binaural hearing** (specifically **ILD-based binaural processing**
    — via its inhibitory relay to the LSO), and its dysfunction may
    **contribute** to **binaural hearing deficits** — **impaired sound
    localization**, **impaired speech understanding in noise**, and
    **impaired binaural unmasking**.

*   **Presbycusis — MNTB Involvement:** **Presbycusis** (age-related
    hearing loss) is characterized by **peripheral auditory dysfunction**
    (cochlear hair cell loss) **and central auditory dysfunction**
    (including **MNTB** dysfunction — **reduced neuron number**,
    **reduced synaptic density**, and **reduced glycinergic
    transmission**). The **MNTB** may show **age-related changes** —
    contributing to **impaired ILD processing** and **impaired
    high-frequency horizontal sound localization** in **older adults**.

*   **Multiple Sclerosis — MNTB Involvement:** **Multiple sclerosis** can
    affect the **MNTB** (as a **brainstem demyelinating lesion**),
    contributing to **impaired ILD-based sound localization** and
    **binaural hearing deficits**.

*   **Pontine Stroke — MNTB Involvement:** A **pontine stroke** (e.g.
    **basilar artery** perforator territory) involving the **MNTB** causes
    **impaired ILD-based sound localization** — often accompanied by
    **other pontine signs** (**hemiparesis**, **facial palsy**,
    **abducens palsy**, **cerebellar ataxia**).

*   **No Named "MNTB Syndrome":** The medial nucleus of the trapezoid
    body is a **bilateral container** of **two functionally distinct
    neuron populations** — it has **no named clinical syndrome** of its
    own. Its clinical relevance is **ILD-specific** — **impaired
    ILD-based sound localization**, **impaired high-frequency horizontal
    sound localization**, and **impaired binaural hearing**.

**What is NOT here:** The medial nucleus of the trapezoid body is **not**
the substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **fear conditioning** (amygdala — central
nucleus + basolateral nuclei), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **Alzheimer's disease** (hippocampus, nucleus
basalis), **Parkinson's disease** (substantia nigra), **acoustic
neuroma** (CN VIII nerve), **vestibular neuritis** (vestibular nerve),
**labyrinthitis** (inner ear), or **auditory neuropathy spectrum
disorder** (cochlear nerve or hair cell). Its clinical relevance is
**ILD-specific**, via the **inhibitory relay for interaural level
difference (ILD) processing** it subserves. **No named MNTB syndrome
exists.**

Lateralization Notes
--------------------
This is the **bilateral** medial nucleus of the trapezoid body container.
The MNTB is **bilaterally symmetric** with the **left** and **right**
sub-containers **strictly mirrored** — and it carries **NO warning at
the container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right**
    sub-containers are **structurally identical** — same neuron
    populations (principal neurons receiving the calyx of Held; local
    circuit interneurons), same functional system (inhibitory relay for
    ILD processing), same bilateral framing. The bilateral symmetry is
    **strict**.

*   **Contralateral Input and Ipsilateral Output (Structural Fact, NOT a
    Lateralization Warning):** The **left MNTB** receives **contralateral
    (right) cochlear nuclei** input (via the **right trapezoid body** and
    the **calyx of Held**) and **projects** its **inhibitory output** to
    the **ipsilateral (left) LSO**. The **right MNTB** receives
    **contralateral (left) cochlear nuclei** input and **projects** its
    **inhibitory output** to the **ipsilateral (right) LSO**. **This
    contralateral-input / ipsilateral-output** arrangement is a
    **structural fact** of the **MNTB** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **MNTB's role
    as the inhibitory relay** for the **LSO's ILD computation**.

*   **Crossed Inhibitory Pathway (Structural Fact, NOT a Lateralization
    Warning):** The **MNTB** is the **neural substrate** of the
    **crossed inhibitory pathway** in the **LSO** — the **left MNTB**
    **inhibits** the **left LSO** (via the **right cochlear nuclei**
    input), and the **right MNTB** **inhibits** the **right LSO** (via
    the **left cochlear nuclei** input). **This crossed inhibitory
    pathway** is a **structural fact** of the **ILD-processing
    system** — it is **not** a functional lateralization. It is the
    **neural substrate** of the **contralateral inhibition** that
    **enables** the **LSO** to **compare** the **ipsilateral** and
    **contralateral** sound levels.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The MNTB is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the MNTB.

*   **NO Amygdala-Lateralization Warning of their own (the MNTB is
    BINAURAL AUDITORY, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The MNTB is a **binaural auditory inhibitory
    relay** — consumers must **not** conflate it with the **amygdala**
    or with the **fear circuit**.

**A consumer that assumes "left MNTB = right MNTB" will be structurally
correct** — the two sides are **strictly symmetric** (the
contralateral-input / ipsilateral-output arrangement and the crossed
inhibitory pathway are structural facts, not lateralizations). The MNTB
is a **strict-mirror pair with NO warning at the container level** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The container is **bilateral**, but
    it does **not** import ``left`` or ``right`` at module level — it
    exposes them as **structural children** and lets consumers resolve
    them through the memory/recall layer.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../superior_olivary_complex/lateral_superior_olive/``,
    ``.../superior_olivary_complex/medial_superior_olive/``,
    ``.../superior_olivary_complex/``, ``.../pons/tegmentum/``,
    ``.../pons/cranial_nerve_nuclei/``, ``.../midbrain/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    MNTB's relationships to the **LSO**, the **MSO**, the **cochlear
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
    populations** (principal neurons receiving the calyx of Held; local
    circuit interneurons). Consumers must not conflate the container
    with its children.
*   **BILATERAL CONTAINER — left and right are STRUCTURALLY SYMMETRIC.**
    The **left** and **right** sub-containers are a **strict-mirror
    pair** with **no warning at the container level**. Any
    lateralization is documented **inside the left and right
    sub-containers** and in the **Lateralization Notes**.
*   **INHIBITORY RELAY — NOT an excitatory relay.** The **MNTB** neurons
    are **glycinergic** — they release **glycine** (an **inhibitory**
    neurotransmitter). This is the **opposite** of the **excitatory
    (glutamatergic)** principal neurons of the **LSO** and the **MSO**.
    Consumers must **not** conflate the MNTB with an **excitatory
    relay**.
*   **NOT the LSO — the MNTB PROJECTS TO the LSO.** The **LSO** is the
    **ILD processor**; the **MNTB** is the **inhibitory relay** that
    **projects to** the LSO. Consumers must **not** conflate the MNTB
    with the LSO.
*   **NOT the MSO — that is the ITD processor.** Consumers must **not**
    conflate the MNTB with the MSO.
*   **NOT the cochlear nuclei — those are the UPSTREAM monaural
    first-order relay.** Consumers must **not** conflate the MNTB with
    the cochlear nuclei.
*   **NOT the trapezoid body — that is the WHITE-MATTER AFFERENT TRACT
    the MNTB is NAMED AFTER.** The **MNTB** is grey matter; the
    **trapezoid body** is white matter. Consumers must **not** conflate
    the two.
*   **NOT the lateral lemniscus — that is the WHITE-MATTER EFFERENT TRACT
    of the SOC, not the MNTB's own efferent.** The **MNTB's principal
    efferent target is the ipsilateral LSO** — the MNTB is an
    **intrinsic** superior olivary complex relay. Consumers must **not**
    conflate the MNTB with the lateral lemniscus.
*   **NOT the inferior colliculus, the medial geniculate body, or the
    primary auditory cortex — those are DOWNSTREAM AUDITORY
    STRUCTURES.** Consumers must **not** conflate the MNTB with any of
    them.
*   **NOT the facial nerve nucleus or the abducens nucleus — those are
    ANATOMICALLY ADJACENT SIBLINGS.** Consumers must **not** conflate
    the MNTB with either of them.
*   **NOT the cochlear or vestibulocochlear nerve — those are the
    PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE.** Consumers must
    **not** conflate the MNTB with either nerve.
*   **NOT the whole superior olivary complex — that is the PARENT.**
    Consumers must **not** conflate the MNTB with the whole superior
    olivary complex.
*   **MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — NOT a single uniform
    nucleus.** The **principal neurons** (glycinergic, receiving the
    **calyx of Held**) and the **local circuit interneurons** are
    **prose**, not structural children. Consumers must **not** treat the
    MNTB as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The MNTB is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the MNTB is BINAURAL AUDITORY.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **MNTB** is a **binaural auditory inhibitory relay** —
    it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The MNTB is a local container under the
    superior_olivary_complex container, not a cross-listed container.
*   **No nested cross-listing.** The MNTB has no nested dual-framing
    module. It is a single bilateral container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex import medial_nucleus_of_trapezoid_body

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex."
        "medial_nucleus_of_trapezoid_body"
    )

**Do not** assume the MNTB is a **leaf**. It is a **container** — its
structural children are ``left`` and ``right``, each of which is a
**leaf** at the tree level with **prose neuron populations**.

**Do not** assume the MNTB is an **excitatory relay**. The **MNTB**
neurons are **glycinergic** — they release **glycine** (an **inhibitory**
neurotransmitter).

**Do not** assume the MNTB is the **LSO**, the **MSO**, the **cochlear
nuclei**, the **trapezoid body**, the **lateral lemniscus**, the
**inferior colliculus**, the **medial geniculate body**, or the
**primary auditory cortex**. Those are **different auditory
structures** — the **LSO** (ILD processor), the **MSO** (ITD processor),
the **cochlear nuclei** (upstream monaural first-order relay), the
**trapezoid body** (afferent white-matter tract), the **lateral
lemniscus** (efferent white-matter tract), and the **downstream**
midbrain/thalamic/cortical auditory relays.

**Do not** assume the MNTB's **efferent axons** travel in the **lateral
lemniscus**. The **MNTB's principal efferent target is the ipsilateral
LSO** — the **MNTB is an intrinsic superior olivary complex relay**, and
its **output reaches the inferior colliculus indirectly, via the LSO**.

**Do not** assume the MNTB is the **facial nerve nucleus** or the
**abducens nucleus**. Those are **anatomically adjacent siblings** —
different functional systems.

**Do not** assume the MNTB is the **cochlear nerve** or the
**vestibulocochlear nerve**. Those are the **peripheral auditory
conduction infrastructure** — the MNTB is **central grey matter**.

**Do not** assume the MNTB is the **whole superior olivary complex**.
The **superior olivary complex** is the **parent** — the **MNTB** is one
of its **three sub-nuclei**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the MNTB. **The MNTB is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the MNTB's structural children (recommended consumer pattern)::

    MEDIAL_NUCLEUS_OF_TRAPEZOID_BODY_CHILDREN = ("left", "right")
    # The container is bilateral. The left and right sub-containers are
    # LEAVES at the tree level, with prose neuron populations (principal
    # neurons receiving the calyx of Held; local circuit interneurons).

Iterating the MNTB's left and right sub-containers (recommended consumer
pattern)::

    for side in ("left", "right"):
        mntb_side_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"medial_nucleus_of_trapezoid_body.{side}"
        )
        # resolve mntb_side_path through the memory/recall layer

Reaching the LSO (recommended consumer pattern — the SIBLING the MNTB
PROJECTS TO)::

    # The LSO is the ILD PROCESSOR sibling under the
    # superior_olivary_complex container:
    #
    #   .../superior_olivary_complex/lateral_superior_olive/
    #
    # The MNTB PROJECTS its inhibitory (glycinergic) output to the
    # ipsilateral LSO — the two are FUNCTIONALLY COUPLED and are BOTH
    # ESSENTIAL for ILD processing.

Reaching the MSO (recommended consumer pattern — the ITD processor
sibling)::

    # The MSO is the ITD PROCESSOR sibling under the
    # superior_olivary_complex container:
    #
    #   .../superior_olivary_complex/medial_superior_olive/
    #
    # The MNTB is the inhibitory relay for ILD processing; the MSO is the
    # ITD processor. They are DIFFERENT STRUCTURES with DIFFERENT
    # binaural cues.

Reaching the cochlear nuclei (recommended consumer pattern — the
UPSTREAM SOURCE)::

    # The cochlear nuclei are the UPSTREAM MONAURAL FIRST-ORDER relay —
    # the CONTRALATERAL cochlear nuclei (specifically the globular bushy
    # cells in the AVCN) PROJECT TO the MNTB via the trapezoid body (the
    # calyx of Held):
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/  (and right/)
    #
    # The cochlear nuclei are UPSTREAM; the MNTB is DOWNSTREAM (the
    # glycinergic inhibitory relay).

Reaching the trapezoid body (recommended consumer pattern — the
white-matter afferent tract the MNTB is NAMED AFTER)::

    # The trapezoid body is the WHITE-MATTER afferent tract that carries
    # the contralateral cochlear nuclei axons to the MNTB:
    #
    #   .../white_matter/.../trapezoid_body/  (or equivalent path)
    #
    # The MNTB is NAMED AFTER the trapezoid body (it is the "medial
    # nucleus of the trapezoid body") — but the MNTB is the grey-matter
    # neuron cluster, and the trapezoid body is the white-matter fiber
    # tract.

Reaching the LSO via its left and right sub-containers (recommended
consumer pattern — the detailed target of the MNTB's inhibitory
projection)::

    # The left MNTB projects its inhibitory output to the left LSO; the
    # right MNTB projects its inhibitory output to the right LSO:
    #
    #   .../superior_olivary_complex/lateral_superior_olive/left/
    #   .../superior_olivary_complex/lateral_superior_olive/right/
    #
    # The MNTB's principal efferent target is the ipsilateral LSO.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mntb_side_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"medial_nucleus_of_trapezoid_body.{side}"
        )
        # resolve mntb_side_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The MNTB's neuron populations are prose, not modules:
    #   principal neurons (large glycinergic projection neurons) ->
    #       receive contralateral cochlear nuclei input via the calyx of
    #       Held (the largest synapse in the mammalian brain); project
    #       inhibitory (glycinergic) output to the ipsilateral LSO
    #   local circuit interneurons -> modulate the principal neurons
    #       within the MNTB
    #
    # Do not attempt to resolve these as sub-paths of the MNTB — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical MNTB anatomy:** Pickles, J.O. (2015). *An Introduction
    to the Physiology of Hearing*, 4th ed. (Medial nucleus of the
    trapezoid body and the glycinergic inhibitory relay — definitive.)
*   **MNTB — inhibitory relay:** Smith, P.H., Joris, P.X., Yin, T.C.T.
    (1998). "Anatomy and physiology of principal cells of the medial
    nucleus of the trapezoid body (MNTB) of the cat." *Journal of
    Neurophysiology* 79:3127–3142. (MNTB — glycinergic inhibitory
    relay; projects to the LSO.)
*   **Calyx of Held:** Held, H. (1893). *Die centrale Gehörleitung*.
    *Archiv für Anatomie und Physiologie* 17:201–248. (Original
    description of the calyx of Held — the giant presynaptic terminal
    on the MNTB principal neurons.)
*   **Calyx of Held — modern review:** Borst, J.G.G., Soria van Hoeve,
    J. (2012). "The calyx of Held synapse: from model synapse to
    auditory relay." *Annual Review of Physiology* 74:199–224. (Calyx
    of Held — the largest synapse in the mammalian brain; the MNTB
    principal neuron input.)
*   **LSO and MNTB — excitation-inhibition:** Tollin, D.J. (2003). "The
    lateral superior olive as a source of ascending and descending
    auditory pathways." *Journal of the Association for Research in
    Otolaryngology* 4:311–327. (LSO — ILD processing; MNTB inhibition.)
*   **Binaural sound localization — review:** Grothe, B., Pecka, M.,
    McAlpine, D. (2010). "Mechanisms of sound localization and coding
    in mammals." *Physiological Reviews* 90:983–1012. (LSO and MSO —
    ILD and ITD processing; MNTB as the inhibitory relay.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Medial nucleus of the
    trapezoid body in overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An
    Atlas of Structures, Sections, and Systems*, 8th ed. (MNTB and the
    pontomedullary junction.)
*   **Binaural hearing deficits:** Middlebrooks, J.C., Green, D.M.
    (1991). "Sound localization by human listeners." *Annual Review of
    Psychology* 42:135–159. (Binaural hearing deficits — impaired sound
    localization.)
*   **Presbycusis — MNTB involvement:** Frisina, R.D., Walton, J.P.
    (2006). "Age-related structural and functional changes in the
    auditory system." In *Handbook of the Biology of Aging*.
    (Presbycusis — MNTB age-related changes.)
*   **Multiple sclerosis — MNTB involvement:** Furst, M., Aharonson,
    V., Levine, R.A., et al. (2000). "Sound lateralization in patients
    with unilateral or bilateral multiple sclerosis." *Annals of
    Neurology* 47:389–393. (Multiple sclerosis — MNTB involvement;
    binaural hearing deficits.)
*   **Pontine stroke — MNTB involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — MNTB involvement; binaural hearing
    deficits.)
*   **LSO (contrast — the ILD processor sibling the MNTB PROJECTS TO):**
    Tollin, D.J. (2003). "The lateral superior olive as a source of
    ascending and descending auditory pathways." *Journal of the
    Association for Research in Otolaryngology* 4:311–327. (LSO — ILD
    processing; the MNTB's principal efferent target.)
*   **MSO (contrast — the ITD processor sibling):** Yin, T.C.T., Chan,
    J.C.K. (1990). "Interaural time sensitivity in medial superior
    olive of cat." *Journal of Neurophysiology* 64:465–488. (MSO — ITD
    processing; sibling of the MNTB.)
*   **Cochlear nuclei (contrast — the UPSTREAM monaural first-order
    relay):** Cant, N.B., Benson, C.G. (2003). "Parallel auditory
    pathways: projection patterns of the different neuronal populations
    in the cochlear nuclei." *Brain Research Bulletin* 60:457–474.
    (Cochlear nuclei — monaural first-order relay; the contralateral
    cochlear nuclei project to the MNTB via the trapezoid body.)
*   **Trapezoid body (contrast — the white-matter afferent tract the
    MNTB is NAMED AFTER):** Pickles, J.O. (2015). *An Introduction to
    the Physiology of Hearing*, 4th ed. (Trapezoid body — afferent
    white-matter tract from the cochlear nuclei to the MNTB.)
*   **Lateral lemniscus (contrast — the white-matter efferent tract of
    the SOC, NOT the MNTB's own efferent):** Pickles, J.O. (2015). *An
    Introduction to the Physiology of Hearing*, 4th ed. (Lateral
    lemniscus — efferent white-matter tract from the LSO and MSO to the
    inferior colliculus; NOT the MNTB's efferent.)
*   **Inferior colliculus (contrast — the midbrain downstream auditory
    relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002). "The
    inferior colliculus: a hub for the central auditory system." In
    *Integrative Functions in the Mammalian Auditory Pathway*. (Inferior
    colliculus — downstream of the LSO and MSO.)
*   **Medial geniculate body (contrast — the thalamic downstream
    auditory relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The
    Inferior Colliculus: A Hub for the Central Auditory System*. (Medial
    geniculate body — downstream of the inferior colliculus.)
*   **Primary auditory cortex (contrast — the cortical downstream
    auditory target):** Pickles, J.O. (2015). *An Introduction to the
    Physiology of Hearing*, 4th ed. (Primary auditory cortex — downstream
    of the medial geniculate body.)
*   **Facial nerve nucleus (contrast — the adjacent branchial motor
    nucleus):** May, M., Schaitkin, B.M. (2000). *The Facial Nerve*, 2nd
    ed. (Facial nerve nucleus — anatomically adjacent to the MNTB;
    functionally distinct.)
*   **Abducens nucleus (contrast — the adjacent somatic motor
    nucleus):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye
    Movements*, 5th ed. (Abducens nucleus — anatomically adjacent to the
    MNTB; functionally distinct.)
*   **SLEA (contrast — the MNTB is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the MNTB.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the MNTB.)
*   NeuroNames — Medial nucleus of the trapezoid body; FMA — Medial
    nucleus of trapezoid body.
"""