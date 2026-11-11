"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain.lamina_terminalis.vascular_organ_of_lamina_terminalis
==========================================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── basal_forebrain
                    └── lamina_terminalis
                        └── vascular_organ_of_lamina_terminalis   <-- THIS MODULE

**Primary synonym:** Organum vasculosum of the lamina terminalis
(OVLT); vascular organ of the lamina terminalis; supraoptic crest
(historical); "the OVLT."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**circumventricular organ** — a **fenestrated-capillary bed** with
**neurosecretory neurons** embedded in the **lamina terminalis**.
**Part of:** The **forebrain circumventricular system** and the
**osmoregulatory circuit** (thirst, vasopressin, sodium homeostasis).
**Structural parent:** ``.../basal_forebrain/lamina_terminalis/`` →
**only child** of the lamina terminalis container.
**Structural children:** **None.** This is a **leaf** module. The
**fenestrated capillaries**, **neurosecretory neurons**, and
**tanycytes** are documented as **prose**, not as structural
children.
**Boundary status (midline structure — duplication pair):** **Boundary
case — a midline structure, not an anatomically paired one.** The
OVLT is a **single midline organ** embedded in the mid-portion of the
lamina terminalis. The tree wires it under ``left/`` and ``right/``
as **structural duplicates** of the same midline organ. Consumers
must **not** treat the left and right modules as anatomically separate
structures — they are the **two halves of the same midline organ**.
See *Lateralization Notes*.
**Boundary status (circumventricular organ — not a neural
processor):** **Boundary case — a sensory circumventricular organ,
not a neural processing structure.** The OVLT is a **sensory CVO**:
its **fenestrated capillaries** lack the blood-brain barrier, allowing
**circulating molecules** (osmolality, angiotensin II, pyrogens,
relaxin) to **access** its neurons directly. It **senses** plasma
composition and **drives** hypothalamic responses — it does **not**
process neural information in the way a cortical area or a deep
nucleus does. Consumers must not treat the OVLT as a processor; it
is a **sensor** and a **neurohemal interface**.
**Boundary status (not the lamina terminalis membrane):** **Boundary
case — the OVLT is INSIDE the lamina terminalis, but the two are
distinct structures.** The **lamina terminalis** (the parent) is the
**thin grey-matter membrane** forming the anterior wall of the third
ventricle. The **OVLT** (this module) is the **circumventricular organ
embedded in the membrane's mid-portion**. The membrane is the
**housing**; the OVLT is the **functional core**. Consumers must
resolve both — the **membrane** (parent module) and the **OVLT**
(this module) — as **distinct structures**. A consumer that resolves
the lamina terminalis and expects the OVLT functions will be
**partially misled** (the membrane itself does not sense osmolality);
a consumer that resolves the OVLT and expects the membrane will be
**partially misled** (the OVLT is a small organ, not the whole
membrane).
**Boundary status (the classical CVO group is split):** **Boundary
case — the classical "lamina terminalis CVO group" is split across the
tree.** Classical anatomy groups **three CVOs** with the lamina
terminalis region:
*   **OVLT** — **HERE** (this module).
*   **Subfornical organ (SFO)** —
    ``.../diencephalon/hypothalamus/.../subfornical_organ/`` — **NOT
    here**.
*   **Median eminence** —
    ``.../diencephalon/hypothalamus/.../median_eminence/`` — **NOT
    here**.
Additionally, **three other CVOs** are elsewhere:
*   **Pineal gland** —
    ``.../diencephalon/epithalamus/pineal_gland/`` — **NOT here**.
*   **Subcommissural organ** —
    ``.../diencephalon/subcommissural_organ/`` — **NOT here**.
*   **Area postrema** —
    ``.../hindbrain/myelencephalon/medulla_oblongata/.../area_postrema/``
    — **NOT here**.
