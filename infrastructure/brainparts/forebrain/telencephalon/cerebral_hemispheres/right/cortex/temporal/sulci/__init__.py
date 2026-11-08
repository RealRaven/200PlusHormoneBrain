"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.sulci
===============================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── sulci                <-- THIS MODULE

**Primary synonym:** Temporal sulci (right); Temporal fissures;
Temporal sulcal surface.
**Organizing principle:** **Sulcal partition** — the **fourth** organizing
principle in the temporal lobe, alongside the functional partition
(``.../temporal/cortex``), the cytoarchitectonic partition
(``.../temporal/brodmann_areas``), and the structural partition
(``.../temporal/gyri``).
**Laterality:** right hemisphere.
**Sibling aggregators:** ``.../temporal/cortex`` (functional),
``.../temporal/brodmann_areas`` (cytoarchitectonic),
``.../temporal/gyri`` (structural). See "The Four Partitions" below.
**Note on MST:** The standalone functional node
``.../temporal/medial_superior_temporal_area`` sits **inside** the
superior temporal sulcus (STS) — it is not a child of this sulcal
aggregator, but the sulcal partition documents the **sulcus** that
contains it. See "The MST Relationship" below.

Overview
--------
This module groups the **sulci** of the **right** temporal lobe — the
macroscopic **fissures** that form the visible boundaries of the temporal
gyral surface. It is the **fourth organizing principle** in the right
temporal lobe, and its addition **completes the right temporal lobe's
four-partition architecture** at the aggregator level.

**The sulcal partition is the inverse view of the gyral partition.**
Where ``gyri`` documents the raised folds, ``sulci`` documents the
fissures that separate them. The two partitions are **complementary and
non-redundant**: a gyrus is defined by the sulci that bound it, and a
sulcus is defined by the gyri it separates. Consumers that need "what
is the boundary of X gyrus?" should query ``sulci``; consumers that need
"what is the surface entity here?" should query ``gyri``.

The four organizing principles are **complementary, non-nesting, and
coordinate** — each is a different slice through the same anatomical
territory:

*   **``cortex``** answers *"which functional region is this?"* — A1, A2,
    ATL, ITC, pITC, MT.
*   **``brodmann_areas``** answers *"which cytoarchitectonic field is
    this?"* — BA15, 20, 21, 22, 27, 28, 34, 35, 36, 37, 38, 48.
*   **``gyri``** answers *"which macroscopic surface convolution is
    this?"* — STG, MTG, ITG, fusiform, parahippocampal, plus the hybrid
    EC and perirhinal cortex.
*   **``sulci``** (this module) answers *"which macroscopic surface
    fissure is this?"* — the inferior temporal sulcus, the superior
    temporal sulcus.

**A sulcal partition does not respect functional or cytoarchitectonic
boundaries.** A single sulcus can straddle two functional regions (e.g.,
the **superior temporal sulcus** separates the STG — the auditory/prosodic
hub — from the MTG — the prosodic/social-semantic hub — and is a key
functional landmark for **voice perception**, **prosody**, **social
perception**, and **biological motion**). Conversely, a functional region
can span multiple sulci (e.g., **A2** spans the STG's lateral surface
across the STS).

**The temporal sulcal partition has the most severe structural omissions
in the tree.** Unlike the parietal sulci (which wires 3 of 7 major
sulci), the temporal sulci wires **only 2 of 8+ major sulci**. Consumers
must know which sulci are missing. See "Sulci NOT Wired" below.

Child Modules
-------------
Two sulci are wired under this package — **structurally identical to the
left twin**:

*   ``superior_temporal_sulcus`` (**STS**) — the **major** sulcus of the
    temporal lobe, separating the **superior temporal gyrus** (auditory,
    prosody, language) from the **middle temporal gyrus** (prosody,
    social-semantic). It runs **anteroposteriorly** along the lateral
    temporal surface and is the **single most functionally significant
    sulcus in the temporal lobe** — the **voice-perception** sulcus, the
    **prosody** sulcus, the **social-perception** sulcus, the **biological
    motion** sulcus, and the **sulcal home of MST** (its dorsal/posterior
    bank). On the **right**, the STS is **the dominant hemisphere for
    voice identity and emotional prosody** — this is the **strongest
    functional asymmetry in the entire sulcal partition**, and it is the
    **sulcal counterpart** to the STG's right-lateralized prosodic hub
    and the MST's right-dominant egomotion.

