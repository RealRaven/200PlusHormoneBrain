"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.claustrum
================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── claustrum   <-- THIS MODULE

**Primary synonym:** Claustrum; claustrum (Latin: "barrier, bolt,
enclosure"); "the hidden nucleus"; "the claustrum."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**thin, irregular grey-matter sheet** — a **subcortical lamina**
between the **putamen** (medial) and the **insular cortex**
(lateral).
**Part of:** The **subcortical** container — the **only leaf child**
of the subcortical container (the other four are containers:
``basal_forebrain``, ``basal_ganglia``, ``extended_amygdala``,
``medial_temporal_lobe``).
**Structural parent:** ``.../left/subcortical/`` → **direct child** of
the subcortical container.
**Structural children:** **None.** This is a **leaf** module. The
**dorsal/ventral** and **anterior/posterior** subdivisions and the
**claustro-cortical networks** are documented as **prose**, not as
structural children.
**Boundary status (SHEET, not a deep nucleus — "subcortical" by
POSITION, not by cytology):** **Boundary case — the claustrum is a
THIN GREY-MATTER SHEET, not a deep nucleus.** The claustrum is
**lens-shaped** (hence its Latin name, from *claudere* — "to close,"
because it "closes" the putamen from the insular cortex), and it
is **thin** (a few millimeters at its thickest) — **not a deep
nucleus** in the way the **basal ganglia** or **thalamus** are.
"Subcortical" is a **structural convenience** here — the claustrum
is **deep to the insular cortex** (hence "subcortical" by position),
but it is **not a deep nucleus** by **cytology** (it is a **sheet**
of grey matter, more like a **lamina** than a **mass**). Consumers
must **not** treat the claustrum as a deep nucleus — it is a
**thin sheet**, and its **function** is **debated** (see *Function in
the Human Brain*).
**Boundary status (NOT the putamen — sibling of the basal ganglia,
separated by the external capsule):** **Boundary case — the putamen
is a BASAL GANGLIA structure, a SIBLING of the subcortical container,
separated from the claustrum by the EXTERNAL CAPSULE.** The
**putamen** (``.../subcortical/basal_ganglia/striatum/dorsal_striatum/putamen/``)
is **medial** to the claustrum, separated by the **external capsule**
(a white-matter tract). The claustrum is **lateral** to the external
capsule, and **medial** to the **extreme capsule** (which separates it
from the insular cortex). The claustrum and the putamen are
**structurally separate** (different subcortical children — the
putamen under the basal ganglia, the claustrum as a direct child of
the subcortical container) and **functionally distinct** (the putamen
is motor/sensorimotor; the claustrum's function is debated).
Consumers must **not** conflate the two — the **putamen** is a basal
ganglia nucleus; the **claustrum** is a subcortical sheet.
**Boundary status (NOT the insular cortex — LATERAL neighbor,
separated by the extreme capsule):** **Boundary case — the insular
cortex is a NEOCORTICAL structure, LATERAL to the claustrum,
separated by the EXTREME CAPSULE.** The **insular cortex**
(``.../left/cortex/insular/``) is the **six-layered neocortical
mantle** overlying the claustrum, separated by the **extreme
capsule** (a thin white-matter tract). The claustrum is **deep** to
the insular cortex — that is why it is "subcortical" by position.
But the claustrum is **NOT** part of the insular cortex — it is a
**separate structure** under the **subcortical** container, and the
insular cortex is a **neocortical** structure under the **cortex**
container. Consumers must **not** resolve the claustrum through the
insular cortex, or the insular cortex through the claustrum — they are
**two different structures** in **two different containers**.
**Boundary status (NOT the external capsule or extreme capsule —
white-matter separators, not claustrum components):** **Boundary
case — the external capsule and the extreme capsule are WHITE-MATTER
tracts that SEPARATE the claustrum from its neighbors, but they are
NOT claustrum components.** The **external capsule** separates the
**putamen** (medial) from the **claustrum**; the **extreme capsule**
separates the **claustrum** from the **insular cortex** (lateral).
Both are **white-matter tracts** under ``.../left/white_matter/`` —
**not** claustrum children. Consumers must **not** resolve them
through the claustrum.
**Boundary status (NO SLEA relationship — SLEA-FREE leaf):**
**Boundary case — the claustrum has NO extended-amygdala
relationship, NO SLEA overlap, and NO amygdala-lateralization
warning.** The **SLEA overlap** belongs to the **ventral striatum**
(via the **nucleus accumbens**) and the **ventral pallidum** —
**not** to the claustrum. The claustrum is a **subcortical sheet**
with **extensive cortical connections**, and it is **NOT** an
extended-amygdala component. Consumers must **not** import
amygdala-lateralization claims into the claustrum — **there is no
anatomical relationship** to support them. **The warning gradient
that runs through the nucleus accumbens and ventral pallidum does NOT
apply to this module** — the claustrum is a **strict mirror with no
warning**.
**Boundary status (NO rhinencephalon-excluded status — NOT one of the
five):** **Boundary case — the claustrum is NOT one of the FIVE
rhinencephalon-excluded structures.** The five excluded structures
are the **amygdala**, **hippocampus**, **septal nuclei**,
**anterior perforated substance**, and **olfactory tubercle** — all
of which are **wired elsewhere** in the subcortical tree. The
**claustrum is not one of them** — it is a **separate subcortical
leaf**, and it does **not** appear in the `CLASSICAL_FULL_RHINENCEPHALON`
union pattern. Consumers reconstructing the **classical full
rhinencephalon** must **NOT** include the claustrum — it is **not**
a rhinencephalic structure in any classical or modern sense.
**Boundary status (function DEBATED — the defining documentation
caveat):** **Boundary case — the claustrum's FUNCTION is genuinely
DEBATED, and the module documents the debate rather than asserting a
settled function.** The claustrum's **extensive reciprocal
connections** with almost the entire cortex (especially **sensory,
motor, and prefrontal** cortices) are **well established** — but its
**functional role** is **not settled**. The **leading hypotheses**
are:
*   **Salience and attention coordination (leading hypothesis):** The
    claustrum may **coordinate cortical networks** involved in
    **salience detection, attention, and interoception** — its
    extensive connectivity and its position between the insula and
    the striatum make it a candidate **"salience hub."**
*   **Consciousness (controversial — Crick & Koch, 2005):** Crick and
    Koch (2005) proposed the claustrum as a **"conductor" of
    consciousness** — a single structure coordinating cortical areas
    into a unified conscious experience. This is a **hypothesis**, not
    an established fact, and the evidence is **limited** (see the
    Koubeissi case, below).
*   **Slow-wave sleep and cortical synchronization (preclinical):**
    Some **preclinical** studies suggest the claustrum is involved in
    **slow-wave sleep** and **cortical synchronization** — but this
    is **not established** in humans.
*   **Multisensory integration (preclinical):** The claustrum may
    **integrate** inputs from **multiple sensory modalities** — but
    the evidence is **preclinical** and **contested**.
**Consumers must treat the claustrum as a structure with DEBATED
function** — the module documents the debate, and **does not assert**
a settled function. **No named "claustrum syndrome" exists** — see
*Associated Disorders*.
**Boundary status (not a single functional system — the "unitary" vs.
"modular" debate):** **Boundary case — the claustrum may be a
SINGLE UNIFIED STRUCTURE or a SET of MODULAR SUBREGIONS, and the
debate is UNRESOLVED.** Some models treat the claustrum as a **single
"unitary" structure** with **one function** (e.g., Crick & Koch's
"conductor"); others treat it as a **set of modular subregions**,
each connecting to a **different cortical area** (sensory, motor,
prefrontal) and **functionally distinct**. The **"modular"
interpretation** is **better supported** by the **connectivity
evidence** (the claustrum has **topographic** connections with
**different cortical areas**), but the **"unitary" interpretation**
remains **influential** (especially for the **consciousness**
hypothesis). Consumers must **not** assume the claustrum is a single
functional system — it may be **modular**, and the debate is
**unresolved**.
**Boundary status (rare case report of consciousness loss — Koubeissi
et al., 2014):** **Boundary case — the claustrum's most famous
experimental association is a SINGLE CASE REPORT (Koubeissi et al.,
2014) in which electrical stimulation produced LOSS OF CONSCIOUSNESS.**
The **Koubeissi et al. (2014)** case report described a patient with
**epilepsy** whose **claustrum** was **electrically stimulated** (as
part of **intracranial EEG monitoring**), producing **loss of
consciousness** — the patient **stopped reading** and **did not
respond** during stimulation, and **resumed** when stimulation
stopped. This is **the strongest evidence** for the
**consciousness hypothesis**, but it is a **single case report** —
**not** a replicated finding — and it must be interpreted
**cautiously**. Consumers must **not** treat the claustrum as "the
seat of consciousness" — the evidence is **one case**, and the
**function remains debated**.

Overview
--------
The claustrum is a **thin, irregular grey-matter sheet** lying
**between the putamen** (medial, separated by the **external
capsule**) and the **insular cortex** (lateral, separated by the
**extreme capsule**), **deep to the insular cortex** and **lateral
to the basal ganglia**. Its Latin name (*claustrum* — "barrier,
bolt, enclosure") reflects its **position**: it is a **lens-shaped
sheet** that "closes" the putamen from the insular cortex. It is the
**only leaf child** of the **subcortical container** — the other four
children (``basal_forebrain``, ``basal_ganglia``,
``extended_amygdala``, ``medial_temporal_lobe``) are **containers**,
while the claustrum is a **single structure** with **no children**.

**The claustrum has extensive reciprocal connections with almost the
entire cortex.** It receives **afferent** input from **sensory,
motor, and prefrontal** cortices (and from the **thalamus**), and it
projects **back** to the same cortical areas — a **reciprocal
cortico-claustro-cortical loop**. Its **connectivity** is
**topographic** — different **claustrum subregions** connect to
**different cortical areas** (a **sensory** zone, a **motor** zone, a
**prefrontal** zone, etc.) — suggesting a **modular** organization.
The **extensive connectivity** is **well established**; the
**functional role** of that connectivity is **debated**.

**The claustrum's function is genuinely debated.** The **leading
hypotheses** — **salience/attention coordination**, **consciousness**
(Crick & Koch, 2005), **slow-wave sleep**, and **multisensory
integration** — are **not mutually exclusive**, and the evidence for
each is **limited or preclinical**. **No named "claustrum syndrome"
exists** — the structure is **not** the substrate for any established
clinical disorder. The claustrum's **most famous experimental
association** is the **Koubeissi et al. (2014) case report** in which
**electrical stimulation** produced **loss of consciousness** — a
**single case**, not a replicated finding.

**The claustrum is SLEA-free.** The **extended amygdala (SLEA)**
overlap belongs to the **ventral striatum** (via the **nucleus
accumbens**) and the **ventral pallidum** — **not** to the claustrum.
**The warning gradient that runs through the nucleus accumbens and
ventral pallidum does NOT apply to this module** — the claustrum is
a **strict mirror with no warning**.

**The claustrum is NOT one of the five rhinencephalon-excluded
structures.** The five are the **amygdala**, **hippocampus**,
**septal nuclei**, **anterior perforated substance**, and **olfactory
tubercle** — all wired elsewhere. The claustrum is a **separate
subcortical leaf** and does **not** appear in the
`CLASSICAL_FULL_RHINENCEPHALON` union pattern. Consumers reconstructing
the **classical full rhinencephalon** must **NOT** include the
claustrum.

**The claustrum is a paired structure.** Each hemisphere has its own
claustrum, with **ipsilateral** cortical connections. The two sides
are **bilaterally symmetric** and **largely non-lateralized** — no
**strong** lateralized syndrome has been reported, though **weak,
contested** lateralization has been suggested (left for language,
right for visual attention). See *Lateralization Notes*.

Subdivisions (prose, not structural children)
---------------------------------------------
The claustrum has **several subdivisions**, all documented as
**prose** — and all **debated** in their boundaries:

*   **Dorsal/ventral subdivisions** — the **dorsal** part is more
    **sensory/motor** (connected to sensory and motor cortices); the
    **ventral** part is more **limbic-adjacent** (connected to the
    **insular** and **amygdala-adjacent** cortices). This is a
    **graded** subdivision, not a sharp boundary.

*   **Anterior/posterior subdivisions** — the **anterior** part is
    more **prefrontal-adjacent**; the **posterior** part is more
    **parietal-occipital-adjacent**. This is a **graded** subdivision,
    not a sharp boundary.

*   **Modular cortical connectivity zones** — the **leading
    interpretation** is that the claustrum is **modular** — different
    subregions connect to **different cortical areas** (a **sensory
    zone**, a **motor zone**, a **prefrontal zone**). The **"unitary"
    vs. "modular"** debate is **unresolved** (see *Boundary status
    (not a single functional system)*).

**These subdivisions are prose, not structural children.** The tree
wires the claustrum as a **single leaf** — the subdivisions are
**topographic** or **connection-based**, not **separate nuclei**.
Consumers that need subdivision-level resolution should consult the
references, not the tree.

The Claustrum / Putamen Boundary
--------------------------------
This is the **medial** boundary of the claustrum:

*   **Claustrum** (this module) — the **subcortical sheet** lateral
    to the **external capsule**. **Subcortical container** child.

*   **Putamen** (``.../subcortical/basal_ganglia/striatum/dorsal_striatum/putamen/``)
    — the **motor/sensorimotor** nucleus **medial** to the external
    capsule. **Basal ganglia** child.

**They are separated by the external capsule (white matter).** The
putamen is a **basal ganglia nucleus**; the claustrum is a
**subcortical sheet**. They are **structurally separate** (different
subcortical children) and **functionally distinct** (the putamen is
motor/sensorimotor; the claustrum's function is debated). Consumers
must **not** conflate the two.

The Claustrum / Insular Cortex Boundary
---------------------------------------
This is the **lateral** boundary of the claustrum:

*   **Claustrum** (this module) — the **subcortical sheet** medial
    to the **extreme capsule**. **Subcortical container** child.

*   **Insular cortex** (``.../left/cortex/insular/``) — the
    **six-layered neocortical mantle** lateral to the extreme
    capsule. **Cortex** container child.

**They are separated by the extreme capsule (white matter).** The
claustrum is **deep** to the insular cortex — that is why it is
"subcortical" by position. But they are **two different structures**
in **two different containers** (subcortical vs. cortex). Consumers
must **not** resolve the claustrum through the insular cortex, or
the insular cortex through the claustrum.

The Claustrum / White-Matter Separators Boundary
------------------------------------------------
This is the **white-matter** boundary of the claustrum:

*   **Claustrum** (this module) — the **grey-matter sheet** between
    the **external capsule** (medial) and the **extreme capsule**
    (lateral).

*   **External capsule** — ``.../left/white_matter/`` — the
    **white-matter tract** separating the **putamen** from the
    **claustrum**.

*   **Extreme capsule** — ``.../left/white_matter/`` — the
    **white-matter tract** separating the **claustrum** from the
    **insular cortex**.

**Both capsules are white matter, NOT claustrum components.** They
**separate** the claustrum from its neighbors, but they are **not**
claustrum children. Consumers must **not** resolve them through the
claustrum.

The Claustrum / Extended Amygdala Boundary
------------------------------------------
This is the **SLEA** boundary — **NOT applicable** to the claustrum:

*   **Claustrum** (this module) — **SLEA-FREE**. No extended-amygdala
    relationship, no SLEA overlap, no amygdala-lateralization warning.

*   **Extended amygdala** (``.../extended_amygdala/``) — the **BNST**
    and the **central amygdaloid nucleus**. **Classically** the
    extended amygdala; **SLEA** adds the **ventral pallidum** and
    parts of the **nucleus accumbens**.

**The claustrum is NOT part of the extended amygdala.** It is a
**subcortical sheet** with **cortical connections**, and its
**relationship to the amygdala is indirect** (via the **insular
cortex** and **amygdala-adjacent cortices**) — **not** an SLEA
relationship. The **SLEA union pattern** does **NOT** include the
claustrum. Consumers must **not** import the SLEA warning into the
claustrum — it is **SLEA-free**.

Function in the Human Brain
---------------------------
The claustrum's function is **debated** — the module documents the
**leading hypotheses**, **without asserting** a settled function:

*   **Salience and Attention Coordination (Leading Hypothesis):**
    The claustrum's **extensive reciprocal connections** with
    **sensory, motor, and prefrontal** cortices suggest a role in
    **coordinating cortical networks** involved in **salience
    detection, attention, and interoception**. Its position **between
    the insula and the striatum** makes it a candidate **"salience
    hub"** — a structure that **integrates** across cortical
    modalities and **coordinates** the cortical response to
    **behaviorally relevant** stimuli. This is the **leading
    hypothesis**, but it is **not settled**.

*   **Consciousness (Controversial — Crick & Koch, 2005):** Crick and
    Koch (2005) proposed the claustrum as a **"conductor" of
    consciousness** — a single structure **coordinating** cortical
    areas into a **unified conscious experience**. This is a
    **hypothesis**, and the **evidence is limited** — the **Koubeissi
    et al. (2014) case report** (below) is the **strongest support**,
    but it is a **single case**. The **"claustrum as consciousness
    organ"** is a **controversial** idea, **not** an established fact.

*   **Slow-Wave Sleep and Cortical Synchronization (Preclinical):**
    Some **preclinical** studies suggest the claustrum is involved in
    **slow-wave sleep** and **cortical synchronization** — its
    **widespread cortical projections** could **synchronize** cortical
    activity during **slow-wave sleep**. The evidence is
    **preclinical** and **not established** in humans.

*   **Multisensory Integration (Preclinical):** The claustrum may
    **integrate** inputs from **multiple sensory modalities** — its
    **sensory-zone** connections could **combine** visual, auditory,
    and somatosensory information. The evidence is **preclinical** and
    **contested**.

*   **Loss of Consciousness on Stimulation (Koubeissi et al., 2014 —
    single case):** The **most famous experimental association** is
    the **Koubeissi et al. (2014)** case report — **electrical
    stimulation** of the **claustrum** in a **patient with epilepsy**
    produced **loss of consciousness** (the patient **stopped
    reading** and **did not respond**), and **resumed** when
    stimulation stopped. This is the **strongest evidence** for the
    **consciousness hypothesis**, but it is a **single case report**
    — **not** a replicated finding — and it must be interpreted
    **cautiously**.

*   **NOT a settled functional system.** The claustrum is **not**
    established as a **sensory processor**, a **motor processor**, a
    **limbic processor**, or a **"consciousness organ"** — the
    **leading hypotheses** (salience, consciousness, slow-wave sleep,
    multisensory integration) are **not mutually exclusive**, and the
    evidence for each is **limited or preclinical**.

**The unifying theme:** the claustrum is a **thin subcortical sheet**
with **extensive cortical connections** and a **genuinely debated
function**. The **connectivity** is **well established**; the
**functional role** is **not settled**. **No named "claustrum
syndrome" exists** — the module documents the **debate**, and
**does not assert** a settled function.

Associated Disorders
--------------------
The claustrum has **no named clinical syndrome** — its clinical
associations are **rare case reports** and **contested** findings:

*   **Loss of Consciousness on Stimulation (Koubeissi et al., 2014 —
    single case):** **Electrical stimulation** of the **claustrum**
    in a **patient with epilepsy** produced **loss of consciousness**
    — the **strongest experimental association** of the claustrum,
    but a **single case report**. **No named syndrome** — the case
    is a **single observation**, not a replicated clinical entity.

*   **Claustrum Lesions (Rare Case Reports):** **Focal claustrum
    lesions** (from stroke, tumor, or surgery) are **rare**, and their
    clinical effects are **variable** — some reports describe
    **attention deficits**, **salience impairment**, or **subtle
    cognitive changes**, but **no consistent syndrome** has emerged.
    The **rarity** of isolated claustrum lesions (because the
    structure is **small** and **deep**) limits the **clinical
    evidence**.

*   **Schizophrenia (Contested — Morphometric Findings):** Some
    **morphometric** studies report **claustrum volume reductions**
    in **schizophrenia**, but the findings are **inconsistent** and
    **contested**. The claustrum's **extensive cortical
    connectivity** makes it a **plausible** node in **schizophrenia
    network models**, but the **evidence is not established**.

*   **Alzheimer's Disease (Contested):** Some studies report
    **claustrum pathology** in **Alzheimer's disease**, but the
    findings are **inconsistent** and **contested** — the claustrum
    is **not** a **primary** Alzheimer's substrate (the **nucleus
    basalis** is).

*   **Epilepsy (Stimulation Context):** The **Koubeissi et al.
    (2014)** case was in a **patient with epilepsy** undergoing
    **intracranial EEG monitoring** — the claustrum **stimulation**
    was part of the **epilepsy workup**, not a treatment for
    epilepsy. The claustrum is **not** an **epilepsy substrate** in
    the way the **hippocampus** is.

**What is NOT here:** The claustrum is **not** the substrate for
**Parkinson's disease** (putamen), **Huntington's disease** (caudate),
**dystonia** (putamen), **Tourette syndrome** (caudate), **addiction**
(nucleus accumbens), **depression** (nucleus accumbens and ventral
pallidum), **Kluver-Bucy syndrome** (amygdala), **temporal lobe
epilepsy** (hippocampus), or **Alzheimer's disease** (nucleus
basalis). Its clinical footprint is **rare case reports** (loss of
consciousness on stimulation, focal lesions) and **contested
morphometric findings** (schizophrenia, Alzheimer's) — **no named
syndrome** exists, and the structure's **function is debated**.

Lateralization Notes
--------------------
This is the **left** claustrum module. The claustrum is **bilaterally
symmetric** and **largely non-lateralized** — and it carries **NO
warning**:

*   **Bilateral Cortical Connections:** Each claustrum has
    **ipsilateral** reciprocal connections with its own hemisphere's
    cortex. The two sides are **functionally symmetric** for the
    claustrum's (debated) functions.

*   **Weak Lateralization (Contested):** Some studies suggest **left
    claustrum** involvement in **language-related** tasks and **right
    claustrum** involvement in **visual attention** — but this is
    **weak**, **contested**, and **not a strong basis for
    classification**. **No strong lateralized syndrome** has been
    reported.

*   **NO Extended-Amygdala Warning (strict mirror with no warning):**
    The claustrum has **NO extended-amygdala relationship**, **NO
    SLEA overlap**, and **NO amygdala-lateralization warning**. The
    **SLEA warning** belongs to the **nucleus accumbens** and
    **ventral pallidum** — **not** here. Consumers must **not**
    import amygdala-lateralization claims into the claustrum —
    **there is no anatomical relationship** to support them.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module** — **not** to the claustrum. **The claustrum is
    SLEA-free** — the right-amygdala fear association **does not**
    apply to it.

**A consumer that assumes "left claustrum = right claustrum" will be
structurally and functionally correct** — the two sides are
**symmetric**, no **strong** lateralized syndrome has been
demonstrated, and the **weak** lateralization reported for language
and visual attention is **contested**, not a strong classification
basis. The claustrum is a **strict-mirror pair with no warning** —
matching the **dorsal striatum leaves** and the **olfactory
tubercle** in their **SLEA-free** status.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``.../white_matter/``, ``.../extended_amygdala/``, or
    any other container. The claustrum's relationships to the putamen,
    insular cortex, external capsule, extreme capsule, and extended
    amygdala are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **dorsal/ventral**
    and **anterior/posterior** subdivisions and the **modular
    cortical connectivity zones** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve subdivision-level detail through the references.
*   **SHEET, not a deep nucleus.** The claustrum is a **thin
    grey-matter sheet** — "subcortical" by **position**, not by
    **cytology**. Consumers must not treat it as a deep nucleus in the
    way the basal ganglia or thalamus are.
*   **NOT the putamen — sibling of the basal ganglia.** The putamen
    is a **basal ganglia** structure, separated from the claustrum by
    the **external capsule**. Consumers must not conflate them.
*   **NOT the insular cortex — lateral neighbor, separated by the
    extreme capsule.** The insular cortex is a **neocortical**
    structure under the **cortex** container — **not** the claustrum.
*   **NOT the external capsule or extreme capsule — white-matter
    separators.** Both are **white matter** under
    ``.../left/white_matter/`` — **not** claustrum components.
*   **NO SLEA relationship — SLEA-FREE leaf.** The claustrum is
    **not** an extended-amygdala component. The **SLEA warning** does
    **not** apply to it.
*   **NO rhinencephalon-excluded status — NOT one of the five.**
    Consumers reconstructing the **classical full rhinencephalon**
    must **NOT** include the claustrum.
*   **Function DEBATED — the module documents the debate.** The
    **leading hypotheses** (salience/attention, consciousness,
    slow-wave sleep, multisensory integration) are **not mutually
    exclusive**, and the evidence for each is **limited or
    preclinical**. **No named "claustrum syndrome" exists.**
*   **NOT a single functional system — the "unitary" vs. "modular"
    debate is unresolved.** Some models treat the claustrum as a
    **single unified structure** (Crick & Koch's "conductor"); others
    treat it as **modular subregions** with **different cortical
    connections**. The **"modular" interpretation** is **better
    supported** by the connectivity evidence, but the debate is
    **unresolved**.
*   **The Koubeissi et al. (2014) case is a SINGLE CASE REPORT.** It
    is the **strongest experimental association** for the
    **consciousness hypothesis**, but it is **one case** — **not** a
    replicated finding. Consumers must **not** treat the claustrum as
    "the seat of consciousness."
*   **No ``AREA_PATHS`` hop.** The claustrum is a local leaf under the
    subcortical container, not a cross-listed leaf.
*   **No nested cross-listing.** The claustrum has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with right claustrum — strict mirror with NO
    warning.** Left and right claustrum modules are **structurally
    identical** — same leaf status, same subdivisions as prose, same
    **SLEA-free** status, same **function debated** caveat, same
    **Koubeissi case** reference, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical import claustrum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical.claustrum"
    )

**Do not** assume the claustrum is the **putamen**. The **putamen**
is a **basal ganglia** structure (motor/sensorimotor), separated from
the claustrum by the **external capsule**. The **claustrum** is a
**subcortical sheet** with **debated function**.

**Do not** assume the claustrum is the **insular cortex**. The
**insular cortex** is a **neocortical** structure (under the
**cortex** container), separated from the claustrum by the **extreme
capsule**.

**Do not** assume the claustrum **contains** the external capsule or
extreme capsule. Both are **white matter** — separators, **not**
claustrum components.

**Do not** assume the claustrum has a **structural child**. It is a
**leaf** — the subdivisions are **prose only**.

**Do not** import **amygdala-lateralization claims** into the
claustrum. **The claustrum is SLEA-free** — there is **no anatomical
relationship** to the amygdala, and the right-amygdala fear
association **does not** apply to it.

**Do not** include the claustrum in the **classical full
rhinencephalon** union — the claustrum is **NOT** one of the five
excluded structures.

**Do not** treat the claustrum as "the seat of consciousness" — the
**Koubeissi et al. (2014)** case is a **single case report**, and the
function remains **debated**.

Iterating the claustrum's (empty) children (recommended consumer
pattern)::

    CLAUSTRUM_CHILDREN = ()
    # The claustrum is a leaf. The subdivisions and modular cortical
    # connectivity zones are prose, not modules.

Reconstructing the classical full rhinencephalon (recommended
consumer pattern — the claustrum is NOT included)::

    # The claustrum is NOT one of the five rhinencephalon-excluded
    # structures. Do not include it in the union:
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",
        ),
        # NOTE: claustrum is NOT included — it is not a rhinencephalic
        # structure in any classical or modern sense.
    }

