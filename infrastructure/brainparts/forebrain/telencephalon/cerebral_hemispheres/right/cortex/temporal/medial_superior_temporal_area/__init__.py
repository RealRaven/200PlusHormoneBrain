"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.medial_superior_temporal_area
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── medial_superior_temporal_area   <-- THIS MODULE

**Primary synonym:** Medial superior temporal area (MST), right; **V5a**;
MST/V5a; Medial superior temporal visual area; Dorsal medial superior
temporal area.
**Organizing principle:** **Standalone functional node at the LOBE level**
— **not** a child of the functional `cortex/` partition, **not** a gyral
leaf, **not** a Brodmann leaf. See "Standalone-Node Status" below.
**Functional family:** **Motion-processing** — the **optic-flow and
egomotion companion** of the middle temporal visual area (MT/V5).
**Location:** The **dorsal/posterior bank of the superior temporal
sulcus (STS)** and the **adjacent lateral occipitotemporal cortex**, at
the **temporo-parieto-occipital junction**, just **posterior and dorsal
to MT/V5**.
**Structural parent:** Direct child of ``.../temporal`` (the lobe-level
aggregator) — **sibling** of the four partitions (``brodmann_areas``,
``cortex``, ``gyri``, ``sulci``), not a child of any of them.
**Cytoarchitectonic type:** **Neocortical (granular)** — an
**extrastriate visual association area** with a **dense layer IV** and
**large layer III pyramidal cells**, similar to MT but **less heavily
myelinated**.

Overview
--------
The **right medial superior temporal area (MST)** is the **right-hemisphere
optic-flow and self-motion hub** — the **dominant hemisphere for
egomotion, heading perception, and structure-from-motion** in the human
brain, and the **motion-in-depth companion** of the adjacent MT/V5 area.
Where MT analyses **local motion** (direction and speed of moving elements
in the visual field), **MST analyses global motion** — the **optic flow**
that results from the observer's own movement through the environment.
The right MST is therefore the **principal cortical substrate for the
perception of self-motion**, and it supports the **visually guided
control of navigation and locomotion**.

**This is the right-hemisphere twin of the left MST, and the pair is
RIGHT-DOMINANT for its core functions.** Unlike the left-loaded
(asymmetric-by-function, left-verbal) or parallel-laden (fusiform gyrus)
patterns documented elsewhere in the temporal lobe, MST's lateralization
is a **sensory-domain weighting**: the right hemisphere is **dominant**
for optic-flow, egomotion, and heading, and the left hemisphere is the
**contra-lateral specialist**. This is the **same pattern** already
documented in the adjacent MT/V5 area — the two motion-processing
companions share the same right-dominant sensory weighting.

**MST is the first STANDALONE FUNCTIONAL NODE at the lobe level in the
tree** — and it is the **only module in the temporal lobe that is not
wired under any of the four partitions** (``brodmann_areas``,
``cortex``, ``gyri``, ``sulci``). It is a **direct child of the lobe
aggregator** ``.../temporal``, sitting as a **sibling** to the four
partitions:

::

    temporal/
    ├── brodmann_areas/
    ├── cortex/
    ├── gyri/
    ├── medial_superior_temporal_area/   <-- THIS MODULE (standalone)
    └── sulci/

**Why is MST wired as a standalone node instead of under ``cortex/``?**
The tree's authors placed MST at the lobe level because it fits **none**
of the four partition categories cleanly:

*   **Not a Brodmann field** — MST has **no single clean Brodmann
    number**. It sits at the boundary of BA19 (occipital), BA37
    (temporal), and BA39 (parietal), and its most commonly cited
    cytoarchitectonic designation is **V5a**, which is not a Brodmann
    field at all.

*   **Not a functional region under ``cortex/``** — the six ``cortex/``
    functional regions (A1, A2, ATL, ITC, pITC, MT) are **large-scale
    functional regions**, each defined by a broad functional domain.
    MST is **too functionally specific** to sit alongside them — it is
    an individual **motion-processing area**, not a broad region.

*   **Not a gyrus** — MST is located **within the superior temporal
    sulcus (STS)**, not on a gyral surface. It is **sulcal**, not gyral.

