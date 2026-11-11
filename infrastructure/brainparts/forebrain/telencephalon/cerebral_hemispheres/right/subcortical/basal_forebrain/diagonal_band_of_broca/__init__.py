"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain.diagonal_band_of_broca
===============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_forebrain
                    └── diagonal_band_of_broca   <-- THIS MODULE

**Primary synonym:** Diagonal band of Broca (DBB); band of Broca;
diagonal band; fasciculus diagonalis Brocae (historical — see
*Boundary status*).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A **band
of grey matter** containing **cholinergic and GABAergic projection
neurons** — the **vertical limb** (nucleus of the diagonal band,
NDB) and the **horizontal limb**.
**Part of:** The **basal forebrain** container — and, functionally,
the **basal forebrain cholinergic system** (with the nucleus basalis
and the medial septal nucleus).
**Structural parent:** ``.../right/subcortical/basal_forebrain/`` →
**direct child** of the basal forebrain container.
**Structural children:** **None.** This is a **leaf** module. The
**vertical limb** and **horizontal limb** are documented as **prose**,
not as structural children. The **cholinergic and GABAergic neuron
populations** within each limb are documented as **prose**, not as
sub-modules.
**Boundary status (grey matter, NOT white matter):** **Boundary
case — the name is a historical accident, and the structure is grey
matter, not an axonal tract.** The **diagonal band of Broca** is a
**band of grey matter** containing **cholinergic and GABAergic
projection neurons**, not an axonal bundle. Its name ("band," and the
historical Latin "fasciculus") reflects **19th-century gross anatomy**,
which could not distinguish grey from white matter at this location.
Consumers must **not** resolve the diagonal band as a white-matter
tract; it is under the **basal forebrain** here, and its neurons
project to the hippocampus, olfactory bulb, and cortex. See
*Boundary status (not white matter)* in the Design Contract.
**Boundary status (sibling of septal nuclei):** **Boundary case —
sibling of the septal nuclei, not part of them.** The diagonal band
and the **medial septal nucleus** are **anatomically adjacent** and
**functionally coupled** (together forming the "septal region" and
the **septohippocampal cholinergic system**). The tree wires them as
**siblings**: ``septal_nuclei/`` and ``diagonal_band_of_broca/``.
Consumers that need the **septohippocampal cholinergic system** must
**union** the two leaves, or resolve them separately. The diagonal
band is **not** a child of the septal nuclei, and the septal nuclei
are **not** a child of the diagonal band.
**Boundary status (sibling of APS):** **Boundary case — the band
crosses the APS surface, but is a sibling.** The **diagonal band**
crosses the **anterior perforated substance (APS)** surface (and is
often described as "within" it). The APS is a **sibling** under
``basal_forebrain/anterior_perforated_substance/`` — **not** a parent
of the diagonal band. The band is **not** a child of the APS.
**Boundary status (sibling of nucleus basalis):** **Boundary case —
both are cholinergic basal forebrain nuclei, but they are siblings.**
The **nucleus basalis** (of Meynert) and the **diagonal band** are
both **cholinergic projection nuclei** of the basal forebrain, and
together with the medial septal nucleus they form the **basal
forebrain cholinergic system**. The tree wires them as **siblings**
under ``basal_forebrain/``. Consumers that need the **cholinergic
system** as a unit must **union** them, or resolve each separately.
**Boundary status (not rhinencephalon):** **Boundary case — the
horizontal limb projects to the olfactory bulb, but the band is NOT
rhinencephalic.** The **horizontal limb** of the diagonal band
provides **cholinergic and GABAergic input to the olfactory bulb** —
a **centrifugal modulation** of olfactory processing. This is an
**olfactory-related function**, but the diagonal band itself is
**not** a rhinencephalon leaf. It is under the **basal forebrain**,
and consumers must not resolve it through the rhinencephalon.

