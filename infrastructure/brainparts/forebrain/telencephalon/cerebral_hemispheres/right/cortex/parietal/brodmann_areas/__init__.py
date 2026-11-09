"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas
========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── brodmann_areas     <-- THIS MODULE

**Ontology:** Brodmann (1909) cytoarchitectonic partition
**Laterality:** right hemisphere
**Parent lobe:** right parietal lobe (lobus parietalis, laterality = right)

Overview
--------
Brodmann-area aggregator for the **right parietal lobe**. Structurally
identical to the left-hemisphere twin at
``.../left/cortex/parietal/brodmann_areas``; only the laterality segment
differs. Every contract described in the left module — ``ITERABLE_AREAS``,
``LOCAL_AREAS``, ``AREA_PATHS``, the BA3 cross-listing, and the BA26
boundary case — applies verbatim here.

Consumers that iterate hemispheres must treat these two modules as
**interchangeable by shape**: same iteration constants, same names, same
cross-listing structure. Hemisphere-specific *behaviour* belongs to the
consumer layer (memory stores, recall weights, hormone gating), never to
this module.

Brodmann's map is a *cytoarchitectonic* partition — it does **not** respect
gyral/sulcal boundaries. That caveat applies symmetrically to both
hemispheres. The authoritative iteration contract is ``ITERABLE_AREAS``, not
``os.listdir`` and not bare ``__all__``.

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

BA3 lives at ``.../right/parietal/gyri/postcentral_gyrus/brodmann_area_3``.
It is included in ``ITERABLE_AREAS`` so that a hemisphere-wide iteration over
Brodmann fields is complete. See the left-module docstring for the full
rationale — it applies identically here.

⚠ Boundary case: brodmann_area_26
---------------------------------
BA26 (ectosplenial area) sits on the cingulate/retrosplenial–parietal border.
It is **also** wired under
``.../right/cortex/cingulate/brodmann_areas/brodmann_area_26_retrosplenial``.
Consumers unioning ``brodmann_areas`` of cingulate and parietal on the right
side must **deduplicate by area number** — same rule as the left side.

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
            "cerebral_hemispheres.right.cortex.parietal."
            "gyri.postcentral_gyrus.brodmann_area_3"
        ),
    }

    __all__ = list(LOCAL_AREAS)

Why this contract exists
~~~~~~~~~~~~~~~~~~~~~~~~
Same three failure modes as the left hemisphere — BA3 omission, BA26
double-count, string-path drift — all of which are hemisphere-agnostic. See
the left-module docstring for the detailed walkthrough.

Lateralization Notes
--------------------
The **Brodmann field inventory is identical** between left and right parietal
lobes. What differs is functional weighting (documented at the consumer
layer, not encoded here):

* Right BA39 (angular gyrus) participates more strongly in visuospatial and
  attentional reorienting; left BA39 is language-adjacent.
* Right BA40 (supramarginal gyrus) shows greater involvement in spatial
  attention; left BA40 in praxis and phonological processing.
* Right BA7 and right intraparietal fields carry the dominant role in
  contralateral (left-hemibody) spatial attention and body schema — the
  anatomical substrate of left hemispatial neglect when lesioned.
* Right S1 (BA3/1/2) represents the **left** hemibody; left S1 represents the
  right hemibody. This decussation is a property of the anatomical wiring,
  not of any module in this package.

None of the above is encoded as code paths. Both hemisphere aggregators must
remain structurally interchangeable so that bilateral consumers can write
``for side in ("left", "right"): ...`` without special-casing.

Design Contract
---------------
* **No side effects on import.** Pure namespace.
* **No cross-hemisphere imports.** Right side only.
* **No hormone imports.** Dependency DAG unchanged:
  ``chemicals_hormones → memory → brainparts``.
* **``__all__`` lists only ``LOCAL_AREAS``**, so ``from ... import *`` is safe
  but **not** the recommended iteration contract — use ``ITERABLE_AREAS``.
* **``AREA_PATHS`` is data, not code.** Add keys as new cross-listings appear;
  the ``.get(area, f"{__name__}.{area}")`` fallback is the default resolver.

Usage
-----
Complete, BA3-safe iteration on the right side::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas import (
        ITERABLE_AREAS, LOCAL_AREAS, AREA_PATHS,
    )

    for area in ITERABLE_AREAS:
        path = AREA_PATHS.get(area, f"{__name__}.{area}")

Direct import (fine for single areas)::

    from ...parietal.brodmann_areas import brodmann_area_40   # supramarginal gyrus

Cross-listed (go through the gyrus, not this package)::

    from ...parietal.gyri.postcentral_gyrus import brodmann_area_3

Bilateral iteration (the recommended consumer pattern)::

    for side in ("left", "right"):
        pkg = importlib.import_module(
            f"infrastructure.brainparts.forebrain.telencephalon."
            f"cerebral_hemispheres.{side}.cortex.parietal.brodmann_areas"
        )
        for area in pkg.ITERABLE_AREAS:
            path = pkg.AREA_PATHS.get(area, f"{pkg.__name__}.{area}")

References
----------
* Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
* Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
* NeuroNames — Brodmann areas (right hemisphere).
* FMA — Brodmann area 1, 2, 3, 5, 7, 26, 39, 40 (right members).
* Terminologia Anatomica (FIPAT, 2019) — for gyral / sulcal boundaries.
"""