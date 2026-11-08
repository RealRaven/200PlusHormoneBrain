"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri.postcentral_gyrus.brodmann_area_3
==============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── gyri
                        └── postcentral_gyrus
                            └── brodmann_area_3   <-- THIS MODULE

**Primary synonym:** Brodmann Area 3 (BA3); Area 3 of Brodmann (1909).
**Subdivisions:** **BA3a** and **BA3b** — two cytoarchitectonically and
functionally distinct fields that are conventionally grouped under the
single Brodmann label "area 3" but are increasingly recognized as separate
entities in modern parcellations.
**Part of:** Primary somatosensory cortex (**S1**), alongside BA1 and BA2.
**Structural parent:** ``.../parietal/gyri/postcentral_gyrus`` — **not**
``.../parietal/brodmann_areas``.
**Cross-listing status:** The **only** Brodmann-area leaf in the tree that
lives under a gyral container rather than under the ``brodmann_areas``
aggregator. It is the resolution target for
``brodmann_areas.AREA_PATHS["brodmann_area_3"]``.
**Location:** The **posterior bank of the central sulcus** and the
**fundus** of the central sulcus, at the transition between the primary
somatosensory and primary motor cortices.

Overview
--------
Brodmann Area 3 (BA3) is the **rostral-most component of the primary
somatosensory cortex (S1)** and the **first cortical stage of the
somatosensory processing cascade**. It occupies the **posterior bank of
the central sulcus** (BA3b) and the **fundus of the central sulcus**
(BA3a), adjacent to the agranular primary motor cortex (BA4) on the
anterior bank. It is the **thalamic gateway** for discriminative touch,
proprioception, and nociception.

**BA3 is not a single homogeneous field.** Modern cytoarchitectonic and
electrophysiological work distinguishes **two functionally dissociable
subfields**:

*   **BA3b** — the **thalamic gateway** and the **first cortical stage of
    tactile processing**. It is **"S1 proper"** in the strict sense (Kaas,
    1983) and receives the **densest thalamocortical input** from the
    ventroposterior lateral (VPL) and ventroposterior medial (VPM) nuclei
    of the thalamus. It is a **koniocortex** with a very high cell-packing
    density in layer IV and shows specific responsivity to **FA1, SA1, and
    SA2** cutaneous afferents. It is the **principal cortical target of
    the lemniscal pathway** for discriminative touch.

*   **BA3a** — a **hybrid field** at the fundus of the central sulcus,
    adjacent to area 4. It has a **blend of motor and sensory features**
    — an overall low cell-packing density, few larger pyramidal cells in
    deep layer III, and an **incipient layer IV**. It receives
    **proprioceptive signals** from deep receptors (muscle spindles) via
    the **ventroposterior oral nucleus (VPO)** and the
    **ventroposterior superior nucleus (VPS)** , and it is also
    **nociresponsive** — particularly to **C-fiber-mediated slow/burning
    pain** — via a distinct region at the S1–M1 border that some authors
    propose to call **"BA3c"** .

**The BA3/BA3b distinction is the key internal contract of this module.**
BA3b is the thalamic gateway for **cutaneous touch**; BA3a is the
proprioceptive and **nociresponsive** field at the sensory–motor
transition. They are conventionally grouped under "BA3" in the Brodmann
map, but they are **functionally and cytoarchitectonically distinct**, and
they should not be conflated by consumers.

**This module is the cross-listing resolution target.** Every earlier
docstring in the parietal subtree — from the ``brodmann_areas`` aggregator
through BA1, BA2, the S1 functional-region node, and the gyri aggregator —
has pointed at this path as the place where BA3 actually lives. This
module is the **resolution** of that promise. A consumer that iterates
``brodmann_areas.LOCAL_AREAS`` will see BA1 and BA2 but **not** BA3; they
must use ``ITERABLE_AREAS`` and resolve BA3 through this gyrus.

Two-Partition Context
---------------------
This module is a **cytoarchitectonic leaf** under a **structural
container** (the postcentral gyrus). It is the **only** such module in the
tree:

