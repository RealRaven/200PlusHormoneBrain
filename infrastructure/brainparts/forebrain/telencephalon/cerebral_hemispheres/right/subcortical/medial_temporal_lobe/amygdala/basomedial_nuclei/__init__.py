"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.amygdala.basomedial_nuclei
=======================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── medial_temporal_lobe
                    └── amygdala
                        └── basomedial_nuclei   <-- THIS MODULE

**Primary synonym:** Basomedial nuclei; basomedial nucleus of the
amygdala (BM); accessory basal nucleus (AB); nucleus basomedialis
amygdalae; "the accessory basal nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**heterogeneous grey-matter nuclear group** — the **fear-modulatory
/ extinction structure** of the amygdala, and the **third of the
three components** of the **basolateral complex (BLA)**.
**Part of:** The **amygdala** container — specifically, the
**fear-modulatory / extinction** component (with the **lateral
nucleus** as the **sensory input**, the **basolateral nuclei** as
the **fear-learning** structures, and the **central nucleus** as
the **fear-output**). The **amygdala** is the
**fear/emotion/salience** container of the medial temporal lobe.
**Structural parent:** ``.../right/subcortical/medial_temporal_lobe/amygdala/``
→ **direct child** of the amygdala container.
**Structural children:** **None.** This is a **leaf** module. The
**dorsal (magnocellular)** and **ventral (parvicellular)**
subdivisions are documented as **prose**, not as structural
children.
**Boundary status (FEAR-MODULATORY / EXTINCTION structures — the
INHIBITORY-CONTROL node):** **Boundary case — the basomedial
nuclei are the FEAR-MODULATORY / EXTINCTION structures of the
amygdala — the INHIBITORY-CONTROL node for fear extinction.** They
receive **prefrontal cortical** input (especially the
**ventromedial prefrontal cortex** — the **extinction hub**) and
**sensory input** from the **lateral nucleus**, and they
**project** to the **central nucleus** (fear-output) to
**suppress** fear responses and support **extinction**. **The
basomedial nuclei are the principal substrate** of **fear
extinction** — they **inhibit** the fear response and **compete**
with the **fear-learning** basolateral nuclei. Consumers must
**not** treat the basomedial nuclei as **fear-learning**
structures — the **basolateral nuclei** are the **fear-learning**
structures, and the **basomedial nuclei** are the
**fear-modulatory / extinction** structures.
**Boundary status (NOT the central nucleus — the central nucleus is
the FEAR-OUTPUT):** **Boundary case — the basomedial nuclei are
NOT the central nucleus; the central nucleus is the
FEAR-OUTPUT structure.** The **central nucleus** (``.../central_nucleus/``)
is the **grey-matter fear-output structure** — it **produces** the
**autonomic and behavioral** fear responses. The **basomedial
nuclei** (here) are the **fear-MODULATORY structures** — they
**project** to the central nucleus to **suppress** fear responses
and support **extinction**. **The basomedial nuclei are upstream
and modulatory relative to the central nucleus** in the fear
circuit. Consumers must **not** conflate the two — the
**basomedial nuclei** are the **fear-modulatory / extinction**
structures; the **central nucleus** is the **fear-output**
structure.
**Boundary status (NOT the basolateral nuclei — those are the
FEAR-LEARNING structures):** **Boundary case — the basomedial
nuclei are NOT the basolateral nuclei; the basolateral nuclei are
the FEAR-LEARNING structures.** The **basolateral nuclei**
(``.../basolateral_nuclei/``) are the **CS-US association** node —
they **acquire** the fear association. The **basomedial nuclei**
(here) are the **fear-modulatory / extinction** structures — they
**inhibit** the fear response and support **extinction**. **The
basomedial nuclei are downstream/modulatory relative to the
basolateral nuclei** in the fear-extinction circuit. Consumers
must **not** conflate the two — the **basolateral nuclei**
**acquire** fear; the **basomedial nuclei** **modulate /
extinguish** it.
**Boundary status (NOT the lateral nucleus — the lateral nucleus is
the SENSORY INPUT):** **Boundary case — the basomedial nuclei are
NOT the lateral nucleus; the lateral nucleus is the SENSORY INPUT
structure.** The **lateral nucleus** (``.../lateral_nucleus/``) is
the **sensory interface** — it receives **auditory, visual, and
somatosensory** input and **relays** it to the basolateral nuclei
and basomedial nuclei. The **basomedial nuclei** (here) are the
**fear-modulatory / extinction** structures — they **receive**
sensory input from the lateral nucleus and **prefrontal input**
from the cortex, and they **modulate** the fear response.
Consumers must **not** conflate the two — the **lateral nucleus**
is the **sensory input**; the **basomedial nuclei** are the
**fear-modulatory / extinction** structures.
**Boundary status (NOT the whole basolateral complex (BLA) — the
BLA spans THREE siblings):** **Boundary case — the basomedial
nuclei are NOT the whole basolateral complex (BLA); the BLA in the
broader sense spans THREE siblings.** The **basolateral complex
(BLA)** is often used in the literature to refer collectively to:
*   **Lateral nucleus** (``.../lateral_nucleus/``) — the sensory
    input.