Overview
--------
The diagonal band of Broca is a **band of grey matter** running
**diagonally** across the **ventral surface of the basal forebrain**
— from the **medial septal area** (rostrodorsally) to the
**anterior perforated substance and amygdala** (caudoventrally). It
contains **two limbs** — the **vertical limb** (also called the
**nucleus of the diagonal band**, NDB) and the **horizontal limb** —
each with its own **cholinergic and GABAergic projection neurons**.

**The diagonal band is one of the three major cholinergic nuclei of
the basal forebrain.** Together with the **medial septal nucleus**
and the **nucleus basalis of Meynert**, it forms the **basal
forebrain cholinergic system** — the **major source of acetylcholine**
for the hippocampus, olfactory bulb, and cortex. Its **cholinergic
neurons** are among the **earliest to degenerate in Alzheimer's
disease**, and its **loss** contributes to the **cholinergic
deficit** that is the basis of **cholinesterase-inhibitor therapy**.

**The diagonal band is NOT a white-matter tract, despite its name.**
This is its **most important anatomical fact**. The "band" is **grey
matter** containing **neurons**, not axons. Its name is a
**19th-century gross-anatomical artifact** — early anatomists saw a
"band" of tissue running diagonally and gave it a "fasciculus" name,
but modern cytoarchitectonics shows it is a **nucleus** (or pair of
nuclei) with **projection neurons**. Consumers must not resolve it as
a white-matter tract.

**The diagonal band's two limbs have different projection targets.**
The **vertical limb** (NDB) projects primarily to the **hippocampus**
(via the fornix), supporting **septohippocampal theta** and **memory**.
The **horizontal limb** projects to the **olfactory bulb**, the
**piriform cortex**, and the **amygdala**, supporting **olfactory
modulation** and **limbic integration**. The two limbs are
**functionally distinct** but **cytoarchitecturally continuous** — the
tree treats them as **prose**, not as separate leaves.

**The diagonal band is a sibling of the septal nuclei.** The **medial
septal nucleus** and the **vertical limb of the diagonal band** are
**anatomically adjacent** and **functionally coupled** — they are the
two **cholinergic sources to the hippocampus**, and they are often
described together as the **septohippocampal cholinergic system**.
The tree wires them as **siblings** under the basal forebrain. A
consumer that needs the **septohippocampal cholinergic system** as a
unit must **union** ``septal_nuclei/medial_septal_nuclei/`` and
``diagonal_band_of_broca/`` — the diagonal band is **not** a child of
the septal nuclei, and vice versa.

The Two Limbs (prose, not structural children)
----------------------------------------------
The diagonal band is classically divided into **two limbs**, with
**distinct projection targets**:

*   **Vertical limb** (nucleus of the diagonal band, NDB) — the
    **dorsomedial** part, adjacent to the **medial septal nucleus**.
    Its **cholinergic and GABAergic neurons** project to the
    **hippocampus** (via the **fornix** and the **fimbria**),
    supporting **septohippocampal theta** and **memory**.
    **Functionally continuous** with the medial septal nucleus — the
    two are the **septohippocampal cholinergic system**.

*   **Horizontal limb** — the **ventrolateral** part, running
    along the **ventral surface** of the basal forebrain and crossing
    the **anterior perforated substance** and the **amygdala**.
    Its **cholinergic and GABAergic neurons** project to the
    **olfactory bulb**, the **piriform cortex**, and the **amygdala**,
    supporting **olfactory modulation** and **limbic integration**.

**These two limbs are prose, not structural children.** The tree does
**not** wire them as sub-modules — the diagonal band is a **single
leaf**. Consumers that need limb-level resolution should consult the
references, not the tree.

**The "vertical" and "horizontal" labels are orientation-dependent.**
In the **human brain**, the limb that runs **dorsoventrally** is the
**vertical limb**, and the limb that runs **rostrocaudally** (crossing
the APS) is the **horizontal limb**. In **rodents** and other
mammals, the orientation is different, and the same names are applied
to **homologous** structures. Consumers should be aware that the
**limb labels are not anatomically absolute** — they are
**orientation-dependent conventions**.

