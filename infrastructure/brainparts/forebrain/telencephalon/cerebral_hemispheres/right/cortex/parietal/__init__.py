"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal
==========================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal          <-- THIS MODULE

**Primary synonym:** Right parietal lobe (lobus parietalis dexter)
**Terminologia Anatomica:** A14.1.09.001 (lobus parietalis) + laterality = right
**NeuroNames:** 93 (Parietal lobe) with laterality attribute = right
**Embryological origin:** Dorsal pallium (pallium dorsale) — alar plate derivative

Overview
--------
The **right parietal lobe** is the dorsal neocortical lobe of the right cerebral
hemisphere. It is the exact anatomical mirror of its left counterpart: same
Brodmann fields, same gyral and sulcal architecture, same FMA partonomy — but
distinguished by **functional lateralization** and by being addressed through a
different path in the hierarchy.

Functionally, the right parietal lobe is the dominant hemisphere for:

* **Spatial attention and arousal** — the right-hemisphere ventral attention
  network (temporoparietal junction, right inferior parietal lobule) is the
  principal driver of orienting to salient contralateral and ipsilateral
  stimuli. Right-sided lesions produce **hemispatial neglect** far more often
  and more severely than left-sided lesions.
* **Body schema and corporeal awareness** — right superior parietal lobule and
  intraparietal sulcus support the online body model. Lesions produce
  **anosognosia**, **somatoparaphrenia**, and **personal neglect**.
* **Visuospatial and constructional processing** — mental rotation, line
  bisection, figure copying. Right parietal damage → **constructional apraxia**.
* **Contralateral somatosensation** — right S1 represents the **left** side of
  the body (decussated); right S2 mirrors this for the left hemibody.
* **Multisensory spatial integration** — right intraparietal sulcus carries a
  privileged role in cross-modal spatial remapping (visual–tactile–auditory).
* **Attentional reorienting** — right TPJ is a core node of the salience/
  reorienting network.

In the **200PlusHormoneBrain** architecture, this module is the container for
the right parietal lobe's anatomical primitives. It is structurally identical
to the left module; the only differences are the path segment (`right` vs
`left`) and the downstream functional annotations applied by consumers
(memory stores, recall weights, hormone gating).

Child Modules
-------------
Identical to the left parietal lobe (verified against the left module tree).
Children are imported explicitly; nothing is re-exported at the `__init__`
level, so the namespace stays flat and the FMA partonomy stays legible.

Brodmann Areas
~~~~~~~~~~~~~~
Located under :mod:`...parietal.brodmann_areas`:

* ``brodmann_area_1`` — primary somatosensory, postcentral gyrus (S1)
* ``brodmann_area_2`` — primary somatosensory, postcentral gyrus (S1)
* ``brodmann_area_5`` — somatosensory association cortex (PPC)
* ``brodmann_area_7`` — visuomotor / spatial association cortex (PPC)
* ``brodmann_area_26`` — ectosplenial area *(boundary case; overlaps
  cingulate/retrosplenial in some atlases)*
* ``brodmann_area_39`` — angular gyrus
* ``brodmann_area_40`` — supramarginal gyrus

*Note:* ``brodmann_area_3`` is **not** duplicated at this level — it lives
under ``gyri.postcentral_gyrus.brodmann_area_3``, matching the left module.
This is deliberate and consistent (see left-parietal docstring).

Cortex Regions
~~~~~~~~~~~~~~
Located under :mod:`...parietal.cortex`:

* ``primary_somatosensory_cortex`` — S1 (Brodmann 3/1/2); left hemibody
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
This is the **right** parietal lobe. Left-hemisphere equivalents live under
``...cerebral_hemispheres.left.cortex.parietal``.

**Documented anatomical asymmetries** (descriptive, not encoded as code paths):

* The right intraparietal sulcus and right inferior parietal lobule are on
  average **larger** in surface area and show greater sulcal depth than the
  left (Van Essen et al., 2012; Goldberg et al., 2013).
* The right angular gyrus sits slightly more posterior and inferior relative
  to the left in most individuals; the left angular gyrus is larger and more
  anteriorly extended.
* Functional weightings (spatial attention, body schema, neglect vulnerability)
  are encoded at the **consumer** layer — not duplicated here.

**Do not** encode side-specific behaviour in this module. The right module and
left module must remain structurally interchangeable so that consumers can
iterate hemispheres generically.

Design Contract
---------------
* **No side effects on import.** Pure namespace.
* **No cross-hemisphere imports.** Left and right modules never import each
  other. Hemisphere is a path dimension, not a runtime flag.
* **No hormone imports here.** `infrastructure.chemicals_hormones` references
  parietal paths by string via the memory/recall layer. Dependency DAG stays:
  ``chemicals_hormones → memory → brainparts``.
* **Bilateral consumers** must iterate hemispheres (``for side in ("left",
  "right")``) rather than importing both — this keeps the import graph a tree,
  not a diamond.

Usage
-----
Resolve by path (preferred)::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal \
        import brodmann_areas, cortex, gyri, sulci

    s1_r  = cortex.primary_somatosensory_cortex   # left hemibody
    ppc_r = cortex.posterior_parietal_cortex      # right-dominant spatial network

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.cortex.posterior_parietal_cortex"
    )

References
----------
* Terminologia Anatomica (FIPAT, 2019) — A14.1.09.001 (lobus parietalis)
* NeuroNames 93 — Parietal lobe (laterality = right)
* Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
* Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
* Van Essen, D.C. et al. (2012). *Cereb Cortex* 22(10):2225–2246 — cortical
  asymmetries.