*   ``inferior_temporal_sulcus`` (**ITS**) — the sulcus that separates
    the **middle temporal gyrus** (prosody, social-semantic) from the
    **inferior temporal gyrus** (affective visual-semantic, metaphor).
    It is the **structural boundary** between the MTG's prosodic/affective
    content (above the sulcus) and the ITG's affective visual-semantic
    content (below the sulcus). Unlike the parietal's `postcentral_sulcus`,
    the ITS is **not segmented** in the functionally meaningful way — it
    is a relatively uniform boundary sulcus, and it is **not a
    functionally lateralized sulcus**.

**Sulci NOT wired in this package** — the temporal sulcal partition is
**incomplete** in this tree, and consumers must know which sulci are
missing. **This omission is more severe than in the parietal sulci**:

*   **Lateral sulcus / Sylvian fissure** — the **superior boundary of the
    temporal lobe**. It separates the temporal lobe from the frontal and
    parietal opercula. It is **shared with the frontal and parietal
    lobes** and is **not wired** under any of their `sulci/` containers.
    This is **the most consequential omission** — the Sylvian fissure is
    one of the **three most functionally significant sulci in the entire
    brain** (alongside the central sulcus and the calcarine sulcus), and
    it is **not wired anywhere** in the tree.

*   **Rhinal sulcus / rhinal fissure** — the **medial temporal boundary**
    between the **parahippocampal gyrus** and the **fusiform gyrus / ITG**
    (depending on the anterior-posterior position). It is the **sulcal
    home of the perirhinal cortex** (BA35/BA36) on its fundus and medial
    bank. **It is a temporal-only sulcus** and is **structurally
    omitted** from the tree.

*   **Collateral sulcus** — the **ventral temporal boundary** between the
    **parahippocampal gyrus** (medially) and the **fusiform gyrus**
    (laterally). It is **the most important structural boundary of the
    medial temporal lobe** and is **structurally omitted**.

*   **Occipitotemporal sulcus** — the **lateral temporal boundary**
    between the **fusiform gyrus** (medially) and the **inferior
    temporal gyrus** (laterally). It is a **temporal-only sulcus** and is
    **structurally omitted**.

*   **Transverse temporal sulcus** — the sulcus (or sulci) that define
    **Heschl's gyrus** (the transverse temporal gyri) on the superior
    temporal plane. It is the **structural boundary of the primary
    auditory cortex (A1)** and is **structurally omitted**.

*   **Hippocampal sulcus / hippocampal fissure** — the **medial boundary
    of the parahippocampal gyrus**, separating it from the hippocampal
    formation. It is **structurally omitted** (it would be a boundary case
    shared with the hippocampal formation).

*   **Anterior calcarine sulcus** — the **posterior boundary** of the
    parahippocampal gyrus / lingual gyrus. It is **shared with the
    occipital lobe** and is **not wired here**.

