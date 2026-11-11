"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical
=======================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            ├── cortex
            ├── rhinencephalon
            ├── subcortical   <-- THIS MODULE
            └── white_matter

**Primary synonym:** Subcortical structures (telencephalic); subcortical
grey matter (telencephalic); basal telencephalon (partial).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container node** — the parent of five subcortical children.
**Part of:** The **telencephalon** — specifically the **subcortical
component** of the left cerebral hemisphere.
**Structural parent:** ``.../cerebral_hemispheres/left/`` → **sibling of
``cortex/``, ``rhinencephalon/``, and ``white_matter/``**.
**Structural children (five, closed set):**
``basal_forebrain``, ``basal_ganglia``, ``claustrum``,
``extended_amygdala``, ``medial_temporal_lobe``.
**Boundary status (not diencephalon):** **Boundary case — telencephalic
subcortical only.** The subcortical container holds **telencephalic**
structures. The **thalamus, hypothalamus, epithalamus, and subthalamus**
are **diencephalic** and live under
``.../forebrain/diencephalon/`` — **not** here. Consumers resolving
"subcortical" broadly must **union** this module with
``.../forebrain/diencephalon/`` to get the full subcortical grey matter
of the forebrain.
**Boundary status (not brainstem):** **Boundary case — telencephalic
only.** The **midbrain, pons, and medulla** are under
``.../midbrain/`` and ``.../hindbrain/`` — **not** here. The
subcortical container does **not** extend below the forebrain.
**Boundary status (not rhinencephalon):** **Boundary case — the
olfactory structures the rhinencephalon excluded live here.** The
rhinencephalon deliberately excludes the **amygdala**, **hippocampus**,
**septal nuclei**, **olfactory tubercle**, and **anterior perforated
substance** — and those structures live **here**, under the
subcortical children (``medial_temporal_lobe/``, ``basal_forebrain/``).
Consumers that need the **olfactory components** of those structures
must resolve them **through their subcortical modules**, not through
the rhinencephalon. See *The Subcortical/Rhinencephalon Boundary*
below.
**Boundary status (not cortex):** **Boundary case — "subcortical" is a
structural convenience, not a cytological claim.** Not all subcortical
children are "subcortical" in the same sense:
*   ``basal_ganglia`` and ``basal_forebrain`` are **deep grey-matter
    nuclei** — genuinely subcortical.
*   ``medial_temporal_lobe`` houses the **amygdala** (partly
    corticoid) and **hippocampus** (archicortex) — **cortical-like**
    structures placed here for structural grouping, not because they
    are "subcortical" cytologically.
*   ``claustrum`` is a **thin grey-matter sheet** between the insula
    and putamen — "subcortical" by position, but not a deep nucleus.
Consumers must not treat "subcortical" as a **cytological**
category; it is a **structural grouping** of telencephalic grey matter
that is neither neocortical nor allocortical-olfactory nor white
matter.
**Boundary status (not white matter):** **Boundary case — grey matter
only.** The subcortical container holds **grey matter** (nuclei,
cortex-like sheets). The **white-matter tracts** of the hemisphere
(internal capsule, corona radiata, corpus callosum, fornix, etc.) are
under ``.../left/white_matter/`` — **not** here. Consumers resolving
"subcortical" and expecting white matter will be **misled**.

Overview
--------
The subcortical container is the **structural home for telencephalic
grey matter that is neither neocortical nor allocortical-olfactory**.
It contains **five children**, ranging from deep nuclei (basal
ganglia) to cortex-like structures (amygdala, hippocampus) to a thin
grey-matter sheet (claustrum). It is the **deepest and most
heterogeneous** of the four left-hemisphere containers.

**The five children are structurally diverse.** They are not a single
functional system — they are a **structural grouping** of grey matter
that does not fit the neocortical, allocortical-olfactory, or
white-matter containers:

*   ``basal_forebrain`` — the **medial/ventral basal telencephalon**:
    anterior perforated substance, diagonal band of Broca, lamina
    terminalis, nucleus basalis, septal nuclei, substantia
    innominata. These are **deep nuclei** and **basal cortical
    regions** — genuinely subcortical.

*   ``basal_ganglia`` — the **dorsal and ventral striatum** (caudate,
    putamen, nucleus accumbens, olfactory tubercle) and the **globus
    pallidus** (with ventral pallidum). These are **deep grey-matter
    nuclei** — genuinely subcortical.

*   ``claustrum`` — a **thin grey-matter sheet** between the insula
    and the putamen. "Subcortical" by **position** (deep to the
    insular cortex), but not a **deep nucleus** in the same sense as
    the basal ganglia. Its function is still debated.