*   **Basolateral nuclei** (``.../basolateral_nuclei/``) — the
    fear-learning structures.
*   **Basomedial nuclei** (here) — the fear-modulatory /
    extinction structures.
**The tree splits the BLA into THREE siblings** — a **deliberate
boundary choice** reflecting their **functional and anatomical
distinctness**. Consumers that need the **"BLA as a unit"** must
**union** the three leaves — the tree does **not** provide the
union as a single path. **The basomedial nuclei are the THIRD and
FINAL leaf of the BLA triad** — after this module, the BLA triad
is **fully documented** at the leaf level (with the lateral
nucleus and basolateral nuclei already written).
**Boundary status (SLEA-FREE — the basomedial nuclei are NOT
extended-amygdala components):** **Boundary case — the basomedial
nuclei are SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala)
and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **basomedial nuclei** are
**fear-modulatory / extinction structures** — they are **NOT**
extended-amygdala components, and they carry **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the
basomedial nuclei — they are **SLEA-free**.
**Boundary status (NOT the fear-output — the basomedial nuclei
MODULATE fear, they do not OUTPUT it):** **Boundary case — the
basomedial nuclei are the FEAR-MODULATORY structures, NOT the
fear-output structures.** They **inhibit** the fear response and
**support extinction**, but they do **not** directly produce the
**autonomic and behavioral** fear responses. The
**right-amygdala fear association** belongs to the **amygdala
module** — specifically the **central nucleus** (fear-output) and
the **basolateral nuclei** (fear-learning). Consumers must **not**
conflate the basomedial nuclei with the **fear-output** — the
**basomedial nuclei** are the **modulatory / extinction**
structures; the **central nucleus** is the **output** structure.
**Boundary status (NOT a single functional system — the basomedial
nuclei have TWO subdivisions):** **Boundary case — the basomedial
nuclei are a HETEROGENEOUS nuclear group with TWO subdivisions
(dorsal / magnocellular, ventral / parvicellular), not a single
uniform nucleus.** The **dorsal (magnocellular)** subdivision is
more **associative** (stronger prefrontal connections); the
**ventral (parvicellular)** subdivision is more
**autonomic**-linked (stronger brainstem projections). The two
subdivisions are **cytoarchitecturally distinct** but
**anatomically continuous** — the tree wires them as **prose**,
not as structural children. Consumers must **not** treat the
basomedial nuclei as a single uniform nucleus.
**Boundary status (NOT the medial temporal lobe, amygdala container,
or hippocampus — a leaf child of the amygdala):** **Boundary case —
the basomedial nuclei are a LEAF child of the amygdala container,
not the container itself, and not the medial temporal lobe or the
hippocampus.** The **amygdala** container contains the
**basomedial nuclei** and **nine other children**. Consumers must
**not** conflate the fear-modulatory structures with the amygdala
container, the medial temporal lobe, or the hippocampus.

Overview
--------
The basomedial nuclei are the **fear-modulatory / extinction
structures** of the amygdala — the **inhibitory-control node** for
**fear extinction**, and the **third of the three components** of
the **basolateral complex (BLA)** (with the **lateral nucleus** and
the **basolateral nuclei**). They are a **leaf** module under the
amygdala container, and they are the **principal substrate** of
**fear extinction** in the amygdala.

