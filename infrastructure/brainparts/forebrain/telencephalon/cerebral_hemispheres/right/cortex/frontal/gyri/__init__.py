"""
Frontal Lobe Gyri — Right Hemisphere
=====================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── frontal
                              └── gyri          ← THIS PACKAGE

The **gyri** (singular: gyrus) are the convex folds of the right frontal
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
    ├── inferior_frontal_gyrus   [prosody, inhibition, coherence, humor]
    ├── middle_frontal_gyrus     [visuospatial WM, vigilance, spatial attention]
    └── superior_frontal_gyrus   [limb motor planning, mentalizing, branching]

Lateralization note
-------------------
This is the **right** hemisphere. The right frontal lobe is the mirror-
image cytoarchitectonic homologue of the left, but is **functionally
lateralized** for a complementary set of operations. In the majority of
right-handers the right frontal lobe is dominant for:

* **affective prosody** — production and perception of intonation,
  stress, and emotional tone (damage ⇒ *aprosodia*); supported by the
  right inferior frontal gyrus, the homologue of Broca's area
* **response inhibition under high conflict** — right IFG / pre-SMA
  network, especially in go/no-go and stop-signal tasks
* **discourse coherence and non-literal language** — sarcasm, irony,
  metaphor, humor appreciation, and narrative-level inference (right
  IFG and frontopolar cortex)
* **visuospatial working memory and spatial attention** — right MFG
  (DLPFC homologue) and right SFG (FEF homologue); lesion ⇒ left
  hemispatial neglect
* **sustained attention / vigilance** — right-lateralized fronto-
  parietal network; right MFG is a core node
* **mentalizing / theory of mind** — right SFG (BA 10) and medial
  frontopolar cortex contribute to perspective-taking, though ToM is
  largely bilateral with left-dominant verbal components
* **contralateral (left-limb) motor planning** — right precentral,
  premotor, and SMA regions (BAs 4, 6) drive the left arm and hand

Left-hemisphere homologues (see ``../../left/...``) carry the
complementary specializations (speech production, syntactic processing,
verbal working memory, sequential/analytical reasoning, right-limb motor
planning).

--------------------------------------------------------------------------------
DIRECT CHILDREN — NEUROANATOMICAL & FUNCTIONAL SPEC
--------------------------------------------------------------------------------

1. inferior_frontal_gyrus
   ~~~~~~~~~~~~~~~~~~~~~~
   The ventral-most frontal gyrus. Composed of the same three *pars* as
   on the left, but functionally re-tuned:

       pars orbitalis        (BA 47)   [affective valuation, humor detection]
       pars triangularis     (BA 45)   [non-literal / figurative language]
       pars opercularis      (BA 44)   [prosodic-motor output, response inhibition]

   ``BA 44 + 45 = right Broca homologue`` — the *prosody* and *inhibition*
   counterpart of the left speech-production region. Damage to the right
   IFG produces aprosodia (flat, monotone speech) and disinhibited
   emotional reactions.

   Key long-range connections:
       • arcuate fasciculus (right)  → right posterior superior temporal gyrus
       • uncinate fasciculus (right) → right anterior temporal lobe
       • frontal aslant tract        → right supplementary motor area
       • inferior longitudinal fasc. → right occipitotemporal cortex

   Computational role in this architecture:
       [affective-prosody bus, response-inhibition gate,
        non-literal language decoder, humor / irony detector,
        discourse-coherence integrator]

2. middle_frontal_gyrus
   ~~~~~~~~~~~~~~~~~~~~~
   The intermediate frontal gyrus, largely coextensive with the
   **right dorsolateral prefrontal cortex (DLPFC)**:

       BA 9  (dorsal MFG)     [rule maintenance, task-set]
       BA 46 (mid-DLPFC)      [visuospatial working memory]
       BA 8  (caudal MFG)     [frontal eye fields — contralateral saccades]

   Right DLPFC is the dominant node for **visuospatial** as opposed to
   **verbal** working memory, and for **top-down spatial attention**.

   Computational role:
       [visuospatial-working-memory register, spatial attentional gain,
        vigilance / sustained-attention engine, set-shifting under
        spatial conflict, prospective-memory slot]

   Key long-range connections:
       • SLF I / II / III    → right parietal & temporal association cortex
       • fronto-striatal loop → right caudate (cognitive-associative)
       • corpus callosum     → homotopic left MFG

   Clinical anchor: right MFG / inferior parietal lesions cause **left
   hemispatial neglect**, the canonical right-lateralized attentional
   deficit.

3. superior_frontal_gyrus
   ~~~~~~~~~~~~~~~~~~~~~~~
   The dorsal-most frontal gyrus. Functionally re-tuned relative to the
   left:

       BA 6  (medial SFG)   supplementary & pre-supplementary motor area
                            — left-limb motor sequencing & bimanual
                            coordination
       BA 8  (caudal SFG)   frontal eye fields (contralateral saccades)
       BA 9  (dorsal SFG)   executive control (largely bilateral)
       BA 10 (frontopolar)  mentalizing / theory of mind, cognitive
                            branching, prospective memory
       BA 32/24 (medial)    anterior cingulate / conflict & error monitoring

   Computational role:
       [left-limb motor-sequence planner, metacognitive monitor,
        mentalizing / perspective-taking integrator,
        cognitive-branching scheduler, conflict & error monitor]

   Key long-range connections:
       • cingulum bundle      → posterior cingulate / parahippocampal
       • frontal aslant tract → right IFG (prosody homologue)
       • thalamo-cortical     → mediodorsal & VA/VL nuclei
       • corpus callosum      → homotopic left SFG

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
    declared in each child's ``BRODMANN_AREAS`` constant. The right
    hemisphere uses the SAME BA numbers as the left — Brodmann's map is
    numerically symmetric — but the functional annotations differ.

..cortex
    Functional network decomposition (prefrontal_cortex, premotor_cortex,
    primary_motor_cortex, supplementary_motor_cortex). A single gyrus
    can contribute to multiple functional networks — e.g. right MFG
    supplies both ``prefrontal_cortex`` and ``premotor_cortex``.

..__pycache__ note
    Cross-hemispheric symmetry contract: every child package here has a
    name-identical sibling under ``../../left/...``. Any change to
    ``BRODMANN_AREAS`` on one side must be mirrored on the other, even
    when ``FUNCTIONAL_ROLES`` and ``HORMONE_RECEPTORS`` legitimately
    differ.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT FOR EACH CHILD PACKAGE
--------------------------------------------------------------------------------

Every child gyrus package (e.g. ``inferior_frontal_gyrus/__init__.py``)
MUST expose the following module-level names so the rest of the system
can query it uniformly:

    GYRUS_NAME : str
        Canonical snake_case name, identical to the folder name AND to
        the left-hemisphere sibling. Example: "inferior_frontal_gyrus"

    HEMISPHERE : str
        "right" (this branch) or "left" (the sibling branch).

    LOBE : str
        "frontal"

    BRODMANN_AREAS : tuple[int, ...]
        Sorted tuple of Brodmann area numbers contained in this gyrus.
        MUST equal the left-hemisphere sibling's tuple (Brodmann's map
        is symmetric). Example: (44, 45, 47) for IFG.

    PARS : dict[str, tuple[int, ...]]
        Sub-parcellation mapping *pars name* → Brodmann areas it covers.
        MUST have identical keys to the left sibling; values may be
        identical because BA numbering is symmetric.
        Example: {"pars_opercularis": (44,),
                  "pars_triangularis": (45,),
                  "pars_orbitalis":   (47,)}
        Use an empty dict if the gyrus has no classic parcellation.

    FUNCTIONAL_ROLES : tuple[str, ...]
        Free-form tags matching the bracketed annotations above. These
        are EXPECTED to differ from the left sibling — that is the whole
        point of the hemisphere split.
        Example for right IFG: ("affective_prosody", "response_inhibition",
                  "non_literal_language", "humor_detection",
                  "discourse_coherence")

    CONNECTIVITY : dict[str, tuple[str, ...]]
        White-matter bundle → tuple of target regions. Same bundle names
        as the left sibling, but target regions are on the right.
        Example: {"arcuate_fasciculus": ("superior_temporal_gyrus",),
                  "uncinate_fasciculus": ("anterior_temporal_lobe",)}

    HORMONE_RECEPTORS : dict[str, tuple[str, ...]]
        Hormone / neuromodulator → tuple of receptor families expressed
        in this gyrus. This is the hook into the ``chemicals_hormones``
        package. Right-hemisphere receptor densities differ subtly from
        the left (e.g. right IFG shows stronger noradrenergic and
        oxytocinergic modulation relevant to prosody and social
        cognition). Example for right IFG:
            {"dopamine":     ("D1", "D2"),
             "noradrenaline": ("alpha-1", "alpha-2", "beta"),
             "oxytocin":     ("OXTR",),
             "testosterone": ("AR",),
             "estrogen":     ("ER-alpha", "ER-beta")}

    SUBDIVISIONS : tuple[str, ...]
        Names of any nested sub-packages. Must mirror the left sibling's
        structure exactly.

    __all__ : list[str]
        Must include every public name above so that
        ``from ...gyri import inferior_frontal_gyrus`` works and
        ``inferior_frontal_gyrus.HEMISPHERE`` resolves to ``"right"``.

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
   hormone engine, and the UI can iterate over right gyri:

       GYRI = {
           "inferior_frontal_gyrus": inferior_frontal_gyrus,
           "middle_frontal_gyrus":   middle_frontal_gyrus,
           "superior_frontal_gyrus": superior_frontal_gyrus,
       }

3. Expose a flat Brodmann-area index. Because Brodmann numbering is
   hemisphere-symmetric, this dictionary must contain the SAME keys as
   the left-hemisphere ``BRODMANN_TO_GYRUS``. The *values* (gyrus names)
   are also the same — the hemisphere is disambiguated by the module
   path, not by the index:

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
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

This package is the structural mirror of ``../../left/cortex/frontal/gyri``.
The following invariants MUST hold and should be asserted by a
cross-hemisphere test in ``tests/``:

  * Child package names are identical left ↔ right.
  * ``BRODMANN_AREAS`` tuples are identical left ↔ right.
  * ``PARS`` keys are identical left ↔ right (values may be identical
    too, since BA numbers are symmetric).
  * ``CONNECTIVITY`` bundle names are identical left ↔ right; targets
    are the right-hemisphere equivalents.
  * ``FUNCTIONAL_ROLES`` and ``HORMONE_RECEPTORS`` are EXPECTED to
    differ — the whole architecture exists to model the asymmetry.
  * ``SUBDIVISIONS`` trees are structurally isomorphic.

Any deviation is a bug, not a feature, unless documented in the child
package's docstring with a citation.

--------------------------------------------------------------------------------
CHECKLIST BEFORE MOVING TO THE NEXT PACKAGE
--------------------------------------------------------------------------------

[ ] Three child packages exist and each has its own __init__.py with the
    full contract (GYRUS_NAME … __all__), and HEMISPHERE == "right".
[ ] Every child package name matches its left-hemisphere sibling.
[ ] Every BRODMANN_AREAS tuple matches its left-hemisphere sibling.
[ ] Every Brodmann area listed in BRODMANN_TO_GYRUS actually appears in
    some child's BRODMANN_AREAS.
[ ] Every sulcus named in the cross-reference section has a matching
    sibling package under ..sulci.
[ ] Every functional role tag used in the docstring also appears in the
    child's FUNCTIONAL_ROLES tuple, and each role has been sanity-checked
    against the right-hemisphere lateralization literature (prosody,
    vigilance, visuospatial WM, inhibition, mentalizing, left-limb motor).
[ ] HORMONE_RECEPTORS keys are a subset of the 12 families in
    infrastructure/chemicals_hormones/ (hpg, hpa, metabolic, satiety,
    neuro_modulators, social, fluid, immune, structural, circadian,
    xenobiotic, gasotransmitters).
[ ] A cross-hemisphere symmetry test exists and passes.
"""