::

    Structural container (gyrus)         Cytoarchitectonic leaf (this module)
    ────────────────────────────         ────────────────────────────────────
    postcentral_gyrus               ──▶  brodmann_area_3   **CROSS-LISTED**
                                           ├── BA3a (fundus; proprioception /
                                           │   nociception)
                                           └── BA3b (posterior bank; thalamic
                                               gateway for discriminative touch)

**This is a deliberate architectural inversion.** Every other Brodmann-area
leaf lives under ``.../parietal/brodmann_areas/``. BA3 lives here because
its cytoarchitectonic territory is **anatomically co-extensive with the
postcentral gyrus** — it is the only S1 field whose entire extent is
contained within a single gyrus. Consumers must **not** assume that all
Brodmann leaves live under ``brodmann_areas/``.

**Resolution contract for consumers:**

*   If you need **BA3 by name**, use
    ``brodmann_areas.ITERABLE_AREAS`` and resolve it via
    ``AREA_PATHS["brodmann_area_3"]``, which points here.
*   If you need **BA3a or BA3b separately**, they are subfields of this
    module. They are **not** wired as separate child packages; use the
    ``SUBFIELDS`` constant below.
*   If you iterate ``brodmann_areas.LOCAL_AREAS``, you will **miss BA3**.
    This is documented, not a bug.

Cytoarchitecture
----------------
The two BA3 subfields are cytoarchitectonically distinct and are
increasingly recognized as separate entities:

*   **BA3b (S1 proper)** — **koniocortex** with a very high cell-packing
    density in the supragranular layers, particularly layer IV. Small
    granular neurons and small pyramidal neurons give it an overall
    "dusty" appearance under low-power microscopy. It has the
    **narrowest fingertip tuning** in the S1 hierarchy (2.6 fingertips
    FWHM), widening to 4.0 in BA1 and 9.3 in BA2. It is the
    **principal thalamocortical recipient** of the lemniscal pathway from
    VPL/VPM.

*   **BA3a** — a **transitional/hybrid** cortex at the fundus of the
    central sulcus, with **fewer granule cells and larger pyramidal cells**
    than BA3b. It has an **incipient layer IV** and a **blend of motor and
    sensory features**. It receives **muscle spindle** input via VPO
    and deep-receptor input via VPS. It contains a **nociresponsive
    region** at the S1–M1 border that is **C-fiber-dominated** and is
    associated with **slow/second/burning pain** — a functionally
    distinct zone that some authors propose to call **"BA3c"** .

**Thalamic input summary:**

*   **BA3b** ← VPL/VPM (cutaneous, lemniscal); also sparse VPS, VPI, and
    anterior pulvinar.
*   **BA3a** ← VPO (muscle spindle), VPS (deep receptors); also VPLc
    (hand representation).

Function in the Human Brain
---------------------------
The left BA3 is the **left-lateralized thalamic gateway and first cortical
stage of somatosensory processing**. Its best-supported functions cluster
into five domains:

*   **Discriminative Touch — First Cortical Stage (BA3b):** BA3b is the
    **first cortical stage of the tactile processing cascade** that
    comprises BA1, the posterior parietal cortex, and SII. It receives
    the **densest thalamic input** from VPL/VPM and is the **principal
    cortical target of the lemniscal pathway** for fine discriminative
    touch. It shows specific responsivity to **FA1, SA1, and SA2**
    cutaneous afferents and is the substrate for **elementary tactile
    feature detection**, including **two-point discrimination**.

*   **Proprioception — Deep Receptor Input (BA3a):** BA3a receives
    **muscle spindle** signals via VPO and **deep-receptor** signals via
    VPS. It is the **proprioceptive gateway** of S1 — the first cortical
    stage of the processing cascade that leads to limb-position sense and
    kinaesthesia.

*   **Nociception — Slow/Burning Pain (BA3a, "BA3c"):** A distinct
    nociresponsive region at the **S1–M1 border** within BA3a responds
    preferentially to **C-fiber-mediated slow/burning pain** (second
    pain), in contrast to the **Aδ-mediated fast/discriminative pain**
    (first pain) that is generated in **BA3b–BA1**. This region is
    probably engaged in **interoception and autonomic control** and
    contributes to the **sympathetic response to noxious stimulation** —
    "arguably the most intolerable aspect of pain experience" .
    Ablation of this region has been shown to **reduce pain sensibility**.