**The basomedial nuclei are the EXTINCTION node.** They receive
**prefrontal cortical** input (especially the **ventromedial
prefrontal cortex** — the **extinction hub**) and **sensory input**
from the **lateral nucleus**, and they **project** to the
**central nucleus** (fear-output) to **suppress** fear responses
and support **extinction**. **The basomedial nuclei are the
principal substrate** of **fear extinction** — they **inhibit**
the fear response and **compete** with the **fear-learning**
basolateral nuclei.

**The basomedial nuclei are the fear-MODULATORY structures, NOT the
fear-OUTPUT or fear-LEARNING.** The **central nucleus**
(``.../central_nucleus/``) is the **fear-output structure** — it
**produces** the **autonomic and behavioral** fear responses. The
**basolateral nuclei** (``.../basolateral_nuclei/``) are the
**fear-learning structures** — they **acquire** the fear
association. The **basomedial nuclei** (here) are the
**fear-modulatory / extinction** structures — they **inhibit** the
fear response. **The basomedial nuclei are downstream/modulatory
relative to the basolateral nuclei** and **upstream/modulatory
relative to the central nucleus**.

**The basomedial nuclei are NOT the lateral nucleus or the
basolateral nuclei.** The **lateral nucleus**
(``.../lateral_nucleus/``) is the **sensory input**; the
**basolateral nuclei** (``.../basolateral_nuclei/``) are the
**fear-learning** structures. **The three siblings** form the
**basolateral complex (BLA)** in the broader sense — the tree
**splits them into three leaves** for **functional and anatomical
granularity**. **The basomedial nuclei are the THIRD and FINAL
leaf of the BLA triad** — after this module, the BLA triad is
**fully documented** at the leaf level.

**The basomedial nuclei are SLEA-FREE.** They are **not**
extended-amygdala components, and they carry **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The basomedial nuclei have TWO subdivisions.** The **dorsal
(magnocellular)** and **ventral (parvicellular)** subdivisions are
**cytoarchitecturally distinct** but **anatomically continuous** —
they are **prose**, not structural children. The **dorsal**
subdivision is more **associative**; the **ventral** is more
**autonomic**-linked.

**The basomedial nuclei are a paired structure.** Each hemisphere
has its own basomedial nuclei, with **ipsilateral** cortical and
thalamic connections. The two sides are **bilaterally symmetric**
and **partially lateralized** — the **right** basomedial nuclei
are more involved in **unconscious/automatic** extinction, and the
**left** basomedial nuclei are more involved in
**verbal/semantic** extinction. This is **partial**, **contested**,
and documented in the **amygdala module** (not at the nucleus
level). See *Lateralization Notes*.

Subdivisions (prose, not structural children)
---------------------------------------------
The basomedial nuclei have **two cytoarchitectonic subdivisions**,
all documented as **prose**:

*   **Dorsal (magnocellular) subdivision** — the **dorsal** part,
    with **larger cells**. It is more **associative** — it has
    **stronger prefrontal** and **higher-order sensory**
    connections, and it is involved in **complex extinction
    learning** (e.g., **contextual extinction**, **cognitive
    reappraisal**).

*   **Ventral (parvicellular) subdivision** — the **ventral** part,
    with **smaller cells**. It is more **autonomic**-linked — it has
    **stronger brainstem** and **hypothalamic** connections, and it
    is involved in **autonomic extinction responses** (e.g.,
    **heart rate**, **blood pressure**).

**These subdivisions are prose, not structural children.** The tree
wires the **basomedial nuclei** as a **single leaf** under the
amygdala — the **dorsal (magnocellular)** and **ventral
(parvicellular)** subdivisions are **prose**, not structural
children. Consumers that need **subdivision-level** resolution
should consult the references, not the tree.

The Basomedial Nuclei / Basolateral Nuclei Boundary
---------------------------------------------------
This is the **fear-learning** boundary:

*   **Basomedial nuclei** (this module) — the **fear-modulatory /
    extinction** structures (inhibitory control of fear).

