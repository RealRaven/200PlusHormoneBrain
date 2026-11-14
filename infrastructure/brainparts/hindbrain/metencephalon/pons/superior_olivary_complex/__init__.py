"""
infrastructure.brainparts.hindbrain.metencephalon.pons.superior_olivary_complex
==============================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── superior_olivary_complex   <-- THIS MODULE
                ├── left
                │   ├── lateral_superior_olive
                │   ├── medial_nucleus_of_trapezoid_body
                │   └── medial_superior_olive
                └── right
                    └── (mirror of left)

**Primary synonym:** Superior olivary complex; SOC; superior olivary
nuclei; "the pontine binaural sound-localization relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem special sensory nuclear complex** — a **bilateral
collection** of **anatomically delimited auditory nuclei** in the
**ventral pontine tegmentum**, at the **pontomedullary junction**, just
**dorsolateral to the trapezoid body** and **ventral to the facial
colliculus**. It is the **second-order central auditory relay** — the
**first brainstem site of binaural convergence** and the **principal
substrate** of **interaural time difference (ITD)** and **interaural
level difference (ILD)** processing for **horizontal sound
localization**.
**Part of:** The **pons** container — specifically, the **ventral
pontine tegmentum** (the **auditory relay** component). The **pons** is
the **metencephalic** brainstem segment.
**Structural parent:** ``.../pons/`` → **direct child** of the pons
container.
**Structural children:** **Two sub-containers** — ``left`` and
``right`` — the **bilateral halves** of the superior olivary complex.
Each of ``left`` and ``right`` is a **sub-container** with **three
structural children** — the ``lateral_superior_olive``, the
``medial_nucleus_of_trapezoid_body``, and the ``medial_superior_olive``.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
superior olivary complex is a CONTAINER, not a leaf.** It has **two
structural children** (``left`` and ``right``), each of which is a
**sub-container** with **three structural children**
(``lateral_superior_olive``, ``medial_nucleus_of_trapezoid_body``,
``medial_superior_olive``). Consumers must **not** treat the superior
olivary complex as a leaf, and must **not** assume the left, right, and
their sub-nuclei are absent — they are the **structural children and
grandchildren** of the superior olivary complex.
**Boundary status (BILATERAL CONTAINER — left and right are STRUCTURALLY
SYMMETRIC):** **Boundary case — the superior olivary complex is a
BILATERAL container.** The **left** and **right** sub-containers are
**structurally symmetric** — same three sub-nuclei under each
(lateral superior olive, medial nucleus of trapezoid body, medial
superior olive), same functional system (binaural sound localization),
same bilateral framing. The bilateral symmetry is **strict**. Consumers
must **not** assume a left/right asymmetry at the container level — the
container is a **strict mirror pair**. Any lateralization is documented
**inside the left and right sub-containers** and in the
**Lateralization Notes** below, not imported from elsewhere.
**Boundary status (BINAURAL SPECIAL SENSORY — NOT a monaural relay):**
**Boundary case — the superior olivary complex is BINAURAL SPECIAL
SENSORY, NOT a monaural relay.** Unlike the **cochlear nuclei**
(which **receive** monaural auditory input from the **ipsilateral**
cochlea and are the **first central auditory relay**), the **superior
olivary complex** (here) **receives bilateral auditory input** from
**both cochlear nuclei** (via the **trapezoid body**) and is the
**first site of binaural convergence** — the **first brainstem site**
where **left-ear** and **right-ear** signals **converge on the same
neuron**. It is the **principal substrate** of **binaural
sound-localization** (ITD and ILD processing). They are **DIFFERENT
STRUCTURES** — the **cochlear nuclei** are **monaural first-order**;
the **superior olivary complex** is **binaural second-order**. Consumers
must **not** conflate the superior olivary complex with the cochlear
nuclei.
**Boundary status (GREY-MATTER NUCLEI — NOT the trapezoid body):**
**Boundary case — the superior olivary complex is the GREY-MATTER
NUCLEI, NOT the trapezoid body.** The **trapezoid body** is the
**white-matter decussating tract** that **carries** the **bilateral
auditory axons** from the **cochlear nuclei** to the **superior
olivary complex** — the **afferent limb** of the binaural sound-
localization pathway. The **superior olivary complex** (here) is the
**grey-matter neuron clusters** that **receive** the trapezoid-body
axons and **project** to the **inferior colliculus** (via the
**lateral lemniscus**). They are **DIFFERENT STRUCTURES** — the
**nuclei** are grey matter; the **trapezoid body** is white matter.
**This distinction is clinically load-bearing** — a **superior olivary
complex lesion** causes **impaired sound localization** in the
**horizontal plane** (with **normal** pure-tone thresholds, because
the **cochlear nuclei** and the **ascending pathway** are intact); a
**trapezoid body lesion** causes **the same clinical syndrome** (the
superior olivary complex is cut off from its **contralateral cochlear
input**). Consumers must **not** conflate the superior olivary complex
with the trapezoid body.
**Boundary status (NOT the lateral lemniscus — that is the WHITE-MATTER
EFFERENT TRACT):** **Boundary case — the superior olivary complex is
NOT the lateral lemniscus.** The **lateral lemniscus** is the
**white-matter ascending tract** that **carries** the **efferent axons**
from the **superior olivary complex** (and the **cochlear nuclei**,
directly, via the **intermediate acoustic stria**) to the **inferior
colliculus**. The **superior olivary complex** (here) is the
**grey-matter neuron clusters** that **give rise to** the lateral
lemniscus axons. They are **DIFFERENT STRUCTURES** — the **nuclei** are
grey matter; the **lateral lemniscus** is white matter. Consumers must
**not** conflate the superior olivary complex with the lateral
lemniscus.
**Boundary status (NOT the cochlear nuclei — those are the UPSTREAM
MONAURAL FIRST-ORDER RELAY):** **Boundary case — the superior olivary
complex is NOT the cochlear nuclei.** The **cochlear nuclei**
(``.../vestibulocochlear_nuclei/cochlear_nuclei/``) are the **first
central auditory relay** — they **receive** the **monaural** auditory
input from the **ipsilateral cochlea** and **project** to the
**superior olivary complex** (via the **trapezoid body**) and the
**inferior colliculus** (via the **intermediate acoustic stria** and
the **lateral lemniscus**). The **superior olivary complex** (here) is
the **second-order binaural relay** that **receives** the bilateral
cochlear nuclei projections and **performs** the **first binaural
computation** (ITD and ILD processing). They are **DIFFERENT
STRUCTURES** — the **cochlear nuclei** are **monaural first-order**;
the **superior olivary complex** is **binaural second-order**.
**This distinction is clinically load-bearing** — a **cochlear nuclei
lesion** causes **ipsilateral sensorineural hearing loss** (because
the first-order relay is lost); a **superior olivary complex lesion**
causes **impaired sound localization in the horizontal plane** (because
the binaural computation is lost, but the **monaural auditory
sensitivity** — pure-tone thresholds — is **preserved**). Consumers
must **not** conflate the superior olivary complex with the cochlear
nuclei.
**Boundary status (NOT the inferior colliculus — that is the MIDBRAIN
DOWNSTREAM AUDITORY RELAY):** **Boundary case — the superior olivary
complex is NOT the inferior colliculus.** The **inferior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
and ``.../right/``) is the **midbrain auditory relay** — it **receives**
the **ascending auditory projections** from the **superior olivary
complex** (via the **lateral lemniscus**) and the **cochlear nuclei**
(via the **intermediate acoustic stria**) and **projects** to the
**medial geniculate body** of the thalamus. The **superior olivary
complex** (here) is the **pontine binaural relay** — it is **upstream**
of the inferior colliculus and the **site of the first binaural
computation**. They are **DIFFERENT STRUCTURES** — the **superior
olivary complex** is **pontine** and **upstream**; the **inferior
colliculus** is **midbrain** and **downstream**. Consumers must **not**
conflate the superior olivary complex with the inferior colliculus.
**Boundary status (NOT the medial geniculate body — that is the
THALAMIC DOWNSTREAM AUDITORY RELAY):** **Boundary case — the superior
olivary complex is NOT the medial geniculate body.** The **medial
geniculate body**
(``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
and ``.../right/``) is the **thalamic auditory relay** — it **receives**
the **ascending auditory projections** from the **inferior colliculus**
and **projects** to the **primary auditory cortex**. The **superior
olivary complex** (here) is the **pontine binaural relay** — it is
**upstream** of the medial geniculate body. They are **DIFFERENT
STRUCTURES** — the **superior olivary complex** is **pontine** and
**upstream**; the **medial geniculate body** is **diencephalic** and
**downstream**. Consumers must **not** conflate the superior olivary
complex with the medial geniculate body.
**Boundary status (NOT the primary auditory cortex — that is the CORTICAL
DOWNSTREAM AUDITORY TARGET):** **Boundary case — the superior olivary
complex is NOT the primary auditory cortex.** The **primary auditory
cortex** (Heschl's gyrus, Brodmann areas 41 and 42)
(``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
and ``.../right/``) is the **cortical target** of the **ascending
auditory pathway**. The **superior olivary complex** (here) is the
**pontine binaural relay** — it is **upstream** of the primary auditory
cortex. They are **DIFFERENT STRUCTURES** — the **superior olivary
complex** is **pontine** and **upstream**; the **primary auditory
cortex** is **cortical** and **downstream**. Consumers must **not**
conflate the superior olivary complex with the primary auditory cortex.
**Boundary status (NOT the facial nerve nucleus — that is a SIBLING
under the pons container, and the facial nerve fibers loop around the
abducens nucleus nearby):** **Boundary case — the superior olivary
complex is NOT the facial nerve nucleus.** The **facial nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
``.../right/``) is the **branchial motor** nucleus for the **muscles of
facial expression**. The **superior olivary complex** (here) is the
**auditory binaural relay**. They are **DIFFERENT STRUCTURES** —
different functional systems (branchial motor vs. auditory binaural
processing). They are **anatomically adjacent** (both are in the
**ventral pontine tegmentum**) — this proximity is a **classic source
of confusion** — consumers must **not** conflate the superior olivary
complex with the facial nerve nucleus.
**Boundary status (NOT the abducens nucleus — that is a SIBLING under
the cranial_nerve_nuclei container):** **Boundary case — the superior
olivary complex is NOT the abducens nucleus.** The **abducens nucleus**
(``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and ``.../right/``)
is the **somatic motor** nucleus for the **lateral rectus**. The
**superior olivary complex** (here) is the **auditory binaural relay**.
They are **DIFFERENT STRUCTURES** — different functional systems
(somatic motor vs. auditory binaural processing). They are
**anatomically adjacent** — the **superior olivary complex** is **near
the genu of the facial nerve** and the **abducens nucleus**; this
proximity is a **classic source of confusion** — consumers must **not**
conflate the superior olivary complex with the abducens nucleus.
**Boundary status (NOT the cochlear nerve or the vestibulocochlear
nerve — those are the PERIPHERAL AUDITORY CONDUCTION
INFRASTRUCTURE):** **Boundary case — the superior olivary complex is
NOT the cochlear nerve or the vestibulocochlear nerve.** The **cochlear
nerve** (the cochlear division of CN VIII) and the **vestibulocochlear
nerve** (CN VIII) are the **white-matter peripheral nerves** that
**carry** the **primary auditory axons** from the **spiral ganglion**
to the **cochlear nuclei**. The **superior olivary complex** (here) is
the **central grey-matter binaural relay** — it is **downstream** of
the cochlear nuclei and the **first site of binaural convergence**.
They are **DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **superior olivary complex** is **central grey
matter**. Consumers must **not** conflate the superior olivary complex
with the cochlear or vestibulocochlear nerve.
**Boundary status (NOT the pons or the pontine tegmentum — those are
the PARENT and its tegmentum):** **Boundary case — the superior olivary
complex is NOT the pons or the pontine tegmentum.** The **pons**
(``.../pons/``) is the **whole metencephalic brainstem segment**; the
**pontine tegmentum** is the **dorsal pontine grey-matter region**.
The **superior olivary complex** (here) is a **specific bilateral
nuclear complex** in the **ventral pontine tegmentum**. Consumers must
**not** conflate the superior olivary complex with the **whole pons**
or with the **whole pontine tegmentum**.
**Boundary status (NOT a single uniform nucleus — THREE functionally
distinct SUB-NUCLEI per side):** **Boundary case — the superior olivary
complex is NOT a single uniform nucleus; it contains THREE
functionally distinct sub-nuclei per side.** The **lateral superior
olive (LSO)** — the **principal substrate** of **interaural level
difference (ILD) processing** for **high-frequency sound localization**
(in humans, the LSO is smaller than in many other mammals, but it
retains ILD-related function). The **medial superior olive (MSO)** —
the **principal substrate** of **interaural time difference (ITD)
processing** for **low-frequency sound localization** (in humans, the
MSO is the **dominant** binaural sound-localization nucleus). The
**medial nucleus of the trapezoid body (MNTB)** — the **inhibitory
relay** that **receives** the **contralateral cochlear nuclei**
globular bushy cell projections (via the **trapezoid body**) and
**projects** an **inhibitory (glycinergic)** input to the **ipsilateral
LSO** — it is the **neural substrate** of **contralateral inhibition**
that is **essential** for **ILD processing**. **Each sub-nucleus is
functionally distinct** — the tree wires them as **structural children**
of ``left`` and ``right``. Consumers must **not** treat the superior
olivary complex as a single uniform nucleus — it is a **distributed
collection** of functionally distinct sub-nuclei.
**Boundary status (SLEA-FREE — the superior olivary complex is NOT an
extended-amygdala component):** **Boundary case — the superior olivary
complex is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **superior olivary complex** is an **auditory binaural
relay** — it is **NOT** an extended-amygdala component, and it carries
**NO SLEA warning**. Consumers must **not** import the SLEA warning
into the superior olivary complex — it is **SLEA-free**.

Overview
--------
The superior olivary complex is the **pontine binaural sound-localization
relay** — the **first site of binaural convergence** in the ascending
auditory pathway, where the **left-ear** and **right-ear** signals
converge on the same neuron. It is a **bilateral container** under the
pons container, with **two structural children** (``left`` and
``right``), each of which is a **sub-container** with **three structural
children** — the **lateral superior olive (LSO)**, the **medial nucleus
of the trapezoid body (MNTB)**, and the **medial superior olive (MSO)**.

**The superior olivary complex is a CONTAINER, NOT a leaf.** Its
structural children are ``left`` and ``right``; the **three sub-nuclei**
under each side (LSO, MNTB, MSO) are the **structural grandchildren**.

**The superior olivary complex is BINAURAL SPECIAL SENSORY, NOT a
monaural relay.** The **cochlear nuclei** are the **monaural
first-order relay**; the **superior olivary complex** is the **binaural
second-order relay** — the **first site of binaural convergence** and
the **principal substrate** of **ITD and ILD processing**.

**The superior olivary complex is GREY-MATTER NUCLEI, NOT the trapezoid
body.** The **trapezoid body** is the **white-matter afferent tract**;
the **lateral lemniscus** is the **white-matter efferent tract**. The
**superior olivary complex** is the **grey-matter neuron clusters** that
**receive** the trapezoid-body axons and **give rise to** the
lateral-lemniscus axons.

**The superior olivary complex is NOT the cochlear nuclei.** The
**cochlear nuclei** are the **monaural first-order relay**; the
**superior olivary complex** is the **binaural second-order relay**.
**This distinction is clinically load-bearing** — a **cochlear nuclei
lesion** causes **ipsilateral sensorineural hearing loss**; a
**superior olivary complex lesion** causes **impaired sound localization
in the horizontal plane** with **preserved pure-tone thresholds**.

**The superior olivary complex is NOT the inferior colliculus, the medial
geniculate body, or the primary auditory cortex.** Those are the
**downstream** auditory relays — the **superior olivary complex** is the
**pontine binaural relay**.

**The superior olivary complex is THREE-SUB-NUCLEI-PER-SIDE.** The
**LSO** (ILD processing), the **MNTB** (inhibitory relay for
contralateral inhibition), and the **MSO** (ITD processing) are
**functionally distinct** and are **structural children** of ``left``
and ``right``.

**The superior olivary complex is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Sub-Container and Sub-Nucleus Composition (structural children and
grandchildren, prose)
-----------------------------------------------------------------------
The superior olivary complex contains **two structural children** — the
``left`` and ``right`` sub-containers — each of which has **three
structural children** (the sub-nuclei):

*   **Lateral superior olive (LSO)**
    (``.../superior_olivary_complex/left/lateral_superior_olive/`` and
    ``.../right/``) — the **principal substrate** of **interaural level
    difference (ILD) processing** for **high-frequency sound
    localization**. The **LSO** receives **excitatory** input from the
    **ipsilateral cochlear nuclei** (via the **trapezoid body**) and
    **inhibitory** input from the **ipsilateral MNTB** (which itself
    receives **contralateral cochlear nuclei** input) — this
    **excitation-inhibition** arrangement is the **neural substrate** of
    **ILD processing** (the **LSO** neuron **compares** the **ipsilateral
    sound level** with the **contralateral sound level**). In humans,
    the LSO is **smaller** than in many other mammals (especially in
    **echo-locating bats and rodents**), but it **retains ILD-related
    function** — the **human LSO** is **less dominant** than the
    **human MSO** for binaural sound localization. **ILD processing is
    the functional system** subserved primarily by the LSO.

*   **Medial superior olive (MSO)**
    (``.../superior_olivary_complex/left/medial_superior_olive/`` and
    ``.../right/``) — the **principal substrate** of **interaural time
    difference (ITD) processing** for **low-frequency sound
    localization**. The **MSO** receives **bilateral excitatory** input
    from the **ipsilateral cochlear nuclei** and the **contralateral
    cochlear nuclei** (via the **trapezoid body**) — the **MSO** neuron
    acts as a **coincidence detector**, **firing maximally** when the
    **ipsilateral** and **contralateral** inputs arrive **simultaneously**
    (Jeffress model). **ITD processing is the functional system**
    subserved primarily by the MSO — the **human MSO** is the
    **dominant binaural sound-localization nucleus** (the **LSO** is
    **smaller** in humans).

*   **Medial nucleus of the trapezoid body (MNTB)**
    (``.../superior_olivary_complex/left/medial_nucleus_of_trapezoid_body/``
    and ``.../right/``) — the **inhibitory relay** that **receives** the
    **contralateral cochlear nuclei** globular bushy cell projections
    (via the **trapezoid body**) and **projects** an **inhibitory
    (glycinergic)** input to the **ipsilateral LSO**. The **MNTB** is
    the **neural substrate** of **contralateral inhibition** that is
    **essential** for **ILD processing** — the **MNTB** **converts**
    the **excitatory** contralateral cochlear-nuclei input into an
    **inhibitory** LSO input, so that the **LSO** can **compare** the
    **ipsilateral** and **contralateral** sound levels. **Inhibitory
    relay for ILD processing is the functional system** subserved
    primarily by the MNTB.

**These sub-nuclei are structural children of ``left`` and ``right``.**
The superior olivary complex's **structural children** are ``left`` and
``right``; the **sub-nuclei** (LSO, MNTB, MSO) are children of ``left``
and ``right``. Consumers resolving sub-nucleus detail go **through**
``left`` or ``right``.

The Superior Olivary Complex / Trapezoid Body Boundary
------------------------------------------------------
This is the **grey-matter vs. white-matter AFFERENT** boundary:

*   **Superior olivary complex** (this module) — the **grey-matter
    neuron clusters** that **receive** the trapezoid-body axons.

*   **Trapezoid body** — the **white-matter decussating tract** that
    **carries** the **bilateral auditory axons** from the **cochlear
    nuclei** to the **superior olivary complex** — the **afferent limb**
    of the **binaural sound-localization pathway**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**tract** is white matter. **This distinction is clinically
load-bearing** — a **superior olivary complex lesion** causes **impaired
sound localization in the horizontal plane**; a **trapezoid body
lesion** causes **the same clinical syndrome** (the superior olivary
complex is cut off from its **contralateral cochlear input**). Consumers
must **not** conflate the superior olivary complex with the trapezoid
body.

The Superior Olivary Complex / Lateral Lemniscus Boundary
--------------------------------------------------------
This is the **grey-matter vs. white-matter EFFERENT** boundary:

*   **Superior olivary complex** (this module) — the **grey-matter
    neuron clusters** that **give rise to** the lateral lemniscus axons.

*   **Lateral lemniscus** — the **white-matter ascending tract** that
    **carries** the **efferent axons** from the **superior olivary
    complex** (and the **cochlear nuclei**, directly, via the
    **intermediate acoustic stria**) to the **inferior colliculus**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**tract** is white matter. Consumers must **not** conflate the superior
olivary complex with the lateral lemniscus.

The Superior Olivary Complex / Cochlear Nuclei Boundary
------------------------------------------------------
This is the **binaural second-order vs. monaural first-order** boundary:

*   **Superior olivary complex** (this module) — the **binaural
    second-order relay** that **receives** bilateral cochlear nuclei
    projections and **performs** the **first binaural computation**.

*   **Cochlear nuclei**
    (``.../vestibulocochlear_nuclei/cochlear_nuclei/``) — the
    **monaural first-order relay** that **receives** the **monaural**
    auditory input from the **ipsilateral cochlea** and **projects** to
    the **superior olivary complex** (via the **trapezoid body**) and
    the **inferior colliculus** (via the **intermediate acoustic
    stria** and the **lateral lemniscus**).

**They are DIFFERENT STRUCTURES** — the **cochlear nuclei** are
**monaural first-order**; the **superior olivary complex** is **binaural
second-order**. **This distinction is clinically load-bearing** — a
**cochlear nuclei lesion** causes **ipsilateral sensorineural hearing
loss** (because the first-order relay is lost); a **superior olivary
complex lesion** causes **impaired sound localization in the horizontal
plane** (because the binaural computation is lost, but **monaural
auditory sensitivity** — pure-tone thresholds — is **preserved**).
Consumers must **not** conflate the superior olivary complex with the
cochlear nuclei.

The Superior Olivary Complex / Inferior Colliculus Boundary
-----------------------------------------------------------
This is the **pontine binaural relay vs. midbrain downstream relay**
boundary:

*   **Superior olivary complex** (this module) — the **pontine binaural
    relay** — the **first site of binaural convergence**.

*   **Inferior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/``
    and ``.../right/``) — the **midbrain auditory relay** that
    **receives** the **ascending auditory projections** from the
    **superior olivary complex** (via the **lateral lemniscus**) and
    the **cochlear nuclei** (via the **intermediate acoustic stria**)
    and **projects** to the **medial geniculate body**.

**They are DIFFERENT STRUCTURES** — the **superior olivary complex** is
**pontine** and **upstream**; the **inferior colliculus** is **midbrain**
and **downstream**. Consumers must **not** conflate the superior olivary
complex with the inferior colliculus.

The Superior Olivary Complex / Medial Geniculate Body Boundary
--------------------------------------------------------------
This is the **pontine binaural relay vs. thalamic downstream relay**
boundary:

*   **Superior olivary complex** (this module) — the **pontine binaural
    relay**.

*   **Medial geniculate body**
    (``.../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/``
    and ``.../right/``) — the **thalamic auditory relay** that
    **receives** the **ascending auditory projections** from the
    **inferior colliculus** and **projects** to the **primary auditory
    cortex**.

**They are DIFFERENT STRUCTURES** — the **superior olivary complex** is
**pontine** and **upstream**; the **medial geniculate body** is
**diencephalic** and **downstream**. Consumers must **not** conflate the
superior olivary complex with the medial geniculate body.

The Superior Olivary Complex / Primary Auditory Cortex Boundary
---------------------------------------------------------------
This is the **pontine binaural relay vs. cortical downstream target**
boundary:

*   **Superior olivary complex** (this module) — the **pontine binaural
    relay**.

*   **Primary auditory cortex** (Heschl's gyrus, Brodmann areas 41 and
    42)
    (``.../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/``
    and ``.../right/``) — the **cortical target** of the **ascending
    auditory pathway**.

**They are DIFFERENT STRUCTURES** — the **superior olivary complex** is
**pontine** and **upstream**; the **primary auditory cortex** is
**cortical** and **downstream**. Consumers must **not** conflate the
superior olivary complex with the primary auditory cortex.

The Superior Olivary Complex / Facial Nerve Nucleus Boundary
-----------------------------------------------------------
This is the **auditory binaural relay vs. branchial motor** boundary:

*   **Superior olivary complex** (this module) — the **auditory binaural
    relay**.

*   **Facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
    ``.../right/``) — the **branchial motor** nucleus for the **muscles
    of facial expression**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. branchial motor). They are
**anatomically adjacent** (both are in the **ventral pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the superior olivary complex with the
facial nerve nucleus.

The Superior Olivary Complex / Abducens Nucleus Boundary
--------------------------------------------------------
This is the **auditory binaural relay vs. somatic motor** boundary:

*   **Superior olivary complex** (this module) — the **auditory binaural
    relay**.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and
    ``.../right/``) — the **somatic motor** nucleus for the **lateral
    rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(auditory binaural processing vs. somatic motor). They are
**anatomically adjacent** — the **superior olivary complex** is **near
the genu of the facial nerve** and the **abducens nucleus**; this
proximity is a **classic source of confusion** — consumers must **not**
conflate the superior olivary complex with the abducens nucleus.

The Superior Olivary Complex / Cochlear and Vestibulocochlear Nerves
Boundary
--------------------------------------------------------------------
This is the **central grey matter vs. peripheral white matter** boundary:

*   **Superior olivary complex** (this module) — the **central grey-matter
    binaural relay**.

*   **Cochlear nerve** (the cochlear division of CN VIII) and
    **vestibulocochlear nerve** (CN VIII) — the **peripheral white-matter
    nerves** that **carry** the **primary auditory axons** from the
    **spiral ganglion** to the **cochlear nuclei**.

**They are DIFFERENT STRUCTURES** — the **nerves** are **peripheral
white matter**; the **superior olivary complex** is **central grey
matter**. Consumers must **not** conflate the superior olivary complex
with the cochlear or vestibulocochlear nerve.

The Superior Olivary Complex / Pons Boundary
--------------------------------------------
This is the **container vs. parent** boundary:

*   **Superior olivary complex** (this module) — the **auditory binaural
    relay** component of the **ventral pontine tegmentum** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal /
    corticobulbar tracts**, the **middle cerebellar peduncle**, the
    **cranial-nerve nuclei**, the **parabrachial area**, the **PPRF**,
    the **parvocellular reticular nucleus**, the **pontine nuclei**,
    and the **superior olivary complex**.

**The superior olivary complex is a child of the pons.** Consumers must
**not** conflate the superior olivary complex with the **whole pons**.

The Superior Olivary Complex / SLEA Boundary
--------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Superior olivary complex** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The superior olivary complex is NOT part of the SLEA continuum.** It is
an **auditory binaural relay**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the superior olivary
complex.

Function in the Human Brain
---------------------------
The superior olivary complex's functions are **binaural sound
localization in the horizontal plane** — **NOT a single unified
function**:

*   **Interaural Time Difference (ITD) Processing (Medial Superior
    Olive):** The **MSO** **receives** **bilateral excitatory** input
    from the **ipsilateral cochlear nuclei** and the **contralateral
    cochlear nuclei** (via the **trapezoid body**) and acts as a
    **coincidence detector** — it **fires maximally** when the
    **ipsilateral** and **contralateral** inputs arrive
    **simultaneously**. **ITD** is the **difference in arrival time**
    of a sound at the two ears — it is the **dominant cue** for
    **horizontal sound localization** of **low-frequency sounds**
    (< ~1.5 kHz in humans). **The human MSO** is the **dominant
    binaural sound-localization nucleus**.

*   **Interaural Level Difference (ILD) Processing (Lateral Superior
    Olive and MNTB):** The **LSO** **receives** **excitatory** input
    from the **ipsilateral cochlear nuclei** (via the **trapezoid
    body**) and **inhibitory** input from the **ipsilateral MNTB**
    (which itself receives **contralateral cochlear nuclei** input).
    **ILD** is the **difference in sound level** at the two ears — it
    is the **dominant cue** for **horizontal sound localization** of
    **high-frequency sounds** (> ~1.5 kHz in humans), because
    **high-frequency sounds** are **shadowed** by the **head** (the
    **head shadow effect**). The **MNTB** is the **inhibitory relay**
    that **converts** the **excitatory** contralateral cochlear-nuclei
    input into an **inhibitory** LSO input — the **neural substrate** of
    **contralateral inhibition** that is **essential** for ILD
    processing.

*   **Binaural Convergence:** The **superior olivary complex** is the
    **first site of binaural convergence** in the **ascending auditory
    pathway** — the **cochlear nuclei** are **monaural**, and the
    **inferior colliculus** and **higher centers** are **binaural**.
    The **superior olivary complex** **integrates** the **ipsilateral**
    and **contralateral** auditory signals into a **single binaural
    representation** of **sound-source location** in the **horizontal
    plane**.

*   **Topographic Organization:** The **MSO** and the **LSO** are
    **topographically organized** — **each MSO neuron** is **tuned** to
    a **specific ITD** (a **specific horizontal sound-source location**),
    and **each LSO neuron** is **tuned** to a **specific ILD** (a
    **specific horizontal sound-source location**). **This topographic
    organization** is the **neural substrate** of the **auditory
    space map** in the **brainstem**.

*   **NOT a neural processor in the classical sense.** The superior
    olivary complex is a **binaural relay** — it **receives** the
    **monaural** auditory signals from the **cochlear nuclei** and
    **performs** the **first binaural computation** (ITD and ILD
    processing) — it **projects** the **binaural** representation to
    the **inferior colliculus** (via the **lateral lemniscus**). The
    **processing** of **binaural sound localization** is **distributed**
    across the **cochlear nuclei** (monaural auditory processing), the
    **superior olivary complex** (binaural ITD and ILD processing), the
    **inferior colliculus** (integration of binaural and spectral cues
    and auditory space map), the **medial geniculate body** (thalamic
    relay), and the **primary auditory cortex** (cortical processing).
    The **superior olivary complex** is the **first binaural relay** —
    the **brainstem entry point** for **sound localization**.

**The unifying theme:** the superior olivary complex is the **pontine
binaural sound-localization relay** — the **first site of binaural
convergence** and the **principal substrate** of **ITD processing**
(via the MSO) and **ILD processing** (via the LSO and MNTB). It is
**three-sub-nuclei-per-side** (LSO for ILD; MNTB for contralateral
inhibition; MSO for ITD), **binaural special sensory** (not a monaural
relay), **SLEA-free**, and **NOT the trapezoid body** — the **trapezoid
body** is the **white-matter afferent tract** that the superior olivary
complex **receives from**.

Associated Disorders
--------------------
The superior olivary complex has **no named "superior olivary complex
syndrome"** — its clinical associations are **sub-nucleus-specific** and
**binaural-specific**:

*   **Superior Olivary Complex Lesion — Impaired Sound Localization with
    Preserved Pure-Tone Thresholds:** A lesion of the **superior olivary
    complex** (e.g. **pontine stroke**, **tumor**, **demyelination**)
    causes **impaired sound localization in the horizontal plane** with
    **preserved pure-tone thresholds** (because the **monaural auditory
    pathway** — the **cochlear nuclei** and the **ascending auditory
    pathway** — is intact). **The binaural-specific pattern** is the
    **substrate** of the **superior olivary complex** functions — this
    is the **classic "binaural hearing deficit"** that **distinguishes**
    a **superior olivary complex lesion** from a **cochlear nuclei
    lesion** (which causes **ipsilateral sensorineural hearing loss**)
    or a **middle ear lesion** (which causes **conductive hearing
    loss**).

*   **Binaural Hearing Deficit — Superior Olivary Complex Involvement:**
    **Binaural hearing** is the **ability to use** the **differences**
    between the **two ears** to **localize sound** and to **understand
    speech in noise** (the **binaural squelch effect** and the
    **binaural summation effect**). **The superior olivary complex** is
    **one of the neural substrates** of **binaural hearing**, and its
    dysfunction may **contribute** to **binaural hearing deficits** —
    **impaired sound localization**, **impaired speech understanding in
    noise**, and **impaired binaural unmasking** (the ability to detect
    a signal in noise by comparing the two ears).

*   **Auditory Neuropathy Spectrum Disorder (ANSD) — Superior Olivary
    Complex Sparing:** **Auditory neuropathy spectrum disorder** is a
    **hearing disorder** characterized by **preserved outer hair cell
    function** (otoacoustic emissions are present) but **disrupted
    auditory nerve response** (auditory brainstem response is abnormal or
    absent). **The superior olivary complex** is **spared** in
    **ANSD** — the disorder is at the **cochlear nerve** or **inner
    hair cell level**. Consumers must **not** conflate **ANSD** with a
    **superior olivary complex** lesion.

*   **Age-Related Hearing Loss (Presbycusis) — Superior Olivary Complex
    Involvement:** **Presbycusis** (age-related hearing loss) is
    characterized by **peripheral auditory dysfunction** (cochlear hair
    cell loss) **and central auditory dysfunction** (including
    **superior olivary complex** dysfunction). **The superior olivary
    complex** may show **age-related changes** — **reduced neuron
    number**, **reduced synaptic density**, and **reduced binaural
    processing** — contributing to **impaired sound localization** and
    **impaired speech understanding in noise** in **older adults**.

*   **Multiple Sclerosis — Superior Olivary Complex Involvement:**
    **Multiple sclerosis** can affect the **superior olivary complex**
    (as a **brainstem demyelinating lesion**), contributing to
    **impaired sound localization** and **binaural hearing deficits**.

*   **Pontine Stroke — Superior Olivary Complex Involvement:** A
    **pontine stroke** (e.g. **basilar artery** perforator territory)
    involving the **superior olivary complex** causes **impaired sound
    localization** in the **horizontal plane** — often accompanied by
    **other pontine signs** (**hemiparesis**, **facial palsy**,
    **abducens palsy**, **cerebellar ataxia**).

*   **No Named "Superior Olivary Complex Syndrome":** The superior
    olivary complex is a **bilateral container** of **three functionally
    distinct sub-nuclei per side** — it has **no named clinical syndrome**
    of its own. Its clinical relevance is **binaural-hearing-specific** —
    **impaired sound localization**, **impaired speech understanding in
    noise**, and **impaired binaural unmasking**.

**What is NOT here:** The superior olivary complex is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **vestibular neuritis** (vestibular nerve), **labyrinthitis**
(inner ear), or **auditory neuropathy spectrum disorder** (cochlear nerve
or hair cell). Its clinical relevance is **binaural-hearing-specific**,
via the **three functionally distinct sub-nuclei per side** it subserves.
**No named superior olivary complex syndrome exists.**

Lateralization Notes
--------------------
This is the **bilateral** superior olivary complex container. The
superior olivary complex is **bilaterally symmetric** with the **left**
and **right** sub-containers **strictly mirrored** — and it carries
**NO warning at the container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right**
    sub-containers are **structurally identical** — same three sub-nuclei
    under each (LSO, MNTB, MSO), same functional system (binaural sound
    localization), same bilateral framing. The bilateral symmetry is
    **strict**.

*   **Binaural Convergence (Structural Fact, NOT a Lateralization
    Warning):** The **left** and **right** superior olivary complexes
    are **binaural** — each receives **bilateral** input from the
    **left** and **right cochlear nuclei** (via the **trapezoid
    body**). **This bilateral input** is a **structural fact** of the
    **binaural sound-localization system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **first
    binaural computation** in the ascending auditory pathway.

*   **Ipsilateral and Contralateral Inputs (Structural Fact, NOT a
    Lateralization Warning):** The **left MSO** receives **ipsilateral
    (left) cochlear nuclei** input and **contralateral (right) cochlear
    nuclei** input; the **left LSO** receives **ipsilateral (left)
    cochlear nuclei** input and **inhibitory input** from the
    **ipsilateral (left) MNTB** (which itself receives **contralateral
    (right) cochlear nuclei** input). **These ipsilateral and
    contralateral inputs** are **structural facts** of the **binaural
    sound-localization system** — they are **not** functional
    lateralizations. They are the **neural substrate** of the **ITD and
    ILD processing** in the human brain.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The superior
    olivary complex is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the superior
    olivary complex.

*   **NO Amygdala-Lateralization Warning of their own (the superior
    olivary complex is BINAURAL AUDITORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The superior olivary
    complex is a **pontine binaural auditory relay** — consumers must
    **not** conflate it with the **amygdala** or with the **fear
    circuit**.

**A consumer that assumes "left superior olivary complex = right
superior olivary complex" will be structurally correct** — the two sides
are **strictly symmetric** (the binaural convergence and the
ipsilateral/contralateral inputs are structural facts, not
lateralizations). The superior olivary complex is a **strict-mirror pair
with NO warning at the container level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The container is **bilateral**, but
    it does **not** import ``left`` or ``right`` at module level — it
    exposes them as **structural children** and lets consumers resolve
    them through the memory/recall layer.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../pons/tegmentum/``, ``.../pons/parabrachial_area/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../pons/pontine_nuclei/``, ``.../midbrain/``,
    ``.../diencephalon/``, ``.../cortex/``, or any other container. The
    superior olivary complex's relationships to the **trapezoid body**,
    the **lateral lemniscus**, the **cochlear nuclei**, the **inferior
    colliculus**, the **medial geniculate body**, the **primary
    auditory cortex**, the **facial nerve nucleus**, the **abducens
    nucleus**, the **cochlear** and **vestibulocochlear nerves**, the
    **pons**, and the **SLEA continuum** are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children `left` and `right`, each
    with three structural children (LSO, MNTB, MSO).** The **sub-nuclei**
    are **structural grandchildren** of the superior olivary complex.
    Consumers must not conflate the container with its children or
    grandchildren.
*   **BILATERAL CONTAINER — left and right are STRUCTURALLY SYMMETRIC.**
    The **left** and **right** sub-containers are a **strict-mirror
    pair** with **no warning at the container level**. Any
    lateralization is documented **inside the left and right
    sub-containers** and in the **Lateralization Notes**.
*   **BINAURAL SPECIAL SENSORY — NOT a monaural relay.** The **superior
    olivary complex** is the **binaural second-order relay**; the
    **cochlear nuclei** are the **monaural first-order relay**.
    Consumers must **not** conflate the two.
*   **GREY-MATTER NUCLEI — NOT the trapezoid body or the lateral
    lemniscus.** The **trapezoid body** is the **afferent white-matter
    tract**; the **lateral lemniscus** is the **efferent white-matter
    tract**. The **superior olivary complex** is the **grey-matter
    neuron clusters** that receive from the trapezoid body and project
    to the lateral lemniscus. Consumers must **not** conflate the two.
*   **NOT the cochlear nuclei, the inferior colliculus, the medial
    geniculate body, or the primary auditory cortex — those are UPSTREAM
    or DOWNSTREAM auditory structures.** The **cochlear nuclei** are
    **upstream** (monaural first-order); the **inferior colliculus**,
    **medial geniculate body**, and **primary auditory cortex** are
    **downstream**. Consumers must **not** conflate the superior olivary
    complex with any of them.
*   **NOT the facial nerve nucleus or the abducens nucleus — those are
    anatomically adjacent SIBLINGS.** Consumers must **not** conflate
    the superior olivary complex with either of them.
*   **NOT the cochlear or vestibulocochlear nerve — those are the
    PERIPHERAL AUDITORY CONDUCTION INFRASTRUCTURE.** Consumers must
    **not** conflate the superior olivary complex with either nerve.
*   **NOT a single uniform nucleus — THREE functionally distinct
    sub-nuclei per side.** The **LSO** (ILD processing), **MNTB**
    (inhibitory relay), and **MSO** (ITD processing) are **structural
    children** of ``left`` and ``right``. Consumers must **not** treat
    the superior olivary complex as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The superior
    olivary complex is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output — the superior olivary complex is BINAURAL
    AUDITORY.** The **fear-output** structure is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **superior olivary complex** is a **pontine binaural
    auditory relay** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The superior olivary complex is a local
    container under the pons container, not a cross-listed container.
*   **No nested cross-listing.** The superior olivary complex has no
    nested dual-framing module. It is a single bilateral container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import superior_olivary_complex

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.superior_olivary_complex"
    )

**Do not** assume the superior olivary complex is a **leaf**. It is a
**container** — its structural children are ``left`` and ``right``, each
of which is a **sub-container** with **three structural children** (LSO,
MNTB, MSO).

**Do not** assume the **three sub-nuclei** (LSO, MNTB, MSO) are **direct
structural children** of the superior olivary complex. They are
**structural grandchildren** under ``left`` and ``right``.

**Do not** assume the superior olivary complex is the **trapezoid body**
or the **lateral lemniscus**. The **trapezoid body** is the **afferent
white-matter tract**; the **lateral lemniscus** is the **efferent
white-matter tract**. The **superior olivary complex** is the
**grey-matter neuron clusters** that receive from the trapezoid body and
project to the lateral lemniscus.

**Do not** assume the superior olivary complex is the **cochlear
nuclei**. The **cochlear nuclei** are the **monaural first-order
relay**; the **superior olivary complex** is the **binaural second-order
relay**.

**Do not** assume the superior olivary complex is the **inferior
colliculus**, the **medial geniculate body**, or the **primary auditory
cortex**. Those are the **downstream** auditory relays — the **superior
olivary complex** is the **pontine binaural relay**.

**Do not** assume the superior olivary complex is the **facial nerve
nucleus** or the **abducens nucleus**. Those are **anatomically
adjacent siblings** — different functional systems.

**Do not** assume the superior olivary complex is the **cochlear nerve**
or the **vestibulocochlear nerve**. Those are the **peripheral auditory
conduction infrastructure** — the superior olivary complex is **central
grey matter**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the superior olivary complex. **The superior olivary
complex is SLEA-FREE** — it is **not** an extended-amygdala component,
and it is **NOT part of the fear circuit**.

Iterating the superior olivary complex's structural children (recommended
consumer pattern)::

    SUPERIOR_OLIVARY_COMPLEX_CHILDREN = ("left", "right")
    # The container is bilateral. The three sub-nuclei (LSO, MNTB, MSO)
    # are structural grandchildren under left and right — not direct
    # structural children of the superior olivary complex.

Iterating the superior olivary complex's sub-nuclei (recommended consumer
pattern — through `left` or `right`)::

    for side in ("left", "right"):
        for sub in (
            "lateral_superior_olive",
            "medial_nucleus_of_trapezoid_body",
            "medial_superior_olive",
        ):
            sub_path = (
                f"hindbrain.metencephalon.pons.superior_olivary_complex."
                f"{side}.{sub}"
            )
            # resolve sub_path through the memory/recall layer

Reaching the trapezoid body (recommended consumer pattern — the
white-matter afferent tract)::

    # The trapezoid body is the WHITE-MATTER afferent tract from the
    # cochlear nuclei to the superior olivary complex:
    #
    #   .../white_matter/.../trapezoid_body/  (or equivalent path)
    #
    # The superior olivary complex RECEIVES the trapezoid body axons; the
    # trapezoid body is the AFFERENT limb of the binaural
    # sound-localization pathway.

Reaching the lateral lemniscus (recommended consumer pattern — the
white-matter efferent tract)::

    # The lateral lemniscus is the WHITE-MATTER efferent tract from the
    # superior olivary complex (and the cochlear nuclei, via the
    # intermediate acoustic stria) to the inferior colliculus:
    #
    #   .../white_matter/.../lateral_lemniscus/  (or equivalent path)
    #
    # The superior olivary complex GIVES RISE TO the lateral lemniscus
    # axons; the lateral lemniscus is the EFFERENT limb of the binaural
    # sound-localization pathway.

Reaching the cochlear nuclei (recommended consumer pattern — the
UPSTREAM monaural first-order relay)::

    # The cochlear nuclei are the MONAURAL FIRST-ORDER relay — they
    # project to the superior olivary complex (via the trapezoid body):
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/cochlear_nuclei/  (and right/)
    #
    # The cochlear nuclei are UPSTREAM (monaural first-order); the
    # superior olivary complex is DOWNSTREAM (binaural second-order).

Reaching the inferior colliculus (recommended consumer pattern — the
DOWNSTREAM midbrain auditory relay)::

    # The inferior colliculus is the DOWNSTREAM midbrain auditory relay:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/inferior_colliculus/  (and right/)
    #
    # The superior olivary complex is UPSTREAM of the inferior colliculus;
    # the inferior colliculus is DOWNSTREAM of the superior olivary
    # complex.

Reaching the medial geniculate body (recommended consumer pattern — the
DOWNSTREAM thalamic auditory relay)::

    # The medial geniculate body is the DOWNSTREAM thalamic auditory
    # relay:
    #
    #   .../diencephalon/thalamus/left/metathalamus/medial_geniculate_body/  (and right/)
    #
    # The superior olivary complex is UPSTREAM of the medial geniculate
    # body; the medial geniculate body is DOWNSTREAM of the superior
    # olivary complex.

Reaching the primary auditory cortex (recommended consumer pattern — the
DOWNSTREAM cortical auditory target)::

    # The primary auditory cortex (Heschl's gyrus, Brodmann areas 41 and
    # 42) is the DOWNSTREAM cortical auditory target:
    #
    #   .../cerebral_hemispheres/left/cortex/temporal/cortex/primary_auditory_cortex/  (and right/)
    #
    # The superior olivary complex is UPSTREAM of the primary auditory
    # cortex; the primary auditory cortex is DOWNSTREAM of the superior
    # olivary complex.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        soc_path = (
            f"hindbrain.metencephalon.pons.superior_olivary_complex."
            f"{side}"
        )
        # resolve soc_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The superior olivary complex's three sub-nuclei per side are
    # structural children of left and right:
    #   lateral_superior_olive (LSO)      -> interaural level difference
    #                                        (ILD) processing; high-
    #                                        frequency sound localization;
    #                                        receives ipsilateral
    #                                        cochlear nuclei excitation
    #                                        and ipsilateral MNTB
    #                                        inhibition
    #   medial_nucleus_of_trapezoid_body  -> inhibitory relay (glycinergic);
    #   (MNTB)                               receives contralateral
    #                                        cochlear nuclei globular
    #                                        bushy cell input; projects
    #                                        inhibitory input to ipsilateral
    #                                        LSO; essential for ILD
    #                                        processing
    #   medial_superior_olive (MSO)       -> interaural time difference
    #                                        (ITD) processing; low-
    #                                        frequency sound localization;
    #                                        receives bilateral excitatory
    #                                        cochlear nuclei input;
    #                                        coincidence detector
    #
    # Do not attempt to resolve these as sub-paths of the superior
    # olivary complex — resolve them at the sub-nucleus level through
    # the left and right sub-containers.

References
----------
*   **Canonical superior olivary complex anatomy:** Pickles, J.O. (2015).
    *An Introduction to the Physiology of Hearing*, 4th ed. (Superior
    olivary complex and binaural sound localization — definitive.)
*   **Binaural sound localization — review:** Grothe, B., Pecka, M.,
    McAlpine, D. (2010). "Mechanisms of sound localization and coding in
    mammals." *Physiological Reviews* 90:983–1012. (Superior olivary
    complex — ITD and ILD processing; MSO and LSO.)
*   **MSO and ITD processing:** Yin, T.C.T., Chan, J.C.K. (1990).
    "Interaural time sensitivity in medial superior olive of cat."
    *Journal of Neurophysiology* 64:465–488. (MSO — ITD processing;
    coincidence detection.)
*   **LSO and ILD processing:** Tollin, D.J. (2003). "The lateral
    superior olive as a source of ascending and descending auditory
    pathways." *Journal of the Association for Research in Otolaryngology*
    4:311–327. (LSO — ILD processing; MNTB inhibition.)
*   **MNTB — inhibitory relay:** Smith, P.H., Joris, P.X., Yin, T.C.T.
    (1998). "Anatomy and physiology of principal cells of the medial
    nucleus of the trapezoid body (MNTB) of the cat." *Journal of
    Neurophysiology* 79:3127–3142. (MNTB — inhibitory relay for ILD
    processing.)
*   **Human binaural processing:** Middlebrooks, J.C. (2015). "Sound
    localization." In *The Auditory System*. (Human binaural sound
    localization — MSO dominance and LSO contribution.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Superior olivary complex
    in overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An Atlas
    of Structures, Sections, and Systems*, 8th ed. (Superior olivary
    complex and the pontomedullary junction.)
*   **Binaural hearing deficits:** Middlebrooks, J.C., Green, D.M.
    (1991). "Sound localization by human listeners." *Annual Review of
    Psychology* 42:135–159. (Binaural hearing deficits — impaired sound
    localization.)
*   **Age-related hearing loss (presbycusis) — superior olivary complex
    involvement:** Frisina, R.D., Walton, J.P. (2006). "Age-related
    structural and functional changes in the auditory system." In
    *Handbook of the Biology of Aging*. (Presbycusis — superior olivary
    complex age-related changes.)
*   **Multiple sclerosis — superior olivary complex involvement:**
    Furst, M., Aharonson, V., Levine, R.A., et al. (2000). "Sound
    lateralization in patients with unilateral or bilateral
    multiple sclerosis." *Annals of Neurology* 47:389–393. (Multiple
    sclerosis — superior olivary complex involvement; binaural hearing
    deficits.)
*   **Pontine stroke — superior olivary complex involvement:** Bassetti,
    C., Bogousslavsky, J., Barth, A., Regli, F. (1996). "Isolated
    infarcts of the pontine nuclei: a clinical and neuroimaging study."
    *Brain* 119:1237–1253. (Pontine stroke — superior olivary complex
    involvement; binaural hearing deficits.)
*   **Trapezoid body (contrast — the white-matter afferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Trapezoid body — afferent white-matter tract
    from the cochlear nuclei to the superior olivary complex.)
*   **Lateral lemniscus (contrast — the white-matter efferent tract):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Lateral lemniscus — efferent white-matter tract
    from the superior olivary complex to the inferior colliculus.)
*   **Cochlear nuclei (contrast — the monaural first-order relay):**
    Cant, N.B., Benson, C.G. (2003). "Parallel auditory pathways:
    projection patterns of the different neuronal populations in the
    cochlear nuclei." *Brain Research Bulletin* 60:457–474. (Cochlear
    nuclei — monaural first-order relay; projects to the superior
    olivary complex via the trapezoid body.)
*   **Inferior colliculus (contrast — the midbrain downstream auditory
    relay):** Casseday, J.H., Fremouw, T., Covey, E. (2002). "The
    inferior colliculus: a hub for the central auditory system." In
    *Integrative Functions in the Mammalian Auditory Pathway*. (Inferior
    colliculus — downstream of the superior olivary complex.)
*   **Medial geniculate body (contrast — the thalamic downstream auditory
    relay):** Winer, J.A., Schreiner, C.E. (eds.) (2005). *The Inferior
    Colliculus: A Hub for the Central Auditory System*. (Medial
    geniculate body — downstream of the superior olivary complex.)
*   **Primary auditory cortex (contrast — the cortical downstream
    auditory target):** Pickles, J.O. (2015). *An Introduction to the
    Physiology of Hearing*, 4th ed. (Primary auditory cortex — downstream
    of the superior olivary complex.)
*   **Facial nerve nucleus (contrast — the adjacent branchial motor
    nucleus):** May, M., Schaitkin, B.M. (2000). *The Facial Nerve*, 2nd
    ed. (Facial nerve nucleus — anatomically adjacent to the superior
    olivary complex; functionally distinct.)
*   **Abducens nucleus (contrast — the adjacent somatic motor
    nucleus):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye
    Movements*, 5th ed. (Abducens nucleus — anatomically adjacent to the
    superior olivary complex; functionally distinct.)
*   **SLEA (contrast — the superior olivary complex is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the superior
    olivary complex.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the superior olivary complex.)
*   NeuroNames — Superior olivary complex; FMA — Superior olivary complex.
"""
