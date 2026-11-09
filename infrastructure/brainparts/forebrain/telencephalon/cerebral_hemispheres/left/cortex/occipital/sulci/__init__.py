"""
Occipital Sulci — Left Hemisphere
==================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── sulci          ← THIS PACKAGE

The **sulci** (singular: sulcus) are the **negative space** of the
folded cortical sheet — the grooves and fissures that separate one
gyrus from another and that mark the boundaries of the visual areas
on the medial and lateral surfaces of the occipital lobe. In this
architecture the sulci layer is the **boundary scaffold**: it
answers *"what separates gyrus X from gyrus Y?"* and *"which visual
area does this sulcus mark?"* — while the sibling ``..gyri``,
``..cuneus``, and ``..cortex`` packages answer *"where does the
computation live?"*.

The relationship is strictly **dual**:

    every sulcus entry names the two (or three) gyri it separates
    every gyrus boundary is mirrored by a sulcus entry

**The occipital sulci are unusual among the cortical lobes** in two
respects:

  (a) **The calcarine sulcus defines a primary sensory area** — its
      banks are the seat of V1 (the primary visual cortex), and the
      **stria of Gennari** is visible on the banks, making the V1 /
      V2 border **architectonically unambiguous**. No other sulcus
      in the cortex defines a primary sensory area with such a
      precise, histologically visible boundary.

  (b) **The calcarine sulcus's fundus represents a specific
      retinotopic meridian** — the **horizontal meridian** of the
      visual field is at the fundus of the calcarine sulcus. This is
      the **only sulcus in the cortex** whose depth carries a named
      retinotopic representation.

These two facts make the occipital sulci the **most functionally
load-bearing sulci in the cortex** — they are not merely anatomical
boundaries but **retinotopic landmarks** for the visual field.

Direct children (3)
-------------------
::

    sulci
    ├── calcarine_sulcus              [V1 banks; horizontal meridian]
    ├── lunate_sulcus                 [V1/V2 border, when present]
    └── transverse_occipital_sulcus   [lateral occipital gyri / parietal
                                       boundary; V3A/V3B territory]

**Only three of the classical occipital sulci are current children**
of this package. The others — the **parieto-occipital sulcus** (the
medial boundary with the parietal lobe) and the **lateral
occipitotemporal sulcus** (the ventral boundary with the temporal
lobe) — are **cross-lobe sulci** that may live under ``..parietal``
and ``..temporal`` rather than under this package. They are
**forward references** or **cross-package references** (see the
FORWARD-DECLARATION CAVEAT).

The **occipital polar region** at the caudal end of the occipital
lobe does **not** have a dedicated sulcus — the occipital pole is the
caudal convergence of the cuneus and lingual gyrus, and the
calcarine sulcus terminates in the occipital pole. There is no
"occipital polar sulcus" in the classical scheme.

--------------------------------------------------------------------------------
THE DUALITY CONTRACT — SULCI ↔ GYRI, WITH THREE SPECIAL CASES
--------------------------------------------------------------------------------

The occipital sulci package is **dual** to the occipital gyral
packages — ``..gyri`` (lateral occipital gyrus), ``..cuneus``
(medial-surface upper-bank landmark), and the lingual gyrus
(forward reference). But the occipital lobe has **three special
cases** that distinguish its duality from the frontal lobe's simpler
pattern:

**Special case 1: The calcarine sulcus bounds the cuneus and the
lingual gyrus, not two "standard" gyri.**

The calcarine sulcus separates:

    cuneus (upper bank) — a **parent-level gyral package** (a
                          surface landmark for V1's dorsal
                          representation of the lower field)
    lingual gyrus (lower bank) — a **forward reference** (a
                          medial-surface gyral package that has not
                          yet been promoted)

**Both banks of the calcarine sulcus are V1 territory.** This is the
only sulcus in the cortex whose **two banks are both primary sensory
cortex**, and it is the only sulcus whose banks are **both
retinotopically organized** (upper bank = lower field; lower bank =
upper field).

**Special case 2: The lunate sulcus is an inconstant sulcus that
only some brains have.**

The lunate sulcus is **present in roughly 40–60 % of human brains**
depending on the series. **When present**, it marks the **V1 / V2
border on the lateral surface** of the occipital lobe. **When
absent**, the V1 / V2 border must be inferred from the **retinotopic
retinotopic map** (the vertical meridian) rather than from a
surface sulcus.

**This is the only occipital sulcus whose presence is probabilistic**,
and the ``PRESENCE_PROBABILITY`` field must be carried by the lunate
sulcus child package (see ``..sulci/lunate_sulcus``).

**Special case 3: The transverse occipital sulcus is a dorsal
boundary, not an intra-occipital sulcus.**

The transverse occipital sulcus is **not** an intra-occipital sulcus
that separates two occipital gyri. It is the **dorsal boundary of
the lateral occipital gyri**, separating them from the parietal
lobe's angular gyrus. **It is a lobar boundary** on the lateral
surface (paralleling the parieto-occipital sulcus, which is the
lobar boundary on the medial surface).

**The transverse occipital sulcus's "duality" is therefore
different** — it bounds one occipital gyrus (lateral occipital
gyrus) on its ventral side and one **parietal** gyrus (angular
gyrus) on its dorsal side. The **parietal side of the duality**
must be declared in the ``..parietal/sulci`` package, not here.

**The duality contract therefore has three rules for the occipital
lobe:**

    Rule 1 (cuneus / lingual gyrus duality)
        The calcarine sulcus's two banks are both V1 territory, and
        both banks must be declared as **bounding gyri** by the
        calcarine sulcus package:
            cuneus (upper bank, parent-level gyral sibling)
            lingual gyrus (lower bank, forward reference)

    Rule 2 (lunate sulcus's conditional boundary)
        The lunate sulcus's V1 / V2 boundary is **conditional on
        its presence** — the sulcus package must carry a
        ``PRESENCE_PROBABILITY`` field, and the V1 / V2 border
        must be inferrable from retinotopy when the sulcus is
        absent.

    Rule 3 (lobar boundaries)
        The transverse occipital sulcus (dorsal) and the parieto-
        occipital sulcus (rostral-medial) are **lobar boundaries**,
        not intra-occipital sulci. The transverse occipital sulcus
        lives here (because its ventral bank is an occipital
        gyrus); the parieto-occipital sulcus lives in the
        ``..parietal`` or shared sulcal package (because its
        rostral bank is the precuneus, a parietal gyrus).

--------------------------------------------------------------------------------
DIRECT CHILDREN — ANATOMICAL & BOUNDARY SPEC
--------------------------------------------------------------------------------

1. calcarine_sulcus
   ~~~~~~~~~~~~~~~~~
   The **defining sulcus of the occipital lobe** — the horizontal
   sulcus on the **medial surface**, running caudo-rostrally from
   the **occipital pole** (caudally) to the **isthmus of the
   cingulate gyrus** / **parieto-occipital sulcus** (rostrally).

   **Bounding gyri:**
       upper bank     → **cuneus** (parent-level gyral sibling)
       lower bank     → **lingual gyrus** (forward reference)

   **Retinotopic role:**
       The **fundus** of the calcarine sulcus represents the
       **horizontal meridian** of the visual field. The **upper
       bank** carries the **dorsal V1 representation of the lower
       contralateral field** (**lower RIGHT** on the left side).
       The **lower bank** carries the **ventral V1 representation
       of the upper contralateral field** (**upper RIGHT** on the
       left side).

   **Architectonic signature:**
       The **stria of Gennari** is visible on both banks of the
       calcarine sulcus. The stria's **abrupt disappearance** at
       the V1 / V2 border is the architectonic basis of the
       architectonically unambiguous V1 / V2 boundary.

   **Clinical significance:**
       The calcarine sulcus is the **surface landmark for the
       calcarine cortex** — the V1 territory whose lesions
       produce **homonymous hemianopia** (right homonymous
       hemianopia for a left calcarine lesion).

   **Cross-reference:** ``..cuneus`` (upper-bank gyrus),
   ``..gyri`` (the lingual gyrus is a forward reference in
   ``..gyri``), ``..cortex/primary_visual_cortex`` (the V1
   functional area), and ``..brodmann_areas/brodmann_area_17``
   (the BA 17 cytoarchitectonic area).

2. lunate_sulcus
   ~~~~~~~~~~~~~~~
   The **inconstant lateral-surface sulcus** that, **when present**,
   marks the **V1 / V2 border** on the lateral surface of the
   occipital lobe.

   **Bounding gyri (when present):**
       rostral bank    → **V2 lateral territory** (the
                         extrastriate portion of the lateral
                         occipital gyrus)
       caudal bank     → **V1 lateral territory** (the lateral
                         portion of the calcarine cortex at the
                         occipital pole)

   **Retinotopic role:**
       The lunate sulcus, when present, marks the **vertical
       meridian** of the visual field — the V1 / V2 border. **When
       absent**, the V1 / V2 border must be inferred from the
       retinotopic map.

   **Presence probability:**
       **Present in roughly 40–60 % of human brains** depending on
       the series. The ``..sulci/lunate_sulcus`` child package
       must carry an explicit ``PRESENCE_PROBABILITY`` field.

   **Architectonic signature:**
       The V1 / V2 border is marked by the **abrupt disappearance
       of the stria of Gennari** at the lateral edge of the
       calcarine cortex. This architectonic signature is present
       on both banks of the lateral occipital sulcus when the
       lunate sulcus is present.

   **Clinical significance:**
       The lunate sulcus is a **secondary landmark** for the
       V1 / V2 border. Its primary clinical relevance is as a
       **retinotopic reference point** in mapping the visual
       field onto the lateral surface of the occipital lobe.

   **Cross-reference:** ``..gyri/lateral_occipital_gyrus`` (the
   lateral occipital gyrus contains the lateral V2 territory),
   ``..cortex/primary_visual_cortex`` (V1), and
   ``..cortex/v2`` (V2).

3. transverse_occipital_sulcus
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   The **dorsal-surface sulcus** that separates the **lateral
   occipital gyri** (ventrally) from the **parietal lobe's
   angular gyrus** (dorsally). It runs transversely across the
   lateral occipital convexity.

   **Bounding gyri:**
       ventral bank    → **lateral occipital gyrus** (occipital
                         gyral child of ``..gyri``)
       dorsal bank     → **angular gyrus** (parietal lobe)

   **Retinotopic role:**
       The transverse occipital sulcus is **not** a strict
       retinotopic landmark — it is a **lobar boundary** on the
       lateral surface. Its clinical significance is as the
       **dorsal boundary of the occipital lobe's lateral
       surface**.

   **Additional note:**
       The transverse occipital sulcus is **adjacent to the
       V3A / V3B territory** (forward references in
       ``..cortex``). V3A and V3B are the dorsal extrastriate
       areas that continue the dorsal motion pathway, and the
       transverse occipital sulcus is the surface landmark for
       their vicinity.

   **Cross-reference:** ``..gyri/lateral_occipital_gyrus`` (the
   ventral bounding gyrus), ``..cortex/v3a`` (forward reference),
   ``..cortex/v3b`` (forward reference), and the parietal lobe's
   ``..parietal/gyri`` package (the dorsal bounding gyrus, angular
   gyrus).

--------------------------------------------------------------------------------
FORWARD REFERENCES AND CROSS-PACKAGE REFERENCES
--------------------------------------------------------------------------------

**The parieto-occipital sulcus** is the **medial boundary between
the occipital and parietal lobes** — it separates the **cuneus**
(occipital) from the **precuneus** (parietal). **It is NOT a
current child of this package.** Its placement options are:

  (a) **Under ``..parietal/sulci``** — as a parietal boundary
      with the occipital lobe (because the precuneus is the
      parietal gyrus and the sulcus is the parietal lobe's
      caudal boundary).

  (b) **Under a shared ``..sulci`` parent** — if the tree adds a
      cortex-level ``..sulci`` package for inter-lobar sulci.

  (c) **Under this package** — as a medial boundary with the
      parietal lobe (because the cuneus, its caudal bank, is the
      occipital gyrus).

**The current tree leaves the placement open.** The
**calcarine sulcus** (this package's primary child) is **adjacent**
to the parieto-occipital sulcus at the **anterior calcarine
banks** — the two sulci meet at the isthmus of the cingulate gyrus
/ precuneus region. **When the parieto-occipital sulcus is added to
the tree, the calcarine sulcus package must cross-reference it as
the rostral neighbouring sulcus**, and the cuneus package must
cross-reference it as its **rostral bounding sulcus**.

**The lateral occipitotemporal sulcus** is the **ventral boundary
between the occipital and temporal lobes** — it separates the
**lateral occipital gyrus** (occipital) from the **fusiform gyrus**
(temporal). **It is NOT a current child of this package.** Its
placement options are the same as the parieto-occipital sulcus's:

  (a) **Under ``..temporal/sulci``** — as a temporal boundary with
      the occipital lobe.

  (b) **Under a shared ``..sulci`` parent**.

  (c) **Under this package** — as a lateral boundary with the
      temporal lobe (because the lateral occipital gyrus is the
      occipital gyrus).

**The current tree leaves the placement open.** When the lateral
occipitotemporal sulcus is added, the lateral occipital gyrus
package must cross-reference it as its **ventral bounding sulcus**,
and the fusiform gyrus package must cross-reference it as its
**dorsal bounding sulcus**.

**Both forward-reference sulci are byte-identical to the left
sibling's** — their placement questions are properties of the
occipital lobe's inter-lobar boundaries, not of the hemisphere.

--------------------------------------------------------------------------------
CROSS-REFERENCES (sibling modules under ``occipital/``)
--------------------------------------------------------------------------------

..gyri
    The **lateral-surface gyral parent**. The transverse occipital
    sulcus bounds the lateral occipital gyrus dorsally; the
    lunate sulcus, when present, crosses it. The ``..gyri``
    package cross-references the transverse occipital sulcus as
    its **dorsal boundary**.

..cuneus
    The **medial-surface upper-bank gyral landmark**. The
    calcarine sulcus bounds the cuneus caudally (the upper bank
    of the calcarine is the lower margin of the cuneus). The
    ``..cuneus`` package cross-references the calcarine sulcus
    as its **caudal bounding sulcus** and the parieto-occipital
    sulcus as its **rostral bounding sulcus**.

..brodmann_areas
    The **cytoarchitectonic sibling**. The calcarine sulcus is the
    surface landmark for **BA 17** (the primary visual cortex);
    the lunate sulcus, when present, marks the **BA 17 / BA 18**
    border on the lateral surface; the transverse occipital
    sulcus is adjacent to the **BA 18 / BA 19** transition
    (V3A / V3B territory).

..cortex
    The **functional sibling**. The calcarine sulcus is the
    surface landmark for **V1**; the lunate sulcus, when present,
    marks the **V1 / V2** border; the transverse occipital sulcus
    is adjacent to the **V3A / V3B** territory (forward
    references). Each of the three current sulci must cross-
    reference the corresponding V area as its **primary
    functional overlay**.

..cortex.temporal
    The **ventral neighbour of the occipital lobe**. The
    **lateral occipitotemporal sulcus** is the boundary with the
    temporal lobe — it separates the lateral occipital gyrus
    from the fusiform gyrus. **The sulcus lives in the temporal
    lobe's sulci package (or a shared package)**, not here. When
    it is added, the temporal package must declare it as one of
    its dorsal boundaries.

..cortex.parietal
    The **dorsal neighbour of the occipital lobe**. The
    **transverse occipital sulcus** is the boundary with the
    parietal lobe — the dorsal bounding gyrus is the parietal
    angular gyrus. The **parieto-occipital sulcus** is the
    medial boundary — its rostral bounding gyrus is the parietal
    precuneus. **Both parieto-occipital and transverse
    occipital sulci must be cross-referenced from the parietal
    package** as occipital-parietal boundaries. The parietal
    package must declare the transverse occipital sulcus and
    the parieto-occipital sulcus as **dorsal / rostral
    boundaries** of the angular gyrus and precuneus
    respectively.

..cortex.frontal
    **No direct sulcal adjacency.** The frontal lobe's posterior
    boundary is the central sulcus, which is far from the
    occipital sulci. Recorded here to pre-empt a false
    cross-reference.

..cortex.cingulate
    **Indirect adjacency.** The **isthmus of the cingulate
    gyrus** is rostral to the calcarine sulcus, and the **parieto-
    occipital sulcus** separates the cuneus from the precuneus.
    The cingulate package's posterior extent (the isthmus) is
    adjacent to the occipital lobe's rostral extent. The cingulate
    package must declare the calcarine sulcus as one of its
    **caudal neighbours**.

..cortex.insular  — indirect
    No direct insular → occipital sulcus projection.
    Recorded here to pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **Indirect relationship.** The LGN is the thalamic relay to
    V1, whose territory is bounded by the calcarine sulcus. The
    LGN is **not** directly adjacent to any occipital sulcus.

../../subcortical/medial_temporal_lobe/hippocampus
    **Indirect relationship.** The hippocampus is in the medial
    temporal lobe, adjacent to the temporal-occipital junction
    via the collateral sulcus and the parahippocampal gyrus. The
    occipital sulci are **not** directly adjacent to the
    hippocampus.

../../right/cortex/occipital/sulci
    The **right-hemisphere homologue**. Structural fields
    (child package names, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    functional landmarks) MUST be byte-identical. Geometric and
    clinical fields (VARIANTS, CLINICAL_ANCHORS) diverge — the
    left calcarine sulcus's V1 banks carry the **right** visual
    hemifield; the right calcarine sulcus's V1 banks carry the
    **left** visual hemifield. The left lunate sulcus's V1 / V2
    border marks the **right** hemifield's V1 / V2 boundary; the
    right's marks the **left** hemifield's. The left transverse
    occipital sulcus is the boundary of the left lateral
    occipital gyrus; the right's is the boundary of the right
    lateral occipital gyrus. **The three current sulci and the
    two forward-reference sulci are structurally identical on
    both sides** — what differs is the **represented visual
    hemifield** and the **clinical anchors**.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT FOR EACH CHILD PACKAGE
--------------------------------------------------------------------------------

Every child sulcus package (e.g. ``calcarine_sulcus/__init__.py``)
MUST expose the following module-level names:

    SULCUS_NAME : str
        Canonical snake_case name, identical to the folder name.
        Example: "calcarine_sulcus"

    HEMISPHERE : str
        "left" (this branch) or "right" (the sibling branch).

    LOBE : str
        "occipital"

    BOUNDING_GYRI : dict[str, tuple[str, ...]]
        Direction → tuple of gyrus names it bounds in that
        direction. **The occipital sulci require special handling
        for inter-lobar boundaries** (see the DUALITY CONTRACT
        above):
            calcarine_sulcus:
                {"upper_bank": ("cuneus",),
                 "lower_bank": ("lingual_gyrus",)}
            lunate_sulcus (when present):
                {"rostral": ("v2_lateral_territory",),
                 "caudal": ("v1_lateral_territory",)}
            transverse_occipital_sulcus:
                {"ventral": ("lateral_occipital_gyrus",),
                 "dorsal": ("angular_gyrus",)}
                # **Note: the dorsal bounding gyrus is a
                # parietal gyrus, not an occipital gyrus.**

    BRODMANN_ADJACENCY : dict[str, tuple[int, ...]]
        Side → tuple of Brodmann areas abutting the sulcus on
        that side.
            calcarine_sulcus:
                {"upper_bank": (17,),
                 "lower_bank": (17,)}
                # Both banks are BA 17 (V1).
            lunate_sulcus (when present):
                {"rostral": (18,),   # V2, part of BA 18
                 "caudal": (17,)}    # V1, BA 17
            transverse_occipital_sulcus:
                {"ventral": (19,),   # V3d / V4d / LOC, part of
                                     # BA 19
                 "dorsal": (39,)}    # Angular gyrus, BA 39

    EXTENT : dict[str, tuple[str, ...]]
        Landmarks at each end of the sulcus.
            calcarine_sulcus:
                {"caudal": ("occipital_pole",),
                 "rostral": ("isthmus_of_cingulate_gyrus",
                             "parieto_occipital_sulcus")}
            lunate_sulcus (when present):
                {"dorsal": ("transverse_occipital_sulcus",),
                 "ventral": ("lateral_occipitotemporal_sulcus",)}
            transverse_occipital_sulcus:
                {"medial": ("parieto_occipital_sulcus",),
                 "lateral": ("preoccipital_notch",)}

    PRESENCE_PROBABILITY : float
        **Only for the lunate sulcus** — approximately 0.5
        (present in roughly 40–60 % of human brains). Use
        ``1.0`` for the calcarine and transverse occipital
        sulci (both are reliably present).

    RETINOTOPIC_ROLE : str
        The retinotopic meridian or functional landmark the
        sulcus represents.
            calcarine_sulcus: "horizontal_meridian_upper_lower_
                              banks_dorsal_ventral_v1"
            lunate_sulcus: "vertical_meridian_v1_v2_border"
            transverse_occipital_sulcus: "lobar_boundary_not_
                                         retinotopic"

    VARIANTS : tuple[str, ...]
        Common anatomical variants and their approximate
        prevalence.
            calcarine_sulcus:
                ("continuous_~90%",
                 "interrupted_~10%",
                 "rostral_extension_to_isthmus_~70%")
            lunate_sulcus:
                ("absent_~40%",
                 "continuous_~35%",
                 "fragmented_~25%")
            transverse_occipital_sulcus:
                ("continuous_~80%",
                 "interrupted_~20%")

    CLINICAL_ANCHORS : tuple[str, ...]
        Free-form tags matching the clinical-significance notes.
            calcarine_sulcus: ("v1_surface_landmark",
                              "homonymous_hemianopia_lesion",
                              "macular_sparing_field_defect",
                              "cortical_blindness_bilateral")
            lunate_sulcus: ("v1_v2_border_landmark",
                           "conditional_landmark_absent_in_~40%")
            transverse_occipital_sulcus:
                ("lobar_boundary_landmark",
                 "v3a_v3b_territory_adjacency",
                 "angular_gyrus_parietal_boundary")

    CONNECTIVITY : dict[str, tuple[str, ...]]
        Optional. Sulci are grooves, not tracts, but they are
        **landmarks for white-matter bundles** that run beneath
        them.
            calcarine_sulcus:
                {"optic_radiation": ("traverses_beneath_calcarine_"
                                     "sulcus",)}
                # The optic radiation (geniculocalcarine tract)
                # runs beneath the calcarine sulcus en route to
                # V1.
            lunate_sulcus: {}  # no major bundle
            transverse_occipital_sulcus:
                {"inferior_longitudinal_fasciculus":
                     ("traverses_beneath_transverse_occipital_"
                      "sulcus",)}

    SUBDIVISIONS : tuple[str, ...]
        Names of any nested sub-packages. Must be empty in the
        current tree.

    __all__ : list[str]
        Must include every public name above.

The child's ``__init__.py`` should additionally contain a docstring
following the SAME template used in the frontal sulci children:
hierarchical location → bounding gyri → Brodmann adjacency →
retinotopic role → extent → variants → clinical significance →
cross-references → contract reminder → checklist.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``sulci/__init__.py`` is a pure namespace + registry. It must:

1. Import the three child packages (no side effects):
       from . import calcarine_sulcus
       from . import lunate_sulcus
       from . import transverse_occipital_sulcus

2. Expose a machine-readable registry:

       SULCI = {
           "calcarine_sulcus":            calcarine_sulcus,
           "lunate_sulcus":               lunate_sulcus,
           "transverse_occipital_sulcus": transverse_occipital_sulcus,
       }

3. Expose the **inverse index** — gyrus name → tuple of sulci
   that bound it. This must be derived from the children's
   ``BOUNDING_GYRI`` dicts, not hand-written, so it cannot drift:

       GYRUS_TO_SULCI = {
           # computed at import time by inverting BOUNDING_GYRI
           "cuneus":                ("calcarine_sulcus",),
           "lingual_gyrus":         ("calcarine_sulcus",),
           "lateral_occipital_gyrus": ("lunate_sulcus",
                                       "transverse_occipital_sulcus"),
           "angular_gyrus":         ("transverse_occipital_sulcus",),
       }

   **The inversion must tolerate unresolved gyrus names** (the
   lingual gyrus and angular gyrus are forward references, and
   the lingual gyrus is a forward reference in ``..gyri``). The
   parent's inversion function must record them as **forward
   references** rather than failing.

4. Expose a flat Brodmann-to-sulcus adjacency index,
   many-to-many:

       BRODMANN_TO_SULCI = {
           17: ("calcarine_sulcus", "lunate_sulcus"),
           18: ("lunate_sulcus",),
           19: ("transverse_occipital_sulcus",),
           39: ("transverse_occipital_sulcus",),
       }

   Like ``GYRUS_TO_SULCI``, this must be derived from the
   children's ``BRODMANN_ADJACENCY`` dicts.

5. Expose a **retinotopic role index**:

       RETINOTOPIC_ROLE_INDEX = {
           "calcarine_sulcus":            "horizontal_meridian",
           "lunate_sulcus":               "vertical_meridian",
           "transverse_occipital_sulcus": None,  # lobar
       }

   This is a hand-written index (the retinotopic role is a
   functional fact, not a derivation from the other fields), and
   it is the **only occipital sulci index that requires manual
   curation**.

6. Expose the **hemifield index** for the occipital sulci:

       SULCUS_HEMIFIELD = {
           "calcarine_sulcus":            "right",   # left side
           "lunate_sulcus":               "right",   # left side
           "transverse_occipital_sulcus": "right",   # left side
       }

   **All three sulci carry the right hemifield on the left side**
   — they bound V1's (calcarine), V1/V2's (lunate), and V3d/V4d/
   LOC's (transverse occipital) territory, all of which represent
   the right hemifield. **The right hemisphere's sulci carry the
   left hemifield** (documented in the right sibling).

7. Expose the **forward-reference sulci** list:

       FORWARD_REFERENCE_SULCI = (
           "parieto_occipital_sulcus",
           "lateral_occipitotemporal_sulcus",
       )

   The **parieto-occipital sulcus** and the **lateral
   occipitotemporal sulcus** are inter-lobar boundaries that are
   not yet packages in the tree. **When they are created, they
   must be resolved in the same commit, in both hemispheres**,
   and their placement (under ``..occipital/sulci``,
   ``..parietal/sulci`` / ``..temporal/sulci``, or a shared
   ``..sulci`` parent) must be decided hemisphere-invariantly.

8. Define ``__all__ = list(SULCI) + ["GYRUS_TO_SULCI",
                                    "BRODMANN_TO_SULCI",
                                    "RETINOTOPIC_ROLE_INDEX",
                                    "SULCUS_HEMIFIELD",
                                    "FORWARD_REFERENCE_SULCI"]``

9. Contain **no** logic beyond the above. Any behaviour belongs in
   ``cortex/`` or in the ``memory/`` layer.

--------------------------------------------------------------------------------
DUALITY CONTRACT — SULCI ↔ GYRI, WITH THE THREE OCCIPITAL SPECIAL CASES
--------------------------------------------------------------------------------

This package and the occipital gyral packages (``..gyri``,
``..cuneus``, and the lingual gyrus forward reference) are
**dual**. The following invariants MUST hold and are asserted by a
test in ``tests/``:

  * For every sulcus S in this package and every
    (direction, gyrus-tuple) pair in S.BOUNDING_GYRI, the gyrus G in
    that tuple MUST list S in its own boundary cross-references.

  * For every gyrus G in the occipital gyral packages and every
    sulcus S named in G's boundary cross-references, S MUST appear
    in this package and MUST name G in its BOUNDING_GYRI.

  * Every gyrus named in any BOUNDING_GYRI MUST exist as a
    **current package** or be a **documented forward reference**.
    **The occipital sulci's BOUNDING_GYRI includes three forward
    references**: the lingual gyrus (medial-surface forward
    reference in ``..gyri``), the angular gyrus (parietal
    forward reference in ``..gyri`` — actually a parietal gyrus,
    so it is a cross-lobe forward reference), and the V1 lateral
    territory and V2 lateral territory (which are **anatomical
    sub-regions** of the calcarine cortex and lateral occipital
    gyrus respectively, not standalone gyrus packages).

  * Every Brodmann area in any BRODMANN_ADJACENCY MUST appear in
    some gyrus's BRODMANN_AREAS (or be a documented cross-lobe
    forward reference — BA 39 is the parietal angular gyrus and
    lives in ``..parietal/brodmann_areas/``, not here).

**The three occipital special cases** (cuneus / lingual gyrus
duality, lunate sulcus conditional presence, transverse occipital
lobar boundary) mean that the duality contract for the occipital
lobe is **more permissive about forward references** than the
frontal lobe's. **The parent inversion function must tolerate the
following unresolved names**:

    lingual_gyrus              — medial-surface forward reference
    angular_gyrus              — parietal cross-lobe forward
                                 reference
    v1_lateral_territory       — sub-region of calcarine cortex
    v2_lateral_territory       — sub-region of lateral occipital
                                 gyrus

**These four names must be listed in the parent's
FORWARD_REFERENCE_GYRI field** (see the implementation contract
above), and the duality test must treat them as forward references
rather than failures.

**The duality contract is byte-identical on both hemispheres** —
the occipital sulci's bounding relationships are topological, not
lateralized. What differs is the **represented visual hemifield**
and the **clinical anchors**.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are two inter-lobar forward-reference sulci and four
forward-reference gyrus names for this package**, which together
constitute the **largest forward-reference burden of any occipital
sulci package**:

**Forward-reference sulci (2):**

1. **Parieto-occipital sulcus** — the medial boundary between the
   cuneus (occipital) and the precuneus (parietal). **Its
   placement is open**: under this package (as an occipital
   boundary), under ``..parietal/sulci`` (as a parietal boundary),
   or under a shared ``..sulci`` parent. **The decision must be
   made in the same commit as its creation, in both hemispheres.**

2. **Lateral occipitotemporal sulcus** — the ventral boundary
   between the lateral occipital gyrus (occipital) and the
   fusiform gyrus (temporal). **Its placement is open**: same
   three options. **The decision must be made in the same commit
   as its creation, in both hemispheres.**

**Forward-reference gyrus names (4):**

1. **Lingual gyrus** — the lower-bank gyrus of the calcarine
   sulcus. A **forward reference in ``..gyri``** (see the
   ``..gyri`` parent's caveat). When created, it should be
   placed either at the ``..occipital`` parent level (like the
   cuneus) or under ``..gyri`` — the decision must preserve the
   cuneus / lingual gyrus symmetry.

2. **Angular gyrus** — the dorsal bounding gyrus of the transverse
   occipital sulcus. A **parietal gyrus**, not an occipital one.
   When created under ``..parietal/gyri``, it must cross-
   reference the transverse occipital sulcus as one of its
   **ventral boundaries**.

3. **V1 lateral territory** — the caudal bank of the lunate
   sulcus. **Not a standalone gyrus package** — it is a sub-
   region of the calcarine cortex that lies on the lateral
   surface of the occipital lobe. When the lunate sulcus is
   promoted to a package, the V1 lateral territory must be
   declared as the **caudal bounding region** within the
   lunate sulcus package itself (not as a gyrus package).

4. **V2 lateral territory** — the rostral bank of the lunate
   sulcus. Same as V1 lateral territory — a sub-region of the
   lateral occipital gyrus, not a standalone gyrus package.

**All forward references are byte-identical to the left sibling's**
— the inter-lobar boundary placement questions are properties of
the occipital lobe's anatomy, not of the hemisphere.

**When the four forward-reference gyrus names and the two forward-
reference sulci are resolved, the parent's ``GYRUS_TO_SULCI`` and
``BRODMANN_TO_SULCI`` indices must be updated in the same commit,
in both hemispheres.**

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/cortex/occipital/sulci``:

    MUST be identical (byte-for-byte):
        LOBE                         "occipital"
        SULCI_CHILDREN               the same three child names
                                     (calcarine, lunate,
                                     transverse occipital)
        Each child's SULCUS_NAME, LOBE, BOUNDING_GYRI,
                                     BRODMANN_ADJACENCY,
                                     RETINOTOPIC_ROLE, EXTENT,
                                     VARIANTS, SUBDIVISIONS
        The derived GYRUS_TO_SULCI and BRODMANN_TO_SULCI indices
        The RETINOTOPIC_ROLE_INDEX
        The FORWARD_REFERENCE_SULCI list
        The forward-reference gyrus list (lingual, angular,
                                     V1 lateral territory,
                                     V2 lateral territory)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        SULCUS_HEMIFIELD       **all "right"** (left) vs
                               **all "left"** (right) — the
                               occipital sulci bound territories
                               that represent the
                               contralateral visual hemifield,
                               so the left sulci all carry the
                               right hemifield and the right
                               sulci all carry the left
                               hemifield.
        CLINICAL_ANCHORS       left: the calcarine sulcus is the
                               surface landmark for the
                               left V1 (which processes the
                               RIGHT hemifield); its lesions
                               produce **right homonymous
                               hemianopia**; the lunate
                               sulcus, when present, marks
                               the **right** hemifield's
                               V1 / V2 border; the transverse
                               occipital sulcus bounds the
                               left lateral occipital gyrus.
                               right: the calcarine sulcus is
                               the surface landmark for the
                               right V1 (which processes the
                               LEFT hemifield); its lesions
                               produce **left homonymous
                               hemianopia**; the lunate
                               sulcus, when present, marks
                               the **left** hemifield's
                               V1 / V2 border; the transverse
                               occipital sulcus bounds the
                               right lateral occipital
                               gyrus.

**The sulcal topology (BOUNDING_GYRI, BRODMANN_ADJACENCY, and the
derived indices) is byte-identical on both sides** — sulcal
boundaries are topological, not lateralized.

**The sulcal geometry may differ** (the lunate sulcus's
PRESENCE_PROBABILITY may differ slightly across hemispheres — some
studies report left-right asymmetry in lunate sulcus presence, but
the current tree treats it as 0.5 on both sides). **Any such
asymmetry belongs in the child package's VARIANTS field, not in
this parent's contract.**

**The clinical anchors and the SULCUS_HEMIFIELD field are the only
places where the two hemispheres diverge** — and they diverge in
exactly one direction: **the contralateral visual hemifield**.

**The FORWARD_REFERENCE_SULCI list and the forward-reference
gyrus list are byte-identical on both sides** and must not be
allowed to drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/sulci/`` — a sibling of
    ``brodmann_areas``, ``cortex``, ``cuneus``, and ``gyri``.
[ ] The three current sulci (calcarine, lunate, transverse
    occipital) are imported and registered.
[ ] ``SULCI_CHILDREN`` lists the three child names and is
    byte-identical to the right sibling's.
[ ] Each child's BOUNDING_GYRI, BRODMANN_ADJACENCY,
    RETINOTOPIC_ROLE, EXTENT, VARIANTS, and SUBDIVISIONS are
    byte-identical to the right sibling's.
[ ] **The calcarine sulcus's BOUNDING_GYRI correctly names the
    cuneus (upper bank) and the lingual gyrus (lower bank,
    forward reference)** — the two banks of the calcarine are
    both V1 territory.
[ ] **The calcarine sulcus's BRODMANN_ADJACENCY is BA 17 on
    both banks** — V1 is BA 17 on both sides of the sulcus.
[ ] **The calcarine sulcus's RETINOTOPIC_ROLE is
    "horizontal_meridian_upper_lower_banks_dorsal_ventral_v1"**
    — the fundus of the calcarine is the horizontal meridian.
[ ] **The lunate sulcus carries a PRESENCE_PROBABILITY field**
    (approximately 0.5) — it is the only occipital sulcus whose
    presence is probabilistic.
[ ] **The lunate sulcus's BOUNDING_GYRI correctly names the V2
    lateral territory (rostral bank) and the V1 lateral territory
    (caudal bank)** — both are sub-regions, not standalone
    gyri.
[ ] **The lunate sulcus's BRODMANN_ADJACENCY is BA 18 (rostral)
    and BA 17 (caudal)** — the V1 / V2 border.
[ ] **The transverse occipital sulcus's BOUNDING_GYRI correctly
    names the lateral occipital gyrus (ventral) and the angular
    gyrus (dorsal, parietal forward reference)**.
[ ] **The transverse occipital sulcus's BRODMANN_ADJACENCY is
    BA 19 (ventral) and BA 39 (dorsal, parietal)** — the
    occipital / parietal boundary.
[ ] ``GYRUS_TO_SULCI`` is present, derived from the children's
    BOUNDING_GYRI, and tolerates the four forward-reference gyrus
    names (lingual, angular, V1 lateral territory, V2 lateral
    territory).
[ ] ``BRODMANN_TO_SULCI`` is present, derived from the children's
    BRODMANN_ADJACENCY, and tolerates the BA 39 parietal forward
    reference.
[ ] ``RETINOTOPIC_ROLE_INDEX`` is present — the **only
    manually-curated index in the package** — and correctly
    records the calcarine's horizontal meridian, the lunate's
    vertical meridian, and the transverse occipital's non-
    retinotopic lobar role.
[ ] ``SULCUS_HEMIFIELD`` is present with all three sulci
    assigned to "right" on the left side.
[ ] ``FORWARD_REFERENCE_SULCI`` lists the parieto-occipital
    sulcus and the lateral occipitotemporal sulcus.
[ ] **The parieto-occipital sulcus is documented as the medial
    boundary between the cuneus (occipital) and the precuneus
    (parietal)**, with its placement open (this package vs
    ``..parietal/sulci`` vs shared ``..sulci``).
[ ] **The lateral occipitotemporal sulcus is documented as the
    ventral boundary between the lateral occipital gyrus
    (occipital) and the fusiform gyrus (temporal)**, with its
    placement open.
[ ] **The lingual gyrus is documented as a forward reference in
    ``..gyri``** — the lower-bank gyrus of the calcarine sulcus,
    to be placed either at the parent level or under ``..gyri``,
    preserving the cuneus / lingual gyrus symmetry.
[ ] **The angular gyrus is documented as a parietal forward
    reference** — the dorsal bounding gyrus of the transverse
    occipital sulcus, to be created under ``..parietal/gyri``
    with a cross-reference back to the transverse occipital
    sulcus.
[ ] **The V1 lateral territory and V2 lateral territory are
    documented as sub-regions** of the calcarine cortex and the
    lateral occipital gyrus respectively, not as standalone
    gyrus packages.
[ ] **The duality contract is documented with the three
    occipital special cases**: calcarine / lingual gyrus duality,
    lunate sulcus conditional presence, transverse occipital
    lobar boundary.
[ ] **The occipital sulci's uniqueness among the cortical lobes
    is documented**: the calcarine sulcus defines a primary
    sensory area (V1) with an architectonically visible
    boundary (the stria of Gennari), and its fundus represents
    a specific retinotopic meridian (the horizontal meridian).
[ ] **The occipital pole's lack of a dedicated sulcus is
    documented** — the occipital pole is the caudal convergence
    of the cuneus and lingual gyrus; there is no "occipital
    polar sulcus" in the classical scheme.
[ ] Every child's own docstring (calcarine, lunate, transverse
    occipital) follows the same template used in the frontal
    sulci children — hierarchical location → bounding gyri →
    Brodmann adjacency → retinotopic role → extent → variants
    → clinical significance → cross-references → contract →
    checklist.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (child names, BOUNDING_GYRI, BRODMANN_ADJACENCY, derived
    indices, RETINOTOPIC_ROLE_INDEX, forward references) match
    the right sibling; SULCUS_HEMIFIELD and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    sulci carry the right hemifield, and the right sulci carry
    the left hemifield. The `SULCUS_HEMIFIELD` field is the
    single source of truth for this asymmetry.
[ ] **The forward references are byte-identical to the right
    sibling's** — the parieto-occipital sulcus, the lateral
    occipitotemporal sulcus, the lingual gyrus, the angular
    gyrus, the V1 lateral territory, and the V2 lateral
    territory are the same forward-reference names on both
    sides.
[ ] Any downstream code querying "what sulci are in the left
    occipital lobe?" must receive the three current sulci
    (calcarine, lunate, transverse occipital) plus the two
    forward-reference sulci (parieto-occipital, lateral
    occipitotemporal), with the forward references marked.
[ ] Any downstream code querying "what does the calcarine
    sulcus bound?" must receive "the cuneus (upper bank) and
    the lingual gyrus (lower bank)" — both V1 territory.
[ ] Any downstream code querying "what does the calcarine
    sulcus represent retinotopically?" must receive "the
    horizontal meridian of the visual field, at the fundus
    of the sulcus."
[ ] Any downstream code querying "what does the lunate sulcus
    represent retinotopically, and when does it exist?" must
    receive "the vertical meridian (V1 / V2 border) on the
    lateral surface, when present (~50 % of brains)."
[ ] Any downstream code querying "what does the transverse
    occipital sulcus bound?" must receive "the lateral
    occipital gyrus (ventral) and the angular gyrus
    (dorsal, parietal)."
[ ] Any downstream code querying "what visual hemifield does
    the left calcarine sulcus represent?" must receive "the
    RIGHT visual hemifield" — the SULCUS_HEMIFIELD field is
    the source of truth.
[ ] Any downstream code assigning the parieto-occipital
    sulcus's placement must resolve it consistently across
    hemispheres — no asymmetric placement is permitted.
[ ] Any downstream code assigning the lateral
    occipitotemporal sulcus's placement must resolve it
    consistently across hemispheres — no asymmetric placement
    is permitted.
[ ] Any downstream code querying "what is the occipital
    lobe's most functionally load-bearing sulcus?" must
    receive "the calcarine sulcus — it defines V1 with an
    architectonically visible boundary (the stria of
    Gennari) and its fundus represents the horizontal
    meridian, the only sulcus in the cortex with both
    properties."
"""