*   **Basolateral nuclei** (``.../basolateral_nuclei/``) — the
    **fear-learning** structures (CS-US association).

**The basomedial nuclei are downstream/modulatory relative to the
basolateral nuclei** in the fear-extinction circuit — they
**modulate** the fear response and support **extinction**.
Consumers must **not** conflate the two — the **basolateral
nuclei** **acquire** fear; the **basomedial nuclei** **modulate /
extinguish** it.

The Basomedial Nuclei / Lateral Nucleus Boundary
------------------------------------------------
This is the **sensory-input** boundary:

*   **Basomedial nuclei** (this module) — the **fear-modulatory /
    extinction** structures.

*   **Lateral nucleus** (``.../lateral_nucleus/``) — the
    **sensory-input** structures (auditory, visual, somatosensory).

**The lateral nucleus is upstream of the basomedial nuclei** in the
sensory-to-fear circuit — it **relays** sensory input to the
basomedial nuclei for **fear modulation and extinction**. Consumers
must **not** conflate the two — the **lateral nucleus** is the
**sensory input**; the **basomedial nuclei** are the
**fear-modulatory / extinction** structures.

The Basomedial Nuclei / Central Nucleus Boundary
------------------------------------------------
This is the **fear-output** boundary:

*   **Basomedial nuclei** (this module) — the **fear-modulatory /
    extinction** structures.

*   **Central nucleus** (``.../central_nucleus/``) — the
    **fear-output** structures (autonomic and behavioral fear
    responses).

**The basomedial nuclei are upstream and modulatory relative to the
central nucleus** in the fear circuit — they **project** to the
central nucleus to **suppress** fear responses. Consumers must
**not** conflate the two — the **basomedial nuclei** **modulate /
extinguish** fear; the **central nucleus** **outputs** it.

The Basomedial Nuclei / Basolateral Complex (BLA) Boundary
----------------------------------------------------------
This is the **broader-grouping** boundary:

*   **Basomedial nuclei** (this module) — one of the **three
    components** of the **basolateral complex (BLA)**.

*   **Basolateral complex (BLA)** in the **broader sense** — the
    **collective** grouping of the **lateral nucleus**, the
    **basolateral nuclei**, and the **basomedial nuclei**.

**The tree splits the BLA into THREE siblings** — a **deliberate
boundary choice** reflecting their **functional and anatomical
distinctness**. Consumers that need the **"BLA as a unit"** must
**union** the three leaves — the tree does **not** provide the
union as a single path. **The basomedial nuclei are the THIRD and
FINAL leaf of the BLA triad** — after this module, the BLA triad
is **fully documented** at the leaf level (with the lateral
nucleus and basolateral nuclei already written).

The Basomedial Nuclei / SLEA Boundary
-------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Basomedial nuclei** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The basomedial nuclei are NOT part of the SLEA continuum.** They
are **fear-modulatory / extinction structures**, and they carry
**no SLEA warning**. Consumers must **not** import the SLEA warning
into the basomedial nuclei.

Function in the Human Brain
---------------------------
The basomedial nuclei's functions are **fear modulation and
extinction** — **NOT fear-output or fear-learning**:

*   **Fear Extinction (Primary Function):** The **basomedial
    nuclei** are the **principal substrate** of **fear extinction**
    — they receive **prefrontal cortical** input (especially the
    **ventromedial prefrontal cortex** — the **extinction hub**)
    and they **project** to the **central nucleus** to **suppress**
    fear responses and support **extinction**. The **basomedial
    nuclei** are the **site** where **extinction learning**
    competes with **fear learning**.

*   **Fear Modulation (Inhibitory Control):** The **basomedial
    nuclei** are involved in **fear modulation** — they **inhibit**
    the fear response and **dampen** the **basolateral nuclei**'s
    fear-learning output. They are the **inhibitory-control** node
    of the fear circuit.

*   **Cognitive Reappraisal (with the Prefrontal Cortex):** The
    **basomedial nuclei** are involved in **cognitive reappraisal**
    — the **prefrontal cortex** (**ventromedial** and
    **dorsolateral**) projects to the basomedial nuclei to
    **modulate** the fear response via **top-down control**. This is
    the **neural substrate** of **cognitive reappraisal** of
    emotional stimuli.