Reaching the putamen (recommended consumer pattern — NOTE the
external capsule boundary)::

    # The putamen is MEDIAL to the claustrum, separated by the
    # EXTERNAL CAPSULE. It is a BASAL GANGLIA structure, not a
    # claustrum child:
    #
    #   subcortical.basal_ganglia.striatum.dorsal_striatum.putamen
    #
    # Do NOT resolve the putamen through the claustrum.

Reaching the insular cortex (recommended consumer pattern — NOTE
the extreme capsule boundary)::

    # The insular cortex is LATERAL to the claustrum, separated by
    # the EXTREME CAPSULE. It is a NEOCORTICAL structure, not a
    # claustrum child:
    #
    #   cortex.insular
    #
    # Do NOT resolve the insular cortex through the claustrum.

Reaching the external capsule and extreme capsule (recommended
consumer pattern — NOTE the white-matter boundary)::

    # The external capsule and extreme capsule are WHITE-MATTER
    # tracts that separate the claustrum from its neighbors. They are
    # NOT claustrum components:
    #
    #   white_matter.external_capsule
    #   white_matter.extreme_capsule
    #
    # Do NOT resolve them through the claustrum.

Reaching the extended amygdala's SLEA components (recommended
consumer pattern — NOTE the claustrum is NOT included)::

    # The SLEA classification includes the nucleus accumbens and the
    # ventral pallidum. It does NOT include the claustrum:
    #
    #   subcortical.extended_amygdala
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #
    # The claustrum is SLEA-FREE — do not include it.

