"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain.nucleus_basalis
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── basal_forebrain
                    └── nucleus_basalis   <-- THIS MODULE

**Primary synonym:** Nucleus basalis of Meynert (NBM, NB); basal
nucleus of Meynert; magnocellular nucleus basalis; nucleus basalis
telencephali (classical).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**magnocellular cholinergic nucleus** — the **principal source of
cortical acetylcholine**.
**Part of:** The **basal forebrain cholinergic system** (with the
medial septal nucleus and the diagonal band of Broca) — and, more
broadly, the **cortically projecting cholinergic system**.
**Structural parent:** ``.../left/subcortical/basal_forebrain/`` →
**direct child** of the basal forebrain container.
**Structural children:** **None.** This is a **leaf** module. The
**magnocellular cholinergic neurons**, **non-cholinergic neurons**,
and **NGF-receptor (TrkA)-positive populations** are documented as
**prose**, not as structural children.
**Boundary status (NOT the "nucleus basalis of the diagonal band"):**
**Boundary case — the name is a historical source of confusion, and
the "nucleus basalis of the diagonal band" is a DIFFERENT structure
(a sibling).** Older literature sometimes uses **"nucleus basalis of
the diagonal band"** for the **nucleus of the diagonal band (NDB)** —
the **vertical limb** of the **diagonal band of Broca**
(``.../basal_forebrain/diagonal_band_of_broca/``). **That is not this
structure.** The **nucleus basalis of Meynert** (this module) is the
**cortically projecting** cholinergic nucleus; the **NDB** is the
**septohippocampal** cholinergic nucleus. They are **siblings** under
the basal forebrain, both cholinergic, but **anatomically and
functionally distinct**. Consumers must not conflate them — and must
not resolve the "nucleus basalis of the diagonal band" through this
module.
**Boundary status (embedded in the substantia innominata, but a
sibling — NOT a child):** **Boundary case — the nucleus basalis is
embedded in the substantia innominata, but the substantia innominata
is a SIBLING, not a parent.** The **nucleus basalis** lies **within**
the **substantia innominata** — the grey-matter region between the
globus pallidus and the anterior perforated substance. But the tree
wires **both as siblings** under the basal forebrain:
``substantia_innominata/`` and ``nucleus_basalis/``. The nucleus
basalis is **not** a child of the substantia innominata, and the
substantia innominata is **not** a container for it. Consumers must
not resolve the nucleus basalis as a substantia-innominata child — and
must not expect the substantia innominata module to contain it.
**Boundary status (sibling of the septal nuclei and diagonal band):**
**Boundary case — sibling of the other two cholinergic nuclei, not a
parent or child.** The nucleus basalis, the **medial septal nucleus**
(under ``septal_nuclei/medial_septal_nuclei/``), and the **diagonal
band of Broca** (``diagonal_band_of_broca/``) are the **three
cholinergic nuclei** of the basal forebrain — the **basal forebrain
cholinergic system**. The tree wires all three as **siblings**.
Consumers that need the **basal forebrain cholinergic system** as a
unit must **union** the three leaves — the nucleus basalis is **one of
three**, not the whole system.
**Boundary status (NOT rhinencephalic, despite amygdala and some
cortical projections):** **Boundary case — the nucleus basalis
projects to the amygdala and to olfactory cortex, but it is NOT a
rhinencephalon structure.** The nucleus basalis provides
**cholinergic input** to the **amygdala** and to **olfactory cortical
areas** (piriform, orbitofrontal), among many other targets. This is
**cholinergic modulation**, not **olfactory processing**. The nucleus
basalis is a **basal forebrain** structure, not a rhinencephalon leaf.
Consumers must not resolve it through ``rhinencephalon/`` — it is
**not** an olfactory structure, despite projecting to olfactory
targets.
**Boundary status (NOT the amygdala):** **Boundary case — the nucleus
basalis projects to the amygdala but is not the amygdala.** The
nucleus basalis provides **cholinergic input** to the **amygdala**,
where it modulates **emotional processing** and **memory
consolidation**. But the nucleus basalis is **not** an amygdala
structure, **not** in the medial temporal lobe, and **not** adjacent to
the amygdala. It is a **ventral basal forebrain nucleus**.
Consumers must not resolve the amygdala through the nucleus basalis,
and must not import **amygdala-lateralization claims** into the
nucleus basalis — its cholinergic projection to the amygdala is
**bilateral** and **not lateralized**.
**Boundary status ("magnocellular" — NOT the hypothalamic
magnocellular neurons):** **Boundary case — "magnocellular" describes
cell size, not a hypothalamic identity.** The nucleus basalis is
called the **magnocellular nucleus basalis** because its **cholinergic
neurons are large** (~30–50 μm). This "magnocellular" label is
**not** the same as the **magnocellular neurosecretory neurons** of
the **paraventricular** and **supraoptic** nuclei of the hypothalamus
(which produce **vasopressin** and **oxytocin**). The two
"magnocellular" populations are **anatomically and functionally
distinct**. Consumers must not conflate them.

