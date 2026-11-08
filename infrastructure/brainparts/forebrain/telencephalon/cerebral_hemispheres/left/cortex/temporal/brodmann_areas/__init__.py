"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.brodmann_areas
======================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── brodmann_areas     <-- THIS MODULE

**Ontology:** Brodmann (1909) cytoarchitectonic partition
**Laterality:** left hemisphere
**Parent lobe:** left temporal lobe (lobus temporalis)
**Child count:** **12 Brodmann-area leaves** — the largest Brodmann
aggregator in the temporal lobe.

Overview
--------
Brodmann-area aggregator for the **left temporal lobe**. Each child module
corresponds to one cytoarchitectonic field as defined by Brodmann (1909)
and carried forward in the FMA and NeuroNames ontologies, with modern
refinements from the observer-independent parcellations of Amunts, Zilles,
and colleagues.

The temporal Brodmann inventory is **structurally richer** than the
parietal inventory in three ways that consumers must understand:

1. **Two boundary-case areas shared with the cingulate lobe** — BA15
   (subgenual) and BA48 (retrosplenial). Both also appear in the cingulate
   `brodmann_areas` partition on the left. Consumers that union the
   Brodmann areas of the temporal and cingulate lobes **must deduplicate
   by area number**.

2. **One nested cross-listing** — **BA22** lives under **both**
   `brodmann_areas/brodmann_area_22` (this partition) **and**
   `gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22`
   (the nested Wernicke's-area leaf). This is **different from the BA3
   cross-listing** in the parietal lobe, where BA3 lives **only** under
   the gyrus and is resolved via `AREA_PATHS`. **BA22 has two modules.**

3. **Three cytoarchitectonically hybrid names** — BA27/28/34 (entorhinal
   and piriform) and BA35/36 (perirhinal) are **allocortical or
   transitional** fields whose cytoarchitecture is **not neocortical**.
   The Brodmann map treats them as standard fields, but their
   cytoarchitecture is structurally distinct (fewer layers, less laminar
   differentiation).

**The authoritative iteration contract for this module is
``ITERABLE_AREAS``** — not ``os.listdir`` and not bare ``__all__``. Unlike
the parietal aggregator, **``ITERABLE_AREAS`` and ``LOCAL_AREAS`` are
identical here** (all 12 areas are local). The **nested BA22 module** is
**not** a cross-listing in the `AREA_PATHS` sense — it is a **separate,
structurally identical module** with a different functional framing. See
"Nested BA22 cross-listing" below.

Child Modules
-------------
All 12 Brodmann-area leaves are top-level children of this package:

::

    brodmann_area_15              — subgenual area  ⚠ boundary case (cingulate)
    brodmann_area_20              — inferior temporal (visual semantic)
    brodmann_area_21              — middle temporal (semantic, language)
    brodmann_area_22              — Wernicke's area (left-lateralized) ⚠ NESTED
    brodmann_area_27              — presubicular / piriform (olfactory)
    brodmann_area_28              — entorhinal (MTL memory gateway)
    brodmann_area_34              — dorsal entorhinal
    brodmann_area_35              — perirhinal (memory)
    brodmann_area_36              — perirhinal / parahippocampal (memory)
    brodmann_area_37              — fusiform (VWFA left; FFA right)
    brodmann_area_38              — temporal pole (semantic left; social right)
    brodmann_area_48_retrosubicular — retrosplenial  ⚠ boundary case (cingulate)

Nested BA22 cross-listing
-------------------------
**BA22 is the first area in the tree with a nested cross-listing** — a
Brodmann field that lives under **both** `brodmann_areas/` **and** a
gyral path:

::

    brodmann_areas/
    └── brodmann_area_22      <-- the top-level Brodmann leaf (this partition)

    gyri/
    └── superior_temporal_gyrus/
        └── wernickes_area/
            └── brodmann_area_22   <-- the nested Wernicke's-area leaf

**Both are BA22.** The two modules are **structurally identical** in their
cytoarchitectonic constants (layer structure, cell density, thalamic
input). **Only the functional framing differs:**

*   `brodmann_areas/brodmann_area_22` — **cytoarchitectonic framing**:
    this is BA22 as a Brodmann field, with its laminar organization,
    boundaries, and connectivity. Used by consumers that iterate the
    Brodmann partition.
*   `gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22` —
    **functional framing**: this is BA22 as **Wernicke's area**, the
    speech-comprehension hub. Used by consumers that need the aphasia
    syndrome, the language network, or the clinical framing.

**This is different from BA3 in the parietal lobe:**

| Feature | BA3 (parietal) | BA22 (temporal) |
|---|---|---|
| Top-level leaf under `brodmann_areas/`? | **No** (only under gyrus) | **Yes** |
| Nested under a gyral path? | Yes | **Yes** |
| Resolved via `AREA_PATHS`? | **Yes** | No (two separate modules) |
| Both modules exist? | **No** | **Yes** |
| Purpose of duplication | `AREA_PATHS` hop | **Dual framing** (cytoarchitectonic vs. functional) |

**Consumers must not assume** that `brodmann_areas.brodmann_area_22` and
`gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22` are
different cortical territories. They are the **same territory** with
**different framing**. A consumer that needs Wernicke's area should use
the nested path; a consumer that needs BA22 as a cytoarchitectonic field
should use the top-level path. **Both are correct.**

**On the right hemisphere, the same nested structure exists**, but the
**functional content differs**: the right BA22 is the right superior
temporal auditory/prosodic cortex, not the speech-comprehension hub. The
"Wernicke's area" name is inherited structurally on the right, not
functionally.

Boundary Cases
--------------
Two Brodmann areas in this partition are **boundary cases shared with the
cingulate lobe**:

*   **`brodmann_area_15`** — the **subgenual area**, located at the
    **ventral, medial prefrontal/cingulate junction**. Brodmann
    classified it as part of the temporal lobe, but it sits on the
    **subcallosal/subgenual** surface, which most modern atlases place in
    the **medial frontal/cingulate** territory. It is **also wired**
    under `.../cortex/cingulate/brodmann_areas/brodmann_area_15` (if the
    cingulate partition wires it). Consumers that union the Brodmann
    areas of the temporal and cingulate lobes **must deduplicate by area
    number**.

*   **`brodmann_area_48_retrosubicular`** — the **retrosplenial
    subdivision**, located at the **medial posterior cingulate/medial
    temporal junction**. Brodmann's area 48 is the **retrosubicular
    area** in the retrosplenial complex; it is also mapped as part of the
    **dorsal posterior cingulate** in most modern atlases. It is **also
    wired** under `.../cortex/cingulate/brodmann_areas/
    brodmann_area_48_retrosplenial` (if the cingulate partition wires
    it). Consumers that union the two lobes must deduplicate by area
    number.

**Neither BA15 nor BA48 is a "temporal lobe proper" field.** They sit on
the **medial boundary** between the temporal and cingulate territories,
and the tree's authors placed them in the temporal partition because
Brodmann's original map lists them there. **Consumers should treat them
as boundary cases, not as core temporal cortex.** A spatial query to the
"left temporal lobe" that iterates `ITERABLE_AREAS` will return BA15 and
BA48 — which is correct per Brodmann but **misleading** if the consumer
assumes the result is confined to the temporal convexity.

Hybrid cytoarchitectonic areas
------------------------------
Four areas in this partition are **allocortical or transitional**, not
neocortical:

*   **BA27** — presubicular/piriform (olfactory); **paleocortical**
*   **BA28** — entorhinal; **allocortical** (transitional to
    neocortex)
*   **BA34** — dorsal entorhinal; **allocortical**
*   **BA35** — perirhinal; **periallocortical** (transitional)

These areas appear in the Brodmann map alongside neocortical fields, but
their **cytoarchitecture is structurally distinct** — fewer layers, less
laminar differentiation, and different connectivity. A consumer that
assumes all Brodmann areas have the same cytoarchitectonic type will be
wrong for these four fields. The `CYTOARCHITECTONIC_TYPE` constant below
makes the distinction explicit.

Why this contract exists
~~~~~~~~~~~~~~~~~~~~~~~~
Without explicit constants, three classes of silent bug are possible:

1. **The BA22 double-count.** A consumer that iterates both
   `brodmann_areas.brodmann_area_22` and
   `gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22` will
   double-count BA22 unless it deduplicates by area number.
2. **The BA15/BA48 boundary bleed.** A consumer that iterates the
   temporal `brodmann_areas` and assumes the result is confined to the
   temporal convexity will include BA15 and BA48 — which sit on the
   medial surface, not the lateral temporal convexity.
3. **The allocortical/neocortical conflation.** A consumer that treats
   BA27/28/34/35 as standard neocortical fields will misapply
   computational assumptions (laminar structure, columnar organization,
   etc.) that are **not valid** for allocortical or transitional cortex.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    cingulate partition. The boundary cases (BA15, BA48) are documented as
    **data** (``BOUNDARY_AREAS``), not as structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **``__all__`` lists all 12 local areas.** Unlike the parietal
    aggregator (which lists only ``LOCAL_AREAS`` to exclude the
    cross-listed BA3), the temporal aggregator's ``__all__`` is **equal**
    to ``ITERABLE_AREAS`` — all 12 areas are local.
*   **BA22 is NOT in ``AREA_PATHS``.** Unlike BA3, which must be resolved
    through a non-default path, BA22 has a top-level leaf right here. The
    nested Wernicke's-area leaf is a **dual-framing module**, not a
    resolution target.
*   **``NESTED_CROSS_LISTINGS`` is data, not code.** Add keys as new
    nested cross-listings appear; the contract documents them explicitly.
*   **Boundary areas are data.** ``BOUNDARY_AREAS`` maps the two boundary
    areas to their shared lobe.

Usage
-----
Resolve Brodmann areas by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal import brodmann_areas

    for area in brodmann_areas.ITERABLE_AREAS:
        # iterate the complete temporal Brodmann inventory
        ...

Direct import (fine for single areas)::

    from ...temporal.brodmann_areas import brodmann_area_22

For the nested Wernicke's-area framing of BA22 (functionally named)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 — same territory, different framing

For the boundary-case areas (shared with cingulate)::

    from ...temporal.brodmann_areas import BOUNDARY_AREAS
    # BOUNDARY_AREAS["brodmann_area_15"] = "shared_with_cingulate_subgenual"
    # BOUNDARY_AREAS["brodmann_area_48_retrosubicular"] = "shared_with_cingulate_retrosplenial"

Deduplicated cross-partition iteration (recommended consumer pattern)::

    from ...temporal import brodmann_areas as temporal_bas
    from ...cingulate import brodmann_areas as cingulate_bas

    seen = set()
    for ba in temporal_bas.ITERABLE_AREAS:
        if ba in seen:
            continue
        seen.add(ba)
        # ...
    for ba in cingulate_bas.ITERABLE_AREAS:
        if ba in seen:
            continue
        seen.add(ba)
        # ...

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der
    Grosshirnrinde*. (The classical cytoarchitectonic partition; the
    temporal lobe includes BA15, 20, 21, 22, 27, 28, 34, 35, 36, 37, 38,
    48.)
*   von Economo, C., & Koskinas, G.N. (1925). *Die Cytoarchitektonik der
    Hirnrinde des erwachsenen Menschen*. (Refined cytoarchitectonic
    parcellation of the temporal lobe; correspondence to Brodmann areas
    noted.)
*   **Modern cytoarchitectonic parcellation:** Amunts, K., et al. (2005).
    "Cytoarchitectonic mapping of the human amygdala, hippocampal region
    and entorhinal cortex." *Anat Embryol*; Eickhoff, S.B., et al. (2005).
    "A new SPM toolbox for combining probabilistic cytoarchitectonic maps
    and functional imaging data." *NeuroImage*, 25(4), 1325–1335.
    (Observer-independent parcellations that refine Brodmann's temporal
    areas.)
*   **Wernicke's area and BA22:** Wernicke, C. (1874). *Der aphasische
    Symptomencomplex*. (Classical description of sensory aphasia and its
    localization to the posterior superior temporal gyrus.)
*   **Allocortical / transitional cytoarchitecture (BA27, 28, 34, 35):**
    Insausti, R., et al. (1998). "Entorhinal cortex of the human, monkey,
    and rat." *Hippocampus*, 8(2), 103–124; Witter, M.P., & Amaral, D.G.
    (2004). "Hippocampal formation." In *The Rat Nervous System*, 3rd ed.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed.
*   NeuroNames — Brodmann areas of the temporal lobe (left).
*   FMA — Brodmann areas 15, 20, 21, 22, 27, 28, 34, 35, 36, 37, 38, 48
    (left members).
*   Terminologia Anatomica (FIPAT, 2019) — for gyral / sulcal boundaries
    that the Brodmann fields approximate.
"""