*   **Anxiety Regulation (with the Prefrontal Cortex and BNST):**
    The **basomedial nuclei** are involved in **anxiety regulation**
    — they **modulate** the **BNST** (sustained anxiety hub) and
    the **central nucleus** (fear-output) to **dampen** the
    **anxiety response**. This is the **inhibitory-control** node
    of the **SLEA fear-anxiety continuum**.

*   **Contextual Extinction (with the Hippocampus):** The
    **basomedial nuclei** (with the **hippocampus**) are involved
    in **contextual extinction** — the **hippocampus** provides
    **contextual** information, and the basomedial nuclei use it to
    **modulate** the fear response based on **contextual safety**.

*   **NOT a neural processor in the classical sense.** The
    **basomedial nuclei** are a **fear-modulatory structure** —
    they **modulate** fear but do **not produce** the fear-output.
    The **processing** happens in the **basolateral nuclei**
    (learning), the **basomedial nuclei** (modulation /
    extinction), and the **central nucleus** (output).

**The unifying theme:** the basomedial nuclei are the
**fear-modulatory / extinction structures** of the amygdala — the
**inhibitory-control node** for **fear extinction**, and the
**principal substrate** of **cognitive reappraisal** and **anxiety
regulation**. They are **SLEA-free**, **fear-modulatory**, and
**NOT the fear-output or fear-learning structure** — the
**fear-output** is the **central nucleus**, the **fear-learning**
structures are the **basolateral nuclei**, and the **basomedial
nuclei** are the **modulatory / extinction** structures that
**inhibit** the fear response.

Associated Disorders
--------------------
The basomedial nuclei are involved in **fear extinction, fear
modulation, and anxiety regulation** — their clinical associations
are **fear and anxiety** disorders, especially **extinction
deficits**:

*   **PTSD (Extinction Deficit — Basomedial Dysfunction):** The
    **basomedial nuclei** are **dysfunctional** in **PTSD** —
    **impaired extinction** and **fear generalization** are
    associated with **basomedial dysfunction**. **The prefrontal
    projections** that normally **inhibit** the basolateral nuclei
    via the basomedial nuclei are **dysfunctional**.

*   **Anxiety Disorders (Extinction Deficit — Basomedial
    Dysfunction):** The **basomedial nuclei** are **dysfunctional**
    in **generalized anxiety disorder**, **specific phobias**, and
    **panic disorder** — **impaired extinction** and **fear
    generalization** contribute to **chronic anxiety**.

*   **Exposure Therapy (Basomedial Function — Extinction
    Substrate):** **Exposure therapy** for **PTSD** and **anxiety
    disorders** relies on **fear extinction** — the **basomedial
    nuclei** are the **principal substrate** of **extinction
    learning** during exposure therapy. **Enhancing basomedial
    function** (e.g., with **D-cycloserine** or **behavioral
    augmentation**) is an **active area of research**.

*   **Obsessive-Compulsive Disorder (Extinction Deficit —
    Contested):** The **basomedial nuclei** are **dysfunctional**
    in **OCD** — **impaired extinction** and **fear generalization**
    contribute to **compulsions** and **avoidance**. The evidence is
    **mixed** and **contested**.

*   **Autism Spectrum Disorder (Contested — Basomedial
    Dysfunction):** The **basomedial nuclei** are **dysfunctional**
    in **autism spectrum disorder** — contributing to
    **social-emotional** deficits and **atypical fear extinction**.
    The evidence is **contested** in its specificity.

*   **No Named "Basomedial Nuclei Syndrome":** The basomedial
    nuclei are **fear-modulatory structures** — they have **no
    named clinical syndrome** of their own. Their clinical
    relevance is the **fear-extinction** and **anxiety-regulation**
    functions they subserve, and the **PTSD** and **anxiety
    disorder** syndromes they contribute to.