Overview
--------
The nucleus basalis of Meynert is the **principal source of cortical
acetylcholine** and the **most clinically prominent** of the basal
forebrain cholinergic nuclei. It is a **magnocellular cholinergic
nucleus** embedded in the **substantia innominata**, on the **ventral
surface of the basal forebrain**, medial to the **globus pallidus**
and posterior to the **anterior perforated substance**. It contains
**large cholinergic projection neurons** (~90,000–200,000 per side in
humans, depending on counting method) that project to the **entire
neocortex**, the **amygdala**, and (to a lesser extent) the
**thalamus** and **brainstem**.

**The nucleus basalis is the "cortical acetylcholine faucet."** It
provides roughly **70–80%** of the **cortical cholinergic
innervation** — the diagonal band and medial septal nucleus provide
most of the rest, primarily to the **hippocampus** and **olfactory
bulb**. Its cholinergic projections **modulate cortical excitability,
attention, learning, and plasticity** — it is the **neuromodulatory
substrate** for **arousal, vigilance, and memory encoding**.

**The nucleus basalis is the "Alzheimer's nucleus."** Its
**cholinergic neurons** are among the **earliest and most severely
affected** in **Alzheimer's disease** — loss of **60–90%** of nucleus
basalis neurons is a **pathological hallmark** of advanced AD, and the
resulting **cortical cholinergic deficit** is the basis of the
**cholinergic hypothesis** and of **cholinesterase-inhibitor therapy**
(donepezil, rivastigmine, galantamine). **This is the nucleus
basalis's signature clinical association** — more than any other
basal forebrain structure, the nucleus basalis is **defined clinically
by its role in Alzheimer's disease**.

**The nucleus basalis is a paired structure.** Each hemisphere has its
own nucleus basalis, projecting primarily to its **ipsilateral**
cortex. The two are **bilaterally symmetric** and **functionally
non-lateralized** — Alzheimer's cholinergic loss is **bilateral**, and
no lateralized syndrome has been demonstrated. See *Lateralization
Notes*.

**The nucleus basalis is NOT the diagonal band's NDB.** The "nucleus
basalis of the diagonal band" (NDB) is the **vertical limb of the
diagonal band** — a **sibling** under the basal forebrain. It is the
**septohippocampal** cholinergic nucleus, projecting primarily to the
**hippocampus** (via the fornix), not to the cortex. The **nucleus
basalis of Meynert** (this module) is the **cortically projecting**
cholinergic nucleus. The two are **siblings**, **both cholinergic**,
but **functionally distinct**.

**The nucleus basalis is NOT the substantia innominata.** It is
**embedded in** the substantia innominata — the substantia innominata
is the **grey-matter region** that contains the nucleus basalis, the
**magnocellular preoptic nucleus**, and **scattered cholinergic and
GABAergic neurons**. The tree wires **both as siblings** under the
basal forebrain. Consumers must not resolve the nucleus basalis as a
substantia-innominata child.

