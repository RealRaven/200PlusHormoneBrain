"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas.brodmann_area_26
=========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── brodmann_areas
                        └── brodmann_area_26   <-- THIS MODULE

**Primary synonym:** Brodmann Area 26 (BA26); **Ectosplenial area**;
**Ectosplenial cortex**.
**Cytoarchitectonic designation:** Area 26 of Brodmann (1909). In the
retrosplenial region, Brodmann defined three areas: area 26 (ectosplenial
cortex) in the granular part, area 29 (granular retrosplenial cortex), and
area 30 (agranular retrosplenial cortex).
**Part of:** The **retrosplenial region**, a transitional zone between the
hippocampal formation and the isocortical posterior cingulate gyrus.
**Location:** A narrow band located in the **isthmus of the cingulate
gyrus**, adjacent to the fasciolar gyrus internally, just posterior to the
splenium of the corpus callosum, in the right hemisphere.

Overview
--------
Brodmann Area 26 (BA26) is the **ectosplenial area** — the most primitive and
medial component of the retrosplenial region. It is cytoarchitectonically
distinct: its laminar pattern comprises a molecular layer, a cell-dense
external layer of small pyramidal cells, and an inner layer resembling the
neuronal population of layer VI of the isocortex. It is the
first step in a **stepwise transition** from the simple allocortical
structure of the supracommissural hippocampus, through areas 26, 29, and 30,
to the elaborated six-layered isocortex of area 23.

**Critical boundary note: BA26 is a *boundary case*.** It sits on the
cingulate/retrosplenial–parietal border. It is a parietal Brodmann field by
virtue of its inclusion in Brodmann's parietal listing, but its anatomical
home is the **retrosplenial/cingulate** territory. This module is therefore
**also wired** under
``.../right/cortex/cingulate/brodmann_areas/brodmann_area_26_retrosplenial``.
This duplication is intentional. Consumers that union the ``brodmann_areas``
of the cingulate and parietal lobes **must deduplicate by area number**.

This module is structurally identical to the left-hemisphere twin at
``.../left/cortex/parietal/brodmann_areas/brodmann_area_26``. The
**cytoarchitectonic identity and the majority of the intrinsic functional
roles of BA26 are the same in both hemispheres**. Unlike the left-loaded
BA1/BA2/BA5 pattern and the right-loaded BA7 pattern, **BA26 is a
*symmetric-with-one-asymmetry* module**: most functions are bilateral, and
exactly **one** function is lateralized — and it is lateralized **in opposite
directions** on the two sides (left: lexical-semantic; right: encoding).
That asymmetry is documented below.

Function in the Human Brain
---------------------------
BA26 is a small paralimbic transition zone with functions that bridge
memory, emotion, and spatial cognition. Its best-supported roles are:

*   **Autobiographical and Episodic Memory:** BA26 is part of the
    retrosplenial memory system. The retrosplenial cortex, of which BA26 is a
    component, is one of several brain areas that produce **anterograde
    amnesia** when damaged. It is involved in the **retrieval and
    encoding of episodic and autobiographical memories** and in **topographical
    and topokinetic memory** (memory for routes and spatial layouts).

*   **Default Mode Network (DMN) Connectivity:** BA26 is functionally
    connected to the **posterior default mode network**. The
    posterior cingulate/retrosplenial region (including BA26, 29, and 30) is
    a core node of the DMN, a network that shows increased activity during
    autobiographical memory retrieval and future planning.

*   **Integration of Affective and Mnemonic Information:** BA26 serves as a
    **transition region** between the posterior cingulate cortex and the
    temporal lobe, integrating **emotional and mnemonic** signals.

*   **Right-Lateralized Memory Encoding (present here, absent on the left):**
    The broader posterior cingulate/retrosplenial cluster shows
    **right-lateralized** activation for the **encoding of words and faces**.
    This is a **right-hemisphere property** of the retrosplenial cluster and
    is documented here, **not** in the left BA26 twin.

*   **Motor Learning (Non-Initiation):** Unlike more anterior cingulate
    regions, BA26 is **not** involved in the initiation of motor actions but
    is active during **motor learning**, including the learning of complex
    movements.

*   **Fear Conditioning and Self/Other Distinction:** The broader posterior
    cingulate cluster (including BA26) has been implicated in **fear
    conditioning** and in the **distinction between self and other**.

Associated Disorders
--------------------
Dysfunction of BA26 is rarely seen in isolation. It is most commonly affected
together with adjacent areas **BA23, BA29, and BA30**. Reported associations
include:

*   **Anterograde Amnesia:** Damage to the retrosplenial region, including
    BA26, can produce **anterograde amnesia** — an inability to form new
    declarative memories.

*   **PTSD (Findings Reported):** Reduced blood flow in BA26 has been
    reported in PTSD, particularly during **triggered memories**.

*   **Early Default Mode Network Disruption:** The posterior cingulate region
    (of which BA26 is a component) is a DMN hub and shows **early anatomical
    connectivity loss in Alzheimer's disease**.