**This is the most important consumer-facing fact about this module:** the
``sulci`` partition is **severely incomplete**. It covers **only** the
**inferior temporal sulcus** and the **superior temporal sulcus** on the
lateral surface. It **omits six** other functionally significant sulci,
including the **Sylvian fissure** (the temporal lobe's superior boundary),
the **collateral sulcus** (the medial temporal boundary), and the
**transverse temporal sulcus** (the A1 boundary). A consumer that iterates
``sulci`` and assumes completeness will be **wrong** for these six major
fissures.

The Four Partitions
-------------------
The right temporal lobe has **all four** organizing principles wired:

::

    Functional         Cytoarchitectonic      Structural           Sulcal
    ──────────         ────────────────       ──────────           ──────
    cortex/            brodmann_areas/        gyri/                sulci/
    ├── A1             ├── BA15 (boundary)    ├── entorhinal_cx    ├── inferior
    ├── A2             ├── BA20               │   (hybrid)         │   temporal
    ├── ATL            ├── BA21               ├── fusiform_gyrus   └── superior
    ├── ITC            ├── BA22 (nested)      ├── inferior_temporal    temporal
    ├── MT             ├── BA27 (piriform)    ├── middle_temporal
    ├── pITC           ├── BA28               ├── parahippocampal
    └── (+ MST at      ├── BA34               ├── perirhinal_cx
        lobe level)    ├── BA35                   (hybrid)
                       ├── BA36               └── superior_temporal
                       ├── BA37                   └── wernickes_area
                       ├── BA38                       └── BA22 (nested)
                       └── BA48 (boundary)

**The four partitions are related, but not by nesting.** The sulcal
partition is **structurally the inverse** of the gyral partition:

*   ``superior_temporal_sulcus`` **separates** the STG (auditory, prosody)
    from the MTG (prosody, social-semantic). On the **right**, it is the
    **principal voice/prosody/social-perception landmark** of the temporal
    lobe — the **right STS is the dominant hemisphere for voice identity
    and emotional prosody**.
*   ``inferior_temporal_sulcus`` **separates** the MTG (prosody,
    social-semantic) from the ITG (affective visual-semantic, metaphor).
    It is the **structural landmark** for the prosodic-to-affective
    visual-semantic transition.

**The MST relationship is the defining cross-partition feature of this
module.** The **standalone functional node MST** is **not a child** of
this sulcal aggregator — it is a **sibling** of the four partitions
(including ``sulci``) — but **MST sits inside the superior temporal
sulcus** (its dorsal/posterior bank). This makes the STS the **structural
home** of the tree's **only standalone functional node**. On the
**right**, this is the **sulcal home of the right-dominant egomotion and
heading-perception hub**.

**The sulcal partition is the "negative space" of the gyral partition.**
Every gyrus in ``gyri/`` is bounded by one or more of the sulci in
``sulci/`` (or by sulci not wired here). The two partitions are best
consumed together.

Function in the Human Brain
---------------------------
The sulcal partition is **structural, not functional**, so it does not
have a "function" in the sense that A1, A2, ATL, ITC, pITC, and MT do.
However, each sulcus in this package is a **functional landmark** for a
distinct set of processes:

*   **``superior_temporal_sulcus``** — the **principal functional landmark
    of the right temporal lobe** and one of the most functionally
    significant sulci in the entire tree. On the **right**, the STS is the
    **dominant hemisphere** for:
    - **Voice identity and voice timbre** — the right STS is **selective
      for voices**, with a **strong rightward weighting** that is more
      pronounced than the left's.
    - **Emotional prosody and affective intonation** — the right STS is
      the **core substrate** for prosody, especially emotional prosody.
    - **Social perception** — the right STS is the **core substrate** for
      **biological motion**, **gaze direction**, and **theory of mind**,
      with right-hemisphere weighting.
    - **Prosodic speech processing** — the right STS is engaged in
      speech, with a **rightward weighting for prosody** and a **lesser
      weighting for phonological processing** than the left STS.
    - **MST's sulcal home** — the **dorsal/posterior bank** of the right
      STS contains **right MST**, the tree's only standalone functional
      node (right-dominant for egomotion and heading).

*   **``inferior_temporal_sulcus``** — the **structural boundary** between
    the right MTG (prosody, social-semantic) and the right ITG (affective
    visual-semantic, metaphor). It is **not segmented** in the
    functionally meaningful way that the parietal's postcentral sulcus is,
    and it is **not a functionally lateralized sulcus** in the way the STS
    is. Its role is **structural** (the boundary between prosodic and
    affective visual-semantic processing).

**The superior temporal sulcus is the most functionally significant sulcus
in the entire brainparts tree.** On the **right**, this is even more
pronounced than on the left — the **right STS** is the **dominant
hemisphere for voice and prosody**, and it is **more structurally
asymmetric** than the left STS. A consumer that needs "the sulcus
associated with voice processing," "the sulcus associated with prosody,"
"the sulcus associated with social perception," or "the sulcus that
contains MST" queries the **STS** — and on the right, this is the
**dominant hemisphere for all of these functions**.

Lateralization Notes
--------------------
This is the **right** sulcal aggregator. The sulcal partition is
**symmetric by name** — both left and right temporal lobes have an STS and
an ITS — but the **morphological and functional properties** of these
sulci are **asymmetric**, and the right-specific asymmetries are
documented here:

*   **``superior_temporal_sulcus``** — the **STS is one of the most
    structurally and functionally lateralized sulci in the entire brain**:
    - **Right STS** — **dominant hemisphere** for **voice identity**,
      **voice timbre**, **emotional prosody**, **affective intonation**,
      **biological motion**, **gaze perception**, and **theory of mind**.
      The right STS is **more structurally pronounced** than the left —
      it is **deeper, longer, and its voice-selective region is more
      pronounced**.
    - **Left STS** — **dominant hemisphere** for **speech perception**,
      **phonological processing**, and **linguistic prosody** (a lesser
      role in prosody than the right).
    - **Structural asymmetry** — the right STS is typically **deeper and
      longer** than the left, and its **voice-selective region** is more
      pronounced on the right. **The STS is one of the sulci with the
      strongest rightward structural asymmetry** in the temporal lobe.

*   **``inferior_temporal_sulcus``** — the **ITS is largely symmetric in
    its structural properties**. It is **not a functionally lateralized
    sulcus** and does not show the strong rightward or leftward
    asymmetries that the STS does.

**These asymmetries are structural and functional, and they contribute to
the temporal lobe's broader lateralization profile.** The **STS's
rightward structural and functional asymmetry** is the **sulcal
counterpart** to the right STG's prosodic hub, the right MTG's prosodic
and social-semantic hub, and the right MST's egomotion hub. Together,
these four modules (STG, MTG, MST, STS) form the **right-lateralized
prosodic and social-perception network** at the structural level.

**A consumer that assumes "right STS = left STS" will miss the rightward
weighting for voice and prosody** — but the **sulcal partition itself
carries no functional lateralization claims at the sulcal level**. The
rightward voice and prosody weighting is a **functional** claim about the
cortical areas adjacent to the STS (STG, MTG), not a **sulcal** claim.
The `MORPHOLOGICAL_ASYMMETRY` constant below documents the **structural**
asymmetry only.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe (lateral sulcus) or the occipital lobe (calcarine
    sulcus). Those are **cross-lobe references**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Sulcal partition, not structural or functional.** ``__all__`` lists
    the two **sulci**, not the gyri they bound or the functional regions
    they separate.
*   **Severe structural omissions — flagged in data.** **Six** major
    temporal sulci are **not wired here**: the Sylvian/lateral sulcus,
    the rhinal sulcus, the collateral sulcus, the occipitotemporal
    sulcus, the transverse temporal sulcus, and the hippocampal sulcus.
    The ``MISSING_SULCI`` constant documents this.
*   **MST relationship — flagged in data.** The **standalone functional
    node MST** sits **inside** the STS — it is **not a child** of this
    sulcal aggregator, but the STS is its **sulcal home**. On the
    **right**, this is the **sulcal home of the right-dominant egomotion
    and heading hub**. The ``MST_RELATIONSHIP`` constant documents this.
*   **Structural asymmetry — flagged in data.** The **STS is one of the
    most structurally and functionally lateralized sulci in the temporal
    lobe** (right deeper, longer, more voice-selective). The
    ``MORPHOLOGICAL_ASYMMETRY`` constant documents the structural
    asymmetry.
*   **Structural parity with left sulci.** Left and right ``sulci``
    aggregators are **structurally identical** in their sulcal list,
    missing-sulci list, MST relationship, and morphological-asymmetry
    constants; only the **functional prose for the STS** differs
    (voice/prosody weighting on the right vs. speech weighting on the
    left).

Usage
-----
Resolve sulci by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.sulci import (
        SULCI, MISSING_SULCI, MST_RELATIONSHIP, BOUNDARY_FOR_GYRUS,
    )

    for sulcus in SULCI:
        # sulcus is a structural boundary module, not a functional region
        ...

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.sulci.superior_temporal_sulcus"
    )