Function in the Human Brain
---------------------------
The diagonal band's functions are **cholinergic modulation** and
**septohippocampal / olfactory-limbic integration**:

*   **Septohippocampal Theta and Memory (Vertical Limb):** The
    vertical limb's **cholinergic and GABAergic neurons** project to
    the **hippocampus** and are the **pacemaker** for
    **septohippocampal theta** — the **4–8 Hz rhythm** that
    organizes hippocampal activity during **exploration, REM sleep,
    and memory encoding**. **Lesions of the vertical limb** disrupt
    theta and impair **spatial memory**.

*   **Olfactory Modulation (Horizontal Limb):** The horizontal
    limb's **cholinergic and GABAergic neurons** project to the
    **olfactory bulb**, where they **modulate glomerular gain** and
    **attention-dependent olfactory processing**. This is a
    **centrifugal modulation** — the diagonal band **shapes** the
    bulb's output, but it does **not** process olfactory information
    itself.

*   **Cortical Cholinergic Modulation (with Nucleus Basalis):** The
    diagonal band (especially the vertical limb) contributes to the
    **basal forebrain cholinergic system** that modulates cortical
    **excitability, attention, and learning** — alongside the nucleus
    basalis. Its **loss in Alzheimer's disease** contributes to the
    **cortical cholinergic deficit**.

*   **Limbic Integration (Horizontal Limb):** The horizontal limb
    projects to the **amygdala** and to the **piriform cortex**,
    supporting **olfactory-limbic integration** — the association of
    odors with **emotion and memory**. The diagonal band is a
    **modulatory** input to these structures, not a **primary**
    processor.

*   **NOT a primary olfactory or memory structure.** The diagonal band
    **modulates** the hippocampus and olfactory bulb; it does **not**
    implement memory or olfaction itself. Those are properties of the
    **hippocampus** (under
    ``subcortical/medial_temporal_lobe/hippocampus/``) and the
    **olfactory bulb and piriform cortex** (under
    ``rhinencephalon/``), documented in their own modules.

**The unifying theme:** the diagonal band is a **cholinergic and
GABAergic projection nucleus** of the basal forebrain, with **two
limbs** projecting to the **hippocampus** and the **olfactory
bulb/limbic structures**. It is a **modulator**, not a processor. Its
**most famous function** is **septohippocampal theta**; its **most
famous clinical association** is **Alzheimer's disease** (cholinergic
loss).

Associated Disorders
--------------------
Diagonal band disorders are **cholinergic** and **memory-related**:

*   **Alzheimer's Disease — Cholinergic Loss:** The **cholinergic
    neurons** of the diagonal band (especially the vertical limb) are
    among the **earliest to degenerate** in Alzheimer's disease. Their
    loss contributes to the **cortical and hippocampal cholinergic
    deficit** that is the basis of **cholinesterase-inhibitor
    therapy** (donepezil, rivastigmine, galantamine). **This is the
    diagonal band's signature clinical association.**

*   **Septohippocampal Amnesia:** Lesions of the vertical limb (or its
    projections via the fornix) disrupt **septohippocampal theta** and
    contribute to **memory impairment** — especially in **Korsakoff
    syndrome** (with mammillary body and anterior thalamic lesions)
    and in **basal forebrain amnesia** (with septal and diagonal band
    involvement after ACoA aneurysm rupture).

*   **Basal Forebrain Amnesia:** **ACoA aneurysm rupture** and
    **surgical resection** of basal forebrain tumors can damage the
    diagonal band (and the septal nuclei), producing **anterograde
    amnesia** and **confabulation** — the **basal forebrain amnesia
    syndrome** (Damasio et al., 1985).

*   **Olfactory Dysfunction (Horizontal Limb):** Lesions of the
    horizontal limb can impair **olfactory modulation** and contribute
    to **odor discrimination deficits** — but the diagonal band's
    contribution is **modulatory**, not primary. The bulb and piriform
    cortex are the primary substrates.

