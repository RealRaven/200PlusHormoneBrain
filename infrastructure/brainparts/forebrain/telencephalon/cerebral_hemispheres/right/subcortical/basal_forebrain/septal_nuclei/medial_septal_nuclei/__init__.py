"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain.septal_nuclei.medial_septal_nuclei
==========================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_forebrain
                    └── septal_nuclei
                        └── medial_septal_nuclei   <-- THIS MODULE

**Primary synonym:** Medial septal nucleus (MSN, MS); medial septum;
nucleus septalis medialis; medial septal area; "the medial septum."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**magnocellular cholinergic nucleus** — one of the **three basal
forebrain cholinergic nuclei** (with the diagonal band and nucleus
basalis).
**Part of:** The **basal forebrain cholinergic system** (with the
diagonal band and nucleus basalis) and the **septohippocampal
cholinergic system** (with the **vertical limb of the diagonal
band**). Also the **medial olfactory stria target** (one of the five
rhinencephalon-excluded structures).
**Structural parent:** ``.../basal_forebrain/septal_nuclei/`` →
**only wired child** of the septal nuclei container.
**Structural children:** **None.** This is a **leaf** module. The
**cholinergic** and **GABAergic** neuronal populations, and the
**septohippocampal** and **septobulbar** projection pathways, are
documented as **prose**, not as structural children.
**Boundary status (NOT the lateral septal nucleus):** **Boundary
case — the medial septal nucleus is the CHOLINERGIC component; the
LATERAL septal nucleus is the GABAERGIC component and is a
DOCUMENTED GAP (not wired).** The septal region classically has
**two major components**: the **medial** septal nucleus (this module
— cholinergic, projects to hippocampus and olfactory bulb) and the
**lateral** septal nucleus (GABAergic, projects to hypothalamus and
brainstem; involved in reward, anxiety, fear, and social behavior).
The tree wires **only the medial** nucleus — the **lateral** septal
nucleus is **not in the tree dump** (see the parent `septal_nuclei`
module's *Boundary status (ONE-child container)*). Consumers must
**not** conflate the two: they are **cytoarchitecturally and
functionally distinct**, and the **lateral** component's functions
are documented as **prose in the parent**, not as a child here.
**Boundary status (NOT the diagonal band — sibling):** **Boundary
case — the diagonal band of Broca is a SIBLING, not a parent or
child.** The **medial septal nucleus** and the **vertical limb of
the diagonal band (NDB)** are **anatomically adjacent** and
**functionally coupled** — together they form the **septohippocampal
cholinergic system** (the two cholinergic sources to the
hippocampus). The tree wires them as **siblings** under the basal
forebrain: ``septal_nuclei/medial_septal_nuclei/`` and
``diagonal_band_of_broca/``. The medial septal nucleus is **not** a
child of the diagonal band, and the diagonal band is **not** a child
of the septal nuclei. Consumers that need the **septohippocampal
cholinergic system** as a unit must **union** the two leaves — the
medial septal nucleus is **one of two**, not the whole system.
**Boundary status (NOT the nucleus basalis — sibling):** **Boundary
case — the nucleus basalis of Meynert is a SIBLING, not a parent or
child.** The **medial septal nucleus** and the **nucleus basalis**
are the **two major cholinergic nuclei** of the basal forebrain — but
they are **functionally distinct**: the medial septal nucleus
projects primarily to the **hippocampus** and **olfactory bulb**;
the nucleus basalis projects primarily to the **neocortex** and
**amygdala**. The tree wires them as **siblings**. Consumers that
need the **basal forebrain cholinergic system** as a unit must
**union** the three cholinergic leaves (medial septal, diagonal band,
nucleus basalis).
**Boundary status (NOT the septum pellucidum):** **Boundary case —
"medial septal nucleus" is NOT the "septum pellucidum."** The
**septum pellucidum** is a **thin midline membrane** between the
lateral ventricles — a **telencephalic midline structure**, not a
nucleus. The **medial septal nucleus** is a **grey-matter nucleus**
in the basal forebrain. The two share the word "septum" but are
**anatomically distinct**. Consumers must not conflate them.
**Boundary status (NOT the amygdala — despite the parent container's
limbic connections):** **Boundary case — the medial septal nucleus
is primarily cholinergic/hippocampal, NOT primarily limbic/amygdalar.**
The **parent septal nuclei container** has **strong limbic
connections to the amygdala** (mainly via the **lateral** septal
nucleus), but the **medial** septal nucleus — this module — is
**primarily cholinergic and projects to the hippocampus and
olfactory bulb**, **not** primarily to the amygdala. It has some
**amygdala connections** (via the bed nucleus of the stria
terminalis and other routes), but its **defining function** is
**septohippocampal theta**, not **emotional processing**. Consumers
must **not** import amygdala-lateralization claims into the **medial**
septal nucleus — and must not conflate it with the **lateral**
septal nucleus, which **is** the limbic-amygdalar component (and is
**not wired**).
**Boundary status (one of the five rhinencephalon-excluded
structures — via the MOS):** **Boundary case — the medial septal
nucleus is the MEDIAL OLFACTORY STRIA (MOS) TARGET.** The **medial
olfactory stria** — a **rhinencephalon leaf** (part of
``olfactory_tract/``) — projects to the **septal region**, and
classical anatomy therefore groups the septal nuclei with the
**rhinencephalon**. The tree **excludes** them (narrow olfactory
definition) and places them under the **basal forebrain**. The
**medial septal nucleus** is the **specific MOS target** — it
receives **MOS input** and contributes to **olfactory modulation**
(via its projection to the olfactory bulb). Consumers reconstructing
the **classical full rhinencephalon** must **union** the
rhinencephalon with the **parent septal nuclei container** (which is
the level at which the rhinencephalon redirects).

Overview
--------
The medial septal nucleus is a **magnocellular cholinergic nucleus**
in the **medial basal forebrain**, located **inferior to the septum
pellucidum**, **anterior to the lamina terminalis**, and **medial to
the diagonal band of Broca**. It is the **cholinergic component** of
the septal region — the **lateral septal nucleus** is the
**GABAergic** component (and is **not wired** in the tree).

**The medial septal nucleus is the "hippocampal acetylcholine
faucet."** Together with the **vertical limb of the diagonal band
(NDB)**, it provides the **cholinergic and GABAergic innervation of
the hippocampus** — the **septohippocampal cholinergic system**. It
is the **pacemaker** for **septohippocampal theta** (the **4–8 Hz
rhythm** organizing hippocampal activity during **exploration, REM
sleep, and memory encoding**), and its **cholinergic neurons**
modulate **hippocampal excitability, plasticity, and memory**.

**The medial septal nucleus is also the "olfactory bulb cholinergic
modulator."** Together with the **horizontal limb of the diagonal
band**, it provides **cholinergic and GABAergic input to the
olfactory bulb** — a **centrifugal modulation** of olfactory
processing. This is the **olfactory function** that connects the
medial septal nucleus to the **rhinencephalon** (via the **medial
olfactory stria**), even though the nucleus itself is under the
**basal forebrain**, not the rhinencephalon.

**The medial septal nucleus is NOT the lateral septal nucleus.** The
**lateral** septal nucleus is the **GABAergic** component of the
septal region — it projects to the **hypothalamus** and **brainstem**,
is involved in **reward, anxiety, fear, and social behavior**, and is
**not cholinergic**. The tree **does not wire** the lateral septal
nucleus — it is a **documented gap** (see the parent `septal_nuclei`
module). Consumers that need the lateral septal nucleus must resolve
its functions as **prose in the parent module**; they cannot resolve
it as a child of the septal nuclei, and they cannot resolve it as a
child of the medial septal nucleus.

**The medial septal nucleus is a paired structure.** Each hemisphere
has its own medial septal nucleus, projecting **ipsilaterally** to
its own hippocampus and olfactory bulb. The two are **bilaterally
symmetric** and **functionally non-lateralized** — septohippocampal
theta, hippocampal cholinergic modulation, and olfactory bulb
modulation are **bilateral functions**. See *Lateralization Notes*.

Cytoarchitecture (prose, not structural children)
-------------------------------------------------
The medial septal nucleus has **no structural children** in the tree,
but its **cellular composition** is distinctive:

*   **Magnocellular cholinergic neurons** — the **defining
    population**. Large neurons (~20–40 μm) that synthesize
    **acetylcholine** (via **choline acetyltransferase, ChAT**) and
    project to the **hippocampus** (via the **fornix** and the
    **fimbria**) and to the **olfactory bulb** (via the **medial
    forebrain bundle**). They express **TrkA** (the **NGF receptor**)
    and **p75** (the **low-affinity neurotrophin receptor**), like the
    nucleus basalis cholinergic neurons.

*   **GABAergic neurons** — the medial septal nucleus also contains
    **GABAergic** neurons that project to the hippocampus (with the
    cholinergic neurons) and contribute to the **septohippocampal
    theta** rhythm. The GABAergic and cholinergic neurons are
    **intermingled** — the septohippocampal projection is
    **mixed cholinergic/GABAergic**, not purely cholinergic.

*   **Glutamatergic neurons** — a **smaller** population of
    glutamatergic neurons also projects to the hippocampus, contributing
    to the **septohippocampal pathway**. The medial septal nucleus is
    therefore **not purely cholinergic** — it is a **mixed
    cholinergic/GABAergic/glutamatergic** nucleus.

*   **Calbindin- and calretinin-positive neurons** — calcium-binding
    protein-positive subpopulations that contribute to the
    **heterogeneity** of the medial septal nucleus and to the
    **GABAergic** projection.

**These cellular features are prose, not structural children.** The
tree does **not** wire the cholinergic, GABAergic, or glutamatergic
populations as sub-modules. Consumers that need cytoarchitectural
detail should consult the references, not the tree.

The Medial Septal Nucleus / Lateral Septal Nucleus Boundary
-----------------------------------------------------------
This is the **most consequential boundary** in the medial septal
nucleus module, because the **lateral** septal nucleus is **not
wired**:

*   **Medial septal nucleus** (this module) — **cholinergic**;
    projects to **hippocampus** and **olfactory bulb**; pacemaker for
    **septohippocampal theta**; **wired** as the only child of the
    septal nuclei.

*   **Lateral septal nucleus** — **GABAergic**; projects to
    **hypothalamus** and **brainstem**; involved in **reward,
    anxiety, fear, and social behavior**; **NOT wired** in the tree
    (documented gap; see the parent module).

**Consumers that need the "septal region" must union both — but the
lateral septal nucleus is only available as prose.** This is the
**fundamental asymmetry** of the septal region in this tree: the
**medial** component is **wired**, the **lateral** component is a
**documented gap**. The medial septal nucleus module **receives** the
medial component; the parent `septal_nuclei` module documents the
lateral component as prose. Consumers that need the **full septal
region** must read **both** modules — the medial septal nucleus (this
module) for the cholinergic component, and the parent `septal_nuclei`
for the lateral (GABAergic) prose.

The Medial Septal Nucleus / Other Cholinergic Nuclei Boundary
-------------------------------------------------------------
The medial septal nucleus is **one of three** basal forebrain
cholinergic nuclei:

| Cholinergic nucleus | Tree path | Primary targets |
|---|---|---|
| **Medial septal nucleus** (this module) | `subcortical/basal_forebrain/septal_nuclei/medial_septal_nuclei/` | **Hippocampus** (via fornix), **olfactory bulb** |
| **Diagonal band of Broca** | `subcortical/basal_forebrain/diagonal_band_of_broca/` | **Hippocampus** (vertical limb), **olfactory bulb** (horizontal limb), **cortex** (some) |
| **Nucleus basalis of Meynert** | `subcortical/basal_forebrain/nucleus_basalis/` | **Neocortex**, **amygdala**, thalamus |

**All three are siblings under the basal forebrain.** Consumers that
need the **basal forebrain cholinergic system** as a unit must
**union** the three leaves. The medial septal nucleus is the
**hippocampal** one (with the diagonal band's vertical limb) and the
**olfactory bulb** one (with the diagonal band's horizontal limb).
The **nucleus basalis** is the **cortical** one.

The Medial Septal Nucleus / Septohippocampal System Boundary
------------------------------------------------------------
The medial septal nucleus and the **vertical limb of the diagonal
band (NDB)** together form the **septohippocampal cholinergic
system** — the **two cholinergic sources to the hippocampus**.

**They are siblings, not parent/child.** Consumers that need the
**septohippocampal system** as a unit must **union**
``septal_nuclei/medial_septal_nuclei/`` and
``diagonal_band_of_broca/`` — they are **two separate leaves**, not a
container and a child.

Function in the Human Brain
---------------------------
The medial septal nucleus's functions are **cholinergic and
GABAergic modulation of the hippocampus and olfactory bulb**:

*   **Septohippocampal Theta (Pacemaker Function):** The medial
    septal nucleus is the **primary pacemaker** for
    **septohippocampal theta** — the **4–8 Hz rhythm** organizing
    hippocampal activity during **exploration, REM sleep, and memory
    encoding**. Its **cholinergic and GABAergic neurons** project to
    the hippocampus (via the fornix) and **drive** the theta rhythm.
    **Lesions disrupt theta** and impair **spatial memory**.

*   **Hippocampal Cholinergic Modulation (Modulatory Function):** The
    medial septal nucleus's **cholinergic projections** to the
    hippocampus modulate **hippocampal excitability, plasticity, and
    memory**. Its **cholinergic signal** is a **neuromodulatory
    broadcast** that **tunes** hippocampal circuits, supporting
    **memory encoding and retrieval**.

*   **Hippocampal GABAergic Modulation (Modulatory Function):** The
    medial septal nucleus's **GABAergic projections** to the
    hippocampus modulate **local inhibition** and contribute to the
    **theta rhythm** — the septohippocampal pathway is **mixed
    cholinergic/GABAergic**, not purely cholinergic.

*   **Olfactory Bulb Cholinergic Modulation (Olfactory Function):**
    The medial septal nucleus projects to the **olfactory bulb**
    (with the diagonal band's horizontal limb), modulating
    **glomerular gain** and **attention-dependent olfactory
    processing**. This is the **olfactory function** that connects
    the medial septal nucleus to the **rhinencephalon** via the
    **medial olfactory stria**.

*   **Medial Olfactory Stria Reception (Olfactory Input):** The
    medial septal nucleus **receives input** from the **medial
    olfactory stria (MOS)** — the **rhinencephalon** projection that
    carries olfactory information to the septal region. The medial
    septal nucleus is therefore a **MOS target** — a
    **rhinencephalon-excluded structure** that is **olfactory-linked**
    but **wired under the basal forebrain**.

*   **NOT a cortical processor, NOT a limbic processor.** The medial
    septal nucleus **modulates** the hippocampus and olfactory bulb;
    it does **not** process cortical or limbic information in the way
    a cortical area or the **lateral** septal nucleus does. It is a
    **modulatory nucleus** — the **hippocampal cholinergic
    pacemaker**, not an emotional or cognitive processor.

**The unifying theme:** the medial septal nucleus is the **hippocampal
cholinergic pacemaker** — the source of **septohippocampal theta**,
the **cholinergic and GABAergic modulator** of the hippocampus, and
the **olfactory bulb cholinergic modulator**. It is **not** the
lateral septal nucleus (GABAergic, limbic), **not** the diagonal band
(sibling), **not** the nucleus basalis (cortical), and **not** the
septum pellucidum (membrane).

Associated Disorders
--------------------
Medial septal nucleus disorders are **cholinergic**, **amnestic**, and
**theta-related**:

*   **Korsakoff Syndrome — Medial Septal Involvement:** **Korsakoff
    syndrome** (thiamine deficiency) involves **mammillary body**,
    **anterior thalamic**, and **septal** damage — producing
    **anterograde amnesia** and **confabulation**. The **medial
    septal nucleus** is part of the **amnesic circuit**; its damage
    contributes to the **memory impairment**.

*   **Basal Forebrain Amnesia — Medial Septal Damage:** **ACoA
    aneurysm rupture** and **surgical resection** can damage the
    **medial septal nucleus** (and the diagonal band), producing
    **anterograde amnesia** and **confabulation** — the **basal
    forebrain amnesia syndrome** (Damasio et al., 1985). The
    **septohippocampal pathway** is disrupted, contributing to the
    memory deficit.

*   **Septohippocampal Amnesia (Animal Models):** **Medial septal
    lesions** in animals disrupt **septohippocampal theta** and
    impair **spatial memory** — findings that support the medial
    septal nucleus's role in **hippocampal function**.

*   **Alzheimer's Disease — Medial Septal Cholinergic Loss:** The
    **medial septal nucleus**'s **cholinergic neurons** are **less
    severely affected** than the **nucleus basalis** neurons in
    Alzheimer's, but they still contribute to the **hippocampal
    cholinergic deficit** and to **memory impairment**.
    **Septohippocampal cholinergic loss** is part of the broader
    **basal forebrain cholinergic deficit** in AD.

*   **Schizophrenia — Medial Septal/Cholinergic Deficit
    (Contested):** Some studies report **medial septal volume
    reduction** and **cholinergic deficits** in schizophrenia,
    possibly contributing to **cognitive and psychotic symptoms**.
    The evidence is **mixed**, and the **medial septal** role is
    **not established**.

*   **Fornix DBS for Alzheimer's — Therapeutic (Adjacent to Medial
    Septal):** **Deep brain stimulation of the fornix** (the output
    pathway of the medial septal nucleus) has been investigated as an
    **experimental therapy** for Alzheimer's disease, based on the
    rationale that **stimulating the fornix** may **enhance
    hippocampal cholinergic tone** and **memory**. Results have been
    **mixed**, but the approach is **clinically relevant** to the
    medial septal nucleus's projections.

*   **Septal DBS for Depression (Contrast — Lateral Septal):** The
    **lateral septal nucleus** (not wired) is the target of
    **experimental DBS for depression** — **not** the medial septal
    nucleus. Consumers must **not** conflate the two: the medial
    septal nucleus is the **cholinergic/hippocampal** component; the
    lateral septal nucleus is the **GABAergic/limbic** component.

**What is NOT here:** The medial septal nucleus is **not** the
substrate for **Alzheimer's disease** as a whole (nucleus basalis is
the primary cholinergic substrate), **depression** (the **lateral**
septal nucleus is the affective component), **anxiety** (lateral
septal), **reward/addiction** (lateral septal + nucleus accumbens), or
**Kluver-Bucy syndrome** (amygdala). Its clinical footprint is
**cholinergic-hippocampal** (Korsakoff, basal forebrain amnesia,
Alzheimer's contribution, fornix DBS) and **theta-related** (animal
models) — a **distinct category** from the **lateral** septal
nucleus's **limbic-affective** footprint.

Lateralization Notes
--------------------
This is the **right** medial septal nucleus module. The medial septal
nucleus is **bilaterally symmetric** and **functionally
non-lateralized**:

*   **Bilateral Cholinergic Projection:** Each medial septal nucleus
    projects **ipsilaterally** to its own hippocampus (via the
    fornix) and to its own olfactory bulb. The two sides are
    **functionally symmetric** for septohippocampal theta and
    hippocampal/olfactory cholinergic modulation.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the medial septal nucleus has **no documented
    left-lateralized or right-lateralized function**. **Korsakoff**
    septal damage is **bilateral**; **basal forebrain amnesia** is
    **bilateral**; **Alzheimer's** cholinergic loss is **bilateral**.

*   **Partial Lateralization (Contested — Parent Container):** The
    parent **septal nuclei** container reports **weak, contested**
    partial lateralization (left > right for reward; right > left for
    anxiety) — but that lateralization is attributed to the
    **lateral** septal nucleus (the GABAergic, limbic component), **not**
    the **medial** septal nucleus. The medial septal nucleus is
    **primarily cholinergic/hippocampal** and is **functionally
    symmetric** — its lateralization is **not established**.

*   **Amygdala-Projection Asymmetry (Weaker than Parent Container):**
    The **parent** septal nuclei container has **strong amygdala
    connections** (mainly via the **lateral** septal nucleus) and
    therefore carries a **moderate** amygdala-lateralization warning.
    The **medial** septal nucleus — this module — has **weaker
    amygdala connections** (it is primarily cholinergic/hippocampal),
    so its amygdala-lateralization warning is **lighter** than the
    parent container's. **This is true on the right side as well**:
    the right medial septal nucleus is **not** the right lateral
    septal nucleus, and the right amygdala's fear association
    belongs to the **parent container's lateral component** (prose-
    only, not wired) and to the **amygdala module** (amygdala
    proper), **not** to the medial septal nucleus. Consumers must
    **not** import the **right amygdala's fear association** into
    the **medial** septal nucleus — the medial septal nucleus is
    **not** a limbic-amygdalar structure in the way the **lateral**
    septal nucleus is.

**A consumer that assumes "right medial septal nucleus = left medial
septal nucleus" will be structurally and functionally correct** — the
two sides are symmetric, no lateralized function has been
demonstrated, and the medial septal nucleus's **bilateral cholinergic
projections** are the anatomical substrate of its **bilateral
functions**. This is a **strict-mirror pair with a lighter warning** —
lighter than the **parent** septal nuclei container, because the
**medial** septal nucleus's amygdala connections are **weaker** than
the container's (which are dominated by the **lateral** component).
**The right-side module keeps the warning light**, matching the
parent-child warning gradient — the medial septal nucleus is
primarily cholinergic/hippocampal, and the right-amygdala fear claim
does not belong here.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``rhinencephalon/``, ``.../diencephalon/``, ``cortex/``, or the
    other subcortical containers. The medial septal nucleus's
    relationships to the hippocampus, olfactory bulb, diagonal band,
    and nucleus basalis are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **cholinergic**,
    **GABAergic**, and **glutamatergic** neuronal populations, and the
    **septohippocampal** and **septobulbar** projection pathways, are
    documented as **prose**, not as sub-modules. Consumers must not
    assume any exist as children; resolve cytoarchitectural and
    projection detail through the references.
*   **NOT the lateral septal nucleus.** The **lateral** septal nucleus
    is the **GABAergic** component of the septal region — **not
    wired** in the tree (a **documented gap** in the parent
    `septal_nuclei` module). The **medial** septal nucleus (this
    module) is the **cholinergic** component. Consumers must not
    conflate them.
*   **NOT the diagonal band — sibling.** The diagonal band is a
    **sibling** under the basal forebrain, not a parent or child.
    Consumers that need the **septohippocampal cholinergic system** as
    a unit must **union** ``septal_nuclei/medial_septal_nuclei/`` and
    ``diagonal_band_of_broca/``.
*   **NOT the nucleus basalis — sibling.** The nucleus basalis is a
    **sibling** under the basal forebrain. Consumers that need the
    **basal forebrain cholinergic system** as a unit must **union**
    the three cholinergic leaves.
*   **NOT the septum pellucidum.** "Medial septal nucleus" is a
    **grey-matter nucleus**; "septum pellucidum" is a **midline
    membrane**. Do not conflate them.
*   **Weaker amygdala connections than the parent container — and
    the right-side module keeps the warning light.** The **medial**
    septal nucleus is primarily **cholinergic/hippocampal**; the
    **lateral** septal nucleus is the **limbic-amygdalar** component
    (and is **not wired**). The right medial septal nucleus is
    **not** the right lateral septal nucleus, and the right-amygdala
    fear claim does **not** belong here.
*   **One of the five rhinencephalon-excluded structures — via the
    MOS.** The medial septal nucleus is the **medial olfactory stria
    target**. Consumers reconstructing the **classical full
    rhinencephalon** must union the rhinencephalon with the **parent
    septal nuclei container**.
*   **No ``AREA_PATHS`` hop.** The medial septal nucleus is a local
    leaf under the septal nuclei, not a cross-listed leaf.
*   **No nested cross-listing.** The medial septal nucleus has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left medial septal nucleus — strict
    mirror with a lighter warning.** Right and left medial septal
    nucleus modules are **structurally identical** — same leaf
    status, same cytoarchitectural prose, same lateral-septal-gap
    note, same cholinergic-sibling notes, same non-lateralized
    caveat. **The amygdala-lateralization warning is lighter than the
    parent container's**, because the **medial** septal nucleus's
    amygdala connections are **weaker** than the parent's (which are
    dominated by the **lateral** component). **The right-side module
    keeps the warning light** — no dedicated Usage block, no
    emphatic contrast reference, only a **moderate** Lateralization
    note — matching the parent-child warning gradient.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain.septal_nuclei import medial_septal_nuclei

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_forebrain.septal_nuclei.medial_septal_nuclei"
    )