*   ``extended_amygdala`` — the **extended amygdala** and its
    **stria terminalis / bed nucleus of the stria terminalis**. A
    **limbic-forebrain continuum** bridging the amygdala and the
    basal forebrain.

*   ``medial_temporal_lobe`` — the **amygdala** (partly corticoid
    nuclei) and the **hippocampus** (archicortex). These are the
    **most cortical-like** of the subcortical children; they are
    grouped here for **structural convenience**, not because they
    are "subcortical" cytologically.

**"Subcortical" is a structural convenience, not a cytological
claim.** This is the subcortical container's **defining caveat**. The
five children are not a single kind of tissue; they are a **structural
grouping** of telencephalic grey matter that does not fit the
neocortical, allocortical-olfactory, or white-matter containers. The
amygdala and hippocampus are **cortex-like**; the claustrum is a
**sheet**; the basal ganglia and basal forebrain are **deep nuclei**.
Consumers must not treat "subcortical" as a **cytological** category.

**The subcortical container is the deepest in the left hemisphere.**
Its children themselves have children (``basal_ganglia/striatum/dorsal_striatum/caudate_nucleus/``,
``medial_temporal_lobe/hippocampus/cornu_ammonis/ca1/``, etc.), so the
subcortical container is a **multi-level tree**, not a flat one.
Consumers iterating the subcortical container must be prepared to
recurse.

Container Contents (five children, closed set)
----------------------------------------------
The subcortical container has **exactly five children**. Consumers may
iterate them, but should not assume any others exist:

*   **``basal_forebrain``** — the **medial/ventral basal
    telencephalon**. Children: ``anterior_perforated_substance``,
    ``diagonal_band_of_broca``, ``lamina_terminalis`` (→
    ``vascular_organ_of_lamina_terminalis``), ``nucleus_basalis``,
    ``septal_nuclei`` (→ ``medial_septal_nuclei``),
    ``substantia_innominata``. **Depth: three levels** (some
    grandchildren). Genuinely subcortical (deep nuclei and basal
    cortical regions).

*   **``basal_ganglia``** — the **dorsal and ventral striatum** and
    the **globus pallidus**. Children: ``globus_pallidus`` (→
    ``ventral_pallidum``) and ``striatum`` (→ ``dorsal_striatum`` →
    ``caudate_nucleus``, ``putamen``; ``ventral_striatum`` →
    ``nucleus_accumbens``, ``olfactory_tubercle``). **Depth: four
    levels** (deepest child in the subcortical container).
    Genuinely subcortical (deep grey-matter nuclei).

*   **``claustrum``** — a **thin grey-matter sheet** between the
    insula and the putamen. **Depth: leaf (no children).** A
    "subcortical" sheet by position, not a deep nucleus.

*   **``extended_amygdala``** — the **extended amygdala** and its
    **stria terminalis / bed nucleus of the stria terminalis**.
    Child: ``stria_terminalis`` (→
    ``bed_nucleus_of_stria_terminalis``). **Depth: two levels.** A
    **limbic-forebrain continuum** bridging the amygdala and the
    basal forebrain.

*   **``medial_temporal_lobe``** — the **amygdala** and the
    **hippocampus**. Children: ``amygdala`` (with its own children
    including ``main_olfactory_system``, ``accessory_olfactory_system``,
    ``basolateral_nuclei``, ``central_nucleus``, ``lateral_nucleus``,
    ``medial_nucleus``, etc.) and ``hippocampus`` (→
    ``cornu_ammonis`` → ``ca1``/``ca2``/``ca3``/``ca4``;
    ``dentate_gyrus``, ``parasubiculum``, ``presubiculum``,
    ``subiculum``). **Depth: five levels** (deepest branch in the
    telencephalon). Cortical-like structures (partly corticoid
    amygdala; archicortical hippocampus) placed here for structural
    grouping.

**Not children (deliberately excluded):**
*   **Diencephalic structures** (thalamus, hypothalamus, epithalamus,
    subthalamus) → ``.../forebrain/diencephalon/``.
*   **Brainstem structures** (midbrain, pons, medulla) →
    ``.../midbrain/`` and ``.../hindbrain/``.
*   **Neocortical structures** → ``.../left/cortex/``.
*   **Allocortical olfactory structures** (piriform, periamygdaloid,
    olfactory bulb/tract/AON, uncus) → ``.../left/rhinencephalon/``.
*   **White-matter tracts** → ``.../left/white_matter/``.
*   **Lateral ventricles** → ``.../telencephalon/lateral_ventricles/``
    (not under subcortical).

