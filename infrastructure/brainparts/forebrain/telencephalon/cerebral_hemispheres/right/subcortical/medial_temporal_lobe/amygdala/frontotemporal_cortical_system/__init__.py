"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.amygdala.frontotemporal_cortical_system
====================================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── medial_temporal_lobe
                    └── amygdala
                        └── frontotemporal_cortical_system   <-- THIS MODULE

**Primary synonym:** Frontotemporal cortical system (of the
amygdala); amygdala-prefrontal cortical system; cortico-amygdaloid
cortical system; "the amygdala's cortical interface."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**cortical-region system** — the **grey-matter cortical regions**
(prefrontal, orbitofrontal, insular, anterior cingulate, anterior
temporal) that **send and receive** the **amygdala-cortex fibers**.
**Part of:** The **amygdala** container — specifically, the
**cortico-amygdaloid** component (with the **amygdala_cortex_pathways**
as its **fiber-pathway sibling**). The **amygdala** is the
**fear/emotion/salience** container of the medial temporal lobe.
**Structural parent:** ``.../right/subcortical/medial_temporal_lobe/amygdala/``
→ **direct child** of the amygdala container.
**Structural children:** **None.** This is a **leaf** module. The
**prefrontal**, **orbitofrontal**, **insular**, **anterior
cingulate**, and **anterior temporal** cortical subregions are
documented as **prose**, not as structural children.
**Boundary status (CORTICAL REGIONS — NOT the fiber pathways they
use):** **Boundary case — the frontotemporal_cortical_system is the
CORTICAL REGIONS (grey matter), NOT the FIBER PATHWAYS (white
matter) that connect them to the amygdala.** The
**frontotemporal_cortical_system** (here) is the **anatomical
system of cortical regions** (prefrontal, orbitofrontal, insular,
anterior cingulate, anterior temporal) — the **grey-matter cortical
regions**. The **amygdala_cortex_pathways**
(``.../amygdala_cortex_pathways/``) are the **white-matter fiber
connections** — the **conduction infrastructure**. **They are
DIFFERENT STRUCTURES**: the **cortical system** is the **grey-matter
cortical regions**; the **pathways** are the **white-matter
fibers**. Consumers must **not** conflate the two — the
**frontotemporal_cortical_system** is the **cortical regions**; the
**amygdala_cortex_pathways** are the **fibers**.
**Boundary status (NOT the whole frontal or temporal cortex — only
the AMYGDALA-FACING cortical regions):** **Boundary case — the
frontotemporal_cortical_system is NOT the whole frontal or temporal
cortex — it is only the AMYGDALA-FACING cortical regions.** The
**whole frontal cortex** (``cortex/frontal/``) and the **whole
temporal cortex** (``cortex/temporal/``) are **much larger**
structures — they include the **primary motor cortex**, the
**primary auditory cortex**, the **visual association cortex**, the
**language areas** (Broca's, Wernicke's), and the **whole
neocortical temporal lobe**. The **frontotemporal_cortical_system**
(here) is the **subset** of frontal and temporal cortical regions
that **reciprocally connect with the amygdala** — the **prefrontal**
(dorsolateral, ventrolateral, ventromedial, orbitofrontal), the
**anterior cingulate**, the **insular**, and the **anterior
temporal** cortices. Consumers must **not** conflate the
**amygdala-facing cortical system** with the **whole frontal or
temporal cortex** — it is a **specific subset** of cortical regions
defined by their **amygdala connectivity**.
**Boundary status (NOT the central nucleus — the central nucleus is
the FEAR-OUTPUT):** **Boundary case — the
frontotemporal_cortical_system is NOT the central nucleus; the
central nucleus is the FEAR-OUTPUT structure.** The **central
nucleus** (``.../central_nucleus/``) is the **grey-matter
fear-output structure** — it **produces** the **autonomic and
behavioral** fear responses. The **frontotemporal_cortical_system**
(here) is the **cortical modulatory system** — it **sends and
receives** the **amygdala-cortex fibers** that **regulate** the
fear response. **The cortical system is upstream and modulatory
relative to the central nucleus** in the fear circuit — the
**prefrontal** and **cingulate** cortices **project** to the
amygdala (including the central nucleus) to **suppress** fear
responses and support **extinction**. Consumers must **not**
conflate the two — the **frontotemporal_cortical_system** is the
**cortical modulatory system**; the **central nucleus** is the
**fear-output** structure.
**Boundary status (NOT the basolateral nuclei — those are the
FEAR-LEARNING structures):** **Boundary case — the
frontotemporal_cortical_system is NOT the basolateral nuclei; the
basolateral nuclei are the FEAR-LEARNING structures.** The
**basolateral nuclei** (``.../basolateral_nuclei/``) are the
**CS-US association** node — they **acquire** the fear
association. The **frontotemporal_cortical_system** (here) is the
**cortical modulatory system** — it **regulates** the fear
response via the **amygdala-cortex pathways**. **The cortical
system is upstream and modulatory relative to the basolateral
nuclei** — the **prefrontal** cortex **projects** to the
basolateral nuclei to **modulate** fear learning. Consumers must
**not** conflate the two — the **basolateral nuclei** are the
**fear-learning** structures; the **frontotemporal_cortical_system**
is the **cortical modulatory system**.
**Boundary status (NOT the basomedial nuclei — those are the
FEAR-MODULATORY / EXTINCTION structures):** **Boundary case — the
frontotemporal_cortical_system is NOT the basomedial nuclei; the
basomedial nuclei are the FEAR-MODULATORY / EXTINCTION structures.**
The **basomedial nuclei** (``.../basomedial_nuclei/``) are the
**fear-modulatory** structures — they **inhibit** the fear response
and support **extinction**. The **frontotemporal_cortical_system**
(here) is the **cortical modulatory system** — the **prefrontal**
cortex **projects** to the basomedial nuclei to **support
extinction**. **The cortical system is upstream of the basomedial
nuclei** — the **ventromedial prefrontal cortex** is the
**extinction hub** that **drives** the basomedial nuclei. Consumers
must **not** conflate the two — the **basomedial nuclei** are the
**fear-modulatory / extinction** structures; the
**frontotemporal_cortical_system** is the **cortical modulatory
system**.
**Boundary status (NOT the lateral nucleus — the lateral nucleus is
the SENSORY INPUT):** **Boundary case — the
frontotemporal_cortical_system is NOT the lateral nucleus; the
lateral nucleus is the SENSORY INPUT structure.** The **lateral
nucleus** (``.../lateral_nucleus/``) is the **sensory interface** —
it receives **auditory, visual, and somatosensory** input and
**relays** it to the basolateral nuclei. The
**frontotemporal_cortical_system** (here) is the **cortical
modulatory system** — it **regulates** the fear response via the
**amygdala-cortex pathways**. Consumers must **not** conflate the
two — the **lateral nucleus** is the **sensory input**; the
**frontotemporal_cortical_system** is the **cortical modulatory
system**.
**Boundary status (NOT the amygdala_cortex_pathways — those are the
FIBER PATHWAYS):** **Boundary case — the frontotemporal_cortical_system
is NOT the amygdala_cortex_pathways; the amygdala_cortex_pathways
are the FIBER PATHWAYS.** The **amygdala_cortex_pathways**
(``.../amygdala_cortex_pathways/``) are the **white-matter fiber
connections** — the **conduction infrastructure**. The
**frontotemporal_cortical_system** (here) is the **grey-matter
cortical regions** — the **cortical modulatory system**. **They are
DIFFERENT STRUCTURES**: the **cortical system** is the **grey-matter
cortical regions**; the **pathways** are the **white-matter
fibers**. Consumers must **not** conflate the two — the
**frontotemporal_cortical_system** is the **cortical regions**; the
**amygdala_cortex_pathways** are the **fibers**.
**Boundary status (SLEA-FREE — the cortical system is NOT an
extended-amygdala component):** **Boundary case — the
frontotemporal_cortical_system is SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component** in
the amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The
**frontotemporal_cortical_system** is a **cortical modulatory
system** — it is **NOT** an extended-amygdala component, and it
carries **NO SLEA warning**. Consumers must **not** import the SLEA
warning into the frontotemporal_cortical_system — it is
**SLEA-free**.
**Boundary status (NOT the fear-output — the cortical system
MODULATES fear, it does not OUTPUT it):** **Boundary case — the
frontotemporal_cortical_system is the CORTICAL MODULATORY system,
NOT the fear-output structure.** It **regulates** the fear response
via the **amygdala-cortex pathways**, but it does **not** directly
produce the **autonomic and behavioral** fear responses. The
**right-amygdala fear association** belongs to the **amygdala
module** — specifically the **central nucleus** (fear-output) and
the **basolateral nuclei** (fear-learning). Consumers must **not**
conflate the cortical system with the **fear-output** — the
**cortical system** is the **modulatory** system; the **central
nucleus** is the **output** structure.
**Boundary status (NOT a single functional system — MULTIPLE
cortical regions with DIFFERENT functions):** **Boundary case — the
frontotemporal_cortical_system is a HETEROGENEOUS cortical system
with MULTIPLE cortical regions and MULTIPLE functions, not a single
uniform system.** The system includes:
*   **Prefrontal cortex** (dorsolateral, ventrolateral,
    ventromedial, orbitofrontal) — the **top-down emotional
    regulation** and **cognitive reappraisal** interface.