* Goldberg, E. et al. (2013). *The New Executive Brain* — right-hemisphere
  dominance for spatial attention.
""""""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal
==========================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal          <-- THIS MODULE

**Primary synonym:** Right parietal lobe (lobus parietalis dexter)
**Terminologia Anatomica:** A14.1.09.001 (lobus parietalis) + laterality = right
**NeuroNames:** 93 (Parietal lobe) with laterality attribute = right
**Embryological origin:** Dorsal pallium (pallium dorsale) — alar plate derivative

Overview
--------
The **right parietal lobe** is the dorsal neocortical lobe of the right cerebral
hemisphere. It is the exact anatomical mirror of its left counterpart: same
Brodmann fields, same gyral and sulcal architecture, same FMA partonomy — but
distinguished by **functional lateralization** and by being addressed through a
different path in the hierarchy.

Functionally, the right parietal lobe is the dominant hemisphere for:

* **Spatial attention and arousal** — the right-hemisphere ventral attention
  network (temporoparietal junction, right inferior parietal lobule) is the
  principal driver of orienting to salient contralateral and ipsilateral
  stimuli. Right-sided lesions produce **hemispatial neglect** far more often
  and more severely than left-sided lesions.
* **Body schema and corporeal awareness** — right superior parietal lobule and
  intraparietal sulcus support the online body model. Lesions produce
  **anosognosia**, **somatoparaphrenia**, and **personal neglect**.
* **Visuospatial and constructional processing** — mental rotation, line
  bisection, figure copying. Right parietal damage → **constructional apraxia**.
* **Contralateral somatosensation** — right S1 represents the **left** side of
  the body (decussated); right S2 mirrors this for the left hemibody.
* **Multisensory spatial integration** — right intraparietal sulcus carries a
  privileged role in cross-modal spatial remapping (visual–tactile–auditory).
* **Attentional reorienting** — right TPJ is a core node of the salience/
  reorienting network.

In the **200PlusHormoneBrain** architecture, this module is the container for
the right parietal lobe's anatomical primitives. It is structurally identical
to the left module; the only differences are the path segment (`right` vs
`left`) and the downstream functional annotations applied by consumers
(memory stores, recall weights, hormone gating).

Child Modules
-------------
Identical to the left parietal lobe (verified against the left module tree).
Children are imported explicitly; nothing is re-exported at the `__init__`
level, so the namespace stays flat and the FMA partonomy stays legible.

Brodmann Areas
~~~~~~~~~~~~~~
Located under :mod:`...parietal.brodmann_areas`:

* ``brodmann_area_1`` — primary somatosensory, postcentral gyrus (S1)
* ``brodmann_area_2`` — primary somatosensory, postcentral gyrus (S1)
* ``brodmann_area_5`` — somatosensory association cortex (PPC)
* ``brodmann_area_7`` — visuomotor / spatial association cortex (PPC)
* ``brodmann_area_26`` — ectosplenial area *(boundary case; overlaps
  cingulate/retrosplenial in some atlases)*
* ``brodmann_area_39`` — angular gyrus
* ``brodmann_area_40`` — supramarginal gyrus

*Note:* ``brodmann_area_3`` is **not** duplicated at this level — it lives
under ``gyri.postcentral_gyrus.brodmann_area_3``, matching the left module.
This is deliberate and consistent (see left-parietal docstring).

Cortex Regions
~~~~~~~~~~~~~~
Located under :mod:`...parietal.cortex`:

* ``primary_somatosensory_cortex`` — S1 (Brodmann 3/1/2); left hemibody
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
This is the **right** parietal lobe. Left-hemisphere equivalents live under
``...cerebral_hemispheres.left.cortex.parietal``.

**Documented anatomical asymmetries** (descriptive, not encoded as code paths):

* The right intraparietal sulcus and right inferior parietal lobule are on
  average **larger** in surface area and show greater sulcal depth than the
  left (Van Essen et al., 2012; Goldberg et al., 2013).
* The right angular gyrus sits slightly more posterior and inferior relative
  to the left in most individuals; the left angular gyrus is larger and more
  anteriorly extended.
* Functional weightings (spatial attention, body schema, neglect vulnerability)
  are encoded at the **consumer** layer — not duplicated here.

**Do not** encode side-specific behaviour in this module. The right module and
left module must remain structurally interchangeable so that consumers can
iterate hemispheres generically.

Design Contract
---------------
* **No side effects on import.** Pure namespace.
* **No cross-hemisphere imports.** Left and right modules never import each
  other. Hemisphere is a path dimension, not a runtime flag.
* **No hormone imports here.** `infrastructure.chemicals_hormones` references
  parietal paths by string via the memory/recall layer. Dependency DAG stays:
  ``chemicals_hormones → memory → brainparts``.
* **Bilateral consumers** must iterate hemispheres (``for side in ("left",
  "right")``) rather than importing both — this keeps the import graph a tree,
  not a diamond.

Usage
-----
Resolve by path (preferred)::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal \
        import brodmann_areas, cortex, gyri, sulci

    s1_r  = cortex.primary_somatosensory_cortex   # left hemibody
    ppc_r = cortex.posterior_parietal_cortex      # right-dominant spatial network

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.cortex.posterior_parietal_cortex"
    )

References
----------
* Terminologia Anatomica (FIPAT, 2019) — A14.1.09.001 (lobus parietalis)
* NeuroNames 93 — Parietal lobe (laterality = right)
* Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
* Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
* Van Essen, D.C. et al. (2012). *Cereb Cortex* 22(10):2225–2246 — cortical
  asymmetries.
* Goldberg, E. et al. (2013). *The New Executive Brain* — right-hemisphere
  dominance for spatial attention.
"""