Cytoarchitecture (prose, not structural children)
-------------------------------------------------
The nucleus basalis has **no structural children** in the tree, but
its **cellular composition** is distinctive:

*   **Magnocellular cholinergic neurons** — the **defining
    population**. Large neurons (~30–50 μm) that synthesize
    **acetylcholine** (via **choline acetyltransferase, ChAT**) and
    project to the **neocortex** and **amygdala**. They express
    **TrkA** (the **NGF receptor**) and **p75** (the **low-affinity
    neurotrophin receptor**) — **NGF-responsive** neurons, which is
    why **NGF** is a **survival factor** for them and why **NGF
    deprivation** is implicated in their degeneration in Alzheimer's.

*   **Non-cholinergic neurons** — the nucleus basalis also contains
    **GABAergic**, **peptidergic**, and **other** non-cholinergic
    neurons (roughly **10–30%** of the population depending on
    species and region). These are **less well characterized** than
    the cholinergic neurons, but they contribute to the nucleus's
    **modulatory output**.

*   **Estrogen receptor-positive neurons** — a **subpopulation** of
    nucleus basalis neurons expresses **estrogen receptors**
    (ERα, ERβ). This is one basis for the **sex difference** in
    Alzheimer's risk (women have higher AD risk, partly attributed to
    **estrogen loss** after menopause) and for the **neuroprotective**
    effects of estrogen on cholinergic neurons.

*   **Subdivisions** — the nucleus basalis is classically divided into
    **subdivisions** (anterior, intermediate, posterior; or
    **Ch4** subdivisions in the Mesulam nomenclature: Ch4am, Ch4al,
    Ch4i, Ch4p). These subdivisions project to **different cortical
    regions** — anterior to **frontal** cortex, intermediate to
    **parietal** and **temporal**, posterior to **occipital** and
    **medial temporal** — but they are **cytoarchitecturally
    continuous** and are documented as **prose**, not as sub-modules.

**These cellular features are prose, not structural children.** The
tree does **not** wire the cholinergic, GABAergic, peptidergic, or
estrogen-receptor-positive populations as sub-modules, and does **not**
wire the Ch4 subdivisions. Consumers that need subdivision-level
resolution should consult the references, not the tree.

The Nucleus Basalis / Substantia Innominata Boundary
----------------------------------------------------
This is the **most commonly confused** boundary for consumers:

*   **Substantia innominata** (``substantia_innominata/``) — the
    **grey-matter region** between the globus pallidus and the
    anterior perforated substance. Its **boundaries are
    cytoarchitecturally graded**, and it contains **scattered
    cholinergic and GABAergic neurons** in addition to the nucleus
    basalis.

*   **Nucleus basalis** (this module) — the **magnocellular cholinergic
    nucleus** embedded **within** the substantia innominata. It is
    the **largest and most distinctive** cellular population within
    the region, but it is **not** coextensive with the region — the
    substantia innominata is **larger** and contains **more** than the
    nucleus basalis.

**Both are siblings under the basal forebrain.** The tree wires them
separately. Consumers that need the **cholinergic nucleus** resolve
the nucleus basalis; consumers that need the **grey-matter region**
resolve the substantia innominata. The **nucleus basalis is not a
child of the substantia innominata** — it is a **sibling** that
happens to be **embedded** in the substantia innominata's territory.

The Nucleus Basalis / Other Cholinergic Nuclei Boundary
-------------------------------------------------------
The nucleus basalis is **one of three** basal forebrain cholinergic
nuclei:

| Cholinergic nucleus | Tree path | Primary targets |
|---|---|---|
| **Nucleus basalis of Meynert** (this module) | `subcortical/basal_forebrain/nucleus_basalis/` | **Neocortex**, **amygdala**, thalamus |
| **Medial septal nucleus** | `subcortical/basal_forebrain/septal_nuclei/medial_septal_nuclei/` | **Hippocampus** (via fornix), olfactory bulb |
| **Diagonal band of Broca** | `subcortical/basal_forebrain/diagonal_band_of_broca/` | **Hippocampus** (vertical limb, NDB), **olfactory bulb** (horizontal limb), **cortex** (some) |