The Subcortical/Rhinencephalon Boundary
---------------------------------------
This is the **most consequential boundary** for consumers building an
olfactory or limbic registry. The rhinencephalon **deliberately
excluded** the following structures, and they live **here**:

*   **Amygdala** → ``subcortical/medial_temporal_lobe/amygdala/``.
    Its **``main_olfactory_system``** child is the amygdala's
    **nuclear** olfactory component — distinct from the
    **periamygdaloid cortex** (which is the **cortical** surface
    over the amygdala, wired under the rhinencephalon).

*   **Hippocampus** → ``subcortical/medial_temporal_lobe/hippocampus/``.
    Classical anatomy sometimes grouped the hippocampus with the
    rhinencephalon; the tree **excludes** it and places it here.

*   **Septal nuclei** → ``subcortical/basal_forebrain/septal_nuclei/``.
    The **medial olfactory stria** target, classically rhinencephalic;
    the tree places it here.

*   **Olfactory tubercle** →
    ``subcortical/basal_forebrain/striatum/ventral_striatum/olfactory_tubercle/``.
    A primary olfactory target, classically rhinencephalic; the tree
    places it **inside the ventral striatum** — a deliberate boundary
    choice that reflects its striatal-like cytoarchitecture.

*   **Anterior perforated substance** →
    ``subcortical/basal_forebrain/anterior_perforated_substance/``.
    The grey matter through which the lenticulostriate arteries pass;
    classically rhinencephalic; the tree places it here.

**Consumers that need the "full classical rhinencephalon"** must
**union** the rhinencephalon container with these five subcortical
structures. The rhinencephalon's narrow definition is documented in
its own module; the subcortical container is the **structural home**
of the excluded structures.

The Subcortical/Cortex Boundary
-------------------------------
This boundary is **less sharp than it looks**, because "subcortical"
is a structural convenience:

*   **``claustrum``** — "subcortical" by **position** (deep to the
    insula), but a **grey-matter sheet**, not a deep nucleus. Its
    function (consciousness? salience? inter-areal coordination?) is
    still debated.

*   **``medial_temporal_lobe/amygdala``** — the **corticomedial
    nuclei** are **cortex-like** (allocortical), and the
    **basolateral nuclei** are **nucleus-like**. The amygdala is
    grouped here for **structural convenience**, not because it is
    entirely "subcortical."

*   **``medial_temporal_lobe/hippocampus``** — the **archicortex**
    (three-layered) of the hippocampus is **cortex-like**, and its
    **subiculum** is a **transitional cortex**. Grouped here for
    structural convenience.

**Consumers that need "all cortical-like telencephalic grey matter"**
must **union** ``cortex/`` + ``rhinencephalon/`` + the
``medial_temporal_lobe/`` component of ``subcortical/``. The tree's
"subcortical" grouping is a **structural convenience**, not a
**cytological category**.

Function in the Human Brain
---------------------------
The subcortical container has **no single function** — it is a
**structural grouping** of five functionally distinct children:

*   **``basal_ganglia``** — motor control, action selection,
    reinforcement learning, habit formation, reward.
*   **``basal_forebrain``** — cortical activation (nucleus basalis,
    cholinergic), septal-hippocampal theta, reward (septal nuclei),
    olfactory relay (anterior perforated substance, diagonal band).
*   **``claustrum``** — function debated; implicated in
    **inter-areal coordination**, **salience**, and possibly
    **consciousness**.
*   **``extended_amygdala``** — **limbic-forebrain continuum**:
    stress, anxiety, fear, reward, autonomic regulation.
*   **``medial_temporal_lobe``** — **memory** (hippocampus),
    **emotion** (amygdala), **olfactory-limbic integration** (both).

**The unifying theme:** the subcortical container houses the
**telencephalic grey matter that is not neocortical, not
allocortical-olfactory, and not white matter**. It is a **structural
grouping**, not a functional system. Consumers must read each child's
own module for its functions.

Associated Disorders
--------------------
The subcortical container has **no single syndrome** — its children's
disorders are documented in their own modules:

*   **Basal ganglia** — Parkinson's, Huntington's, dystonia, OCD,
    addiction (via the ventral striatum).
*   **Basal forebrain** — Alzheimer's (nucleus basalis
    cholinergic loss), septal-hippocampal amnesia, olfactory
    dysfunction (anterior perforated substance, diagonal band).
*   **Claustrum** — no named syndrome; implicated in
    consciousness-related phenomena (rare lesion case reports).
*   **Extended amygdala** — anxiety disorders, PTSD, addiction,
    stress-related disorders.
