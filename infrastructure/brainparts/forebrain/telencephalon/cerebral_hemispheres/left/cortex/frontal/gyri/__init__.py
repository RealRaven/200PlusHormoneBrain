"""
Frontal Lobe Gyri — Left Hemisphere
====================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── frontal
                              └── gyri          ← THIS PACKAGE

The **gyri** (singular: gyrus) are the convex folds of the left frontal
lobe. They are separated from one another by the frontal *sulci* (see
sibling package ``..sulci``). In this architecture the gyri layer is the
**spatial scaffold** — it answers *"where on the folded cortical sheet
does a computation live?"* — while the sibling ``..brodmann_areas`` and
``..cortex`` packages answer *"what computation is it?"* and *"which
functional network does it belong to?"*.

Direct children (3)
-------------------
::

    gyri
    ├── inferior_frontal_gyrus   [language production, inhibition, semantics]
    ├── middle_frontal_gyrus     [working memory, attention, cognitive control]
    └── superior_frontal_gyrus   [executive function, metacognition, motor planning]

Lateralization note
-------------------
This is the **left** hemisphere. In the overwhelming majority of right-
handers (and ~70 % of left-handers) the left frontal lobe is dominant
for:

* **speech production** — Broca's area lives in the inferior frontal gyrus
  (pars opercularis + triangularis)
* **praxis / skilled motor sequencing** — premotor and SMA on the superior
  frontal gyrus
* **sequential / analytical reasoning** — DLPFC on the middle frontal gyrus
* **verbal working memory** — phonological loop components of MFG/SFG

Right-hemisphere homologues (see ``../../right/...``) will carry the
complementary specializations (prosody, visuospatial attention, holistic
semantics, emotional inhibition).

--------------------------------------------------------------------------------
DIRECT CHILDREN — NEUROANATOMICAL & FUNCTIONAL SPEC
--------------------------------------------------------------------------------

1. inferior_frontal_gyrus
   ~~~~~~~~~~~~~~~~~~~~~~
   The ventral-most frontal gyrus. Composed of three *pars*:

       pars orbitalis        (BA 47)   [semantic retrieval, reward-guided choice]
       pars triangularis     (BA 45)   [syntactic processing, semantic control]
       pars opercularis      (BA 44)   [phonological/speech-motor output]

   ``BA 44 + 45 = Broca's area`` (left hemisphere dominant).
   Right-hemisphere homologue supports emotional prosody and response
   inhibition.

   Key long-range connections:
       • arcuate fasciculus          → posterior superior temporal gyrus
       • uncinate fasciculus         → anterior temporal lobe
       • frontal aslant tract        → supplementary motor area
       • inferior longitudinal fasc. → occipitotemporal cortex

   Computational role in this architecture:
       [language production bus, response inhibition gate,
        semantic working-memory buffer, mirror-observation channel]

2. middle_frontal_gyrus
   ~~~~~~~~~~~~~~~~~~~~~
   The intermediate frontal gyrus, largely coextensive with the
   **dorsolateral prefrontal cortex (DLPFC)**:

       BA 9  (dorsal MFG)     [rule maintenance, task-set]
       BA 46 (mid-DLPFC)      [spatial & verbal working memory]
       BA 8  (caudal MFG)     [frontal eye fields — saccade planning]

   Computational role:
       [working-memory register, attentional gain controller,
        set-shifting / rule-switching engine, prospective-memory slot]

   Key long-range connections:
       • SLF I / II / III    → parietal & temporal association cortex
       • fronto-striatal loop → caudate (cognitive-associative territory)
       • corpus callosum     → homotopic right MFG

3. superior_frontal_gyrus
   ~~~~~~~~~~~~~~~~~~~~~~~
   The dorsal-most frontal gyrus. Spans several functionally distinct
   zones:

       BA 6  (medial SFG)   supplementary & pre-supplementary motor area
       BA 8  (caudal SFG)   frontal eye fields (shared with MFG)
       BA 9  (dorsal SFG)   executive control
       BA 10 (frontopolar)  cognitive branching, prospective memory,
                            metacognition, theory-of-mind (medial aspect)
       BA 32/24 (medial)    anterior cingulate / conflict monitoring

   Computational role:
       [executive scheduler, metacognitive monitor,
        motor-sequence planner, self-referential / ToM integrator,
        conflict & error monitor]

   Key long-range connections:
       • cingulum bundle      → posterior cingulate / parahippocampal
       • frontal aslant tract → Broca's area / IFG
       • thalamo-cortical     → mediodorsal & VA/VL nuclei
       • corpus callosum      → homotopic right SFG

--------------------------------------------------------------------------------
CROSS-REFERENCES (sibling modules under ``frontal/``)
--------------------------------------------------------------------------------

..sulci
    The negative space between these gyri. Every gyrus boundary in
    this package must be mirrored by a sulcus entry in ``..sulci``:
        inferior_frontal_sulcus  separates IFG from MFG
        superior_frontal_sulcus  separates MFG from SFG
        precentral_sulcus        separates SFG from precentral gyrus
        olfactory_sulcus         bounds IFG orbitally

..brodmann_areas
    Cytoarchitectonic map. Each gyrus *contains* one or more Brodmann
    areas. The mapping is many-to-one (gyrus → areas) and must be
    declared in each child's ``BRODMANN_AREAS`` constant.

..cortex
    Functional network decomposition (prefrontal_cortex, premotor_cortex,
    primary_motor_cortex, supplementary_motor_cortex). A single gyrus
    can contribute to multiple functional networks — e.g. MFG supplies
    both ``prefrontal_cortex`` and ``premotor_cortex``.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT FOR EACH CHILD PACKAGE
--------------------------------------------------------------------------------

Every child gyrus package (e.g. ``inferior_frontal_gyrus/__init__.py``)
MUST expose the following module-level names so the rest of the system
can query it uniformly:

    GYRUS_NAME : str
        Canonical snake_case name, identical to the folder name.
        Example: "inferior_frontal_gyrus"

    HEMISPHERE : str
        "left" (this branch) or "right" (the sibling branch).

    LOBE : str
        "frontal"

    BRODMANN_AREAS : tuple[int, ...]
        Sorted tuple of Brodmann area numbers contained in this gyrus.
        Example: (44, 45, 47) for IFG.

    PARS : dict[str, tuple[int, ...]]
        Sub-parcellation mapping *pars name* → Brodmann areas it covers.
        Example: {"pars_opercularis": (44,),
                  "pars_triangularis": (45,),
                  "pars_orbitalis":   (47,)}
        Use an empty dict if the gyrus has no classic parcellation.

    FUNCTIONAL_ROLES : tuple[str, ...]
        Free-form tags matching the bracketed annotations above.
        Example: ("language_production", "response_inhibition",
                  "semantic_control", "mirror_observation")

    CONNECTIVITY : dict[str, tuple[str, ...]]
        White-matter bundle → tuple of target regions.
        Example: {"arcuate_fasciculus": ("superior_temporal_gyrus",),
                  "uncinate_fasciculus": ("anterior_temporal_lobe",)}

    HORMONE_RECEPTORS : dict[str, tuple[str, ...]]
        Hormone / neuromodulator → tuple of receptor families expressed
        in this gyrus. This is the hook into the ``chemicals_hormones``
        package. Example for IFG:
            {"dopamine":   ("D1", "D2"),
             "estrogen":   ("ER-alpha", "ER-beta"),
             "testosterone": ("AR",),
             "oxytocin":   ("OXTR",)}

    SUBDIVISIONS : tuple[str, ...]
        Names of any nested sub-packages (e.g. IFG currently has none,
        but if you later split ``pars_opercularis`` into its own package
        it must be listed here).

    __all__ : list[str]
        Must include every public name above so that
        ``from ...gyri import inferior_frontal_gyrus`` works and
        ``inferior_frontal_gyrus.GYRUS_NAME`` resolves.

The child's ``__init__.py`` should additionally contain a docstring
following the SAME template used here: hierarchical location →
direct children (if any) → lateralization note → cross-references →
contract reminder.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``gyri/__init__.py`` is a pure namespace + registry. It must:

1. Import the three child packages (no side effects):
       from . import inferior_frontal_gyrus
       from . import middle_frontal_gyrus
       from . import superior_frontal_gyrus

2. Expose a machine-readable registry so the memory system, the
   hormone engine, and the UI can iterate over gyri without hard-coding:

       GYRI = {
           "inferior_frontal_gyrus": inferior_frontal_gyrus,
           "middle_frontal_gyrus":   middle_frontal_gyrus,
           "superior_frontal_gyrus": superior_frontal_gyrus,
       }

3. Expose a flat Brodmann-area index for quick lookup:

       BRODMANN_TO_GYRUS = {
           44: "inferior_frontal_gyrus",
           45: "inferior_frontal_gyrus",
           47: "inferior_frontal_gyrus",
            6: "superior_frontal_gyrus",
            8: "middle_frontal_gyrus",   # FEF — shared with SFG
            9: "middle_frontal_gyrus",   # dorsal MFG
           10: "superior_frontal_gyrus",
           24: "superior_frontal_gyrus",
           32: "superior_frontal_gyrus",
           46: "middle_frontal_gyrus",
       }

4. Define ``__all__ = ["inferior_frontal_gyrus",
                        "middle_frontal_gyrus",
                        "superior_frontal_gyrus",
                        "GYRI", "BRODMANN_TO_GYRUS"]``

5. Contain **no** logic beyond the above. Any behaviour belongs in
   ``cortex/`` or in the ``memory/`` layer.

--------------------------------------------------------------------------------
CHECKLIST BEFORE MOVING TO THE NEXT PACKAGE
--------------------------------------------------------------------------------

[ ] Three child packages exist and each has its own __init__.py with the
    full contract (GYRUS_NAME … __all__).
[ ] Every Brodmann area listed in BRODMANN_TO_GYRUS actually appears in
    some child's BRODMANN_AREAS.
[ ] Every sulcus named in the cross-reference section has a matching
    sibling package under ..sulci.
[ ] Every functional role tag used in the docstring also appears in the
    child's FUNCTIONAL_ROLES tuple.
[ ] HORMONE_RECEPTORS keys are a subset of the 12 families in
    infrastructure/chemicals_hormones/ (hpg, hpa, metabolic, satiety,
    neuro_modulators, social, fluid, immune, structural, circadian,
    xenobiotic, gasotransmitters).
"""