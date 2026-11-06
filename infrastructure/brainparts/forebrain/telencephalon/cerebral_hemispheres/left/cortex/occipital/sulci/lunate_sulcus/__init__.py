"""
Lunate Sulcus — Left Hemisphere
================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── sulci
                                    └── lunate_sulcus   ← THIS PACKAGE

This is a **leaf sulcus package** describing the left hemisphere's
**lunate sulcus** — the **inconstant lateral-surface sulcus** that,
**when present**, marks the **V1 / V2 border** on the lateral surface
of the occipital lobe. It is the **only occipital sulcus whose
presence is probabilistic** — present in roughly **40–60 % of
human brains** depending on the series — and it is the **only sulcus
in the entire cortex** that carries an explicit
``PRESENCE_PROBABILITY`` field below 1.0.

Parent: ``..sulci`` (left occipital sulci parent) — sibling to
``calcarine_sulcus`` and ``transverse_occipital_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/occipital/sulci/lunate_sulcus``. The sulcus
name, the bounding sub-regions (V1 lateral territory caudal, V2
lateral territory rostral), the Brodmann adjacency (BA 17 caudal,
BA 18 rostral), the vertical-meridian retinotopic role, the
**PRESENCE_PROBABILITY ≈ 0.5**, the extent landmarks, and the
connectivity (no major bundle beneath the sulcus) are identical on
both sides; the **represented visual hemifield** and the **clinical
significance** diverge — on the left, the lunate sulcus marks the
**RIGHT** hemifield's V1 / V2 border (when present), and left
lunate-based resections must account for the right-hemifield
vertical meridian. The right lunate sulcus marks the mirror
arrangement (left hemifield).

**The lunate sulcus is the LATERAL-surface counterpart to the
calcarine sulcus's MEDIAL-surface V1 / V2 border mark.** The
calcarine's V1 / V2 border is marked architectonically by the
**abrupt disappearance of the stria of Gennari** at the outer
margins of the calcarine banks — this is the primary,
architectonically unambiguous V1 / V2 boundary marker on the medial
surface. **The lunate sulcus, when present, is the surface groove
that marks approximately the same V1 / V2 border on the LATERAL
surface**, near the occipital pole. **When the lunate is absent**,
the V1 / V2 border is **still architectonically marked by the
stria of Gennari** — the stria's boundary is intact regardless of
whether the surface groove is present — but the boundary is **not
visible as a surface sulcus**.

**This asymmetry between medial and lateral V1 / V2 border markers
is a structural feature of the occipital lobe**, not a defect. The
medial V1 / V2 border (calcarine) is **always** marked by the
stria of Gennari; the lateral V1 / V2 border (lunate) is marked by
a sulcus **in about half of brains** and by the stria of Gennari
alone in the other half.

--------------------------------------------------------------------------------
WHAT THE LUNATE SULCUS IS
--------------------------------------------------------------------------------

The lunate sulcus is a **short, vertically oriented (or slightly
oblique) sulcus on the LATERAL surface of the occipital lobe**, near
the **occipital pole** — the lateral-surface counterpart to the
medial calcarine sulcus's V1 / V2 border. The name comes from the
Latin **luna** ("moon") — the sulcus is lunate-shaped (crescent-
shaped) in lateral view when present.

**When present**, the lunate sulcus separates:

    rostral bank       →  **V2 lateral territory** (the V2
                          extrastriate cortex lateral to the
                          occipital pole)
                          →  the **vertical meridian** on the
                             rostral side of the sulcus
                          →  the **higher-tier extrastriate**
                             side

    caudal bank        →  **V1 lateral territory** (the lateral
                          portion of the striate cortex near
                          the occipital pole)
                          →  the **vertical meridian** on the
                             caudal side of the sulcus
                          →  the **primary visual cortex**
                             side

**The lunate sulcus, when present, marks the VERTICAL MERIDIAN of
the visual field on the lateral surface.** The vertical meridian is
the boundary between the left and right halves of each hemifield's
representation — but in the context of a single hemisphere, it is
the boundary between V1's representation of the contralateral
hemifield and V2's representation of the same hemifield. **On the
left, the lunate sulcus marks the RIGHT hemifield's vertical
meridian.** **On the right, it marks the LEFT hemifield's vertical
meridian.**

**The stria of Gennari's abrupt disappearance** at the V1 / V2
border is the **architectonic signature** that is visible on both
banks of the lunate sulcus **when it is present**. The stria
disappears as one crosses from V1 (calcarine cortex) into V2
(extrastriate belt), and this disappearance is what makes the
V1 / V2 border architectonically unambiguous **regardless of
whether the lunate sulcus is present as a surface groove**.

**The lunate sulcus is inconstant.** It is **absent in roughly
40–60 % of human brains** depending on the series. **When absent**,
the lateral V1 / V2 border is **not visible as a surface sulcus** —
the transition from V1 to V2 is a gradual cortical transition
marked only by the stria of Gennari's disappearance, which is
visible histologically but not as a surface groove. **In the
absent case**, the lateral surface of the occipital lobe near the
pole is a relatively smooth transition from calcarine cortex (V1)
to extrastriate cortex (V2 / V3d / V4d), without a visible sulcal
boundary.

**Left-hemisphere specificity**: the left lunate sulcus, **when
present**, marks the **RIGHT** hemifield's V1 / V2 border on the
lateral surface of the left occipital lobe. **Left
lunate-based surgical resections** (for lesions near the occipital
pole, or for epilepsy surgery in the lateral occipital region)
must account for the **right-hemifield vertical meridian** — the
boundary between V1 (calcarine cortex) and V2 (extrastriate)
territory near the left occipital pole. **When the lunate is
absent**, the boundary must be inferred from the retinotopic map
or from the stria of Gennari (visible on fresh specimens or on
high-resolution histology), not from the surface sulcus.

**The left lunate sulcus is a secondary landmark for the left
V1 / V2 border** — its primary clinical relevance is as a
**retinotopic reference point** and as a **surgical landmark** for
resections that need to distinguish V1 (eloquent visual cortex)
from V2 (extrastriate, non-eloquent in the sense of primary
vision) on the lateral surface.

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction     Gyrus(es) bounded
    ---------     --------------------------------------------------------
    rostral       **V2 lateral territory** — the V2 extrastriate
                  cortex lateral to the occipital pole. **NOT a
                  standalone gyrus package** — it is a sub-region
                  of the **lateral occipital gyrus** (V2
                  territory).
    caudal        **V1 lateral territory** — the lateral portion
                  of the striate cortex near the occipital pole.
                  **NOT a standalone gyrus package** — it is a
                  sub-region of the **calcarine cortex** (V1
                  territory).

**This is the only sulcus in the cortex whose bounding "gyri" are
BOTH sub-regions, not standalone gyrus packages.** The lunate
sulcus separates V1's **lateral territory** (the caudal bank)
from V2's **lateral territory** (the rostral bank), and **neither
is a standalone gyrus**. V1's territory is the **calcarine banks
+ the lateral territory near the occipital pole** (a continuous
V1 territory that extends from the medial calcarine banks to the
lateral occipital pole). V2's territory is the **extrastriate
belt around V1 + the lateral occipital gyrus** (a continuous V2
territory that surrounds V1 and extends onto the lateral
surface).

**The lunate sulcus's bounding "gyri" are therefore sub-regions
of the calcarine cortex (V1) and the lateral occipital gyrus
(V2)**, not separate gyrus packages. **This is why the parent
``..sulci`` package's forward-reference list includes
`v1_lateral_territory` and `v2_lateral_territory`** — they are
documented as sub-regions, not as expected future gyrus packages.

**The duality contract for the lunate sulcus is therefore
sub-regional** — the sulcus bounds sub-regions of two existing
gyral / cortical territories (calcarine cortex for V1, lateral
occipital gyrus for V2), and the parent inversion function must
record this as a **sub-regional duality**, not a gyrus-package
duality.

**This field is byte-identical to the right sibling's** — the
bounding sub-regions are topological, not lateralized.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side          Brodmann area
    -----------   --------------------------------------------------------
    rostral bank  **BA 18** — the secondary visual cortex (V2)
    caudal bank   **BA 17** — the primary visual cortex (V1)

**The lunate sulcus separates BA 17 (V1) from BA 18 (V2) on the
lateral surface.** This is the same **V1 / V2 cytoarchitectonic
boundary** that the calcarine sulcus's outer margins mark on the
medial surface — but the lunate is **only present in ~half of
brains**, so the BA 17 / BA 18 border is **always
architectonically unambiguous** (marked by the stria of Gennari)
but **only sometimes visible as a surface sulcus** (the lunate).

**This is the only sulcus in the cortex whose Brodmann adjacency
is BA 17 / BA 18** — the calcarine sulcus has BA 17 on **both**
sides (V1 on both banks), the transverse occipital sulcus has BA
19 / BA 39, and the lunate is the only sulcus whose two sides
carry the **primary (BA 17) / secondary (BA 18)** transition.

**This field is byte-identical to the right sibling's.**

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    dorsal end
        Reaches the **lateral surface of the occipital lobe**,
        near the **transverse occipital sulcus** (or the
        occipito-parietal junction). The dorsal extent of the
        lunate varies with the size of the V1 lateral
        territory.

    ventral end
        Reaches the **lateral occipitotemporal sulcus** (or the
        occipito-temporal junction), near the ventral edge of
        the lateral occipital gyrus. The ventral extent of the
        lunate varies with the size of the V1 lateral
        territory.

**The lunate sulcus is a short sulcus** — it does not run the full
anteroposterior extent of the lateral surface, unlike the
transverse occipital sulcus (which is a lobar boundary) or the
calcarine sulcus (which runs the full anteroposterior extent of
the medial surface). **Its extent is limited to the
V1 / V2 border region near the occipital pole**, and it is
typically **2–4 cm long** when present.

**This field is byte-identical to the right sibling's**, except
for the anatomical variability of its exact endpoints when
present, which belongs in the child package's EXTENT dict (not
the parent's contract).

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

The lunate sulcus's **primary variant is presence / absence** —
it is the **only occipital sulcus whose presence is
probabilistic**.

    absent                         ~40–60 %
        **The most common variant is absence.** The lunate
        sulcus is **not present as a surface groove** in
        40–60 % of brains. In this case, the V1 / V2 border on
        the lateral surface is **marked only by the stria of
        Gennari's disappearance**, which is visible
        histologically but not as a surface sulcus.

    continuous_present             ~35 %
        The lunate sulcus is a **single, continuous groove**
        from its dorsal to its ventral end, marking the
        V1 / V2 border on the lateral surface. This is the
        **classic form** when the sulcus is present.

    fragmented_present             ~25 %
        The lunate sulcus is present but **broken into
        segments** by a small bridging gyrus, or it is
        **partially fused** with an adjacent sulcus (the
        transverse occipital sulcus dorsally, or the lateral
        occipitotemporal sulcus ventrally). This is the
        **variant form** when the sulcus is present.

    left_right_asymmetry           documented
        **The lunate sulcus's presence is roughly symmetric
        across hemispheres** (~50 % on both sides in most
        series), but **individual brains often show
        asymmetric presence** — the lunate may be present on
        one side and absent on the other. **Left-right
        asymmetry in lunate presence is a documented
        individual difference**, not a systematic hemisphere
        asymmetry. **Any such asymmetry in a given subject
        must be recorded in the subject-specific data**, not
        hard-coded in this package's VARIANTS field.

    striate_cortex_lateral_extension   always
        **The striate cortex (V1) extends to the lateral
        surface near the occipital pole regardless of the
        lunate's presence.** V1's lateral territory is
        **always** present — it is the surface **sulcus**
        that is inconstant, not the underlying cortex.
        **This is the invariant across all lunate variants**
        — the V1 / V2 border is always there, but it is only
        **sometimes** visible as a surface groove.

These variants are **geometric and presence/absence**, not
topological. The ``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY``
fields describe the sulcus **when it is present**. When absent,
the fields are **not applicable** — the V1 / V2 border exists
but is not marked by the sulcus. **Downstream code that queries
the lunate sulcus must check ``PRESENCE_PROBABILITY`` first** and
treat the sulcus's bounding relationships as **conditional on
presence**.

**The invariant across all variants is the stria of Gennari's
presence** — V1's lateral territory is **always** present, and
the V1 / V2 border is **always** architectonically unambiguous,
even when the lunate sulcus is absent.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_lunate_v1_v2_border_landmark
        **This is the left lunate sulcus's primary clinical
        anchor.** **When present**, the left lunate sulcus is
        the **surface landmark for the RIGHT hemifield's
        V1 / V2 border** on the lateral surface of the left
        occipital lobe. **Left lunate-based surgical
        resections** (for lesions near the occipital pole, or
        for epilepsy surgery in the lateral occipital region)
        must account for the **right-hemifield vertical
        meridian** — the boundary between V1 (eloquent visual
        cortex) and V2 (extrastriate) territory near the
        left occipital pole. **The lunate sulcus is the only
        surface landmark that marks this boundary on the
        lateral surface** — when it is present.

    left_lunate_conditional_landmark_absent_in_40pct
        **The left lunate sulcus's secondary clinical anchor
        — an ABSENCE anchor.** **When the lunate sulcus is
        absent** (~40–60 % of cases), **the lateral V1 / V2
        border is not visible as a surface sulcus**. The
        boundary must be inferred from the **retinotopic
        map** (using fMRI or other functional mapping) or
        from the **stria of Gennari** (visible on fresh
        specimens or high-resolution histology). **This
        anchor is a warning to downstream code and to
        surgeons**: the absence of the lunate sulcus is
        **not** a signal that the V1 / V2 border is absent
        — it is a signal that the boundary is not **visible
        as a surface groove**.

    left_lunate_surgical_landmark_for_v1_v2_border
        **The left lunate sulcus's surgical anchor.**
        **When present**, the left lunate sulcus is a
        surgical landmark for resections in the lateral
        occipital region that must **preserve V1** (the
        eloquent visual cortex) while resecting V2 or V3d
        territory. **When absent**, the surgeon must rely
        on intraoperative neurophysiological mapping
        (visual evoked potentials from the lateral
        occipital surface) rather than on the surface
        sulcus. **The lunate sulcus's inconstancy is a
        surgical planning consideration** — the surgeon
        must have a plan for both the present and absent
        cases.

    left_lunate_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from the lateral occipital region near the
        lunate sulcus. **The lunate sulcus is a surface
        landmark for the V1 / V2 border in the epileptogenic
        zone** when the seizure onset is in the lateral
        occipital cortex. **The lunate sulcus's inconstancy
        complicates the pre-surgical workup** — when the
        sulcus is absent, the epileptogenic zone must be
        mapped from the retinotopic and functional MRI
        rather than from the surface sulcus.

    left_lunate_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra
        that precede a migraine headache — reflects
        **cortical spreading depression** spreading across
        the calcarine and lateral occipital cortex.
        **The lunate sulcus, when present, is a surface
        landmark for the lateral V1 / V2 border where the
        spreading depression passes from V1 into V2** on
        the lateral surface. **This anchor is hemisphere-
        invariant**, but the aura's field involvement is
        contralateral (right field on the left side).

    left_lunate_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** can
        involve the lateral occipital cortex near the
        lunate sulcus and produce a **right homonymous
        hemianopia or quadrantic defect** with **right
        macular sparing**. **The lunate sulcus's
        contribution to the infarct's clinical signature
        is as a surface landmark for the boundary between
        V1 (eloquent) and V2 (non-eloquent) territory** in
        the lateral occipital region. **The lunate
        sulcus's inconstancy** means that the surface
        landmark is only available in ~half of cases; in
        the other half, the boundary must be inferred from
        the retinotopic map.

    left_lunate_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive
        visual dysfunction — involves the lateral occipital
        cortex including the lunate sulcus territory.
        **Left lunate** is part of the substrate of the
        progressive ventral stream dysfunction that
        produces progressive reading deficits in later-
        stage PCA.

**The lunate sulcus's clinical anchors are narrower than the
calcarine sulcus's** — the lunate is a **conditional landmark**
(when present) for the V1 / V2 border, not a primary field-defect
anchor. **The field-defect anchors** (right homonymous hemianopia,
macular sparing, etc.) belong to the **calcarine sulcus**, not
the lunate. **The lunate's anchors are focused on** the V1 / V2
border landmark function, the surgical planning considerations,
and the epileptogenic zone localization.

**The absence anchor** (`left_lunate_conditional_landmark_absent_
in_40pct`) is a **structural warning** — downstream code must
not assume the lunate sulcus is present, and must have a fallback
plan (retinotopic mapping, stria of Gennari) for cases where it
is absent.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, and occipital infarct — are **documented
identically in both siblings**, with the side-appropriate field
label. **The lunate-specific anchors** (`left_lunate_v1_v2_
border_landmark`, `left_lunate_conditional_landmark_absent_in_
40pct`, `left_lunate_surgical_landmark_for_v1_v2_border`) are
**left-hemisphere-specific in the sense that they mark the
RIGHT hemifield's V1 / V2 border** — the right hemifield is what
the left lateral occipital cortex represents.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    structures within / beneath the sulcus
        **No major white-matter bundle specifically associated
        with the lunate sulcus.** The optic radiation terminates
        more caudally at the occipital pole, in the calcarine
        banks. The pericalcarine white matter (short-range
        association fibers between V1 and V2) is **more
        medial**, along the calcarine sulcus. **The V1 / V2
        border that the lunate sulcus marks, when present, is a
        cortico-cortical transition (V1 to V2), not a white-
        matter tract boundary.**

    white-matter bundles in the vicinity (not specifically
    beneath the sulcus)
        **optic radiation** — terminates more caudally at the
        occipital pole
        **inferior longitudinal fasciculus** — runs laterally,
        in the white matter of the lateral occipital and
        temporal lobes, not specifically beneath the lunate
        sulcus

**The lunate sulcus has no major white-matter bundle beneath
it** — this is unlike the calcarine sulcus (which has the optic
radiation beneath it) or the transverse occipital sulcus (which
has the inferior longitudinal fasciculus beneath it). **The
lunate sulcus is a pure cortical-transition landmark** (V1 to
V2), not a white-matter landmark.

**This field is byte-identical to the right sibling's** — the
absence of a specific white-matter bundle beneath the lunate
sulcus is a property of the occipital lobe's white-matter
architecture, not of the hemisphere.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..sulci  (parent)
    The left occipital sulci parent. The lunate sulcus is one of
    its three current children.

..sulci.calcarine_sulcus
    The **medial-surface V1 / V2 border marker** — the primary,
    architectonically unambiguous V1 / V2 boundary marked by the
    **abrupt disappearance of the stria of Gennari** at the outer
    margins of the calcarine banks. **The lunate sulcus is the
    LATERAL-surface counterpart** to the calcarine's medial-
    surface V1 / V2 border mark — but where the calcarine's
    V1 / V2 border is **always** architectonically visible, the
    lunate's lateral V1 / V2 border is **only sometimes**
    visible as a surface sulcus.

..sulci.transverse_occipital_sulcus
    The **dorsal-surface sulcus** that bounds the lateral
    occipital gyri. **The lunate sulcus is ventral to the
    transverse occipital sulcus** and may partially fuse with
    it when both are present.

..gyri.lateral_occipital_gyrus
    The **lateral-surface gyral parent**. **The V2 lateral
    territory (the lunate's rostral bank) is a sub-region of the
    lateral occipital gyrus** — it is the V2 portion of the
    lateral occipital gyrus's functional overlays (which also
    include V3d, V4d, and LOC). **The lateral occipital gyrus
    does not have a standalone V2 sub-region as a child** —
    the V2 territory is **part of** the gyrus, not a separate
    package.

..gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The **V1 lateral territory (the lunate's caudal bank) is
    continuous with V1's medial territory** on the calcarine
    banks — the two are the same V1 cortex, connected over the
    occipital pole. **The lingual gyrus is the lower-bank
    portion of the medial V1 territory**, and the V1 lateral
    territory is the extension of V1 onto the lateral surface.

..brodmann_areas.brodmann_area_17_primary_visual
    The **V1 cytoarchitectonic counterpart** of the lunate
    sulcus's caudal bank. **BA 17's territory extends onto the
    lateral surface near the occipital pole**, and the lunate
    sulcus (when present) is the surface boundary between BA 17
    (V1) and BA 18 (V2) on the lateral surface.

..brodmann_areas.brodmann_area_18
    The **V2 cytoarchitectonic counterpart** of the lunate
    sulcus's rostral bank. **BA 18's territory extends onto the
    lateral surface as the V2 extrastriate belt**, and the
    lunate sulcus (when present) is the surface boundary between
    BA 17 and BA 18 on the lateral surface.

...cortex.primary_visual_cortex
    The **V1 functional counterpart** of the lunate sulcus's
    caudal bank. **V1's territory extends onto the lateral
    surface near the occipital pole**, and the lunate sulcus
    (when present) is the lateral-surface V1 / V2 border
    landmark.

...cortex.v2
    The **V2 functional counterpart** of the lunate sulcus's
    rostral bank. **V2's territory extends onto the lateral
    surface as the extrastriate belt**, and the lunate sulcus
    (when present) is the lateral-surface V1 / V2 border
    landmark.

...cortex.v3
    The **V3 territory** is further lateral and ventral to V2.
    **No direct adjacency to the lunate sulcus** — the lunate
    sulcus marks the V1 / V2 border, not the V2 / V3 border.

...cortex.v4
    **No direct adjacency to the lunate sulcus.** V4 is further
    lateral / ventral.

..cortex.temporal
    The **lateral occipitotemporal sulcus** (the ventral
    boundary of the lateral occipital gyrus, into the fusiform
    gyrus) is **ventral to the lunate sulcus**. **No direct
    adjacency** between the lunate sulcus and the temporal
    lobe — the temporal lobe is separated from the occipital by
    the lateral occipitotemporal sulcus, which is a separate
    sulcus.

..cortex.parietal
    The **transverse occipital sulcus** (the dorsal boundary of
    the lateral occipital gyrus) is **dorsal to the lunate
    sulcus**. **No direct adjacency** between the lunate sulcus
    and the parietal lobe.

..cortex.frontal
    **No direct sulcal adjacency.**

..cortex.cingulate
    **No direct sulcal adjacency.** The isthmus of the cingulate
    gyrus is at the rostral extent of the calcarine sulcus,
    which is medial to the lunate sulcus.

..cortex.insular  — indirect
    No direct insular → lunate sulcus projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **Indirect relationship.** The LGN is the thalamic relay to
    V1 (the lunate's caudal bank). The optic radiation
    terminates more caudally at the occipital pole, not
    specifically beneath the lunate sulcus.

../../subcortical/medial_temporal_lobe/hippocampus
    **No direct hippocampal → lunate sulcus projection.**

../../right/cortex/occipital/sulci/lunate_sulcus
    The **right-hemisphere homologue**. Structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    RETINOTOPIC_ROLE, EXTENT, PRESENCE_PROBABILITY, VARIANTS,
    SUBDIVISIONS, CONNECTIVITY) MUST be byte-identical. The
    **represented visual hemifield** and the **clinical
    significance** diverge — the right lunate sulcus (when
    present) marks the **LEFT hemifield's V1 / V2 border** on
    the right lateral occipital surface, and right lunate-based
    resections must account for the left-hemifield vertical
    meridian.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "lunate_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    BOUNDING_GYRI       = {                          # identical to right
                              "rostral": ("v2_lateral_territory",),
                              "caudal":  ("v1_lateral_territory",),
                          }
        # **Both bounding "gyri" are sub-regions**, not
        # standalone gyrus packages. The parent inversion
        # function must record them as **sub-regional
        # bounding relationships**, not as expected future
        # gyrus packages.

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "rostral": (18,),   # V2
                              "caudal":  (17,),   # V1
                          }

    EXTENT              = {                          # identical to right
                              "dorsal":  ("lateral_surface_of_"
                                          "occipital_lobe",
                                          "transverse_occipital_"
                                          "sulcus"),
                              "ventral": ("lateral_occipito_"
                                          "temporal_sulcus",),
                          }

    PRESENCE_PROBABILITY = 0.5
        # **The lunate sulcus is present in roughly 40–60 %
        # of human brains.** This is the **only occipital
        # sulcus whose presence is probabilistic**, and it
        # is the **only sulcus in the cortex** that carries
        # an explicit ``PRESENCE_PROBABILITY`` field below
        # 1.0. **Downstream code must check this field
        # before using the lunate sulcus's bounding
        # relationships.**

    RETINOTOPIC_ROLE     = "vertical_meridian_v1_v2_border"
        # **The lunate sulcus, when present, marks the
        # VERTICAL MERIDIAN of the visual field on the
        # lateral surface** — the boundary between V1
        # (caudal bank) and V2 (rostral bank) near the
        # occipital pole. **On the left, the represented
        # hemifield is the RIGHT hemifield's vertical
        # meridian.**

    VISUAL_HEMIFIELD     = "right"
        # **The represented visual hemifield** — left
        # lunate sulcus (when present) marks the RIGHT
        # hemifield's V1 / V2 border.

    VARIANTS            = (                          # DIFFERS from right
                              "absent_~40_to_60_pct",
                              "continuous_present_~35_pct",
                              "fragmented_present_~25_pct",
                              "left_right_asymmetry_documented",
                              "striate_cortex_lateral_extension_"
                              "always",
                          )
        # **The presence/absence variants are the primary
        # variants** — the lunate sulcus is the only
        # occipital sulcus whose presence is
        # probabilistic. The **striate_cortex_lateral_
        # extension_always** entry records the invariant
        # — V1's lateral territory is **always** present,
        # regardless of the lunate's presence.

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "left_lunate_v1_v2_border_"
                              "landmark",
                              "left_lunate_conditional_"
                              "landmark_absent_in_40pct",
                              "left_lunate_surgical_landmark_"
                              "for_v1_v2_border",
                              "left_lunate_occipital_epilepsy_"
                              "visual_auras",
                              "left_lunate_migraine_visual_"
                              "aura",
                              "left_lunate_occipital_infarct_"
                              "pca_territory",
                              "left_lunate_posterior_cortical_"
                              "atrophy",
                          )
        # **The lunate-specific anchors** (`v1_v2_border_
        # landmark`, `conditional_landmark_absent_in_40pct`,
        # `surgical_landmark_for_v1_v2_border`) are the
        # **primary lunate anchors**. **The field-defect
        # anchors** (homonymous hemianopia, macular sparing,
        # etc.) belong to the **calcarine sulcus**, not the
        # lunate.

    CONNECTIVITY        = {}   # no major bundle beneath the sulcus
        # **The lunate sulcus has no specific white-matter
        # bundle beneath it.** The optic radiation terminates
        # more caudally at the occipital pole, and the
        # pericalcarine white matter is more medial. The
        # lunate sulcus is a pure cortical-transition
        # landmark (V1 to V2), not a white-matter landmark.

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "SULCUS_NAME",
        "HEMISPHERE",
        "LOBE",
        "BOUNDING_GYRI",
        "BRODMANN_ADJACENCY",
        "EXTENT",
        "PRESENCE_PROBABILITY",
        "RETINOTOPIC_ROLE",
        "VISUAL_HEMIFIELD",
        "VARIANTS",
        "CLINICAL_ANCHORS",
        "CONNECTIVITY",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references the lunate sulcus lives in
``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are two forward references in this package's
BOUNDING_GYRI, and they are both SUB-REGIONS, not
forward-reference gyrus packages:**

1. **V1 lateral territory** — the caudal bank of the lunate
   sulcus. **It is a sub-region of the calcarine cortex (V1
   territory)**, not a standalone gyrus package. **It will
   never be a standalone package** — it is a portion of V1's
   cortex that extends onto the lateral surface, and it is
   modelled as part of the calcarine cortex (``..cortex/
   primary_visual_cortex``) and the cuneus / lingual gyrus
   packages, not as its own gyrus.

2. **V2 lateral territory** — the rostral bank of the lunate
   sulcus. **It is a sub-region of the lateral occipital
   gyrus (V2 territory)**, not a standalone gyrus package.
   **It will never be a standalone package** — it is a
   portion of the lateral occipital gyrus's V2 overlay, and it
   is modelled as part of the ``..gyri/lateral_occipital_
   gyrus`` package.

**This is the only sulcus in the cortex whose bounding
"gyri" are BOTH sub-regions that will never become standalone
gyrus packages.** The parent ``..sulci`` package's forward-
reference list includes `v1_lateral_territory` and
`v2_lateral_territory` as **documented sub-regions**, not as
expected future gyrus packages. **The inversion function must
record them as sub-regional bounding relationships**, and the
duality test must treat them as **intentionally-resolved
sub-regions**, not as unresolved forward references.

**The resolution for these sub-regions is not "wait for the
package to be created"** — it is "acknowledge that they are
sub-regions of existing gyral / cortical territories". **The
parent inversion function must record them with a
`SUB_REGION = True` flag** (or equivalent), so that downstream
code querying "what is the V1 lateral territory?" can receive
"a sub-region of the calcarine cortex, not a standalone
gyrus."

**All forward references are byte-identical to the right
sibling's.**

--------------------------------------------------------------------------------
PROMOTION RULE (when a lunate segment becomes a package)
--------------------------------------------------------------------------------

The lunate sulcus is **short, inconstant, and architectonically
continuous** when present. **No SUBDIVISIONS promotion is
recommended for the lunate sulcus.**

**The one conceivable subdivision is a dorsal / ventral split** —
a hypothetical separation into a "dorsal lunate sulcus" and a
"ventral lunate sulcus." **This subdivision has no anatomical
precedent in the tree** (the lunate is a short sulcus, not a
long anteroposterior one), and it is **not recommended**.

**The recommended structural treatment is to keep the lunate
sulcus as a single leaf sulcus package**, with the
**PRESENCE_PROBABILITY field** expressing its inconstancy and
with the bounding sub-regions expressed through
``BOUNDING_GYRI`` and the parent's sub-regional inversion.

**When the parent's `PRESENCE_PROBABILITY`-aware duality test
is implemented**, it must **skip the lunate sulcus when the
sulcus is absent in a given subject** — the duality test asserts
the sulcus's bounding relationships **conditional on its
presence**, not unconditionally.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../lunate_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME                  "lunate_sulcus"
        LOBE                         "occipital"
        BOUNDING_GYRI                rostral (v2_lateral_territory),
                                     caudal (v1_lateral_territory)
        BRODMANN_ADJACENCY           rostral (18,), caudal (17,)
        EXTENT                       dorsal (lateral_surface /
                                     transverse_occipital_sulcus),
                                     ventral (lateral_occipito_
                                     temporal_sulcus)
        PRESENCE_PROBABILITY         0.5 — the lunate is the only
                                     probabilistic occipital sulcus
        RETINOTOPIC_ROLE             "vertical_meridian_v1_v2_
                                     border"
        VARIANTS                     absent ~40–60%, continuous
                                     ~35%, fragmented ~25%,
                                     left-right asymmetry
                                     documented, striate cortex
                                     lateral extension always
        SUBDIVISIONS                 both empty
        CONNECTIVITY                 {} — no major bundle beneath
                                     the sulcus

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        RETINOTOPIC_ROLE       the **represented hemifield** flips
                               — the left lunate marks the RIGHT
                               hemifield's vertical meridian; the
                               right lunate marks the LEFT
                               hemifield's vertical meridian.
        CLINICAL_ANCHORS       left: right-hemifield V1/V2 border
                               landmark, conditional landmark
                               absence (~40%), surgical landmark
                               for V1/V2 border, occipital
                               epilepsy visual auras, migraine
                               aura, occipital infarct, PCA.
                               right: left-hemifield V1/V2 border
                               landmark, conditional landmark
                               absence (~40%), surgical landmark
                               for V1/V2 border, occipital
                               epilepsy visual auras, migraine
                               aura, occipital infarct, PCA
                               (Benson syndrome).

**The visual-hemifield asymmetry is the sharpest single entry.**
When present, the left lunate sulcus marks the RIGHT hemifield's
V1 / V2 border; the right's marks the LEFT.

**The `PRESENCE_PROBABILITY` field is byte-identical on both
sides** — 0.5 on the left and 0.5 on the right. **The lunate
sulcus's inconstancy is a species-level property, not a
hemisphere-level one.** **Any documented asymmetry in a specific
subject must be recorded in the subject-specific data**, not
hard-coded in either the left or the right package.

**The sub-regional bounding relationships
(`v1_lateral_territory`, `v2_lateral_territory`) are
byte-identical on both sides** — the lunate's bounding
territories are sub-regions of the same parent gyral / cortical
territories on both hemispheres.

**The other structural fields (BRODMANN_ADJACENCY, EXTENT,
RETINOTOPIC_ROLE structure, VARIANTS, SUBDIVISIONS,
CONNECTIVITY) are byte-identical on both sides.**

**The hemisphere-invariant anchors** — occipital epilepsy visual
auras, migraine aura, occipital infarct, and PCA (with the
right's Benson subtype emphasis) — are **documented identically
in both siblings**, with the side-appropriate field label.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "lunate_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] BOUNDING_GYRI is byte-identical to the right sibling's:
    rostral (v2_lateral_territory), caudal
    (v1_lateral_territory).
[ ] **Both bounding "gyri" are documented as SUB-REGIONS, not
    standalone gyrus packages**: V2 lateral territory is a
    sub-region of the lateral occipital gyrus; V1 lateral
    territory is a sub-region of the calcarine cortex.
[ ] BRODMANN_ADJACENCY is byte-identical to the right sibling's:
    rostral (BA 18), caudal (BA 17).
[ ] **The lunate sulcus is documented as the only sulcus in
    the cortex whose Brodmann adjacency is BA 17 / BA 18** —
    the primary / secondary visual cortex transition.
[ ] EXTENT is byte-identical to the right sibling's:
    - dorsal: lateral surface / transverse occipital sulcus
    - ventral: lateral occipitotemporal sulcus
[ ] **PRESENCE_PROBABILITY = 0.5** is present — **the lunate
    sulcus is the only occipital sulcus whose presence is
    probabilistic, and the only sulcus in the cortex with an
    explicit ``PRESENCE_PROBABILITY`` below 1.0.**
[ ] RETINOTOPIC_ROLE is "vertical_meridian_v1_v2_border" and
    documents the role:
    - when present, the sulcus marks the vertical meridian of
      the visual field on the lateral surface
    - the vertical meridian is the V1 / V2 border
    - **on the left, the represented hemifield is the RIGHT
      hemifield's vertical meridian**
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] VARIANTS is byte-identical to the right sibling's and
    documents:
    - **absent ~40–60 %** (the most common variant is absence)
    - continuous present ~35 %
    - fragmented present ~25 %
    - left-right asymmetry documented (individual-level, not
      systematic hemisphere asymmetry)
    - **striate cortex lateral extension always** — the
      invariant across all variants; V1's lateral territory is
      always present, regardless of the sulcus's presence
[ ] **The invariant across all variants is documented**: V1's
    lateral territory is **always** present, and the
    V1 / V2 border is **always** architectonically
    unambiguous (marked by the stria of Gennari), even when
    the lunate sulcus is absent.
[ ] CONNECTIVITY is `{}` (empty dict) — **no major white-
    matter bundle beneath the lunate sulcus**. The lunate is
    a **pure cortical-transition landmark** (V1 to V2), not
    a white-matter landmark.
[ ] CLINICAL_ANCHORS contains the left-specific anchors:
    - left_lunate_v1_v2_border_landmark
    - **left_lunate_conditional_landmark_absent_in_40pct**
    - left_lunate_surgical_landmark_for_v1_v2_border
    - left_lunate_occipital_epilepsy_visual_auras
    - left_lunate_migraine_visual_aura
    - left_lunate_occipital_infarct_pca_territory
    - left_lunate_posterior_cortical_atrophy
[ ] **The `v1_v2_border_landmark` anchor is conditional on the
    sulcus being present** — the anchor documents the
    landmark when the sulcus is present.
[ ] **The `conditional_landmark_absent_in_40pct` anchor is a
    POSITIVE structural warning** — downstream code must not
    assume the lunate is present, and must have a fallback
    plan (retinotopic mapping, stria of Gennari) for cases
    where it is absent.
[ ] **The `surgical_landmark_for_v1_v2_border` anchor documents
    the surgical planning consideration** — the lunate
    sulcus, when present, is a surgical landmark for
    resections in the lateral occipital region that must
    preserve V1; when absent, intraoperative mapping is
    required.
[ ] **The field-defect anchors** (homonymous hemianopia,
    macular sparing, cortical blindness, Anton syndrome,
    blindsight) are **explicitly NOT included** in the
    lunate's `CLINICAL_ANCHORS` — those belong to the
    **calcarine sulcus**, not the lunate. **The lunate's
    anchors are focused on the V1/V2 border landmark
    function, surgical planning, and epileptogenic zone
    localization.**
[ ] **The lunate sulcus is documented as the LATERAL-surface
    counterpart to the calcarine sulcus's MEDIAL-surface
    V1/V2 border mark** — with the important difference that
    the calcarine's V1/V2 border is always architectonically
    visible, while the lunate's lateral V1/V2 border is only
    sometimes visible as a surface sulcus.
[ ] **The stria of Gennari's role is documented** — the stria
    is the **primary** architectonic marker for the V1/V2
    border, always present regardless of the lunate's
    presence.
[ ] **The sub-regional forward reference is documented**: V1
    lateral territory and V2 lateral territory are
    **sub-regions** of the calcarine cortex and the lateral
    occipital gyrus, not standalone gyrus packages. **They
    will never become standalone packages**, and the parent
    inversion function must record them as sub-regional
    bounding relationships.
[ ] **The parent's `PRESENCE_PROBABILITY`-aware duality test
    is documented** — the lunate sulcus's bounding
    relationships are asserted **conditional on the sulcus's
    presence**, not unconditionally.
[ ] No SUBDIVISIONS promotion is recommended — the lunate is
    a short, inconstant, architectonically continuous sulcus
    when present.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    EXTENT, PRESENCE_PROBABILITY, RETINOTOPIC_ROLE,
    VARIANTS, SUBDIVISIONS, CONNECTIVITY) match the right
    sibling; VISUAL_HEMIFIELD and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    lunate sulcus (when present) marks the RIGHT hemifield's
    V1/V2 border; the right's marks the LEFT.
[ ] **The `PRESENCE_PROBABILITY` byte-identity is verified**:
    0.5 on both sides. **Any documented left-right asymmetry
    in a specific subject must be recorded in subject-specific
    data**, not in the package's structural fields.
[ ] Any downstream code querying "what does the left lunate
    sulcus bound?" must receive "the V1 lateral territory
    (caudal) and V2 lateral territory (rostral), **when the
    sulcus is present**. Both bounding territories are
    sub-regions of the calcarine cortex and the lateral
    occipital gyrus respectively."
[ ] Any downstream code querying "what does the left lunate
    sulcus represent retinotopically?" must receive "the
    VERTICAL MERIDIAN of the RIGHT hemifield — the V1/V2
    border — **when the sulcus is present**."
[ ] Any downstream code querying "is the lunate sulcus
    always present?" must receive "**no — it is present in
    roughly 40–60 % of human brains (PRESENCE_PROBABILITY =
    0.5)**. Downstream code must check `PRESENCE_PROBABILITY`
    before using the lunate's bounding relationships."
[ ] Any downstream code querying "what happens when the
    lunate sulcus is absent?" must receive "the lateral
    V1/V2 border is **not visible as a surface sulcus**, but
    it is **still architectonically marked by the stria of
    Gennari's disappearance**. The boundary must be inferred
    from the retinotopic map or the stria, not from the
    surface sulcus."
[ ] Any downstream code querying "what white-matter bundle
    runs beneath the lunate sulcus?" must receive "**none**
    — the lunate sulcus is a pure cortical-transition
    landmark (V1 to V2), not a white-matter landmark. The
    optic radiation terminates more caudally at the
    occipital pole."
[ ] Any downstream code assigning **field-defect anchors**
    (homonymous hemianopia, macular sparing, cortical
    blindness, etc.) must route through the **calcarine
    sulcus**, not the lunate sulcus — those anchors belong
    to the calcarine, not the lunate.
[ ] **The forward-reference caveat is byte-identical to the
    right sibling's** — the V1 lateral territory and V2
    lateral territory are **sub-regions that will never
    become standalone gyrus packages**.
[ ] **The sub-regional flag is documented**: the parent
    inversion function must record `v1_lateral_territory`
    and `v2_lateral_territory` with a `SUB_REGION = True`
    flag (or equivalent), so that downstream code can
    distinguish sub-regional bounding relationships from
    forward-reference gyrus packages.
[ ] **The lunate sulcus's inconstancy is documented as a
    species-level property, not a hemisphere-level one** —
    it is present in ~50 % of brains on both hemispheres,
    and the `PRESENCE_PROBABILITY` field is 0.5 on both
    sides.
"""