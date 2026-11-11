"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain.septal_nuclei
======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── basal_forebrain
                    └── septal_nuclei   <-- THIS MODULE
                        └── medial_septal_nuclei

**Primary synonym:** Septal nuclei; septal region; septum (in the
limbic sense — NOT the septum pellucidum); septal area;
"the septum."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**heterogeneous group of nuclei** in the **medial basal forebrain**,
including **cholinergic** (medial) and **GABAergic** (lateral)
components.
**Part of:** The **basal forebrain** container — and, functionally,
the **septohippocampal system** (with the diagonal band) and the
**limbic forebrain** (with the amygdala, hypothalamus, and
hippocampus).
**Structural parent:** ``.../left/subcortical/basal_forebrain/`` →
**direct child** of the basal forebrain container.
**Structural children (one, closed set):**
``medial_septal_nuclei``.
**Boundary status (ONE-child container — the lateral septal nucleus
is NOT wired):** **Boundary case — the tree wires only the
`medial_septal_nuclei` child; the LATERAL septal nucleus is a
DOCUMENTED GAP, not a child.** Classical anatomy treats the **lateral
septal nucleus** and the **medial septal nucleus** as the **two main
components** of the septal region. The tree's dump shows **only**
``medial_septal_nuclei/`` under ``septal_nuclei/`` — the **lateral
septal nucleus is not present**. Consumers that need the **lateral
septal nucleus** must be aware that:
*   It is **not** in the tree dump.
*   Its **functions** (reward, anxiety, fear, social behavior) are
    **documented as prose** in this module, not as a child module.
*   Its **distinct** cytoarchitecture (GABAergic, **not** cholinergic)
    and **projections** (hypothalamus, brainstem, amygdala) are
    **prose**, not structural children.
The **medial septal nucleus** — the **cholinergic** component — is the
**only wired child**, and it is documented in its own module.
**Boundary status (one of the five rhinencephalon-excluded
structures):** **Boundary case — the septal nuclei are one of the five
structures the rhinencephalon excluded.** The **medial olfactory
stria (MOS)** — a **rhinencephalon leaf** — projects to the **septal
nuclei**. Classical anatomy therefore groups the septal nuclei with
the **rhinencephalon**. The tree **excludes** them and places them
**here**, under the **basal forebrain**. Consumers reconstructing the
**classical full rhinencephalon** must **union** the rhinencephalon
with this container (and with the other four excluded structures). See
the `CLASSICAL_FULL_RHINENCEPHALON` pattern below.
**Boundary status (one of the three basal forebrain cholinergic
nuclei — with siblings, NOT children):** **Boundary case — the
medial septal nucleus is one of three cholinergic nuclei, and the
other two are SIBLINGS, not children.** The **medial septal
nucleus** (under ``septal_nuclei/medial_septal_nuclei/``), the
**diagonal band of Broca** (``diagonal_band_of_broca/``), and the
**nucleus basalis of Meynert** (``nucleus_basalis/``) are the **three
cholinergic nuclei** of the basal forebrain — the **basal forebrain
cholinergic system**. The tree wires all three as **siblings** under
``basal_forebrain/``. The **diagonal band** and **nucleus basalis**
are **not** children of the septal nuclei. Consumers that need the
**basal forebrain cholinergic system** as a unit must **union** the
three leaves — the septal nuclei are **one of three**, not the whole
system.
**Boundary status (septohippocampal system — with diagonal band as a
sibling):** **Boundary case — the medial septal nucleus and the
vertical limb of the diagonal band form the septohippocampal system,
but they are SIBLINGS.** The **medial septal nucleus** and the
**vertical limb of the diagonal band (NDB)** are **anatomically
adjacent** and **functionally coupled** — together they are the
**septohippocampal cholinergic system**. The tree wires them as
**siblings** (``septal_nuclei/medial_septal_nuclei/`` and
``diagonal_band_of_broca/``). Consumers that need the
**septohippocampal system** as a unit must **union** the two leaves.
**Boundary status (NOT the septum pellucidum):** **Boundary case —
"septal nuclei" is NOT the "septum pellucidum."** The **septum
pellucidum** is a **thin midline membrane** between the lateral
ventricles — a **telencephalic midline structure** (not shown in the
visible tree dump, but if wired, it would be under the
**telencephalon** partition, not the basal forebrain). The **septal
nuclei** are **grey-matter nuclei** in the basal forebrain. The two
share the word "septum" but are **anatomically distinct**. Consumers
must not conflate them — "septal nuclei" (this module) is a
**grey-matter group**; "septum pellucidum" is a **midline membrane**.
**Boundary status (NOT the amygdala — despite strong limbic
connections):** **Boundary case — the septal nuclei have strong
limbic connections to the amygdala, but they are NOT the amygdala.**
The septal nuclei receive **amygdala input** (via the **stria
terminalis** and other routes) and project to **amygdala targets** —
they are **functionally coupled** to the amygdala in **fear, anxiety,
and reward** circuits. But the septal nuclei are **not** an amygdala
structure, **not** in the medial temporal lobe, and **not** adjacent
to the amygdala. They are **ventral basal forebrain nuclei**.
Consumers must not resolve the amygdala through the septal nuclei,
and must not import **amygdala-lateralization claims** into the septal
nuclei — their limbic connections are **bilateral** and **not
lateralized**.