*   **Somatotopic Representation of the Right Hemibody:** BA3b contains a
    complete **mirror-image somatotopic map** of the **right** hemibody,
    which is a **mirror image of the BA1 map**. The **foot** is
    represented **posteriorly**, and the **genitalia** are represented
    **anterior** to the foot sensory area. The **lips** have an
    **ipsilateral** representation in **BA3b/BA1** in addition to the
    contralateral one — a rare exception to the strictly contralateral
    organization of S1.

*   **Hierarchical Cascade Initiation (BA3b → BA1 → BA2):** BA3b initiates
    the **serial hierarchy** of S1: BA3b (elementary features, two-point
    discrimination) → BA1 (texture) → BA2 (size/shape, proprioception).
    Fingertip tuning widths widen progressively from **2.6** (BA3b) to
    **4.0** (BA1) and **9.3** (BA2) fingertips FWHM, providing direct
    evidence for the hierarchical cascade.

Associated Disorders
--------------------
Damage to or dysfunction of the left BA3 is associated with:

*   **Bilateral Astereognosis (Left-Lateralized — the signature left-S1
    syndrome):** A small infarct in the **left postcentral gyrus**,
    strategically sparing BA3a/BA3b but destroying BA1, can produce
    **bilateral astereognosis** — the inability to recognize objects by
    touch with **either** hand. The lesion deprives BA1 of afferents
    from BA3a/BA3b and deafferents its targets (BA2, S2, and the
    contralateral BA1). This is a **left-lateralized** syndrome and
    does **not** occur with right BA3 lesions.

*   **Impaired Two-Point Discrimination (BA3b lesion):** Selective deficit
    in elementary tactile feature detection, consistent with BA3b's role
    as the first cortical stage of discriminative touch.

*   **Impaired Proprioception (BA3a lesion):** Deficits in limb-position
    sense and kinaesthesia, consistent with BA3a's role as the
    proprioceptive gateway.

*   **Altered Slow/Burning Pain Perception (BA3a/"BA3c" lesion or
    ablation):** Ablation of the nociresponsive region in the depth of
    the central sulcus **reduces pain sensibility** and might offer an
    effective means of ameliorating some pathological pain conditions.

**What is NOT here:** The **right-hemibody** representation, the
**right-lateralized spatial-attention** functions, and the
**contralateral-only** astereognosis phenotype are properties of the
**right** BA3 module. They are **not** part of this left module and must
not be imported from the right twin.

Lateralization Notes
--------------------
This is the **left** BA3 module. The lateralization landscape is
**left-loaded** for stereognosis dominance — the same pattern as the left
S1 functional-region node and the left BA1/BA2 leaves:

*   **Left-Lateralized Functions (unique to this twin):**
    - **Bilateral astereognosis** — a small left postcentral lesion that
      deafferents BA1 from BA3a/BA3b produces bilateral loss; a right
      lesion produces contralateral-only loss.
    - **Left postcentral gyrus dominance for stereognosis** (Oppenheim,
      1906; Moll et al., 2017) — the left BA3/BA1 complex is the dominant
      substrate for tactile object recognition in some individuals.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Contralateral-only astereognosis** — a right postcentral lesion
      produces **left-hand** astereognosis only.
    - **Right S1 left-hand facilitation** — the right S1/SA shows stronger
      facilitation during left-hand stimulation (see right BA1/S1
      modules).

*   **Symmetric Functions (bilateral properties of BA3, copied verbatim
    to the right twin):**
    - BA3b thalamic gateway and first cortical stage of tactile processing.
    - BA3b → BA1 → BA2 hierarchical cascade (elementary features →
      texture → size/shape).
    - BA3a proprioceptive and nociresponsive processing (muscle spindle,
      C-fiber slow pain).
    - Somatotopic mirror representations (BA3b ↔ BA1), with hemibody
      flipped (left BA3 → **right** hemibody).
    - Ipsilateral lip representation in BA3b/BA1.

