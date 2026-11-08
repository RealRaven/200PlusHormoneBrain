"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri
==============================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── gyri                <-- THIS MODULE

**Primary synonym:** Temporal gyri (left); Temporal convolutions;
Temporal gyral surface.
**Organizing principle:** **Structural / gyral partition** — the third
organizing principle in the temporal lobe, alongside the functional
partition (``.../temporal/cortex``) and the cytoarchitectonic partition
(``.../temporal/brodmann_areas``).
**Laterality:** left hemisphere.
**Sibling aggregators:** ``.../temporal/cortex`` (functional),
``.../temporal/brodmann_areas`` (cytoarchitectonic),
``.../temporal/sulci`` (sulcal). See "The Three Partitions" below.

Overview
--------
This module groups the **gyri** of the left temporal lobe — the
macroscopic surface convolutions that are the **structural** partition
of the temporal territory. It is the **third organizing principle** in
the temporal lobe, after the functional partition (A1/A2/ATL/ITC/pITC/MT)
and the cytoarchitectonic partition (BA15–BA48).

The three organizing principles are **complementary, non-nesting, and
coordinate** — each is a different slice through the same anatomical
territory, and each answers a different question:

*   **``cortex``** answers *"which functional region is this?"* — A1, A2,
    ATL, ITC, pITC, MT.
*   **``brodmann_areas``** answers *"which cytoarchitectonic field is
    this?"* — BA15, 20, 21, 22, 27, 28, 34, 35, 36, 37, 38, 48.
*   **``gyri``** (this module) answers *"which macroscopic surface
    convolution is this?"* — the gyral landmarks visible on every MRI.

**A gyral partition does not respect functional or cytoarchitectonic
boundaries — and the temporal gyral partition is the most structurally
complex of the four partitions in the tree.** Unlike the parietal gyri
(which contain only neocortical surface convolutions), the temporal gyri
contain **two hybrid structural-functional names** (``entorhinal_cortex``,
``perirhinal_cortex``), **one allocortical/transitional gyrus**
(``parahippocampal_gyrus``), and **one gyrus with a nested Brodmann
cross-listing** (``superior_temporal_gyrus`` → ``wernickes_area`` →
``brodmann_area_22``).

Child Modules
-------------
Seven gyri are wired under this package:

*   ``superior_temporal_gyrus`` (**STG**) — the **auditory and language
    gyrus**. Contains **A1** (Heschl's gyrus, on its superior plane),
    **A2** (the lateral STG/STS), and **BA22** (Wernicke's area) as a
    **nested cross-listing** under ``wernickes_area``. It is the
    **only gyrus in the tree that contains a nested Brodmann module**.

*   ``middle_temporal_gyrus`` (**MTG**) — the **semantic and prosodic
    gyrus**. Contains the **anterior BA21** (semantic comprehension,
    shared with ATL), the **posterior BA21** (prosodic comprehension
    on the right), and parts of **BA20** and **BA37**. It is the
    **largest gyrus in the temporal lobe** and the **principal language-
    adjacent gyral surface**.

*   ``inferior_temporal_gyrus`` (**ITG**) — the **visual semantic
    gyrus**. Contains the core **BA20** field (visual-semantic
    association) and parts of **BA37** (anterior fusiform). It is the
    **left-hemisphere visual-semantic interface** at the gyral level.

*   ``fusiform_gyrus`` (**FG**) — the **ventral occipitotemporal
    gyrus**. Contains the core **BA37** field, including the **VWFA
    (left)** and **FFA (right)**. It is the **most functionally
    lateralized gyrus in the temporal lobe** — pure parallel-laden
    (words vs. faces).

*   ``parahippocampal_gyrus`` (**PHG**) — the **medial temporal memory
    gyrus**. Contains parts of **BA27** (presubiculum), **BA28**
    (entorhinal), **BA34** (dorsal entorhinal), **BA35** (perirhinal),
    and **BA36** (perirhinal/parahippocampal). It is the **most
    allocortical gyrus in the tree** and the **principal cortical
    interface to the hippocampus**.

*   ``entorhinal_cortex`` (**EC**) — the **memory gateway hybrid
    "gyrus"**. This is **not a gyrus in the classical structural
    sense** — it is a **cytoarchitectonically defined region**
    (allocortical/periallocortical) that sits **within the
    parahippocampal gyrus**. Its presence under ``gyri/`` reflects the
    tree's choice to treat it as a **structurally addressable memory
    unit**, not as a surface convolution. **Consumers must not assume
    that ``entorhinal_cortex`` is a gyrus in the same sense as
    ``superior_temporal_gyrus``** — it is a **hybrid name**.

*   ``perirhinal_cortex`` (**PRC**) — the **object-recognition memory
    hybrid "gyrus"**. Like ``entorhinal_cortex``, this is a
    **cytoarchitectonically defined region** (periallocortical/
    proisocortical) that sits **within the parahippocampal gyrus**.
    It contains **BA35** (medial perirhinal) and **BA36** (lateral
    perirhinal). **Consumers must not assume that ``perirhinal_cortex``
    is a gyrus in the classical sense** — it is a **hybrid name**.

**Structural omissions and non-classical entries:**

*   **Temporal pole (BA38)** is **not wired as a separate gyrus** under
    ``gyri/``. It is part of the anterior temporal lobe and is reachable
    only as a Brodmann leaf (``.../temporal/brodmann_areas/brodmann_area_38``).
    This is a **structural omission** — consumers that need the temporal
    pole as a structural unit must query the Brodmann partition.
*   **Uncus** is **not wired as a separate gyrus**. It is part of the
    parahippocampal gyrus's anterior portion and the olfactory cortex's
    medial surface.
*   **Medial occipitotemporal gyrus (lingual gyrus)** is **not wired
    here** — it lives under the occipital lobe's ``gyri/`` partition
    (if wired).

The Three Partitions
--------------------
The left temporal lobe has **three organizing principles fully wired**:

::

    Functional         Cytoarchitectonic      Structural
    ──────────         ────────────────       ──────────
    cortex/            brodmann_areas/        gyri/   <-- THIS
    ├── A1             ├── BA15 (boundary)    ├── entorhinal_cortex (hybrid)
    ├── A2             ├── BA20               ├── fusiform_gyrus
    ├── ATL            ├── BA21               ├── inferior_temporal_gyrus
    ├── ITC            ├── BA22 (Wernicke)    ├── middle_temporal_gyrus
    ├── MT             ├── BA27 (piriform)    ├── parahippocampal_gyrus
    ├── pITC           ├── BA28               ├── perirhinal_cortex (hybrid)
    └── (+ MST at     ├── BA34               └── superior_temporal_gyrus
        lobe level)    ├── BA35                   └── wernickes_area
                       ├── BA36                       └── BA22 (nested)
                       ├── BA37
                       ├── BA38
                       └── BA48 (boundary)

**The three partitions are related, but not by nesting:**

*   **A1 (functional) → superior_temporal_gyrus (structural) → BA41/BA42
    (cytoarchitectonic, in the *insular* partition)** — a **cross-lobe**
    mapping: the functional and structural anchors are temporal, but the
    cytoarchitectonic anchor is insular.
*   **A2 (functional) → superior_temporal_gyrus (structural) → BA22
    (cytoarchitectonic)** — a clean three-way correspondence **with a
    nested cross-listing**.
*   **ATL (functional) → multiple gyri (structural) → multiple Brodmann
    fields (cytoarchitectonic)** — a **many-to-many** correspondence
    spanning the temporal pole, MTG, and ITG.
*   **MT (functional) → no single gyrus (structural) → BA19
    (cytoarchitectonic, in the *occipital* partition)** — MT is
    **gyrally ambiguous** because it sits at the temporo-parieto-
    occipital junction and is **not a full gyrus**.
*   **ITC (functional) → inferior_temporal_gyrus + fusiform_gyrus
    (structural) → BA20 + BA37 (cytoarchitectonic)** — a **two-gyrus,
    two-field correspondence**.
*   **pITC (functional) → fusiform_gyrus (structural) → BA37
    (cytoarchitectonic)** — a **one-gyrus, one-field correspondence**
    with the VWFA/FFA split.

**The most important consumer-facing fact about this module:** the
``gyri`` partition does **not** cover the **entire** temporal lobe
cleanly. Three kinds of non-classical entries appear:

1. **Hybrid names** — ``entorhinal_cortex`` and ``perirhinal_cortex``
   are **cytoarchitectonically defined regions** presented as "gyri".
   They are reachable via ``gyri/`` but are **not surface convolutions**.
2. **Nested cross-listing** — ``superior_temporal_gyrus/wernickes_area/
   brodmann_area_22`` is a **Brodmann leaf under a gyral path**, the
   first nested cross-listing in the tree.
3. **Structural omission** — the **temporal pole (BA38)** and the
   **uncus** are not wired as separate gyri.

Consumers that need a **complete structural partition** must query
``gyri`` **plus** the Brodmann leaves for the missing gyral names.

Function in the Human Brain
---------------------------
The gyral partition is **structural, not functional**, so it does not
have a "function" in the sense that A1, A2, ATL, ITC, pITC, and MT do.
However, each gyrus in this package **contains** functional and
cytoarchitectonic content:

*   **``superior_temporal_gyrus``** — contains **A1** (basic acoustics),
    **A2** (speech/prosody), and **BA22** (Wernicke's area). It is the
    **auditory and language gyrus**.
*   **``middle_temporal_gyrus``** — contains **BA21** (semantic
    comprehension, prosodic comprehension) and parts of **BA20/BA37**.
    It is the **semantic and prosodic gyrus**.
*   **``inferior_temporal_gyrus``** — contains **BA20**
    (visual-semantic association). It is the **visual-semantic gyrus**.
*   **``fusiform_gyrus``** — contains **BA37** (VWFA left; FFA right).
    It is the **reading and face gyrus**.
*   **``parahippocampal_gyrus``** — contains the **medial temporal
    memory structures** (BA27, BA28, BA34, BA35, BA36). It is the
    **memory gateway gyrus**.
*   **``entorhinal_cortex``** — contains **BA28 and BA34** (the
    entorhinal complex). It is the **hippocampal-neocortical gateway**
    at the gyral level.
*   **``perirhinal_cortex``** — contains **BA35 and BA36**. It is the
    **object-recognition memory** region at the gyral level.

Consumers that need the **function** of a gyrus should query its
corresponding functional-region module (A1, A2, ATL, ITC, pITC, MT) or
its cytoarchitectonic leaf (BA20–BA38), not this structural aggregator.

Lateralization Notes
--------------------
This is the **left** gyral aggregator. The gyral partition is **symmetric
by name** — both left and right temporal lobes have an STG, MTG, ITG,
fusiform, parahippocampal gyrus, entorhinal cortex, and perirhinal
cortex — but the **contents** of each gyrus are lateralized at the
functional and cytoarchitectonic levels:

*   **``superior_temporal_gyrus``** — the left STG contains **A1 left**
    (speech-weighted), **A2 left** (speech processing), and **BA22 left**
    (Wernicke's area). The right STG contains the right A2 (prosodic/
    music) and the right BA22 (**not** Wernicke's area — the name is
    inherited structurally, not functionally accurate).
*   **``middle_temporal_gyrus``** — the left MTG contains **BA21 left**
    (semantic comprehension); the right MTG contains **BA21 right**
    (prosodic comprehension).
*   **``inferior_temporal_gyrus``** — the left ITG contains **BA20 left**
    (visual-semantic naming); the right ITG contains **BA20 right**
    (non-verbal visual semantics).
*   **``fusiform_gyrus``** — the left FG contains the **VWFA** (reading);
    the right FG contains the **FFA** (face recognition).
*   **``parahippocampal_gyrus``, ``entorhinal_cortex``,
    ``perirhinal_cortex``** — these contain **bilaterally organized**
    memory structures (BA27–BA36), with only **weak** left-verbal /
    right-spatial weightings.

**A consumer that iterates the gyral partition will get a symmetric list
of names, but the functional content of each gyrus is asymmetric** —
strongly so for the STG (Wernicke's) and FG (VWFA/FFA), moderately so
for the MTG and ITG, weakly so for the parahippocampal and entorhinal/
perirhinal structures.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    occipital lobe (fusiform's occipital continuation) or the insular
    lobe (BA41/BA42). Those are **cross-lobe references**, not structural
    parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural partition, not functional or cytoarchitectonic.**
    ``__all__`` lists the seven **gyri** (including the two hybrid
    names), not the functional regions or Brodmann fields they contain.
*   **Nested cross-listing is documented as data.** The
    ``superior_temporal_gyrus/wernickes_area/brodmann_area_22`` nested
    module is the **first nested cross-listing in the tree**. The
    ``NESTED_CROSS_LISTINGS`` constant documents it.
*   **Hybrid names are flagged as data.** The ``HYBRID_NAMES`` constant
    flags ``entorhinal_cortex`` and ``perirhinal_cortex`` as
    **cytoarchitectonically defined regions**, not classical gyri.
*   **Structural omissions are flagged as data.** The
    ``MISSING_GYRI`` constant lists the **temporal pole (BA38)** and
    the **uncus** as gyral structures that are **not wired under
    ``gyri/``**.
*   **Structural parity with right temporal gyri.** Left and right
    ``gyri`` aggregators are **structurally identical** in their gyral
    list and mapping constants; only the **lateralization prose** differs.

Usage
-----
Resolve gyri by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri import (
        GYRI, HYBRID_NAMES, NESTED_CROSS_LISTINGS, MISSING_GYRI,
        CONTAINED_REGIONS, CONTAINED_BRODMANN_AREAS,
    )

    for gyrus in GYRI:
        # gyrus is a structural module name, not a functional region
        ...

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.gyri.superior_temporal_gyrus"
    )

For the nested Wernicke's-area framing (functionally named)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 — Wernicke's area, functionally framed

For the hybrid names::

    from ...temporal.gyri import HYBRID_NAMES
    # HYBRID_NAMES = ("entorhinal_cortex", "perirhinal_cortex")
    # These are cytoarchitectonically defined regions, NOT classical gyri.

For the structural omissions::

    from ...temporal.gyri import MISSING_GYRI
    # MISSING_GYRI = ("temporal_pole", "uncus")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        gyri_pkg = importlib.import_module(
            f"infrastructure.brainparts.forebrain.telencephalon."
            f"cerebral_hemispheres.{side}.cortex.temporal.gyri"
        )
        for gyrus in gyri_pkg.GYRI:
            # query the right- or left-hemisphere gyrus
            ...

References
----------
*   Terminologia Anatomica (FIPAT, 2019) — gyrus temporalis superior,
    medius, inferior; gyrus fusiformis; gyrus parahippocampalis;
    gyrus temporalis transversus (Heschl).
*   Ono, M., Kubik, S., & Abernathey, C.D. (1990). *Atlas of the Cerebral
    Sulci*. (Gyral and sulcal anatomy of the temporal lobe.)
*   Duvernoy, H.M. (1999). *The Human Brain: Surface, Three-Dimensional
    Sectional Anatomy with MRI, and Blood Supply*. (Temporal gyral
    landmarks on MRI.)
*   **Heschl's gyrus and transverse temporal gyri:** *Heschl's gyrus —
    an overview* (ScienceDirect). The primary auditory cortex is
    located on the **posteromedial two-thirds of the first transverse
    temporal gyrus (Heschl's gyrus)**.
*   **Superior temporal gyrus and Wernicke's area:** Wernicke, C. (1874).
    *Der aphasische Symptomencomplex*. (Wernicke's area on the posterior
    STG.)
*   **Fusiform gyrus VWFA/FFA parallel-laden:** Kanwisher, N., et al.
    (1997). "The fusiform face area: a module in human extrastriate
    cortex specialized for face perception." *J Neurosci*, 17(11),
    4302–4311; Cohen, L., et al. (2000). "The visual word form area."
    *Brain*, 123(2), 291–307.
*   **Parahippocampal gyrus and medial temporal memory:** Squire, L.R., &
    Zola-Morgan, S. (1991). "The medial temporal lobe memory system."
    *Science*, 253(5026), 1380–1386.
*   **Entorhinal cortex as gateway:** Witter, M. (2011). "Entorhinal
    cortex." *Scholarpedia*, 6(10), 4380. (Major gateway between the
    hippocampal formation and the neocortex.)
*   **Perirhinal cortex:** *Perirhinal Cortex — an overview*
    (ScienceDirect). (Object-recognition and familiarity memory.)
*   **Cytoarchitectonic parcellation of the fusiform gyrus:** Caspers,
    S., et al. (2013). (FG1 and FG2 subdivisions; FG2 lateralized for
    visual language on the left, face processing on the right.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Temporal gyral and sulcal landmarks.)
*   NeuroNames — Temporal gyri (left); FMA — left temporal lobe partonomy.
"""