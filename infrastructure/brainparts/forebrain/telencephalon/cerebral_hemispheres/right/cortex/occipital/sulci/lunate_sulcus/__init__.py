"""
Lunate Sulcus — Right Hemisphere
=================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── sulci
                                    └── lunate_sulcus   ← THIS PACKAGE

This is a **leaf sulcus package** describing the right hemisphere's
**lunate sulcus** — the **inconstant lateral-surface sulcus** that,
**when present**, marks the **V1 / V2 border** on the lateral surface
of the occipital lobe. It is the **only occipital sulcus whose
presence is probabilistic** — present in roughly **40–60 % of
human brains** depending on the series — and it is the **only sulcus
in the entire cortex** that carries an explicit
``PRESENCE_PROBABILITY`` field below 1.0.

Parent: ``..sulci`` (right occipital sulci parent) — sibling to
``calcarine_sulcus`` and ``transverse_occipital_sulcus``.

This package is the **structural mirror** of
``../../left/cortex/occipital/sulci/lunate_sulcus``. The sulcus
name, the bounding sub-regions (V1 lateral territory caudal, V2
lateral territory rostral), the Brodmann adjacency (BA 17 caudal,
BA 18 rostral), the vertical-meridian retinotopic role, the
**PRESENCE_PROBABILITY ≈ 0.5**, the extent landmarks, and the
connectivity (no major bundle beneath the sulcus) are identical on
both sides; the **represented visual hemifield** and the **clinical
significance** diverge — on the right, the lunate sulcus marks the
**LEFT** hemifield's V1 / V2 border (when present), and right
lunate-based resections must account for the left-hemifield vertical
meridian. The left lunate sulcus marks the mirror arrangement
(right hemifield).

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

**This structural framing is byte-identical to the left sibling's**
— the medial-vs-lateral V1 / V2 border marker asymmetry is a
property of the occipital lobe's anatomy, not of the hemisphere.

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
the boundary between V1's representation of the contralateral
hemifield and V2's representation of the same hemifield. **On the
right, the lunate sulcus marks the LEFT hemifield's vertical
meridian.** **On the left, it marks the RIGHT hemifield's vertical
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
visible histologically but not as a surface groove.

**Right-hemisphere specificity**: the right lunate sulcus, **when
present**, marks the **LEFT** hemifield's V1 / V2 border on the
lateral surface of the right occipital lobe. **Right
lunate-based surgical resections** (for lesions near the
occipital pole, or for epilepsy surgery in the lateral occipital
region) must account for the **left-hemifield vertical meridian** —
the boundary between V1 (calcarine cortex) and V2 (extrastriate)
territory near the right occipital pole. **When the lunate is
absent**, the boundary must be inferred from the retinotopic map
or from the stria of Gennari (visible on fresh specimens or on
high-resolution histology), not from the surface sulcus.

**The right lunate sulcus is a secondary landmark for the right
V1 / V2 border** — its primary clinical relevance is as a
**retinotopic reference point** and as a **surgical landmark** for
resections that need to distinguish V1 (eloquent visual cortex)
from V2 (extrastriate, non-eloquent in the sense of primary
vision) on the lateral surface. **The right lunate's territory
feeds the right V4v → LOC → right FFA face-recognition pathway**
— the left-hemifield V1 signal from the right lunate's caudal
bank is part of the primary visual input to the right face
pathway, and right lunate-based resections that damage V1's
lateral territory can contribute to face-processing deficits when
the downstream right FFA is also affected.

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
gyral / cortical territories, and the parent inversion function
must record this as a **sub-regional duality**, not a gyrus-
package duality.

**This field is byte-identical to the left sibling's.**

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
sides, the transverse occipital sulcus has BA 19 / BA 39, and the
lunate is the only sulcus whose two sides carry the **primary (BA
17) / secondary (BA 18)** transition.

**This field is byte-identical to the left sibling's.**

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    dorsal end
        Reaches the **lateral surface of the occipital lobe**,
        near the **transverse occipital sulcus** (or the
        occipito-parietal junction).

    ventral end
        Reaches the **lateral occipitotemporal sulcus** (or the
        occipito-temporal junction), near the ventral edge of
        the lateral occipital gyrus.

**The lunate sulcus is a short sulcus** — it does not run the full
anteroposterior extent of the lateral surface, unlike the
transverse occipital sulcus (which is a lobar boundary) or the
calcarine sulcus (which runs the full anteroposterior extent of
the medial surface). **Its extent is limited to the
V1 / V2 border region near the occipital pole**, and it is
typically **2–4 cm long** when present.

**This field is byte-identical to the left sibling's.**

--------------------------------------------------------------------------------
VARIANTS (right-hemisphere specific)
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
        occipitotemporal sulcus ventrally).

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

**This field is byte-identical to the left sibling's** — the
lunate sulcus's inconstancy is a species-level property, not a
hemisphere-level one. **Any documented left-right asymmetry in
lunate presence in a specific subject must be recorded in the
subject-specific data**, not hard-coded in either the left or the
right package's VARIANTS field.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_lunate_v1_v2_border_landmark
        **This is the right lunate sulcus's primary clinical
        anchor.** **When present**, the right lunate sulcus is
        the **surface landmark for the LEFT hemifield's
        V1 / V2 border** on the lateral surface of the right
        occipital lobe. **Right lunate-based surgical
        resections** (for lesions near the occipital pole, or
        for epilepsy surgery in the lateral occipital region)
        must account for the **left-hemifield vertical
        meridian** — the boundary between V1 (eloquent visual
        cortex) and V2 (extrastriate) territory near the
        right occipital pole.

    right_lunate_conditional_landmark_absent_in_40pct
        **The right lunate sulcus's secondary clinical anchor
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

    right_lunate_surgical_landmark_for_v1_v2_border
        **The right lunate sulcus's surgical anchor.**
        **When present**, the right lunate sulcus is a
        surgical landmark for resections in the lateral
        occipital region that must **preserve V1** (the
        eloquent visual cortex) while resecting V2 or V3d
        territory. **When absent**, the surgeon must rely
        on intraoperative neurophysiological mapping
        (visual evoked potentials from the lateral
        occipital surface) rather than on the surface
        sulcus.

    right_lunate_v1_contribution_to_prosopagnosia
        **The right lunate sulcus's right-lateralized
        downstream anchor — the mirror of the left's
        `left_lunate_surgical_landmark` emphasis.**
        **The right lunate's caudal bank (V1 lateral
        territory) is the upstream visual input to the
        right V4v → LOC → right FFA face-recognition
        chain.** Right lunate-based resections that damage
        V1's lateral territory can **contribute to
        prosopagnosia** when the downstream right FFA is
        also affected. **The deficit is a face-recognition
        deficit**, not a reading deficit — the right
        hemisphere does not have a right VWFA equivalent.
        **This anchor has no symmetric counterpart on the
        left.**

    right_lunate_v1_contribution_to_visuospatial_deficit
        **The right lunate sulcus's visuospatial anchor.**
        **The right lunate's caudal bank (V1 lateral
        territory) is part of the right occipital lobe's
        visuospatial substrate.** Right lunate-based
        resections that damage V1's lateral territory can
        **contribute to visuospatial deficits** — impaired
        spatial localization, impaired spatial attention,
        and impaired visuospatial working memory — **that
        are more severe than the left equivalent** because
        the right hemisphere is the dominant visuospatial
        hemisphere. **This anchor has no symmetric
        counterpart on the left at the same weighting.**

    right_lunate_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from the lateral occipital region near the
        lunate sulcus. **The lunate sulcus is a surface
        landmark for the V1 / V2 border in the epileptogenic
        zone** when the seizure onset is in the lateral
        occipital cortex. **The right lunate's auras project
        to the LEFT visual field.**

    right_lunate_migraine_visual_aura
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
        contralateral (left field on the right side).

    right_lunate_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct**
        can involve the lateral occipital cortex near the
        lunate sulcus and produce a **left homonymous
        hemianopia or quadrantic defect** with **left
        macular sparing**. **The lunate sulcus's
        contribution to the infarct's clinical signature
        is as a surface landmark for the boundary between
        V1 (eloquent) and V2 (non-eloquent) territory** in
        the lateral occipital region. **Isolated right PCA
        infarcts do not produce alexia without agraphia** —
        that syndrome is left-lateralized.

    right_lunate_posterior_cortical_atrophy_benson_syndrome
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive
        visual dysfunction — involves the lateral occipital
        cortex including the lunate sulcus territory.
        **Right lunate** is part of the substrate of the
        progressive dorsal / ventral stream dysfunction
        that produces **Benson syndrome** — progressive
        prosopagnosia, visuospatial deficits, optic ataxia,
        simultanagnosia. **On the right, PCA presents with
        the visuospatial / prosopagnosic syndrome**; on
        the left, with the progressive reading deficits.

**The lunate sulcus's clinical anchors are narrower than the
calcarine sulcus's** — the lunate is a **conditional landmark**
(when present) for the V1 / V2 border, not a primary field-defect
anchor. **The field-defect anchors** (left homonymous hemianopia,
macular sparing, etc.) belong to the **calcarine sulcus**, not
the lunate.

**The right lunate carries two right-only positive anchors** that
the left does not carry at the same weighting:
`right_lunate_v1_contribution_to_prosopagnosia` (the mirror of
the left's reading-related emphasis) and
`right_lunate_v1_contribution_to_visuospatial_deficit` (the right
hemisphere's visuospatial dominance). These are the right-side
counterparts to the left lunate's left-lateralized emphasis on
the V1 / V2 border's role in the left reading pathway.

**The absence anchor**
(`right_lunate_conditional_landmark_absent_in_40pct`) is a
**structural warning** — downstream code must not assume the
lunate sulcus is present, and must have a fallback plan
(retinotopic mapping, stria of Gennari) for cases where it is
absent.

**The hemisphere-invariant anchors** — occipital epilepsy visual
auras, migraine aura, occipital infarct, and PCA (with the
right's Benson subtype emphasis) — are **documented identically
in both siblings**, with the side-appropriate field label.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    structures within / beneath the sulcus
        **No major white-matter bundle specifically associated
        with the lunate sulcus.** The optic radiation terminates
        more caudally at the occipital pole, in the calcarine
        banks. The pericalcarine white matter (short-range
        association fibers between V1 and V2) is **more
        medial**, along the calcarine sulcus.

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

**This field is byte-identical to the left sibling's.**

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..sulci  (parent)
    The right occipital sulci parent. The lunate sulcus is one of
    its three current children.

..sulci.calcarine_sulcus
    The **medial-surface V1 / V2 border marker** — the primary,
    architectonically unambiguous V1 / V2 boundary marked by the
    **abrupt disappearance of the stria of Gennari**. **The
    lunate sulcus is the LATERAL-surface counterpart** to the
    calcarine's medial-surface V1 / V2 border mark.

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
    include V3d, V4d, and LOC). **On the right, the lateral
    occipital gyrus's LOC feeds the right FFA face pathway**,
    and the lunate's V1 lateral territory is part of the
    upstream V1 input to that chain.

..gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The **V1 lateral territory (the lunate's caudal bank) is
    continuous with V1's medial territory** on the calcarine
    banks. **The lingual gyrus is the lower-bank portion of
    the medial V1 territory**, and the V1 lateral territory is
    the extension of V1 onto the lateral surface.

..brodmann_areas.brodmann_area_17_primary_visual
    The **V1 cytoarchitectonic counterpart** of the lunate
    sulcus's caudal bank. **BA 17's territory extends onto the
    lateral surface near the occipital pole.**

..brodmann_areas.brodmann_area_18
    The **V2 cytoarchitectonic counterpart** of the lunate
    sulcus's rostral bank. **BA 18's territory extends onto the
    lateral surface as the V2 extrastriate belt.**

...cortex.primary_visual_cortex
    The **V1 functional counterpart** of the lunate sulcus's
    caudal bank. **V1's territory extends onto the lateral
    surface near the occipital pole.**

...cortex.v2
    The **V2 functional counterpart** of the lunate sulcus's
    rostral bank. **V2's territory extends onto the lateral
    surface as the extrastriate belt.**

...cortex.v3
    The **V3 territory** is further lateral and ventral to V2.
    **No direct adjacency to the lunate sulcus** — the lunate
    marks the V1 / V2 border, not the V2 / V3 border. **On
    the right, V3d (in the cuneus's dorsal bank) is the
    dominant motion substrate**, and it is downstream of the
    lunate's V2 territory, not part of it.

...cortex.v4
    **No direct adjacency to the lunate sulcus.** V4 is further
    lateral / ventral. **On the right, V4v (downstream of V2)
    feeds the right LOC → right FFA face pathway**, and the
    lunate's V1 lateral territory is the upstream V1 input to
    that chain.

..cortex.temporal
    The **lateral occipitotemporal sulcus** (the ventral
    boundary of the lateral occipital gyrus, into the fusiform
    gyrus) is **ventral to the lunate sulcus**. **On the
    right, the fusiform gyrus contains the right FFA** — the
    face-recognition endpoint. **No direct adjacency** between
    the lunate sulcus and the temporal lobe.

..cortex.parietal
    The **transverse occipital sulcus** (the dorsal boundary of
    the lateral occipital gyrus) is **dorsal to the lunate
    sulcus**. **No direct adjacency** between the lunate sulcus
    and the parietal lobe.

..cortex.frontal
    **No direct sulcal adjacency.**

..cortex.cingulate
    **No direct sulcal adjacency.**

..cortex.insular  — indirect
    No direct insular → lunate sulcus projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **Indirect relationship.** The LGN is the thalamic relay to
    V1 (the lunate's caudal bank). The optic radiation
    terminates more caudally at the occipital pole.

../../subcortical/medial_temporal_lobe/hippocampus
    **No direct hippocampal → lunate sulcus projection.**

../../left/cortex/occipital/sulci/lunate_sulcus
    The **left-hemisphere homologue**. Structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    EXTENT, PRESENCE_PROBABILITY, RETINOTOPIC_ROLE,
    VARIANTS, SUBDIVISIONS, CONNECTIVITY) MUST be
    byte-identical. The **represented visual hemifield** and
    the **clinical significance** diverge — the left lunate
    sulcus (when present) marks the **RIGHT hemifield's**
    V1 / V2 border on the left lateral occipital surface, and
    left lunate-based resections must account for the
    right-hemifield vertical meridian. **The left lunate
    carries the left-lateralized V1/V2 border emphasis in the
    left reading pathway**, while the right lunate carries
    the right-lateralized V1/V2 border emphasis in the right
    face pathway.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "lunate_sulcus"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    BOUNDING_GYRI       = {                          # identical to left
                              "rostral": ("v2_lateral_territory",),
                              "caudal":  ("v1_lateral_territory",),
                          }
        # **Both bounding "gyri" are sub-regions**, not
        # standalone gyrus packages. The parent inversion
        # function must record them with a `SUB_REGION = True`
        # flag (or equivalent).

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "rostral": (18,),   # V2
                              "caudal":  (17,),   # V1
                          }

    EXTENT              = {                          # identical to left
                              "dorsal":  ("lateral_surface_of_"
                                          "occipital_lobe",
                                          "transverse_occipital_"
                                          "sulcus"),
                              "ventral": ("lateral_occipito_"
                                          "temporal_sulcus",),
                          }

    PRESENCE_PROBABILITY = 0.5
        # **Byte-identical to the left sibling's.** The lunate
        # is the only probabilistic occipital sulcus, and it is
        # present in roughly 40–60 % of human brains on both
        # hemispheres. **Any documented left-right asymmetry in
        # a specific subject must be recorded in subject-
        # specific data**, not hard-coded in either the left or
        # the right package.

    RETINOTOPIC_ROLE     = "vertical_meridian_v1_v2_border"
        # **The lunate sulcus, when present, marks the
        # VERTICAL MERIDIAN of the visual field on the
        # lateral surface.** **On the right, the represented
        # hemifield is the LEFT hemifield's vertical
        # meridian.**

    VISUAL_HEMIFIELD     = "left"
        # **The represented visual hemifield** — right
        # lunate sulcus (when present) marks the LEFT
        # hemifield's V1 / V2 border.

    VARIANTS            = (                          # identical to left
                              "absent_~40_to_60_pct",
                              "continuous_present_~35_pct",
                              "fragmented_present_~25_pct",
                              "left_right_asymmetry_documented",
                              "striate_cortex_lateral_extension_"
                              "always",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from left
                              "right_lunate_v1_v2_border_"
                              "landmark",
                              "right_lunate_conditional_"
                              "landmark_absent_in_40pct",
                              "right_lunate_surgical_landmark_"
                              "for_v1_v2_border",
                              "right_lunate_v1_contribution_to_"
                              "prosopagnosia",
                              "right_lunate_v1_contribution_to_"
                              "visuospatial_deficit",
                              "right_lunate_occipital_epilepsy_"
                              "visual_auras",
                              "right_lunate_migraine_visual_"
                              "aura",
                              "right_lunate_occipital_infarct_"
                              "pca_territory",
                              "right_lunate_posterior_cortical_"
                              "atrophy_benson_syndrome",
                          )
        # **The lunate-specific anchors** (`v1_v2_border_
        # landmark`, `conditional_landmark_absent_in_40pct`,
        # `surgical_landmark_for_v1_v2_border`) are the
        # **primary lunate anchors**, mirroring the left's.
        # **The right-only positive anchors**
        # (`v1_contribution_to_prosopagnosia`,
        # `v1_contribution_to_visuospatial_deficit`) mirror
        # the left's left-lateralized reading-related
        # emphasis. **The field-defect anchors** (homonymous
        # hemianopia, macular sparing, etc.) belong to the
        # **calcarine sulcus**, not the lunate.

    CONNECTIVITY        = {}   # no major bundle beneath the sulcus
        # **Byte-identical to the left sibling's.**

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
forward-reference gyrus packages** (byte-identical to the left
sibling's):

1. **V1 lateral territory** — the caudal bank of the lunate
   sulcus. **A sub-region of the calcarine cortex (V1
   territory).** It will never be a standalone package.

2. **V2 lateral territory** — the rostral bank of the lunate
   sulcus. **A sub-region of the lateral occipital gyrus (V2
   territory).** It will never be a standalone package.

**This is the only sulcus in the cortex whose bounding
"gyri" are BOTH sub-regions that will never become standalone
gyrus packages.** The parent inversion function must record them
with a `SUB_REGION = True` flag (or equivalent), so that
downstream code can distinguish sub-regional bounding
relationships from forward-reference gyrus packages.

**The resolution for these sub-regions is not "wait for the
package to be created"** — it is "acknowledge that they are
sub-regions of existing gyral / cortical territories".

**All forward references are byte-identical to the left
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
precedent in the tree** and is **not recommended**.

**The recommended structural treatment is to keep the lunate
sulcus as a single leaf sulcus package**, with the
**PRESENCE_PROBABILITY field** expressing its inconstancy and
with the bounding sub-regions expressed through
``BOUNDING_GYRI`` and the parent's sub-regional inversion.

**When the parent's `PRESENCE_PROBABILITY`-aware duality test
is implemented**, it must **skip the lunate sulcus when the
sulcus is absent in a given subject** — the duality test
asserts the sulcus's bounding relationships **conditional on its
presence**, not unconditionally.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../lunate_sulcus``:

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
        PRESENCE_PROBABILITY         0.5
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
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        RETINOTOPIC_ROLE       the **represented hemifield** flips
                               — the right lunate marks the LEFT
                               hemifield's vertical meridian;
                               the left lunate marks the RIGHT
                               hemifield's vertical meridian.
        CLINICAL_ANCHORS       right: left-hemifield V1/V2
                               border landmark, conditional
                               landmark absence (~40%), surgical
                               landmark for V1/V2 border,
                               **right_lunate_v1_contribution_to_
                               prosopagnosia**,
                               **right_lunate_v1_contribution_to_
                               visuospatial_deficit**, occipital
                               epilepsy visual auras, migraine
                               aura, occipital infarct, PCA
                               (Benson syndrome).
                               left: right-hemifield V1/V2
                               border landmark, conditional
                               landmark absence (~40%), surgical
                               landmark for V1/V2 border,
                               occipital epilepsy visual auras,
                               migraine aura, occipital infarct,
                               PCA.

**The visual-hemifield asymmetry is the sharpest single entry.**
When present, the right lunate sulcus marks the LEFT hemifield's
V1 / V2 border; the left's marks the RIGHT.

**The `PRESENCE_PROBABILITY` field is byte-identical on both
sides** — 0.5 on the right and 0.5 on the left. **The lunate
sulcus's inconstancy is a species-level property, not a
hemisphere-level one.** **Any documented asymmetry in a specific
subject must be recorded in the subject-specific data**, not
hard-coded in either package.

**The sub-regional bounding relationships
(`v1_lateral_territory`, `v2_lateral_territory`) are
byte-identical on both sides.**

**The right-only positive anchors are the second sharpest entry.**
The right lunate carries two positive anchors that the left does
not carry at the same weighting:
`right_lunate_v1_contribution_to_prosopagnosia` (the right
hemisphere's face-pathway contribution) and
`right_lunate_v1_contribution_to_visuospatial_deficit` (the right
hemisphere's visuospatial dominance). These mirror the left's
left-lateralized emphasis on the V1/V2 border's role in the left
reading pathway.

**The hemisphere-invariant anchors** — occipital epilepsy visual
auras, migraine aura, occipital infarct, and PCA (with the
right's Benson subtype emphasis) — are **documented identically
in both siblings**, with the side-appropriate field label.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "lunate_sulcus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] BOUNDING_GYRI is byte-identical to the left sibling's:
    rostral (v2_lateral_territory), caudal
    (v1_lateral_territory).
[ ] **Both bounding "gyri" are documented as SUB-REGIONS**, not
    standalone gyrus packages.
[ ] BRODMANN_ADJACENCY is byte-identical to the left sibling's:
    rostral (BA 18), caudal (BA 17).
[ ] **The lunate sulcus is documented as the only sulcus in
    the cortex whose Brodmann adjacency is BA 17 / BA 18.**
[ ] EXTENT is byte-identical to the left sibling's.
[ ] **PRESENCE_PROBABILITY = 0.5** is present — byte-identical
    to the left sibling's, and the **only sulcus in the
    cortex** with an explicit ``PRESENCE_PROBABILITY`` below
    1.0.
[ ] RETINOTOPIC_ROLE is "vertical_meridian_v1_v2_border" and
    documents the role:
    - when present, the sulcus marks the vertical meridian of
      the visual field on the lateral surface
    - **on the right, the represented hemifield is the LEFT
      hemifield's vertical meridian**
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class
    field.
[ ] VARIANTS is byte-identical to the left sibling's and
    documents the same presence/absence variants.
[ ] **The invariant across all variants is documented**:
    V1's lateral territory is always present, and the
    V1 / V2 border is always architectonically unambiguous
    (marked by the stria of Gennari), even when the lunate
    sulcus is absent.
[ ] CONNECTIVITY is `{}` (empty dict) — **no major white-
    matter bundle beneath the lunate sulcus**.
[ ] CLINICAL_ANCHORS contains the right-specific anchors:
    - right_lunate_v1_v2_border_landmark
    - **right_lunate_conditional_landmark_absent_in_40pct**
    - right_lunate_surgical_landmark_for_v1_v2_border
    - **right_lunate_v1_contribution_to_prosopagnosia**
    - **right_lunate_v1_contribution_to_visuospatial_deficit**
    - right_lunate_occipital_epilepsy_visual_auras
    - right_lunate_migraine_visual_aura
    - right_lunate_occipital_infarct_pca_territory
    - right_lunate_posterior_cortical_atrophy_benson_syndrome
[ ] **The `v1_v2_border_landmark` anchor is conditional on the
    sulcus being present.**
[ ] **The `conditional_landmark_absent_in_40pct` anchor is a
    POSITIVE structural warning.**
[ ] **The `surgical_landmark_for_v1_v2_border` anchor documents
    the surgical planning consideration.**
[ ] **The `v1_contribution_to_prosopagnosia` anchor is a
    right-lateralized positive anchor** — the right lunate's
    V1 lateral territory is part of the upstream V1 input to
    the right V4v → LOC → right FFA face pathway.
[ ] **The `v1_contribution_to_visuospatial_deficit` anchor is
    a right-lateralized positive anchor** — the right
    hemisphere's visuospatial dominance gives the right
    lunate's V1 territory a more consequential role in
    visuospatial function than the left's.
[ ] **The field-defect anchors are explicitly NOT included** in
    the right lunate's `CLINICAL_ANCHORS` — those belong to the
    **calcarine sulcus**.
[ ] **The lunate sulcus is documented as the LATERAL-surface
    counterpart to the calcarine sulcus's MEDIAL-surface
    V1/V2 border mark.**
[ ] **The stria of Gennari's role is documented** — the stria
    is the **primary** architectonic marker for the V1/V2
    border, always present regardless of the lunate's
    presence.
[ ] **The sub-regional forward reference is documented** — V1
    lateral territory and V2 lateral territory are sub-regions
    that will never become standalone gyrus packages.
[ ] **The parent's `PRESENCE_PROBABILITY`-aware duality test
    is documented.**
[ ] No SUBDIVISIONS promotion is recommended.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    EXTENT, PRESENCE_PROBABILITY, RETINOTOPIC_ROLE,
    VARIANTS, SUBDIVISIONS, CONNECTIVITY) match the left
    sibling; VISUAL_HEMIFIELD and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    lunate sulcus (when present) marks the LEFT hemifield's
    V1/V2 border; the left's marks the RIGHT.
[ ] **The `PRESENCE_PROBABILITY` byte-identity is verified**:
    0.5 on both sides.
[ ] **The right-only positive anchors are verified**:
    `right_lunate_v1_contribution_to_prosopagnosia` and
    `right_lunate_v1_contribution_to_visuospatial_deficit`
    are present on the right and absent on the left.
[ ] Any downstream code querying "what does the right lunate
    sulcus bound?" must receive "the V1 lateral territory
    (caudal) and V2 lateral territory (rostral), **when the
    sulcus is present**. Both bounding territories are
    sub-regions of the calcarine cortex and the lateral
    occipital gyrus respectively."
[ ] Any downstream code querying "what does the right lunate
    sulcus represent retinotopically?" must receive "the
    VERTICAL MERIDIAN of the LEFT hemifield — the V1/V2
    border — **when the sulcus is present**."
[ ] Any downstream code querying "is the lunate sulcus
    always present?" must receive "**no — it is present in
    roughly 40–60 % of human brains (PRESENCE_PROBABILITY =
    0.5)**."
[ ] Any downstream code querying "what happens when the
    lunate sulcus is absent?" must receive "the lateral
    V1/V2 border is **not visible as a surface sulcus**,
    but it is **still architectonically marked by the stria
    of Gennari's disappearance**."
[ ] Any downstream code querying "what white-matter bundle
    runs beneath the lunate sulcus?" must receive "**none**
    — the lunate sulcus is a pure cortical-transition
    landmark (V1 to V2)."
[ ] Any downstream code assigning **field-defect anchors**
    must route through the **calcarine sulcus**, not the
    lunate sulcus.
[ ] Any downstream code assigning **prosopagnosia** must
    note the right lunate sulcus's **upstream V1
    contribution** to the right V4v → LOC → right FFA
    chain.
[ ] Any downstream code assigning **visuospatial deficits**
    must note the right lunate sulcus's V1 territory role
    in the right hemisphere's visuospatial substrate.
[ ] **The forward-reference caveat is byte-identical to the
    left sibling's.**
[ ] **The sub-regional flag is documented** — the parent
    inversion function must record `v1_lateral_territory`
    and `v2_lateral_territory` with a `SUB_REGION = True`
    flag.
[ ] **The lunate sulcus's inconstancy is documented as a
    species-level property, not a hemisphere-level one.**
"""