Function status (debated — consult references)::

    # The claustrum's function is DEBATED. The leading hypotheses
    # are:
    #   - salience and attention coordination (leading)
    #   - consciousness (Crick & Koch, 2005 — controversial)
    #   - slow-wave sleep / cortical synchronization (preclinical)
    #   - multisensory integration (preclinical)
    #
    # No named "claustrum syndrome" exists. Do not assert a settled
    # function for the claustrum — the documentation must reflect
    # the debate.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cl_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"claustrum"
        )
        # resolve cl_path through the memory/recall layer

References
----------
*   **Canonical claustrum anatomy:** Sherk, H. (1986). "The
    claustrum and the cerebral cortex." In *Cerebral Cortex* (Jones,
    E.G., Peters, A., eds.), Vol. 5. (Definitive anatomical overview;
    claustrum position, shape, and cortical connectivity.)
*   **Claustrum connectivity:** Crick, F.C., Koch, C. (2005). "What
    is the function of the claustrum?" *Philosophical Transactions of
    the Royal Society B* 360:1271–1279. (The **consciousness
    hypothesis** — the claustrum as a "conductor" of consciousness;
    influential but **controversial**.)
*   **Claustrum review:** Edelstein, L.R., Denaro, F.J. (2004). "The
    claustrum: a historical review of its anatomy, physiology,
    cytochemistry, and development." *Cellular and Molecular
    Biology* 50:675–702. (Historical and functional review.)