*   **Medial temporal lobe** — hippocampal amnesia, Alzheimer's,
    temporal lobe epilepsy, fear conditioning deficits, Kluver-Bucy
    syndrome (amygdala), olfactory-limbic deficits.

**What is NOT here:** The subcortical container is **not** the
substrate for **neocortical syndromes** (aphasias, agnosias,
apraxias), **diencephalic syndromes** (thalamic pain, hypothalamic
syndromes), or **brainstem syndromes** (cranial nerve palsies,
respiratory failure). Those are documented in their own modules. The
subcortical container houses the **telencephalic subcortical
substrates** for motor, limbic, reward, memory, and olfactory-limbic
disorders.

Lateralization Notes
--------------------
This is the **left** subcortical container. Its **five children** are
**not uniformly lateralized**:

*   **Bilaterally symmetric (presumed):** ``basal_ganglia``,
    ``basal_forebrain``, ``claustrum``, ``extended_amygdala`` —
    structurally symmetric, no strong functional lateralization
    established.

*   **Partial lateralization (amygdala):** The **right amygdala** is
    sometimes reported as **more involved in fear processing**; the
    **left amygdala** as **more involved in verbal/semantic
    processing**. **This is a partial lateralization**, and it is
    documented in the **amygdala module**, **not** in this container.

*   **Partial lateralization (hippocampus):** The **left
    hippocampus** is sometimes reported as **more involved in verbal
    memory**; the **right hippocampus** as **more involved in
    spatial memory**. **This is a partial lateralization**, and it is
    documented in the **hippocampus module**, **not** in this
    container.

**The container itself is neither lateralized nor non-lateralized.**
Its **children** have their own lateralization profiles, documented in
their own modules. Consumers must **not** import container-level
lateralization claims into any child; the container is a **structural
grouping**, and its lateralization is **the sum of its children's
lateralizations**, which are themselves partial.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``rhinencephalon/``, ``white_matter/``, or
    ``.../diencephalon/``. The subcortical container's relationships
    to those partitions are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — five children, closed set.** The subcortical
    container has exactly five children: ``basal_forebrain``,
    ``basal_ganglia``, ``claustrum``, ``extended_amygdala``,
    ``medial_temporal_lobe``. Consumers may iterate them, but should
    not assume any others exist.
*   **"Subcortical" is a structural convenience, not a cytological
    claim.** The five children are **not** a single kind of tissue.
    They range from deep nuclei (basal ganglia) to cortex-like
    structures (amygdala, hippocampus) to a thin grey-matter sheet
    (claustrum). Consumers must not treat "subcortical" as a
    **cytological category**.
*   **Telencephalic only — not diencephalic, not brainstem.** The
    subcortical container holds **telencephalic** structures only.
    The diencephalon (thalamus, hypothalamus, epithalamus,
    subthalamus) is under ``.../forebrain/diencephalon/``. The
    brainstem (midbrain, pons, medulla) is under ``.../midbrain/``
    and ``.../hindbrain/``. Consumers resolving "subcortical"
    broadly must **union** this module with the diencephalon for the
    full forebrain subcortical grey matter.
*   **The rhinencephalon's excluded structures live here.** The
    amygdala, hippocampus, septal nuclei, olfactory tubercle, and
    anterior perforated substance are **here**, not in the
    rhinencephalon. Consumers that need the **classical full
    rhinencephalon** must **union** the rhinencephalon with these
    five subcortical structures.
*   **Grey matter only — not white matter.** The subcortical container
    holds **grey matter**. White-matter tracts are under
    ``.../left/white_matter/``. Consumers resolving "subcortical" and
    expecting white matter will be **misled**.
*   **Deep, multi-level tree — prepared to recurse.** The subcortical
    container's children themselves have children (up to **five
    levels deep** — e.g., ``medial_temporal_lobe/hippocampus/cornu_ammonis/ca1/``).
    Consumers iterating the subcortical container must be prepared to
    **recurse**, not just iterate one level.
*   **No ``AREA_PATHS`` hop.** The subcortical container is a local
    container, not a cross-listed leaf.
*   **No nested cross-listing.** The subcortical container has no
    nested dual-framing module. It is a single container.
*   **Structural parity with right subcortical container.** Left and
    right subcortical containers are **structurally identical** —
    same five children, same depth, same "structural convenience"
    caveat, same rhinencephalon-exclusion redirects.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left import subcortical

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical"
    )

**Do not** assume the subcortical container is under ``cortex/`` or
``rhinencephalon/``. It is a **sibling** of both. A consumer that
iterates ``cortex/`` or ``rhinencephalon/`` and expects to find the
subcortical structures there will **miss them**.

**Do not** assume the subcortical container is a **flat structure**.
It is a **deep, multi-level tree** (up to five levels). Consumers
must be prepared to **recurse**.