**All three are siblings under the basal forebrain.** Consumers that
need the **basal forebrain cholinergic system** as a unit must
**union** the three leaves. The nucleus basalis is **the cortical
one**; the medial septal nucleus and diagonal band are the
**hippocampal and olfactory-bulb** ones (with some overlap in cortical
projection).

Function in the Human Brain
---------------------------
The nucleus basalis's functions are **cholinergic modulation of
cortex and amygdala**:

*   **Cortical Activation and Arousal (Primary Function):** The
    nucleus basalis's **cholinergic projections** to the **entire
    neocortex** modulate **cortical excitability, arousal, and
    vigilance**. Its **firing** is highest during **waking and
    attention-demanding tasks**, and it is **silent during slow-wave
    sleep** — it is the **neuromodulatory substrate** for **cortical
    activation**.

*   **Attention and Learning (Modulatory Function):** The nucleus
    basalis's cholinergic input to the **prefrontal cortex** and
    **sensory cortices** modulates **attention**, **sensory
    processing**, and **learning**. Its **lesion** produces
    **attentional deficits** in animal models; its **stimulation**
    enhances **cortical plasticity**.

*   **Memory Consolidation (Amygdala and Cortical Function):** The
    nucleus basalis's cholinergic input to the **amygdala** and
    **medial temporal cortex** contributes to **emotional memory
    consolidation** — **emotional arousal** enhances memory partly
    via **cholinergic modulation** of the amygdala and hippocampus.
    This is why **emotional events** are remembered better than
    neutral ones.

*   **Cortical Plasticity (Developmental and Adult Function):**
    Nucleus basalis cholinergic input is **required** for
    **experience-dependent cortical plasticity** — for example, in
    **barrel cortex** (rodent) and **visual cortex** (monocular
    deprivation). Its cholinergic signal is a **permissive** signal
    for **cortical reorganization**.

*   **Cortical Blood Flow (Vascular Function):** The nucleus basalis
    provides **cholinergic innervation to cortical blood vessels**,
    contributing to **activity-dependent cerebral blood flow** —
    the basis of the **BOLD signal** in fMRI. This is a **vascular**
    function, not a neural one, but it is clinically relevant to
    **neuroimaging interpretation**.

*   **NOT a cortical processor.** The nucleus basalis **modulates**
    the cortex; it does **not** process cortical information. Its
    cholinergic signal is a **neuromodulatory broadcast** — it
    **tunes** cortical circuits but does **not** compute them.
    Consumers must not resolve the nucleus basalis as a cortical
    area or as a memory structure; it is a **modulatory nucleus**.

**The unifying theme:** the nucleus basalis is the **cortical
acetylcholine faucet** — a **magnocellular cholinergic nucleus** that
provides the **neuromodulatory substrate** for **arousal, attention,
learning, memory consolidation, and cortical plasticity**. Its **loss
in Alzheimer's disease** is the basis of the **cholinergic
hypothesis** and of **cholinesterase-inhibitor therapy**.

Associated Disorders
--------------------
Nucleus basalis disorders are **cholinergic**, **cognitive**, and
**neurodegenerative**:

*   **Alzheimer's Disease — Cholinergic Loss (the signature
    disorder):** Loss of **60–90%** of nucleus basalis neurons is a
    **pathological hallmark** of advanced Alzheimer's disease. The
    resulting **cortical cholinergic deficit** is the basis of the
    **cholinergic hypothesis** and of **cholinesterase-inhibitor
    therapy** (donepezil, rivastigmine, galantamine). The nucleus
    basalis is **the most famous "Alzheimer's nucleus"** in the
    brain.