**Do not** assume the medial septal nucleus is the **lateral septal
nucleus**. The **lateral** septal nucleus is **GABAergic** and **not
wired** in the tree (a **documented gap**). The **medial** septal
nucleus (this module) is **cholinergic**. They are **different
structures** with **different functions**.

**Do not** assume the medial septal nucleus is the **septum
pellucidum**. "Medial septal nucleus" is a **grey-matter nucleus**;
"septum pellucidum" is a **midline membrane**. They are **different
structures**.

**Do not** assume the medial septal nucleus is a **child of the
diagonal band** or **nucleus basalis**. Both are **siblings** under
the basal forebrain.

**Do not** import **amygdala-lateralization claims** into the medial
septal nucleus. Its **amygdala connections are weaker** than the
parent septal nuclei container's — the **lateral** septal nucleus is
the limbic-amygdalar component, and it is **not wired**. **This is
true on the right side as well** — the right medial septal nucleus is
**not** the right lateral septal nucleus, and the right amygdala's
fear association belongs to the **amygdala module** (amygdala proper)
and to the **parent container's lateral component** (prose-only),
**not** here.

**Do not** assume the medial septal nucleus has structural children.
It is a **leaf**. The **cholinergic**, **GABAergic**, and
**glutamatergic** populations and the **septohippocampal** and
**septobulbar** projection pathways are **prose only** — they are not
wired as modules.