*   **Koubeissi et al. (2014) — single case report:** Koubeissi,
    M.Z., Bartolomei, F., Beltagy, A., Picard, F. (2014).
    "Electrical stimulation of a small brain area reversibly disrupts
    consciousness." *Epilepsy & Behavior* 37:32–35. (The **single
    case report** — claustrum stimulation produced loss of
    consciousness; the **strongest experimental association** of the
    claustrum, but a **single case**, not a replicated finding.)
*   **Modular vs. unitary debate:** Remedios, R., Logothetis, N.K.,
    Kayser, C. (2010). "Unimodal responses prevail within the
    multisensory claustrum." *Journal of Neuroscience*
    30:12902–12907. (Modular claustrum — different subregions respond
    to different modalities.)
*   **Multisensory integration (preclinical):** Mathur, B.N. (2014).
    "The claustrum in review." *Frontiers in Systems Neuroscience*
    8:48. (Review of claustrum function — salience, attention,
    multisensory integration, and consciousness hypotheses.)
*   **Claustrum and slow-wave sleep (preclinical):** Narikiyo, K., et
    al. (2020). "The claustrum coordinates cortical slow-wave
    activity." *Nature Neuroscience* 23:741–753. (Preclinical
    evidence for claustrum in slow-wave sleep and cortical
    synchronization.)