*   **Anterior cingulate cortex** — the **emotional conflict and
    salience** interface.
*   **Insular cortex** — the **interoceptive and emotional
    awareness** interface.
*   **Anterior temporal cortex** — the **social cognition and
    sensory association** interface.
**Each cortical region is functionally distinct** — the tree wires
them as **prose** under the frontotemporal_cortical_system leaf, not
as structural children. Consumers must **not** treat the system as a
single uniform cortical region — it is a **distributed cortical
system** defined by its **amygdala connectivity**.
**Boundary status (NOT the medial temporal lobe, amygdala container,
or hippocampus — a leaf child of the amygdala):** **Boundary case —
the frontotemporal_cortical_system is a LEAF child of the amygdala
container, not the container itself, and not the medial temporal
lobe or the hippocampus.** The **amygdala** container contains the
**frontotemporal_cortical_system** and **nine other children**.
Consumers must **not** conflate the cortical system with the
amygdala container, the medial temporal lobe, or the hippocampus.

Overview
--------
The frontotemporal cortical system is the **cortical-region
sibling** of the **amygdala_cortex_pathways** — the **grey-matter
cortical regions** (prefrontal, orbitofrontal, insular, anterior
cingulate, anterior temporal) that **send and receive** the
**amygdala-cortex fibers**. It is a **leaf** module under the
amygdala container, and it is the **cortical modulatory system**
that supports **top-down emotional regulation** (cortex → amygdala)
and **emotional salience modulation** (amygdala → cortex).