**What is NOT here:** The basomedial nuclei are **not** the
substrate for **fear-output** disorders (that is the **central
nucleus** — autonomic and behavioral fear responses),
**fear-learning** disorders alone (that is the **basolateral
nuclei** — CS-US association), or **sensory processing** disorders
(that is the **lateral nucleus** — sensory input). Their clinical
footprint is **fear extinction** and **anxiety regulation** — a
**distinct category** from the **fear-output** footprint of the
central nucleus and the **fear-learning** footprint of the
basolateral nuclei.

Lateralization Notes
--------------------
This is the **right** basomedial nuclei module. The basomedial nuclei
are **bilaterally symmetric** and **partially lateralized** — and
they carry **NO warning**:

*   **Bilateral Fear-Extinction Functions:** Each hemisphere has
    its own basomedial nuclei, with **ipsilateral** cortical and
    thalamic connections. The two sides are **functionally
    symmetric** for **basic fear extinction**.

*   **Partial Lateralization (Contested — Automatic vs.
    Semantic):** The **right** basomedial nuclei are sometimes
    reported to be **more involved in unconscious/automatic**
    extinction; the **left** basomedial nuclei are sometimes
    reported to be **more involved in verbal/semantic** extinction.
    This is **partial**, **contested**, and documented in the
    **amygdala module** (not at the nucleus level). **On the right
    side**, the **unconscious/automatic** association is the
    **weaker** of the two lateralization claims — it is **not** a
    strong basis for module-level classification.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    basomedial nuclei are **SLEA-free** — they are **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning or the amygdala-lateralization warning into the
    basomedial nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the
    basomedial nuclei are FEAR-MODULATORY, not the whole
    amygdala):** The **right-amygdala fear association** belongs to
    the **amygdala module** — specifically the **central nucleus**
    (fear-output) and the **basolateral nuclei** (fear-learning).
    The basomedial nuclei are **one component** of the fear
    circuit — consumers must **not** conflate them with the **whole
    amygdala** or with the **central nucleus** or the **basolateral
    nuclei**. The **basomedial nuclei** are **fear-modulatory
    structures**, not the **whole fear circuit**. **This is true on
    the right side as well** — the right basomedial nuclei are
    **fear-modulatory structures** with **no SLEA relationship** of
    their own, and the right-amygdala fear association belongs to
    the **amygdala module** (central nucleus + basolateral nuclei),
    not to the basomedial nuclei as a whole.

**A consumer that assumes "right basomedial nuclei = left basomedial
nuclei" will be structurally correct** — the two sides are
**symmetric** and **partially lateralized** (the lateralization is
documented in the amygdala module). The basomedial nuclei are a
**strict-mirror pair with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../lateral_nucleus/``, ``.../basolateral_nuclei/``,
    ``.../central_nucleus/``, or any other container. The basomedial
    nuclei's relationships to the lateral nucleus, basolateral
    nuclei, central nucleus, and prefrontal cortex are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **dorsal
    (magnocellular)** and **ventral (parvicellular)** subdivisions
    are documented as **prose**, not as sub-modules. Consumers must
    not assume any exist as children; resolve subdivision-level
    detail through the references.
*   **FEAR-MODULATORY / EXTINCTION structures — NOT the fear-output
    or fear-learning.** The **basomedial nuclei** are the
    **inhibitory-control** node; they **modulate / extinguish** fear
    and **project** to the **central nucleus** (fear-output).
    Consumers must **not** conflate the **basomedial nuclei** with
    the **central nucleus** or the **basolateral nuclei**.
*   **NOT the basolateral nuclei — those are the FEAR-LEARNING
    structures.** The **basolateral nuclei** are upstream of the
    basomedial nuclei in the fear-extinction circuit.
*   **NOT the lateral nucleus — the lateral nucleus is the SENSORY
    INPUT.** The **lateral nucleus** is upstream of the basomedial
    nuclei in the sensory-to-fear circuit.
*   **NOT the central nucleus — the central nucleus is the
    FEAR-OUTPUT.** The **basomedial nuclei** are upstream and
    modulatory relative to the central nucleus in the fear circuit.
*   **NOT the whole basolateral complex (BLA).** The **BLA** in the
    broader sense spans **THREE siblings** — the lateral nucleus,
    the basolateral nuclei, and the basomedial nuclei. Consumers
    that need the **"BLA as a unit"** must **union** the three
    leaves.
