"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal
=========================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal          <-- THIS MODULE

**Primary synonym:** Parietal lobe (lobus parietalis)
**FMA ID:** 61826 (left parietal lobe)
**NeuroNames ID:** 93 (Parietal lobe, left)
**Embryological origin:** Dorsal pallium (pallium dorsale) — alar plate derivative

Overview
--------
The **parietal lobe** is the dorsal-most neocortical lobe of the left cerebral
hemisphere. It lies posterior to the frontal lobe (separated by the central
sulcus), anterior to the occipital lobe (separated by the parieto-occipital
sulcus), and superior to the temporal lobe (separated by the lateral sulcus /
Sylvian fissure).

Functionally, the left parietal lobe is the principal substrate for:

* **Somatosensory processing** — primary (S1, Brodmann 3/1/2) and secondary
  (S2) somatosensory cortex.
* **Spatial attention and body schema** — posterior parietal cortex (PPC,
  Brodmann 5/7), especially in the left hemisphere where it supports
  praxis and language-adjacent spatial functions.
* **Multisensory integration** — convergence of tactile, proprioceptive,
  visual, and auditory streams.
* **Numerical and symbolic cognition** — angular gyrus (Brodmann 39)
  and supramarginal gyrus (Brodmann 40) of the left hemisphere.
* **Praxis / tool use** — left inferior parietal lobule.

In the **200PlusHormoneBrain** architecture, this module is the container for
the left parietal lobe's anatomical primitives. Each child module corresponds
to a discrete FMA/NeuroNames entity and is intended to be an importable,
introspectable unit of brain structure — usable by memory stores, hormone
gating, and recall-weighting logic that need to tag or query parietal function.

Child Modules
-------------
This package re-exports nothing at the `__init__` level; children are imported
explicitly to keep the namespace flat and to mirror the FMA partonomy exactly.

Brodmann Areas
~~~~~~~~~~~~~~
Located under :mod:`...parietal.brodmann_areas`:

* ``brodmann_area_1`` — primary somatosensory, postcentral gyrus (S1)
* ``brodmann_area_2`` — primary somatosensory, postcentral gyrus (S1)
* ``brodmann_area_3`` — primary somatosensory, postcentral gyrus (S1) *
  *(note: also wired under ``gyri.postcentral_gyrus`` — retained here for
  Brodmann-indexed lookup)*
* ``brodmann_area_5`` — somatosensory association cortex (PPC)
* ``brodmann_area_7`` — visuomotor / spatial association cortex (PPC)
* ``brodmann_area_26`` — ectosplenial area *(boundary case; overlaps with
  cingulate/retrosplenial in some atlases)*
* ``brodmann_area_39`` — angular gyrus
* ``brodmann_area_40`` — supramarginal gyrus

Cortex Regions
~~~~~~~~~~~~~~
Located under :mod:`...parietal.cortex`:

* ``primary_somatosensory_cortex`` — S1 (Brodmann 3/1/2)
* ``secondary_somatosensory_cortex`` — S2 (opercular region)
* ``posterior_parietal_cortex`` — PPC (Brodmann 5/7)

Gyri
~~~~
Located under :mod:`...parietal.gyri`:

* ``postcentral_gyrus`` — containing ``brodmann_area_3``
* ``paracentral_lobule`` — medial surface, shared with frontal lobe
* ``precuneus`` — medial surface, posterior to paracentral lobule

Sulci
~~~~~
Located under :mod:`...parietal.sulci`:

* ``intraparietal_sulcus`` — separates superior and inferior parietal lobules
* ``postcentral_sulcus`` — posterior boundary of postcentral gyrus
* ``marginal_sulcus`` — medial surface, bounds precuneus

Lateralization Notes
--------------------
This is the **left** parietal lobe. Right-hemisphere equivalents live under
``...cerebral_hemispheres.right.cortex.parietal``. Asymmetric functional
weightings (e.g., left-lateralized praxis, language-adjacent number
cognition) are encoded at the *consumer* layer (memory stores, recall
weights), not duplicated here.

Design Contract
---------------
* **No side effects on import.** This `__init__.py` is a pure namespace.
* **No cross-hemisphere imports.** Left- and right-hemisphere modules never
  import each other; hemisphere is a path dimension, not a runtime flag.
* **No hormone imports here.** Hormone wiring (`infrastructure.chemicals_hormones`)
  references parietal paths by *string* through the memory/recall layer, not
  by direct import — preserving a clean dependency DAG:
  ``chemicals_hormones → memory → brainparts``.

Usage
-----
Resolve by path (preferred — decoupled from Python imports)::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal \
        import brodmann_areas, cortex, gyri, sulci

    s1 = cortex.primary_somatosensory_cortex
    ppc = cortex.posterior_parietal_cortex

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.cortex.primary_somatosensory_cortex"
    )

References
----------
* FMA: 61826 — Left parietal lobe
* NeuroNames: 93 — Parietal lobe (left)
* Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
* Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
* Terminologia Anatomica (FIPAT, 2019) — A14.1.09.001 (lobus parietalis)
"""