Iterating the medial septal nucleus's (empty) children (recommended
consumer pattern)::

    MSN_CHILDREN = ()
    # The medial septal nucleus is a leaf. Cholinergic, GABAergic,
    # and glutamatergic populations are prose, not modules.

Reconstructing the septohippocampal cholinergic system
(recommended consumer pattern)::

    # The septohippocampal system spans TWO sibling leaves. Union
    # them:
    SEPTOHIPPOCAMPAL_CHOLINERGIC = (
        "subcortical.basal_forebrain.septal_nuclei.medial_septal_nuclei",
        "subcortical.basal_forebrain.diagonal_band_of_broca",
    )
    # Both project to the hippocampus via the fornix. Classical
    # anatomy often groups them as the "septal region."

Reconstructing the basal forebrain cholinergic system (recommended
consumer pattern)::

    # The basal forebrain cholinergic system spans THREE sibling
    # leaves. Union them:
    BASAL_FOREBRAIN_CHOLINERGIC = (
        "subcortical.basal_forebrain.nucleus_basalis",
        "subcortical.basal_forebrain.septal_nuclei.medial_septal_nuclei",
        "subcortical.basal_forebrain.diagonal_band_of_broca",
    )

Reconstructing the classical full rhinencephalon (recommended
consumer pattern)::

    # The medial septal nucleus is part of the septal nuclei, which
    # are one of the five structures the rhinencephalon excluded.
    # The union is at the PARENT level (septal_nuclei), not the
    # child level (medial_septal_nuclei):
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",            # PARENT of THIS MODULE
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",
        ),
    }