*   **Not a sulcus** — the STS is the sulcus; MST is the **cortical area
    within it**, not the sulcus itself.

**MST is therefore the structural and functional anomaly of the temporal
lobe** — it is a **cortical area that does not fit any of the tree's
structural categories**, and the tree's authors solved this by wiring it
**directly under the lobe aggregator** as a **standalone functional
node**.

**The standalone-node status is the defining architectural feature of
this module.** Consumers **must not** expect MST to behave like a
``cortex/`` functional region, a ``gyri/`` structural leaf, a
``brodmann_areas/`` cytoarchitectonic leaf, or a ``sulci/`` structural
sulcus. It is a **fifth category** — the **standalone functional node**
— and it must be queried at the **lobe level**.

Standalone-Node Status
----------------------
MST is the **first standalone functional node at the lobe level in the
tree** — and it is **bilaterally instantiated**. It is a **direct child
of ``.../temporal``**, sitting as a **sibling** to the four partitions,
**identical in structure to the left twin**:

::

    temporal/
    ├── brodmann_areas/          (cytoarchitectonic partition)
    ├── cortex/                  (functional partition)
    ├── gyri/                    (structural-gyral partition)
    ├── medial_superior_temporal_area/   <-- THIS MODULE (standalone)
    └── sulci/                   (structural-sulcal partition)

**Consumers must not assume that MST lives under ``cortex/``.** The path
``.../temporal/cortex/medial_superior_temporal_area`` **does not exist**
— it is a common mistake to try to reach MST via the functional
partition, because MST is a "functional area." It is not. It is a
**standalone functional node at the lobe level**.

**Resolution contract for consumers:**

*   If you need **right MST as a functional area**, use
    ``.../right/.../temporal/medial_superior_temporal_area``.
*   If you need **MST's cytoarchitectonic correlate**, it is **not a
    single Brodmann field** — it is most commonly designated **V5a** in
    the observer-independent literature, and it sits at the boundary of
    BA19/BA37/BA39.
*   **Do not** query ``cortex/medial_superior_temporal_area`` — it does
    not exist.
*   **Do not** query ``brodmann_areas/medial_superior_temporal_area`` —
    it does not exist.

**The standalone-node pattern is now established bilaterally**, and it
serves as the **architectural precedent** for other anomalous cortical
areas in future lobes — e.g., the **frontal eye fields (FEF)** and the
**supplementary eye field (SEF)** in the frontal lobe.

Functional Context: The MT/MST Motion-Processing Complex
--------------------------------------------------------
MST is the **optic-flow companion** of MT/V5. Where MT analyses **local
motion** — the **direction and speed of moving elements** in the visual
field — **MST analyses global motion** — the **optic-flow patterns** that
are generated by the observer's own motion through the environment:

*   **MT (V5)** — **local motion detection**; direction and speed
    selectivity; the **input area** to the motion-processing hierarchy.

*   **MST (V5a)** — **global motion integration**; **optic flow**;
    **self-motion perception**; the **downstream area** that uses MT's
    local motion signals to compute the **direction and speed of the
    observer's own movement**.

**MST is therefore not a "sub-region" of MT — it is a functionally
distinct downstream area.** The tree correctly wires them as **separate
modules**: MT is a ``cortex/`` functional region, and MST is a
**standalone functional node at the lobe level**. The two areas have
**different cytoarchitectonic identities**, **different connectivity
profiles**, and **different functional roles** — and the tree's
architecture reflects this by placing them in **different structural
categories**.

**On the right, this functional contrast is particularly pronounced** —
the right MST is the **dominant hemisphere for egomotion and heading
perception**, and it draws heavily on the right MT's local motion signals
to compute the **direction and speed of self-motion**.

Function in the Human Brain
---------------------------
The right MST is the **dominant hemisphere optic-flow and self-motion
hub**. Its best-supported functions cluster into six domains — **five
right-dominant and one bilateral**:

*   **Egomotion and Heading Perception (Right-Dominant — the defining
    right-MST function):** MST uses optic-flow signals to compute the
    **direction and speed of the observer's own movement** through the
    environment. This is the **egomotion** function, and it is
    **right-dominant** in most individuals — the **right MST** is the
    **dominant hemisphere for self-motion perception** and **heading
    perception**. This is the **principal right-lateralized function** of
    MST.

*   **Optic-Flow Analysis (Right-Dominant):** MST neurons are **selective
    for the global patterns of motion** that result from self-motion —
    **radial expansion** (forward motion), **radial contraction**
    (backward motion), **rotation** (roll), and **translation** (lateral
    motion). The right MST is the **dominant hemisphere** for these
    optic-flow components.

*   **Structure-from-Motion and Depth-from-Motion (Right-Dominant):** MST
    uses **motion signals** to extract **depth structure** — the ability
    to perceive the **three-dimensional shape and layout** of the
    environment from **motion cues**. This is a **right-dominant**
    function, consistent with the broader right-hemisphere dominance for
    depth-from-motion.

*   **Motion-in-Depth and Motion Parallax (Right-Dominant):** MST analyses
    **motion-in-depth** — motion **toward or away from the observer** —
    and **motion parallax** — the differential motion of near and far
    objects that results from the observer's own movement. These are
    **right-dominant** functions, consistent with the broader
    right-hemisphere dominance for motion.

*   **Visually Guided Locomotion (Bilateral):** MST provides the **sensory
    signals** that guide **visually guided locomotion** — the ability to
    **steer through the environment** while avoiding obstacles. On the
    **right**, this function is **weighted toward full-field optic-flow
    integration**; on the left, it is weighted toward **contra-lateral
    processing**. The function is **bilateral** but with the right
    hemisphere contributing the **dominant full-field component**.

*   **Contra-Lateral Optic-Flow Processing (Left-Dominant — contrast):**
    The **left MST** contributes primarily to **contra-lateral (right
    visual hemifield) optic-flow processing** and to **local motion
    integration**. This is the **contrast case** for the right MST's
    full-field dominance — the left hemisphere is the **contra-lateral
    specialist**, not the **full-field dominant**.

Associated Disorders
--------------------
Damage to or dysfunction of the right MST is associated with:

*   **Impaired Egomotion Perception (Right-Dominant — the signature
    right-MST syndrome):** Difficulty **perceiving the direction and
    speed of one's own movement** — the egomotion function — with a
    **right-lateralized** weighting. This is the **principal
    right-lateralized syndrome** of MST damage.

*   **Impaired Heading Perception (Right-Dominant):** Difficulty
    **perceiving the direction of one's own movement** through the
    environment, consistent with the right MST's dominance for heading
    perception.

*   **Impaired Optic-Flow Processing (Right-Dominant):** Difficulty
    **interpreting the global patterns of motion** that result from
    self-motion — a direct consequence of right MST damage.

*   **Impaired Structure-from-Motion and Depth-from-Motion
    (Right-Dominant):** Difficulty **extracting three-dimensional
    structure from motion cues** — a right-dominant function.

*   **Impaired Visually Guided Locomotion (Bilateral, with Right
    Emphasis):** Difficulty **steering through the environment** while
    avoiding obstacles, consistent with MST's role in visually guided
    locomotion. On the **right**, the deficit is more severe when
    **full-field** optic-flow integration is required.

*   **Findings Reported in Vestibular and Navigational Disorders
    (Bilateral):** The right MST has been implicated in **vestibular
    dysfunction** (optic-flow processing is closely coupled to the
    vestibular system) and in **navigational disorders**, though these
    are **findings reported** rather than established syndrome
    attributions.

**What is NOT here:** **Akinetopsia** (motion blindness) is an **MT/V5**
syndrome, not a right-MST-specific syndrome — though right-MST damage can
**contribute** to severe motion-perception deficits when it extends to or
is accompanied by MT/V5 damage. **Prosopagnosia** (right FFA), **pure
alexia** (left VWFA), and **Wernicke's aphasia** (left BA22) are **not**
MST syndromes. The right MST is a **motion-processing area**, not a face,
word, or language area.