**The frontotemporal_cortical_system is the CORTICAL REGIONS, NOT
the fiber pathways.** The **amygdala_cortex_pathways**
(``.../amygdala_cortex_pathways/``) are the **white-matter fiber
connections** — the **conduction infrastructure**. The
**frontotemporal_cortical_system** (here) is the **grey-matter
cortical regions** — the **cortical modulatory system**. **They are
DIFFERENT STRUCTURES** — the **cortical system** is the **cortical
regions**; the **pathways** are the **fibers**.

**The frontotemporal_cortical_system is NOT the whole frontal or
temporal cortex.** It is only the **AMYGDALA-FACING cortical
regions** — the subset of frontal and temporal cortical regions that
**reciprocally connect with the amygdala**. The **whole frontal
cortex** (``cortex/frontal/``) and the **whole temporal cortex**
(``cortex/temporal/``) are **much larger** structures — they include
the **primary motor cortex**, the **primary auditory cortex**, the
**language areas**, and the **whole neocortical temporal lobe**. The
**frontotemporal_cortical_system** is a **specific subset** defined
by its **amygdala connectivity**.

**The frontotemporal_cortical_system is SLEA-FREE.** It is **not**
an extended-amygdala component, and it carries **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The frontotemporal_cortical_system is MODULATORY, NOT the
fear-output.** The **fear-output** structure is the **central
nucleus**; the **fear-learning** structures are the **basolateral
nuclei**; the **fear-modulatory / extinction** structures are the
**basomedial nuclei**. The **cortical system** is the **cortical
modulatory system** — it **regulates** the fear response via the
**amygdala-cortex pathways** but does **not** directly produce the
**fear-output**.

**The frontotemporal_cortical_system is a paired structure.** Each
hemisphere has its own frontotemporal cortical system, with
**ipsilateral** and **bilateral** connections to the amygdala. The
two sides are **bilaterally symmetric** and **partially lateralized**
— the **right** frontotemporal cortical system is more involved in
**unconscious/automatic** emotional processing, and the **left**
frontotemporal cortical system is more involved in
**verbal/semantic** emotional processing. This is **partial**,
**contested**, and documented in the **amygdala module** (not at the
cortical-system level). See *Lateralization Notes*.

Cortical Region Composition (prose, not structural children)
------------------------------------------------------------
The frontotemporal_cortical_system is a **distributed cortical
system** — documented as **prose**, not as structural children:

*   **Prefrontal cortex** (dorsolateral, ventrolateral,
    ventromedial, orbitofrontal) — the **top-down emotional
    regulation** and **cognitive reappraisal** interface. The
    **ventromedial prefrontal cortex** is the **extinction hub** —
    it **projects** to the **basomedial nuclei** and the
    **basolateral nuclei** to **suppress** fear responses. The
    **orbitofrontal cortex** is the **reward and emotional
    valuation** interface.

*   **Anterior cingulate cortex** (dorsal, ventral, subgenual) —
    the **emotional conflict and salience** interface. The
    **subgenual anterior cingulate** is involved in **emotional
    regulation** and **depression**; the **dorsal anterior
    cingulate** is involved in **emotional conflict** and
    **salience**.

*   **Insular cortex** (anterior, posterior) — the **interoceptive
    and emotional awareness** interface. The **anterior insula** is
    involved in **emotional awareness**, **empathy**, and
    **interoception**; the **posterior insula** is involved in
    **sensory integration**.

*   **Anterior temporal cortex** — the **social cognition and
    sensory association** interface. The **anterior temporal lobe**
    is involved in **semantic memory**, **social cognition**, and
    **emotional face processing**.