Reaching the medial septal nucleus's downstream targets (recommended
consumer pattern)::

    # The medial septal nucleus projects to structures documented
    # elsewhere in the tree. Resolve them at their own paths:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #   rhinencephalon.olfactory_bulb
    #   (via white_matter.fornix and white_matter.medial_forebrain_bundle)
    #
    # These are NOT medial septal nucleus children. They are
    # downstream targets.

Reaching the medial olfactory stria (recommended consumer pattern)::

    # The medial olfactory stria is a rhinencephalon leaf. It projects
    # TO the septal nuclei (this module's parent):
    #
    #   rhinencephalon.olfactory_tract
    #
    # The MOS is the INPUT to the septal region, not a child of the
    # medial septal nucleus.

Reaching the lateral septal nucleus's FUNCTIONS (recommended consumer
pattern — note the GAP)::

    # The lateral septal nucleus is NOT in the tree (documented gap
    # in the parent septal_nuclei module). Its functions (reward,
    # anxiety, fear, social behavior) are documented as PROSE in the
    # PARENT module, NOT here. Resolve:
    #
    #   subcortical.basal_forebrain.septal_nuclei
    #     -> parent module's "Lateral septal nucleus (NOT wired —
    #        documented as prose)" section
    #
    # Do NOT attempt to resolve a "lateral_septal_nuclei" path — it
    # does not exist in the tree.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        msn_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.septal_nuclei.medial_septal_nuclei"
        )
        # resolve msn_path through the memory/recall layer