Overview
--------
The septal nuclei ("septum") are a **group of grey-matter nuclei** in
the **medial basal forebrain**, located **anterior to the lamina
terminalis**, **inferior to the septum pellucidum**, and **medial to
the diagonal band of Broca**. Classical anatomy divides them into
**two major components**:

*   **Medial septal nucleus** — the **cholinergic** component,
    projecting to the **hippocampus** (via the **fornix**) and to the
    **olfactory bulb**. It is the **pacemaker** for
    **septohippocampal theta** and a **core component** of the
    **septohippocampal cholinergic system** (with the vertical limb
    of the diagonal band). **This is the only component wired as a
    child in the tree.**

*   **Lateral septal nucleus** — the **GABAergic** component,
    receiving **hippocampal** and **amygdala** input and projecting to
    the **hypothalamus**, **brainstem**, and **midbrain** nuclei. It
    is **not cholinergic** and is **functionally distinct** from the
    medial nucleus — it is involved in **reward, anxiety, fear, and
    social behavior**. **This is NOT wired in the tree** (see
    *Boundary status (ONE-child container)*).

**The tree wires only the medial septal nucleus.** This is a
**documented gap**: the lateral septal nucleus is **classically part
of the septal region** but is **not present** in the tree dump. The
module documents the lateral nucleus's functions as **prose** (below),
but consumers must be aware that **resolving the lateral septal
nucleus through the tree is not possible** — it is a gap.

**The septal nuclei are one of the five rhinencephalon-excluded
structures.** The **medial olfactory stria (MOS)** projects to the
septal nuclei, and classical anatomy groups them with the
**rhinencephalon**. The tree **excludes** them (narrow olfactory
definition) and places them here, under the **basal forebrain**.
Consumers reconstructing the **classical full rhinencephalon** must
**union** the rhinencephalon with this container.

**The septal nuclei are a paired structure.** Each hemisphere has its
own septal nuclei, with the **medial septal nuclei** near the midline
and the **lateral septal nuclei** further laterally. The two sides are
**bilaterally symmetric** and **largely non-lateralized** — though
some **partial lateralization** has been reported (see *Lateralization
Notes*).

Container Contents (one child, closed set)
------------------------------------------
The septal nuclei container has **exactly one child**:

*   **``medial_septal_nuclei``** — the **medial septal nucleus**, the
    **cholinergic** component of the septal region. Projects to the
    **hippocampus** (via the **fornix**), supporting
    **septohippocampal theta** and **memory**; and to the **olfactory
    bulb** (with the diagonal band's horizontal limb), supporting
    **olfactory modulation**. **Depth: leaf (no children).** It is
    **one of the three basal forebrain cholinergic nuclei** (with the
    nucleus basalis and the diagonal band).

**Not children (deliberately excluded — the LATERAL SEPTAL NUCLEUS
gap):**

*   **Lateral septal nucleus** — **NOT wired in the tree**. Classical
    anatomy includes it as the **GABAergic** component of the septal
    region, involved in **reward, anxiety, fear, and social behavior**.
    Its functions are documented as **prose** in this module, but it
    is **not** a structural child. Consumers that need it cannot
    resolve it through the tree — this is a **documented gap**.

*   **Nucleus of the diagonal band (NDB)** — **NOT a child of the
    septal nuclei**. It is the **vertical limb of the diagonal band**
    (``.../basal_forebrain/diagonal_band_of_broca/``), a **sibling**.
    Classical anatomy sometimes groups it with the septal nuclei, but
    the tree separates them.

*   **Nucleus basalis of Meynert** — **NOT a child**. It is
    ``.../basal_forebrain/nucleus_basalis/``, a **sibling** (the
    **cortical** cholinergic nucleus).

*   **Amygdala** — **NOT a child**. It is under
    ``subcortical/medial_temporal_lobe/amygdala/``. The septal nuclei
    have **strong limbic connections** to the amygdala but are not
    structurally related to it as parent/child.

*   **Septum pellucidum** — **NOT a child** and **NOT the same
    structure**. It is a **thin midline membrane** between the lateral
    ventricles, not a group of nuclei. See *Boundary status (NOT the
    septum pellucidum)*.

*   **Preoptic area** — **NOT a child**. It is
    ``.../diencephalon/hypothalamus/anterior/preoptic_area/``, a
    **diencephalic** sibling region, posterior to the septal nuclei.

The Septal Nuclei / Rhinencephalon Boundary
-------------------------------------------
The septal nuclei are **one of the five rhinencephalon-excluded
structures** — the **medial olfactory stria (MOS) target**. The
rhinencephalon modules **redirect** them here; this module **receives**
them. Consumers reconstructing the **classical full rhinencephalon**
must union:

    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",            # THIS MODULE
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",
        ),
    }