Lateralization Notes
--------------------
This is the **right** MST module. The lateralization landscape is
**right-dominant for optic-flow and egomotion** — a **sensory-domain
weighting** that mirrors the right-dominant motion pattern already
documented in the adjacent MT/V5 area:

*   **Right-Dominant Functions (dominant in this twin):**
    - **Egomotion and heading perception** — the right MST is the
      **dominant hemisphere for self-motion**.
    - **Full-field optic-flow analysis** — the right MST is the dominant
      hemisphere for radial, rotational, and translational optic flow.
    - **Structure-from-motion and depth-from-motion** — right-dominant.
    - **Motion-in-depth and motion parallax** — right-dominant.

*   **Left-Lateralized Functions (present in the left twin, but not
    dominant):**
    - **Contra-lateral optic-flow processing** — the left MST contributes
      to the **right visual hemifield's** optic flow.
    - **Local motion integration** — the left MST contributes to the local
      sensory input that is integrated into global motion by the
      right-hemisphere network.

*   **Symmetric Functions (bilateral properties of MST):**
    - Basic optic-flow selectivity (radial, rotational, translational).
    - Visually guided locomotion (bilateral, with right weighting).
    - Contralateral visual-field representation.

**This is the "right-dominant sensory weighting" pattern at its most
pronounced** — the **same pattern** already documented in the adjacent
MT/V5 area, and the **same pattern** documented in the temporal lobe's
motion-processing hierarchy more generally. MST is a **sensory area**, and
its lateralization is a **hemispheric weighting** for a single sensory
domain (optic flow), not a **division of cognitive labor** (like the ATL,
ITC, MTG, or STG).

**A consumer that assumes "right MST = left MST" will miss the
right-dominant optic-flow and egomotion functions** — but the left twin is
**not** merely "denying" a right-hemisphere claim; it is **carrying a
contra-lateral subset** of the optic-flow-processing function.

**The right-dominant weighting is preserved from the left twin as an
architectural constant** — the `RIGHT_DOMINANT` constant in **both**
modules documents the right-hemisphere dominance for egomotion and
heading. The **left twin's `LEFT_CONTRIBUTION` constant** documents the
left hemisphere's **contra-lateral subset**. The two constants together
encode the **symmetric-magnitude, opposite-direction** architecture of
the MT/MST motion-processing complex.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    occipital lobe (V1, MT/V5) or the parietal lobe (MST's downstream
    targets). Those are **downstream/upstream targets**, not structural
    parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Standalone-node status — flagged in data.** MST is a **direct
    child of the lobe aggregator**, not a child of any of the four
    partitions. The ``STANDALONE_NODE`` constant is **True**, and the
    ``STRUCTURAL_PARENT`` constant is **"temporal"** (the lobe), not
    **"temporal/cortex"**.
*   **No Brodmann anchor — flagged in data.** MST has **no single clean
    Brodmann field**. Its most common cytoarchitectonic designation is
    **V5a**, which is not a Brodmann number. The ``BRODMANN_ANCHOR``
    constant is **None**.
*   **Neocortical granular type — flagged in data.** MST is a
    **neocortical extrastriate association area** with a **dense layer
    IV** and **large layer III pyramidal cells**. The
    ``CYTOARCHITECTONIC_TYPE`` constant is **"neocortical_granular"**.
*   **Right-dominant sensory weighting — flagged in data.** The
    ``RIGHT_DOMINANT`` constant documents the right-hemisphere
    dominance for optic-flow, egomotion, and heading perception. **The
    same constant is present in the left twin** (as an architectural
    encoding of the pair-wide lateralization pattern), but the **prose
    foregrounds the right's dominance**.
*   **Structural parity with left MST.** Left and right MST modules are
    **structurally identical** in their standalone-node status and
    cytoarchitectonic constants; only the **lateralization prose**
    differs (full-field dominant vs. contra-lateral specialist).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal import medial_superior_temporal_area

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.medial_superior_temporal_area"
    )

**⚠ WARNING:** MST is a **standalone functional node at the lobe level**.
It is **NOT** under ``cortex/``. The path
``.../temporal/cortex/medial_superior_temporal_area`` **does not exist**.
Use the ``STANDALONE_NODE`` constant to check::

    from ...temporal.medial_superior_temporal_area import STANDALONE_NODE, STRUCTURAL_PARENT
    # STANDALONE_NODE = True
    # STRUCTURAL_PARENT = "temporal"  (the lobe aggregator)