**A consumer that assumes "left BA3 = symmetric" will miss the
left-lateralized stereognosis dominance that defines the left twin.** The
BA3 pair is **left-loaded**, exactly like the S1 pair and the BA1/BA2
leaves.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../frontal/gyri/precentral_gyrus`` or
    ``.../frontal/brodmann_areas/brodmann_area_4``. The motor counterpart
    (BA4) is a separate module in the frontal lobe.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cross-listed leaf — the ONLY Brodmann-area leaf under a gyrus.**
    This module lives under ``.../gyri/postcentral_gyrus/``, **not** under
    ``.../brodmann_areas/``. It is the resolution target for
    ``brodmann_areas.AREA_PATHS["brodmann_area_3"]``. Consumers must
    **not** assume that all Brodmann leaves live under
    ``brodmann_areas/``.
*   **BA3a and BA3b are subfields, not separate modules.** They are
    documented within this single module via the ``SUBFIELDS`` constant.
    Consumers that need subfield-level resolution should use that
    constant, not a filesystem walk.
*   **Structural parity with right BA3.** Left and right BA3 modules must
    be structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. The cytoarchitecture, thalamic input, and
    hierarchical position are **symmetric**; only the lateralization
    prose (bilateral astereognosis) and the contralateral target differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri.postcentral_gyrus import brodmann_area_3

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.gyri.postcentral_gyrus.brodmann_area_3"
    )

For BA3 via the ``brodmann_areas`` aggregator (the **only** correct way
to reach it from that partition)::

    from ...parietal.brodmann_areas import ITERABLE_AREAS, AREA_PATHS
    # AREA_PATHS["brodmann_area_3"] points at this module

For BA3a and BA3b separately::

    from ...parietal.gyri.postcentral_gyrus.brodmann_area_3 import SUBFIELDS
    # SUBFIELDS["brodmann_area_3a"], SUBFIELDS["brodmann_area_3b"]

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba3_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.gyri.postcentral_gyrus.brodmann_area_3"
        )
        # resolve ba3_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
    (BA3 as a single field; the modern BA3a/BA3b distinction is a later
    refinement.)
*   **BA3a vs BA3b functional dissociation:** *Differential Organization of
    Touch and Pain in Human Primary Somatosensory Cortex* (2000),
    *J Neurophysiol*, 83(3), 1770. BA3b represents the first cortical stage
    of the tactile processing cascade; nociceptive SI responses are
    generated in area 1, not in the tactile hierarchy.
*   **Thalamic input:** Kaas, J.H., et al. (1984); Jones, E.G., & Friedman,
    D.P. (1982); *Thalamocortical connections* (theses.hal.science,
    tel-01186557). **VPL/VPM** → BA3b (densest input); **VPO** → BA3a
    (muscle spindle); **VPS** → BA3a and BA2 (deep receptors).
*   **BA3b as "S1 proper":** Kaas, J.H. (1983); *Cortical lateralization of
    cheirosensory processing in callosal dysgenesis* (2019), *PMC*,
    PMC6541908. "S1 sensu stricto is made up of BA 3b only, or 'S1 proper'".
*   **Hierarchical cascade and fingertip tuning widths:** *Intraparietal
    Sulcus* (ScienceDirect); *Postcentral Gyrus* (ScienceDirect). BA3b
    (2.6 fingertips FWHM) → BA1 (4.0) → BA2 (9.3).
*   **BA3a nociresponsive region / "BA3c":** *A nociresponsive specific area
    of human somatosensory cortex within BA3a: BA3c?* (2020),
    *NeuroImage*, 220, 117074. The depth of the central sulcus contains a
    C-fiber-dominated nociresponsive region associated with slow/burning
    pain; ablation reduces pain sensibility.
*   **Left BA3/BA1 stereognosis dominance:** Moll, J., et al. (2017).
    *Cogn Behav Neurol*, 30(3), 102–115. A small infarct in the crown of
    the left postcentral gyrus (BA1) produced bilateral astereognosis;
    the lesion spared BA3a/BA3b but deprived BA1 of their afferents.
*   **Ipsilateral lip representation in BA3b/BA1:** *Ipsilateral
    representation of oral structures in human anterior parietal
    somatosensory cortex* (pesquisa.bvsalud.org).
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Brodmann area 3 (left); FMA — left postcentral gyrus
    (BA3 partonomy).
"""