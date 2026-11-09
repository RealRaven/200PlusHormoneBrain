"""
Inferior Frontal Sulcus (IFS) — Right Hemisphere
=================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
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
``../../left/cortex/frontal/sulci/inferior_frontal_sulcus``. Structural
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

On the right hemisphere it is **deeper, longer, and more continuous**
than its left counterpart, and it is the dorsal boundary of the **right
frontal operculum** — the cortex that houses the right Broca homologue,
the right arcuate fasciculus cap, and the right inferior frontal
gyrus's affective-prosody and response-inhibition networks. It begins
caudally at the inferior precentral sulcus, runs forward and slightly
downward across the lateral convexity, and terminates rostrally in the
pars triangularis / pars orbitalis region of the right IFG.

Anatomically it is one of the three **principal frontal sulci**
(alongside the superior frontal sulcus and the precentral sulcus) that
parcellate the lateral frontal convexity into the three named frontal
gyri (IFG, MFG, SFG). Its topology — which gyri it separates, and which
Brodmann areas abut it — is identical to the left hemisphere's. What
differs is its geometry (deeper, more continuous) and its clinical
significance (prosody, inhibition, affective valuation, right
ventral-attention network rather than speech production and reading).

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

**This field is byte-identical to the left-hemisphere sibling.** Sulcal
topology — which gyrus lies on which side of which groove — is
hemisphere-invariant. Both ``..gyri.inferior_frontal_gyrus`` and
``..gyri.middle_frontal_gyrus`` on the right declare the IFS as one of
their boundaries in their own docstrings. The duality contract asserts
that this declaration is the exact inverse of the one above.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side      Brodmann areas abutting the sulcus
    ------    --------------------------------------------------------
    ventral   BA 44, BA 45, BA 47
    dorsal    BA 6, BA 8, BA 9, BA 46

Interpretation (right-hemisphere functional annotations):

    ventral (right IFG side)
        BA 44  pars opercularis  — prosodic-motor output / response
                                   inhibition
        BA 45  pars triangularis — non-literal language / discourse
                                   coherence
        BA 47  pars orbitalis    — humor / affective valuation /
                                   emotion regulation

    dorsal (right MFG side)
        BA 6   premotor strip (caudal end) — spatial action
                                           preparation
        BA 8   FEF (caudal-dorsal end) — reflexive saccade planning /
                                        reorienting to salience
        BA 9   dorsal MFG — spatial task-set maintenance
        BA 46  mid-DLPFC — visuospatial working-memory register

The IFS therefore separates the **ventral affective-prosodic /
pragmatic** subdivision of the right frontal lobe (BA 44/45/47) from
the **dorsal spatial-executive / attentional** subdivision
(BA 6/8/9/46). It is the surface landmark for the boundary between the
two great functional systems of the right lateral frontal cortex — a
structural analogue of the left IFS's boundary, but with
affective-spatial content in place of language-executive content.

**This field is byte-identical to the left-hemisphere sibling.** The
Brodmann-area adjacency is numerically symmetric across hemispheres;
the functional annotations above differ but the BA numbers do not.

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
        for a short distance before terminating. On the right, this
        junction is more reliably identifiable than on the left
        because the right IFS is more continuous.

    rostral end
        Terminates in the **pars triangularis / pars orbitalis
        region** of the right IFG, usually at the horizontal ramus
        of the lateral fissure. In many brains the rostral end of
        the IFS merges with the **lateral orbital sulcus** (a
        component of the compound ``orbital_sulcus``) as it curves
        onto the orbital surface.

**This field is byte-identical to the left-hemisphere sibling.** The
landmarks at each end are hemisphere-invariant; only their reliability
as surgical/imaging landmarks differs, and that is captured in
CLINICAL_ANCHORS, not here.

--------------------------------------------------------------------------------
VARIANTS (right-hemisphere specific)
--------------------------------------------------------------------------------

Approximate prevalences from the neuroimaging and post-mortem
literature. These numbers are **right-hemisphere estimates** — they
differ from the left-hemisphere estimates, which live in the left
sibling's docstring.

    continuous_branch           ~75 %
        The most common form: a single continuous sulcus from the
        precentral sulcus to the pars triangularis, uninterrupted
        along its length. **More common on the right (~75 %)** than
        on the left (~60 %) — the right IFS is generally more
        continuous.

    interrupted_branch          ~15 %
        The sulcus is interrupted by one or more **transverse frontal
        gyri** — small bridging gyri that connect the IFG and MFG
        across the sulcus. When this happens, the IFS is a series
        of separate segments rather than a single continuous groove.
        **Less common on the right (~15 %)** than on the left (~20 %).

    transverse_frontal_gyrus    ~10 %
        A bridging gyrus (also called the *gyrus transversus
        frontalis* or *gyrus intermedius*) connecting the right IFG
        and right MFG across the IFS. Often bilateral but **less
        common on the right (~10 %)** than on the left (~20 %) —
        one of the few frontal sulci where the left is more variable
        than the right. When present on the right, it is a corridor
        for short-range cortico-cortical connections between the
        ventral affective-prosodic network and the dorsal
        spatial-executive network.

    duplicated_branch           ~5 %
        A second parallel sulcus running alongside the main IFS,
        creating a slender intermediate gyrus between them. Rare
        but well documented. Slightly more common on the right
        than on the left in some cohorts.

    fused_with_orbital          ~5 %
        The rostral end of the IFS fuses smoothly with the lateral
        orbital sulcus, so that the boundary between the lateral
        frontal convexity and the orbital surface is a single
        continuous groove rather than two meeting sulci. **Less
        common on the right (~5 %)** than on the left (~10 %) —
        the right IFS more often terminates cleanly before the
        orbital surface.

These variants are **not** functional distinctions — they are
geometric ones. The BOUNDING_GYRI and BRODMANN_ADJACENCY fields do not
change across variants. Only the ``VARIANTS`` field records the
geometric differences, so that downstream code can query "is this
subject's right IFS continuous?" without hard-coding a single geometry.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_operculum_landmark
        The IFS is the **dorsal boundary of the right frontal
        operculum**. In awake craniotomy for right frontal
        resections, the IFS is the surface landmark for the
        superior margin of the right Broca homologue (BA 44 + BA
        45), which on the right carries affective prosody and
        response inhibition rather than speech production. Its
        depth and continuity determine how safely the right
        operculum can be retracted, and because the right IFS is
        more continuous than the left, it is a **more reliable
        surgical landmark**.

    right_arcuate_operculum
        The right arcuate fasciculus caps the right operculum
        beneath the IFS. Its dorsolateral surface is the floor of
        the sulcus in standard dissections. The right arcuate is,
        on average, **thinner and less continuous than the left**
        (consistent with the right hemisphere's non-dominant role
        in language), so the right IFS is a **less reliable**
        arcuate landmark than the left. Right-IFS-region damage
        can nonetheless interrupt the right arcuate and produce
        **affective aprosodia** (flat, monotone speech) and
        **impaired prosody perception**.

    right_ventral_attention_corridor
        The right IFS is the surface landmark for the corridor
        connecting the right IFG (prosody, inhibition) to the right
        FEF and right pre-SMA (reorienting, spatial action). The
        frontal aslant tract on the right runs beneath the caudal
        IFS and is a core component of the **right ventral
        attention network** — the stimulus-driven "circuit
        breaker" that reorients attention to salient events. This
        is a **right-lateralized** clinical anchor; the left IFS
        has no equivalent.

    right_amygdala_corridor
        The right pars orbitalis (BA 47) lies ventral to the
        rostral IFS and is densely connected to the right
        amygdala. Right-IFS-region damage that extends ventrally
        into BA 47 can disrupt **explicit emotion regulation**
        (reappraisal) and produce the affective disinhibition
        seen in right orbitofrontal / opercular lesions. This is
        a right-lateralized anchor; the left IFG's amygdala
        projection is sparser.

    right_operculum_surgical_corridor
        The right IFS is a **surgical corridor** for reaching the
        right insula and right basal ganglia without traversing
        the prosody-inhibition cortex. The *trans-sulcal* approach
        enters through the IFS rather than through the gyral
        surface, preserving the right IFG's cortex while accessing
        the underlying insular and striatal structures — the
        right-hemisphere counterpart of the left trans-sulcal
        approach, but with prosody/inhibition preservation as the
        surgical goal rather than language preservation.

    prosody_network_anatomical_correlate
        Right-hemisphere IFS depth and continuity have been
        associated with **affective prosody perception** in
        developmental studies; the transverse frontal gyrus variant
        on the right has been associated with reduced prosody
        accuracy, possibly because it alters the short-range
        connectivity between the ventral affective-prosodic network
        and the dorsal spatial-executive network. This is the
        right-hemisphere analogue of the left IFS's dyslexia
        correlate.

These anchors are **right-hemisphere-specific**: the corresponding
left-hemisphere anchors (Broca's-area landmark, aslant-tract corridor,
left-arcuate operculum, surgical corridor for language preservation,
dyslexia correlate) are documented in the left sibling's docstring.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus)
--------------------------------------------------------------------------------

A sulcus is not a connective structure — it is a groove, not a tract.
But a sulcus *is* a **surface landmark for the white-matter bundles
that pass beneath it**, and those bundles must be recorded so that
downstream code can query "what runs under this sulcus?" without
re-deriving it from first principles.

    arcuate_fasciculus (dorsal segment, right)
        → caps_right_operculum
        The right arcuate's dorsal segment runs immediately
        beneath the right IFS at the caudal end of the sulcus,
        capping the right operculum. **Thinner and less continuous
        than the left arcuate** — the right IFS is therefore a
        less reliable arcuate landmark than the left IFS. On the
        right, the arcuate carries acoustic-to-prosodic mapping
        rather than sound-to-articulation mapping.

    frontal_aslant_tract (right)
        → traverses_beneath_caudal_right_ifs
        → right_pre_supplementary_motor_area
        → right_pars_opercularis_of_ifg
        The right aslant tract crosses beneath the right IFS at its
        caudal end, connecting the right medial frontal motor strip
        to the right ventral prosody-motor cortex. It is a core
        component of the right ventral attention network.

    superior_longitudinal_fasciculus III (SLF III, right)
        → caps_right_operculum
        → right_inferior_parietal_lobule
        The right SLF III runs beneath the caudal right IFS and
        continues posteriorly to the right inferior parietal
        lobule. **Thinner on the right than on the left.** On the
        right it carries prosodic working memory and spatial
        attention rather than the left's phonological working
        memory.

    uncinate_fasciculus (right)
        → traverses_beneath_rostral_right_ifs
        → right_anterior_temporal_lobe
        The right uncinate's frontal segment passes beneath the
        rostral right IFS (in the pars triangularis / pars
        orbitalis region), connecting the right ventral
        affective-pragmatic network to the right anterior temporal
        lobe. On the right, it carries socio-emotional meaning
        rather than the left's semantic control.

    extreme_capsule (right)
        → traverses_beneath_right_ifs
        → right_insula (anterior)
        The right extreme capsule runs from the right IFG across
        the right insula; its frontal origin lies beneath the
        right IFS.

    short-range U-fibres (transverse_frontal_gyrus variant only, right)
        → connects_right_ifg_to_right_mfg
        When the right transverse frontal gyrus is present, short
        U-fibres run *through* the bridging gyrus, connecting the
        right IFG and right MFG across the IFS. This is the only
        case in which a bundle crosses the sulcus itself rather
        than running beneath it.

    amygdala projections (right, via ventral IFG)
        → right_basolateral_nuclei
        → right_central_nucleus
        The right pars orbitalis (BA 47) sends a **dense**
        projection to the right amygdala, passing beneath the
        rostral right IFS. This is the anatomical substrate of the
        right IFS's role in emotion regulation and affective
        disinhibition. **Denser on the right than on the left.**

These entries are **right-hemisphere-specific** in two respects:
(a) the right arcuate and SLF III are thinner and less continuous than
the left's, making the right IFS a less reliable landmark for them;
(b) the right amygdala projection from pars orbitalis is denser than
the left's, making the right IFS a more reliable landmark for the
emotion-regulation corridor.

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
    as its **dorsal** boundary. On the right these BAs carry
    prosody (BA 44), non-literal language (BA 45), and affective
    valuation (BA 47) rather than their left-hemisphere roles.
    (Note: the BA 44/45/47 packages live under
    ``frontal/brodmann_areas/`` and are not yet modelled in the
    current tree; the forward references are reserved here so that
    they can be wired up when the BA packages are created.)

..brodmann_areas.brodmann_area_6
..brodmann_areas.brodmann_area_8
..brodmann_areas.brodmann_area_9
..brodmann_areas.brodmann_area_46
    The dorsal BAs. Each of these packages must declare the IFS
    as its **ventral** boundary. On the right these BAs carry
    spatial action preparation (BA 6), reflexive saccade
    planning (BA 8), spatial task-set maintenance (BA 9), and
    visuospatial working memory (BA 46). (Note: BA 9 and BA 46
    live under the MFG's BRODMANN_AREAS; BA 6 and BA 8 are
    shared between MFG and SFG — see the MFG and SFG docstrings
    for the canonical-home conventions.)

..cortex.prefrontal_cortex
    The IFS separates the ventral vlPFC (BA 47) from the dorsal
    DLPFC (BA 9, BA 46). On the right, this is the boundary
    between the affective-valuation subdivision and the spatial-
    executive subdivision of the DLPFC. The prefrontal_cortex
    package must declare the IFS as the **surface boundary**
    between these two functional subdivisions.

..cortex.premotor_cortex
    The caudal end of the IFS abuts the premotor strip (BA 6)
    and the FEF (BA 8). On the right, the FEF is the dominant
    node of the ventral attention network. The premotor_cortex
    package must declare the IFS as a **surface landmark** for
    its ventral margin.

..cortex.supplementary_motor_cortex
    The right pre-SMA (medial BA 6) projects via the frontal
    aslant tract to the right pars opercularis, passing beneath
    the caudal right IFS. The supplementary_motor_cortex package
    must declare this corridor.

../../subcortical/basal_ganglia/striatum/dorsal_striatum
    The corticostriatal projections from the right IFG and right
    MFG pass beneath the right IFS en route to the right caudate
    and putamen. The striatum package must declare the IFS as a
    landmark for the **corticostriatal corridor** between the
    ventral affective-prosodic cortex and the dorsal spatial-
    executive cortex.

../../subcortical/medial_temporal_lobe/amygdala
    The right pars orbitalis (BA 47) sends a **dense** projection
    to the right amygdala, passing beneath the rostral right IFS.
    This is the anatomical substrate of the right IFS's emotion-
    regulation role. The amygdala package must declare the right
    IFS as one of its cortical-landmark corridors, and must note
    that the projection is denser on the right than on the left.

../../left/cortex/frontal/sulci/inferior_frontal_sulcus
    The left-hemisphere homologue. Structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    EXTENT, SUBDIVISIONS) MUST be byte-identical to this package.
    Geometric and clinical fields (VARIANTS, CLINICAL_ANCHORS,
    CONNECTIVITY) are EXPECTED to differ — the right IFS is
    deeper, more continuous, and less variable; its clinical
    anchors are prosody-network, right-arcuate, right-operculum,
    and right-amygdala rather than Broca's-area and aslant-tract.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "inferior_frontal_sulcus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to left
                              "ventral": ("inferior_frontal_gyrus",),
                              "dorsal":  ("middle_frontal_gyrus",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "ventral": (44, 45, 47),
                              "dorsal":  (6, 8, 9, 46),
                          }

    EXTENT              = {                          # identical to left
                              "caudal":  ("inferior_precentral_sulcus",
                                          "precentral_sulcus"),
                              "rostral": ("pars_triangularis",
                                          "pars_orbitalis"),
                          }

    VARIANTS            = (                          # DIFFERS from left
                              "continuous_branch_~75%",
                              "interrupted_branch_~15%",
                              "transverse_frontal_gyrus_~10%",
                              "duplicated_branch_~5%",
                              "fused_with_orbital_~5%",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from left
                              "right_operculum_landmark",
                              "right_arcuate_operculum",
                              "right_ventral_attention_corridor",
                              "right_amygdala_corridor",
                              "right_operculum_surgical_corridor",
                              "prosody_network_anatomical_correlate",
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
right-IFG connectivity — the promotion takes this form:

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
  4. Mirror the promotion on the left side in the same commit — no
     asymmetric subdivision is permitted.

**Boundary-segment caveat**: if a segment split is proposed, the
**caudal segment** must still meet the inferior precentral sulcus at
its caudal end, and the **rostral segment** must still terminate in
the pars triangularis / pars orbitalis region. The EXTENT field at the
parent level records the two end landmarks; each segment inherits the
one at its respective end.

**Duality caveat**: a segment split must NOT break the duality
contract with ``..gyri``. The right IFG and right MFG declare the IFS
as a whole as their boundary — they do not declare ``pars_anterior``
and ``pars_posterior`` separately. The parent package therefore remains
the canonical boundary partner for both gyri, and the segments are
**internal refinements**, not new boundary partners. If a future
parcellation decides the gyri should declare segments directly, that
is a joint change across three packages (IFG, MFG, IFS) and must be
made in the same commit, in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../inferior_frontal_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME          "inferior_frontal_sulcus"
        LOBE                 "frontal"
        BOUNDING_GYRI        the same IFG ↔ MFG boundary
        BRODMANN_ADJACENCY   the same BA 44/45/47 ↔ BA 6/8/9/46
        EXTENT               the same two end landmarks
        SUBDIVISIONS         both empty (or both non-empty in the
                             same way, if a segment split is ever
                             done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "right" vs "left"
        VARIANTS             right: ~75% continuous, ~15%
                             interrupted, ~10% transverse frontal
                             gyrus, ~5% duplicated, ~5% fused with
                             orbital;
                             left: ~60% continuous, ~20% interrupted,
                             ~20% transverse frontal gyrus, ~5%
                             duplicated, ~10% fused with orbital.
                             (Right is the more continuous, less
                             variable hemisphere for this sulcus.)
        CLINICAL_ANCHORS     right: prosody-network corridor,
                             right-arcuate/operculum landmark,
                             right ventral-attention corridor,
                             right amygdala corridor, right
                             operculum surgical corridor, prosody
                             anatomical correlate;
                             left: Broca's-area landmark,
                             frontal-aslant-tract corridor,
                             arcuate/operculum landmark, surgical
                             corridor for language preservation,
                             dyslexia correlate.
        CONNECTIVITY         right: right arcuate (thinner), right
                             SLF III (thinner), right uncinate,
                             right extreme capsule, right
                             transverse U-fibres, and the **right
                             amygdala projection** from pars
                             orbitalis (denser than the left's);
                             left: left arcuate, left SLF III,
                             left uncinate, left extreme capsule,
                             left transverse U-fibres — without
                             the dense amygdala entry.

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

[ ] SULCUS_NAME is exactly "inferior_frontal_sulcus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BOUNDING_GYRI is byte-identical to the left sibling:
    {"ventral": ("inferior_frontal_gyrus",),
     "dorsal":  ("middle_frontal_gyrus",)}.
[ ] BOUNDING_GYRI names exactly two gyri, both present in the right
    ``..gyri.GYRI``.
[ ] BRODMANN_ADJACENCY is byte-identical to the left sibling:
    {"ventral": (44, 45, 47), "dorsal": (6, 8, 9, 46)}.
[ ] Every BA in BRODMANN_ADJACENCY appears in some gyrus's
    BRODMANN_AREAS in the right ``..gyri`` package.
[ ] EXTENT is byte-identical to the left sibling.
[ ] SUBDIVISIONS is empty and byte-identical to the left sibling.
[ ] VARIANTS documents the RIGHT-hemisphere prevalences
    (continuous ~75 %, interrupted ~15 %, transverse frontal gyrus
    ~10 %, duplicated ~5 %, fused with orbital ~5 %), and these
    differ from the left sibling's prevalences.
[ ] CLINICAL_ANCHORS contains the six right-specific anchors:
    right_operculum_landmark, right_arcuate_operculum,
    right_ventral_attention_corridor, right_amygdala_corridor,
    right_operculum_surgical_corridor,
    prosody_network_anatomical_correlate.
[ ] CONNECTIVITY contains the seven right-specific bundle entries
    (right arcuate, right aslant, right SLF III, right uncinate,
    right extreme capsule, right transverse U-fibres, **right
    amygdala projection** — the last being right-only).
[ ] Every CONNECTIVITY target is either a real package in the tree
    or a documented forward reference.
[ ] Both ``..gyri.inferior_frontal_gyrus`` and
    ``..gyri.middle_frontal_gyrus`` on the right declare the IFS as
    one of their boundaries — the duality contract passes.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT,
    SUBDIVISIONS) match the left sibling; geometric and clinical
    fields (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) deliberately
    differ.
[ ] No asymmetric SUBDIVISIONS promotion has been done without the
    left sibling.
[ ] The right-only amygdala projection (CONNECTIVITY:
    "amygdala_projections") is absent from the left sibling's
    CONNECTIVITY dict — this asymmetry is intentional and is
    documented in both packages.
[ ] The duality caveat in the PROMOTION RULE is documented: if the
    IFS is ever segmented, the parent remains the canonical
    boundary partner for IFG and MFG, in both hemispheres.
"""