**MST has NO single Brodmann field.** Use the `BRODMANN_ANCHOR` constant::

    from ...temporal.medial_superior_temporal_area import BRODMANN_ANCHOR
    # BRODMANN_ANCHOR = None

For the optic-flow and egomotion functions::

    from ...temporal.medial_superior_temporal_area import SYMMETRIC_FUNCTIONS
    # SYMMETRIC_FUNCTIONS = ("optic_flow_analysis",
    #                        "visually_guided_locomotion",
    #                        "contralateral_visual_field_representation")

For the right-dominant functions::

    from ...temporal.medial_superior_temporal_area import RIGHT_DOMINANT
    # RIGHT_DOMINANT = ("egomotion",
    #                   "heading_perception",
    #                   "structure_from_motion",
    #                   "motion_in_depth",
    #                   "motion_parallax")

For the left contra-lateral contribution (documented here as a
contrast)::

    from ...temporal.medial_superior_temporal_area import LEFT_CONTRIBUTION
    # LEFT_CONTRIBUTION = ("contra_lateral_optic_flow_processing",
    #                      "local_motion_integration")

For the adjacent MT/V5 area (which IS under ``cortex/``)::

    from ...temporal.cortex import mt
    # MT is the local-motion companion of MST, wired under cortex/

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mst_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.medial_superior_temporal_area"
        )
        # resolve mst_path through the memory/recall layer

References
----------
*   **MST overview:** *Medial Superior Temporal Area — an overview*
    (ScienceDirect). MST (V5a) is a **motion-processing area adjacent
    to MT/V5** that analyses **optic flow** — the global patterns of
    motion that result from self-motion — and supports **egomotion,
    heading perception, and visually guided locomotion**.
*   **Optic-flow selectivity:** Tanaka, K., & Saito, H. (1989). "Analysis
    of motion of the visual field by direction, expansion/contraction,
    and rotation cells clustered in the dorsal part of the medial
    superior temporal area of the macaque monkey." *J Neurophysiol*,
    62(3), 626–641. MST neurons are **selective for radial expansion,
    radial contraction, rotation, and translation** — the elementary
    components of optic flow.
*   **Egomotion and heading:** Duffy, C.J., & Wurtz, R.H. (1991).
    "Sensitivity of MST neurons to optic flow stimuli." *J Neurophysiol*,
    65(6), 1329–1345. MST neurons are **sensitive to the optic-flow
    patterns** that result from self-motion and support **heading
    perception**.
*   **Right-dominance for self-motion:** *An enhanced role for right
    hV5/MT+ in the analysis of motion in the contra- and ipsi-lateral
    visual hemi-fields* (2019), *Behav Brain Res*. The **right
    hemisphere** (including the adjacent MT/MST complex) is **dominant
    for optic-flow and self-motion processing**.
*   **Structure-from-motion:** Orban, G.A., et al. (1999). "Human
    cortical regions involved in extracting depth from motion."
    *Neuron*, 24(4), 929–940. Human MT/V5+ (the MT/MST complex) is part
    of a network with **right hemisphere dominance** involved in
    extracting **depth from motion**.
*   **Anatomical location:** *Superior Temporal Sulcus — an overview*
    (ScienceDirect). MST sits in the **dorsal/posterior bank of the
    superior temporal sulcus (STS)** and the **adjacent lateral
    occipitotemporal cortex**, at the **temporo-parieto-occipital
    junction**.
*   **Cytoarchitecture (V5a):** *Delineating extrastriate visual area
    MT(V5) using cortical myeloarchitecture* (2013), *NeuroImage*. The
    MT/MST complex is identifiable by **myeloarchitecture**; MST (V5a)
    is **less heavily myelinated** than MT (V5).
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Lateral temporal and superior temporal sulcus
    anatomy.)
*   NeuroNames — Medial superior temporal area (right); FMA — right
    superior temporal sulcus cortex.
"""