*   **SLEA-FREE — no extended-amygdala relationship.** The basomedial
    nuclei are **not** extended-amygdala components, and they carry
    **no SLEA warning**.
*   **NOT a single functional system — TWO subdivisions.** The
    **dorsal (magnocellular)** (associative) and **ventral
    (parvicellular)** (autonomic-linked) subdivisions are **prose**,
    not structural children.
*   **No ``AREA_PATHS`` hop.** The basomedial nuclei are a local
    leaf under the amygdala, not a cross-listed leaf.
*   **No nested cross-listing.** The basomedial nuclei have no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left basomedial nuclei — strict
    mirror with NO warning.** Right and left basomedial nuclei
    modules are **structurally identical** — same leaf status, same
    **fear-modulatory** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.amygdala import basomedial_nuclei

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "medial_temporal_lobe.amygdala.basomedial_nuclei"
    )

**Do not** assume the basomedial nuclei are the **central nucleus**.
The **central nucleus** is the **fear-output** structure; the
**basomedial nuclei** are the **fear-modulatory / extinction**
structures. They are **different structures** in the fear circuit.

**Do not** assume the basomedial nuclei are the **basolateral
nuclei**. The **basolateral nuclei** are the **fear-learning**
structures; the **basomedial nuclei** are the **fear-modulatory /
extinction** structures.

**Do not** assume the basomedial nuclei are the **lateral nucleus**.
The **lateral nucleus** is the **sensory input** structure; the
**basomedial nuclei** are the **fear-modulatory / extinction**
structures.

**Do not** assume the basomedial nuclei are the **whole basolateral
complex (BLA)**. The **BLA** spans **three siblings** — the
**lateral nucleus**, the **basolateral nuclei**, and the
**basomedial nuclei**. Consumers that need the **"BLA as a unit"**
must **union** the three leaves.

**Do not** import the **SLEA warning** into the basomedial nuclei.
**The basomedial nuclei are SLEA-FREE** — they are **not** an
extended-amygdala component. **The right-side module carries the
same no-warning status** — the right basomedial nuclei are
fear-modulatory structures with **no SLEA relationship** of their
own, and the right-amygdala fear association belongs to the
**amygdala module** (central nucleus + basolateral nuclei), not to
the basomedial nuclei as a whole.

Iterating the basomedial nuclei's (empty) children (recommended
consumer pattern)::

    BASOMEDIAL_NUCLEI_CHILDREN = ()
    # The basomedial nuclei are a leaf. The dorsal (magnocellular)
    # and ventral (parvicellular) subdivisions are prose, not
    # modules.

Reconstructing the basolateral complex (BLA) as a unit (recommended
consumer pattern — the tree SPLITS it into three siblings)::

    # The basolateral complex (BLA) in the broader sense spans THREE
    # siblings. The tree does NOT provide this union as a single
    # path. THIS MODULE completes the triad:
    BASOLATERAL_COMPLEX = {
        "subcortical.medial_temporal_lobe.amygdala.lateral_nucleus": (
            # Lateral nucleus — sensory input
        ),
        "subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei": (
            # Basolateral nuclei — fear-learning
        ),
        "subcortical.medial_temporal_lobe.amygdala.basomedial_nuclei": (
            # Basomedial nuclei — fear-modulatory / extinction (THIS MODULE)
        ),
    }