*   **Parkinson's Disease — Cholinergic Loss:** Nucleus basalis
    cholinergic loss is **less severe than in Alzheimer's** (roughly
    **30–50%**), but it contributes to **cognitive impairment**,
    **gait dysfunction**, and **falls** in PD — and **cholinergic
    deficits** are a **therapeutic target** in PD dementia.

*   **Lewy Body Dementia (LBD):** Nucleus basalis cholinergic loss in
    LBD is **more severe than in Alzheimer's** (roughly **70–80%** or
    more), and it is a **major contributor** to the **cognitive
    fluctuations** and **visual hallucinations** of LBD.
    **Cholinesterase inhibitors** are **more effective** in LBD than
    in Alzheimer's, consistent with the more severe cholinergic
    deficit.

*   **Deep Brain Stimulation (DBS) for Alzheimer's — Therapeutic:**
    **DBS of the nucleus basalis** has been investigated as an
    **experimental therapy** for Alzheimer's disease, based on the
    rationale that **stimulating residual nucleus basalis neurons**
    may **enhance cortical cholinergic tone**. Results have been
    **mixed** (some early promise, some negative), but the approach
    is still **under investigation** and is a **clinically relevant**
    application of nucleus basalis anatomy.

*   **Schizophrenia — Cholinergic Deficit (Contested):** Some studies
    report **decreased nucleus basalis cholinergic markers** in
    schizophrenia, possibly contributing to **cognitive symptoms**
    (attention, working memory). The evidence is **mixed**, and
    **cholinergic treatments** (e.g., **xanomeline**, a muscarinic
    agonist) have shown some efficacy in **cognitive and psychotic
    symptoms** — but the role of the nucleus basalis in schizophrenia
    is **not established**.

*   **Vascular Dementia — Cholinergic Deficit:** **Vascular dementia**
    can involve **nucleus basalis cholinergic loss** (via ischemia of
    the substantia innominata region), contributing to **cognitive
    impairment**. **Cholinesterase inhibitors** are sometimes used,
    with **modest** benefit.

*   **Attention and Arousal Deficits (Animal Models):** **Nucleus
    basalis lesions** in animals produce **attentional deficits**,
    **impaired cortical plasticity**, and **reduced cortical
    cholinergic tone** — findings that support its role in **attention
    and learning**.

**What is NOT here:** The nucleus basalis is **not** the substrate for
**basal forebrain amnesia** (septum/DBB), **temporal lobe epilepsy**
(hippocampus), **Kluver-Bucy syndrome** (amygdala), or **Wernicke's
aphasia** (BA22). Its clinical footprint is **cholinergic-cognitive**
(Alzheimer's, LBD, PD dementia), **arousal-attention** (animal
models), and **therapeutic** (DBS trials). It is the **cortical
cholinergic nucleus** — not the septohippocampal or amygdala one.

Lateralization Notes
--------------------
This is the **left** nucleus basalis module. The nucleus basalis is
**bilaterally symmetric** and **functionally non-lateralized**:

*   **Bilateral Cortical Projection:** Each nucleus basalis projects
    primarily to its **ipsilateral** neocortex and amygdala. The two
    sides are **functionally symmetric** for cortical cholinergic
    modulation.

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the nucleus basalis has **no documented left-lateralized or
    right-lateralized function**. **Alzheimer's** cholinergic loss is
    **bilateral**; **cortical arousal** is **bilateral**.

*   **Amygdala-Projection Asymmetry (Contrast):** The **right
    amygdala** is sometimes reported as more involved in **fear
    processing** than the left, and the nucleus basalis provides
    **cholinergic input to the amygdala** — but that projection is
    **bilateral** and **not lateralized**. The **right amygdala's fear
    association does not transfer** to the nucleus basalis. Consumers
    must **not** import amygdala-lateralization claims into the
    nucleus basalis — it is a **bilateral cholinergic modulator**, not
    a lateralized emotional structure.

*   **No Cortical-Level Asymmetries:** The subtle left-verbal /
    right-emotional asymmetries reported for **orbitofrontal** and
    **insular** odor processing are **cortical-level** phenomena
    **downstream** of the nucleus basalis. Do not import them into the
    nucleus basalis.