**Note on syndrome attribution:** BA26 is **not** a classical lesion-syndrome
node in the way that BA39 (Gerstmann) or BA7 (neglect) are. Its clinical
relevance is as part of the **retrosplenial memory system** and the **posterior
DMN**, not as a standalone cortical field with a named syndrome. Consumers
should treat BA26 as a **contributor** to retrosplenial/DMN function, not as
a primary syndrome substrate.

Lateralization Notes
--------------------
This is the **right** hemisphere BA26 module.

*   **Right-Lateralized Memory Encoding (unique to this twin):** The broader
    posterior cingulate/retrosplenial cluster shows **right-lateralized**
    activation for the **encoding of words and faces**. This is the
    principal lateralized function attributable to BA26 on the right side.

*   **No Left-Lateralized Lexical-Semantic Role.** The **lexical-semantic
    processing** and **semantic emotional information processing** functions
    of the posterior cingulate cluster are **left-lateralized**. They are
    documented in the left BA26 twin and are **absent from this module**.
    Do **not** inherit the left twin's lexical-semantic claim into this
    right-hemisphere module — the left twin's claim and this module's
    denial are the **complementary halves of the same asymmetry**, not
    contradictory claims.

*   **No Neglect Role.** Unlike right BA7 and the right inferior parietal
    lobule, BA26 is **not** a node of the spatial-attention / neglect network.
    It sits in the retrosplenial memory/DMN system, not the dorsal attention
    network. This is the one place in the **right** parietal Brodmann set
    where a right-hemisphere module does **not** carry a neglect claim —
    the claim belongs to right BA7/BA39/BA40/TPJ territory, not to BA26.

*   **No Stereognosis or Praxis Role.** BA26 is not part of the S1 or praxis
    networks. Do not inherit the stereognosis or apraxia claims from BA1, BA2,
    or BA5.

*   **Symmetric Functions (copied verbatim from the left twin):** The
    following functions are **bilateral properties** of the retrosplenial
    region and are documented identically in both BA26 twins:
    - Autobiographical and episodic memory.
    - DMN connectivity.
    - Affective–mnemonic integration.
    - Motor learning.
    - Fear conditioning and self/other distinction.

Design Contract
---------------
*   **No side effects on import.** This `__init__.py` is a pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No hormone imports here.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cross-listing with cingulate.** This module is a **duplicate** of the
    cingulate BA26 entry at
    ``.../right/cortex/cingulate/brodmann_areas/brodmann_area_26_retrosplenial``.
    Consumers that iterate Brodmann areas across lobes **must deduplicate by
    area number**. This is the same boundary case flagged in the parent
    ``brodmann_areas`` package's ``ITERABLE_AREAS`` and ``AREA_PATHS``
    contracts.
*   **Retrosplenial transition zone.** BA26 is the most primitive (allocortical)
    component of the retrosplenial region. It should not be conflated with the
    adjacent isocortical BA23 (posterior cingulate) or with the granular BA29 /
    agranular BA30. The laminar transition is the defining cytoarchitectonic
    feature.
*   **Structural parity with left BA26.** Left and right BA26 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. Only the path segment (`right` vs `left`) and the
    lateralization prose differ. **However** — this module carries one
    right-lateralized claim (encoding) that the left twin does not, and the
    left twin carries one left-lateralized claim (lexical-semantic) that this
    module does not. The two modules are structurally parallel but **not**
    content-identical, and the asymmetry is **symmetric in magnitude**: each
    side has exactly one lateralized function, and the two functions are
    different.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas import brodmann_area_26

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.brodmann_areas.brodmann_area_26"
    )

Bilateral iteration (recommended consumer pattern, with deduplication)::

    seen_areas = set()
    for side in ("left", "right"):
        ba26_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.brodmann_areas.brodmann_area_26"
        )
        # resolve ba26_path; skip if "26" in seen_areas

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
*   von Economo, C., & Koskinas, G.N. (1925). *Die Cytoarchitektonik der
    Hirnrinde des erwachsenen Menschen*. (Retrosplenial subdivisions LB2, LD,
    LE1, LE2, LF1, LF2; LE2/LE1/LD correspond to BA26/29/30.)
*   Rose, M. (1928). *J Psychol Neurol*, 37, 467–624. (Granular vs agranular
    retrosplenial subdivision.)
*   Braak, H. (1979). *Z Mikrosk Anat Forsch*, 93(3), 469–486. (Primitive
    laminar pattern of ectosplenial area 26.)
*   Vogt, B.A., et al. (2001). *Cingulate Neurobiology and Disease*. (Retrosplenial
    connectivity and subdivisions.)
*   Neurofeedback Academy — Brodmann Area 26 (Ectosplenial Cortex). (Memory,
    DMN, paralimbic functions.)
*   NeuroWiki (Denmark) — BA 26. (Right-lateralized memory encoding for words
    and faces; contrast with the left-lateralized lexical-semantic findings;
    memory and motor-learning functions.)
*   ScienceDirect — Retrosplenial Region (Areas 26, 29, and 30 of Brodmann).
    (Cytoarchitecture and retrosplenial transition zone.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Brodmann area 26 (right); FMA — Brodmann area 26 (right member).
"""