"""
Frontal Lobe Sulci — Left Hemisphere
=====================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── frontal
                              └── sulci          ← THIS PACKAGE

The **sulci** (singular: sulcus) are the **negative space** of the
folded cortical sheet — the grooves and fissures that separate one gyrus
from another. In this architecture the sulci layer is the **boundary
scaffold**: it answers *"what separates gyrus X from gyrus Y?"* — while
the sibling ``..gyri`` package answers *"where does the computation
live?"*.

The relationship is strictly **dual**:

    every sulcus entry names the two (or three) gyri it separates
    every gyrus boundary is mirrored by a sulcus entry

There is no sulcus without a pair of gyri, and no pair of adjacent gyri
without a sulcus between them. If you add a sulcus, you are asserting
that two gyri are now separated — update ``..gyri`` accordingly. If you
add a gyrus, you are asserting that at least one new boundary exists —
update this package accordingly. The symmetry test in ``tests/`` will
check this.

Direct children (6)
-------------------
::

    sulci
    ├── inferior_frontal_sulcus   [IFG ↔ MFG]
    ├── olfactory_sulcus          [IFG ↔ orbital surface]
    ├── orbital_sulcus            [orbital gyri boundaries]
    ├── paracentral_sulcus        [SFG ↔ paracentral lobule (medial)]
    ├── precentral_sulcus         [MFG/SFG ↔ precentral gyrus]
    └── superior_frontal_sulcus   [MFG ↔ SFG]

Lateralization note
-------------------
This is the **left** hemisphere. The sulcal *pattern* of the left frontal
lobe is largely symmetric with the right, but the sulci are **shallower
and less variable** on the left in most individuals — the right frontal
operculum, in particular, is often deeper and more complex. The left
lateral fissure (Sylvian) ascends more steeply at its posterior end,
which subtly changes the angle at which the inferior frontal sulcus meets
the precentral sulcus. None of this changes the *names* or *bounding
relationships* — the six sulci in this package exist on both sides with
the same names, the same bounding gyri, and the same Brodmann-area
adjacencies. Only the geometric descriptors (depth, angle, variability)
differ, and those are recorded in each child's docstring, not here.

--------------------------------------------------------------------------------
DIRECT CHILDREN — ANATOMICAL & BOUNDARY SPEC
--------------------------------------------------------------------------------

1. inferior_frontal_sulcus
   ~~~~~~~~~~~~~~~~~~~~~~~~
   The horizontal sulcus running caudo-rostrally **between the inferior
   frontal gyrus (ventral) and the middle frontal gyrus (dorsal)**.

   Bounding gyri:
       ventral  → inferior_frontal_gyrus
       dorsal   → middle_frontal_gyrus

   Caudal end:  meets the inferior precentral sulcus (the inferior
                continuation of the precentral sulcus).
   Rostral end: terminates in the pars triangularis / pars orbitalis
                region of the IFG.

   Brodmann adjacency (the areas it separates):
       ventrally  BA 44, BA 45, BA 47  (IFG)
       dorsally   BA 6, BA 8, BA 9, BA 46  (MFG)

   Clinical significance:
       The inferior frontal sulcus is a landmark for the **frontal
       operculum** — the cortex that overhangs the insula. Its depth
       and continuity vary across individuals; in ~20 % of brains it
       is interrupted by a transverse gyrus connecting IFG and MFG
       (the *transverse frontal gyrus*), which is a normal variant.

   Cross-reference: ``..gyri.inferior_frontal_gyrus`` and
   ``..gyri.middle_frontal_gyrus`` both declare this sulcus as one of
   their boundaries.

2. olfactory_sulcus
   ~~~~~~~~~~~~~~~~~
   The shallow sulcus on the **orbital surface** of the frontal lobe,
   running longitudinally and bounding the **olfactory tract** laterally.

   Bounding gyri:
       medial   → gyrus rectus / medial orbital gyrus
       lateral  → orbital part of the inferior frontal gyrus
                  (pars orbitalis, BA 47)

   The olfactory bulb and tract lie *within* this sulcus in life; the
   sulcus is the anatomical groove that houses them. It separates the
   medial orbital surface from the lateral orbital surface.

   Brodmann adjacency:
       medially   BA 11, BA 12  (orbitofrontal / gyrus rectus)
       laterally  BA 47  (pars orbitalis of IFG)

   Clinical significance:
       The olfactory sulcus is the landmark for the **olfactory
       tract**, and its depth predicts olfactory bulb volume. In
       Parkinson's disease and in Alzheimer's disease the olfactory
       sulcus is among the earliest-affected cortical landmarks
       (olfactory dysfunction is a prodromal sign of both).

   Cross-reference: ``..gyri.inferior_frontal_gyrus`` declares this
   sulcus as its ventral-orbital boundary. The medial orbital gyri
   are not yet modelled as a gyrus package; when they are, they must
   declare this sulcus as their lateral boundary.

3. orbital_sulcus
   ~~~~~~~~~~~~~~~
   The family of shallow sulci on the **orbital surface** of the
   frontal lobe — the orbital sulci form an **H-shape** (or, in some
   individuals, an X-shape or a single transverse groove) that
   parcellates the orbital surface into the medial, lateral,
   anterior, and posterior orbital gyri.

   Bounding gyri (multiple — this is a compound sulcus):
       medial orbital gyrus   ↔  anterior orbital gyrus
       anterior orbital gyrus ↔  lateral orbital gyrus
       lateral orbital gyrus  ↔  posterior orbital gyrus
       (and the medial orbital gyrus ↔ gyrus rectus boundary, in
        some parcellations)

   Brodmann adjacency:
       BA 11, BA 12, BA 13, BA 14, BA 47  (orbitofrontal cortex
       subdivisions)

   Clinical significance:
       The orbital sulci are the anatomical substrate of the
       **orbitofrontal cortex's** functional parcellation. The
       medial orbital gyrus is more engaged in reward valuation;
       the lateral orbital gyrus in punishment / reversal learning;
       the anterior orbital gyrus in olfaction; the posterior
       orbital gyrus in visceral / autonomic integration. None of
       these orbital gyri are yet modelled as separate gyrus
       packages, but the orbital sulcus package must anticipate
       them.

   Cross-reference: ``..gyri.inferior_frontal_gyrus`` (pars
   orbitalis) declares the lateral orbital sulcus as one of its
   boundaries. When orbital gyri packages are added, they must
   declare this sulcus as their mutual boundary.

4. paracentral_sulcus
   ~~~~~~~~~~~~~~~~~~~
   The short sulcus on the **medial surface** of the hemisphere,
   running dorsoventrally just **caudal to the paracentral lobule**
   and **rostral to the marginal sulcus** (which itself separates
   the paracentral lobule from the precuneus).

   Bounding gyri:
       rostral  → superior_frontal_gyrus (medial aspect, BA 6)
       caudal   → paracentral lobule (which is the medial
                  continuation of the pre- and postcentral gyri,
                  BA 4 + BA 3 + BA 1 + BA 2 + BA 5)

   The paracentral sulcus therefore marks the **medial boundary
   between the frontal motor strip (SFG's medial BA 6 / SMA) and
   the paracentral lobule** — the medial continuation of the
   primary sensorimotor cortex that represents the contralateral
   leg and foot.

   Brodmann adjacency:
       rostrally  BA 6  (SMA / pre-SMA)
       caudally   BA 4, BA 3, BA 1, BA 2  (paracentral lobule,
                  medial primary sensorimotor strip)

   Clinical significance:
       The paracentral lobule is the medial cortical representation
       of the contralateral leg and foot. The paracentral sulcus
       is the rostral boundary of that representation. Damage to the
       paracentral lobule produces contralateral leg weakness /
       sensory loss; the sulcus itself is a landmark for
       localizing medial frontal lesions.

   Cross-reference: ``..gyri.superior_frontal_gyrus`` declares this
   sulcus as its caudal-medial boundary. The paracentral lobule is
   currently modelled implicitly (as the medial continuation of
   pre- and postcentral gyri) rather than as a separate gyrus
   package; when it becomes one, it must declare the paracentral
   sulcus as its rostral boundary.

5. precentral_sulcus
   ~~~~~~~~~~~~~~~~~~
   The long, prominent sulcus running dorsoventrally along the
   **posterior margin of the frontal lobe**, separating the frontal
   gyri from the precentral gyrus (the primary motor cortex, BA 4).

   Bounding gyri:
       rostral  → middle_frontal_gyrus (dorsal portion of the
                  sulcus) AND superior_frontal_gyrus (most-dorsal
                  portion, where the sulcus turns medially)
       caudal   → precentral gyrus (BA 4, primary motor cortex) —
                  **not a frontal gyrus**; it is the most-posterior
                  frontal-lobe fold and is the anatomical substrate
                  of BA 4

   In the current architecture, the precentral gyrus is modelled as
   a child of ``..gyri`` in some parcellations (as ``precentral_gyrus``
   under ``primary_motor_cortex``) and as a direct child of
   ``cortex.frontal`` in others. Whichever convention is adopted, the
   precentral sulcus MUST be the sulcus that separates it from the
   MFG and SFG.

   In many brains the precentral sulcus is interrupted by a
   *transverse precentral sulcus* or by the superior / inferior
   precentral sulci proper, and it often joins the superior frontal
   sulcus at its dorsal end.

   Brodmann adjacency:
       rostrally  BA 6, BA 8, BA 9, BA 46  (premotor / DLPFC)
       caudally   BA 4  (primary motor cortex)

   Clinical significance:
       The precentral sulcus is the **surgical and functional
       landmark** for the primary motor cortex. In awake craniotomy
       it is used to localize M1 by direct electrical stimulation —
       stimulation just caudal to the sulcus produces contralateral
       movement; stimulation just rostral (in premotor cortex) does
       not, unless the current is increased. The sulcus is also a
       landmark for the **frontal eye fields** (which sit at its
       dorsal junction with the superior frontal sulcus) and for
       the **Broca's area homologue** at its ventral junction with
       the inferior frontal sulcus.

   Cross-reference: ``..gyri.middle_frontal_gyrus`` and
   ``..gyri.superior_frontal_gyrus`` both declare this sulcus as
   their caudal boundary. ``cortex.primary_motor_cortex`` must
   declare this sulcus as its rostral boundary.

6. superior_frontal_sulcus
   ~~~~~~~~~~~~~~~~~~~~~~~~
   The long horizontal sulcus running caudo-rostrally **between the
   middle frontal gyrus (ventral) and the superior frontal gyrus
   (dorsal)**.

   Bounding gyri:
       ventral  → middle_frontal_gyrus
       dorsal   → superior_frontal_gyrus

   Caudal end:  joins the precentral sulcus (or the superior
                precentral sulcus) at the dorsal frontal convexity.
   Rostral end: terminates in the frontopolar region, often
                meeting the superior frontal ramus of the lateral
                fissure or simply fading into the frontal pole.

   Brodmann adjacency:
       ventrally  BA 8, BA 9, BA 46  (MFG — DLPFC / FEF)
       dorsally   BA 6, BA 8, BA 9, BA 10  (SFG — SMA, pre-SMA,
                  dorsal DLPFC, frontopolar)

   Clinical significance:
       The superior frontal sulcus is the **dorsal boundary of the
       DLPFC** and the landmark for the **dorsal attention network**
       on the frontal convexity. The FEF sits at the junction of the
       superior frontal sulcus and the precentral sulcus — this
       junction is the single most reliable surface landmark for
       the FEF. The sulcus is also a landmark for the **SMA / pre-SMA
       border** on the medial surface, where it turns over the
       dorsal edge of the hemisphere.

   Cross-reference: ``..gyri.middle_frontal_gyrus`` and
   ``..gyri.superior_frontal_gyrus`` both declare this sulcus as one
   of their boundaries.

--------------------------------------------------------------------------------
CROSS-REFERENCES (sibling modules under ``frontal/``)
--------------------------------------------------------------------------------

..gyri
    The **positive space** of the frontal lobe. Every sulcus here
    bounds two or more gyri there; the two packages must remain in
    dual lock-step:

        inferior_frontal_sulcus   → IFG ↔ MFG
        olfactory_sulcus          → IFG/orbital ↔ medial orbital
        orbital_sulcus            → orbital gyri (compound)
        paracentral_sulcus        → SFG ↔ paracentral lobule
        precentral_sulcus         → MFG/SFG ↔ precentral gyrus
        superior_frontal_sulcus   → MFG ↔ SFG

    The ``..gyri`` package's docstrings already declare these
    boundaries from the gyrus side. This package declares them from
    the sulcus side. The symmetry test asserts that the two
    declarations are exact inverses of each other.

..brodmann_areas
    Every sulcus separates two or more Brodmann areas. The mapping
    is **many-to-many** (a sulcus separates multiple area pairs),
    and must be declared per-sulcus in each child's
    ``BRODMANN_ADJACENCY`` constant. The parent index must NOT
    attempt to invert this into a single-valued map — sulci and BA
    areas are genuinely many-to-many.

..cortex
    The functional network decomposition (prefrontal_cortex,
    premotor_cortex, primary_motor_cortex, supplementary_motor_cortex)
    is **sulcus-agnostic** — functional networks cross sulcal
    boundaries freely. A single functional network may span
    multiple gyri separated by multiple sulci; a single sulcus may
    separate multiple functional networks. The sulci package must
    NOT try to encode functional boundaries — only anatomical
    boundaries.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT FOR EACH CHILD PACKAGE
--------------------------------------------------------------------------------

Every child sulcus package (e.g. ``inferior_frontal_sulcus/__init__.py``)
MUST expose the following module-level names:

    SULCUS_NAME : str
        Canonical snake_case name, identical to the folder name.
        Example: "inferior_frontal_sulcus"

    HEMISPHERE : str
        "left" (this branch) or "right" (the sibling branch).

    LOBE : str
        "frontal"

    BOUNDING_GYRI : dict[str, tuple[str, ...]]
        Direction → tuple of gyrus names it bounds in that direction.
        A sulcus has at least two entries (one per side); compound
        sulci (orbital_sulcus) may have more.

        Example for inferior_frontal_sulcus:
            {"ventral": ("inferior_frontal_gyrus",),
             "dorsal":  ("middle_frontal_gyrus",)}

        Example for orbital_sulcus (compound):
            {"medial_anterior":   ("medial_orbital_gyrus",
                                   "anterior_orbital_gyrus"),
             "anterior_lateral":  ("anterior_orbital_gyrus",
                                   "lateral_orbital_gyrus"),
             "lateral_posterior": ("lateral_orbital_gyrus",
                                   "posterior_orbital_gyrus")}

    BRODMANN_ADJACENCY : dict[str, tuple[int, ...]]
        Side → tuple of Brodmann areas abutting the sulcus on that
        side. Mirrors BOUNDING_GYRI but in BA space.

        Example for inferior_frontal_sulcus:
            {"ventral": (44, 45, 47),
             "dorsal":  (6, 8, 9, 46)}

    EXTENT : dict[str, tuple[str, ...]]
        Landmarks at each end of the sulcus.
        Example for inferior_frontal_sulcus:
            {"caudal":  ("inferior_precentral_sulcus",
                         "precentral_sulcus"),
             "rostral": ("pars_triangularis", "pars_orbitalis")}
        Use an empty dict for short sulci with no defined endpoints
        (paracentral_sulcus may use an empty dict or name its two
        neighbouring sulci).

    VARIANTS : tuple[str, ...]
        Common anatomical variants and their approximate prevalence.
        Example for inferior_frontal_sulcus:
            ("transverse_frontal_gyrus_~20%",
             "continuous_branch_~60%",
             "interrupted_branch_~20%")

    CLINICAL_ANCHORS : tuple[str, ...]
        Free-form tags matching the clinical-significance notes above.
        Example for precentral_sulcus:
            ("m1_surgical_landmark",
             "fef_surface_landmark",
             "broca_homologue_landmark")

    CONNECTIVITY : dict[str, tuple[str, ...]]
        Optional. Sulci are not connective structures (they are
        grooves, not tracts), but they are **landmarks for tracts**.
        This field names the white-matter bundles that run *beneath*
        the sulcus in standard dissections.
        Example for inferior_frontal_sulcus:
            {"arcuate_fasciculus": ("caps_operculum",),
             "superior_longitudinal_fasciculus_III":
                 ("traverses_inferior_frontal_gyrus",)}
        Use an empty dict if no tract is canonically associated.

    SUBDIVISIONS : tuple[str, ...]
        Names of any nested sub-packages. Must be empty in the
        current tree (no sulcus has been subdivided). When a compound
        sulcus (orbital_sulcus) is eventually split into
        ``medial_orbital_sulcus / anterior_orbital_sulcus / ...``,
        the sub-package names go here.

    __all__ : list[str]
        Must include every public name above.

The child's ``__init__.py`` should additionally contain a docstring
following the SAME template used here: hierarchical location →
bounding gyri → Brodmann adjacency → extent → variants → clinical
significance → cross-references → contract reminder.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``sulci/__init__.py`` is a pure namespace + registry. It must:

1. Import the six child packages (no side effects):
       from . import inferior_frontal_sulcus
       from . import olfactory_sulcus
       from . import orbital_sulcus
       from . import paracentral_sulcus
       from . import precentral_sulcus
       from . import superior_frontal_sulcus

2. Expose a machine-readable registry:

       SULCI = {
           "inferior_frontal_sulcus":  inferior_frontal_sulcus,
           "olfactory_sulcus":         olfactory_sulcus,
           "orbital_sulcus":           orbital_sulcus,
           "paracentral_sulcus":       paracentral_sulcus,
           "precentral_sulcus":        precentral_sulcus,
           "superior_frontal_sulcus":  superior_frontal_sulcus,
       }

3. Expose the **inverse index** — gyrus name → tuple of sulci that
   bound it. This must be derived from the children's
   ``BOUNDING_GYRI`` dicts, not hand-written, so it cannot drift:

       GYRUS_TO_SULCI = {
           # computed at import time by inverting BOUNDING_GYRI
           "inferior_frontal_gyrus": (
               "inferior_frontal_sulcus",
               "olfactory_sulcus",
               "precentral_sulcus",
           ),
           "middle_frontal_gyrus": (
               "inferior_frontal_sulcus",
               "superior_frontal_sulcus",
               "precentral_sulcus",
           ),
           "superior_frontal_gyrus": (
               "superior_frontal_sulcus",
               "precentral_sulcus",
               "paracentral_sulcus",
           ),
       }

   The inversion function must be defined in this file (no external
   helpers) and must fail loudly if any child's BOUNDING_GYRI names
   a gyrus that is not present in ``..gyri.GYRI``.

4. Expose a flat Brodmann-to-sulcus adjacency index, many-to-many:

       BRODMANN_TO_SULCI = {
           44: ("inferior_frontal_sulcus",),
           45: ("inferior_frontal_sulcus",),
           47: ("inferior_frontal_sulcus", "olfactory_sulcus"),
            6: ("superior_frontal_sulcus", "precentral_sulcus",
                "paracentral_sulcus"),
            8: ("superior_frontal_sulcus", "precentral_sulcus"),
            9: ("superior_frontal_sulcus", "precentral_sulcus"),
           10: ("superior_frontal_sulcus",),
           46: ("inferior_frontal_sulcus", "superior_frontal_sulcus",
                "precentral_sulcus"),
       }

   Like GYRUS_TO_SULCI, this must be derived from the children's
   BRODMANN_ADJACENCY dicts, not hand-written.

5. Define ``__all__ = list(SULCI) + ["GYRUS_TO_SULCI",
                                    "BRODMANN_TO_SULCI"]``

6. Contain **no** logic beyond the above. Any behaviour belongs in
   ``cortex/`` or in the ``memory/`` layer.

--------------------------------------------------------------------------------
DUALITY CONTRACT — SULCI ↔ GYRI
--------------------------------------------------------------------------------

This package and ``..gyri`` are **dual**. The following invariants MUST
hold and are asserted by a test in ``tests/``:

  * For every sulcus S in this package and every
    (direction, gyrus-tuple) pair in S.BOUNDING_GYRI, the gyrus G in
    that tuple MUST list S in its own boundary cross-references.
  * For every gyrus G in ``..gyri`` and every sulcus S named in G's
    boundary cross-references, S MUST appear in this package and MUST
    name G in its BOUNDING_GYRI.
  * Every gyrus named in any BOUNDING_GYRI MUST exist in
    ``..gyri.GYRI``.
  * Every Brodmann area in any BRODMANN_ADJACENCY MUST appear in some
    gyrus's BRODMANN_AREAS.

If any of these fails, the frontal lobe's spatial scaffold is
inconsistent and the architecture cannot locate a computation on the
folded sheet. This is a **blocking** test, not a warning.

--------------------------------------------------------------------------------
CHECKLIST BEFORE MOVING TO THE NEXT PACKAGE
--------------------------------------------------------------------------------

[ ] Six child packages exist, each with its own __init__.py exposing
    the full contract (SULCUS_NAME … __all__).
[ ] Every BOUNDING_GYRI names a gyrus that exists in
    ``..gyri.GYRI``.
[ ] Every named gyrus's docstring declares the sulcus back.
[ ] The inverted indices GYRUS_TO_SULCI and BRODMANN_TO_SULCI are
    computed, not hand-written, and are stable under import order.
[ ] The orbital_sulcus child correctly encodes its compound nature
    (multiple boundary pairs) rather than pretending to be a simple
    two-sided sulcus.
[ ] The paracentral_sulcus child's BOUNDING_GYRI correctly names
    ``superior_frontal_gyrus`` on its rostral side and the
    paracentral lobule on its caudal side — the latter may need a
    forward declaration until the paracentral lobule becomes a gyrus
    package.
[ ] The precentral_sulcus child's BOUNDING_GYRI correctly names
    ``middle_frontal_gyrus`` and ``superior_frontal_gyrus`` on its
    rostral side, and the precentral gyrus on its caudal side.
[ ] No functional-network information is stored here — sulci encode
    anatomical boundaries only; functional networks live in
    ``..cortex``.
[ ] The right-hemisphere mirror of this package declares the same six
    sulci with the same BOUNDING_GYRI and BRODMANN_ADJACENCY (these
    fields are hemisphere-invariant). Only the geometric descriptors
    (depth, variability, prevalence of variants) differ, and those
    live in each child's VARIANTS field, not in the parent.
"""