**These cortical regions are prose, not structural children.** The
tree wires the **frontotemporal_cortical_system** as a **single
leaf** under the amygdala — the **prefrontal**, **orbitofrontal**,
**insular**, **anterior cingulate**, and **anterior temporal**
cortical regions are **prose**, not structural children. Consumers
that need **cortical-region-level** resolution should consult the
references, not the tree.

The Frontotemporal Cortical System / Amygdala_Cortex_Pathways Boundary
---------------------------------------------------------------------
This is the **most consequential sibling** boundary — **cortical
regions vs. fiber pathways**:

*   **Frontotemporal_cortical_system** (this module) — the
    **grey-matter cortical regions** (prefrontal, orbitofrontal,
    insular, anterior cingulate, anterior temporal).

*   **Amygdala_cortex_pathways** (``.../amygdala_cortex_pathways/``)
    — the **white-matter fiber pathways** (uncinate fasciculus,
    external capsule fibers, extreme capsule fibers, other
    cortico-amygdaloid tracts).

**They are siblings under the amygdala.** The **cortical system** is
the **cortical regions**; the **pathways** are the **fibers**.
**Consumers must not conflate the two** — the
**frontotemporal_cortical_system** is the **cortical regions**; the
**amygdala_cortex_pathways** are the **fibers**.

The Frontotemporal Cortical System / Central Nucleus Boundary
-------------------------------------------------------------
This is the **fear-output** boundary:

*   **Frontotemporal_cortical_system** (this module) — the
    **cortical modulatory system**.

*   **Central nucleus** (``.../central_nucleus/``) — the
    **fear-output** structure.

**The cortical system is upstream and modulatory relative to the
central nucleus** in the fear circuit — the **prefrontal** and
**cingulate** cortices **project** to the amygdala (including the
central nucleus) to **suppress** fear responses. Consumers must
**not** conflate the two — the **cortical system** **modulates /
extinguishes** fear; the **central nucleus** **outputs** it.

The Frontotemporal Cortical System / Basolateral Nuclei Boundary
----------------------------------------------------------------
This is the **fear-learning** boundary:

*   **Frontotemporal_cortical_system** (this module) — the
    **cortical modulatory system**.

*   **Basolateral nuclei** (``.../basolateral_nuclei/``) — the
    **fear-learning** structures (CS-US association).

**The cortical system is upstream and modulatory relative to the
basolateral nuclei** — the **prefrontal** cortex **projects** to
the basolateral nuclei to **modulate** fear learning. Consumers
must **not** conflate the two — the **basolateral nuclei** **learn**
fear; the **cortical system** **modulates** it.

The Frontotemporal Cortical System / Basomedial Nuclei Boundary
---------------------------------------------------------------
This is the **fear-modulatory / extinction** boundary:

*   **Frontotemporal_cortical_system** (this module) — the
    **cortical modulatory system**.

*   **Basomedial nuclei** (``.../basomedial_nuclei/``) — the
    **fear-modulatory / extinction** structures.

**The cortical system is upstream of the basomedial nuclei** — the
**ventromedial prefrontal cortex** is the **extinction hub** that
**drives** the basomedial nuclei to **suppress** fear responses.
Consumers must **not** conflate the two — the **basomedial nuclei**
are the **fear-modulatory / extinction** structures; the
**frontotemporal_cortical_system** is the **cortical modulatory
system**.

The Frontotemporal Cortical System / Lateral Nucleus Boundary
-------------------------------------------------------------
This is the **sensory-input** boundary:

*   **Frontotemporal_cortical_system** (this module) — the
    **cortical modulatory system**.

*   **Lateral nucleus** (``.../lateral_nucleus/``) — the
    **sensory-input** structures (auditory, visual, somatosensory).

**The cortical system and the lateral nucleus are DIFFERENT
structures** — the lateral nucleus is the **sensory input**; the
cortical system is the **cortical modulatory system**. Consumers
must **not** conflate the two.

The Frontotemporal Cortical System / Whole Frontal and Temporal Cortex Boundary
------------------------------------------------------------------------------
This is the **cortical-subset** boundary:

*   **Frontotemporal_cortical_system** (this module) — the
    **AMYGDALA-FACING subset** of frontal and temporal cortical
    regions.

*   **Whole frontal cortex** (``cortex/frontal/``) and **whole
    temporal cortex** (``cortex/temporal/``) — the **much larger**
    neocortical structures, including the **primary motor cortex**,
    the **primary auditory cortex**, the **language areas**, and the
    **whole neocortical temporal lobe**.

**The frontotemporal_cortical_system is a SUBSET of the whole
frontal and temporal cortex** — it is defined by its **amygdala
connectivity**, not by its **neocortical location**. Consumers must
**not** conflate the **amygdala-facing cortical system** with the
**whole frontal or temporal cortex**.

The Frontotemporal Cortical System / SLEA Boundary
--------------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Frontotemporal_cortical_system** (this module) — **SLEA-FREE**.
    No extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The frontotemporal_cortical_system is NOT part of the SLEA