*   **Schizophrenia (contested):** Cascella, N.G., Gerner, G.J.,
    Fieldstone, S.C., Sawa, A., Schretlen, D.J. (2011). "The
    claustrum in schizophrenia." *Schizophrenia Research*
    130:1–8. (Contested morphometric findings in schizophrenia.)
*   **Alzheimer's disease (contested):** Moryś, J., et al. (1994).
    "The claustrum in Alzheimer's disease." *Acta Neuropathologica*
    87:614–620. (Contested claustrum pathology in Alzheimer's
    disease.)
*   **Putamen (contrast — medial boundary):** Alexander, G.E.,
    DeLong, M.R., Strick, P.L. (1986). "Parallel organization of
    functionally segregated circuits linking basal ganglia and
    cortex." *Annual Review of Neuroscience* 9:357–381. (Putamen as
    a basal ganglia structure — separated from the claustrum by the
    external capsule.)
*   **Insular cortex (contrast — lateral boundary):** Nieuwenhuys,
    R., Voogd, J., van Huijzen, C. (2008). *The Human Central
    Nervous System*, 4th ed. (Insular cortex as a neocortical
    structure — separated from the claustrum by the extreme
    capsule.)
*   **White matter (contrast — external and extreme capsules):**
    Schmahmann, J.D., Pandya, D.N. (2006). *Fiber Pathways of the
    Brain*. (External capsule and extreme capsule as white-matter
    tracts separating the claustrum from its neighbors.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical
    pathway to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association does
    **not** apply to the claustrum — the claustrum is **SLEA-free**
    and has **no anatomical relationship** to the amygdala.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Claustrum in overview.)
*   NeuroNames — Claustrum (left); FMA — Claustrum (left member).
"""