Reaching the central nucleus (recommended consumer pattern — the
fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure — downstream
    # of the basomedial nuclei (via the modulatory projection):
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #
    # The basomedial nuclei MODULATE / EXTINGUISH fear; the central
    # nucleus OUTPUTS it.

Reaching the basolateral nuclei (recommended consumer pattern — the
fear-learning structures)::

    # The basolateral nuclei are the FEAR-LEARNING structures —
    # upstream of the basomedial nuclei in the fear-extinction
    # circuit:
    #
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # The basolateral nuclei ACQUIRE fear; the basomedial nuclei
    # MODULATE / EXTINGUISH it.

Reaching the lateral nucleus (recommended consumer pattern — the
sensory input)::

    # The lateral nucleus is the SENSORY INPUT structure — upstream
    # of the basomedial nuclei in the sensory-to-fear circuit:
    #
    #   subcortical.medial_temporal_lobe.amygdala.lateral_nucleus
    #
    # The lateral nucleus RELAYS sensory input; the basomedial nuclei
    # MODULATE the fear response.

Reaching the SLEA components (recommended consumer pattern — NOTE
the basomedial nuclei are NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # basomedial nuclei:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The basomedial nuclei are SLEA-FREE.

Subdivision-level detail (not wired — consult references)::

    # The basomedial nuclei's subdivisions are prose, not modules:
    #   dorsal (magnocellular)  -> associative; stronger prefrontal connections
    #   ventral (parvicellular) -> autonomic-linked; stronger brainstem connections
    #
    # Do not attempt to resolve these as sub-paths of the
    # basomedial nuclei.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        bm_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.amygdala.basomedial_nuclei"
        )
        # resolve bm_path through the memory/recall layer

References
----------
*   **Canonical basomedial nuclei anatomy:** Amaral, D.G., Price,
    J.L., Pitkänen, A., Carmichael, S.T. (1992). "Anatomical
    organization of the primate amygdaloid complex." In *The
    Amygdala* (Aggleton, J.P., ed.). (Definitive basomedial nuclei
    anatomy; dorsal / magnocellular and ventral / parvicellular
    subdivisions; "accessory basal nucleus" synonym.)
*   **Fear extinction (basomedial nuclei):** Quirk, G.J., Beer, J.S.
    (2006). "Prefrontal involvement in the regulation of emotion:
    convergence of rat and human studies." *Current Opinion in
    Neurobiology* 16:723–727. (Basomedial nuclei as the extinction
    substrate; prefrontal → basomedial projection.)
*   **Basolateral complex review:** Sah, P., Faber, E.S.L., Lopez
    de Armentia, M., Power, J. (2003). "The amygdaloid complex:
    anatomy and physiology." *Physiological Reviews* 83:803–834.
    (Definitive review of the basolateral complex — lateral,
    basolateral, and basomedial nuclei.)
*   **Basomedial and fear extinction:** Amano, T., Unal, C.T.,
    Paré, D. (2010). "Synaptic correlates of fear extinction in the
    amygdala." *Nature Neuroscience* 13:489–494. (Basomedial
    nuclei as the extinction substrate; synaptic plasticity in the
    basomedial nuclei.)
*   **Cognitive reappraisal:** Ochsner, K.N., Gross, J.J. (2005).
    "The cognitive control of emotion." *Trends in Cognitive
    Sciences* 9:242–249. (Prefrontal → basomedial projection and
    cognitive reappraisal.)
*   **PTSD and extinction deficit:** Rauch, S.L., Shin, L.M.,
    Phelps, E.A. (2006). "Neurocircuitry models of posttraumatic
    stress disorder and extinction: human neuroimaging research —
    past, present, and future." *Biological Psychiatry*
    60:376–382. (Extinction deficit in PTSD; basomedial
    dysfunction.)
*   **Exposure therapy and extinction:** Davis, M., Myers, K.M.,
    Ressler, K.J., Rothbaum, B.O. (2005). "Facilitation of
    extinction of conditioned fear: implications for
    exposure-based psychotherapy." *Biological Psychiatry*
    57:749–753. (Extinction as the substrate of exposure therapy;
    D-cycloserine augmentation.)
*   **Anxiety disorders and extinction deficit:** Milad, M.R.,
    Rauch, S.L., Pitman, R.K., Quirk, G.J. (2006). "Fear
    extinction in rats: implications for human brain imaging and
    anxiety disorders." *Biological Psychology* 73:61–71.
    (Extinction deficit in anxiety disorders.)
*   **SLEA (contrast — the basomedial nuclei are not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the basomedial nuclei.)
*   **Right amygdala lateralization (contrast — the amygdala
    module, not the basomedial nuclei specifically):** Morris,
    J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway to
    the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association
    belongs to the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning) — not to the right
    basomedial nuclei.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Basomedial nuclei in overview.)
*   NeuroNames — Basomedial nuclei (right); FMA — Basomedial nuclei
    (right member).
"""