**The medial olfactory stria is the connection.** The MOS is a
**rhinencephalon leaf** (part of ``olfactory_tract/``); the septal
nuclei are its **target**. The tree separates the **tract** (under
``rhinencephalon/``) from the **target** (under ``subcortical/``),
which is a **deliberate boundary choice** reflecting the narrow
olfactory definition.

The Septal Nuclei / Other Cholinergic Nuclei Boundary
-----------------------------------------------------
The medial septal nucleus is **one of three** basal forebrain
cholinergic nuclei:

| Cholinergic nucleus | Tree path | Primary targets |
|---|---|---|
| **Medial septal nucleus** (this module, child) | `subcortical/basal_forebrain/septal_nuclei/medial_septal_nuclei/` | **Hippocampus** (via fornix), **olfactory bulb** |
| **Diagonal band of Broca** | `subcortical/basal_forebrain/diagonal_band_of_broca/` | **Hippocampus** (vertical limb), **olfactory bulb** (horizontal limb), **cortex** (some) |
| **Nucleus basalis of Meynert** | `subcortical/basal_forebrain/nucleus_basalis/` | **Neocortex**, **amygdala**, thalamus |

**All three are siblings under the basal forebrain.** Consumers that
need the **basal forebrain cholinergic system** as a unit must
**union** the three leaves. The septal nuclei container contributes
**one of three** via its **medial** child — the **lateral** septal
nucleus is **not** cholinergic and is **not** part of the cholinergic
system (and is **not wired**).

Function in the Human Brain
---------------------------
The septal nuclei have **two functionally distinct components**
(medial vs. lateral), and **only the medial** is wired in the tree:

**Medial septal nucleus (wired — see its own module for detail):**

*   **Septohippocampal theta (Vertical-Limb Function):** The medial
    septal nucleus is the **pacemaker** for **septohippocampal
    theta** — the **4–8 Hz rhythm** organizing hippocampal activity
    during **exploration, REM sleep, and memory encoding**. **Lesions
    disrupt theta** and impair **spatial memory**.

*   **Hippocampal cholinergic modulation (Modulatory Function):** The
    medial septal nucleus provides **cholinergic input** to the
    hippocampus (with the vertical limb of the diagonal band),
    modulating **hippocampal excitability, plasticity, and memory**.

