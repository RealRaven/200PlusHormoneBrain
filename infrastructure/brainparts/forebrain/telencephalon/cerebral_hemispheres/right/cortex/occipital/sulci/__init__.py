"""
Occipital Sulci — Right Hemisphere
===================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
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

**This structural framing is byte-identical to the left sibling's**
— the occipital sulci's functional-load-bearing status, the
single-sulcus-defines-a-primary-sensory-area property, and the
horizontal-meridian-in-the-fundus property are all hemisphere-
invariant facts about the occipital lobe.

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
map** (the vertical meridian) rather than from a surface sulcus.

**This is the only occipital sulcus whose presence is probabilistic**,
and the ``PRESENCE_PROBABILITY`` field must be carried by the lunate
sulcus child package.

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

**The three special cases are byte-identical to the left sibling's**
— they are properties of the occipital lobe's anatomy, not of the
hemisphere.

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
       contralateral field** (**lower LEFT** on the right side).
       The **lower bank** carries the **ventral V1 representation
       of the upper contralateral field** (**upper LEFT** on the
       right side).

   **Architectonic signature:**
       The **stria of Gennari** is visible on both banks of the
       calcarine sulcus, and its **abrupt disappearance** at the
       V1 / V2 border is the architectonic basis of the
       architectonically unambiguous V1 / V2 boundary.

   **Clinical significance:**
       The calcarine sulcus is the **surface landmark for the
       calcarine cortex** — the V1 territory whose lesions
       produce **left homonymous hemianopia** (for a right
       calcarine lesion). **Macular sparing** is common (dual
       blood supply to the occipital pole). **Left homonymous
       hemianopia** is the right calcarine sulcus's primary
       clinical anchor.

   **Cross-reference:** ``..cuneus`` (upper-bank gyrus),
   ``..gyri`` (lingual gyrus forward reference),
   ``..cortex/primary_visual_cortex`` (V1), and
   ``..brodmann_areas/brodmann_area_17`` (BA 17).

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
       **Present in roughly 40–60 % of human brains** depending
       on the series. The child package must carry an explicit
       ``PRESENCE_PROBABILITY`` field. **The right-hemisphere
       prevalence is comparable to the left (~50 %), with
       minor study-to-study variation**; any documented
       left-right asymmetry belongs in the child package's
       VARIANTS field.

   **Architectonic signature:**
       The V1 / V2 border is marked by the **abrupt disappearance
       of the stria of Gennari** at the lateral edge of the
       calcarine cortex — present on both banks of the lateral
       occipital sulcus when the lunate sulcus is present.

   **Clinical significance:**
       The lunate sulcus is a **secondary landmark** for the
       V1 / V2 border. Its primary clinical relevance is as a
       **retinotopic reference point** in mapping the visual
       field onto the lateral surface of the occipital lobe.

   **Cross-reference:** ``..gyri/lateral_occipital_gyrus``,
   ``..cortex/primary_visual_cortex`` (V1), and
   ``..cortex/v2`` (V2).

3. transverse_occipital_sulcus
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   The **dorsal-surface sulcus** that separates the **lateral
   occipital gyri** (ventrally) from the **parietal lobe's
   angular gyrus** (dorsally).

   **Bounding gyri:**
       ventral bank    → **lateral occipital gyrus** (occipital
                         gyral child of ``..gyri``)
       dorsal bank     → **angular gyrus** (parietal lobe)

   **Retinotopic role:**
       The transverse occipital sulcus is **not** a strict
       retinotopic landmark — it is a **lobar boundary** on the
       lateral surface.

   **Additional note:**
       The transverse occipital sulcus is **adjacent to the
       V3A / V3B territory** (forward references in
       ``..cortex``). **On the right, V3A is the more strongly
       engaged side**, and the right transverse occipital
       sulcus is the surface landmark for the dominant dorsal
       motion and spatial-attention substrate's vicinity.

   **Cross-reference:** ``..gyri/lateral_occipital_gyrus``,
   ``..cortex/v3a`` (forward reference), ``..cortex/v3b``
   (forward reference), and ``..parietal/gyri`` (angular gyrus).

**This section is structurally identical to the left sibling's** —
the three sulci, their bounding gyri, their Brodmann adjacencies,
their retinotopic roles, and their clinical anchors are the same on
both sides, with the visual hemifield labels flipped (right's
calcarine carries lower LEFT / upper LEFT instead of lower RIGHT /
upper RIGHT).

--------------------------------------------------------------------------------
FORWARD REFERENCES AND CROSS-PACKAGE REFERENCES
--------------------------------------------------------------------------------

**The parieto-occipital sulcus** is the **medial boundary between
the occipital and parietal lobes** — it separates the **cuneus**
(occipital) from the **precuneus** (parietal). **It is NOT a
current child of this package.** Its placement options are:

  (a) **Under ``..parietal/sulci``** — as a parietal boundary
      with the occipital lobe.
  (b) **Under a shared ``..sulci`` parent** — if the tree adds a
      cortex-level ``..sulci`` package for inter-lobar sulci.
  (c) **Under this package** — as a medial boundary with the
      parietal lobe (because the cuneus, its caudal bank, is the
      occipital gyrus).

**The current tree leaves the placement open.** The **calcarine
sulcus** is **adjacent** to the parieto-occipital sulcus at the
**anterior calcarine banks**. **When the parieto-occipital sulcus is
added, the calcarine sulcus package must cross-reference it as the
rostral neighbouring sulcus**, and the cuneus package must
cross-reference it as its **rostral bounding sulcus**.

**The lateral occipitotemporal sulcus** is the **ventral boundary
between the occipital and temporal lobes** — it separates the
**lateral occipital gyrus** (occipital) from the **fusiform gyrus**
(temporal). **On the right, the fusiform gyrus contains the right
FFA** — the face-recognition endpoint downstream of the right
lateral occipital gyrus's LOC. The lateral occipitotemporal sulcus
is therefore the **surface boundary between the right LOC territory
and the right FFA territory**. **It is NOT a current child of this
package**, with the same three placement options as the parieto-
occipital sulcus.

**Both forward-reference sulci are byte-identical to the left
sibling's** — the inter-lobar boundary placement questions are
properties of the occipital lobe's anatomy, not of the hemisphere.

--------------------------------------------------------------------------------
CROSS-REFERENCES (sibling modules under ``occipital/``)
--------------------------------------------------------------------------------

..gyri
    The **lateral-surface gyral parent**. The transverse occipital
    sulcus bounds the lateral occipital gyrus dorsally; the
    lunate sulcus, when present, crosses it.

..cuneus
    The **medial-surface upper-bank gyral landmark**. The
    calcarine sulcus bounds the cuneus caudally (the upper bank
    of the calcarine is the lower margin of the cuneus). **On
    the right, the cuneus's V1 upper-bank representation carries
    the lower LEFT field.**

..brodmann_areas
    The **cytoarchitectonic sibling**. The calcarine sulcus is the
    surface landmark for **BA 17**; the lunate sulcus, when
    present, marks the **BA 17 / BA 18** border on the lateral
    surface; the transverse occipital sulcus is adjacent to the
    **BA 18 / BA 19** transition (V3A / V3B territory). **On the
    right, BA 19's V3A and V5/MT+ are the dominant dorsal-
    stream substrates.**

..cortex
    The **functional sibling**. The calcarine sulcus is the
    surface landmark for **V1**; the lunate sulcus, when present,
    marks the **V1 / V2** border; the transverse occipital sulcus
    is adjacent to the **V3A / V3B** territory (forward
    references). **On the right, V3A and MT/V5 are the dominant
    motion and dorsal-attention substrates**, and the right
    transverse occipital sulcus is the surface landmark for
    their vicinity.

..cortex.temporal
    The **ventral neighbour of the occipital lobe**. The
    **lateral occipitotemporal sulcus** is the boundary with the
    temporal lobe — it separates the lateral occipital gyrus
    from the fusiform gyrus. **On the right, the fusiform gyrus
    contains the right FFA** (the face-recognition endpoint).
    The sulcus lives in the temporal lobe's sulci package (or a
    shared package), not here. When it is added, the temporal
    package must declare it as one of its dorsal boundaries.

..cortex.parietal
    The **dorsal neighbour of the occipital lobe**. The
    **transverse occipital sulcus** is the boundary with the
    parietal lobe — the dorsal bounding gyrus is the parietal
    angular gyrus. The **parieto-occipital sulcus** is the
    medial boundary — its rostral bounding gyrus is the parietal
    precuneus. Both must be cross-referenced from the parietal
    package as occipital-parietal boundaries.

..cortex.frontal
    **No direct sulcal adjacency.** The frontal lobe's posterior
    boundary is the central sulcus, which is far from the
    occipital sulci. Recorded here to pre-empt a false
    cross-reference.

..cortex.cingulate
    **Indirect adjacency.** The **isthmus of the cingulate
    gyrus** is rostral to the calcarine sulcus, and the
    **parieto-occipital sulcus** separates the cuneus from the
    precuneus. The cingulate package's posterior extent (the
    isthmus) is adjacent to the occipital lobe's rostral extent.

..cortex.insular  — indirect
    No direct insular → occipital sulcus projection.
    Recorded here to pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **Indirect relationship.** The LGN is the thalamic relay to
    V1, whose territory is bounded by the calcarine sulcus.

../../subcortical/medial_temporal_lobe/hippocampus
    **Indirect relationship.** The hippocampus is in the medial
    temporal lobe, adjacent to the temporal-occipital junction
    via the collateral sulcus and the parahippocampal gyrus.

../../left/cortex/occipital/sulci
    The **left-hemisphere homologue**. Structural fields
    (child package names, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    functional landmarks, forward-reference lists) MUST be
    byte-identical. Geometric and clinical fields
    (SULCUS_HEMIFIELD, CLINICAL_ANCHORS) diverge — the right
    calcarine sulcus's V1 banks carry the **left** visual
    hemifield; the left calcarine sulcus's V1 banks carry the
    **right** visual hemifield. The right lunate sulcus's
    V1 / V2 border marks the **left** hemifield's V1 / V2
    boundary; the left's marks the **right** hemifield's. The
    right transverse occipital sulcus bounds the right lateral
    occipital gyrus (which feeds the right FFA); the left
    transverse occipital sulcus bounds the left lateral
    occipital gyrus (which feeds the left VWFA). **The three
    current sulci and the two forward-reference sulci are
    structurally identical on both sides** — what differs is
    the **represented visual hemifield** and the **clinical
    anchors**.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT FOR EACH CHILD PACKAGE
--------------------------------------------------------------------------------

Every child sulcus package MUST expose the following module-level
names:

    SULCUS_NAME : str
        Canonical snake_case name, identical to the folder name.

    HEMISPHERE : str
        "right" (this branch) or "left" (the sibling branch).

    LOBE : str
        "occipital"

    BOUNDING_GYRI : dict[str, tuple[str, ...]]
        Direction → tuple of gyrus names it bounds in that
        direction. **Byte-identical to the left sibling's** —
        sulcal topology is hemisphere-invariant.
            calcarine_sulcus:
                {"upper_bank": ("cuneus",),
                 "lower_bank": ("lingual_gyrus",)}
            lunate_sulcus (when present):
                {"rostral": ("v2_lateral_territory",),
                 "caudal": ("v1_lateral_territory",)}
            transverse_occipital_sulcus:
                {"ventral": ("lateral_occipital_gyrus",),
                 "dorsal": ("angular_gyrus",)}

    BRODMANN_ADJACENCY : dict[str, tuple[int, ...]]
        **Byte-identical to the left sibling's.**
            calcarine_sulcus:
                {"upper_bank": (17,),
                 "lower_bank": (17,)}
            lunate_sulcus (when present):
                {"rostral": (18,),
                 "caudal": (17,)}
            transverse_occipital_sulcus:
                {"ventral": (19,),
                 "dorsal": (39,)}

    EXTENT : dict[str, tuple[str, ...]]
        **Byte-identical to the left sibling's.**

    PRESENCE_PROBABILITY : float
        **Only for the lunate sulcus** — approximately 0.5.
        Use ``1.0`` for the calcarine and transverse occipital
        sulci.

    RETINOTOPIC_ROLE : str
        **Byte-identical to the left sibling's.**
            calcarine_sulcus: "horizontal_meridian_upper_lower_
                              banks_dorsal_ventral_v1"
            lunate_sulcus: "vertical_meridian_v1_v2_border"
            transverse_occipital_sulcus: "lobar_boundary_not_
                                         retinotopic"

    VARIANTS : tuple[str, ...]
        **Byte-identical to the left sibling's**, with any
        **right-specific geometric variation** (e.g. if the
        right lunate sulcus has a slightly different presence
        rate or morphology in the literature) recorded here
        rather than in BOUNDING_GYRI. **The current tree uses
        the same variant lists on both sides** because the
        literature does not support a strong hemisphere
        asymmetry in the calcarine or transverse occipital
        sulci, and the lunate sulcus's presence probability is
        comparable on both sides.

    CLINICAL_ANCHORS : tuple[str, ...]
        **Differs from the left sibling's** — the right-sided
        anchors are the mirror of the left-sided ones, with the
        visual hemifield flipped.
            calcarine_sulcus: ("v1_surface_landmark",
                              "left_homonymous_hemianopia_lesion",
                              "macular_sparing_field_defect",
                              "cortical_blindness_bilateral")
            lunate_sulcus: ("v1_v2_border_landmark",
                           "conditional_landmark_absent_in_~40%")
            transverse_occipital_sulcus:
                ("lobar_boundary_landmark",
                 "v3a_v3b_territory_adjacency_dominant_on_right",
                 "angular_gyrus_parietal_boundary")

    CONNECTIVITY : dict[str, tuple[str, ...]]
        **Byte-identical to the left sibling's.**
            calcarine_sulcus:
                {"optic_radiation": ("traverses_beneath_calcarine_"
                                     "sulcus",)}
            lunate_sulcus: {}
            transverse_occipital_sulcus:
                {"inferior_longitudinal_fasciculus":
                     ("traverses_beneath_transverse_occipital_"
                      "sulcus",)}

    SUBDIVISIONS : tuple[str, ...]
        Empty in the current tree.

    __all__ : list[str]
        Every public name above.

The child's ``__init__.py`` should additionally contain a docstring
following the SAME template used in the left sibling's children:
hierarchical location → bounding gyri → Brodmann adjacency →
retinotopic role → extent → variants → clinical significance →
cross-references → contract reminder → checklist.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``sulci/__init__.py`` must:

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
   that bound it, derived from the children's ``BOUNDING_GYRI``
   dicts:

       GYRUS_TO_SULCI = {
           "cuneus":                ("calcarine_sulcus",),
           "lingual_gyrus":         ("calcarine_sulcus",),
           "lateral_occipital_gyrus": ("lunate_sulcus",
                                       "transverse_occipital_sulcus"),
           "angular_gyrus":         ("transverse_occipital_sulcus",),
       }

   **Byte-identical to the left sibling's**, and tolerates the
   four forward-reference gyrus names.

4. Expose a flat Brodmann-to-sulcus adjacency index,
   many-to-many:

       BRODMANN_TO_SULCI = {
           17: ("calcarine_sulcus", "lunate_sulcus"),
           18: ("lunate_sulcus",),
           19: ("transverse_occipital_sulcus",),
           39: ("transverse_occipital_sulcus",),
       }

   **Byte-identical to the left sibling's.**

5. Expose a **retinotopic role index**:

       RETINOTOPIC_ROLE_INDEX = {
           "calcarine_sulcus":            "horizontal_meridian",
           "lunate_sulcus":               "vertical_meridian",
           "transverse_occipital_sulcus": None,  # lobar
       }

   **Byte-identical to the left sibling's** — the retinotopic
   role is hemisphere-invariant (the horizontal meridian is at
   the calcarine fundus on both sides, the vertical meridian is
   at the lunate sulcus on both sides).

6. Expose the **hemifield index** for the occipital sulci:

       SULCUS_HEMIFIELD = {
           "calcarine_sulcus":            "left",   # right side
           "lunate_sulcus":               "left",   # right side
           "transverse_occipital_sulcus": "left",   # right side
       }

   **All three sulci carry the LEFT hemifield on the right side**
   — they bound V1's (calcarine), V1/V2's (lunate), and V3d/V4d/
   LOC's (transverse occipital) territory, all of which represent
   the left hemifield on the right side. **The left hemisphere's
   sulci carry the right hemifield** (documented in the left
   sibling).

   **The `SULCUS_HEMIFIELD` index is the single source of truth
   for the hemisphere asymmetry** — the field is `"left"` on the
   right, `"right"` on the left, and downstream code must query
   this index rather than deriving the hemifield from the gyrus
   packages.

7. Expose the **forward-reference sulci** list:

       FORWARD_REFERENCE_SULCI = (
           "parieto_occipital_sulcus",
           "lateral_occipitotemporal_sulcus",
       )

   **Byte-identical to the left sibling's.** The
   parieto-occipital sulcus and the lateral occipitotemporal
   sulcus are inter-lobar boundaries that are not yet packages
   in the tree. **When they are created, they must be resolved
   in the same commit, in both hemispheres**, with a hemisphere-
   invariant placement decision.

8. Expose the **forward-reference gyrus names** list:

       FORWARD_REFERENCE_GYRI = (
           "lingual_gyrus",
           "angular_gyrus",
           "v1_lateral_territory",
           "v2_lateral_territory",
       )

   **Byte-identical to the left sibling's.** These are the four
   gyrus names that appear in BOUNDING_GYRI but are not
   currently packages.

9. Define ``__all__ = list(SULCI) + ["GYRUS_TO_SULCI",
                                    "BRODMANN_TO_SULCI",
                                    "RETINOTOPIC_ROLE_INDEX",
                                    "SULCUS_HEMIFIELD",
                                    "FORWARD_REFERENCE_SULCI",
                                    "FORWARD_REFERENCE_GYRI"]``

10. Contain **no** logic beyond the above. Any behaviour belongs
    in ``cortex/`` or in the ``memory/`` layer.

--------------------------------------------------------------------------------
DUALITY CONTRACT — SULCI ↔ GYRI, WITH THE THREE OCCIPITAL SPECIAL
CASES
--------------------------------------------------------------------------------

This package and the occipital gyral packages (``..gyri``,
``..cuneus``, and the lingual gyrus forward reference) are **dual**.
The following invariants MUST hold and are asserted by a test in
``tests/``:

  * For every sulcus S in this package and every
    (direction, gyrus-tuple) pair in S.BOUNDING_GYRI, the gyrus G
    in that tuple MUST list S in its own boundary cross-references.

  * For every gyrus G in the occipital gyral packages and every
    sulcus S named in G's boundary cross-references, S MUST appear
    in this package and MUST name G in its BOUNDING_GYRI.

  * Every gyrus named in any BOUNDING_GYRI MUST exist as a
    **current package** or be a **documented forward reference**.
    **The occipital sulci's BOUNDING_GYRI includes four forward
    references**: the lingual gyrus, the angular gyrus, the V1
    lateral territory, and the V2 lateral territory.

  * Every Brodmann area in any BRODMANN_ADJACENCY MUST appear in
    some gyrus's BRODMANN_AREAS (or be a documented cross-lobe
    forward reference — BA 39 is the parietal angular gyrus).

**The three occipital special cases** (cuneus / lingual gyrus
duality, lunate sulcus conditional presence, transverse occipital
lobar boundary) mean that the duality contract for the occipital
lobe is **more permissive about forward references** than the
frontal lobe's. **The parent inversion function must tolerate the
four unresolved gyrus names** listed in
``FORWARD_REFERENCE_GYRI``.

**The duality contract is byte-identical on both hemispheres** —
the occipital sulci's bounding relationships are topological, not
lateralized.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are two inter-lobar forward-reference sulci and four
forward-reference gyrus names for this package** (byte-identical
to the left sibling's):

**Forward-reference sulci (2):**

1. **Parieto-occipital sulcus** — the medial boundary between the
   cuneus (occipital) and the precuneus (parietal). Placement
   open: under this package, under ``..parietal/sulci``, or under
   a shared ``..sulci`` parent.

2. **Lateral occipitotemporal sulcus** — the ventral boundary
   between the lateral occipital gyrus (occipital) and the
   fusiform gyrus (temporal). **On the right, the fusiform gyrus
   contains the right FFA** — the face-recognition endpoint.
   Placement open: same three options.

**Forward-reference gyrus names (4):**

1. **Lingual gyrus** — the lower-bank gyrus of the calcarine
   sulcus. A **forward reference in ``..gyri``**. When created,
   its placement must preserve the cuneus / lingual gyrus
   symmetry.

2. **Angular gyrus** — the dorsal bounding gyrus of the transverse
   occipital sulcus. A **parietal gyrus**, not an occipital one.
   When created under ``..parietal/gyri``, it must cross-
   reference the transverse occipital sulcus as one of its
   **ventral boundaries**.

3. **V1 lateral territory** — the caudal bank of the lunate
   sulcus. A sub-region of the calcarine cortex, not a standalone
   gyrus package.

4. **V2 lateral territory** — the rostral bank of the lunate
   sulcus. A sub-region of the lateral occipital gyrus, not a
   standalone gyrus package.

**All forward references are byte-identical to the left sibling's.**

**When the four forward-reference gyrus names and the two forward-
reference sulci are resolved, the parent's ``GYRUS_TO_SULCI`` and
``BRODMANN_TO_SULCI`` indices must be updated in the same commit,
in both hemispheres.**

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/cortex/occipital/sulci``:

    MUST be identical (byte-for-byte):
        LOBE                         "occipital"
        SULCI_CHILDREN               the same three child names
        Each child's SULCUS_NAME, LOBE, BOUNDING_GYRI,
                                     BRODMANN_ADJACENCY,
                                     RETINOTOPIC_ROLE, EXTENT,
                                     VARIANTS, SUBDIVISIONS,
                                     CONNECTIVITY
        The derived GYRUS_TO_SULCI and BRODMANN_TO_SULCI indices
        The RETINOTOPIC_ROLE_INDEX
        The FORWARD_REFERENCE_SULCI list
        The FORWARD_REFERENCE_GYRI list

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        SULCUS_HEMIFIELD       **all "left"** (right) vs
                               **all "right"** (left) — the
                               occipital sulci bound territories
                               that represent the contralateral
                               visual hemifield.
        CLINICAL_ANCHORS       right: the calcarine sulcus is the
                               surface landmark for the
                               right V1 (which processes the
                               LEFT hemifield); its lesions
                               produce **left homonymous
                               hemianopia**; the lunate
                               sulcus, when present, marks
                               the **left** hemifield's
                               V1 / V2 border; the transverse
                               occipital sulcus bounds the
                               right lateral occipital gyrus
                               (which feeds the right FFA via
                               the right LOC).
                               left: the calcarine sulcus is
                               the surface landmark for the
                               left V1 (which processes the
                               RIGHT hemifield); its lesions
                               produce **right homonymous
                               hemianopia**; the lunate
                               sulcus, when present, marks
                               the **right** hemifield's
                               V1 / V2 border; the transverse
                               occipital sulcus bounds the
                               left lateral occipital gyrus
                               (which feeds the left VWFA
                               via the left LOC).

**The sulcal topology (BOUNDING_GYRI, BRODMANN_ADJACENCY, the
derived indices, RETINOTOPIC_ROLE_INDEX, and the forward-reference
lists) is byte-identical on both sides.**

**The SULCUS_HEMIFIELD and CLINICAL_ANCHORS are the only fields
that diverge** — and they diverge in exactly one direction: **the
contralateral visual hemifield**.

**The FORWARD_REFERENCE_SULCI list and the FORWARD_REFERENCE_GYRI
list are byte-identical on both sides** and must not be allowed to
drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/sulci/`` (right) — a
    sibling of ``brodmann_areas``, ``cortex``, ``cuneus``, and
    ``gyri``.
[ ] The three current sulci (calcarine, lunate, transverse
    occipital) are imported and registered.
[ ] ``SULCI_CHILDREN`` is byte-identical to the left sibling's.
[ ] Each child's BOUNDING_GYRI, BRODMANN_ADJACENCY,
    RETINOTOPIC_ROLE, EXTENT, VARIANTS, and SUBDIVISIONS are
    byte-identical to the left sibling's.
[ ] **The calcarine sulcus's BOUNDING_GYRI correctly names the
    cuneus (upper bank) and the lingual gyrus (lower bank,
    forward reference)** — both banks are V1 territory.
[ ] **The calcarine sulcus's BRODMANN_ADJACENCY is BA 17 on
    both banks.**
[ ] **The calcarine sulcus's RETINOTOPIC_ROLE is
    "horizontal_meridian_upper_lower_banks_dorsal_ventral_v1".**
[ ] **The lunate sulcus carries a PRESENCE_PROBABILITY field**
    (~0.5).
[ ] **The lunate sulcus's BOUNDING_GYRI correctly names the V2
    lateral territory (rostral bank) and the V1 lateral territory
    (caudal bank).**
[ ] **The lunate sulcus's BRODMANN_ADJACENCY is BA 18 (rostral)
    and BA 17 (caudal).**
[ ] **The transverse occipital sulcus's BOUNDING_GYRI correctly
    names the lateral occipital gyrus (ventral) and the angular
    gyrus (dorsal, parietal forward reference).**
[ ] **The transverse occipital sulcus's BRODMANN_ADJACENCY is
    BA 19 (ventral) and BA 39 (dorsal, parietal).**
[ ] ``GYRUS_TO_SULCI`` is present, derived from the children's
    BOUNDING_GYRI, tolerates the four forward-reference gyrus
    names, and is byte-identical to the left sibling's.
[ ] ``BRODMANN_TO_SULCI`` is present, derived from the children's
    BRODMANN_ADJACENCY, tolerates BA 39, and is byte-identical
    to the left sibling's.
[ ] ``RETINOTOPIC_ROLE_INDEX`` is present and byte-identical to
    the left sibling's — the **only manually-curated index in
    the package**.
[ ] ``SULCUS_HEMIFIELD`` is present with all three sulci
    assigned to "left" on the right side.
[ ] ``FORWARD_REFERENCE_SULCI`` lists the parieto-occipital
    sulcus and the lateral occipitotemporal sulcus, and is
    byte-identical to the left sibling's.
[ ] ``FORWARD_REFERENCE_GYRI`` lists the lingual gyrus, the
    angular gyrus, the V1 lateral territory, and the V2 lateral
    territory, and is byte-identical to the left sibling's.
[ ] **The parieto-occipital sulcus is documented as the medial
    boundary between the cuneus (occipital) and the precuneus
    (parietal)**, with its placement open.
[ ] **The lateral occipitotemporal sulcus is documented as the
    ventral boundary between the lateral occipital gyrus
    (occipital) and the fusiform gyrus (temporal)** — **on the
    right, the fusiform gyrus contains the right FFA**, so the
    sulcus is the surface boundary between the right LOC
    territory and the right FFA territory.
[ ] **The lingual gyrus is documented as a forward reference in
    ``..gyri``**, with the cuneus / lingual gyrus symmetry
    noted.
[ ] **The angular gyrus is documented as a parietal forward
    reference** (to be created under ``..parietal/gyri``).
[ ] **The V1 lateral territory and V2 lateral territory are
    documented as sub-regions**, not standalone gyrus packages.
[ ] **The duality contract is documented with the three
    occipital special cases**: calcarine / lingual gyrus duality,
    lunate sulcus conditional presence, transverse occipital
    lobar boundary.
[ ] **The occipital sulci's uniqueness among the cortical lobes
    is documented**: the calcarine sulcus defines a primary
    sensory area with an architectonically visible boundary and
    a specific retinotopic meridian at its fundus.
[ ] **The occipital pole's lack of a dedicated sulcus is
    documented.**
[ ] Every child's own docstring follows the same template used
    in the left sibling's children, with the visual hemifield
    labels flipped.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (child names, BOUNDING_GYRI, BRODMANN_ADJACENCY, derived
    indices, RETINOTOPIC_ROLE_INDEX, forward references) match
    the left sibling; SULCUS_HEMIFIELD and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    sulci carry the left hemifield, and the left sulci carry
    the right hemifield.
[ ] **The forward references are byte-identical to the left
    sibling's** — the two forward-reference sulci and the four
    forward-reference gyrus names are the same on both sides.
[ ] **The right's V3A / MT/V5 dominance is documented** in the
    transverse occipital sulcus's clinical anchor and in the
    ``..cortex`` cross-reference — the right V3A and MT/V5 are
    the dominant motion and dorsal-attention substrates, and
    the right transverse occipital sulcus is the surface
    landmark for their vicinity.
[ ] **The right FFA downstream endpoint is documented** in the
    lateral occipitotemporal sulcus cross-reference — **on the
    right, the fusiform gyrus contains the right FFA**, and
    the lateral occipitotemporal sulcus is the surface boundary
    between the right LOC territory and the right FFA
    territory.
[ ] Any downstream code querying "what sulci are in the right
    occipital lobe?" must receive the three current sulci plus
    the two forward-reference sulci, with the forward
    references marked.
[ ] Any downstream code querying "what does the right
    calcarine sulcus represent retinotopically?" must receive
    "the horizontal meridian of the visual field, at the
    fundus of the sulcus."
[ ] Any downstream code querying "what visual hemifield does
    the right calcarine sulcus represent?" must receive "the
    LEFT visual hemifield" — the SULCUS_HEMIFIELD field is the
    source of truth.
[ ] Any downstream code querying "what does the right
    transverse occipital sulcus bound?" must receive "the
    right lateral occipital gyrus (ventral) and the angular
    gyrus (dorsal, parietal)."
[ ] Any downstream code assigning the parieto-occipital
    sulcus's placement must resolve it consistently across
    hemispheres — no asymmetric placement is permitted.
[ ] Any downstream code assigning the lateral
    occipitotemporal sulcus's placement must resolve it
    consistently across hemispheres — no asymmetric placement
    is permitted.
[ ] Any downstream code assigning the calcarine sulcus's V1
    lesion anchor must specify the **right** side produces
    **left homonymous hemianopia** and the **left** side
    produces **right homonymous hemianopia** — the two are
    mirror-opposite.
[ ] Any downstream code assigning the right face pathway must
    note that **the lateral occipitotemporal sulcus is the
    surface boundary between the right LOC territory and the
    right FFA territory** — the sulcus is the landmark for the
    LOC → FFA transition.
[ ] Any downstream code assigning motion-boundary or
    depth-from-motion processing must note that the **right
    transverse occipital sulcus is the surface landmark for
    the vicinity of V3A / V3B**, which on the right is the
    dominant motion and dorsal-attention substrate.
[ ] **The structural framing, the three occipital special
    cases, the forward references, and the manually-curated
    RETINOTOPIC_ROLE_INDEX are all byte-identical to the left
    sibling's** — they are properties of the occipital lobe's
    anatomy, not of the hemisphere.
"""