*   **Parkinson's Disease:** The diagonal band's **cholinergic
    neurons** can be **affected** in Parkinson's disease, contributing
    to **cognitive impairment** and **olfactory dysfunction** — but
    this is **less well characterized** than its Alzheimer's
    involvement.

**What is NOT here:** The diagonal band is **not** the substrate for
**hippocampal amnesia proper** (hippocampus), **olfactory agnosia**
(piriform cortex), **Kluver-Bucy syndrome** (amygdala), or
**Wernicke's aphasia** (BA22). It is a **modulator** of the
hippocampus, olfactory bulb, and amygdala — not the primary substrate
for their disorders.

Lateralization Notes
--------------------
This is the **right** diagonal band module. The diagonal band is
**bilaterally symmetric** and **functionally non-lateralized**:

*   **Bilateral Septohippocampal Projection:** Each diagonal band
    projects **ipsilaterally** to its own hippocampus. The two sides
    are **functionally symmetric** for septohippocampal theta and
    memory.

*   **Bilateral Olfactory Modulation:** Each horizontal limb projects
    **ipsilaterally** to its own olfactory bulb and piriform cortex.
    The two sides are **functionally symmetric** for olfactory
    modulation.

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the diagonal band has **no documented left-lateralized or
    right-lateralized function**. **Alzheimer's** cholinergic loss is
    **bilateral**; **septohippocampal theta** is **bilateral**.

*   **No Cortical-Level Asymmetries:** The subtle left-verbal /
    right-emotional asymmetries reported for **orbitofrontal** and
    **insular** odor processing are **cortical-level** phenomena
    **downstream** of the diagonal band. Do not import them into the
    diagonal band.

**A consumer that assumes "right diagonal band = left diagonal band"
will be structurally and functionally correct** — the two sides are
symmetric, no lateralized function has been demonstrated, and the
diagonal band's **bilateral cholinergic projections** are the
anatomical substrate of its **bilateral functions**. This is a
**strict-mirror pair**: unlike the periamygdaloid, uncus, and
subcortical container pairs, the diagonal band carries **no
right-side-specific misconception** a consumer is likely to import,
so the right module is a **word-for-word mirror** of the left (with
only the path, hemisphere labels, and FMA member changed).

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``rhinencephalon/``, ``subcortical/`` (other than via
    prose redirects), or ``.../diencephalon/``. The diagonal band's
    projections to the hippocampus, olfactory bulb, piriform cortex,
    and amygdala are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **vertical limb**
    (NDB) and **horizontal limb** are documented as **prose**, not as
    sub-modules. The cholinergic and GABAergic neuron populations
    within each limb are documented as **prose**. Consumers must not
    assume either limb exists as a child; resolve limb-level detail
    through the references.
*   **Grey matter, NOT white matter — despite the name.** The diagonal
    band is a **band of grey matter** containing **cholinergic and
    GABAergic projection neurons**, not an axonal bundle. Its name is a
    **19th-century gross-anatomical artifact**. Consumers must not
    resolve it as a white-matter tract.
*   **Sibling of the septal nuclei.** The diagonal band and the
    **medial septal nucleus** are **anatomically adjacent** and
    **functionally coupled** (the septohippocampal cholinergic
    system), but the tree wires them as **siblings**. Consumers that
    need the **septohippocampal cholinergic system** as a unit must
    **union** ``septal_nuclei/medial_septal_nuclei/`` and
    ``diagonal_band_of_broca/``.
*   **Sibling of the APS.** The band crosses the APS surface, but the
    APS is a **sibling**, not a parent. The band is not a child of the
    APS.
*   **Sibling of the nucleus basalis.** Both are **cholinergic basal
    forebrain nuclei**, but they are **siblings** under the basal
    forebrain. Consumers that need the **basal forebrain cholinergic
    system** as a unit must **union** the diagonal band, the medial
    septal nucleus, and the nucleus basalis.