*   **Olfactory bulb cholinergic modulation (Olfactory Function):**
    The medial septal nucleus projects to the **olfactory bulb**
    (with the diagonal band's horizontal limb), modulating
    **glomerular gain** and **attention-dependent olfactory
    processing**.

**Lateral septal nucleus (NOT wired — documented as prose):**

*   **Reward and reinforcement (Reward Function):** The lateral
    septal nucleus is a **node in the reward circuit** (with the
    nucleus accumbens, VTA, and prefrontal cortex) — its **GABAergic
    neurons** project to the **hypothalamus** and **brainstem**, and
    its activity is associated with **reward anticipation and
    consumption**.

*   **Anxiety and fear modulation (Affective Function):** The lateral
    septal nucleus has **dense amygdala connections** (via the stria
    terminalis) and modulates **anxiety and fear** — **lesions**
    produce **reduced anxiety** in animal models, and **stimulation**
    produces **anxiogenic** effects.

*   **Social behavior (Social Function):** The lateral septal nucleus
    is involved in **social recognition** and **social reward** —
    **lesions** impair **social memory** in rodents.

*   **Hippocampal-septal loop (Memory Function):** The lateral septal
    nucleus receives **hippocampal input** (via the fornix) and
    projects back to the **hypothalamus** and **brainstem** —
    contributing to the **hippocampal-septal-hypothalamic** loop
    involved in **memory and spatial navigation**.

**The unifying theme:** the septal nuclei are the **limbic and
cholinergic interface** of the basal forebrain — the **medial**
component is the **septohippocampal cholinergic** nucleus (wired),
and the **lateral** component is the **GABAergic reward/anxiety**
nucleus (**not wired**). The tree wires **only the medial** component;
the lateral component's functions are documented as **prose** here.

Associated Disorders
--------------------
Septal nuclei disorders are **cholinergic, limbic, and amnestic**:

*   **Korsakoff Syndrome — Septal Involvement:** **Korsakoff
    syndrome** (thiamine deficiency) involves **mammillary body**,
    **anterior thalamic**, and **septal** damage — producing
    **anterograde amnesia** and **confabulation**. The **medial
    septal nucleus** is part of the **amnesic circuit**; its damage
    contributes to the **memory impairment**.

*   **Basal Forebrain Amnesia — Septal Damage:** **ACoA aneurysm
    rupture** and **surgical resection** can damage the **septal
    nuclei** (and the diagonal band), producing **anterograde
    amnesia** and **confabulation** — the **basal forebrain amnesia
    syndrome** (Damasio et al., 1985). **Septal damage** is a
    **key contributor** to this syndrome.

*   **Alzheimer's Disease — Cholinergic Loss:** The **medial septal
    nucleus**'s **cholinergic neurons** are **less severely affected**
    than the **nucleus basalis** neurons in Alzheimer's, but they
    still contribute to the **hippocampal cholinergic deficit** and
    to **memory impairment**. **Septal cholinergic loss** is part of
    the broader **basal forebrain cholinergic deficit**.

*   **Schizophrenia — Septal/Cholinergic Deficit (Contested):** Some
    studies report **septal volume reduction** and **cholinergic
    deficits** in schizophrenia, possibly contributing to **cognitive
    and psychotic symptoms**. The evidence is **mixed**, and the
    **septal** role is **not established**.

*   **Anxiety and Depression — Lateral Septal Function:** The
    **lateral septal nucleus** (not wired) is involved in **anxiety
    and depression** circuits — **septal lesions** produce
    **reduced anxiety** in animal models, and **septal
    deep-brain stimulation** has been investigated (with limited
    evidence) as a **treatment for depression**.

*   **Reward and Addiction — Lateral Septal Function:** The **lateral
    septal nucleus** is part of the **reward circuit** — its
    **GABAergic neurons** modulate **reward and reinforcement**, and
    its involvement in **addiction** is an active area of research.

**What is NOT here:** The septal nuclei are **not** the substrate for
**Alzheimer's disease** as a whole (nucleus basalis is the primary
cholinergic substrate), **Parkinson's disease** (substantia nigra),
**temporal lobe epilepsy** (hippocampus), or **Kluver-Bucy syndrome**
(amygdala). Their clinical footprint is **cholinergic-amnestic**
(Korsakoff, basal forebrain amnesia, Alzheimer's cholinergic
contribution), **limbic-affective** (anxiety, depression, reward),
and **contested** (schizophrenia) — a **distinct category** from the
nucleus basalis's **cortical-cholinergic** footprint.

Lateralization Notes
--------------------
This is the **left** septal nuclei module. The septal nuclei are
**largely symmetric** with **partial lateralization**:

*   **Bilateral Cholinergic Projection:** Each **medial septal
    nucleus** projects **ipsilaterally** to its own hippocampus (and
    olfactory bulb). The two sides are **functionally symmetric** for
    septohippocampal theta and hippocampal cholinergic modulation.

*   **Partial Lateralization (Contested):** Some studies report
    **left-greater-than-right** **septal activation** during
    **reward** and **positive affect**, and **right-greater-than-left**
    **septal activation** during **anxiety** and **negative affect** —
    but these are **partial** and **inconsistently replicated**. They
    are **not** strong lateralized syndromes.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the septal nuclei have **no documented strong
    left-lateralized or right-lateralized function**. **Korsakoff**
    septal damage is **bilateral**; **basal forebrain amnesia** is
    **bilateral**; **Alzheimer's** cholinergic loss is **bilateral**.

