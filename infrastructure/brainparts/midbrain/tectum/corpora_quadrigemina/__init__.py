"""
infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina
==============================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tectum
        ├── left
        │   ├── superior_colliculus
        │   └── inferior_colliculus
        ├── right
        │   ├── superior_colliculus
        │   └── inferior_colliculus
        └── corpora_quadrigemina      <-- THIS MODULE (synonym
            ├── left                     container — the OLDER name
            │   ├── superior_colliculus  for the four colliculi)
            │   └── inferior_colliculus
            └── right
                ├── superior_colliculus
                └── inferior_colliculus

**Primary synonym:** Corpora quadrigemina; **the four bodies**;
**quadrigeminal plate**; **tectal plate**; **tectum mesencephali**;
**corpora quadrigemina anterior** (superior colliculi); **corpora
quadrigemina posterior** (inferior colliculi) — the older Latin
distinction between the two pairs of bodies.
**Cytoarchitectonic designation:** **Not a Brodmann area**. **Not a
single structure.** The corpora quadrigemina are the **four colliculi
as a group** — the **superior colliculus** (left + right) and the
**inferior colliculus** (left + right). The term is the **older
collective name for the tectal plate**; **modern anatomy uses
"tectum"** or **"tectal plate"** for the same region, and
**"superior/inferior colliculus"** for the individual bodies. The
term **"corpora quadrigemina"** remains in clinical use (notably in
**"quadrigeminal cistern"** and in **descriptions of Parinaud
syndrome** as a **"quadrigeminal plate lesion"**).
**Container status:** **This module is a SYNONYM CONTAINER, not a
region container and not a leaf.** It **cross-lists** the **same
four colliculi** that are already wired under
``.../tectum/left/`` and ``.../tectum/right/`` — it **does not add
new leaves**, does **not add new functional claims**, and does **not
re-state** the four colliculi's boundaries, structure classes,
function, lateralization, or clinical associations. Those are
**inherited from** ``.../tectum/`` and from the four colliculi leaf
modules.
**Developmental designation:** **Mesencephalic** — the corpora
quadrigemina are the **same four colliculi** as the tectum, and they
are **unambiguously mesencephalic** — no contested placement, no
junction ambiguity.
**Structural parent:** ``.../tectum/`` → **direct child** of the
tectum region container. This placement makes the corpora
quadrigemina a **sub-path of the tectum** — a **synonym container**
for the **same four colliculi** the tectum already holds.
**Structural children (expected — the tree is authoritative):**
*   ``left/`` — the **left corpora quadrigemina** — a side-scoped
    container holding the **left superior colliculus** and the **left
    inferior colliculus** — **cross-listed** from
    ``.../tectum/left/superior_colliculus/`` and
    ``.../tectum/left/inferior_colliculus/``.
*   ``right/`` — the **right corpora quadrigemina** — a side-scoped
    container holding the **right superior colliculus** and the
    **right inferior colliculus** — **cross-listed** from
    ``.../tectum/right/superior_colliculus/`` and
    ``.../tectum/right/inferior_colliculus/``.
**Boundary status (SYNONYM CONTAINER — the OLDER COLLECTIVE TERM for
the four colliculi):** **Boundary case — the corpora quadrigemina is
a SYNONYM CONTAINER — the older collective term for the FOUR
COLLICULI (superior + inferior, left + right), reachable at
``.../tectum/corpora_quadrigemina/``.** It is **not a new
anatomical region** — it is the **same four colliculi** as
``.../tectum/left/`` and ``.../tectum/right/``, reachable by a
**second path**. The term **"corpora quadrigemina"** (Latin for
**"four bodies"**) predates the **tectum** nomenclature in modern
usage — but the underlying four colliculi are the **same
structures**. Consumers must **not** treat the corpora quadrigemina
as a **distinct anatomical region** — they are a **synonym path**
to the tectum's four colliculi. See *Cross-Listing Statement* and
*Older-Term Framing* below.
**Boundary status (CROSS-LISTING — the four colliculi are reachable
by TWO paths):** **Boundary case — the four colliculi are reachable
by TWO structural paths:**
*   **Modern path** — ``.../tectum/left/superior_colliculus/``,
    ``.../tectum/left/inferior_colliculus/``,
    ``.../tectum/right/superior_colliculus/``,
    ``.../tectum/right/inferior_colliculus/``
*   **Older-term path** — ``.../tectum/corpora_quadrigemina/left/
    superior_colliculus/``, and so on
**Both paths resolve to the SAME FOUR LEAVES.** **The modern path
is the structural home** — the **corpora_quadrigemina** path is the
**older-term alias**. Consumers should resolve by **one** path per
lookup — enumerating **both** paths yields **duplicates** for the
four colliculi. See *Cross-Listing Statement*.
**Boundary status (NO UNIQUE LEAVES — the corpora quadrigemina
contains the SAME four colliculi as the tectum):** **Boundary case —
the corpora quadrigemina contains the SAME FOUR COLLICULI as
``.../tectum/left/`` and ``.../tectum/right/``.** The **four leaves**
are:
*   **Left superior colliculus** — **left SC** — **sensorimotor
    integration / saccade command generator**.
*   **Right superior colliculus** — **right SC** — **sensorimotor
    integration / saccade command generator**.
*   **Left inferior colliculus** — **left IC** — **auditory relay**.
*   **Right inferior colliculus** — **right IC** — **auditory relay**.
**They are the SAME FOUR LEAVES** — the corpora quadrigemina
container does **not** add new structures. Consumers must **not**
assume the corpora quadrigemina contains **different** colliculi
from the tectum — it contains the **same four**. See *The Four
Bodies* below.
**Boundary status (INHERITANCE — structure classes, rostrocaudal
anchors, function, lateralization, and clinical associations are
INHERITED from ``tectum/`` and the four colliculi leaves):**
**Boundary case — the corpora quadrigemina container INHERITS the
substantive content of ``tectum/`` and the four colliculi leaves.**
It does **not** re-state:
*   **The two structure classes** — **SC = sensorimotor integration
    / saccade command generator**; **IC = auditory relay**; **both
    carry NO coupling warning**. These are stated in ``tectum/``
    and in the individual colliculi leaves.
*   **The rostrocaudal anchors** — **SC at the oculomotor / EW /
    mesV level**; **IC at the trochlear level**. These are stated
    in ``tectum/`` and in the individual colliculi leaves.
*   **The saccade hierarchy** — **SC (command) → PPRF / riMLF
    (premotor) → CN III/IV/VI nuclei (motor) → extraocular muscles
    (effector)**. This is stated in ``tectum/``.
*   **The auditory relay chain** — **IC (midbrain relay) → MGN
    (thalamic relay) → A1 (auditory cortex)**. This is stated in
    ``tectum/``.
*   **The boundary stacks** — SC vs. PPRF / riMLF / CN nuclei /
    LGN / pretectum; IC vs. MGN / lateral lemniscus / SC. These are
    stated in ``tectum/`` and in the individual colliculi leaves.
*   **The lateralization facts** — SC and IC are **paired
    structures with NO coupling warning**; the corpora quadrigemina
    are the **four bodies** (two per side). This is stated in
    ``tectum/``.
*   **The clinical associations** — **Parinaud syndrome** (dorsal
    midbrain / quadrigeminal plate lesions), **audiogenic seizures**
    (IC), **saccade deficits** (SC). These are stated in ``tectum/``
    and in the individual colliculi leaves.
Consumers must **not** expect the corpora quadrigemina container to
**re-state** this content — it is **inherited** from ``tectum/``
and the four colliculi leaves. The corpora quadrigemina container's
**own** contribution is the **synonym framing** and the
**cross-listing** — nothing more. See *Design Contract*.
**Boundary status (NOT A NEW REGION — the corpora quadrigemina are
the SAME four colliculi as the tectum, under a DIFFERENT NAME):**
**Boundary case — the corpora quadrigemina is NOT a new region.** It
is the **same four colliculi** as the **tectum** — the **older name
for the same structures**. The distinction in modern usage is
**nominal**: "tectum" or "tectal plate" is preferred for the
**region**; "corpora quadrigemina" is the **older collective term**
for the **four bodies**. **The two names describe the same four
colliculi** — consumers must **not** assume the corpora quadrigemina
are a **separate structure** from the tectum. See *Older-Term
Framing* below.
**Boundary status (NOT the pretectum — the pretectum is a SEPARATE
REGION, ROSTRAL to the superior colliculus):** **Boundary case —
the corpora quadrigemina is NOT the pretectum.** The **pretectum**
(``.../midbrain/pretectum/``) is a **separate region** at the
**diencephalon-midbrain junction** — **rostral** to the superior
colliculus — containing the **olivary pretectal nucleus**, the
**nucleus of the optic tract**, and the **anterior, posterior, and
medial pretectal nuclei**. **The pretectum is not part of the corpora
quadrigemina** — it is a **different region** with **different
functions** (pupillary and optokinetic). Consumers must **not**
conflate the corpora quadrigemina with the pretectum.
**Boundary status (NOT the tegmentum — the tegmentum is VENTRAL to
the cerebral aqueduct):** **Boundary case — the corpora quadrigemina
is NOT the tegmentum.** The **tegmentum**
(``.../midbrain/tegmentum/``) is the **ventral midbrain** — it
contains the **substantia nigra**, the **VTA**, the **red nucleus**,
the **PAG**, the **CN III/IV/Vm/EW nuclei**, the **riMLF**, the
**interstitial nucleus of Cajal**, and the **midbrain reticular
formation**. **The corpora quadrigemina are DORSAL to the cerebral
aqueduct** (they are the tectum); the **tegmentum is VENTRAL to the
aqueduct**. **Different midbrain compartments.** Consumers must
**not** conflate the corpora quadrigemina with the tegmentum.
**Boundary status (NOT the CN nuclei — the CN III, IV, Vm, and EW
nuclei are TEGMENTUM structures):** **Boundary case — the corpora
quadrigemina is NOT the cranial nerve nuclei.** The **oculomotor
nucleus** (CN III), the **Edinger-Westphal nucleus** (CN IIIp), the
**mesencephalic trigeminal nucleus** (CN Vm), and the **trochlear
nucleus** (CN IV) are **tegmentum** structures — they sit at the
**same rostrocaudal levels** as the colliculi but are in the
**ventral (tegmental) compartment**. **The corpora quadrigemina are
the colliculi — the dorsal (tectal) compartment.** Consumers must
**not** conflate the corpora quadrigemina with the CN nuclei.
**Boundary status (NOT the PPRF, riMLF, or interstitial nucleus of
Cajal — those are PREMOTOR SACCADE GENERATORS, DOWNSTREAM of the
superior colliculus):** **Boundary case — the corpora quadrigemina
is NOT the PPRF, the riMLF, or the interstitial nucleus of Cajal.**
Those are **premotor saccade generators** — **downstream** of the
**superior colliculus** in the saccade hierarchy. **The corpora
quadrigemina are the saccade command generator (SC) and the
auditory relay (IC)** — they are **upstream** of the PPRF/riMLF.
Consumers must **not** conflate the corpora quadrigemina with the
premotor saccade generators.
**Boundary status (NOT the lateral lemniscus or the brachia of the
colliculi — those are CONDUCTION PATHWAYS):** **Boundary case — the
corpora quadrigemina is NOT the lateral lemniscus, the brachium of
the superior colliculus, or the brachium of the inferior
colliculus.** Those are **conduction pathways** — **white matter** —
that **connect** the colliculi to their upstream and downstream
targets. **The colliculi are NUCLEI** — **grey matter**. Consumers
must **not** conflate the corpora quadrigemina with the conduction
pathways.
**Boundary status (NOT the thalamic relays — the LGN and MGN are
DIENCEPHALON):** **Boundary case — the corpora quadrigemina is NOT
the lateral geniculate body (LGN) or the medial geniculate body
(MGN).** The **LGN** and **MGN**
(``.../forebrain/diencephalon/thalamus/``) are **thalamic relays**
to **V1** and **A1** for **conscious perception**. **The corpora
quadrigemina are midbrain structures** — the **SC is a saccade
command generator** and the **IC is an auditory relay**. The **IC
projects to the MGN** (but is **not** the MGN); the **SC does
not project to the LGN**. Consumers must **not** conflate the
corpora quadrigemina with the thalamic relays.
**Boundary status (NO COUPLING WARNING — the four colliculi carry
NO coupling warning, same as every non-oscillator class):**
**Boundary case — the four colliculi under the corpora quadrigemina
carry NO coupling warning.** The **SC** is a **sensorimotor
integration** structure — **not an oscillator**; the **IC** is an
**auditory relay** — **not an oscillator**. **Neither carries a
coupling warning** — same rule as motor nuclei, premotor pools,
sensor nuclei, relay nuclei, and conduction pathways. The
**pretectum's** bilateral projection to the EW nuclei (for the
consensual pupillary light reflex) has **no analogue** in the
colliculi — the corpora quadrigemina's two sides are **independent
paired structures**. Consumers must **not** import a **coupling
warning** into the corpora quadrigemina.

Overview
--------
The corpora quadrigemina — Latin for **"the four bodies"** — are the
**older collective name for the four colliculi**: the **superior
colliculus** (left + right) and the **inferior colliculus** (left +
right). The term predates the modern **"tectum"** / **"tectal
plate"** nomenclature; **the same four colliculi** are described by
both names. This module is a **synonym container** — reachable at
``.../tectum/corpora_quadrigemina/`` — that **cross-lists** the
**same four colliculi** as ``.../tectum/left/`` and
``.../tectum/right/``. It carries **no unique leaves**, **no new
functional claims**, and **no new boundary stacks** — those are
**inherited** from ``tectum/`` and the four colliculi leaves. Its
own job is to preserve the **older-term naming** and the
**cross-listing path**.

**The corpora quadrigemina are the SAME FOUR COLLICULI as the
tectum.** The **left SC**, **right SC**, **left IC**, and **right
IC** are the four bodies — under the modern names, the **tectal
plate** or **tectum** — under the older names, the **corpora
quadrigemina**. **The two names describe the same four
structures.** Consumers must **not** treat the corpora quadrigemina
as a **new region**.

**The corpora quadrigemina are a SYNONYM CONTAINER — reachable at
``.../tectum/corpora_quadrigemina/``.** The four colliculi are
reachable by **two paths** — the **modern path** (``.../tectum/
left/`` and ``.../tectum/right/``) and the **older-term path**
(``.../tectum/corpora_quadrigemina/left/`` and ``.../tectum/
corpora_quadrigemina/right/``). **Both paths resolve to the SAME
FOUR LEAVES.** Consumers should resolve by **one** path per lookup.

**The corpora quadrigemina INHERIT the substantive content of
``tectum/`` and the four colliculi leaves.** The **structure-class
split** (SC = sensorimotor integration; IC = auditory relay; both
no coupling warning), the **rostrocaudal anchors** (SC at CN III
level; IC at CN IV level), the **saccade hierarchy**, the
**auditory relay chain**, the **boundary stacks**, the
**lateralization facts**, and the **clinical associations** are all
**stated in ``tectum/`` and in the individual colliculi leaves** —
they are **not re-stated here**. The corpora quadrigemina
container's own contribution is the **synonym framing** and the
**cross-listing**.

Cross-Listing Statement
-----------------------
**The four colliculi are cross-listed between ``.../tectum/`` and
``.../tectum/corpora_quadrigemina/``** — the same four leaves are
reachable by **two** paths:

*   **Modern path (structural home)**
    *   ``.../tectum/left/superior_colliculus/``
    *   ``.../tectum/left/inferior_colliculus/``
    *   ``.../tectum/right/superior_colliculus/``
    *   ``.../tectum/right/inferior_colliculus/``

*   **Older-term path (synonym alias)**
    *   ``.../tectum/corpora_quadrigemina/left/superior_colliculus/``
    *   ``.../tectum/corpora_quadrigemina/left/inferior_colliculus/``
    *   ``.../tectum/corpora_quadrigemina/right/superior_colliculus/``
    *   ``.../tectum/corpora_quadrigemina/right/inferior_colliculus/``

**Both paths resolve to the SAME FOUR LEAVES.** **The modern path is
the structural home** — the **corpora_quadrigemina** path is the
**older-term alias**. Consumers should resolve by **one** path per
lookup — enumerating **both** paths yields **duplicates** for the
four colliculi. This is the **same cross-listing pattern** used
elsewhere in the family (the ``cranial_nerve_nuclei/`` ↔
``tegmentum/`` cross-listing; the pretectum ↔ diencephalon
cross-listing, if present).

**The on-disk tree is authoritative.** If the tree has **both**
``.../tectum/left/`` and ``.../tectum/corpora_quadrigemina/left/``,
the four colliculi are reachable by **either** path. If the tree
has **only** ``.../tectum/corpora_quadrigemina/left/`` (no
``.../tectum/left/``), then the corpora quadrigemina path is the
**sole** path — but the four leaves are still the **same four
colliculi**. The cross-listing is **additive** — the corpora
quadrigemina path **does not replace** the modern path; it **adds**
a synonym alias.

The Four Bodies
---------------
The term **"corpora quadrigemina"** — Latin for **"four bodies"** —
refers to the **four colliculi** together:

*   **Left superior colliculus** — **left SC** — **sensorimotor
    integration / saccade command generator** — **rostral** — at
    the **oculomotor / EW / mesV level**.
*   **Right superior colliculus** — **right SC** — **sensorimotor
    integration / saccade command generator** — **rostral** — at
    the **oculomotor / EW / mesV level**.
*   **Left inferior colliculus** — **left IC** — **auditory relay**
    — **caudal** — at the **trochlear level**.
*   **Right inferior colliculus** — **right IC** — **auditory
    relay** — **caudal** — at the **trochlear level**.

**The two superior colliculi** are the **corpora quadrigemina
anterior** (in older Latin usage). **The two inferior colliculi**
are the **corpora quadrigemina posterior**. **The "four bodies"
naming** emphasizes the **quadrigeminal (four-fold)** symmetry of
the tectal plate — two superior colliculi (one per side) and two
inferior colliculi (one per side).

**These four bodies are the SAME four leaves as ``.../tectum/
left/`` and ``.../tectum/right/``** — nothing is added, nothing is
removed, nothing is changed.

Older-Term Framing
------------------
**"Corpora quadrigemina" is the older name for the tectal plate.**
Modern anatomy prefers **"tectum"**, **"tectal plate"**, or
**"superior/inferior colliculus"** — but **"corpora quadrigemina"
remains in use** in:

*   **Clinical anatomy** — **"quadrigeminal cistern"** (the
    **cisterna quadrigeminalis** — the CSF space dorsal to the
    tectum); **"quadrigeminal plate"** (synonym for the tectal
    plate).
*   **Clinical neurology** — **"quadrigeminal plate lesions"** —
    the **dorsal midbrain lesions** (pineal tumors, tectal gliomas)
    that produce **Parinaud syndrome** — are sometimes described as
    **"quadrigeminal plate syndromes"**.
*   **Historical and comparative anatomy** — the term **"corpora
    quadrigemina"** is used throughout the classical comparative
    and clinical literature.
*   **Neuroradiology** — **"quadrigeminal cistern"** is the
    standard term for the CSF space dorsal to the tectum.

**The tree preserves the older term** as a **synonym path** under
``.../tectum/corpora_quadrigemina/`` — so consumers who **think in
the older terminology** have a **structural home** for it. **The
four colliculi are the same four leaves** under both names —
**nothing new is added** — the older term is **preserved as an
alias**.

Expected Structural Children (prose — the tree is authoritative)
----------------------------------------------------------------
The corpora quadrigemina container is expected to hold **two side
containers** (``left/`` and ``right/``), each holding **the same
two colliculi** as the tectum's side containers:

*   **``left/``** — the **left corpora quadrigemina** — holds the
    **left superior colliculus** (cross-listed from
    ``.../tectum/left/superior_colliculus/``) and the **left
    inferior colliculus** (cross-listed from
    ``.../tectum/left/inferior_colliculus/``).
*   **``right/``** — the **right corpora quadrigemina** — holds the
    **right superior colliculus** (cross-listed from
    ``.../tectum/right/superior_colliculus/``) and the **right
    inferior colliculus** (cross-listed from
    ``.../tectum/right/inferior_colliculus/``).

**These are the SAME FOUR LEAVES as ``.../tectum/left/`` and
``.../tectum/right/``.** The corpora quadrigemina container does
**not** add new structures. The **substantive content** of each
colliculus leaf is the **same** under both paths — the leaves are
**identical**, the paths are **cross-listed**.

**These are the expected children — the on-disk tree is the
authoritative source.** The **leaves** impose the leaf-level
contract (boundary stacks, function, disorders, lateralization,
references) documented in the **four colliculi leaf modules**.

Aggregation Rules (the container's contract on its children)
------------------------------------------------------------
The corpora quadrigemina container **imposes the following rules**
on every leaf under it. These are **inherited** from the tectum
container and are **specialized** for the corpora quadrigemina's
role as a **synonym container**:

*   **SYNONYM-CONTAINER DISCIPLINE.** The corpora quadrigemina is the
    **older-term name** for the tectal plate. Its children are the
    **same four colliculi** as the tectum's — **no unique leaves**,
    **no new regions**. Consumers must **not** assume the corpora
    quadrigemina contains **different** colliculi from the tectum.
*   **CROSS-LISTING DISCIPLINE.** The four colliculi are
    **cross-listed** between ``.../tectum/left/`` +
    ``.../tectum/right/`` and ``.../tectum/corpora_quadrigemina/
    left/`` + ``.../tectum/corpora_quadrigemina/right/``. **Both
    paths resolve to the SAME FOUR LEAVES.** Consumers should
    resolve by **one** path per lookup — enumerating **both** paths
    yields **duplicates**.
*   **INHERITANCE FROM TECTUM.** The **structure classes** (SC =
    sensorimotor integration; IC = auditory relay; both no
    coupling warning), the **rostrocaudal anchors** (SC at CN III
    level; IC at CN IV level), the **saccade hierarchy**, the
    **auditory relay chain**, the **boundary stacks**, the
    **lateralization facts**, and the **clinical associations** are
    **inherited from ``tectum/`` and from the four colliculi
    leaves**. The corpora quadrigemina container does **not**
    re-state them.
*   **NO NEW FUNCTIONAL CLAIMS.** The corpora quadrigemina container
    makes **no new functional claims** — every function belongs to
    a **child** (SC: saccade command generation; IC: auditory
    relay), and every function is **inherited** from the
    corresponding **colliculus leaf**.
*   **OLDER-TERM FRAMING.** The corpora quadrigemina is the **older
    collective name** for the four colliculi; the modern terms are
    **tectum**, **tectal plate**, **superior/inferior colliculus**.
    The **two names describe the same four structures** — this
    container's job is to preserve the **older-term naming** as a
    **synonym path**, not to introduce a **new region**.
*   **NO COUPLING WARNING.** The four colliculi carry **NO coupling
    warning** — same rule as motor nuclei, premotor pools, sensor
    nuclei, relay nuclei, and conduction pathways. Consumers must
    **not** import a **coupling warning** into the corpora
    quadrigemina.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-lobe imports.** This module does **not** import from
    ``../forebrain/`` or ``../hindbrain/``. The corpora
    quadrigemina's relationships to the **pretectum**, the
    **tegmentum**, the **CN nuclei** (III, IV, Vm, EW), the
    **PPRF**, the **riMLF**, the **lateral lemniscus**, the
    **brachia of the colliculi**, the **thalamic relays** (LGN,
    MGN), and the **extraocular muscles** are documented as **prose
    and boundary data** in ``tectum/`` and the four colliculi leaves
    — **not re-stated here**.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **transmitter
    phenotypes** of the collicular neurons are
    ``chemicals_hormones``-layer facts — documented as **prose** in
    the four colliculi leaves, **never imported**.
*   **SYNONYM CONTAINER — not a region container.** The corpora
    quadrigemina is the **older-term name** for the four colliculi —
    **same four leaves** as the tectum, **no unique structures**.
*   **CROSS-LISTING with ``tectum/left/`` and ``tectum/right/``.** The
    four colliculi are reachable by **two paths** — the **modern
    path** (``tectum/``) and the **older-term path**
    (``tectum/corpora_quadrigemina/``). **Both paths resolve to the
    SAME FOUR LEAVES.** Consumers resolve by **one** path per
    lookup.
*   **INHERITANCE from ``tectum/``.** The **structure classes**,
    **rostrocaudal anchors**, **saccade hierarchy**, **auditory
    relay chain**, **boundary stacks**, **lateralization facts**,
    and **clinical associations** are **inherited** from
    ``tectum/`` and the four colliculi leaves — **not re-stated
    here**.
*   **NO UNIQUE LEAVES.** The four leaves under the corpora
    quadrigemina are the **same four leaves** as under the tectum.
*   **NO NEW FUNCTIONAL CLAIMS.** Every function belongs to a
    **child** (SC or IC), and every function is **inherited** from
    the corresponding **colliculus leaf**.
*   **OLDER-TERM FRAMING.** The corpora quadrigemina is the **older
    collective name**; the modern names are **tectum**,
    **tectal plate**, **superior/inferior colliculus**. The **two
    names describe the same four structures**.
*   **NO COUPLING WARNING.** The four colliculi carry **NO coupling
    warning** — same rule as every non-oscillator class.
*   **NOT a new region — the SAME four colliculi.** Consumers must
    **not** treat the corpora quadrigemina as a **distinct region**
    from the tectum.
*   **NOT the pretectum — the pretectum is a SEPARATE REGION,
    ROSTRAL to the SC.**
*   **NOT the tegmentum — the tegmentum is VENTRAL to the cerebral
    aqueduct.**
*   **NOT the CN nuclei — the CN III/IV/Vm/EW nuclei are TEGMENTUM
    structures.**
*   **NOT the PPRF/riMLF — those are PREMOTOR SACCADE GENERATORS,
    downstream of the SC.**
*   **NOT the lateral lemniscus or the brachia — those are
    CONDUCTION PATHWAYS.**
*   **NOT the thalamic relays (LGN, MGN) — those are DIENCEPHALON.**
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the tectum** (``tectum/left/`` + ``tectum/right/`` ↔
    ``tectum/corpora_quadrigemina/left/`` +
    ``tectum/corpora_quadrigemina/right/``) — not into the
    forebrain or hindbrain.
*   **No nested cross-listing.** The corpora quadrigemina is a
    **single synonym container**. It is **not** a container of
    containers — its children are the **same four colliculi** as
    the tectum's.
*   **The on-disk tree is authoritative.** If the tree has **both**
    ``tectum/left/`` + ``tectum/right/`` **and**
    ``tectum/corpora_quadrigemina/left/`` +
    ``tectum/corpora_quadrigemina/right/``, then the four colliculi
    are reachable by **either** path. If the tree has **only**
    ``tectum/corpora_quadrigemina/``, then that is the **sole**
    path — but the four leaves are still the **same four
    colliculi**.

Usage
-----
Resolve the container by path::

    from infrastructure.brainparts.midbrain.tectum import corpora_quadrigemina

Resolve a colliculus leaf by **either** path (they are equivalent)::

    # Modern path (structural home):
    from infrastructure.brainparts.midbrain.tectum.left import superior_colliculus

    # Older-term path (synonym alias — resolves to the SAME leaf):
    from infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.left import superior_colliculus

Or by fully-qualified path string::

    modern_path = "midbrain.tectum.left.superior_colliculus"
    older_term_path = (
        "midbrain.tectum.corpora_quadrigemina.left.superior_colliculus"
    )
    # Both resolve to the SAME leaf.

**Do not** assume the corpora quadrigemina is a **new region**. It is
the **older collective name** for the **four colliculi** — the
**same four leaves** as ``.../tectum/left/`` and
``.../tectum/right/``.

**Do not** assume the corpora quadrigemina contains **different**
colliculi from the tectum. It contains the **same four** — the
**left SC**, **right SC**, **left IC**, and **right IC**.

**Do not** resolve the four colliculi by **both** paths in a single
lookup. Use **one** path — the modern path
(``tectum/left/superior_colliculus``) or the older-term path
(``tectum/corpora_quadrigemina/left/superior_colliculus``).
Enumerating **both** paths yields **duplicates**.

**Do not** assume the corpora quadrigemina is the **pretectum**. The
**pretectum** is a **separate region** at the diencephalon-midbrain
junction — **rostral** to the superior colliculus. The **corpora
quadrigemina** are the **four colliculi** — the tectal plate.
**Different regions, different functions.**

**Do not** assume the corpora quadrigemina is the **tegmentum**. The
**tegmentum** is the **ventral midbrain** — **ventral to the
cerebral aqueduct**. The **corpora quadrigemina** are the **dorsal
midbrain** (the tectum) — **dorsal to the aqueduct**.

**Do not** assume the corpora quadrigemina is a **cranial nerve
nucleus**. The **CN III, IV, Vm, and EW nuclei** are **tegmentum**
structures — at the **same rostrocaudal levels** as the colliculi,
but in the **ventral (tegmental) compartment**. The **corpora
quadrigemina** are the **colliculi** — the **dorsal (tectal)
compartment**.

**Do not** assume the corpora quadrigemina is the **PPRF, riMLF, or
interstitial nucleus of Cajal**. Those are **premotor saccade
generators** — **downstream** of the **superior colliculus**.

**Do not** assume the corpora quadrigemina is the **lateral
lemniscus** or the **brachia of the colliculi**. Those are
**conduction pathways** — **white matter** — that connect the
colliculi to their upstream and downstream targets. The **colliculi
are nuclei** — **grey matter**.

**Do not** assume the corpora quadrigemina is the **LGN or MGN**.
Those are **thalamic relays** to **V1** and **A1** for **conscious
perception**. The **corpora quadrigemina** are **midbrain
structures**.

**Do not** import a **coupling warning** into the corpora
quadrigemina. The **four colliculi carry NO coupling warning** —
same rule as every non-oscillator class.

Iterating the corpora quadrigemina's children (recommended consumer
pattern — NOTE the cross-listing)::

    import pkgutil
    import infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina as cq_pkg

    CQ_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(cq_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("left", "right")
    #
    # Each side container holds the SAME two colliculi as the tectum's
    # side containers:
    # ("superior_colliculus", "inferior_colliculus")
    #
    # These are the SAME FOUR LEAVES as .../tectum/left/ and
    # .../tectum/right/. Enumerating BOTH paths yields DUPLICATES.
    # Use ONE path per lookup.

Reaching the four colliculi (recommended consumer pattern — the
SAME four leaves, by EITHER path)::

    # The four colliculi — the SAME four leaves under both paths:
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.left.superior_colliculus
    #   brainparts.midbrain.tectum.right.superior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.right.superior_colliculus
    #   brainparts.midbrain.tectum.left.inferior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.left.inferior_colliculus
    #   brainparts.midbrain.tectum.right.inferior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.right.inferior_colliculus
    #
    # Use ONE path per lookup. The leaves are IDENTICAL.

Reaching the tectum (recommended consumer pattern — the MODERN
NAME, structural home of the four colliculi)::

    # The tectum is the MODERN NAME for the same region — the
    # structural home of the four colliculi:
    #
    #   brainparts.midbrain.tectum
    #
    # The tectum and the corpora quadrigemina describe the SAME
    # FOUR COLLICULI. Different names, same structures.

Reaching the pretectum (recommended consumer pattern — a SEPARATE
region, ROSTRAL to the SC)::

    # The pretectum is a SEPARATE region at the diencephalon-midbrain
    # junction — ROSTRAL to the superior colliculus:
    #
    #   brainparts.midbrain.pretectum
    #
    # The pretectum is PUPILLARY AND OPTOKINETIC; the corpora
    # quadrigemina (the tectum) are SACCADIC AND AUDITORY. Different
    # regions, different functional systems.

Reaching the tegmentum (recommended consumer pattern — the VENTRAL
midbrain, OPPOSITE the tectum)::

    # The tegmentum is the VENTRAL MIDBRAIN — substantia nigra, VTA,
    # red nucleus, PAG, CN III/IV/Vm/EW nuclei, riMLF, interstitial
    # nucleus of Cajal, midbrain reticular formation:
    #
    #   brainparts.midbrain.tegmentum
    #
    # The corpora quadrigemina (the tectum) are DORSAL to the
    # cerebral aqueduct; the tegmentum is VENTRAL.

Reaching the CN nuclei (recommended consumer pattern — TEGMENTUM
structures at the COLLICULAR LEVELS)::

    # The CN III, EW, mesV nuclei are at the SUPERIOR COLLICULUS
    # level; the CN IV nucleus is at the INFERIOR COLLICULUS level.
    # But they are TEGMENTUM structures, NOT tectum structures:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #
    # The SC drives the CN nuclei via the tectobulbar tract — but
    # the colliculus is not the nucleus.

Reaching the PPRF and riMLF (recommended consumer pattern — PREMOTOR
SACCADE GENERATORS, DOWNSTREAM of the SC)::

    # The PPRF is the HORIZONTAL saccade generator; the riMLF and
    # interstitial nucleus of Cajal are the VERTICAL saccade
    # generators — premotor structures DOWNSTREAM of the superior
    # colliculus in the saccade hierarchy:
    #
    #   brainparts.hindbrain.metencephalon.pons.pprf
    #   brainparts.midbrain.tegmentum.left.riMLF
    #   brainparts.midbrain.tegmentum.left.interstitial_nucleus_of_cajal
    #
    # The SC decides; the PPRF/riMLF execute. Different structures.

Reaching the lateral lemniscus and the brachia (recommended consumer
pattern — CONDUCTION PATHWAYS)::

    # The lateral lemniscus is the AUDITORY conduction pathway to the
    # IC; the brachium of the SC carries retinal input to the SC;
    # the brachium of the IC carries auditory output from the IC to
    # the MGN:
    #
    #   brainparts.hindbrain.metencephalon.pons.lateral_lemniscus
    #   brainparts.midbrain.tectum.left.brachium_of_the_superior_colliculus
    #   brainparts.midbrain.tectum.left.brachium_of_the_inferior_colliculus
    #
    # The brachia and the LL are CONDUCTION PATHWAYS; the SC and IC
    # are NUCLEI.

Reaching the thalamic relays (recommended consumer pattern — LGN
and MGN are DIENCEPHALON, downstream of the IC but not the SC)::

    # The LGN is the VISUAL thalamic relay to V1 (the SC does NOT
    # project to it); the MGN is the AUDITORY thalamic relay to A1
    # (the IC DOES project to it):
    #
    #   brainparts.forebrain.diencephalon.thalamus.lateral_geniculate_body
    #   brainparts.forebrain.diencephalon.thalamus.medial_geniculate_body
    #
    # The corpora quadrigemina are MIDBRAIN structures; the LGN and
    # MGN are THALAMIC (diencephalon) relays. Different structures in
    # different functional systems.

Bilateral iteration (recommended consumer pattern — NOTE the
cross-listing and the no-coupling-warning rule)::

    for side in ("left", "right"):
        for colliculus in (
            "superior_colliculus",
            "inferior_colliculus",
        ):
            # Either path resolves to the same leaf — use ONE:
            modern_path = (
                f"midbrain.tectum.{side}.{colliculus}"
            )
            older_term_path = (
                f"midbrain.tectum.corpora_quadrigemina."
                f"{side}.{colliculus}"
            )
            # Both resolve to the SAME leaf.
            #
            # NOTE: the four colliculi carry NO coupling warning —
            # same rule as every non-oscillator class. The corpora
            # quadrigemina is the OLDER NAME for the same four
            # colliculi as the tectum.

References
----------
*   **Canonical tectum anatomy (including the corpora quadrigemina
    terminology):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (The tectum as the dorsal
    midbrain; the corpora quadrigemina as the four colliculi —
    superior + inferior, left + right; the terminology "corpora
    quadrigemina" vs. "tectum" vs. "tectal plate".)
*   **Corpora quadrigemina — historical framing:** Kahle, W.,
    Frotscher, M. (2003). *Color Atlas of Human Anatomy, Vol. 3:
    Nervous System and Sensory Organs*, 5th ed. (The corpora
    quadrigemina as the older term for the four colliculi — the
    "four bodies" of the tectal plate.)
*   **Quadrigeminal plate — clinical usage:** Parinaud, H. (1883).
    "Paralysie des mouvements associés des yeux." *Annales
    d'Oculistique* 90:1–21. (The "quadrigeminal plate syndrome" —
    Parinaud syndrome — as a dorsal midbrain syndrome involving the
    quadrigeminal plate; the term "quadrigeminal plate" remains in
    clinical use for the tectum.)
*   **Quadrigeminal cistern — neuroradiology:** Newton, T.H.,
    Potts, D.G. (eds.) (1978). *Radiology of the Skull and Brain:
    Ventricles and Cisterns*. (The cisterna quadrigeminalis — the
    quadrigeminal cistern — as the standard neuroradiological term
    for the CSF space dorsal to the tectum.)
*   **Superior colliculus (contrast — the SC leaf):** Sparks, D.L.
    (2002). "The brainstem control of saccadic eye movements."
    *Nature Reviews Neuroscience* 3:952–964. (The superior
    colliculus — the SC leaf — as the saccade command generator in
    the corpora quadrigemina.)
*   **Inferior colliculus (contrast — the IC leaf):** Ehret, G.,
    Romand, R. (eds.) (1997). *The Central Auditory System*. Oxford
    University Press. (The inferior colliculus — the IC leaf — as
    the auditory relay in the corpora quadrigemina.)
*   **SLEA (contrast — the corpora quadrigemina are not SLEA):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the corpora quadrigemina.)
*   NeuroNames — Corpora quadrigemina; Tectum; Superior colliculus;
    Inferior colliculus; FMA — Corpora quadrigemina; Tectum;
    Superior colliculus; Inferior colliculus.
"""