**A consumer that assumes "left nucleus basalis = right nucleus
basalis" will be structurally and functionally correct** — the two
sides are symmetric, no lateralized function has been demonstrated,
and the nucleus basalis's **bilateral cholinergic projections** are
the anatomical substrate of its **bilateral functions**. This is a
**strict-mirror pair**: the nucleus basalis carries **no
right-side-specific misconception** a consumer is likely to import
(despite its amygdala projection, it is not adjacent to the amygdala
and not "over" it), so the right module is a **word-for-word mirror**
of the left.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``rhinencephalon/``, ``.../diencephalon/``, or the
    other subcortical containers. The nucleus basalis's projections
    to the neocortex, amygdala, thalamus, and brainstem are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **cholinergic**,
    **GABAergic**, **peptidergic**, and **estrogen-receptor-positive**
    neuronal populations are documented as **prose**, not as
    sub-modules. The **Ch4 subdivisions** (Ch4am, Ch4al, Ch4i, Ch4p)
    are documented as **prose**, not as sub-modules. Consumers must
    not assume any exist as children; resolve subdivision-level detail
    through the references.
*   **NOT the "nucleus basalis of the diagonal band" (NDB).** The NDB
    is the **vertical limb of the diagonal band**
    (``diagonal_band_of_broca/``), a **sibling**. Consumers must not
    resolve the NDB through this module, or this module through the
    NDB.
*   **NOT the substantia innominata.** The nucleus basalis is
    **embedded in** the substantia innominata, but the substantia
    innominata is a **sibling** (``substantia_innominata/``), not a
    parent. Consumers must not resolve the nucleus basalis as a
    substantia-innominata child.
*   **Sibling of the other two cholinergic nuclei.** The medial
    septal nucleus and the diagonal band are **siblings** under the
    basal forebrain. Consumers that need the **basal forebrain
    cholinergic system** as a unit must **union** the three leaves.
*   **NOT rhinencephalic, despite amygdala and cortical projections.**
    The nucleus basalis projects to the amygdala and olfactory cortex,
    but it is a **basal forebrain** structure, not a rhinencephalon
    leaf.
*   **NOT the amygdala, despite amygdala projection.** The nucleus
    basalis provides cholinergic input to the amygdala, but it is
    **not** an amygdala structure and **not** adjacent to the amygdala.
    Do not import **amygdala-lateralization claims** into the nucleus
    basalis.
*   **"Magnocellular" is a cell-size label, not a hypothalamic
    identity.** The nucleus basalis's **magnocellular** cholinergic
    neurons are **not** the **magnocellular neurosecretory neurons** of
    the paraventricular and supraoptic nuclei. Do not conflate them.
*   **No ``AREA_PATHS`` hop.** The nucleus basalis is a local leaf
    under the basal forebrain, not a cross-listed leaf.
*   **No nested cross-listing.** The nucleus basalis has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with right nucleus basalis.** Left and right
    nucleus basalis modules are **structurally identical** — same leaf
    status, same cytoarchitectural prose, same NDB/substantia
    innominata sibling notes, same basal-forebrain-cholinergic union
    pattern, same non-lateralized caveat.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain import nucleus_basalis

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "basal_forebrain.nucleus_basalis"
    )

**Do not** assume the nucleus basalis is the **"nucleus basalis of
the diagonal band" (NDB)**. The NDB is the **vertical limb of the
diagonal band** (``diagonal_band_of_broca/``), a **sibling**. This
module is the **nucleus basalis of Meynert** — the **cortically
projecting** cholinergic nucleus. They are **different structures**.

**Do not** assume the nucleus basalis is a **child of the substantia
innominata**. It is **embedded in** the substantia innominata, but the
substantia innominata is a **sibling** under the basal forebrain. The
nucleus basalis is **not** a substantia-innominata child.

