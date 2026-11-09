"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.brodmann_areas
=======================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── brodmann_areas     <-- THIS MODULE

**Ontology:** Brodmann (1909) cytoarchitectonic partition
**Laterality:** right hemisphere
**Parent lobe:** right temporal lobe (lobus temporalis)
**Child count:** **12 Brodmann-area leaves** — the largest Brodmann
aggregator in the temporal lobe.

Overview
--------
Brodmann-area aggregator for the **right temporal lobe**. Structurally
identical to the left-hemisphere twin at
``.../left/cortex/temporal/brodmann_areas``: same 12 areas, same nested
BA22 cross-listing, same two cingulate boundary cases, same four
allocortical/transitional fields, same ``ITERABLE_AREAS`` and
``__all__`` contract. **Only the functional framing of the
left-lateralized areas differs.**

The right temporal Brodmann inventory shares three architectural
properties with the left that consumers must understand:

1. **Two boundary-case areas shared with the cingulate lobe** — BA15
   (subgenual) and BA48 (retrosplenial). Both also appear in the
   **right** cingulate `brodmann_areas` partition. Consumers that union
   the Brodmann areas of the right temporal and right cingulate lobes
   **must deduplicate by area number**.

2. **One nested cross-listing** — **BA22** lives under **both**
   `brodmann_areas/brodmann_area_22` (this partition) **and**
   `gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22` (the
   nested "Wernicke's-area" leaf). On the right side, the **Wernicke's
   area name is inherited structurally**, not functionally — the right
   BA22 is the right superior temporal auditory/prosodic cortex, not the
   speech-comprehension hub.

3. **Four allocortical or transitional fields** — BA27, BA28, BA34,
   BA35. Their cytoarchitecture is **not neocortical** (paleocortical,
   allocortical, periallocortical). A consumer that assumes all Brodmann
   areas are neocortical will be wrong for these four.

**The authoritative iteration contract for this module is
``ITERABLE_AREAS``** — not ``os.listdir`` and not bare ``__all__``. As on
the left, **``ITERABLE_AREAS`` and ``LOCAL_AREAS`` are identical here**
(all 12 areas are local). The **nested BA22 module** is a **separate,
structurally identical module** with a different functional framing — not
an `AREA_PATHS` resolution target.

Child Modules
-------------
All 12 Brodmann-area leaves are top-level children of this package —
**structurally identical to the left hemisphere**:

::

    brodmann_area_15              — subgenual area  ⚠ boundary case (cingulate)
    brodmann_area_20              — inferior temporal (non-verbal visual semantic)
    brodmann_area_21              — middle temporal (non-verbal semantic, prosodic)
    brodmann_area_22              — right superior temporal auditory/prosodic ⚠ NESTED
    brodmann_area_27              — presubicular / piriform (olfactory)
    brodmann_area_28              — entorhinal (MTL memory gateway)
    brodmann_area_34              — dorsal entorhinal
    brodmann_area_35              — perirhinal (memory)
    brodmann_area_36              — perirhinal / parahippocampal (memory)
    brodmann_area_37              — fusiform (FFA right; VWFA left)
    brodmann_area_38              — temporal pole (social/emotional right; semantic left)
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
            └── brodmann_area_22   <-- the nested "Wernicke's-area" leaf

**Both are BA22** — but on the **right** side, the two modules carry
**different functional framings**:

*   `brodmann_areas/brodmann_area_22` — **cytoarchitectonic framing**:
    this is right BA22 as a Brodmann field, with its laminar
    organization, boundaries, and connectivity. Used by consumers that
    iterate the Brodmann partition.
*   `gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22` —
    **inherited functional framing**: this is **right BA22** as the
    right superior temporal auditory/prosodic cortex. The "Wernicke's
    area" name is inherited structurally, **not** functionally accurate
    on the right.

