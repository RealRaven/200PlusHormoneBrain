"""
Transverse Occipital Sulcus — Left Hemisphere
==============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── sulci
                                    └── transverse_occipital_sulcus   ← THIS PACKAGE

This is a **leaf sulcus package** describing the left hemisphere's
**transverse occipital sulcus** — the **dorsal-surface sulcus** that
separates the **lateral occipital gyri** (ventrally) from the
**parietal lobe's angular gyrus** (dorsally). It is the **only
sulcus in the occipital lobe that is a lobar boundary on the lateral
surface** (paralleling the parieto-occipital sulcus, which is the
lobar boundary on the medial surface), and it is the surface
landmark for the **V3A / V3B territory** — the dorsal extrastriate
areas that continue the dorsal motion and spatial-attention pathway.

Parent: ``..sulci`` (left occipital sulci parent) — sibling to
``calcarine_sulcus`` and ``lunate_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/occipital/sulci/transverse_occipital_sulcus``.
The sulcus name, the bounding gyri (lateral occipital gyrus
ventral, angular gyrus dorsal-parietal), the Brodmann adjacency
(BA 19 ventral, BA 39 dorsal), the **non-retinotopic lobar
boundary role**, the extent landmarks, and the connectivity
(inferior longitudinal fasciculus beneath the sulcus) are identical
on both sides; the **represented visual hemifield** and the
**clinical significance** diverge — on the left, the transverse
occipital sulcus bounds the **left lateral occipital gyrus** (whose
V3d / V4d / LOC territory feeds the left VWFA reading pathway);
on the right, it bounds the **right lateral occipital gyrus** (whose
V3d / V4d / LOC territory feeds the right FFA face pathway, and
whose V3d is the **dominant motion-boundary and dorsal-attention
substrate** in the human brain).

**The transverse occipital sulcus is a LOBAR boundary**, not an
intra-occipital sulcus. Unlike the calcarine sulcus (which
separates the cuneus from the lingual gyrus, both within the
occipital lobe) or the lunate sulcus (which separates V1 from V2
within the occipital lobe), **the transverse occipital sulcus
separates the occipital lobe from the parietal lobe** on the
lateral surface. Its **ventral bank is an occipital gyrus** (the
lateral occipital gyrus), and its **dorsal bank is a parietal
gyrus** (the angular gyrus). **The transverse occipital sulcus is
therefore the lateral-surface counterpart to the parieto-occipital
sulcus** (which is the medial-surface occipital / parietal
boundary).

**This is a structural distinction that matters for how the sulcus
is registered in the tree.** Unlike an intra-occipital sulcus, whose
two bounding gyri are both occipital, the transverse occipital
sulcus's dorsal bounding gyrus (angular gyrus) lives in the
``..parietal/gyri`` package. **The dorsal bounding relationship is
a cross-lobe reference**, and it must be cross-referenced from the
parietal package in the same commit as this package's creation.

**The transverse occipital sulcus also does NOT carry a named
retinotopic meridian.** Unlike the calcarine sulcus (whose fundus
is the horizontal meridian) and the lunate sulcus (whose banks
carry the vertical meridian when present), **the transverse
occipital sulcus is not a retinotopic landmark** — it is a lobar
boundary. **Its functional significance is as the surface landmark
for the V3A / V3B territory**, which is adjacent to but not
co-terminous with the sulcus itself.

--------------------------------------------------------------------------------
WHAT THE TRANSVERSE OCCIPITAL SULCUS IS
--------------------------------------------------------------------------------

The transverse occipital sulcus is a **horizontally oriented sulcus
on the dorsal aspect of the lateral occipital convexity**, running
**mediolaterally** across the surface between the **parietal lobe's
angular gyrus** (dorsally) and the **lateral occipital gyrus**
(ventrally). The name comes from its **transverse orientation** —
it runs perpendicular to the anteroposterior axis of the lateral
occipital lobe, distinguishing it from the anteroposteriorly
oriented sulci of the lateral surface.

**The transverse occipital sulcus separates:**

    dorsal bank    →  **angular gyrus** (parietal lobe, BA 39)
                      →  part of the **default-mode network** and
                         the **angular gyrus semantic hub**
                      →  **not** an occipital gyrus

    ventral bank   →  **lateral occipital gyrus** (occipital lobe,
                      V3d / V4d / LOC territory)
                      →  part of the **dorsal attention network**
                         via V3d → MT/V5 → IPS
                      →  part of the **ventral stream** via V4d /
                         LOC → fusiform gyrus → left VWFA or
                         right FFA

**The transverse occipital sulcus is therefore a LOBAR boundary** —
the surface groove that separates the occipital lobe's lateral
convexity from the parietal lobe's angular gyrus. **On the left,
the ventral bank is the left lateral occipital gyrus** (feeding
the left VWFA via the LOC), and **on the right, the ventral bank
is the right lateral occipital gyrus** (feeding the right FFA via
the LOC).

**The sulcus is adjacent to the V3A / V3B territory.** V3A and V3B
are the dorsal extrastriate areas that continue the dorsal motion
pathway (V3d → V3A → MT/V5 → IPS). **V3A and V3B overlap the dorsal
bank of the lateral occipital gyrus and extend into the
parietal-occipital transition zone**, and the transverse occipital
sulcus is the **surface landmark for their vicinity**. The sulcus
is **not** the boundary of V3A or V3B — it is the lobar boundary
that **bounds the region where V3A and V3B are located**.

**The transverse occipital sulcus is reliably present** — unlike
the lunate sulcus (~50 % presence), it is present in essentially
every brain. Its variants are geometric (continuity, branching,
partial fusion with adjacent sulci), not presence/absence.

**The sulcus's ventral extent** reaches the **occipital pole**
caudally, where the lateral occipital gyrus converges with the
cuneus / lingual gyrus. **The sulcus's dorsal / medial extent**
reaches the **parieto-occipital sulcus** medially, where the
occipital / parietal boundary transitions from the lateral
surface to the medial surface.

**Left-hemisphere specificity**: the left transverse occipital
sulcus bounds the **left lateral occipital gyrus** ventrally and
the **left angular gyrus** dorsally. The **left angular gyrus** is
the left hemisphere's **semantic hub** — a critical node of the
default-mode network and of the reading-related semantic network.
The **left lateral occipital gyrus**'s LOC territory feeds the
**left VWFA (reading)**. **The transverse occipital sulcus is
therefore the surface boundary between the reading-related ventral
stream (left lateral occipital gyrus → left VWFA) and the semantic
hub (left angular gyrus)** in the left hemisphere. **This is a
left-lateralized functional boundary** — the right's transverse
occipital sulcus separates the right lateral occipital gyrus (face
pathway) from the right angular gyrus (spatial attention), with a
different downstream emphasis.

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction     Gyrus(es) bounded
    ---------     --------------------------------------------------------
    ventral       **lateral_occipital_gyrus** — the lateral-surface
                  gyral child of ``..gyri``, carrying V3d, V4d,
                  and LOC territory. **On the left, feeds the left
                  VWFA reading pathway via the LOC.**
    dorsal        **angular_gyrus** — the parietal lobe's angular
                  gyrus, **a cross-lobe forward reference**. The
                  angular gyrus lives in ``..parietal/gyri``, not
                  in the occipital lobe.

**The transverse occipital sulcus is the only occipital sulcus
whose dorsal bounding gyrus is a PARIETAL gyrus, not an occipital
gyrus.** This is why it is a **lobar boundary** — its two banks
are in different lobes. The **parent ``..sulci`` inversion
function** must record the **angular gyrus as a cross-lobe
forward reference**, not as an occipital gyrus, and must defer the
angular gyrus's bounding relationship to the
``..parietal/gyri`` package.

**The angular gyrus is a forward reference in the current tree**
— it is not yet a package under ``..parietal/gyri``. When it is
created, it must declare the transverse occipital sulcus as one
of its **ventral bounding sulci**, and this package must remove
the ``angular_gyrus`` entry from its forward-reference caveat.

**The lateral occipital gyrus is a current package** — a child of
``..gyri``. It declares the transverse occipital sulcus as its
**dorsal bounding sulcus**. The duality contract between the two
packages is **within the occipital lobe** for the lateral
occipital gyrus (this package and ``..gyri/lateral_occipital_
gyrus``), and **cross-lobe** for the angular gyrus (this package
and the future ``..parietal/gyri/angular_gyrus``).

**This field is byte-identical to the right sibling's** — the
bounding gyri are topological, not lateralized.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side          Brodmann area
    -----------   --------------------------------------------------------
    ventral bank  **BA 19** — the tertiary visual cortex (V3d,
                  V4d, LOC territory within the lateral occipital
                  gyrus)
    dorsal bank   **BA 39** — the angular gyrus of the parietal
                  lobe (not an occipital BA, but the BA that
                  corresponds to the angular gyrus)

**The transverse occipital sulcus separates BA 19 (occipital,
ventral) from BA 39 (parietal, dorsal).** This is **unlike the
other occipital sulci**, which all separate two occipital BAs:
the calcarine separates BA 17 from BA 17, the lunate separates
BA 17 from BA 18, but the transverse occipital separates **BA 19
(occipital) from BA 39 (parietal)**. **The BA 39 / BA 19
transition is a lobar cytoarchitectonic boundary** — it marks the
occipital / parietal transition on the lateral surface.

**The transverse occipital sulcus is adjacent to V3A / V3B**, both
of which are **forward references** in the ``..cortex`` package.
V3A and V3B are **not BA-numbered in the classical scheme** —
they belong to the "BA 19" belt but are distinguished by
retinotopic and functional signatures. **The transverse occipital
sulcus is the surface landmark for their vicinity, but the sulcus
itself is a BA 19 / BA 39 boundary, not a V3A / V3B boundary.**

**This field is byte-identical to the right sibling's.**

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    medial end
        Reaches the **parieto-occipital sulcus** — the medial
        occipital / parietal boundary. The transverse occipital
        sulcus is the lateral-surface continuation of the
        parieto-occipital boundary; together, the two sulci
        form the **complete occipital / parietal boundary**
        (medial + lateral).

    lateral end
        Reaches the **preoccipital notch** — the lateral
        landmark on the occipital / temporal boundary, near the
        occipito-temporal junction. The transverse occipital
        sulcus does **not** extend all the way to the
        temporoparietal junction; its lateral end is at the
        preoccipital notch region.

**The transverse occipital sulcus runs mediolaterally across the
dorsal lateral occipital surface** — from the parieto-occipital
sulcus (medial) to the preoccipital notch (lateral). **Its
trajectory is perpendicular to the anteroposterior axis**, which
is why it is called "transverse" (it crosses the lateral
occipital convexity transversely).

**This field is byte-identical to the right sibling's.**

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

The transverse occipital sulcus is **reliably present in
essentially every human brain** — it is one of the more constant
sulci on the lateral occipital surface. Its variants are
**geometric** (continuity, branching, partial fusion), not
presence/absence.

    continuous_sulcus              most common (~80 %)
        A single, continuous sulcus from the parieto-occipital
        sulcus (medial) to the preoccipital notch (lateral).
        This is the **typical form** in the majority of brains.

    interrupted_or_branching       less common (~20 %)
        The sulcus is interrupted by a small bridging gyrus,
        or it has a **branching pattern** where it sends a
        secondary branch into the lateral occipital gyrus.
        **The lobar boundary is continuous across the
        interruption** — the occipital / parietal transition is
        maintained even when the sulcus is not visible as a
        single groove.

    partial_fusion_with_parieto-occipital  ~30 %
        The transverse occipital sulcus **partially fuses**
        with the **parieto-occipital sulcus** at its medial
        end, forming a continuous groove that transitions
        from the medial surface to the lateral surface. This
        is the **expected continuity** between the two
        occipital / parietal boundary markers.

    partial_fusion_with_lateral_occipitotemporal  ~15 %
        The transverse occipital sulcus **partially fuses**
        with the **lateral occipitotemporal sulcus** at its
        ventral / lateral extent, near the preoccipital notch.
        This is an individual-level variation in the surface
        groove geometry, not a functional distinction.

    left_right_asymmetry           documented
        **The transverse occipital sulcus's presence and
        trajectory are roughly symmetric across hemispheres**,
        but **the exact fusion patterns** (with the parieto-
        occipital sulcus and the lateral occipitotemporal
        sulcus) **may differ between left and right** in a
        given subject. **Any such asymmetry in a specific
        subject must be recorded in subject-specific data**,
        not hard-coded in this package's VARIANTS field.

These variants are **geometric**, not topological. The
``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` fields do not change
across them. Only the ``VARIANTS`` field records the geometric
differences, so that downstream code can query "is this subject's
transverse occipital sulcus continuous?" without hard-coding a
single geometry.

**The invariant across all variants is the lobar boundary's
presence** — the occipital / parietal transition is **always**
there, regardless of the sulcal groove's continuity. This is
analogous to the calcarine sulcus's stria of Gennari invariant
(the V1 / V2 border is always there, even when the sulcus is
interrupted).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_transverse_occipital_lobar_boundary_landmark
        **This is the left transverse occipital sulcus's
        primary clinical anchor.** The sulcus is the **lobar
        boundary between the left occipital lobe and the left
        parietal lobe** on the lateral surface. **It is the
        surface landmark for the occipital / parietal
        transition** in the left hemisphere, and it is used in
        pre-surgical planning for lesions that involve the
        occipital-parietal junction.

    left_transverse_occipital_v3a_v3b_territory_adjacency
        **The left transverse occipital sulcus's
        functional-territory anchor.** The sulcus is adjacent
        to the **V3A / V3B territory** (forward references in
        ``..cortex``). **On the left, V3A and V3B are
        present but are not the dominant dorsal-stream
        substrates** — the right V3A is the dominant motion-
        in-depth and spatial-attention substrate. **The left
        transverse occipital sulcus is therefore the surface
        landmark for the left V3A / V3B vicinity** in a region
        that is functionally subordinate to the right
        hemisphere's dorsal-stream dominance.

    left_transverse_occipital_occipital_parietal_junction_lesion
        **Lesions at the occipital-parietal junction (OPJ)** —
        which the transverse occipital sulcus marks on the
        lateral surface — can produce **a distinctive
        clinical syndrome** that includes **simultanagnosia**,
        **optic ataxia**, and **oculomotor apraxia** (Balint
        syndrome) when bilateral, and **contralateral
        visuospatial deficits** when unilateral. **On the
        left, the OPJ lesion can produce right-hemifield
        visuospatial deficits** and contribute to the broader
        parietal-lobe syndrome. **The transverse occipital
        sulcus is the surface landmark for the lateral
        aspect of the OPJ** — the medial aspect is marked by
        the parieto-occipital sulcus.

    left_transverse_occipital_angular_gyrus_boundary
        **The left transverse occipital sulcus's dorsal
        bounding gyrus is the left angular gyrus** — the left
        hemisphere's **semantic hub**. The sulcus is the
        **ventral boundary of the left angular gyrus**, and
        left angular gyrus lesions (which can be locally
        defined using the transverse occipital sulcus as the
        ventral landmark) produce **semantic deficits** —
        the left angular gyrus is involved in semantic
        retrieval, reading, and the left hemisphere's
        language-linked semantics.

    left_transverse_occipital_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from the lateral occipital cortex near the
        transverse occipital sulcus, or from the adjacent
        V3A / V3B territory. **The sulcus is a surface
        landmark for the V3A / V3B vicinity** in the
        epileptogenic zone. **Left transverse-occipital-
        adjacent auras project to the right visual field**
        and can be preceded or accompanied by **motion
        phosphenes** (from V3A / V3B involvement).

    left_transverse_occipital_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra
        that precede a migraine headache — reflects
        **cortical spreading depression** spreading across
        the occipital and parietal cortex. **The transverse
        occipital sulcus, when the spreading depression
        crosses it, is the surface landmark for the
        occipital-to-parietal transition** of the aura from
        motion/form features (occipital) to the more complex
        visuospatial features (parietal). **This anchor is
        hemisphere-invariant**, but the aura's field
        involvement is contralateral (right field on the
        left side).

    left_transverse_occipital_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** can
        involve the lateral occipital cortex near the
        transverse occipital sulcus and produce a **right
        homonymous hemianopia or quadrantic defect** with
        **right macular sparing**. **The transverse occipital
        sulcus's contribution to the infarct's clinical
        signature is as the surface landmark for the
        occipital-parietal junction** on the lateral surface
        — the PCA-territory lesion at the OPJ can produce
        the combined visual-field and visuospatial syndrome
        that defines the OPJ-lesion clinical picture.

    left_transverse_occipital_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive
        visual dysfunction — involves the occipital-parietal
        junction including the transverse occipital sulcus
        territory. **Left transverse occipital** is part of
        the substrate of the progressive dorsal-stream and
        OPJ dysfunction that produces **progressive
        simultanagnosia** and **progressive reading
        deficits** in later-stage PCA.

**The transverse occipital sulcus's clinical anchors are focused
on its lobar boundary and OPJ-landmark functions** — it is not a
primary field-defect anchor (those belong to the calcarine
sulcus), and it is not a V1/V2 border landmark (that belongs to
the lunate sulcus when present). **The transverse occipital
sulcus's distinctive anchors are**: the lobar boundary landmark,
the V3A / V3B territory adjacency, the OPJ-lesion syndrome, the
angular gyrus boundary, and the migraine / epilepsy / PCA
anchors that involve the occipital-parietal junction.

**The `left_transverse_occipital_v3a_v3b_territory_adjacency`
anchor carries a left-specific note**: on the left, V3A and V3B
are **functionally subordinate** to the right's dominance in
motion-in-depth and spatial attention. **The left transverse
occipital sulcus is still the surface landmark for the left V3A /
V3B vicinity**, but downstream code assigning motion-in-depth or
spatial-attention functions must **weight the right hemisphere
more heavily** (documented in the right sibling).

**The hemisphere-invariant anchors** — occipital epilepsy visual
auras, migraine aura, occipital infarct, and PCA — are
**documented identically in both siblings**, with the
side-appropriate field label. **The OPJ-lesion anchor is also
hemisphere-invariant** in its mechanism (the transverse occipital
sulcus marks the OPJ on both sides), but its **clinical
presentation is lateralized** (left OPJ lesions → right-hemifield
visuospatial deficits; right OPJ lesions → left-hemifield
visuospatial deficits and more severe neglect).

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    structures within / beneath the sulcus
        **inferior longitudinal fasciculus (ILF)** — the
        white-matter bundle that runs beneath the transverse
        occipital sulcus, connecting the lateral occipital
        cortex to the temporal lobe. **The ILF is the sole
        major white-matter bundle specifically associated with
        the transverse occipital sulcus**, and it is the
        substrate of the occipito-temporal connection that
        supports object recognition and visual memory. **On
        the left, the ILF connects the left lateral occipital
        gyrus (LOC) to the left fusiform gyrus / left VWFA**
        — the reading pathway's white-matter bundle.

    white-matter bundles in the vicinity (not specifically
    beneath the sulcus)
        **superior longitudinal fasciculus (SLF)** — runs more
        dorsally, in the parietal white matter, connecting
        the parietal lobe to the frontal lobe
        **optic radiation** — runs more medially / caudally,
        beneath the calcarine sulcus

**The inferior longitudinal fasciculus is the sole major
white-matter bundle specifically associated with the transverse
occipital sulcus**, and it is the substrate of the
occipito-temporal connection that supports object recognition
(via the left VWFA on the left, and the right FFA on the right).
**This is a structural difference from the calcarine sulcus**
(which has the optic radiation beneath it — a thalamo-cortical
sensory relay) **and from the lunate sulcus** (which has no major
bundle beneath it). **The transverse occipital sulcus's
white-matter association is a long-range cortico-cortical
association bundle**, not a sensory relay or a local U-fiber
tract.

**On the left, the ILF is part of the left reading pathway** —
the left lateral occipital gyrus's LOC → left fusiform gyrus →
left VWFA chain is supported by the ILF, and the transverse
occipital sulcus is the surface landmark for the dorsal aspect of
this pathway.

**On the right, the ILF is part of the right face-recognition
pathway** — the right lateral occipital gyrus's LOC → right
fusiform gyrus → right FFA chain is supported by the ILF, and
the transverse occipital sulcus is the surface landmark for the
dorsal aspect of this pathway.

**This field is broadly conserved across hemispheres**, but the
**downstream emphasis** differs — the left's ILF supports the
reading pathway, the right's supports the face pathway.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..sulci  (parent)
    The left occipital sulci parent. The transverse occipital
    sulcus is one of its three current children.

..sulci.calcarine_sulcus
    The **medial-surface V1 / V2 border marker**. **No direct
    adjacency** — the calcarine is medial, the transverse
    occipital is lateral-dorsal. **The two sulci are the
    medial and lateral landmarks, respectively, for the
    occipital lobe's boundaries with the parietal lobe** (the
    parieto-occipital sulcus is the medial lobar boundary;
    the transverse occipital is the lateral lobar boundary).

..sulci.lunate_sulcus
    The **inconstant lateral-surface V1 / V2 border marker**.
    **The transverse occipital sulcus is dorsal to the
    lunate sulcus** and may partially fuse with it when both
    are present. The lunate is at the V1 / V2 border; the
    transverse occipital is at the occipital / parietal
    border. They are different types of boundary.

..gyri.lateral_occipital_gyrus
    The **ventral bounding gyrus**. The lateral occipital
    gyrus is a **child of ``..gyri``**, and it declares the
    transverse occipital sulcus as its **dorsal bounding
    sulcus**. **On the left, the lateral occipital gyrus's
    LOC feeds the left VWFA reading pathway**, and the
    transverse occipital sulcus is the surface landmark for
    the dorsal aspect of that pathway.

..gyri  (forward reference — the angular gyrus is not yet a
    package in the tree)
    The **dorsal bounding gyrus** is the **angular gyrus**, a
    **parietal** gyrus, not an occipital one. The angular
    gyrus is a **cross-lobe forward reference** — it will be
    created under ``..parietal/gyri``, not under
    ``..occipital/gyri``. When created, it must declare the
    transverse occipital sulcus as one of its **ventral
    bounding sulci**.

..brodmann_areas.brodmann_area_19
    The **BA 19 territory of the ventral bank** (V3d, V4d,
    LOC within the lateral occipital gyrus). BA 19's
    territory extends dorsally to the transverse occipital
    sulcus, and the sulcus is the **dorsal surface landmark**
    for BA 19's lateral extent.

..brodmann_areas  (forward reference — BA 39, the angular
    gyrus BA)
    The **dorsal bounding BA is BA 39** (the angular gyrus),
    which lives in ``..parietal/brodmann_areas/``, not in
    ``..occipital/brodmann_areas/``. When BA 39 is created,
    it must declare the transverse occipital sulcus as its
    **ventral bounding sulcus**.

...cortex.v3a  (forward reference)
    The **V3A territory** is adjacent to the transverse
    occipital sulcus. **On the right, V3A is the dominant
    motion-in-depth and spatial-attention substrate**. The
    V3A package must declare the transverse occipital sulcus
    as a **surface landmark** for its vicinity.

...cortex.v3b  (forward reference)
    The **V3B territory** is adjacent to the transverse
    occipital sulcus. The V3B package must declare the
    transverse occipital sulcus as a **surface landmark** for
    its vicinity.

...cortex.v3  (V3d)
    The **V3d territory** is the caudal / dorsal overlay of
    the lateral occipital gyrus. **On the right, V3d is the
    dominant motion substrate**. The V3d package must declare
    the lateral occipital gyrus (and, indirectly, the
    transverse occipital sulcus as the gyrus's dorsal
    boundary) as its **anatomical substrate**.

...cortex.v4  (V4d)
    The **V4d territory** is the mid / lateral overlay of the
    lateral occipital gyrus. **On the left, V4d feeds the
    left LOC → left VWFA reading pathway.** The V4d package
    must declare the lateral occipital gyrus as its
    **anatomical substrate**.

...cortex.loc  (forward reference)
    The **LOC territory** is the rostral overlay of the
    lateral occipital gyrus. **On the left, LOC feeds the
    left VWFA; on the right, LOC feeds the right FFA.** The
    LOC package must declare the lateral occipital gyrus as
    its **anatomical substrate**, and must note the
    transverse occipital sulcus as the gyrus's **dorsal
    boundary**.

..cortex.temporal
    The **inferior longitudinal fasciculus** runs beneath the
    transverse occipital sulcus, connecting the lateral
    occipital cortex to the temporal lobe. **On the left,
    the ILF is part of the left reading pathway** (LOC →
    left fusiform → left VWFA). The temporal package must
    declare the ILF as one of its **white-matter tracts**
    and must note that it **runs beneath the transverse
    occipital sulcus**.

..cortex.parietal
    The **parietal lobe's angular gyrus** is the dorsal
    bounding gyrus of the transverse occipital sulcus. The
    parietal package must declare the transverse occipital
    sulcus as the **ventral boundary** of the angular
    gyrus, and must cross-reference the transverse occipital
    sulcus package from the angular gyrus package.

..cortex.frontal
    **No direct sulcal adjacency.**

..cortex.cingulate
    **No direct sulcal adjacency.**

..cortex.insular  — indirect
    No direct insular → transverse occipital sulcus
    projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **No direct LGN relationship.** The LGN is the thalamic
    relay to V1 (calcarine banks), not to the transverse
    occipital sulcus territory.

../../subcortical/medial_temporal_lobe/hippocampus
    The **inferior longitudinal fasciculus** connects the
    lateral occipital cortex (transverse occipital sulcus
    territory) to the temporal lobe, and from there to the
    parahippocampal gyrus and hippocampus. **On the right,
    the parahippocampal place area (PPA) and the
    retrosplenial complex receive visual input supporting
    scene and spatial memory**, and the ILF is part of the
    white-matter substrate. **On the left, the ILF's reading-
    pathway role (LOC → left VWFA) is the dominant
    association.**

../../right/cortex/occipital/sulci/transverse_occipital_sulcus
    The **right-hemisphere homologue**. Structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    RETINOTOPIC_ROLE, EXTENT, PRESENCE_PROBABILITY,
    VARIANTS, SUBDIVISIONS, CONNECTIVITY) MUST be
    byte-identical. The **represented visual hemifield** and
    the **clinical significance** diverge — the right
    transverse occipital sulcus bounds the **right lateral
    occipital gyrus** (whose V3d / V4d / LOC territory feeds
    the right FFA face pathway, and whose V3d is the
    **dominant motion-boundary and dorsal-attention
    substrate**), and its dorsal bounding gyrus is the
    **right angular gyrus** (right spatial-attention hub).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "transverse_occipital_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    BOUNDING_GYRI       = {                          # identical to right
                              "ventral": ("lateral_occipital_gyrus",),
                              "dorsal":  ("angular_gyrus",),
                          }
        # **The dorsal bounding gyrus (angular gyrus) is a
        # PARIETAL gyrus** — a cross-lobe reference, not an
        # occipital gyrus. The parent inversion function must
        # record the angular gyrus as a **cross-lobe forward
        # reference**.

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "ventral": (19,),   # occipital
                              "dorsal":  (39,),   # parietal
                          }
        # **The dorsal bounding BA (BA 39) is a parietal BA**
        # — a cross-lobe reference. The parent inversion
        # function must record BA 39 as a **cross-lobe forward
        # reference**.

    EXTENT              = {                          # identical to right
                              "medial":  ("parieto_occipital_"
                                          "sulcus",),
                              "lateral": ("preoccipital_notch",
                                          "lateral_occipito_"
                                          "temporal_sulcus"),
                          }

    PRESENCE_PROBABILITY = 1.0
        # **The transverse occipital sulcus is reliably
        # present in essentially every human brain.** Unlike
        # the lunate sulcus (~0.5), the transverse occipital
        # sulcus is not a probabilistic structure.

    RETINOTOPIC_ROLE     = "lobar_boundary_not_retinotopic"
        # **The transverse occipital sulcus is NOT a
        # retinotopic landmark** — it is a lobar boundary
        # between the occipital and parietal lobes on the
        # lateral surface. **The sulcus is adjacent to the
        # V3A / V3B territory, but the sulcus itself does not
        # mark a retinotopic meridian.**

    VISUAL_HEMIFIELD     = "right"
        # **The represented visual hemifield** for the
        # transverse occipital sulcus's ventral bounding
        # territory (the left lateral occipital gyrus). The
        # left lateral occipital gyrus carries the RIGHT
        # hemifield via its V3d / V4d / LOC overlays.
        # **Note: the sulcus itself does not carry a
        # retinotopic role; the field assignment applies to
        # the territory it bounds.**

    VARIANTS            = (                          # DIFFERS from right
                              "continuous_~80%",
                              "interrupted_or_branching_~20%",
                              "partial_fusion_with_parieto_"
                              "occipital_sulcus_~30%",
                              "partial_fusion_with_lateral_"
                              "occipitotemporal_sulcus_~15%",
                              "left_right_asymmetry_documented",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "left_transverse_occipital_lobar_"
                              "boundary_landmark",
                              "left_transverse_occipital_v3a_"
                              "v3b_territory_adjacency",
                              "left_transverse_occipital_"
                              "occipital_parietal_junction_"
                              "lesion",
                              "left_transverse_occipital_angular_"
                              "gyrus_boundary",
                              "left_transverse_occipital_"
                              "occipital_epilepsy_visual_auras",
                              "left_transverse_occipital_"
                              "migraine_visual_aura",
                              "left_transverse_occipital_"
                              "occipital_infarct_pca_"
                              "territory",
                              "left_transverse_occipital_"
                              "posterior_cortical_atrophy",
                          )

    CONNECTIVITY        = {                          # identical to right
                              "inferior_longitudinal_"
                              "fasciculus": (
                                  "traverses_beneath_transverse_"
                                  "occipital_sulcus",
                                  "connects_lateral_occipital_"
                                  "cortex_to_temporal_lobe",
                              ),
                          }
        # **The ILF is the sole major white-matter bundle
        # specifically associated with the transverse
        # occipital sulcus.** **On the left, the ILF supports
        # the LOC → left VWFA reading pathway.**

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
computation that references the transverse occipital sulcus lives
in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is one forward reference in this package's
BOUNDING_GYRI**: the **angular gyrus** (dorsal bank) is a
**parietal** gyrus, not an occipital one. **The angular gyrus
will never be a child of ``..occipital/gyri``** — it will be
created under ``..parietal/gyri``, and it must cross-reference
the transverse occipital sulcus as one of its **ventral bounding
sulci**.

**The angular gyrus is a cross-lobe forward reference**, not an
occipital-gyrus forward reference. **The parent ``..sulci``
inversion function must record the angular gyrus's bounding
relationship as a cross-lobe reference**, so that downstream code
querying "what is the dorsal bounding gyrus of the transverse
occipital sulcus?" receives "the angular gyrus, a **parietal**
gyrus, located in ``..parietal/gyri``."

**The lateral occipital gyrus (ventral bank) is a current
package** — a child of ``..gyri``. Its bounding relationship
with the transverse occipital sulcus is a **within-occipital-
lobe duality** that resolves fully.

**When the angular gyrus is created** under
``..parietal/gyri/angular_gyrus``, it must:
  1. Declare the transverse occipital sulcus as one of its
     **ventral bounding sulci**.
  2. Be cross-referenced from this package's
     ``BOUNDING_GYRI.dorsal`` entry as a **cross-lobe
     reference**.

**All forward references are byte-identical to the right
sibling's** — the angular gyrus's cross-lobe status is a
property of the occipital-parietal boundary, not of the
hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a transverse-occipital segment becomes a
package)
--------------------------------------------------------------------------------

The transverse occipital sulcus is **architectonically
continuous** across its mediolateral extent, and it is **not** a
candidate for subdivision. **No SUBDIVISIONS promotion is
recommended.**

**The one conceivable subdivision is a medial / lateral split** —
a hypothetical separation into a "medial transverse occipital
sulcus" (near the parieto-occipital sulcus) and a "lateral
transverse occipital sulcus" (near the preoccipital notch). **This
subdivision has no anatomical precedent in the tree** — the sulcus
is a single continuous groove, and its medial and lateral ends are
its EXTENT landmarks, not its sub-fields. **It is not
recommended.**

**The recommended structural treatment is to keep the transverse
occipital sulcus as a single leaf sulcus package**, with the
medial and lateral extent landmarks expressed through ``EXTENT``
and the cross-lobe dorsal bounding relationship expressed through
``BOUNDING_GYRI``.

**When the angular gyrus is created** (closing the cross-lobe
forward reference), it must declare the transverse occipital
sulcus as its **ventral bounding sulcus**, and this package must
remove the ``angular_gyrus`` entry from its forward-reference
caveat. **The lateral occipital gyrus's ventral bounding role is
already fully declared** and requires no change.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../transverse_occipital_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME                  "transverse_occipital_sulcus"
        LOBE                         "occipital"
        BOUNDING_GYRI                ventral (lateral_occipital_
                                     gyrus), dorsal (angular_gyrus)
        BRODMANN_ADJACENCY           ventral (19,), dorsal (39,)
        EXTENT                       medial (parieto_occipital_
                                     sulcus), lateral (preoccipital
                                     notch / lateral_occipito_
                                     temporal_sulcus)
        PRESENCE_PROBABILITY         1.0
        RETINOTOPIC_ROLE             "lobar_boundary_not_
                                     retinotopic"
        VARIANTS                     continuous ~80%, interrupted
                                     ~20%, partial fusion with
                                     parieto-occipital ~30%,
                                     partial fusion with lateral
                                     occipitotemporal ~15%,
                                     left-right asymmetry
                                     documented
        SUBDIVISIONS                 both empty
        CONNECTIVITY                 inferior longitudinal
                                     fasciculus (sole major bundle
                                     beneath the sulcus)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
                               — the field assignment applies to
                               the ventral bounding territory
                               (the lateral occipital gyrus),
                               not to the sulcus's retinotopic
                               role (which is None).
        CLINICAL_ANCHORS       left: left lobar boundary
                               landmark, left V3A / V3B
                               territory adjacency (functionally
                               subordinate to right dominance),
                               left OPJ-lesion syndrome, left
                               angular gyrus boundary (semantic
                               hub), left-adjacent occipital
                               epilepsy visual auras, migraine
                               aura, occipital infarct, PCA
                               (progressive simultanagnosia /
                               reading deficits).
                               right: right lobar boundary
                               landmark, right V3A / V3B
                               territory adjacency (dominant
                               dorsal-stream substrate),
                               right OPJ-lesion syndrome (more
                               severe visuospatial deficit /
                               neglect), right angular gyrus
                               boundary (spatial attention hub),
                               right-adjacent occipital epilepsy
                               visual auras, migraine aura,
                               occipital infarct, PCA (Benson
                               syndrome).

**The `VISUAL_HEMIFIELD` field is the sharpest single entry.**
The left transverse occipital sulcus bounds the left lateral
occipital gyrus (carrying the RIGHT hemifield via its V3d / V4d /
LOC overlays); the right bounds the right lateral occipital gyrus
(carrying the LEFT hemifield). **The sulcus itself has no
retinotopic role** (its `RETINOTOPIC_ROLE` is
"lobar_boundary_not_retinotopic"), but its **ventral bounding
territory** carries the contralateral visual hemifield.

**The `PRESENCE_PROBABILITY` field is byte-identical on both
sides** — 1.0 on both hemispheres. The transverse occipital
sulcus is a reliably present lobar boundary, not a probabilistic
structure.

**The `RETINOTOPIC_ROLE` field is byte-identical on both sides**
— the sulcus is a lobar boundary on both hemispheres, not a
retinotopic landmark.

**The `CONNECTIVITY` field is byte-identical on both sides** —
the inferior longitudinal fasciculus runs beneath the transverse
occipital sulcus on both hemispheres, connecting the lateral
occipital cortex to the temporal lobe. **On the left, the ILF's
downstream association is the LOC → left VWFA reading pathway;
on the right, the LOC → right FFA face pathway.**

**The right-only clinical emphasis on V3A / V3B dominance is the
second sharpest entry.** Where the left transverse occipital
sulcus's V3A / V3B adjacency anchor notes that the left's V3A /
V3B are **functionally subordinate** to the right's dominance,
the right's anchor notes that the right's V3A / V3B are the
**dominant dorsal-stream substrate**. **Downstream code assigning
motion-in-depth or spatial-attention functions must weight the
right hemisphere more heavily** — the left transverse occipital
sulcus is the surface landmark for a subordinate dorsal-stream
vicinity, and the right is the surface landmark for the dominant
one.

**The hemisphere-invariant anchors** — occipital epilepsy visual
auras, migraine aura, occipital infarct, and PCA (with the
right's Benson subtype emphasis) — are **documented identically
in both siblings**, with the side-appropriate field label. **The
OPJ-lesion anchor** is also hemisphere-invariant in its
mechanism (the transverse occipital sulcus marks the OPJ on both
sides), but its clinical presentation is lateralized (left OPJ
lesions → right-hemifield visuospatial deficits; right OPJ lesions
→ left-hemifield visuospatial deficits and more severe neglect).

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "transverse_occipital_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] BOUNDING_GYRI is byte-identical to the right sibling's:
    ventral (lateral_occipital_gyrus), dorsal (angular_gyrus).
[ ] **The dorsal bounding gyrus (angular gyrus) is documented as
    a CROSS-LOBE reference** — a parietal gyrus, not an
    occipital one.
[ ] **The lateral occipital gyrus (ventral bounding gyrus) is
    documented as a current package** — a child of ``..gyri``.
[ ] BRODMANN_ADJACENCY is byte-identical to the right sibling's:
    ventral (BA 19), dorsal (BA 39).
[ ] **The dorsal bounding BA (BA 39) is documented as a
    CROSS-LOBE reference** — a parietal BA, not an occipital
    one.
[ ] EXTENT is byte-identical to the right sibling's:
    - medial: parieto-occipital sulcus
    - lateral: preoccipital notch / lateral occipitotemporal
      sulcus
[ ] **PRESENCE_PROBABILITY = 1.0** is present — the transverse
    occipital sulcus is reliably present.
[ ] **RETINOTOPIC_ROLE = "lobar_boundary_not_retinotopic"** —
    the sulcus is NOT a retinotopic landmark, unlike the
    calcarine (horizontal meridian) and lunate (vertical
    meridian) sulci.
[ ] **The transverse occipital sulcus is documented as the
    LATERAL-surface lobar boundary** between the occipital and
    parietal lobes, paralleling the parieto-occipital sulcus
    (medial-surface lobar boundary).
[ ] **The transverse occipital sulcus is documented as adjacent
    to the V3A / V3B territory** — the dorsal extrastriate
    areas that continue the dorsal motion and spatial-attention
    pathway. **The sulcus is NOT the boundary of V3A / V3B;
    it is the surface landmark for their vicinity.**
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field — **the field assignment applies to the ventral
    bounding territory (the left lateral occipital gyrus),
    NOT to the sulcus's retinotopic role (which is None).**
[ ] VARIANTS is byte-identical to the right sibling's and
    documents:
    - continuous ~80%
    - interrupted or branching ~20%
    - partial fusion with parieto-occipital sulcus ~30%
    - partial fusion with lateral occipitotemporal sulcus ~15%
    - left-right asymmetry documented
[ ] **The invariant across all variants is the lobar boundary's
    presence** — the occipital / parietal transition is
    always there, regardless of the sulcal groove's
    continuity.
[ ] CONNECTIVITY documents:
    - **inferior longitudinal fasciculus** (ILF) — the sole
      major white-matter bundle specifically associated with
      the transverse occipital sulcus
    - **The ILF connects the lateral occipital cortex to the
      temporal lobe** — on the left, it is part of the LOC →
      left VWFA reading pathway's white-matter substrate.
[ ] CLINICAL_ANCHORS contains the left-specific anchors:
    - left_transverse_occipital_lobar_boundary_landmark
    - left_transverse_occipital_v3a_v3b_territory_adjacency
      (with the left-specific note about functional
      subordination to the right)
    - left_transverse_occipital_occipital_parietal_junction_
      lesion
    - left_transverse_occipital_angular_gyrus_boundary
    - left_transverse_occipital_occipital_epilepsy_visual_
      auras
    - left_transverse_occipital_migraine_visual_aura
    - left_transverse_occipital_occipital_infarct_pca_
      territory
    - left_transverse_occipital_posterior_cortical_atrophy
[ ] The **lobar boundary landmark** is documented as the
    primary left transverse occipital sulcus anchor.
[ ] The **V3A / V3B territory adjacency** is documented with
    the left-specific note about functional subordination to
    the right.
[ ] The **OPJ-lesion syndrome** is documented as the
    occipital-parietal junction anchor.
[ ] The **angular gyrus boundary** is documented as the
    left angular gyrus (semantic hub) boundary.
[ ] The **inferior longitudinal fasciculus** is documented as
    the sole major bundle beneath the sulcus, and its role
    in the left reading pathway (LOC → left VWFA) is noted.
[ ] **The transverse occipital sulcus is documented as
    adjacent to but distinct from V3A / V3B** — the sulcus
    is a BA 19 / BA 39 boundary, not a V3A / V3B boundary.
[ ] **The transverse occipital sulcus is documented as a
    LOBAR boundary, not an intra-occipital one** — its two
    banks are in different lobes.
[ ] **The transverse occipital sulcus's uniqueness among
    occipital sulci is documented**: it is the only
    occipital sulcus whose dorsal bounding gyrus is a
    parietal gyrus, and the only occipital sulcus whose
    Brodmann adjacency is a cross-lobe occipital / parietal
    transition (BA 19 / BA 39).
[ ] No SUBDIVISIONS promotion is recommended — the sulcus is
    a single continuous lobar boundary groove.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    EXTENT, PRESENCE_PROBABILITY, RETINOTOPIC_ROLE,
    VARIANTS, SUBDIVISIONS, CONNECTIVITY) match the right
    sibling; VISUAL_HEMIFIELD and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    transverse occipital sulcus bounds the left lateral
    occipital gyrus (RIGHT hemifield via its overlays); the
    right bounds the right lateral occipital gyrus (LEFT
    hemifield).
[ ] **The right's V3A / V3B dominance is documented** — the
    right transverse occipital sulcus's V3A / V3B
    adjacency anchor notes the right's dominance, and
    downstream code assigning motion-in-depth or
    spatial-attention functions must weight the right
    hemisphere more heavily.
[ ] Any downstream code querying "what does the left
    transverse occipital sulcus bound?" must receive "the
    left lateral occipital gyrus (ventral) and the left
    angular gyrus (dorsal — a PARIETAL gyrus, cross-lobe
    reference)."
[ ] Any downstream code querying "what does the left
    transverse occipital sulcus represent retinotopically?"
    must receive "**nothing** — the sulcus is a lobar
    boundary, not a retinotopic landmark. The territory
    it bounds (the left lateral occipital gyrus) carries
    the RIGHT visual hemifield via its V3d / V4d / LOC
    overlays."
[ ] Any downstream code querying "is the transverse
    occipital sulcus a retinotopic landmark?" must receive
    "**no** — it is a lobar boundary between the occipital
    and parietal lobes. The calcarine sulcus (horizontal
    meridian) and lunate sulcus (vertical meridian) are the
    retinotopic landmarks; the transverse occipital sulcus
    is the lobar boundary."
[ ] Any downstream code querying "what white-matter bundle
    runs beneath the transverse occipital sulcus?" must
    receive "**the inferior longitudinal fasciculus** —
    connecting the lateral occipital cortex to the temporal
    lobe. On the left, it is part of the LOC → left VWFA
    reading pathway."
[ ] Any downstream code assigning **occipital-parietal
    junction lesion anchors** must route through the
    transverse occipital sulcus (lateral aspect) and the
    parieto-occipital sulcus (medial aspect).
[ ] Any downstream code assigning **motion-in-depth or
    spatial-attention functions** to the V3A / V3B vicinity
    must weight the **right** hemisphere more heavily —
    the right V3A / V3B is the dominant substrate.
[ ] Any downstream code assigning **reading pathway
    functions** must note that the left transverse
    occipital sulcus bounds the left lateral occipital
    gyrus, whose LOC feeds the left VWFA.
[ ] Any downstream code assigning **face pathway functions**
    must note that the right transverse occipital sulcus
    bounds the right lateral occipital gyrus, whose LOC
    feeds the right FFA (documented in the right sibling).
[ ] **The forward-reference caveat is byte-identical to the
    right sibling's** — the angular gyrus is a cross-lobe
    parietal forward reference, not an occipital one.
[ ] **The transverse occipital sulcus is documented as the
    LATERAL-surface lobar boundary**, paralleling the
    parieto-occipital sulcus (medial-surface lobar
    boundary).
[ ] **The inferior longitudinal fasciculus's ILF association
    is documented as a long-range cortico-cortical bundle**,
    not a sensory relay (unlike the calcarine's optic
    radiation) or a local U-fiber tract (unlike the lunate's
    absence of a major bundle).
"""