References
----------
*   **Canonical medial septal anatomy:** Risold, P.Y., Swanson, L.W.
    (1997). "Connections of the rat lateral septal complex." *Brain
    Research Reviews* 24:115–195. (Definitive septal anatomy; medial
    vs. lateral septal distinction.)
*   **Medial septal cholinergic:** Mesulam, M.-M., Mufson, E.J.,
    Levey, A.I., Wainer, B.H. (1983). "Cholinergic innervation of
    cortex by the basal forebrain." *Journal of Comparative
    Neurology* 214:170–197. (Medial septal nucleus as one of the
    three cholinergic nuclei.)
*   **Septohippocampal theta:** Petsche, H., Stumpf, C., Gogolak, G.
    (1962). "The significance of the rabbit's septum as a relay
    station between the midbrain and the hippocampus. I. The control
    of hippocampus arousal activity by the septum cells."
    *Electroencephalography and Clinical Neurophysiology* 14:202–211.
    (Classical description of septohippocampal theta.)
*   **Septohippocampal theta (review):** Buzsáki, G. (2002). "Theta
    oscillations in the hippocampus." *Neuron* 33:325–340.
    (Septohippocampal theta; medial septum and diagonal band as
    pacemakers.)
*   **Medial septal GABAergic/glutamatergic:** Freund, T.F., Antal, M.
    (1988). "GABA-containing neurons in the septum control
    inhibitory interneurons in the hippocampus." *Nature* 336:170–173.
    (Septohippocampal GABAergic projection.)
