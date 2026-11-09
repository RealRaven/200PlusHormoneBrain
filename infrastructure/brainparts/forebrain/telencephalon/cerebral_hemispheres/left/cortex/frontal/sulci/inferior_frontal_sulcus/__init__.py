"""
Inferior Frontal Sulcus (IFS) — Left Hemisphere
================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── frontal
                              └── sulci
                                    └── inferior_frontal_sulcus   ← THIS PACKAGE

This is a **leaf sulcus** package: it has no child packages. A sulcus
is an *edge*, not a *node* — it does not subdivide further. If a future
parcellation scheme splits the IFS into an anterior and a posterior
segment (some atlases do — see the VARIANTS and PROMOTION RULE
sections), those segments become ``SUBDIVISIONS`` entries here, not
nested folders, unless the split becomes anatomically load-bearing
enough to warrant separate packages.

Parent: ``..sulci`` — sibling to ``olfactory_sulcus``,
``orbital_sulcus``, ``paracentral_sulcus``, ``precentral_sulcus``, and
``superior_frontal_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/frontal/sulci/inferior_frontal_sulcus``. Structural
fields (SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, SUBDIVISIONS)
are identical by contract; geometric and clinical fields (VARIANTS,
CLINICAL_ANCHORS, CONNECTIVITY) diverge by design.

--------------------------------------------------------------------------------
WHAT THE IFS IS
--------------------------------------------------------------------------------

The inferior frontal sulcus is a **horizontal sulcus** running
caudo-rostrally across the lateral convexity of the frontal lobe. It is
the groove **between the inferior frontal gyrus (ventral) and the
middle frontal gyrus (dorsal)** — the single most important surface
landmark of the frontal operculum.

It is the dorsal boundary of Broca's area on the left hemisphere. It
begins caudally at the inferior precentral sulcus, runs forward and
slightly downward across the lateral convexity, and terminates
rostrally in the pars triangularis / pars orbitalis region of the IFG,
where it often fuses with the lateral orbital sulcus or simply fades
into the orbital surface.

Anatomically it is one of the three **principal frontal sulci**
(alongside the superior frontal sulcus and the precentral sulcus) that
parcellate the lateral frontal convexity into the three named frontal
gyri (IFG, MFG, SFG).

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction   Gyrus(es) bounded
    ---------   --------------------------------------------------------
    ventral     inferior_frontal_gyrus
    dorsal      middle_frontal_gyrus

The IFS is a **simple, two-sided sulcus** — it separates exactly one
pair of gyri along its entire length. (This is unlike the compound
``orbital_sulcus``, which has three or four boundary pairs, or the
``precentral_sulcus``, which separates MFG *and* SFG from the precentral
gyrus. The IFS is the cleanest two-sided sulcus in the frontal lobe.)

Both ``..gyri.inferior_frontal_gyrus`` and
``..gyri.middle_frontal_gyrus`` declare the IFS as one of their
boundaries in their own docstrings. The duality contract asserts that
this declaration is the exact inverse of the one above.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side      Brodmann areas abutting the sulcus
    ------    --------------------------------------------------------
    ventral   BA 44, BA 45, BA 47
    dorsal    BA 6, BA 8, BA 9, BA 46

Interpretation:

    ventral (IFG side)
        BA 44  pars opercularis  — speech-motor output / phonological
                                   assembly
        BA 45  pars triangularis — syntactic processing / semantic
                                   control
        BA 47  pars orbitalis    — semantic retrieval / affective
                                   valuation

    dorsal (MFG side)
        BA 6   premotor strip (caudal end) — action preparation
        BA 8   FEF (caudal-dorsal end) — saccade planning
        BA 9   dorsal MFG — task-set maintenance
        BA 46  mid-DLPFC — working-memory register

The IFS therefore separates the **ventral language / valuation**
subdivision of the frontal lobe (BA 44/45/47) from the **dorsal
executive / attentional** subdivision (BA 6/8/9/46). It is the
surface landmark for the boundary between the two great functional
systems of the lateral frontal cortex.

This adjacency is **many-to-many**: the sulcus separates seven Brodmann
areas across its two sides, and any single BA on one side can touch
multiple BAs on the other side at different points along the sulcus.
The mapping must therefore live in the child's ``BRODMANN_ADJACENCY``
dict as a per-side tuple, not as a single-valued index.

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    caudal end
        Meets the **inferior precentral sulcus** (the inferior
        continuation of the precentral sulcus, or the precentral
        sulcus proper when the latter is not subdivided). In some
        brains the meeting point is a T-junction; in others the IFS
        turns caudally and runs parallel to the precentral sulcus
        for a short distance before terminating.

    rostral end
        Terminates in the **pars triangularis / pars orbitalis
        region** of the IFG, usually at the horizontal ramus of the
        lateral fissure. In many brains the rostral end of the IFS
        merges with the **lateral orbital sulcus** (a component of
        the compound ``orbital_sulcus``) as it curves onto the
        orbital surface.

The IFS therefore runs the full anteroposterior extent of the lateral
frontal convexity's middle strip — from the precentral sulcus caudally
to the pars triangularis rostrally.

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

Approximate prevalences from the neuroimaging and post-mortem
literature. These numbers are **left-hemisphere estimates** — the
right-hemisphere estimates differ and live in the right sibling's
docstring.

    continuous_branch           ~60 %
        The most common form: a single continuous sulcus from the
        precentral sulcus to the pars triangularis, uninterrupted
        along its length.

    interrupted_branch          ~20 %
        The sulcus is interrupted by one or more **transverse frontal
        gyri** — small bridging gyri that connect the IFG and MFG
        across the sulcus. When this happens, the IFS is a series
        of separate segments rather than a single continuous groove.
        This variant is **more common on the left (~20 %)** than on
        the right (~10 %) — one of the few frontal sulci where the
        left is more variable than the right.

    transverse_frontal_gyrus    ~20 %
        A bridging gyrus (also called the *gyrus transversus
        frontalis* or *gyrus intermedius*) connecting the IFG and
        MFG across the IFS. Often bilateral but more common on the
        left. Functionally it is a corridor for short-range
        cortico-cortical connections between the ventral language
        network and the dorsal executive network.

    duplicated_branch           ~5 %
        A second parallel sulcus running alongside the main IFS,
        creating a slender intermediate gyrus between them. Rare
        but well documented.

    fused_with_orbital          ~10 %
        The rostral end of the IFS fuses smoothly with the lateral
        orbital sulcus, so that the boundary between the lateral
        frontal convexity and the orbital surface is a single
        continuous groove rather than two meeting sulci.

These variants are **not** functional distinctions — they are
geometric ones. The BOUNDING_GYRI and BRODMANN_ADJACENCY fields do not
change across variants. Only the ``VARIANTS`` field records the
geometric differences, so that downstream code can query "is this
subject's IFS continuous?" without hard-coding a single geometry.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    broca_operculum_landmark
        The IFS is the **dorsal boundary of Broca's area**. In
        awake craniotomy for left frontal resections, the IFS is
        the surface landmark for the superior margin of Broca's
        area (BA 44 + BA 45), and its depth and continuity
        determine how safely the operculum can be retracted.

    frontal_aslant_tract_corridor
        The frontal aslant tract — the white-matter bundle that
        connects the pre-SMA (medial SFG) to the pars opercularis
        of the IFG — passes **beneath the IFS** at its caudal end.
        The IFS is therefore the surface landmark for the
        aslant-tract corridor, and damage to this corridor (during
        resection or stroke) produces the classic *apraxia of
        speech* — loss of the ability to initiate speech despite
        intact language comprehension and articulation.

    arcuate_fasciculus_operculum
        The arcuate fasciculus caps the left operculum beneath the
        IFS. Its dorsolateral surface is the floor of the sulcus
        in standard dissections. This is why left-IFS-region
        damage can produce conduction aphasia — the arcuate is
        interrupted even though Broca's area (ventral to the
        sulcus) is intact.

    surgical_corridor
        The IFS is a surgical corridor for reaching the insula and
        the basal ganglia without traversing the language cortex.
        The *trans-sulcal* approach enters through the IFS rather
        than through the gyral surface, preserving the IFG's
        cortex while accessing the underlying insular and striatal
        structures.

    dyslexia_anatomical_correlate
        Left-hemisphere IFS depth and continuity have been
        associated with reading skill in developmental studies;
        the transverse frontal gyrus variant is more common in
        poor readers, possibly because it alters the short-range
        connectivity between the ventral language network and the
        dorsal executive network.

These anchors are **left-hemisphere-specific**: the corresponding
right-hemisphere anchors (prosody-network corridor, right-arcuate
operculum, etc.) are documented in the right sibling's docstring.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus)
--------------------------------------------------------------------------------

A sulcus is not a connective structure — it is a groove, not a tract.
But a sulcus *is* a **surface landmark for the white-matter bundles
that pass beneath it**, and those bundles must be recorded so that
downstream code can query "what runs under this sulcus?" without
re-deriving it from first principles.

    arcuate_fasciculus (dorsal segment)
        → caps_operculum (left)
        The left arcuate's dorsal segment runs immediately
        beneath the IFS at the caudal end of the sulcus, capping
        the left operculum. This is the anatomical substrate of
        the IFS's status as a conduction-aphasia landmark.

    frontal_aslant_tract
        → traverses_beneath_caudal_ifs (left)
        → pre_supplementary_motor_area
        → pars_opercularis_of_ifg
        The aslant tract crosses beneath the IFS at its caudal
        end, connecting the medial frontal motor strip to the
        ventral speech-motor cortex.

    superior_longitudinal_fasciculus III (SLF III)
        → caps_operculum (left)
        → inferior_parietal_lobule
        The SLF III runs beneath the caudal IFS and continues
        posteriorly to the inferior parietal lobule, forming the
        dorsal language pathway.

    uncinate_fasciculus
        → traverses_beneath_rostral_ifs (left)
        → anterior_temporal_lobe
        The uncinate's frontal segment passes beneath the rostral
        IFS (in the pars triangularis / pars orbitalis region),
        connecting the ventral language network to the anterior
        temporal lobe.

    extreme_capsule
        → traverses_beneath_ifs (left)
        → insula (anterior)
        The extreme capsule runs from the IFG across the insula;
        its frontal origin lies beneath the IFS.

    short-range U-fibres (transverse_frontal_gyrus variant only)
        → connects_ifg_to_mfg (left)
        When the transverse frontal gyrus is present, short
        U-fibres run *through* the bridging gyrus, connecting
        the IFG and MFG across the IFS. This is the only case
        in which a bundle crosses the sulcus itself rather than
        running beneath it.

These entries are **left-hemisphere-specific** in two respects:
(a) the left arcuate and SLF III are thicker and more continuous
than the right, making the IFS a more reliable landmark for them on
the left; (b) the left transverse frontal gyrus (when present) carries
different short-range connectivity than the right's, reflecting the
different functional roles of the IFG on each side.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri.inferior_frontal_gyrus
    The ventral bounding gyrus. Its docstring declares the IFS as
    its dorsal boundary. The duality contract asserts this
    declaration is the exact inverse of BOUNDING_GYRI here.

..gyri.middle_frontal_gyrus
    The dorsal bounding gyrus. Its docstring declares the IFS as
    its ventral boundary. The duality contract asserts this
    declaration is the exact inverse of BOUNDING_GYRI here.

..sulci.precentral_sulcus
    The caudal neighbour. The IFS meets the inferior precentral
    sulcus at its caudal end (see EXTENT). The two sulci are
    distinct — the precentral sulcus separates MFG/SFG from the
    precentral gyrus, while the IFS separates IFG from MFG — but
    they share a T-junction.

..sulci.orbital_sulcus
    The rostral-ventral neighbour. The rostral end of the IFS
    often fuses with the lateral orbital sulcus (a component of
    the compound orbital sulcus). When this fusion is present
    (VARIANTS: fused_with_orbital), the two sulci form a single
    continuous groove.

..brodmann_areas.brodmann_area_44
..brodmann_areas.brodmann_area_45
..brodmann_areas.brodmann_area_47
    The ventral BAs. Each of these packages must declare the IFS
    as its **dorsal** boundary. (Note: the BA 44/45/47 packages
    live under ``frontal/brodmann_areas/`` and are not yet
    modelled in the current tree; the forward references are
    reserved here so that they can be wired up when the BA
    packages are created.)

..brodmann_areas.brodmann_area_6
..brodmann_areas.brodmann_area_8
..brodmann_areas.brodmann_area_9
..brodmann_areas.brodmann_area_46
    The dorsal BAs. Each of these packages must declare the IFS
    as its **ventral** boundary. (Note: BA 9 and BA 46 live
    under the MFG's BRODMANN_AREAS; BA 6 and BA 8 are shared
    between MFG and SFG — see the MFG and SFG docstrings for the
    canonical-home conventions.)

..cortex.prefrontal_cortex
    The IFS separates the ventral vlPFC (BA 47) from the dorsal
    DLPFC (BA 9, BA 46). The prefrontal_cortex package must
    declare the IFS as the **surface boundary** between these
    two functional subdivisions.

..cortex.premotor_cortex
    The caudal end of the IFS abuts the premotor strip (BA 6)
    and the FEF (BA 8). The premotor_cortex package must declare
    the IFS as a **surface landmark** for its ventral margin.

../../subcortical/basal_ganglia/striatum/dorsal_striatum
    The corticostriatal projections from the IFG and MFG pass
    beneath the IFS en route to the caudate and putamen. The
    striatum package must declare the IFS as a landmark for
    the **corticostriatal corridor** between the ventral
    language cortex and the dorsal executive cortex.

../../right/cortex/frontal/sulci/inferior_frontal_sulcus
    The right-hemisphere homologue. Structural fields
    (SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    SUBDIVISIONS) MUST be byte-identical to this package.
    Geometric and clinical fields (VARIANTS, CLINICAL_ANCHORS,
    CONNECTIVITY) are EXPECTED to differ — the right IFS is
    deeper, more continuous, and less variable; its clinical
    anchors are prosody-network, right-arcuate, and
    right-operculum rather than Broca's-area and aslant-tract.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "inferior_frontal_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to left
                              "ventral": ("inferior_frontal_gyrus",),
                              "dorsal":  ("middle_frontal_gyrus",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "ventral": (44, 45, 47),
                              "dorsal":  (6, 8, 9, 46),
                          }

    EXTENT              = {
                              "caudal":  ("inferior_precentral_sulcus",
                                          "precentral_sulcus"),
                              "rostral": ("pars_triangularis",
                                          "pars_orbitalis"),
                          }

    VARIANTS            = (                          # DIFFERS from right
                              "continuous_branch_~60%",
                              "interrupted_branch_~20%",
                              "transverse_frontal_gyrus_~20%",
                              "duplicated_branch_~5%",
                              "fused_with_orbital_~10%",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "broca_operculum_landmark",
                              "frontal_aslant_tract_corridor",
                              "arcuate_fasciculus_operculum",
                              "surgical_corridor",
                              "dyslexia_anatomical_correlate",
                          )

    CONNECTIVITY        = { ... }   # as specified above

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "SULCUS_NAME",
        "HEMISPHERE",
        "LOBE",
        "BOUNDING_GYRI",
        "BRODMANN_ADJACENCY",
        "EXTENT",
        "VARIANTS",
        "CLINICAL_ANCHORS",
        "CONNECTIVITY",
        "SUBDIVISIONS",
    ]

Note: ``SUBDIVISIONS`` is an empty tuple — the IFS is a leaf sulcus.
The field is kept for uniformity with the parent ``..sulci`` package's
contract and must NOT be deleted; downstream code iterates
``SUBDIVISIONS`` unconditionally.

No behaviour. This package is a declarative descriptor; all computation
that references the IFS lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
PROMOTION RULE (when a sulcus segment becomes a package)
--------------------------------------------------------------------------------

A sulcus is an **edge**, not a **node**, so the standard promotion rule
(in which a child package is split off from a parent node) does not
directly apply. However, if a future parcellation scheme decides that
the IFS's anterior and posterior segments are anatomically load-bearing
enough to warrant separate packages — some atlases do split the IFS into
``pars_anterior`` and ``pars_posterior``, especially in studies of
Broca's-area connectivity — the promotion takes this form:

    inferior_frontal_sulcus/
        __init__.py
        pars_anterior/
            __init__.py
        pars_posterior/
            __init__.py

Then:

  1. Add "pars_anterior" and "pars_posterior" to this package's
     ``SUBDIVISIONS``.
  2. Keep ``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` at the parent
     level as the **union** of the segments' bounding relationships
     (the parent remains the canonical answer to "what does the IFS
     bound?"; the segments refine *which part* of the IFS bounds
     what).
  3. Each segment's ``__init__.py`` declares its own
     ``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` restricted to its
     anteroposterior extent.
  4. Mirror the promotion on the right side in the same commit — no
     asymmetric subdivision is permitted.

**Boundary-segment caveat**: if a segment split is proposed, the
**caudal segment** must still meet the inferior precentral sulcus at
its caudal end, and the **rostral segment** must still terminate in
the pars triangularis / pars orbitalis region. The EXTENT field at the
parent level records the two end landmarks; each segment inherits the
one at its respective end.

**Duality caveat**: a segment split must NOT break the duality
contract with ``..gyri``. The IFG and MFG declare the IFS as a whole
as their boundary — they do not declare ``pars_anterior`` and
``pars_posterior`` separately. The parent package therefore remains the
canonical boundary partner for both gyri, and the segments are
**internal refinements**, not new boundary partners. If a future
parcellation decides the gyri should declare segments directly, that
is a joint change across three packages (IFG, MFG, IFS) and must be
made in the same commit.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../inferior_frontal_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME          "inferior_frontal_sulcus"
        LOBE                 "frontal"
        BOUNDING_GYRI        the same IFG ↔ MFG boundary
        BRODMANN_ADJACENCY   the same BA 44/45/47 ↔ BA 6/8/9/46
        SUBDIVISIONS         both empty (or both non-empty in the
                             same way, if a segment split is ever
                             done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "left" vs "right"
        VARIANTS             left: ~20% transverse frontal gyrus,
                             ~60% continuous, ~20% interrupted;
                             right: ~10% transverse frontal gyrus,
                             ~75% continuous, ~15% interrupted.
                             (Left is the more variable hemisphere
                             for this sulcus; right is more
                             continuous.)
        CLINICAL_ANCHORS     left: Broca's-area landmark,
                             frontal-aslant-tract corridor,
                             arcuate/operculum landmark,
                             dyslexia correlate;
                             right: prosody-network corridor,
                             right-arcuate/operculum landmark,
                             right opercular surgical corridor.
        CONNECTIVITY         left: left arcuate, left SLF III,
                             left uncinate, left extreme capsule,
                             left transverse U-fibres;
                             right: right arcuate, right SLF III,
                             right uncinate, right extreme capsule,
                             right transverse U-fibres — with
                             subtly different bundle thicknesses
                             (right arcuate and SLF III are, on
                             average, slightly *thinner* than the
                             left's, consistent with the left's
                             language dominance).

Any deviation from the "MUST be identical" list is a bug — sulcal
*topology* (which gyrus is separated from which, and which Brodmann
areas abut the sulcus on each side) is hemisphere-invariant. Any
unexpected similarity in the "MUST differ" list is also a bug — if
left and right IFS end up with identical VARIANTS or CLINICAL_ANCHORS,
the hemisphere-specific geometric and clinical knowledge has not been
captured.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "inferior_frontal_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BOUNDING_GYRI is byte-identical to the right sibling:
    {"ventral": ("inferior_frontal_gyrus",),
     "dorsal":  ("middle_frontal_gyrus",)}.
[ ] BOUNDING_GYRI names exactly two gyri, both present in
    ``..gyri.GYRI``.
[ ] BRODMANN_ADJACENCY is byte-identical to the right sibling:
    {"ventral": (44, 45, 47), "dorsal": (6, 8, 9, 46)}.
[ ] Every BA in BRODMANN_ADJACENCY appears in some gyrus's
    BRODMANN_AREAS in the left ``..gyri`` package.
[ ] EXTENT is byte-identical to the right sibling (the two end
    landmarks are hemisphere-invariant).
[ ] SUBDIVISIONS is empty and byte-identical to the right sibling.
[ ] VARIANTS documents the LEFT-hemisphere prevalences
    (continuous ~60 %, interrupted ~20 %, transverse frontal gyrus
    ~20 %, duplicated ~5 %, fused with orbital ~10 %), and these
    differ from the right sibling's prevalences.
[ ] CLINICAL_ANCHORS contains the five left-specific anchors:
    broca_operculum_landmark, frontal_aslant_tract_corridor,
    arcuate_fasciculus_operculum, surgical_corridor,
    dyslexia_anatomical_correlate.
[ ] CONNECTIVITY contains the six left-specific bundle entries
    (arcuate dorsal segment, frontal aslant, SLF III, uncinate,
    extreme capsule, transverse U-fibres).
[ ] Every CONNECTIVITY target is either a real package in the tree
    (e.g. ``../../subcortical/basal_ganglia/striatum``) or a
    documented forward reference (e.g. BA 44/45/47 packages not
    yet created).
[ ] Both ``..gyri.inferior_frontal_gyrus`` and
    ``..gyri.middle_frontal_gyrus`` declare the IFS as one of
    their boundaries — the duality contract passes.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT,
    SUBDIVISIONS) match the right sibling; geometric and clinical
    fields (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) deliberately
    differ.
[ ] No asymmetric SUBDIVISIONS promotion has been done without the
    right sibling.
[ ] The duality caveat in the PROMOTION RULE is documented: if the
    IFS is ever segmented, the parent remains the canonical
    boundary partner for IFG and MFG.
"""