*   **Horizontal limb projects to the olfactory bulb, but the band is
    NOT rhinencephalic.** The horizontal limb provides
    **cholinergic/GABAergic input to the olfactory bulb**, but the
    diagonal band itself is a **basal forebrain** structure, not a
    rhinencephalon leaf.
*   **Limb labels are orientation-dependent.** The "vertical" and
    "horizontal" labels are **orientation-dependent conventions**,
    not anatomically absolute. The **human** vertical limb
    (dorsoventral) is the **homologue** of the rodent vertical limb
    (which runs in a different orientation), and vice versa.
*   **No ``AREA_PATHS`` hop.** The diagonal band is a local leaf under
    the basal forebrain, not a cross-listed leaf.
*   **No nested cross-listing.** The diagonal band has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with left diagonal band.** Right and left
    diagonal band modules are **structurally identical** — same leaf
    status, same two-limb prose, same "grey matter not white matter"
    caveat, same septal-nuclei/APS/nucleus-basalis sibling notes, same
    non-lateralized caveat. **This is a strict mirror pair** — there
    is no right-side-specific misconception to import, so the prose
    is word-for-word identical apart from hemisphere labels.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain import diagonal_band_of_broca

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_forebrain.diagonal_band_of_broca"
    )

**Do not** assume the diagonal band is a **white-matter tract**. It is
**grey matter** containing cholinergic and GABAergic projection
neurons, despite its name. Consumers iterating white-matter tracts and
expecting the diagonal band there will **miss it**.

**Do not** assume the diagonal band is a **child of the septal nuclei**
or vice versa. They are **siblings** under the basal forebrain. If
the **septohippocampal cholinergic system** is the unit of interest,
**union** ``septal_nuclei/medial_septal_nuclei/`` and
``diagonal_band_of_broca/``.

**Do not** assume the diagonal band is a **child of the APS**. It
**crosses** the APS surface, but it is a **sibling** under the basal
forebrain.

**Do not** assume the diagonal band is **rhinencephalic**. Its
horizontal limb projects to the olfactory bulb, but the band itself is
a **basal forebrain** structure.

**Do not** assume the diagonal band has structural children. It is a
**leaf**. The **vertical limb** (NDB) and **horizontal limb** are
**prose only** — they are not wired as modules.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        dbb_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.diagonal_band_of_broca"
        )
        # resolve dbb_path through the memory/recall layer

Reaching the diagonal band's downstream targets (recommended
consumer pattern)::

    # The diagonal band projects to structures documented elsewhere
    # in the tree. Resolve them at their own paths:
    #
    #   Vertical limb (NDB) targets:
    #     subcortical.medial_temporal_lobe.hippocampus
    #     (via the fornix — fornix is under white_matter/)
    #
    #   Horizontal limb targets:
    #     rhinencephalon.olfactory_bulb
    #     rhinencephalon.piriform_cortex
    #     subcortical.medial_temporal_lobe.amygdala
    #
    # These are NOT diagonal band children. They are downstream
    # targets.

Reconstructing the septohippocampal cholinergic system
(recommended consumer pattern)::

    # The septohippocampal cholinergic system spans TWO sibling
    # leaves. Union them:
    SEPTOHIPPOCAMPAL_CHOLINERGIC = (
        "subcortical.basal_forebrain.septal_nuclei.medial_septal_nuclei",
        "subcortical.basal_forebrain.diagonal_band_of_broca",
    )
    # Both project to the hippocampus via the fornix. The tree
    # splits them for finer granularity; classical anatomy often
    # groups them as the "septal region."

Reconstructing the basal forebrain cholinergic system
(recommended consumer pattern)::

    # The basal forebrain cholinergic system spans THREE sibling
    # leaves. Union them:
    BASAL_FOREBRAIN_CHOLINERGIC = (
        "subcortical.basal_forebrain.nucleus_basalis",
        "subcortical.basal_forebrain.septal_nuclei.medial_septal_nuclei",
        "subcortical.basal_forebrain.diagonal_band_of_broca",
    )
    # Together these are the major sources of cortical and
    # hippocampal acetylcholine; their loss in Alzheimer's disease is
    # the basis of cholinesterase-inhibitor therapy.