continuum.** It is a **cortical modulatory system**, and it carries
**no SLEA warning**. Consumers must **not** import the SLEA warning
into the frontotemporal_cortical_system.

Function in the Human Brain
---------------------------
The frontotemporal_cortical_system's functions are **top-down
emotional regulation** and **emotional salience modulation** — **NOT
fear-output**:

*   **Top-Down Emotional Regulation (Prefrontal Cortex):** The
    **prefrontal cortex** (especially **ventrolateral** and
    **ventromedial**) **projects** to the **amygdala** (including
    the **basolateral nuclei** and the **central nucleus**) to
    **inhibit** fear responses and support **extinction** — the
    **top-down regulation** of emotion. This is the **neural
    substrate** of **cognitive reappraisal** and **emotion
    regulation**.

*   **Emotional Salience Modulation (Anterior Cingulate and
    Insula):** The **anterior cingulate cortex** and the **insular
    cortex** **modulate** the **salience** of emotional stimuli —
    they **enhance** the amygdala's response to **behaviorally
    relevant** stimuli and **dampen** the response to **irrelevant**
    stimuli. This is the **emotional salience modulation** function.

*   **Fear Extinction (Ventromedial Prefrontal Cortex):** The
    **ventromedial prefrontal cortex** is the **extinction hub** —
    it **projects** to the **basomedial nuclei** and the
    **basolateral nuclei** to **suppress** fear responses and
    support **extinction**. The **cortical system** is the
    **cortical substrate** of **extinction learning**.

*   **Social Cognition (Anterior Temporal Cortex):** The **anterior
    temporal cortex** is involved in **social cognition** —
    **emotion recognition**, **theory of mind**, and **social
    decision-making** — via its **reciprocal** connections with the
    amygdala.

*   **Interoception (Insular Cortex):** The **insular cortex** is
    involved in **interoception** — the **perception of internal
    bodily states** — and **emotional awareness**. It is the
    **cortical substrate** of **emotional feeling states**.

*   **NOT a neural processor in the classical sense.** The
    **frontotemporal_cortical_system** is a **cortical modulatory
    system** — it **regulates** the fear response but does **not
    produce** the fear-output. The **processing** happens in the
    **amygdala** (fear-output, fear-learning) and the **cortex**
    (emotional regulation, salience processing).

**The unifying theme:** the frontotemporal_cortical_system is the
**cortical modulatory system** of the **amygdala-cortex interface**
— the **top-down emotional regulation** and **emotional salience
modulation** cortical regions. It is **SLEA-free**, **modulatory**,
and **NOT the fear-output structure** — the **fear-output** is the
**central nucleus**, and the **cortical system** is the **cortical
regions** that **modulate** it.

Associated Disorders
--------------------
The frontotemporal_cortical_system has **no named clinical
syndrome** — its clinical associations are **indirect**, via the
cortical regions it comprises:

*   **PTSD (Impaired Top-Down Regulation — via the Prefrontal
    Cortex):** The **prefrontal cortex** (especially the
    **ventromedial prefrontal cortex**) is **dysfunctional** in
    **PTSD** — **reduced prefrontal inhibition** of the **amygdala**
    contributes to **fear generalization** and **impaired
    extinction**. The **cortical system** is the **cortical
    substrate** of this **top-down regulation** — its dysfunction
    is **indirect**, via the **prefrontal cortex** and the
    **amygdala** structures it connects.

*   **Depression (Reduced Prefrontal Control — via the Prefrontal
    Cortex):** The **prefrontal cortex** (especially the
    **subgenual anterior cingulate** and the **ventromedial
    prefrontal cortex**) is **dysfunctional** in **major depressive
    disorder** — **reduced prefrontal control** of the **amygdala**
    is associated with **negative emotional bias** and **impaired
    emotion regulation**. The **cortical system** is the **cortical
    substrate** of this **prefrontal control**.

*   **Anxiety Disorders (Prefrontal-Cingulate Dysregulation):** The
    **prefrontal cortex** and the **anterior cingulate cortex** are
    **dysfunctional** in **generalized anxiety disorder**, **social
    anxiety disorder**, and **panic disorder** — **reduced top-down
    regulation** of the **amygdala** contributes to **sustained
    anxiety** and **fear generalization**.

*   **Autism Spectrum Disorder (Atypical Fronto-Temporal
    Connectivity):** The **frontotemporal cortical system**
    (especially the **anterior temporal cortex** and the
    **orbitofrontal cortex**) shows **atypical connectivity** in
    **autism spectrum disorder** — contributing to
    **social-emotional** deficits and **atypical emotion
    processing**. The **cortico-amygdaloid** connectivity is **well
    documented** but **contested** in its specificity.

*   **Psychopathy (Reduced Amygdala-Prefrontal Coupling):** The
    **ventromedial prefrontal cortex** shows **reduced coupling**
    with the **amygdala** in **psychopathy** — contributing to
    **impaired fear conditioning**, **reduced empathy**, and
    **impaired moral judgment**.