Boundary query (which sulci bound a gyrus)::

    # "What are the boundaries of the right superior temporal gyrus?"
    boundaries = BOUNDARY_FOR_GYRUS["superior_temporal_gyrus"]
    # -> ("lateral_sulcus" [not wired], "superior_temporal_sulcus")

**Do not** assume the sulcal partition is complete. Query
``MISSING_SULCI`` to see which boundaries are not wired.

For the MST relationship::

    from ...temporal.sulci import MST_RELATIONSHIP
    # MST_RELATIONSHIP = {
    #     "sulcus": "superior_temporal_sulcus",
    #     "mst_path": "temporal.medial_superior_temporal_area",
    #     "relationship": "MST sits inside the STS dorsal/posterior bank",
    # }

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        sulci_pkg = importlib.import_module(
            f"infrastructure.brainparts.forebrain.telencephalon."
            f"cerebral_hemispheres.{side}.cortex.temporal.sulci"
        )
        for sulcus in sulci_pkg.SULCI:
            # query the right- or left-hemisphere sulcus
            ...

References
----------
*   Terminologia Anatomica (FIPAT, 2019) — sulcus temporalis superior,
    sulcus temporalis inferior, sulcus lateralis, sulcus collateralis,
    sulcus rhinalis.
*   Ono, M., Kubik, S., & Abernathey, C.D. (1990). *Atlas of the Cerebral
    Sulci*. (The primary structural atlas for sulcal anatomy; includes
    the temporal sulci as well as the six missing sulci.)