**Do not** assume the nucleus basalis is **rhinencephalic**. It
projects to the amygdala and olfactory cortex, but it is a **basal
forebrain** cholinergic nucleus, not a rhinencephalon leaf.

**Do not** assume the nucleus basalis is **the amygdala**. It projects
to the amygdala, but it is **not** an amygdala structure and **not**
adjacent to the amygdala.

**Do not** import **amygdala-lateralization claims** into the nucleus
basalis. Its cholinergic projection to the amygdala is **bilateral**
and **not lateralized**.

**Do not** conflate **"magnocellular"** nucleus basalis with the
**magnocellular neurosecretory neurons** of the hypothalamus. The two
"magnocellular" populations are **different structures**.

**Do not** assume the nucleus basalis has structural children. It is
a **leaf**. The **Ch4 subdivisions** (Ch4am, Ch4al, Ch4i, Ch4p) and
the **neuronal populations** (cholinergic, GABAergic, peptidergic,
ER-positive) are **prose only** — they are not wired as modules.

Iterating the nucleus basalis's (empty) children (recommended
consumer pattern)::

    NB_CHILDREN = ()
    # The nucleus basalis is a leaf. Ch4 subdivisions and neuronal
    # populations are prose, not modules.

Reconstructing the basal forebrain cholinergic system (recommended
consumer pattern)::

    # The basal forebrain cholinergic system spans THREE sibling
    # leaves. Union them:
    BASAL_FOREBRAIN_CHOLINERGIC = (
        "subcortical.basal_forebrain.nucleus_basalis",
        "subcortical.basal_forebrain.septal_nuclei.medial_septal_nuclei",
        "subcortical.basal_forebrain.diagonal_band_of_broca",
    )
    # The nucleus basalis is the CORTICAL one; the medial septal
    # nucleus and diagonal band are the HIPPOCAMPAL and
    # OLFACTORY-BULB ones (with some cortical overlap).

Reaching the nucleus basalis's downstream targets (recommended
consumer pattern)::

    # The nucleus basalis projects to structures documented elsewhere
    # in the tree. Resolve them at their own paths:
    #
    #   cortex.frontal.cortex.prefrontal_cortex
    #   cortex.parietal.cortex
    #   cortex.temporal.cortex
    #   cortex.occipital.cortex
    #   subcortical.medial_temporal_lobe.amygdala
    #   diencephalon.thalamus
    #
    # These are NOT nucleus basalis children. They are downstream
    # targets.

Reaching the substantia innominata (recommended consumer pattern)::

    # The substantia innominata is a SIBLING of the nucleus basalis,
    # not its parent. Resolve it at its own path:
    #
    #   subcortical.basal_forebrain.substantia_innominata
    #
    # The nucleus basalis is EMBEDDED in the substantia innominata
    # territory, but the two are separate leaves.

Reaching the NDB (the "nucleus basalis of the diagonal band")
(recommended consumer pattern)::

    # The "nucleus basalis of the diagonal band" (NDB) is the
    # VERTICAL LIMB of the diagonal band, NOT this module. Resolve it:
    #
    #   subcortical.basal_forebrain.diagonal_band_of_broca
    #
    # The NDB is the SEPTohippocampal cholinergic nucleus; the
    # nucleus basalis (this module) is the CORTICAL cholinergic
    # nucleus.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        nb_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.nucleus_basalis"
        )
        # resolve nb_path through the memory/recall layer

References
----------
*   **Canonical cholinergic anatomy:** Mesulam, M.-M., Mufson,
    E.J., Levey, A.I., Wainer, B.H. (1983). "Cholinergic innervation
    of cortex by the basal forebrain: cytochemistry and cortical
    connections of the septal area, diagonal band nuclei, nucleus
    basalis (substantia innominata), and hypothalamus in the rhesus
    monkey." *Journal of Comparative Neurology* 214:170–197.
    (Definitive cholinergic anatomy; nucleus basalis as the cortical
    source.)
