"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei
============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── perihypoglossal_nuclei   <-- THIS MODULE
                ├── left
                │   ├── intercalated_nucleus
                │   └── prepositus_nucleus
                └── right
                    ├── intercalated_nucleus
                    └── prepositus_nucleus

**Primary synonym:** Perihypoglossal nuclei; perihypoglossal nuclear
complex; PHN; nuclei perihipoglossi; perihypoglossal complex of
the medulla.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nuclear complex** — a group of **small
nuclei** surrounding the **hypoglossal nucleus** in the
**dorsal medulla oblongata**, comprising the **intercalated
nucleus** (nucleus intercalatus / Staderini's nucleus) and the
**prepositus nucleus** (nucleus prepositus hypoglossi / NPH).
It is **NOT** the **hypoglossal nucleus** itself — the
perihypoglossal nuclei are **separate structures** that **surround
the hypoglossal nucleus** ("peri-" = "around") and are involved
in **oculomotor control** and **gaze holding**, **NOT** tongue
motor control. It is **also NOT** the **nucleus of Roller**
(sometimes grouped with the PHN but not wired in this tree), the
**abducens nucleus** (pons), the **PPRF** (pons), the
**vestibular nuclei** (different medullary region), or the
**nucleus ambiguus** (ventrolateral medulla).
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each a
**container** (not a leaf) with **two leaf children**:
1. ``intercalated_nucleus`` — the **intercalated nucleus of
   Staderini** — an **oculomotor** nucleus involved in
   **vertical gaze** and **vestibulo-ocular** integration.
2. ``prepositus_nucleus`` — the **prepositus nucleus (NPH)** —
   the **neural integrator** for **horizontal gaze holding**.
**Boundary status (NOT the hypoglossal nucleus — a DIFFERENT
structure with a SIMILAR name):** **Boundary case — the
perihypoglossal nuclei are NOT the hypoglossal nucleus.** The
**hypoglossal nucleus** (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``
and ``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is
the **somatic motor** nucleus for the **tongue** — it is **NOT**
part of the perihypoglossal complex. The **perihypoglossal
nuclei** (here) are named **because** they **surround** the
hypoglossal nucleus ("peri-" = "around" + "hypoglossal") — they
are **anatomically adjacent** but **functionally distinct**.
The **hypoglossal nucleus** is **motor** (tongue); the
**perihypoglossal nuclei** are **oculomotor** (gaze holding and
vertical gaze). **They share the name "hypoglossal" but are
DIFFERENT STRUCTURES in DIFFERENT CONTAINERS** — resolve the
hypoglossal nucleus via ``cranial_nerve_nuclei``.
**Boundary status (NOT the nucleus of Roller — sometimes grouped
with the PHN but NOT in this tree):** **Boundary case — the
perihypoglossal nuclei are NOT the nucleus of Roller.** The
**nucleus of Roller** (nucleus rolleri) is a **small medullary
nucleus** that is **sometimes grouped** with the perihypoglossal
complex in the literature — it lies **ventral and lateral** to
the **hypoglossal nucleus**. In **this tree**, the nucleus of
Roller is **NOT wired** as a structural child of the
perihypoglossal nuclei — only the **intercalated nucleus** and
the **prepositus nucleus** are. Consumers must **not** expect
to find the nucleus of Roller under
``perihypoglossal_nuclei`` — resolve it via the references.
**Boundary status (NOT the abducens nucleus — a PONTINE
structure):** **Boundary case — the perihypoglossal nuclei are
NOT the abducens nucleus.** The **abducens nucleus (VI)**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``
and ``.../metencephalon/pons/cranial_nerve_nuclei/right/abducens_nucleus/``)
is a **pontine branchial motor** nucleus — it supplies the
**lateral rectus muscle** and contains the **abducens
internuclear neurons** that **drive** the **contralateral
medial rectus** during **horizontal saccades**. The
**perihypoglossal nuclei** (here) are **medullary oculomotor**
nuclei — they are **NOT** the abducens nucleus. **They are
functionally coupled** in the **horizontal gaze** system — the
**prepositus nucleus** is the **neural integrator** that
**holds** the **horizontal gaze** position after the
**abducens/PPRF** drives the **saccade**. But the **abducens
nucleus** is **pontine**; the **perihypoglossal nuclei** are
**medullary**. Consumers must **not** conflate the two.
**Boundary status (NOT the paramedian pontine reticular formation
(PPRF) — a PONTINE structure):** **Boundary case — the
perihypoglossal nuclei are NOT the paramedian pontine reticular
formation (PPRF).** The **PPRF**
(``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``)
is the **pontine horizontal saccade generator** — it **drives**
the **abducens nucleus** for **horizontal saccades**. The
**perihypoglossal nuclei** (here) are **medullary oculomotor**
nuclei — the **prepositus nucleus** is the **neural
integrator** for **horizontal gaze holding** (the **"memory"**
of the gaze position after the saccade). **They are
functionally coupled** but **anatomically distinct** — the
**PPRF** is **pontine**; the **perihypoglossal nuclei** are
**medullary**. Consumers must **not** conflate the two.
**Boundary status (NOT the vestibular nuclei — a DIFFERENT
medullary region):** **Boundary case — the perihypoglossal
nuclei are NOT the vestibular nuclei.** The **vestibular
nuclei** (superior, medial, lateral, inferior)
(``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``
and ``.../metencephalon/pons/cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
are **pontomedullary** structures that **receive** vestibular
afferents and **drive** the **vestibulo-ocular reflex (VOR)**
and **postural control**. The **perihypoglossal nuclei** (here)
are **medullary oculomotor** nuclei — they **receive** input
from the **vestibular nuclei** and **project** to the
**abducens nucleus** and other **oculomotor** structures, but
they are **NOT** the vestibular nuclei themselves. Consumers
must **not** conflate the two.
**Boundary status (NOT the medial longitudinal fasciculus (MLF)
— a white-matter tract):** **Boundary case — the
perihypoglossal nuclei are NOT the medial longitudinal
fasciculus (MLF).** The **MLF** is a **white-matter tract**
that **connects** the **abducens nucleus** to the
**contralateral oculomotor nucleus** (for **horizontal gaze**)
and **connects** the **vestibular nuclei** to the
**oculomotor/trochlear nuclei** (for the **VOR**). The
**perihypoglossal nuclei** (here) are **grey-matter nuclei** —
they **project** to the **abducens nucleus** and **other
oculomotor** structures **via** the **MLF** and **other
pathways**, but they are **NOT** the MLF. Consumers must **not**
conflate the **nuclei** with the **white-matter tract**.
**Boundary status (NOT the nucleus ambiguus — a DIFFERENT
medullary structure):** **Boundary case — the perihypoglossal
nuclei are NOT the nucleus ambiguus.** The **nucleus ambiguus**
(``.../cranial_nerve_nuclei/left/nucleus_ambiguus/`` and
``.../cranial_nerve_nuclei/right/nucleus_ambiguus/``) is a
**branchial motor** nucleus in the **ventrolateral medulla** —
it supplies the **striated muscles of the pharynx and larynx**.
The **perihypoglossal nuclei** (here) are **dorsal medullary
oculomotor** nuclei — they are **NOT** the nucleus ambiguus.
Consumers must **not** conflate the two.
**Boundary status (NOT the solitary nucleus — a visceral
afferent relay):** **Boundary case — the perihypoglossal nuclei
are NOT the solitary nucleus.** The **solitary nucleus (NTS)**
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
**NOT** an oculomotor structure. Consumers must **not** conflate
the two.
**Boundary status (NOT the dorsal motor nucleus of the vagus or
other cranial nerve nuclei — motor nuclei):** **Boundary case —
the perihypoglossal nuclei are NOT the cranial nerve motor
nuclei.** The **cranial nerve nuclei**
(``.../cranial_nerve_nuclei/``) are the **medullary motor**
nuclei (hypoglossal, dorsal motor vagus, inferior salivatory,
nucleus ambiguus). The **perihypoglossal nuclei** (here) are
**oculomotor nuclei** — **NOT** cranial nerve motor nuclei.
Consumers must **not** conflate the two.
**Boundary status (NOT the medullary pyramid — a white-matter
tract):** **Boundary case — the perihypoglossal nuclei are NOT
the medullary pyramid.** The **medullary pyramid**
(``.../medullary_pyramid/``) is the **ventral white-matter**
corticospinal / corticobulbar tract. The **perihypoglossal
nuclei** (here) are **dorsal medullary grey-matter** nuclei.
Consumers must **not** conflate the two.
**Boundary status (NOT the olivary body, arcuate nucleus,
parafacial zone, paramedian reticular nucleus, or respiratory
centers — DIFFERENT structures):** **Boundary case — the
perihypoglossal nuclei are NOT these other medullary
structures.** Each is a **different structure** — see the
respective modules for their boundary stacks. Consumers must
**not** conflate the **perihypoglossal nuclei** with any of
these.
**Boundary status (NOT the whole medulla oblongata — a small
nuclear complex within it):** **Boundary case — the
perihypoglossal nuclei are NOT the whole medulla oblongata.**
The **medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the cranial nerve nuclei, the
autonomic nuclei, the respiratory centers, the olivary body, the
medullary pyramid, the arcuate nucleus, the parafacial zone, the
paramedian reticular nucleus, the perihypoglossal nuclei (here),
and other structures. The **perihypoglossal nuclei** are **a
small nuclear complex** within the medulla. Consumers must
**not** conflate the **PHN** with the **whole medulla**.
**Boundary status (BILATERAL container with TWO-LEVEL container
structure):** **Boundary case — the perihypoglossal nuclei are a
BILATERAL container with a TWO-LEVEL container structure.** The
**perihypoglossal_nuclei** module (here) is an **unpaired
container**; its **structural children** are ``left`` and
``right`` — each a **container** (not a leaf) with **two leaf
children**: the ``intercalated_nucleus`` and the
``prepositus_nucleus``. Consumers must **not** expect the two
nuclei to be wired **directly** under ``perihypoglossal_nuclei``
— they are under ``left/`` and ``right/``. Resolve them via
``perihypoglossal_nuclei.{left,right}.<nucleus>``.

Overview
--------
The **perihypoglossal nuclei (PHN)** are a **group of small
medullary grey-matter nuclei** that **surround the hypoglossal
nucleus** in the **dorsal medulla** — the **intercalated
nucleus** (nucleus intercalatus / Staderini's nucleus) and the
**prepositus nucleus** (nucleus prepositus hypoglossi / NPH).
They are **oculomotor** structures — they **participate** in
**gaze holding** (the **prepositus nucleus**) and **vertical
gaze** integration (the **intercalated nucleus**), and they are
**functionally coupled** to the **abducens nucleus**, the
**PPRF**, the **vestibular nuclei**, and the **oculomotor
nuclei** in the **horizontal and vertical gaze** systems.

**The perihypoglossal nuclei are the PERIHYPOGLOSSAL nuclei, NOT
the hypoglossal nucleus.** They are **named because** they
**surround** the hypoglossal nucleus ("peri-" = "around" +
"hypoglossal") — but they are **separate structures** with
**different functions** — the **hypoglossal nucleus** is
**motor** (tongue); the **perihypoglossal nuclei** are
**oculomotor** (gaze). Consumers must **not** conflate the two.

**The perihypoglossal nuclei are a BILATERAL container with a
TWO-LEVEL container structure.** Its structural children are
``left`` and ``right`` — each a **container** with **two leaf
children** (the intercalated nucleus and the prepositus nucleus).
The **container itself** is **unpaired**.

**The perihypoglossal nuclei are OCULOMOTOR, NOT motor,
NOT visceral, and NOT autonomic.** They **do not** send motor
axons to muscles and **do not** regulate autonomic function.
They **participate** in **gaze holding**, **vertical gaze**,
and **vestibulo-ocular integration** — they are **part of** the
**oculomotor** system.

**The perihypoglossal nuclei are the neural integrator for
horizontal gaze holding (prepositus nucleus) and a vertical
gaze integration structure (intercalated nucleus).** The
**prepositus nucleus** is the **neural integrator** for
**horizontal gaze** — it **holds** the **horizontal eye
position** after a **saccade** (the **"memory"** of the gaze
position), and it **participates** in **horizontal
vestibulo-ocular reflex** integration. The **intercalated
nucleus** is involved in **vertical gaze** integration and
**vertical vestibulo-ocular reflex** processing.

Bilateral Structure
-------------------
The perihypoglossal nuclei are a **bilateral container** with
**two structural children**, each a **container** (not a leaf):

*   ``left`` — the **left** perihypoglossal nuclei (a **container**
    with the intercalated nucleus and prepositus nucleus as leaf
    children).
*   ``right`` — the **right** perihypoglossal nuclei (a
    **container** with the intercalated nucleus and prepositus
    nucleus as leaf children).

**Each side is itself a container.** The ``left`` and ``right``
modules each have **two leaf children**:

*   ``intercalated_nucleus`` — the **intercalated nucleus of
    Staderini** — an **oculomotor** nucleus involved in
    **vertical gaze**.
*   ``prepositus_nucleus`` — the **prepositus nucleus (NPH)** —
    the **neural integrator** for **horizontal gaze holding**.

**The container itself is unpaired.** There is **no**
``perihypoglossal_nuclei/left/.../left/`` — the ``left`` and
``right`` modules are **containers** with the two nuclei as their
**leaf children**.

**Two-level container structure:** ``perihypoglossal_nuclei`` →
``left`` / ``right`` → ``{intercalated_nucleus,
prepositus_nucleus}``. Consumers that need **side-specific**
resolution descend into ``left`` or ``right`` and then into one
of the two nuclei; consumers that need **bilateral** resolution
iterate over both sides and both nuclei.

The Perihypoglossal Nuclei / Hypoglossal Nucleus Boundary
---------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Perihypoglossal nuclei** (this module) — the **oculomotor**
    nuclei that **surround** the hypoglossal nucleus.

*   **Hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/`` and
    ``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **somatic motor** nucleus for the **tongue**.

**They share the name "hypoglossal" but are DIFFERENT STRUCTURES
in DIFFERENT CONTAINERS with DIFFERENT FUNCTIONS** — the
**hypoglossal nucleus** is **motor** (tongue); the
**perihypoglossal nuclei** are **oculomotor** (gaze). Consumers
must **not** conflate the two — resolve the hypoglossal nucleus
via ``cranial_nerve_nuclei``.

The Perihypoglossal Nuclei / Nucleus of Roller Boundary
-------------------------------------------------------
This is the **sometimes-grouped** boundary:

*   **Perihypoglossal nuclei** (this module) — the **intercalated
    nucleus** and **prepositus nucleus**.

*   **Nucleus of Roller** — a **small medullary nucleus**
    sometimes grouped with the PHN in the literature, **NOT**
    wired in this tree.

**The nucleus of Roller is NOT wired** as a structural child of
the perihypoglossal nuclei — only the intercalated nucleus and
the prepositus nucleus are. Consumers must **not** expect to find
the nucleus of Roller under ``perihypoglossal_nuclei`` — resolve
it via the references.

The Perihypoglossal Nuclei / Abducens Nucleus and PPRF Boundary
---------------------------------------------------------------
This is the **gaze-holding / gaze-generating** boundary:

*   **Perihypoglossal nuclei** (this module) — the **medullary**
    oculomotor nuclei (prepositus nucleus = neural integrator
    for horizontal gaze holding).

*   **Abducens nucleus**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``
    and
    ``.../metencephalon/pons/cranial_nerve_nuclei/right/abducens_nucleus/``)
    and **PPRF**
    (``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``)
    — the **pontine** horizontal **saccade generators**.

**They are functionally coupled** — the **PPRF** drives the
**abducens nucleus** for the **saccade**; the **prepositus
nucleus** **holds** the **gaze position** after the **saccade**.
But they are **anatomically distinct** — the **abducens nucleus**
and **PPRF** are **pontine**; the **perihypoglossal nuclei** are
**medullary**. Consumers must **not** conflate the two.

The Perihypoglossal Nuclei / Vestibular Nuclei and MLF Boundary
---------------------------------------------------------------
This is the **gaze-holding / VOR-and-MLF** boundary:

*   **Perihypoglossal nuclei** (this module) — the **medullary**
    oculomotor nuclei.

*   **Vestibular nuclei**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``
    and
    ``.../metencephalon/pons/cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **vestibulo-ocular reflex** relay.

*   **MLF** — the **white-matter tract** that **connects** the
    **abducens** to the **contralateral oculomotor nucleus** and
    **connects** the **vestibular nuclei** to the
    **oculomotor/trochlear nuclei**.

**They are functionally coupled** but **anatomically distinct**.
Consumers must **not** conflate the **perihypoglossal nuclei**
with the **vestibular nuclei** or with the **MLF**.

The Perihypoglossal Nuclei / Other Medullary Structures Boundary
----------------------------------------------------------------
This is the **oculomotor / non-oculomotor** boundary:

*   **Perihypoglossal nuclei** (this module) — the **medullary**
    oculomotor nuclei.

*   **Nucleus ambiguus, solitary nucleus, dorsal motor nucleus
    of the vagus, medullary pyramid, olivary body, arcuate
    nucleus, parafacial zone, paramedian reticular nucleus,
    respiratory centers** — **other medullary structures**.

**Each is a DIFFERENT STRUCTURE** with a **DIFFERENT function**.
Consumers must **not** conflate the **perihypoglossal nuclei**
with any of these.

Function in the Human Brain
---------------------------
The perihypoglossal nuclei's function is **oculomotor** —
**gaze holding** (prepositus nucleus) and **vertical gaze
integration** (intercalated nucleus) — **NOT motor conduction**,
**NOT tongue motor control**, and **NOT autonomic regulation**:

*   **Horizontal gaze holding (prepositus nucleus):** The
    **prepositus nucleus** is the **neural integrator** for
    **horizontal gaze** — it **converts** the **velocity
    command** from the **PPRF/abducens** into a **position
    command** that **holds** the **eyes** at the **new**
    **eccentric position** after a **saccade**. Without a
    functional **prepositus nucleus**, **horizontal gaze
    holding** fails — the **eyes** **drift back** to the
    **primary position** after a **saccade** (**gaze-evoked
    nystagmus**).

*   **Vertical gaze integration (intercalated nucleus):** The
    **intercalated nucleus** is involved in **vertical gaze**
    integration and **vertical vestibulo-ocular reflex**
    processing — it **participates** in **vertical gaze
    holding** and **vertical VOR** integration.

*   **Vestibulo-ocular integration:** Both the **prepositus
    nucleus** and the **intercalated nucleus** **integrate**
    **vestibular** signals with **oculomotor** commands —
    **participating** in the **horizontal and vertical VOR**.

*   **NOT motor conduction:** The **perihypoglossal nuclei**
    do **not** send motor axons to muscles.

*   **NOT tongue motor control:** The **tongue motor control**
    is the **hypoglossal nucleus** — **NOT** the
    perihypoglossal nuclei.

*   **NOT autonomic regulation:** The **perihypoglossal
    nuclei** do **not** regulate autonomic function.

**The unifying theme:** the perihypoglossal nuclei are the
**medullary oculomotor nuclei** that **surround** the
hypoglossal nucleus — they **hold gaze** (prepositus nucleus)
and **integrate vertical gaze** (intercalated nucleus), and they
**participate** in the **horizontal and vertical VOR**.

Associated Disorders
--------------------
The perihypoglossal nuclei are the **substrate** for
**well-defined clinical syndromes** — their clinical relevance is
**direct**, via **gaze-holding** and **vestibulo-ocular**
dysfunction:

*   **Gaze-evoked nystagmus (via prepositus nucleus
    dysfunction):** **Impaired** horizontal **gaze holding** —
    the **eyes** **drift back** to the **primary position**
    after a **saccade**, producing **gaze-evoked nystagmus**.
    The **prepositus nucleus** is the **neural integrator**;
    its **dysfunction** (from **stroke**, **demyelination**,
    **Wernicke encephalopathy**, **drugs** like
    **benzodiazepines**, or **cerebellar** disease) causes
    **gaze-evoked nystagmus**. This is a **cardinal**
    brainstem/cerebellar sign.

*   **Vertical gaze palsy / vertical gaze-evoked nystagmus (via
    intercalated nucleus dysfunction):** **Impaired** vertical
    **gaze holding** or **vertical saccades** — from
    **intercalated nucleus** dysfunction. This is **less well
    characterized** than horizontal gaze-holding failure.

*   **Vestibulo-ocular reflex abnormalities (via PHN
    dysfunction):** **Impaired** horizontal or vertical **VOR
    integration** — from **PHN** dysfunction. The **PHN** is
    **part of** the **VOR** integration circuitry;
    **abnormalities** can contribute to **VOR gain** or **phase**
    abnormalities.

*   **Wernicke encephalopathy (via PHN involvement):** **Wernicke
    encephalopathy** (thiamine deficiency) **typically**
    involves the **medial vestibular nuclei** and the
    **perihypoglossal nuclei** — producing **nystagmus**,
    **gaze-evoked nystagmus**, and **gaze palsy** in addition to
    the **classic triad** (ophthalmoplegia, ataxia, confusion).
    The **perihypoglossal nuclei** are a **direct substrate** of
    the **oculomotor** findings in Wernicke encephalopathy.

*   **Brainstem stroke (via PHN involvement):** **Medullary**
    **stroke** (lateral medullary syndrome, medial medullary
    syndrome) can **involve** the **perihypoglossal nuclei** or
    their **connections** — contributing to **nystagmus** and
    **gaze-holding** abnormalities. The **PHN** is **one
    contributor** to the **oculomotor** findings in brainstem
    stroke.

*   **No Named "Perihypoglossal Nuclei Syndrome":** The
    perihypoglossal nuclei are a **small nuclear complex** —
    their clinical syndromes are **named for the broader
    brainstem/cerebellar lesion** (Wernicke encephalopathy,
    brainstem stroke) or the **oculomotor sign** (gaze-evoked
    nystagmus), **not** for the nuclei themselves.

**What is NOT here:** The perihypoglossal nuclei are **not** the
substrate for **tongue weakness** (hypoglossal nucleus), **motor
weakness** (corticospinal tract — **NOT** in this container),
**sensory loss** (medial lemniscus, spinothalamic tract — **NOT**
in this container), **autonomic dysfunction** (RVLM, CVLM, NTS —
**NOT** in this container), or **respiratory rhythm** (VRG,
DRG — **NOT** in this container). Their clinical relevance is
the **gaze-holding** and **VOR** functions listed above.

Lateralization Notes
--------------------
The perihypoglossal nuclei are a **bilateral container** with
``left`` and ``right`` structural children — each a **container**
with **two leaf children**.

*   **Bilateral structural children:** ``left`` and ``right``
    are **containers** — each has **two leaf children**
    (``intercalated_nucleus`` and ``prepositus_nucleus``).
    Consumers resolve the **left** nuclei via
    ``perihypoglossal_nuclei.left.<nucleus>`` and the **right**
    nuclei via ``perihypoglossal_nuclei.right.<nucleus>``.

*   **Bilateral symmetry:** The **left** and **right**
    perihypoglossal nuclei are **structurally symmetric** —
    they are **mirror pairs** with the **same**
    cytoarchitecture, **same** projections (with **some
    contralateral** components — see below), and **same**
    functions.

*   **Partly crossed projections:** Some **PHN** projections are
    **ipsilateral** (e.g., **prepositus → ipsilateral
    abducens/vestibular nuclei**) and some are **crossed** (via
    the **MLF** and **other** commissural pathways). The **PHN**
    functions **bilaterally** in **gaze holding** — a
    **unilateral** lesion can cause **bilateral** **gaze-evoked
    nystagmus** (because the **integrator** is **bilaterally**
    distributed).

*   **NO lateralization warning:** The perihypoglossal nuclei
    have **no known functional lateralization** in humans.
    Consumers must **not** import a **lateralization warning**
    into the perihypoglossal nuclei — the **left** and **right**
    nuclei are **functionally symmetric** at the **nucleus
    level**.

*   **NO extended-amygdala / fear-output / SLEA warnings:** The
    perihypoglossal nuclei are **not** part of the amygdala,
    extended-amygdala, or SLEA continuum. They carry **no SLEA
    warning** and **no fear-output warning**.

**A consumer that assumes "left perihypoglossal nuclei = right
perihypoglossal nuclei" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**nucleus level**. The perihypoglossal nuclei are a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The perihypoglossal nuclei
    are a **bilateral container** — they do **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` containers are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../cranial_nerve_nuclei/``,
    ``.../metencephalon/pons/cranial_nerve_nuclei/``,
    ``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``,
    ``.../solitary_nucleus/``,
    ``.../medullary_pyramid/``, ``.../olivary_body/``,
    ``.../arcuate_nucleus/``, ``.../parafacial_zone/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../respiratory_center/``,
    ``.../ventral_respiratory_group/``, or any other container.
    The perihypoglossal nuclei's relationships to the hypoglossal
    nucleus, nucleus of Roller, abducens nucleus, PPRF,
    vestibular nuclei, MLF, nucleus ambiguus, solitary nucleus,
    cranial nerve nuclei, medullary pyramid, olivary body,
    arcuate nucleus, parafacial zone, paramedian reticular
    nucleus, and respiratory centers are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two container children.** The
    structural children are ``left`` and ``right`` — each a
    **container** with two leaf children. The container itself
    is **unpaired**.
*   **Two-level container structure.** ``perihypoglossal_nuclei``
    → ``left`` / ``right`` → **two leaf nuclei**. Consumers must
    **not** expect the two nuclei to be wired directly under
    ``perihypoglossal_nuclei`` — they are under ``left/`` and
    ``right/``.
*   **OCULOMOTOR, NOT motor.** The **hypoglossal nucleus** is
    **NOT** in this container. The perihypoglossal nuclei are
    **oculomotor** — **NOT** tongue motor.
*   **NOT the nucleus of Roller.** The nucleus of Roller is
    **sometimes grouped** with the PHN in the literature but is
    **NOT wired** in this tree — resolve it via the references.
*   **NOT the abducens nucleus, PPRF, vestibular nuclei, or
    MLF.** Those are **different structures** in **different
    containers** (pons for abducens/PPRF/vestibular nuclei; MLF
    is a white-matter tract).
*   **NOT the nucleus ambiguus, solitary nucleus, dorsal motor
    nucleus of the vagus, medullary pyramid, olivary body,
    arcuate nucleus, parafacial zone, paramedian reticular
    nucleus, or respiratory centers.** Each is a **different
    structure**.
*   **No ``AREA_PATHS`` hop.** The perihypoglossal nuclei are a
    **local container** — they are not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The perihypoglossal nuclei have
    no nested dual-framing module. They are a **bilateral
    container** with **two container children**, each with **two
    leaf children**.
*   **Structural parity with the right side — strict mirror.** The
    ``left`` and ``right`` containers are **structurally
    identical** — same two leaf children, same **oculomotor**
    framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import perihypoglossal_nuclei

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "perihypoglossal_nuclei"
    )

**Do not** expect the two nuclei to be wired directly under
``perihypoglossal_nuclei``. The **left** and **right** containers
are **intermediate** — the two nuclei are leaf children of those
containers. Resolve them via
``perihypoglossal_nuclei.{left,right}.<nucleus>``.

**Do not** assume the perihypoglossal nuclei are the
**hypoglossal nucleus**. They **surround** the hypoglossal
nucleus ("peri-" = "around") but are **separate structures** —
the hypoglossal nucleus is **motor** (tongue); the
perihypoglossal nuclei are **oculomotor** (gaze).

**Do not** assume the perihypoglossal nuclei are the **nucleus
of Roller**. The nucleus of Roller is **sometimes grouped** with
the PHN in the literature but is **NOT wired** in this tree.

**Do not** assume the perihypoglossal nuclei are the **abducens
nucleus**, **PPRF**, **vestibular nuclei**, or **MLF**. Those
are **different structures** in **different containers**.

**Do not** assume the perihypoglossal nuclei are the **nucleus
ambiguus**, **solitary nucleus**, **dorsal motor nucleus of the
vagus**, **medullary pyramid**, **olivary body**, **arcuate
nucleus**, **parafacial zone**, **paramedian reticular
nucleus**, or **respiratory centers**. Each is a **different
structure**.

Iterating the perihypoglossal nuclei's structural children
(recommended consumer pattern)::

    PERIHYPOGLOSSAL_NUCLEI_CHILDREN = ("left", "right")
    # Each child is a CONTAINER with two leaf nuclei.

Iterating the two nuclei per side (recommended consumer pattern)::

    PERIHYPOGLOSSAL_NUCLEI_LEAVES = (
        "intercalated_nucleus",
        "prepositus_nucleus",
    )
    # Each is a leaf child of the left/ and right/ containers.

Reaching the left and right perihypoglossal nuclei containers
(recommended consumer pattern)::

    # The left and right containers are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right
    #
    # Each is a CONTAINER with two leaf nuclei.

Reaching the two nuclei (recommended consumer pattern)::

    # The two nuclei under the left container are:
    #
    #   ...perihypoglossal_nuclei.left.intercalated_nucleus
    #   ...perihypoglossal_nuclei.left.prepositus_nucleus
    #
    # The two nuclei under the right container are the mirror.

Reaching the hypoglossal nucleus (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The hypoglossal nucleus is a MOTOR nucleus, NOT part of the
    # perihypoglossal nuclei:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.hypoglossal_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.hypoglossal_nucleus
    #
    # The perihypoglossal nuclei SURROUND the hypoglossal nucleus
    # ("peri-" = "around") but are SEPARATE structures with
    # DIFFERENT functions — the hypoglossal nucleus is motor
    # (tongue); the perihypoglossal nuclei are oculomotor (gaze).

Reaching the abducens nucleus and PPRF (recommended consumer
pattern — NOTE the DIFFERENT containers)::

    # The abducens nucleus and PPRF are PONTINE structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.abducens_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.paramedian_pontine_reticular_formation
    #
    # They are functionally coupled with the prepositus nucleus
    # (PPRF drives the saccade; prepositus holds gaze) but are
    # anatomically distinct — the abducens nucleus and PPRF are
    # pontine; the perihypoglossal nuclei are medullary.

Reaching the vestibular nuclei (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The vestibular nuclei are PONTOMEDULLARY structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei.vestibular_nuclei
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.vestibulocochlear_nuclei.vestibular_nuclei
    #
    # They are functionally coupled with the perihypoglossal
    # nuclei in the VOR — but they are DIFFERENT structures.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        for nucleus in PERIHYPOGLOSSAL_NUCLEI_LEAVES:
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"perihypoglossal_nuclei.{side}.{nucleus}"
            )
            # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Perihypoglossal nuclei; intercalated nucleus; prepositus
    nucleus; oculomotor system.)
*   **Prepositus nucleus — neural integrator:** Cannon, S.C.,
    Robinson, D.A. (1987). "Loss of the neural integrator of
    the oculomotor system from brain stem lesions in monkey."
    *Journal of Neurophysiology* 57:1383–1409. (Prepositus
    nucleus; neural integrator; horizontal gaze holding.)
*   **Prepositus nucleus — anatomy and connections:** McCrea,
    R.A., Baker, R. (1985). "Anatomical connections of the
    nucleus prepositus of the cat." *Journal of Comparative
    Neurology* 237:377–407. (Prepositus nucleus; connections
    to abducens, vestibular nuclei, and cerebellum.)
*   **Prepositus nucleus — vertical and horizontal gaze:** Baker,
    R., et al. (1975). "Postsynaptic potentials in abducens
    motoneurons induced by vestibular stimulation." *Brain
    Research* 94:467–488. (Prepositus nucleus; VOR; gaze
    holding.)
*   **Intercalated nucleus — oculomotor functions:** Langer,
    T., et al. (1986). "The nucleus intercalatus and the
    nucleus prepositus hypoglossi: their involvement in
    vertical and horizontal eye movements." *Experimental
    Brain Research* 64:325–334. (Intercalated nucleus;
    vertical gaze; vertical VOR.)
*   **Perihypoglossal nuclei — overview:** Leigh, R.J., Zee,
    D.S. (2015). *The Neurology of Eye Movements*, 5th ed.
    (Perihypoglossal nuclei; intercalated nucleus; prepositus
    nucleus; neural integrator; gaze-evoked nystagmus.)
*   **Gaze-evoked nystagmus — clinical:** Leigh, R.J., Zee,
    D.S. (2015). *The Neurology of Eye Movements*, 5th ed.
    (Gaze-evoked nystagmus; neural integrator; prepositus
    nucleus.)
*   **Wernicke encephalopathy — oculomotor findings:** Victor,
    M., et al. (1989). *The Wernicke-Korsakoff Syndrome and
    Related Neurologic Disorders Due to Alcoholism and
    Malnutrition*, 2nd ed. (Wernicke encephalopathy; medial
    vestibular nuclei; perihypoglossal nuclei; nystagmus.)
*   **Hypoglossal nucleus (contrast — motor):** Lowe, A.A.
    (1980). "The neural regulation of tongue movement."
    *Progress in Neurobiology* 14:273–349. (Hypoglossal
    nucleus; tongue motor — DIFFERENT from the perihypoglossal
    nuclei.)
*   **Abducens nucleus and PPRF (contrast — pontine horizontal
    gaze):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of
    Eye Movements*, 5th ed. (Abducens nucleus; PPRF; horizontal
    saccades — DIFFERENT from the perihypoglossal nuclei.)
*   **Vestibular nuclei (contrast — VOR relay):** Wilson, V.J.,
    Melvill Jones, G. (1979). *Mammalian Vestibular
    Physiology.* (Vestibular nuclei; VOR — DIFFERENT from the
    perihypoglossal nuclei.)
*   NeuroNames — Perihypoglossal nuclei; FMA — Perihypoglossal
    nuclei.
"""