Consumers reconstructing the **classical lamina terminalis CVO group**
must **union** this module with the **hypothalamus** (SFO, ME).
Consumers reconstructing the **full CVO set** must add the **pineal**,
**subcommissural organ**, and **area postrema**. The OVLT module
provides **only the OVLT**.
**Boundary status (fenestrated capillaries — BBB absent):** **Boundary
case — the OVLT lacks a blood-brain barrier by design.** The OVLT's
**fenestrated capillaries** are the **structural basis** of its
sensory function. They allow **circulating osmolality**, **angiotensin
II**, **pyrogens** (IL-1, LPS), and **relaxin** to reach its neurons
**directly** — bypassing the BBB. This is **not a defect**; it is the
**organ's defining feature**. Consumers must not treat "BBB absent"
as pathology; it is **how the OVLT works**.
**Boundary status (neurohemal organ):** **Boundary case — a
neurohemal interface, not a classical gland.** The OVLT contains
**neurosecretory neurons** that release peptides into its fenestrated
capillaries — it is a **neurohemal organ**, like the **median
eminence** and the **posterior pituitary**, but its secretory products
are **less well characterized**. Consumers must not treat the OVLT as
a classical endocrine gland; it is a **sensory neurohemal interface**
with **both** sensing and secretory functions.

Overview
--------
The organum vasculosum of the lamina terminalis is a **small
circumventricular organ** embedded in the **mid-portion of the lamina
terminalis**, at the **anterior wall of the third ventricle**. It is
a **fenestrated-capillary bed** surrounded by **neurons** and
**tanycytes** (specialized ependymoglial cells), and it **lacks a
blood-brain barrier** — its capillaries are **fenestrated**,
allowing **circulating molecules** to reach its neurons directly.

**The OVLT is one of the three sensory CVOs of the forebrain.** The
**sensory CVOs** are the **OVLT**, the **subfornical organ (SFO)**, and
the **area postrema (AP)**. They share a **fenestrated-capillary,
BBB-absent** structure and a **sensory** function — they **detect**
circulating signals that the rest of the brain cannot see. The OVLT's
**specific sensory role** is to detect **plasma osmolality**,
**circulating angiotensin II**, and **circulating pyrogens** — the
three signals that drive **thirst**, **vasopressin release**, and
**fever**.

**The OVLT is the "osmostat" of the forebrain.** Its **osmosensitive
neurons** (and its **tanycytes**) detect **small increases in plasma
osmolality** (as little as 1–2%) and trigger **thirst** and
**vasopressin (ADH) release**. It also detects **circulating
angiotensin II** (from the renin-angiotensin system) — a **second**
thirst signal that is **independent** of osmolality. The OVLT is
therefore a **convergence point** for **osmotic** and **hormonal**
thirst signals.

**The OVLT is also a site of fever generation.** **Circulating
pyrogens** (IL-1, IL-6, TNF-α, LPS) act on the OVLT (and on the
adjacent **median preoptic nucleus**) to **induce prostaglandin E2
(PGE2) synthesis** via **COX-2**. PGE2 then acts on **thermoregulatory
neurons** in the **preoptic area** to **raise the body's temperature
set-point** — producing **fever**. **Antipyretics** (aspirin,
ibuprofen, acetaminophen) work by **inhibiting COX-2** in this
pathway.