Limb-level detail (not wired — consult references)::

    # The diagonal band's two limbs are prose, not modules:
    #   vertical limb (NDB) -> hippocampus, theta, memory
    #   horizontal limb      -> olfactory bulb, piriform, amygdala
    #
    # Do not attempt to resolve these as sub-paths of the diagonal
    # band. The limb labels are orientation-dependent.

References
----------
*   **Canonical basal forebrain cholinergic anatomy:** Mesulam,
    M.-M., Mufson, E.J., Levey, A.I., Wainer, B.H. (1983).
    "Cholinergic innervation of cortex by the basal forebrain:
    cytochemistry and cortical connections of the septal area,
    diagonal band nuclei, nucleus basalis (substantia innominata),
    and hypothalamus in the rhesus monkey." *Journal of Comparative
    Neurology* 214:170–197. (Definitive cholinergic anatomy of the
    diagonal band.)
*   **Septohippocampal system:** Petsche, H., Stumpf, C., Gogolak, G.
    (1962). "The significance of the rabbit's septum as a relay
    station between the midbrain and the hippocampus. I. The control
    of hippocampus arousal activity by the septum cells."
    *Electroencephalography and Clinical Neurophysiology* 14:202–211.
    (Classical description of septohippocampal theta.)
*   **Vertical limb and theta:** Buzsáki, G. (2002). "Theta
    oscillations in the hippocampus." *Neuron* 33:325–340.
    (Septohippocampal theta; vertical limb and medial septum as
    pacemakers.)
*   **Horizontal limb and olfactory bulb:** Shipley, M.T., Ennis, M.
    (1996). "Functional organization of olfactory system." *Journal
    of Neurobiology* 30:123–176. (Centrifugal cholinergic innervation
    of the olfactory bulb from the horizontal limb.)
*   **Alzheimer's cholinergic loss:** Whitehouse, P.J., et al.
    (1982). "Alzheimer's disease and senile dementia: loss of
    neurons in the basal forebrain." *Science* 215:1237–1239.
    (Basal forebrain cholinergic loss, including diagonal band, in
    Alzheimer's.)
*   **Basal forebrain amnesia:** Damasio, A.R., Graff-Radford, N.R.,
    Eslinger, P.J., Damasio, H., Kassell, N. (1985). "Amnesia
    following basal forebrain lesions." *Archives of Neurology*
    42:263–271. (Basal forebrain amnesia syndrome; septal and
    diagonal band involvement.)
*   **Korsakoff syndrome:** Victor, M., Adams, R.D., Collins, G.H.
    (1989). *The Wernicke-Korsakoff Syndrome*, 2nd ed. (Mammillary
    body and anterior thalamic lesions, with septal and diagonal
    band involvement in the amnesic circuit.)
*   **Diagonal band as grey matter:** Heimer, L., de Olmos, J.,
    Alheid, G.F., Záborszky, L. (1999). "The human basal forebrain:
    an overview." In *The Human Nervous System* (Paxinos, G., ed.),
    2nd ed. (Cytoarchitectonic demonstration that the diagonal band
    is grey matter, not a fasciculus.)
*   **Nomenclature history:** Broca, P. (1878). "Anatomie comparée
    des circonvolutions cérébrales: le grand lobe limbique et la
    scissure limbique dans la série des mammifères." *Revue
    d'Anthropologie* 1:385–498. (Historical description; the name
    "diagonal band" is a gross-anatomical artifact.)
*   **Olfactory modulation:** Doty, R.L. (2015). *Handbook of
    Olfaction and Gustation*, 3rd ed. (Centrifugal modulation of
    olfactory bulb by basal forebrain cholinergic input.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Diagonal band in overview.)
*   NeuroNames — Diagonal band of Broca (right); FMA — Diagonal band
    of Broca (right member).
"""