**Do not** assume "subcortical" means **cytologically subcortical**.
The container holds deep nuclei (basal ganglia), cortex-like
structures (amygdala, hippocampus), and a grey-matter sheet
(claustrum). "Subcortical" is a **structural convenience**, not a
cytological claim.

**Do not** assume the subcortical container holds **white matter**.
White-matter tracts are under ``.../left/white_matter/``.

**Do not** assume the subcortical container holds **diencephalic or
brainstem structures**. The diencephalon is under
``.../forebrain/diencephalon/``; the brainstem is under
``.../midbrain/`` and ``.../hindbrain/``.

Iterating the subcortical container's five children (recommended
consumer pattern)::

    SUBCORTICAL_CHILDREN = (
        "basal_forebrain",
        "basal_ganglia",
        "claustrum",
        "extended_amygdala",
        "medial_temporal_lobe",
    )
    # Closed set. Do not assume additional children.

Recursive iteration over the subcortical tree (recommended consumer
pattern)::

    # The subcortical container is up to five levels deep. Recurse
    # over it rather than iterating one level.
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca1
    #
    # is a valid leaf; so is
    #
    #   subcortical.basal_ganglia.striatum.dorsal_striatum.caudate_nucleus
    #
    # Do not stop at the first level.

Reconstructing the classical full rhinencephalon (recommended
consumer pattern)::

    # The rhinencephalon's narrow definition excludes five
    # structures that classical anatomy includes. Union them:
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",
        ),
    }
    # This is the classical "smell brain + limbic lobe" grouping.
    # The tree's narrow definition is documented in the rhinencephalon
    # module; the excluded structures live here.

Reconstructing the full forebrain subcortical grey matter
(recommended consumer pattern)::

    # "Subcortical" in the broad forebrain sense includes BOTH
    # telencephalic subcortical (this module) AND diencephalic
    # structures. Union them:
    FOREBAIN_SUBCORTICAL = {
        "telencephalon.left.subcortical": SUBCORTICAL_CHILDREN,
        "forebrain.diencephalon": (
            "thalamus",
            "hypothalamus",
            "epithalamus",
            "subthalamus",
            "third_ventricle",
            "pituitary_gland",
            "subcommissural_organ",
        ),
    }
    # The tree splits them; consumers that want "all subcortical"
    # must union.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        sub_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical"
        )
        # resolve sub_path through the memory/recall layer

References
----------
*   **Telencephalic subcortical anatomy:** Heimer, L. (2008). *The
    Human Brain and Spinal Cord: Functional Neuroanatomy and
    Dissection Guide*, 3rd ed. (Basal ganglia, basal forebrain,
    amygdala, hippocampus, claustrum as telencephalic subcortical
    structures.)
*   **Basal ganglia:** Graybiel, A.M. (2008). "Habits, rituals, and
    the evaluative brain." *Annual Review of Neuroscience* 31:359–387.
    (Functional overview of the basal ganglia.)
*   **Basal forebrain:** Mesulam, M.-M., Mufson, E.J., Levey, A.I.,
    Wainer, B.H. (1983). "Cholinergic innervation of cortex by the
    basal forebrain." *Journal of Comparative Neurology* 214:170–197.
    (Nucleus basalis and basal forebrain cholinergic system.)
*   **Claustrum:** Crick, F.C., Koch, C. (2005). "What is the function
    of the claustrum?" *Philosophical Transactions of the Royal
    Society B* 360:1271–1279. (Claustrum function and its debated
    role.)
*   **Extended amygdala:** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special relevance
    for neuropsychiatric disorders." *Neuroscience* 27:1–39.
    (Extended amygdala as a limbic-forebrain continuum.)
*   **Medial temporal lobe:** Amaral, D.G., Insausti, R. (1990). "The
    hippocampal formation." In *The Human Nervous System*
    (Paxinos, G., ed.). (Hippocampus and amygdala as medial temporal
    lobe structures.)
*   **Rhinencephalon exclusion:** Nieuwenhuys, R., Voogd, J., van
    Huijzen, C. (2008). *The Human Central Nervous System*, 4th ed.
    (Narrow olfactory definition; amygdala and hippocampus as
    separate limbic structures.)
*   **Subcortical/cortical boundary:** Swanson, L.W. (2003). *Brain
    Architecture: Understanding the Basic Plan*. (Structural
    groupings and the limits of "cortical" vs. "subcortical"
    categories.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Telencephalic subcortical structures in
    overview.)
*   NeuroNames — Subcortical structures (left); FMA — Subcortical
    structures (left member).
"""