*   **Amygdala-Projection Asymmetry (Contrast):** The **right
    amygdala** is sometimes reported as more involved in **fear
    processing** than the left, and the septal nuclei have **strong
    limbic connections to the amygdala** — but that connection is
    **bilateral** and **not lateralized**. The **right amygdala's
    fear association does not transfer** to the septal nuclei.
    Consumers must **not** import amygdala-lateralization claims into
    the septal nuclei — they are **bilateral limbic nuclei**, not a
    lateralized emotional structure.

**A consumer that assumes "left septal nuclei = right septal nuclei"
will be broadly correct** — the two sides are **largely symmetric**,
and no **strong** lateralized syndrome has been demonstrated. The
**partial** lateralization reported for reward and anxiety is **weak
and contested**, not a strong classification basis. The septal nuclei
are therefore a **strict-mirror pair with a light warning** — the
**medial** component's cholinergic functions are **symmetric**, and
the **lateral** component's (unwired) limbic functions are **largely
symmetric** with only **weak, contested** partial lateralization.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``rhinencephalon/``, ``.../diencephalon/``, ``cortex/``, or the
    other subcortical containers. The septal nuclei's relationships
    to the medial olfactory stria, amygdala, hypothalamus,
    hippocampus, and diagonal band are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **ONE-child container — the lateral septal nucleus is a
    documented GAP.** The tree wires **only** ``medial_septal_nuclei``
    under ``septal_nuclei/``. The **lateral septal nucleus** is
    **classically part of the septal region** but is **not** in the
    tree dump. Its functions (reward, anxiety, fear, social behavior)
    are documented as **prose**, not as a child module. Consumers
    must be aware that **resolving the lateral septal nucleus through
    the tree is not possible**.
*   **One of the five rhinencephalon-excluded structures.** The
    septal nuclei are **here**, not under ``rhinencephalon/``.
    Consumers reconstructing the **classical full rhinencephalon**
    must union the rhinencephalon with this container.
*   **One of the three cholinergic nuclei — with siblings, NOT
    children.** The **medial** septal nucleus is one of the three
    basal forebrain cholinergic nuclei. The **diagonal band** and
    **nucleus basalis** are **siblings**, not children. Consumers
    that need the **basal forebrain cholinergic system** as a unit
    must **union** the three leaves.
*   **Septohippocampal system — with diagonal band as a sibling.**
    The **medial** septal nucleus and the **vertical limb of the
    diagonal band** form the **septohippocampal cholinergic system**,
    but the tree wires them as **siblings**. Consumers that need the
    **septohippocampal system** as a unit must **union** the two
    leaves.
*   **NOT the septum pellucidum.** "Septal nuclei" (this module) is a
    **grey-matter group**; "septum pellucidum" is a **midline
    membrane**. Do not conflate them.
*   **NOT the amygdala, despite strong limbic connections.** The
    septal nuclei have **strong amygdala connections** but are **not**
    the amygdala and **not** adjacent to it. Do not import
    **amygdala-lateralization claims** into the septal nuclei.
*   **Lateral septal nucleus is NOT cholinergic.** The **lateral**
    septal nucleus is **GABAergic**, not cholinergic. It is **not**
    part of the basal forebrain cholinergic system. Only the
    **medial** septal nucleus is cholinergic.
*   **No ``AREA_PATHS`` hop.** The septal nuclei are a local
    container under the basal forebrain, not a cross-listed leaf.
*   **No nested cross-listing.** The septal nuclei have no nested
    dual-framing module. It is a single container.
*   **Structural parity with right septal nuclei — strict mirror
    with light warning.** Left and right septal nuclei modules are
    **structurally identical** — same one-child closed set, same
    lateral-septal gap, same rhinencephalon-exclusion redirect, same
    cholinergic-system union pattern. **The amygdala-lateralization
    warning is stated in the right-side module's Lateralization
    section**, because the septal nuclei's strong amygdala
    connections make the right-amygdala fear claim tempting to
    import — but the warning is **lighter** than the emphatic warnings
    in periamygdaloid/uncus/subcortical.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain import septal_nuclei

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "basal_forebrain.septal_nuclei"
    )

**Do not** assume the septal nuclei container has a **lateral septal
nucleus** child. The tree wires **only** ``medial_septal_nuclei``.
The **lateral** septal nucleus is a **documented gap** — it is
**classically part** of the septal region but is **not** in the tree
dump. Its functions are documented as **prose**, not as a child.