*   **Septal lesions and memory:** Thomas, G.J., Brito, G.N., Stein,
    D.P., Berko, J.K. (1982). "Memory and septal-hippocampal
    function." *Physiological Psychology* 10:353–358. (Septal lesions
    and memory impairment.)
*   **Korsakoff syndrome:** Victor, M., Adams, R.D., Collins, G.H.
    (1989). *The Wernicke-Korsakoff Syndrome*, 2nd ed. (Mammillary
    body, anterior thalamic, and septal involvement in the amnesic
    circuit.)
*   **Basal forebrain amnesia:** Damasio, A.R., Graff-Radford, N.R.,
    Eslinger, P.J., Damasio, H., Kassell, N. (1985). "Amnesia
    following basal forebrain lesions." *Archives of Neurology*
    42:263–271. (Septal and diagonal band involvement in basal
    forebrain amnesia.)
*   **Fornix DBS for Alzheimer's:** Laxton, A.W., et al. (2010). "A
    phase I trial of deep brain stimulation of memory circuits in
    Alzheimer's disease." *Annals of Neurology* 68:521–534. (Fornix
    DBS; adjacent to medial septal projections.)
*   **Schizophrenia septal volume (contested):** Keshavan, M.S., et
    al. (1998). "Superior temporal gyrus and the course of early
    schizophrenia." *Biological Psychiatry* 43:531–539. (Septal
    volume reductions in schizophrenia; contested.)
*   **Lateral septal reward and anxiety (contrast):** Sheehan, T.P.,
    Chambers, R.A., Russell, D.S. (2004). "Regulation of affect by
    the lateral septum: implications for neuropsychiatric disorders."
    *Progress in Neurobiology* 73:233–264. (Lateral septal — NOT the
    medial septal — is the affective component; contrast reference.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the medial septal nucleus —
    it belongs to the amygdala module and to the parent septal
    nuclei container's lateral component.)
*   **Septum pellucidum (distinction):** Nieuwenhuys, R., Voogd, J.,
    van Huijzen, C. (2008). *The Human Central Nervous System*, 4th
    ed. (Septum pellucidum as a midline membrane, distinct from the
    septal nuclei.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medial septal nucleus in overview.)
*   NeuroNames — Medial septal nucleus (right); FMA — Medial septal
    nucleus (right member).
"""