*   **No Named "Frontotemporal Cortical System Syndrome":** The
    frontotemporal_cortical_system is a **cortical-region system**,
    not a **single structure** — it has **no named clinical
    syndrome**. Its clinical relevance is **indirect**, via the
    **cortical regions** and the **amygdala** structures they
    connect.

**What is NOT here:** The frontotemporal_cortical_system is **not**
the substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **fear conditioning** (central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), or **Alzheimer's disease** (hippocampus,
nucleus basalis). Its clinical relevance is **indirect**, via the
**top-down emotional regulation** and **emotional salience
modulation** pathways it subserves. **No named frontotemporal
cortical system syndrome exists.**

Lateralization Notes
--------------------
This is the **right** frontotemporal_cortical_system module. The
frontotemporal_cortical_system is **bilaterally symmetric** and
**partially lateralized** — and it carries **NO warning**:

*   **Bilateral Cortical Modulation:** Each hemisphere has its own
    frontotemporal cortical system, with **ipsilateral** and
    **bilateral** connections to the amygdala. The two sides are
    **functionally symmetric** for **basic top-down regulation**.

*   **Partial Lateralization (Contested — Automatic vs.
    Semantic):** The **right** frontotemporal cortical system is
    sometimes reported to be **more involved in
    unconscious/automatic** emotional processing; the **left**
    frontotemporal cortical system is sometimes reported to be
    **more involved in verbal/semantic** emotional processing. This
    is **partial**, **contested**, and documented in the **amygdala
    module** (not at the cortical-system level). **On the right
    side**, the **unconscious/automatic** association is the
    **weaker** of the two lateralization claims — it is **not** a
    strong basis for module-level classification.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    frontotemporal_cortical_system is **SLEA-free** — it is **not**
    an extended-amygdala component. Consumers must **not** import
    the SLEA warning or the amygdala-lateralization warning into the
    frontotemporal_cortical_system.

*   **NO Amygdala-Lateralization Warning of their own (the cortical
    system is MODULATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output)
    and the **basolateral nuclei** (fear-learning). The
    frontotemporal_cortical_system is a **cortical modulatory
    system** — consumers must **not** conflate it with the **whole
    amygdala** or with the **central nucleus**. The
    **frontotemporal_cortical_system** is a **cortical modulatory
    system**, not the **whole fear circuit**. **This is true on the
    right side as well** — the right frontotemporal_cortical_system
    is a **cortical modulatory system** with **no SLEA relationship**
    of its own, and the right-amygdala fear association belongs to
    the **amygdala module** (central nucleus + basolateral nuclei),
    not to the frontotemporal_cortical_system.

**A consumer that assumes "right frontotemporal_cortical_system =
left frontotemporal_cortical_system" will be structurally correct**
— the two sides are **symmetric** and **partially lateralized** (the
lateralization is documented in the amygdala module). The
frontotemporal_cortical_system is a **strict-mirror pair with NO
warning** — **no SLEA warning**, **no amygdala-lateralization
warning of their own**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../amygdala_cortex_pathways/``, ``.../central_nucleus/``,
    ``cortex/frontal/``, ``cortex/temporal/``, or any other
    container. The frontotemporal_cortical_system's relationships to
    the amygdala_cortex_pathways, central nucleus, basolateral
    nuclei, basomedial nuclei, lateral nucleus, and the whole
    frontal / temporal cortex are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **prefrontal**,
    **orbitofrontal**, **insular**, **anterior cingulate**, and
    **anterior temporal** cortical regions are documented as
    **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve cortical-region-level detail through
    the references.
*   **CORTICAL REGIONS — NOT the fiber pathways.** The
    **frontotemporal_cortical_system** is the **grey-matter cortical
    regions**; the **amygdala_cortex_pathways** (sibling) is the
    **white-matter fibers**. Consumers must **not** conflate the
    two.
*   **NOT the whole frontal or temporal cortex — only the
    AMYGDALA-FACING cortical regions.** The frontotemporal
    cortical system is a **specific subset** of frontal and temporal
    cortical regions defined by their **amygdala connectivity**.
    Consumers must **not** conflate the **amygdala-facing cortical
    system** with the **whole frontal or temporal cortex**.
*   **NOT the central nucleus — the central nucleus is the
    FEAR-OUTPUT.** The cortical system is upstream and modulatory
    relative to the central nucleus in the fear circuit.
*   **NOT the basolateral nuclei — those are the FEAR-LEARNING
    structures.** The cortical system is upstream and modulatory
    relative to the basolateral nuclei.
*   **NOT the basomedial nuclei — those are the FEAR-MODULATORY /
    EXTINCTION structures.** The cortical system is upstream of the
    basomedial nuclei — the **ventromedial prefrontal cortex** is
    the **extinction hub** that **drives** them.