**Do not** assume the septal nuclei are the **septum pellucidum**.
"Septal nuclei" is a **grey-matter group**; "septum pellucidum" is a
**midline membrane**. They are **different structures**.

**Do not** assume the septal nuclei are **the amygdala**. They have
**strong amygdala connections**, but they are **not** the amygdala
and **not** adjacent to it. Do not import amygdala-lateralization
claims.

**Do not** assume the septal nuclei contain the **diagonal band** or
**nucleus basalis**. Both are **siblings** under the basal forebrain,
not children. The **three cholinergic nuclei** are **siblings**.

**Do not** assume the **lateral septal nucleus** is **cholinergic**.
It is **GABAergic**. Only the **medial** septal nucleus is
cholinergic.

**Do not** assume the septal nuclei have structural children beyond
``medial_septal_nuclei``. The **lateral** septal nucleus and the
**septohippocampal system** are **prose only** — they are not wired
as modules.

Iterating the septal nuclei's child (recommended consumer
pattern)::

    SEPTAL_CHILDREN = (
        "medial_septal_nuclei",
    )
    # Closed set. The lateral septal nucleus is a DOCUMENTED GAP.

Reconstructing the classical full rhinencephalon (recommended
consumer pattern)::

    # The septal nuclei are one of the five structures the
    # rhinencephalon excluded. The full union is:
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",            # THIS MODULE
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",
        ),
    }

Reconstructing the basal forebrain cholinergic system (recommended
consumer pattern)::

    # The basal forebrain cholinergic system spans THREE sibling
    # leaves. The septal nuclei contribute ONE (the medial
    # component). Union them:
    BASAL_FOREBRAIN_CHOLINERGIC = (
        "subcortical.basal_forebrain.nucleus_basalis",
        "subcortical.basal_forebrain.septal_nuclei.medial_septal_nuclei",
        "subcortical.basal_forebrain.diagonal_band_of_broca",
    )

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

Reaching the lateral septal nucleus's FUNCTIONS (recommended consumer
pattern — note the GAP)::

    # The lateral septal nucleus is NOT in the tree. Its functions
    # (reward, anxiety, fear, social behavior) are documented as
    # PROSE in this module. If you need a path for it, you must:
    #
    #   1. Note the gap in your registry.
    #   2. Optionally, document it as a "virtual" or "prose-only"
    #      node under septal_nuclei, with a clear "NOT IN TREE"
    #      marker.
    #
    # Do NOT attempt to resolve a "lateral_septal_nuclei" path
    # — it does not exist in the tree.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        sept_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.septal_nuclei"
        )
        # resolve sept_path through the memory/recall layer

References
----------
*   **Canonical septal anatomy:** Risold, P.Y., Swanson, L.W. (1997).
    "Connections of the rat lateral septal complex." *Brain Research
    Reviews* 24:115–195. (Definitive lateral septal anatomy and
    connectivity.)
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
*   **Lateral septal reward and anxiety:** Sheehan, T.P., Chambers,
    R.A., Russell, D.S. (2004). "Regulation of affect by the lateral
    septum: implications for neuropsychiatric disorders." *Progress
    in Neurobiology* 73:233–264. (Definitive lateral septal review;
    reward, anxiety, fear.)
*   **Lateral septal social behavior:** Everts, H.G.J., Koolhaas,
    J.M. (1999). "Lateral septal vasopressin in the regulation of
    social memory." *Neuroscience and Biobehavioral Reviews*
    23:1033–1042. (Lateral septal role in social recognition.)
*   **Septal deep brain stimulation for depression:** Sartorius, A.,
    et al. (2010). "Remission of major depression under deep brain
    stimulation of the lateral habenula." (Septal DBS for depression
    is a related experimental approach; limited evidence.)
*   **Septum pellucidum (distinction):** Nieuwenhuys, R., Voogd, J.,
    van Huijzen, C. (2008). *The Human Central Nervous System*, 4th
    ed. (Septum pellucidum as a midline membrane, distinct from the
    septal nuclei.)
*   **Schizophrenia septal volume (contested):** Keshavan, M.S., et
    al. (1998). "Superior temporal gyrus and the course of early
    schizophrenia." *Biological Psychiatry* 43:531–539. (Septal
    volume reductions in schizophrenia; contested.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Septal nuclei in overview.)
*   NeuroNames — Septal nuclei (left); FMA — Septal nuclei (left
    member).
"""