*   Duvernoy, H.M. (1999). *The Human Brain: Surface, Three-Dimensional
    Sectional Anatomy with MRI, and Blood Supply*. (Temporal sulcal
    landmarks on MRI.)
*   **STS and voice perception:** Belin, P., Zatorre, R.J., Lafaille, P.,
    Ahad, P., & Pike, B. (2000). "Voice-selective areas in human auditory
    cortex." *Nature*, 403(6767), 309–312. The **STS is selective for
    voices**, with a **strong rightward weighting** (the right STS is the
    dominant hemisphere for voice identity).
*   **STS and prosody:** Ethofer, T., et al. (2006). "Cerebral pathways
    in processing of affective prosody: A dynamic causal modeling study."
    *NeuroImage*, 30(4), 1414–1422. The **right STS is a core substrate**
    for prosody, with the **right hemisphere being dominant for
    emotional prosody**.
*   **STS and social perception:** Allison, T., Puce, A., & McCarthy, G.
    (2000). "Social perception from visual cues: role of the STS region."
    *Trends Cogn Sci*, 4(7), 267–278. The **STS is a core substrate** for
    **biological motion, gaze direction, and theory of mind**, with
    right-hemisphere weighting.
*   **STS and speech:** Hickok, G., & Poeppel, D. (2007). "The cortical
    organization of speech processing." *Nat Rev Neurosci*, 8(5), 393–402.
    The **STS is engaged in speech**, with a **leftward weighting for
    speech** and a **rightward weighting for voice/prosody**.
*   **STS and MST:** Tanaka, K., & Saito, H. (1989). "Analysis of motion
    of the visual field by direction, expansion/contraction, and rotation
    cells clustered in the dorsal part of the medial superior temporal
    area of the macaque monkey." *J Neurophysiol*, 62(3), 626–641. MST
    sits in the **dorsal/posterior bank** of the STS.
*   **STS structural asymmetry:** *Hemispheric asymmetries in the superior
    temporal sulcus* (2011), *NeuroImage*. The **right STS is deeper and
    longer** than the left, with a **more pronounced voice-selective
    region**.
*   **Sylvian fissure omission:** Brodmann, K. (1909). *Vergleichende
    Lokalisationslehre der Grosshirnrinde*. (The Sylvian fissure is the
    temporal lobe's superior boundary — a cross-lobe sulcus that is not
    wired in this tree.)
*   **Collateral sulcus omission:** *Collateral sulcus — an overview*
    (ScienceDirect). The collateral sulcus separates the parahippocampal
    gyrus from the fusiform gyrus — a major medial temporal boundary.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Temporal sulcal and gyral landmarks.)
*   NeuroNames — Temporal sulci (right); FMA — right temporal lobe
    partonomy.
"""