*   **NOT the lateral nucleus — the lateral nucleus is the SENSORY
    INPUT.** The cortical system and the lateral nucleus are
    **different structures**.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    frontotemporal_cortical_system is **not** an extended-amygdala
    component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the cortical system MODULATES fear.**
    The **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the
    **basomedial nuclei**. The **cortical system** is the
    **modulatory** system.
*   **NOT a single functional system — MULTIPLE cortical regions.**
    The **prefrontal**, **orbitofrontal**, **insular**, **anterior
    cingulate**, and **anterior temporal** cortical regions are
    **prose**, not structural children.
*   **No ``AREA_PATHS`` hop.** The frontotemporal_cortical_system is a
    local leaf under the amygdala, not a cross-listed leaf.
*   **No nested cross-listing.** The frontotemporal_cortical_system
    has no nested dual-framing module. It is a single leaf.
*   **Structural parity with left frontotemporal_cortical_system —
    strict mirror with NO warning.** Right and left frontotemporal
    cortical system modules are **structurally identical** — same
    leaf status, same **cortical-region** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.amygdala import frontotemporal_cortical_system

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "medial_temporal_lobe.amygdala.frontotemporal_cortical_system"
    )

**Do not** assume the frontotemporal_cortical_system is the
**amygdala_cortex_pathways**. The **amygdala_cortex_pathways** are
the **white-matter fiber connections**; the
**frontotemporal_cortical_system** is the **grey-matter cortical
regions**. They are **different structures**.

**Do not** assume the frontotemporal_cortical_system is the **whole
frontal or temporal cortex**. It is only the **amygdala-facing**
subset of frontal and temporal cortical regions — the
**prefrontal**, **orbitofrontal**, **insular**, **anterior
cingulate**, and **anterior temporal** cortices.

**Do not** assume the frontotemporal_cortical_system is the
**central nucleus**. The **central nucleus** is the **fear-output**
structure; the **frontotemporal_cortical_system** is the **cortical
modulatory system**.

**Do not** assume the frontotemporal_cortical_system is the
**basolateral nuclei** or the **basomedial nuclei**. Those are the
**fear-learning** and **fear-modulatory / extinction** structures,
respectively; the **frontotemporal_cortical_system** is the
**cortical modulatory system**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the
frontotemporal_cortical_system. **The frontotemporal_cortical_system
is SLEA-FREE** — it is **not** an extended-amygdala component, and
it is **NOT the fear-output structure**. **The right-side module
carries the same no-warning status** — the right
frontotemporal_cortical_system is a cortical modulatory system with
**no SLEA relationship** of its own, and the right-amygdala fear
association belongs to the **amygdala module** (central nucleus +
basolateral nuclei), not to the frontotemporal_cortical_system.

Iterating the frontotemporal_cortical_system's (empty) children
(recommended consumer pattern)::

    FRONTOTEMPORAL_CORTICAL_SYSTEM_CHILDREN = ()
    # The frontotemporal_cortical_system is a leaf. The prefrontal,
    # orbitofrontal, insular, anterior cingulate, and anterior
    # temporal cortical regions are prose, not modules.

Reaching the amygdala_cortex_pathways (recommended consumer pattern
— the sibling)::

    # The amygdala_cortex_pathways is the FIBER-PATHWAY SIBLING of
    # the frontotemporal_cortical_system — the white-matter fibers:
    #
    #   subcortical.medial_temporal_lobe.amygdala.amygdala_cortex_pathways
    #
    # The cortical system is the CORTICAL REGIONS; the pathways are
    # the FIBERS they use.