**The OVLT is a midline structure.** It is a **single midline organ**;
the tree wires it under **left/** and **right/** as **structural
duplicates**. The **left and right modules** describe the **same
midline organ**, split for structural symmetry. See *Lateralization
Notes*.

Structure (prose, not structural children)
------------------------------------------
The OVLT has **no structural children** in the tree, but its
**cytoarchitecture** is distinctive:

*   **Fenestrated capillaries** — the **defining feature**. Unlike
    the normal brain capillaries (which are **non-fenestrated** and
    form the **blood-brain barrier**), the OVLT's capillaries have
    **pores (fenestrae)** that allow **free exchange** between blood
    and the OVLT's interstitial space. This is how **circulating
    osmolality**, **angiotensin II**, **pyrogens**, and **relaxin**
    reach the OVLT's neurons.

*   **Neurosecretory neurons** — the OVLT contains **neurons** that
    release peptides into its **fenestrated capillaries**. These are
    **neurosecretory cells** — they are **not** classical neurons
    (they do not primarily form synapses; they **secrete** into the
    blood). Their secretory products are **less well characterized**
    than those of the median eminence, but they include **relaxin**
    and possibly **other peptides**.

*   **Tanycytes** — specialized **ependymoglial cells** that line the
    OVLT's **ventricular surface** and extend processes into its
    **neuropil**. Tanycytes are involved in **osmosensing**,
    **peptide transport**, and **CSF-blood exchange**. They are
    **not** neurons; they are **glia-like** cells that contribute to
    the OVLT's **sensory function**.

*   **Glial ensheathment** — the OVLT's neurons are **ensheathed by
    glia** in a pattern that is **intermediate** between normal brain
    tissue (extensive glial ensheathment) and peripheral tissue
    (minimal ensheathment). This **loosened glial barrier** is part
    of the OVLT's **sensory-permissive** architecture.

**These structural features are prose, not structural children.** The
tree does **not** wire fenestrated capillaries, neurosecretory neurons,
tanycytes, or glial ensheathment as sub-modules. Consumers that need
cytoarchitectural detail should consult the references, not the tree.

The OVLT / Lamina Terminalis Boundary
-------------------------------------
This is the **most consequential boundary** in the OVLT module:

*   **Lamina terminalis** (parent) — the **thin grey-matter membrane**
    forming the anterior wall of the third ventricle. Its functions
    are **membrane functions** (housing the OVLT, forming the wall).

*   **OVLT** (this module) — the **circumventricular organ embedded
    in the membrane's mid-portion**. Its functions are
    **sensory-neurosecretory** (osmolality, angiotensin II, pyrogens,
    relaxin → thirst, vasopressin, fever).

**The membrane houses the organ, but they are distinct structures.**
Consumers that need the **membrane** resolve the parent; consumers
that need the **osmoregulatory organ** resolve this module. The
**membrane alone** does not sense osmolality; the **organ alone** is
a small structure, not the whole membrane.

The OVLT / Other CVOs Boundary
------------------------------
The OVLT is **one of six CVOs** in the tree. Its **sibling CVOs** are
documented elsewhere:

| CVO | Tree location | Function |
|---|---|---|
| **OVLT** (this module) | `subcortical/basal_forebrain/lamina_terminalis/vascular_organ_of_lamina_terminalis/` | Osmoregulation, thirst, vasopressin, fever |
| **Subfornical organ (SFO)** | `diencephalon/hypothalamus/.../subfornical_organ/` | Angiotensin II sensing (thirst), osmoregulation |
| **Median eminence** | `diencephalon/hypothalamus/.../median_eminence/` | Neuroendocrine (hypothalamic-releasing hormones → portal system) |
| **Pineal gland** | `diencephalon/epithalamus/pineal_gland/` | Melatonin secretion |
| **Subcommissural organ** | `diencephalon/subcommissural_organ/` | Reissner's fiber/glycoprotein secretion |
| **Area postrema** | `hindbrain/myelencephalon/medulla_oblongata/.../area_postrema/` | Emetic sensing (vomiting) |

**Only the OVLT is in the basal forebrain.** The other five are
**diencephalic or hindbrain**. Consumers reconstructing the
**classical lamina terminalis CVO group** must **union** this module
with the hypothalamus (for SFO and ME). Consumers reconstructing the
**full CVO set** must add the **pineal**, **subcommissural organ**,
and **area postrema**.

**The OVLT and SFO are functionally related** — both are **sensory
CVOs** involved in **thirst and osmoregulation**. The OVLT detects
**osmolality** and **angiotensin II**; the SFO detects **angiotensin
II** (and possibly **relaxin**). They are **functionally coupled** —
both project to the **median preoptic nucleus (MnPO)** — but they are
**anatomically separate** and **wired in different partitions**.

Function in the Human Brain
---------------------------
The OVLT's functions are **sensory, osmoregulatory, and
neurosecretory**:

*   **Osmosensing (Primary Sensory Function):** The OVLT's
    **osmosensitive neurons** and **tanycytes** detect **small
    increases in plasma osmolality** (1–2%). This is the **primary
    osmostat** of the forebrain — the OVLT is **more sensitive** to
    osmolality than the SFO (which is primarily an **angiotensin II**
    sensor).

*   **Thirst (Behavioral Function):** The OVLT projects to the
    **median preoptic nucleus (MnPO)** — the **thirst center** of
    the hypothalamus — which drives **water-seeking behavior**. This
    is the **osmotic thirst** pathway. The OVLT also contributes to
    **angiotensin II-driven thirst** (via its angiotensin II
    receptors).

*   **Vasopressin (ADH) Release (Endocrine Function):** The OVLT
    projects to the **paraventricular nucleus (PVN)** and
    **supraoptic nucleus (SON)** of the hypothalamus — the two
    **magnocellular neurosecretory nuclei** that produce **vasopressin
    (ADH)** and **oxytocin**. The OVLT's osmosensory input **drives
    vasopressin release**, promoting **water retention** by the
    kidney.

*   **Fever Generation (Thermoregulatory Function):** Circulating
    **pyrogens** (IL-1, IL-6, TNF-α, LPS) act on the OVLT (and the
    adjacent **median preoptic nucleus**) to induce **PGE2
    synthesis** via **COX-2**. PGE2 acts on **preoptic
    thermoregulatory neurons** to **raise the temperature
    set-point** — producing **fever**. **Antipyretics** work by
    inhibiting COX-2 in this pathway.

*   **Neurosecretion (Neurohemal Function):** The OVLT's
    **neurosecretory neurons** release peptides (including
    **relaxin**) into its **fenestrated capillaries**. The full
    secretory repertoire is **less well characterized** than that of
    the median eminence, but the OVLT is clearly a **neurohemal
    organ**.

*   **Sodium Homeostasis (Homeostatic Function):** The OVLT
    contributes to **sodium balance** via its osmosensing and
    angiotensin II-sensing functions — it is part of the **central
    sodium-regulating circuit** that includes the SFO, the MnPO, the
    PVN, and the SON.

*   **NOT a neural processor.** The OVLT is a **sensor** and a
    **neurohemal interface** — it does **not** process neural
    information in the way a cortical area or a deep nucleus does.
    Its "functions" are **sensory detection**, **peptide
    secretion**, and **driving hypothalamic responses** — not
    **neural computation**.

**The unifying theme:** the OVLT is the **osmostat of the forebrain**
— a **sensory circumventricular organ** that detects **plasma
osmolality**, **angiotensin II**, and **pyrogens** and drives
**thirst**, **vasopressin release**, and **fever**. It is a
**midline** organ, a **neurohemal interface**, and a **sensor** — not
a neural processor.

Associated Disorders
--------------------
OVLT disorders are **osmoregulatory, thermoregulatory, and
circumventricular**:

*   **Adipsia and Essential Hypernatremia — the signature
    disorder:** **OVLT lesions** (from **craniopharyngioma**,
    **anterior communicating artery aneurysm**, **subarachnoid
    hemorrhage**, **hydrocephalus**, or **surgery** in the region)
    disrupt **osmoregulation** and produce **adipsia** (absence of
    thirst) with **hypernatremia**. Patients do **not feel thirsty**
    despite high plasma osmolality, and they may develop
    **hypernatremia** without adequate water intake. **This is the
    OVLT's signature clinical association.**

*   **Central Fever (Thermoregulatory Disorder):** OVLT involvement
    in **subarachnoid hemorrhage**, **traumatic brain injury**, or
    **hypothalamic surgery** can produce **central fever** — fever
    from **CNS injury** rather than infection. **Antipyretics** work
    partly through the OVLT's COX-2 pathway.

*   **SIADH-Like Syndromes (Contrast — Not OVLT-Specific):** In
    **contrast** to adipsia, lesions that **spare the OVLT but
    disrupt hypothalamic osmoregulation** (e.g., some hypothalamic
    tumors) can produce **SIADH** (syndrome of inappropriate
    antidiuretic hormone). The **OVLT itself** is more often
    associated with **adipsia** and **hypernatremia** than with
    SIADH. **Do not conflate the two** — the OVLT drives **water
    intake** (thirst); hypothalamic lesions drive **ADH release**
    (SIADH).

*   **Craniopharyngioma — OVLT Compression:** **Craniopharyngiomas**
    arise in the **suprasellar region**, adjacent to the lamina
    terminalis and OVLT. They can **compress the OVLT** and produce
    **adipsia**, **hypernatremia**, and **obesity** (from hypothalamic
    involvement). **Craniopharyngioma** is a **classic clinical
    context** for OVLT dysfunction.

*   **Subarachnoid Hemorrhage — OVLT Damage:** **Aneurysmal
    subarachnoid hemorrhage** (especially from **ACoA aneurysms**)
    can **damage the OVLT** and the **lamina terminalis**,
    contributing to **hyponatremia** (from **cerebral salt wasting**
    or **SIADH** — the mechanism is debated), **thirst disorders**,
    and **fever**. The **OVLT** is a **recognized site of secondary
    injury** in SAH.

*   **Lamina Terminalis Fenestration (Neurosurgical — Therapeutic):**
    **Surgical fenestration of the lamina terminalis** is a
    **deliberate neurosurgical procedure** used in **aneurysm
    clipping** (to improve CSF flow and reduce hydrocephalus risk)
    and in **third ventriculostomy**. It can **damage the OVLT** as
    a **side effect** — producing **adipsia** or **hypernatremia**
    post-operatively. This is a **therapeutic disruption**, not a
    disorder, but it is **clinically relevant** because the OVLT is
    at risk during the procedure.

*   **Pregnancy-Induced Hypertension (Contrast — OVLT-Adjacent):**
    **Relaxin**, a hormone elevated in pregnancy, acts on the OVLT
    (and SFO) to drive **thirst** and **vasopressin release**. This
    is a **physiological** OVLT function, but it is **relevant to
    pregnancy-induced hypertension (preeclampsia)** — the OVLT's
    relaxin response is part of the **osmoregulatory adaptation** of
    pregnancy.

**What is NOT here:** The OVLT is **not** the substrate for
**Alzheimer's disease** (nucleus basalis), **basal forebrain
amnesia** (septum/DBB), **putaminal hemorrhage** (APS), **Kluver-Bucy
syndrome** (amygdala), or **temporal lobe epilepsy** (hippocampus).
Its clinical footprint is **osmoregulatory** (adipsia,
hypernatremia), **thermoregulatory** (central fever), and
**circumventricular** (neurosecretion, relaxin) — a **distinct
category** from the other basal forebrain children.

Lateralization Notes
--------------------
This is the **left** OVLT module. The OVLT is **midline**, and its
lateralization status is **unique** in the telencephalon:

*   **Midline structure, not a paired one:** The OVLT is a **single
    midline organ** embedded in the **mid-portion of the lamina
    terminalis**. It is **not** a left-right pair like the **anterior
    perforated substance** (paired), the **diagonal band** (paired),
    the **septal nuclei** (paired), the **nucleus basalis** (paired),
    or the **substantia innominata** (paired). The tree wires it under
    ``left/`` and ``right/`` as **structural duplicates** — the two
    modules describe the **same midline organ**, split for structural
    symmetry.

*   **This left module describes the SAME organ as the right
    module.** Unlike every other structure in the basal forebrain,
    where the left and right modules describe **two anatomically
    separate entities** (one per hemisphere), the left OVLT module
    and the right OVLT module describe **one midline organ**. The
    left/right split is a **structural convention**, not an
    anatomical pairing. Consumers that need the **OVLT** should
    resolve it **once** (either side), not twice — the two paths
    point to the same entity.

*   **No Lateralized Function:** The OVLT has **no documented
    left-lateralized or right-lateralized function**. **Osmolality**,
    **thirst**, **vasopressin release**, and **fever** are **midline
    functions** — they are not lateralized.

*   **No Lateralized Syndrome:** Adipsia, hypernatremia, SIADH-like
    syndromes, and central fever are **midline disorders**, not
    lateralized ones. The **left and right modules** describe the
    **same clinical entity**.

**A consumer that assumes "left OVLT = right OVLT" will be
structurally and functionally correct — but the parity here is
STRONGER than mirroring: it is DUPLICATION.** The OVLT is **midline**,
and the left/right modules describe **one anatomical entity** (the
single midline organ) **duplicated** for structural symmetry.
Consumers must **not** assume the left and right modules describe
**anatomically separate structures** — they describe the **same
midline structure**, wired as a left/right pair for the tree's
structural convention.

**This is a midline duplication pair**, like its **parent lamina
terminalis** — and the **only two such pairs in the basal forebrain**.
The **pineal gland** (under epithalamus) and the **subfornical organ**
(under hypothalamus) are also midline, but they are **diencephalic**.
The **lamina terminalis and its OVLT child** are the **only two
midline structures in the telencephalic-wired portion of the
forebrain**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only. But note that
    the **left module describes a midline structure** — the right
    module is a **structural duplicate**, not an anatomically
    separate structure.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../diencephalon/`` or from any other partition. The OVLT's
    relationships to the SFO, ME, pineal, subcommissural organ, area
    postrema, MnPO, PVN, and SON are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **fenestrated
    capillaries**, **neurosecretory neurons**, **tanycytes**, and
    **glial ensheathment** are documented as **prose**, not as
    sub-modules. Consumers must not assume they exist as children;
    resolve cytoarchitectural detail through the references.
*   **Circumventricular organ — sensory sensor, not a neural
    processor.** The OVLT **senses** plasma composition and **drives**
    hypothalamic responses; it does **not** process neural
    information. Consumers must not treat it as a cortical area or a
    deep nucleus.
*   **BBB absent — defining feature, not pathology.** The OVLT's
    **fenestrated capillaries** are **how it works** — they allow
    circulating osmolality, angiotensin II, pyrogens, and relaxin to
    reach its neurons directly. Do not treat "no BBB" as a defect.
*   **Not the lamina terminalis membrane.** The OVLT is **inside**
    the membrane; the membrane is **not** the OVLT. Consumers must
    resolve both — the **membrane** (parent) and the **OVLT** (this
    module) — as distinct structures.
*   **The classical CVO group is split.** Only the **OVLT** is here;
    the **SFO** and **ME** are under the **hypothalamus**; the
    **pineal** is under **epithalamus**; the **subcommissural
    organ** is under **diencephalon**; the **area postrema** is
    under **medulla**. Consumers reconstructing the classical group
    must **union** this module with the hypothalamus for SFO and ME.
*   **Midline structure, not paired.** The left and right modules are
    **structural duplicates** of the **same midline organ**, not
    anatomically separate structures. Consumers must not treat them
    as separate anatomical entities.
*   **Neurohemal organ.** The OVLT is a **neurohemal interface** —
    it releases peptides into fenestrated capillaries. It is not a
    classical endocrine gland.
*   **No ``AREA_PATHS`` hop.** The OVLT is a local leaf under the
    lamina terminalis, not a cross-listed leaf.
*   **No nested cross-listing.** The OVLT has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with right OVLT — parity is DUPLICATION, not
    mirroring.** Left and right OVLT modules are **structurally
    identical** — same leaf status, same cytoarchitectural prose, same
    CVO-group redirects, same osmoregulatory associations. **The
    structural parity is stronger than for paired structures**,
    because the left and right modules describe the **same midline
    organ** — they are **duplicates**, not mirrors.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain.lamina_terminalis import vascular_organ_of_lamina_terminalis

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "basal_forebrain.lamina_terminalis."
        "vascular_organ_of_lamina_terminalis"
    )

**Do not** assume the OVLT is a **paired left-right structure**. It is
a **single midline organ**; the left and right modules are
**structural duplicates**. Consumers that iterate both sides and expect
**two anatomically separate structures** will be **misled**.

**Do not** assume the OVLT is the **lamina terminalis membrane**. The
membrane is the **parent**; the OVLT is the **organ embedded in it**.
Resolve both as distinct structures.

**Do not** assume the OVLT **contains** the SFO, ME, pineal,
subcommissural organ, or area postrema. Those are **other CVOs**
under different partitions. The OVLT is **one CVO**, not the whole
CVO set.

**Do not** assume the OVLT is a **neural processor** or a **classical
endocrine gland**. It is a **sensory circumventricular organ** — a
**sensor** and a **neurohemal interface**.

**Do not** treat "no blood-brain barrier" as **pathology**. The OVLT's
fenestrated capillaries are **how it works** — its **defining
structural feature**.

Iterating the OVLT's (empty) children (recommended consumer
pattern)::

    OVLT_CHILDREN = ()
    # The OVLT is a leaf. Fenestrated capillaries, neurosecretory
    # neurons, and tanycytes are prose, not modules.

Reaching the classical CVO group (recommended consumer pattern)::

    # The classical "lamina terminalis CVO group" is split across
    # the tree. Union it:
    CLASSICAL_LAMINA_TERMINALIS_CVO_GROUP = {
        "telencephalon.left.subcortical.basal_forebrain.lamina_terminalis": (
            "vascular_organ_of_lamina_terminalis",   # OVLT (this module)
        ),
        "forebrain.diencephalon.hypothalamus": (
            "subfornical_organ",   # SFO
            "median_eminence",     # ME
        ),
    }

Reaching the full CVO set (recommended consumer pattern)::

    # The full CVO set spans FIVE partitions. Union them:
    FULL_CVO_SET = {
        "telencephalon.left.subcortical.basal_forebrain.lamina_terminalis": (
            "vascular_organ_of_lamina_terminalis",   # OVLT
        ),
        "forebrain.diencephalon.hypothalamus": (
            "subfornical_organ",   # SFO
            "median_eminence",     # ME
        ),
        "forebrain.diencephalon.epithalamus": (
            "pineal_gland",        # Pineal
        ),
        "forebrain.diencephalon": (
            "subcommissural_organ",   # SCO
        ),
        "hindbrain.myelencephalon.medulla_oblongata": (
            "area_postrema",       # AP
        ),
    }
    # The tree splits them; consumers that want "all CVOs" must union.

Reaching the OVLT's downstream hypothalamic targets (recommended
consumer pattern)::

    # The OVLT projects to hypothalamic nuclei. These are DOWNSTREAM
    # TARGETS, not OVLT children:
    #
    #   diencephalon.hypothalamus.anterior.preoptic_area.median_preoptic_nucleus
    #   diencephalon.hypothalamus.anterior.paraventricular_nucleus
    #   diencephalon.hypothalamus.anterior.supraoptic_nucleus
    #
    # The OVLT SENSES osmolality and DRIVES these nuclei. They are
    # not its children.

Midline-structure iteration (recommended consumer pattern)::

    # The OVLT is MIDLINE. Do NOT iterate it as a bilateral pair.
    # Resolve it ONCE:
    ovlt_path = (
        "telencephalon.cerebral_hemispheres."
        "{either_left_or_right}.subcortical."
        "basal_forebrain.lamina_terminalis."
        "vascular_organ_of_lamina_terminalis"
    )
    # The left and right paths point to the SAME midline organ.
    # Deduplicate before use:
    seen_midline = set()
    for side in ("left", "right"):
        key = "vascular_organ_of_lamina_terminalis"   # midline key
        if key in seen_midline:
            continue
        seen_midline.add(key)
        # ...

Bilateral iteration (recommended consumer pattern — but note the
deduplication)::

    for side in ("left", "right"):
        ovlt_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.lamina_terminalis."
            f"vascular_organ_of_lamina_terminalis"
        )
        # resolve ovlt_path through the memory/recall layer
        # NOTE: the two paths describe the SAME midline organ,
        # duplicated for structural symmetry. Deduplicate as above.

References
----------
*   **Canonical CVO review:** McKinley, M.J., et al. (2003). "The
    sensory circumventricular organs of the mammalian brain."
    *Advances in Anatomy, Embryology and Cell Biology* 172:1–122.
    (Definitive review; OVLT; SFO; AP; osmoregulation; thirst;
    vasopressin; relaxin.)
*   **Sensory CVOs:** Johnson, A.K., Gross, P.M. (1993). "Sensory
    circumventricular organs and brain homeostatic pathways." *FASEB
    Journal* 7:678–686. (OVLT, SFO, and AP as sensory CVOs;
    osmoregulation; fever.)
*   **OVLT and angiotensin II:** Simpson, J.B. (1981). "The
    circumventricular organs and the central actions of angiotensin
    II." *Neuroendocrinology* 32:248–256. (OVLT as a central site of
    angiotensin II action for thirst.)
*   **OVLT and osmosensing:** Bourque, C.W. (2008). "Central
    mechanisms of osmoregulation." *Experimental Physiology*
    93:165–174. (OVLT osmosensitive neurons; tanycytes;
    osmoregulation.)
*   **OVLT and fever:** Stitt, J.T. (1985). "Evidence for the
    involvement of the organum vasculosum laminae terminalis in the
    febrile responses of rabbits and rats." *Journal of Physiology*
    368:501–511. (OVLT as a site of prostaglandin E2 action for
    fever.)
*   **OVLT and relaxin:** McKinley, M.J., et al. (1997). "Relaxin
    and the central control of osmoregulation." (OVLT and SFO as
    relaxin targets; pregnancy osmoregulation.)
*   **Adipsia and hypernatremia:** Robertson, G.L. (1987). "Physiology
    of ADH secretion and thirst." In *Clinical Neuroendocrinology*
    (Martin, J.B., Reichlin, S., Bick, K.L., eds.). (Osmoregulatory
    disorders; adipsia; hypernatremia; distinction from SIADH.)
*   **Craniopharyngioma and osmoregulatory dysfunction:** Sklar, C.A.
    (1994). "Craniopharyngioma: endocrine sequelae of treatment."
    *Pediatric Neurosurgery* 21:120–123. (Adipsia and hypernatremia
    after craniopharyngioma treatment.)
*   **SAH and OVLT:** Diringer, M.N. (2003). "Management of sodium
    abnormalities following subarachnoid hemorrhage."
    *Neurosurgery Clinics of North America* 14:427–438.
    (Hyponatremia after SAH; OVLT and hypothalamic involvement.)
*   **Lamina terminalis fenestration:** Komotar, R.J., et al. (2008).
    "The role of lamina terminalis fenestration in reducing shunt-
    dependent hydrocephalus following aneurysmal subarachnoid
    hemorrhage." *Journal of Neurosurgery* 108:1001–1007. (Surgical
    fenestration of the lamina terminalis; OVLT at risk.)
*   **CVO overview:** Ganong, W.F. (2000). "Circumventricular organs:
    definition and role in the regulation of endocrine and autonomic
    function." *Clinical and Experimental Pharmacology and
    Physiology* 27:422–427. (Overview of the CVO group including
    OVLT, SFO, ME, pineal, subcommissural organ, area postrema.)
*   **Tanycytes:** Rodríguez, E.M., et al. (2005). "Hypothalamic
    tanycytes: a key component of brain-endocrine interaction."
    *International Review of Cytology* 247:89–164. (Tanycyte
    biology; OVLT and median eminence.)
*   **Neurosecretion:** Duvernoy, H.M., Risold, P.-Y. (2007). *The
    Human Hippocampus*, 3rd ed. (Periventricular and circumventricular
    anatomy; neurohemal organs in overview.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (OVLT in overview.)
*   NeuroNames — Organum vasculosum of the lamina terminalis (left);
    FMA — Vascular organ of the lamina terminalis (left member).
    Note: the OVLT is a **midline structure**, and the FMA "left
    member" designation is a structural convention, not an anatomical
    pairing.
"""