*   **Original description:** Meynert, T. (1872). "Vom Gehirne der
    Säugethiere." In *Handbuch der Lehre von den Geweben des
    Menschen und der Thiere* (Stricker, S., ed.). (Original
    description of the nucleus basalis.)
*   **Alzheimer's cholinergic hypothesis:** Whitehouse, P.J., et al.
    (1982). "Alzheimer's disease and senile dementia: loss of
    neurons in the basal forebrain." *Science* 215:1237–1239.
    (Nucleus basalis loss in Alzheimer's; basis of the cholinergic
    hypothesis.)
*   **Cholinesterase inhibitors:** Rogers, S.L., Friedhoff, L.T.
    (1996). "The efficacy and safety of donepezil in patients with
    Alzheimer's disease." *Dementia* 7:293–303. (Clinical trial
    evidence for cholinesterase inhibitors.)
*   **Lewy body dementia cholinergic loss:** Perry, E.K., et al.
    (1994). "Cholinergic and dopaminergic activities in senile
    dementia of Lewy body type." *Alzheimer Disease and Associated
    Disorders* 8:48–56. (More severe nucleus basalis loss in LBD than
    AD.)
*   **Parkinson's cholinergic loss:** Bohnen, N.I., et al. (2003).
    "Cortical cholinergic function is more severely affected in
    parkinsonian dementia than in Alzheimer disease."
    *Archives of Neurology* 60:1745–1748. (Nucleus basalis
    cholinergic loss in PD dementia.)
*   **DBS of nucleus basalis:** Kuhn, J., et al. (2015). "Deep brain
    stimulation of the nucleus basalis of Meynert in Alzheimer's
    dementia." *Molecular Psychiatry* 20:353–360. (Experimental DBS
    trial for Alzheimer's.)
*   **NGF and nucleus basalis:** Hefti, F. (1986). "Nerve growth
    factor promotes survival of septal cholinergic neurons after
    fimbrial transections." *Journal of Neuroscience* 6:2155–2162.
    (NGF as a survival factor for basal forebrain cholinergic
    neurons.)
*   **Estrogen receptors on nucleus basalis:** Toran-Allerand, C.D.,
    et al. (1992). "Estrogen receptors colocalize with low-affinity
    nerve growth factor receptors in cholinergic neurons of the
    basal forebrain." *PNAS* 89:4668–4672. (ER and p75
    co-expression in nucleus basalis.)
*   **Cortical plasticity:** Bear, M.F., Singer, W. (1986).
    "Modulation of visual cortical plasticity by acetylcholine and
    noradrenaline." *Nature* 320:172–176. (Cholinergic modulation of
    cortical plasticity.)
*   **Cortical blood flow:** Sato, A., Sato, Y. (1992). "Regulation
    of regional cerebral blood flow by cholinergic fibers
    originating in the basal forebrain." *Neuroscience Research*
    14:242–274. (Cholinergic innervation of cortical vessels.)
*   **Mesulam nomenclature:** Mesulam, M.-M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the
    rat: an overview based on an alternative nomenclature (Ch1–Ch6)."
    *Neuroscience* 10:1185–1201. (Ch4 subdivisions of nucleus
    basalis.)
*   **Schizophrenia cholinergic deficit (contested):** Raedler, T.J.,
    et al. (2003). "In vivo determination of muscarinic
    acetylcholine receptor availability in schizophrenia."
    *American Journal of Psychiatry* 160:118–127. (M1 receptor
    deficits in schizophrenia; contested.)
*   **Basal forebrain amnesia:** Damasio, A.R., Graff-Radford, N.R.,
    Eslinger, P.J., Damasio, H., Kassell, N. (1985). "Amnesia
    following basal forebrain lesions." *Archives of Neurology*
    42:263–271. (Basal forebrain amnesia; distinct from nucleus
    basalis cholinergic loss.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Nucleus basalis in overview.)
*   NeuroNames — Nucleus basalis of Meynert (left); FMA — Nucleus
    basalis of Meynert (left member).
"""