Reaching the central nucleus (recommended consumer pattern — the
fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure — downstream
    # of the cortical system (via the modulatory projection):
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #
    # The cortical system MODULATES / EXTINGUISHES fear; the central
    # nucleus OUTPUTS it.

Reaching the basolateral nuclei (recommended consumer pattern — the
fear-learning structures)::

    # The basolateral nuclei are the FEAR-LEARNING structures —
    # downstream of the cortical system (via the modulatory
    # projection):
    #
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # The cortical system MODULATES fear learning; the basolateral
    # nuclei ACQUIRE it.

Reaching the basomedial nuclei (recommended consumer pattern — the
fear-modulatory structures)::

    # The basomedial nuclei are the FEAR-MODULATORY / EXTINCTION
    # structures — downstream of the cortical system (via the
    # ventromedial prefrontal projection):
    #
    #   subcortical.medial_temporal_lobe.amygdala.basomedial_nuclei
    #
    # The ventromedial prefrontal cortex is the EXTINCTION HUB that
    # drives the basomedial nuclei.

Reaching the whole frontal / temporal cortex (recommended consumer
pattern — NOTE the subset boundary)::

    # The WHOLE frontal and temporal cortex is much larger — it
    # includes the primary motor cortex, the primary auditory
    # cortex, the language areas, and the whole neocortical temporal
    # lobe:
    #
    #   cortex.frontal
    #   cortex.temporal
    #
    # The frontotemporal_cortical_system is only the AMYGDALA-FACING
    # subset of those cortices.

Reaching the SLEA components (recommended consumer pattern — NOTE
the frontotemporal_cortical_system is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # frontotemporal_cortical_system:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The frontotemporal_cortical_system is SLEA-FREE.

Cortical-region-level detail (not wired — consult references)::

    # The frontotemporal_cortical_system's cortical regions are
    # prose, not modules:
    #   prefrontal       -> top-down regulation, cognitive reappraisal
    #   orbitofrontal    -> reward and emotional valuation
    #   insular          -> interoception and emotional awareness
    #   anterior cingulate -> emotional conflict and salience
    #   anterior temporal -> social cognition and sensory association
    #
    # Do not attempt to resolve these as sub-paths of the
    # frontotemporal_cortical_system.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ftcs_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.amygdala.frontotemporal_cortical_system"
        )
        # resolve ftcs_path through the memory/recall layer

References
----------
*   **Canonical amygdala-cortex connectivity:** Ghashghaei, H.T.,
    Hilgetag, C.C., Barbas, H. (2007). "Sequence of information
    processing for emotions based on the anatomic dialogue between
    prefrontal cortex and amygdala." *NeuroImage* 34:905–923.
    (Definitive amygdala-prefrontal cortical regions; reciprocal
    connections.)
*   **Prefrontal cortex and emotion regulation:** Ochsner, K.N.,
    Gross, J.J. (2005). "The cognitive control of emotion." *Trends
    in Cognitive Sciences* 9:242–249. (Prefrontal cortex and
    cognitive reappraisal.)
*   **Ventromedial prefrontal cortex and extinction:** Quirk, G.J.,
    Beer, J.S. (2006). "Prefrontal involvement in the regulation of
    emotion: convergence of rat and human studies." *Current Opinion
    in Neurobiology* 16:723–727. (Ventromedial prefrontal cortex as
    the extinction hub.)
*   **Anterior cingulate cortex and emotion:** Etkin, A., Egner, T.,
    Kalisch, R. (2011). "Emotional processing in anterior cingulate
    and medial prefrontal cortex." *Trends in Cognitive Sciences*
    15:85–93. (Anterior cingulate cortex and emotional conflict /
    salience.)
*   **Insular cortex and interoception:** Craig, A.D. (2009). "How
    do you feel? Interoception: the sense of the physiological
    condition of the body." *Nature Reviews Neuroscience* 3:655–666.
    (Insular cortex and interoception / emotional awareness.)
*   **Anterior temporal cortex and social cognition:** Olson, I.R.,
    Plotzker, A., Ezzyat, Y. (2007). "The enigmatic temporal pole: a
    review of findings on social and emotional processing." *Brain*
    130:1718–1731. (Anterior temporal cortex and social cognition.)
*   **PTSD and prefrontal dysfunction:** Rauch, S.L., Shin, L.M.,
    Phelps, E.A. (2006). "Neurocircuitry models of posttraumatic
    stress disorder and extinction: human neuroimaging research —
    past, present, and future." *Biological Psychiatry*
    60:376–382. (Prefrontal dysfunction in PTSD.)
*   **Depression and subgenual cingulate:** Mayberg, H.S. (2003).
    "Modulating dysfunctional limbic-cortical circuits in
    depression: towards development of brain-based algorithms for
    diagnosis and optimised treatment." *British Medical Bulletin*
    65:193–207. (Subgenual anterior cingulate and prefrontal
    dysfunction in depression.)
*   **Autism and fronto-temporal connectivity:** Baron-Cohen, S., et
    al. (2000). "The amygdala theory of autism." *Neuroscience &
    Biobehavioral Reviews* 24:355–364. (Atypical amygdala-cortical
    connectivity in autism.)
*   **Psychopathy and amygdala-prefrontal coupling:** Blair, R.J.R.
    (2007). "The amygdala and ventromedial prefrontal cortex in
    morality and psychopathy." *Trends in Cognitive Sciences*
    11:387–392. (Reduced amygdala-prefrontal coupling in
    psychopathy.)
*   **Amygdala-cortex pathways (contrast — the fiber sibling):**
    Von Der Heide, R.J., Skipper, L.M., Klobusicky, E., Olson, I.R.
    (2013). "Dissecting the uncinate fasciculus: disorders,
    controversies and a hypothesis." *Brain* 136:1692–1707.
    (Uncinate fasciculus as the principal amygdala-cortex fiber
    pathway — distinct from the cortical regions it connects.)
*   **SLEA (contrast — the frontotemporal_cortical_system is not
    included):** Alheid, G.F., Heimer, L. (1988). "New perspectives
    in basal forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the frontotemporal_cortical_system.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical
    pathway to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs
    to the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the right frontotemporal
    cortical system.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Frontotemporal cortical system in overview.)
*   NeuroNames — Frontotemporal cortical system (right); FMA —
    Frontotemporal cortical system (right member).
"""