**Critical difference from the left**: on the left, the nested leaf is
the **speech-comprehension hub** (true Wernicke's area). On the right,
the nested leaf is the **prosodic and non-verbal auditory cortex**. A
consumer that assumes the right nested BA22 produces Wernicke's aphasia
when lesioned will be **wrong** — Wernicke's aphasia is **left-
lateralized**.

**Consumers must not assume** that `brodmann_areas.brodmann_area_22`
and `gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22` are
different cortical territories. They are the **same territory** with
**different framing**. Both are correct.

Boundary Cases
--------------
Two Brodmann areas in this partition are **boundary cases shared with the
right cingulate lobe** — **identical to the left**:

*   **`brodmann_area_15`** — the **subgenual area**, located at the
    **ventral, medial prefrontal/cingulate junction**. It is also wired
    under `.../right/cortex/cingulate/brodmann_areas/brodmann_area_15`
    (if the right cingulate partition wires it). Consumers that union
    the Brodmann areas of the right temporal and right cingulate lobes
    **must deduplicate by area number**.

*   **`brodmann_area_48_retrosubicular`** — the **retrosplenial
    subdivision**, located at the **medial posterior cingulate/medial
    temporal junction**. It is also wired under
    `.../right/cortex/cingulate/brodmann_areas/
    brodmann_area_48_retrosplenial` (if the right cingulate partition
    wires it). Consumers must deduplicate.

**Neither BA15 nor BA48 is a "right temporal lobe proper" field.** They
sit on the **medial boundary** between the right temporal and right
cingulate territories. A spatial query to the "right temporal lobe" that
iterates `ITERABLE_AREAS` will return BA15 and BA48 — which is correct per
Brodmann but **misleading** if the consumer assumes the result is
confined to the temporal convexity.

Hybrid cytoarchitectonic areas
------------------------------
Four areas in this partition are **allocortical or transitional**, not
neocortical — **identical to the left**:

*   **BA27** — presubicular/piriform (olfactory); **paleocortical**
*   **BA28** — entorhinal; **allocortical** (transitional to neocortex)
*   **BA34** — dorsal entorhinal; **allocortical**
*   **BA35** — perirhinal; **periallocortical** (transitional)

These areas appear in the Brodmann map alongside neocortical fields, but
their **cytoarchitecture is structurally distinct** — fewer layers, less
laminar differentiation, and different connectivity. A consumer that
assumes all Brodmann areas have the same cytoarchitectonic type will be
wrong for these four fields. The `CYTOARCHITECTONIC_TYPE` constant below
makes the distinction explicit.

Functional Framing Differences (Right vs Left)
----------------------------------------------
The **structural inventory is identical** between the right and left
temporal Brodmann aggregators. What differs is the **functional framing
attached to specific areas** — documented here as data, not as a
structural difference:

| Area | Left functional framing | Right functional framing |
|---|---|---|
| **BA20** | Visual semantic (verbal) | Non-verbal visual semantic |
| **BA21** | Semantic language; sentence comprehension | Prosodic comprehension; non-verbal semantic |
| **BA22** | **Wernicke's area** — speech comprehension | Right superior temporal auditory / prosodic cortex |
| **BA37** | VWFA — visual word form area | **FFA** — fusiform face area |
| **BA38** | Verbal semantic hub | **Social/emotional hub** |
| **MT (cortex)** | contributing | **right-dominant** for motion |
| **MST (standalone)** | contributing | **right-dominant** for egomotion |
| **BA27, 28, 34, 35, 15, 48** | symmetric | symmetric |

**The functional inversion does not change the Brodmann aggregator
contract** — it only changes the prose attached to each area's docstring.
This module documents the **contract**, not the per-area function; per-area
documentation lives in the leaf modules.

Why this contract exists
~~~~~~~~~~~~~~~~~~~~~~~~
Same three classes of silent bug as the left twin:

1. **The BA22 double-count.** Iterating both
   `brodmann_areas.brodmann_area_22` and
   `gyri.superior_temporal_gyrus/wernickes_area/brodmann_area_22` will
   double-count BA22 unless the consumer deduplicates by area number.
   **On the right side, the double-count is especially insidious** —
   both modules carry the "Wernicke's" name, so a naive consumer might
   assume the right nested leaf also produces Wernicke's aphasia when
   damaged. It does not.
2. **The BA15/BA48 boundary bleed.** Iterating the right temporal
   `brodmann_areas` and assuming the result is confined to the temporal
   convexity will include BA15 and BA48 — which sit on the medial
   surface.
3. **The allocortical/neocortical conflation.** Treating BA27/28/34/35
   as standard neocortical fields will misapply computational
   assumptions (laminar structure, columnar organization) that are **not
   valid** for allocortical or transitional cortex.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    right cingulate partition. Boundary cases (BA15, BA48) are documented
    as **data** (``BOUNDARY_AREAS``), not as structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **``__all__`` lists all 12 local areas.** Equal to
    ``ITERABLE_AREAS`` — all 12 areas are local.
*   **BA22 is NOT in ``AREA_PATHS``.** BA22 has a top-level leaf right
    here; the nested "Wernicke's-area" leaf is a **dual-framing module**,
    not a resolution target.
*   **``NESTED_CROSS_LISTINGS`` is data, not code.** The constant
    documents BA22's dual framing, **and explicitly notes that the
    right nested leaf is prosodic, not speech-comprehension**.
*   **Boundary areas are data.** ``BOUNDARY_AREAS`` maps the two boundary
    areas to their shared lobe.
*   **Structural parity with left.** Left and right temporal Brodmann
    aggregators are **structurally identical** in every constant; only
    the functional framing prose on five areas differs.

Usage
-----
Resolve Brodmann areas by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal import brodmann_areas

    for area in brodmann_areas.ITERABLE_AREAS:
        # iterate the complete right temporal Brodmann inventory
        ...

Direct import (fine for single areas)::

    from ...temporal.brodmann_areas import brodmann_area_22

For the nested right "Wernicke's-area" framing (prosodic cortex)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 — same territory, prosodic framing;
    # NOT the speech-comprehension hub

For the boundary-case areas (shared with right cingulate)::

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

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pkg = importlib.import_module(
            f"infrastructure.brainparts.forebrain.telencephalon."
            f"cerebral_hemispheres.{side}.cortex.temporal.brodmann_areas"
        )
        for area in pkg.ITERABLE_AREAS:
            # resolve area through the corresponding temporal partition
            ...

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der
    Grosshirnrinde*. (The classical cytoarchitectonic partition; the
    temporal lobe includes BA15, 20, 21, 22, 27, 28, 34, 35, 36, 37, 38,
    48 — bilaterally.)
*   von Economo, C., & Koskinas, G.N. (1925). *Die Cytoarchitektonik der
    Hirnrinde des erwachsenen Menschen*. (Refined cytoarchitectonic
    parcellation of the temporal lobe.)
*   **Modern cytoarchitectonic parcellation:** Amunts, K., et al. (2005).
    "Cytoarchitectonic mapping of the human amygdala, hippocampal region
    and entorhinal cortex." *Anat Embryol*; Eickhoff, S.B., et al.
    (2005). "A new SPM toolbox for combining probabilistic
    cytoarchitectonic maps and functional imaging data." *NeuroImage*,
    25(4), 1325–1335.
*   **Right temporal functional framing (prosody, music, faces):**
    Ross, E.D. (1981). "The aprosodias: functional-anatomic organization
    of the affective components of language in the right hemisphere."
    *Arch Neurol*, 38(9), 561–569.
*   **Right FFA dominance:** Kanwisher, N., McDermott, J., & Chun, M.M.
    (1997). "The fusiform face area: a module in human extrastriate
    cortex specialized for face perception." *J Neurosci*, 17(11),
    4302–4311.
*   **Right temporal pole — social/emotional semantics:** Zahn, R., et
    al. (2007). "Social concepts are represented in the superior anterior
    temporal cortex." *PNAS*, 104(15), 6430–6435.
*   **Allocortical / transitional cytoarchitecture (BA27, 28, 34, 35):**
    Insausti, R., et al. (1998). "Entorhinal cortex of the human, monkey,
    and rat." *Hippocampus*, 8(2), 103–124; Witter, M.P., & Amaral, D.G.
    (2004). "Hippocampal formation." In *The Rat Nervous System*, 3rd ed.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed.
*   NeuroNames — Brodmann areas of the temporal lobe (right).
*   FMA — Brodmann areas 15, 20, 21, 22, 27, 28, 34, 35, 36, 37, 38, 48
    (right members).
*   Terminologia Anatomica (FIPAT, 2019) — for gyral / sulcal boundaries
    that the Brodmann fields approximate.
"""