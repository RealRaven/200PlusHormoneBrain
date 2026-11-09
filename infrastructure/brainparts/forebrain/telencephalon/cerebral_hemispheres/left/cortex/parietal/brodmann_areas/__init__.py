"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.brodmann_areas
=======================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── brodmann_areas     <-- THIS MODULE

**Ontology:** Brodmann (1909) cytoarchitectonic partition
**Laterality:** left hemisphere
**Parent lobe:** left parietal lobe (lobus parietalis dexter laterality = left)

Overview
--------
Brodmann-area aggregator for the **left parietal lobe**. Each child module
corresponds to one cytoarchitectonic field as defined by Brodmann (1909) and
carried forward in the FMA and NeuroNames ontologies.

Brodmann's map is a *cytoarchitectonic* partition — it does **not** respect
gyral/sulcal boundaries. This aggregator mirrors that partition faithfully,
which means two things for consumers:

1. An area may be listed here even when its primary **gyral** home lives
   elsewhere in the tree (see ``ITERABLE_AREAS`` below).
2. Conversely, a gyral folder may carry a Brodmann child with **no** top-level
   twin in this aggregator.

**The authoritative iteration contract for this module is ``ITERABLE_AREAS``**
— not ``os.listdir`` and not bare ``__all__``. Downstream consumers (memory
stores, recall weights, hormone gating) must iterate ``ITERABLE_AREAS`` so that
cross-listed areas (notably **BA3**) are not silently missed.

Child Modules (top-level in this package)
-----------------------------------------
::

    brodmann_area_1   — S1, postcentral gyrus (anterior bank of central sulcus)
    brodmann_area_2   — S1, postcentral gyrus (crown)
    brodmann_area_5   — somatosensory association cortex (PPC, superior parietal)
    brodmann_area_7   — visuomotor / spatial association (PPC, superior parietal)
    brodmann_area_26  — ectosplenial area  ⚠ boundary case, see below
    brodmann_area_39  — angular gyrus (inferior parietal lobule)
    brodmann_area_40  — supramarginal gyrus (inferior parietal lobule)

Cross-listed Area (NOT in this package)
---------------------------------------
::

    brodmann_area_3   — S1, posterior bank of central sulcus

BA3 lives at ``.../parietal/gyri/postcentral_gyrus/brodmann_area_3``. It is a
parietal Brodmann area by any anatomical reading, but the project groups it
under the gyrus because that is where its cytoarchitectonic territory sits. It
is included in ``ITERABLE_AREAS`` below so that a hemisphere-wide iteration
over Brodmann fields is complete.

⚠ Boundary case: brodmann_area_26
---------------------------------
BA26 (ectosplenial area) sits on the cingulate/retrosplenial–parietal border.
Most atlases place it primarily in the **cingulate** ribbon; it appears in the
parietal Brodmann listing because it crosses the boundary. It is **also**
wired under ``.../cortex/cingulate/brodmann_areas/brodmann_area_26_retrosplenial``.
This duplication is intentional. Consumers that union ``brodmann_areas`` of
cingulate and parietal must **deduplicate by area number**.

Iteration contract
------------------
The module exposes three constants plus ``__all__``::

    # Complete set of parietal Brodmann fields, including cross-listed BA3.
    ITERABLE_AREAS = (
        "brodmann_area_1",
        "brodmann_area_2",
        "brodmann_area_3",    # cross-listed; lives under gyri.postcentral_gyrus
        "brodmann_area_5",
        "brodmann_area_7",
        "brodmann_area_26",   # boundary case; also under cingulate
        "brodmann_area_39",
        "brodmann_area_40",
    )

    # Subset directly importable from this package (no cross-module hop).
    LOCAL_AREAS = (
        "brodmann_area_1",
        "brodmann_area_2",
        "brodmann_area_5",
        "brodmann_area_7",
        "brodmann_area_26",
        "brodmann_area_39",
        "brodmann_area_40",
    )

    # Per-area importable dotted paths (only where the local default fails).
    # Consumers resolve as:  AREA_PATHS.get(area, f"{__name__}.{area}")
    AREA_PATHS = {
        "brodmann_area_3": (
            "infrastructure.brainparts.forebrain.telencephalon."
            "cerebral_hemispheres.left.cortex.parietal."
            "gyri.postcentral_gyrus.brodmann_area_3"
        ),
    }

    __all__ = list(LOCAL_AREAS)

Why this contract exists
~~~~~~~~~~~~~~~~~~~~~~~~
Without ``ITERABLE_AREAS`` and ``AREA_PATHS``, three classes of silent bug are
possible:

1. **The BA3 gap.** A consumer iterating ``os.listdir`` of this package will
   enumerate 7 areas and miss primary somatosensory cortex's most posterior
   field. Anyone building a somatosensory map from this package alone will be
   wrong by omission. ``ITERABLE_AREAS`` closes the gap; ``AREA_PATHS`` makes
   the hop importable.
2. **The BA26 double-count.** A consumer unioning parietal and cingulate
   Brodmann sets will count BA26 twice unless it deduplicates by number.
3. **String-path drift.** Consumers that build paths by f-string concatenation
   of ``__name__ + area`` will silently miss the BA3 hop. ``AREA_PATHS``
   localises that hop in one place and makes it greppable.

Design Contract
---------------
* **No side effects on import.** Pure namespace.
* **No cross-hemisphere imports.** Left side only.
* **No hormone imports.** Dependency DAG unchanged:
  ``chemicals_hormones → memory → brainparts``.
* **``__all__`` lists only ``LOCAL_AREAS``**, so ``from ... import *`` is safe
  but **not** the recommended iteration contract — use ``ITERABLE_AREAS``.
* **``AREA_PATHS`` is data, not code.** Add keys as new cross-listings appear;
  the ``.get(area, f"{__name__}.{area}")`` fallback is the default resolver.

Usage
-----
Complete, BA3-safe iteration::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.brodmann_areas import (
        ITERABLE_AREAS, LOCAL_AREAS, AREA_PATHS,
    )

    for area in ITERABLE_AREAS:
        path = AREA_PATHS.get(area, f"{__name__}.{area}")

Direct import (fine for single areas)::

    from ...parietal.brodmann_areas import brodmann_area_39   # angular gyrus

Cross-listed (go through the gyrus, not this package)::

    from ...parietal.gyri.postcentral_gyrus import brodmann_area_3

References
----------
* Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
* Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
* NeuroNames — Brodmann areas (left hemisphere).
* FMA — Brodmann area 1, 2, 3, 5, 7, 26, 39, 40 (left members).
* Terminologia Anatomica (FIPAT, 2019) — for gyral / sulcal boundaries.
"""