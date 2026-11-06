"""
Calcarine Sulcus — Left Hemisphere
===================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── sulci
                                    └── calcarine_sulcus   ← THIS PACKAGE

This is a **leaf sulcus package** describing the left hemisphere's
**calcarine sulcus** — the **defining sulcus of the occipital lobe**
and the **single most functionally load-bearing sulcus in the entire
cortex**. It is the surface landmark for **V1 (the primary visual
cortex)**, and it carries **three unique properties** that no other
sulcus in the cortex shares:

  1. **Both of its banks are primary sensory cortex** — the upper
     bank is the **cuneus** (V1 dorsal representation of the lower
     contralateral field), and the lower bank is the **lingual
     gyrus** (V1 ventral representation of the upper contralateral
     field). Every other sulcus in the cortex separates cortex from
     cortex of *different* functional types; the calcarine
     separates **V1 from V1**.

  2. **Its fundus represents a named retinotopic meridian** — the
     **horizontal meridian** of the visual field is at the deepest
     part of the calcarine sulcus. This is the **only sulcus in the
     cortex** whose depth carries a named retinotopic
     representation.

  3. **It carries the architectonically visible stria of Gennari**
     on both banks — the myelinated band through layer IV that is
     visible to the naked eye, and whose **abrupt disappearance at
     the V1 / V2 border** makes the V1 / V2 boundary the most
     architectonically unambiguous boundary in the human cortex.

Parent: ``..sulci`` (left occipital sulci parent) — sibling to
``lunate_sulcus`` and ``transverse_occipital_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/occipital/sulci/calcarine_sulcus``. The
sulcus name, the bounding gyri (cuneus upper bank, lingual gyrus
lower bank), the Brodmann adjacency (BA 17 on both banks), the
horizontal-meridian retinotopic role, the stria of Gennari
architectonic signature, the extent landmarks, and the connectivity
(the optic radiation beneath the sulcus) are identical on both
sides; the **represented visual hemifield** and the **clinical
significance** diverge — on the left, the calcarine sulcus's V1
banks carry the **RIGHT** visual hemifield, and left calcarine
lesions produce **right homonymous hemianopia** with **right
macular sparing**. The right calcarine sulcus carries the mirror
arrangement (left hemifield, left homonymous hemianopia).

--------------------------------------------------------------------------------
WHAT THE CALCARINE SULCUS IS
--------------------------------------------------------------------------------

The calcarine sulcus is the **horizontal sulcus on the medial
surface of the occipital lobe**, running **caudo-rostrally** from
the **occipital pole** (caudally) to the **isthmus of the cingulate
gyrus** / **parieto-occipital sulcus** (rostrally). The name comes
from the Latin **calcar** ("spur") — the sulcus's anterior end has
a spur-like appearance where it meets the parieto-occipital sulcus.

**The sulcus's two banks are the two halves of V1.**

    upper bank       →  **cuneus** (the wedge-shaped medial-surface
                        gyrus between the parieto-occipital sulcus
                        and the calcarine sulcus)
                        →  V1 dorsal representation
                        →  **lower** contralateral visual field
                        →  **lower RIGHT field on the left side**

    lower bank       →  **lingual gyrus** (the medial-surface gyrus
                        below the calcarine sulcus)
                        →  V1 ventral representation
                        →  **upper** contralateral visual field
                        →  **upper RIGHT field on the left side**

    fundus           →  the deepest part of the sulcus
                        →  **horizontal meridian** of the visual
                           field
                        →  the boundary between the upper and
                           lower visual field representations

The **full V1 representation of the contralateral hemifield** is
therefore split across the two banks of the calcarine sulcus — the
upper field on the lower bank, the lower field on the upper bank,
and the horizontal meridian at the fundus. This is why the
calcarine sulcus is the **surface landmark for V1** in a way that no
other sulcus is the surface landmark for its cortical area.

**The stria of Gennari** is the architectonic signature that makes
this visible to the naked eye. The stria is a band of myelinated
axons running through **layer IV** of the striate cortex. It is
visible on both banks of the calcarine sulcus as a **whitish line**
in fresh or fixed specimens, and its **abrupt disappearance at the
V1 / V2 border** is the architectonic basis of the
architectonically unambiguous boundary. **BA 17 was Brodmann's
first area** (1909) precisely because the stria of Gennari made the
boundary visible without microscopy.

**The fundus and the horizontal meridian.** The deepest part of the
calcarine sulcus — the fundus — represents the **horizontal
meridian** of the visual field. This is a **direct retinotopic
correspondence between a sulcal depth and a visual field line**, and
it is the only such correspondence in the human cortex. The upper
bank above the fundus represents the lower field, the lower bank
below the fundus represents the upper field, and the transition at
the fundus is the horizontal meridian.

**The calcarine sulcus's anterior extent** reaches the **isthmus of
the cingulate gyrus** — the narrow strip of cortex that connects
the cingulate gyrus to the parahippocampal gyrus. At the isthmus,
the calcarine sulcus meets the **parieto-occipital sulcus**, which
separates the cuneus (occipital) from the precuneus (parietal). The
anterior calcarine banks are **the most rostral V1 territory** in
the hemisphere.

**The calcarine sulcus's posterior extent** reaches the **occipital
pole** — the most posterior point of the hemisphere, where the
cuneus and lingual gyrus converge and the calcarine sulcus
terminates. The **fovea (macular representation)** is at the
occipital pole, which is why macular sparing is common in calcarine
lesions (the occipital pole has a dual blood supply).

**Left-hemisphere specificity**: the left calcarine sulcus's V1
banks carry the **RIGHT visual hemifield** — the upper bank
(cuneus) carries the lower RIGHT field, and the lower bank (lingual
gyrus) carries the upper RIGHT field, with the horizontal meridian
at the fundus. **Left calcarine lesions produce right homonymous
hemianopia**, and the macular sparing is **right macular sparing**.
The left calcarine sulcus is the surface landmark for the left V1
banks that the **left reading pathway depends on** — the left V1's
right-hemifield input is the **primary visual input** to the left
V4v → LOC → left VWFA chain, and left calcarine damage that extends
into the left splenium produces **alexia without agraphia**.

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction     Gyrus(es) bounded
    ---------     --------------------------------------------------------
    upper bank    **cuneus** — the wedge-shaped medial-surface gyrus
                  between the parieto-occipital sulcus (rostral)
                  and the calcarine sulcus (caudal). The cuneus is
                  a **parent-level gyral sibling** of ``..gyri``
                  (a surface landmark for V1's dorsal bank), not a
                  child of it.
    lower bank    **lingual gyrus** — the medial-surface gyrus below
                  the calcarine sulcus, above the collateral
                  sulcus. The lingual gyrus is a **forward
                  reference** in ``..gyri`` — it is not yet a
                  package.

**This is the only sulcus in the cortex whose two banks are both
primary sensory cortex.** The upper bank (cuneus) and lower bank
(lingual gyrus) both carry V1 (BA 17), and both carry the **dorsal
and ventral halves of the same retinotopic map**. The cuneus is a
**parent-level sibling** of ``..gyri`` because its primary
functional identity is the V1 upper-bank surface landmark; the
lingual gyrus is a **forward reference** in ``..gyri`` with the
same surface-landmark role for the lower bank.

**The calcarine sulcus's duality is therefore with a parent-level
sibling (cuneus) and a forward reference (lingual gyrus), not with
two current ``..gyri`` children.** The parent ``..sulci`` inversion
function must tolerate this — the cuneus is a real package, but
the lingual gyrus is a documented forward reference.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side          Brodmann area
    -----------   --------------------------------------------------------
    upper bank    **BA 17** — the primary visual cortex (V1)
    lower bank    **BA 17** — the primary visual cortex (V1)
    fundus        **BA 17** — the horizontal meridian of V1's
                  retinotopic map

**Both banks of the calcarine sulcus are BA 17.** This is the only
sulcus in the cortex whose **entire extent abuts BA 17 on both
sides** — every other sulcus either separates two different BAs
(e.g., the central sulcus separates BA 4 from BA 3/1/2) or bounds BA
17 on one side only (e.g., the V1 / V2 border separates BA 17 from
BA 18). **The calcarine sulcus is the surface landmark for BA 17's
full extent**, and its two banks are the two halves of BA 17's
retinotopic map.

**The V1 / V2 border is architectonically marked by the abrupt
disappearance of the stria of Gennari** at the outer margin of the
calcarine cortex. This border is **not** the calcarine sulcus
itself — it is the boundary between BA 17 (calcarine banks) and BA
18 (extrastriate belt around V1). The calcarine sulcus's own banks
are entirely BA 17; the **BA 17 / BA 18 transition is at the crest
of the V1 territory**, several millimetres lateral to the calcarine
fundus on each bank.

**This is why the calcarine sulcus is the surface landmark for
BA 17's *full extent*** — both banks and the fundus are BA 17,
with the BA 17 / BA 18 border at the outer margins of the banks.

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    caudal end
        Reaches the **occipital pole** — the most posterior point
        of the hemisphere, where the cuneus and lingual gyrus
        converge and the calcarine sulcus terminates. The
        **fovea (macular representation)** is at the occipital
        pole, which is why macular sparing is common in
        calcarine lesions.

    rostral end
        Reaches the **isthmus of the cingulate gyrus** — the
        narrow strip of cortex connecting the cingulate gyrus to
        the parahippocampal gyrus. At the isthmus, the calcarine
        sulcus meets the **parieto-occipital sulcus**, which
        separates the cuneus (occipital) from the precuneus
        (parietal). The **anterior calcarine banks** are the
        most rostral V1 territory in the hemisphere.

**The calcarine sulcus runs the full anteroposterior extent of the
medial occipital surface** — from the occipital pole (caudal) to
the isthmus (rostral), with the parieto-occipital sulcus at its
anterior margin. **This is the longest sulcus on the medial
occipital surface**, and its full extent is V1 territory on both
banks.

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

The calcarine sulcus is **reliably present in essentially every
human brain** — it is one of the most constant sulci in the
cortex. Its variants are **geometric** (continuity, branching,
lateral drift), not presence/absence.

    continuous_sulcus              most common (~90 %)
        A single, continuous sulcus from the occipital pole to
        the isthmus. This is the **typical form** in the
        majority of brains, and it is the form on which the
        calcarine's retinotopic correspondence is most
        straightforward.

    interrupted_or_branching       less common (~10 %)
        The sulcus is interrupted by a **transverse gyrus** or
        by a **bridging fold** that splits it into segments.
        **The V1 territory is continuous across the interruption**
        — the banks remain V1 even when the sulcus is not
        visible as a single groove — which is why the
        **stria of Gennari**, not the sulcus itself, is the
        primary architectonic landmark for V1.

    rostral_extension_to_isthmus   most common (~70 %)
        The sulcus's anterior end reaches the isthmus of the
        cingulate gyrus and meets the parieto-occipital sulcus.
        In the other ~30 %, it terminates before the isthmus,
        and the most anterior V1 territory is not flanked by a
        visible sulcal groove.

    lateral_drift_of_anterior_end  consistent
        The **anterior end of the calcarine sulcus is more
        lateral than its posterior end**. The sulcus is not
        strictly parasagittal — it drifts laterally as it
        runs rostrally, tracking the lateral drift of the
        cuneus and lingual gyrus. This lateral drift is a
        consistent geometric feature across individuals.

    stria_of_gennari_visible       always
        The **stria of Gennari is visible on both banks** in
        essentially every brain, and its **abrupt disappearance
        at the V1 / V2 border** is the architectonically
        unambiguous boundary. **This is the one invariant
        across all calcarine variants** — even when the sulcal
        groove is interrupted or terminates early, the stria
        marks the V1 territory.

These variants are **geometric**, not topological. The
``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` fields do not change
across them. Only the ``VARIANTS`` field records the geometric
differences, so that downstream code can query "is this subject's
calcarine sulcus continuous?" without hard-coding a single geometry.

**The invariant across all variants is the stria of Gennari's
presence.** This is why the calcarine sulcus's V1 identity is
**architectonically guaranteed** in a way that no other sulcus's
cortical identity is — the stria is visible, and its boundaries are
the V1 / V2 boundaries.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_calcarine_right_homonymous_hemianopia
        **This is the left calcarine sulcus anchor par
        excellence.** A lesion of the left calcarine cortex — or
        the left optic radiation, or the left LGN — produces a
        **right homonymous hemianopia**: loss of the RIGHT half
        of the visual field in both eyes. The deficit is
        **homonymous** (both eyes lose the same side),
        **hemianopic** (half the field is lost), and
        **contralateral** (right side from a left lesion).
        This is the **single most common and most clinically
        consequential effect of a left calcarine lesion**.

    left_calcarine_right_macular_sparing
        **Macular sparing** — preservation of the central 5–10°
        of the visual field within an otherwise complete
        homonymous hemianopia — is a hallmark of **occipital
        (PCA) lesions** and is **less common** in optic-tract
        or chiasmal lesions. The mechanism is the **dual blood
        supply** of the occipital pole: the pole (where the
        fovea is over-represented) receives blood from **both
        the posterior cerebral artery (PCA) and the middle
        cerebral artery (MCA)**, whereas the anterior calcarine
        banks receive blood from the PCA alone. **On the left,
        a left calcarine lesion produces a right hemianopia
        with right macular sparing** — the fovea's dual blood
        supply survives the PCA infarct.

    cortical_blindness_bilateral
        **Bilateral calcarine lesions** produce **cortical
        blindness** — complete loss of vision despite intact
        eyes, optic nerves, and LGN. The patient has no visual
        perception but may retain pupillary light reflexes
        (the reflex arc goes through the pretectum and the
        Edinger-Westphal nucleus, not V1). **This anchor is
        hemisphere-invariant** — it appears on both sides
        with the same clinical significance.

    anton_syndrome
        **Anton syndrome** — **cortical blindness with denial
        of blindness** — is a rare complication of bilateral
        calcarine lesions. **This anchor is hemisphere-
        invariant.**

    blindsight
        **Blindsight** — residual visual function (detection,
        localization, and sometimes discrimination of stimuli)
        in the absence of conscious visual perception — is a
        well-documented phenomenon after **V1 (calcarine)
        lesions**. The residual function is mediated by
        **subcortical visual pathways** (the superior
        colliculus and the pulvinar). **This anchor is
        hemisphere-invariant.**

    left_calcarine_alexia_without_agraphia
        **Alexia without agraphia** (Dejerine 1892) — the
        patient can **write** but cannot **read what they have
        written** — results from a **left calcarine lesion that
        disconnects the intact right occipital cortex from the
        left language areas**, most classically **left PCA
        infarct involving the left calcarine cortex and the
        left splenium of the corpus callosum**. The mechanism
        is: the right hemisphere can still see (the right
        calcarine is intact), but its visual signal cannot
        reach the left VWFA because the splenium is destroyed;
        the left VWFA has no visual input. The patient can
        write (a left-hemisphere motor program) but cannot
        read (the left VWFA is disconnected from vision).
        **This is the canonical left-lateralized calcarine
        syndrome, and it has no symmetric counterpart on the
        right.**

    left_calcarine_hemianopic_alexia
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **right homonymous hemianopia** — is a
        recognized clinical entity. The patient's reading is
        slowed or impaired because they must make large
        **rightward saccades** to compensate for the missing
        right hemifield. **The deficit is milder than alexia
        without agraphia** (the reading network itself is
        intact) but is **more reading-specific** than a
        complete hemianopia alone, because the left reading
        network cannot function efficiently without the full
        right-hemifield input.

    left_calcarine_migraine_visual_aura
        **Migraine visual aura** — the transient, typically
        bilateral, scintillating scotomata and fortification
        spectra that precede a migraine headache — reflects
        **cortical spreading depression** spreading across the
        calcarine cortex. **This anchor is hemisphere-
        invariant**, but the aura's field involvement is
        contralateral (right field on the left side).

    left_calcarine_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** —
        elementary visual hallucinations (flashing lights,
        colored shapes, geometric patterns) in the
        **contralateral visual field** — is a well-
        characterized epilepsy syndrome. **The calcarine
        cortex is the source of the classic elementary visual
        aura**, and **left calcarine auras project to the
        right visual field**.

    left_calcarine_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct**
        involving the calcarine cortex produces a **right
        homonymous hemianopia**, often with **macular
        sparing**, and can also produce **alexia without
        agraphia** if the left splenium is involved. The
        left PCA territory includes the left calcarine
        cortex, the left lingual gyrus, and (via the
        posterior pericallosal artery) the left splenium.

    left_calcarine_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive
        visual dysfunction — involves the calcarine cortex
        in later stages. **Left calcarine** is part of the
        substrate of the progressive ventral stream
        dysfunction that produces progressive reading
        deficits in later-stage PCA.

    left_calcarine_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy
        syndrome)** — a clinicoradiological syndrome of
        vasogenic edema in the posterior cerebral
        circulation — can involve the calcarine cortex and
        produce **cortical blindness, quadrantic field
        defects, or visual hallucinations**. **The syndrome
        is reversible** in most cases.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left calcarine sulcus's V1 banks carry the **RIGHT visual
hemifield**, so left calcarine lesions produce **right-sided**
visual deficits; (b) the left calcarine is the **input stage of
the left reading pathway**, so left calcarine lesions can
contribute to **alexia without agraphia** and **hemianopic
alexia** that have no symmetric counterpart on the right.

**The hemisphere-invariant anchors** — cortical blindness, Anton
syndrome, blindsight, migraine aura, occipital epilepsy, PCA,
PRES, and occipital infarct — are **documented identically in
both siblings**, with the side-appropriate field label.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    structures within / beneath the sulcus
        **optic radiation (geniculocalcarine tract)** — the
        white-matter bundle from the lateral geniculate
        nucleus (LGN) to V1, running beneath the calcarine
        cortex through the temporal and parietal white matter
        and terminating in the calcarine banks. **The optic
        radiation is the sole white-matter bundle specifically
        associated with the calcarine sulcus**, and its
        integrity is the substrate of the calcarine's V1
        function. **On the left, the optic radiation carries
        the RIGHT hemifield signal.**

        **pericalcarine white matter** — the short-range
        association fibers connecting V1 to V2 along the
        V1 / V2 border (the outer margin of the calcarine
        banks).

        **callosal connections via the splenium** — the
        callosal fibers that connect the left and right
        calcarine cortex via the splenium of the corpus
        callosum. **On the left, the splenium carries the
        left-to-right and right-to-left visual signal**,
        and its damage (as in left calcarine + splenium
        infarcts) produces the **alexia without agraphia**
        syndrome.

    white-matter bundles beneath the sulcus
        **optic radiation** (see above)
        **posterior thalamic radiation** — the LGN-to-V1
        and pulvinar-to-V1 fiber bundle, running alongside
        the optic radiation
        **short-range U-fibers** — the local connections
        between the calcarine banks (V1) and the adjacent
        V2 territory

**This field is broadly conserved across hemispheres**, but the
**represented hemifield** differs — the left calcarine carries
the right hemifield via its optic radiation and splenium, and the
right carries the left hemifield.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..sulci  (parent)
    The left occipital sulci parent. The calcarine sulcus is one
    of its three current children (alongside ``lunate_sulcus``
    and ``transverse_occipital_sulcus``).

..sulci.lunate_sulcus
    The **inconstant lateral-surface sulcus** that, when present,
    marks the **V1 / V2 border on the lateral surface**. The
    lunate sulcus is **not** a boundary of the calcarine sulcus
    — it is a separate lateral-surface landmark for the same
    V1 / V2 boundary that the stria of Gennari marks
    architectonically at the calcarine's outer margins.

..sulci.transverse_occipital_sulcus
    The **dorsal-surface sulcus** that bounds the lateral
    occipital gyri. **No direct adjacency** to the calcarine
    sulcus — the two are on different surfaces of the occipital
    lobe (medial vs lateral).

..cuneus
    The **upper-bank bounding gyrus**. The cuneus is a
    **parent-level gyral sibling** of ``..gyri`` (not a child
    of it), and it cross-references the calcarine sulcus as its
    **caudal bounding sulcus**. **On the left, the cuneus's V1
    upper-bank representation carries the lower RIGHT field.**

..gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The **lower-bank bounding gyrus**. The lingual gyrus is a
    **forward reference** in ``..gyri``, and when it is created
    it must declare the calcarine sulcus as its **dorsal
    bounding sulcus**. **On the left, the lingual gyrus's V1
    lower-bank representation carries the upper RIGHT field.**

..brodmann_areas.brodmann_area_17_primary_visual
    The **cytoarchitectonic counterpart** of the calcarine
    sulcus's V1 territory. BA 17's territory is **exactly the
    calcarine banks** (both upper and lower), with the V1 / V2
    border at the outer margins. The BA 17 package must declare
    the calcarine sulcus as its **defining surface landmark**.

...cortex.primary_visual_cortex
    The **functional counterpart** of the calcarine sulcus's V1
    territory. V1's territory is **exactly the calcarine banks**
    (both upper and lower). The primary_visual_cortex package
    must declare the calcarine sulcus as its **defining surface
    landmark**, and must note that the **fundus represents the
    horizontal meridian**.

...cortex.v2
    The **V1 / V2 border** is architectonically marked by the
    **abrupt disappearance of the stria of Gennari** at the
    outer margins of the calcarine banks. The V2 package must
    cross-reference the calcarine sulcus as the **inner
    boundary of V2's territory** (V2 surrounds V1, and V1 is
    the calcarine banks).

...cortex.v3
    The **V3 territory** is further lateral (in the extrastriate
    belt), and is **not a boundary of the calcarine sulcus**.
    Recorded here to pre-empt a false cross-reference.

...cortex.v4
    Same as V3 — no direct adjacency to the calcarine sulcus.

..cortex.temporal
    The **optic radiation** runs through the temporal white
    matter en route to the calcarine cortex. **On the left, the
    optic radiation carries the right-hemifield signal** from
    the LGN to the left calcarine banks. The temporal package
    must declare the optic radiation as one of its **white-
    matter tracts** and must note that it **terminates in the
    calcarine sulcus's banks**.

..cortex.parietal
    The **posterior thalamic radiation** and the **parietal
    white matter** are adjacent to the calcarine's caudal
    extent. **No direct sulcal adjacency** — the parietal lobe's
    angular gyrus is on the lateral surface, not the medial.

..cortex.frontal
    **No direct sulcal adjacency.** The frontal lobe's posterior
    boundary is the central sulcus, far from the calcarine
    sulcus.

..cortex.cingulate
    The **isthmus of the cingulate gyrus** is at the **rostral
    extent of the calcarine sulcus**. The cingulate package
    must declare the isthmus as its **caudal extent** and must
    cross-reference the calcarine sulcus as its **caudal
    neighbour**.

..cortex.insular  — indirect
    No direct insular → calcarine sulcus projection. Recorded
    here to pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **The LGN is the thalamic relay to V1** — the optic
    radiation runs from the LGN to the calcarine banks.
    **On the left, the left LGN carries the right hemifield
    signal** to the left calcarine. The thalamus package must
    declare the LGN as the source of the optic radiation to
    the left calcarine sulcus.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **modulatory projection to V1** via
    the posterior thalamic radiation, which runs adjacent to
    the optic radiation.

../../subcortical/medial_temporal_lobe/hippocampus
    **No direct hippocampal → calcarine projection.** The
    parahippocampal gyrus is adjacent to the lingual gyrus
    (the calcarine's lower bank) but does not directly connect
    to the calcarine cortex. Recorded here to pre-empt a
    false cross-reference.

../../right/cortex/occipital/sulci/calcarine_sulcus
    The **right-hemisphere homologue**. Structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    RETINOTOPIC_ROLE, EXTENT, VARIANTS, SUBDIVISIONS,
    CONNECTIVITY) MUST be byte-identical. The **represented
    visual hemifield** and the **clinical significance**
    diverge — the right calcarine sulcus's V1 banks carry the
    **LEFT visual hemifield**, and right calcarine lesions
    produce **left homonymous hemianopia** with **left macular
    sparing**.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "calcarine_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    BOUNDING_GYRI       = {                          # identical to right
                              "upper_bank": ("cuneus",),
                              "lower_bank": ("lingual_gyrus",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "upper_bank": (17,),
                              "lower_bank": (17,),
                              "fundus":     (17,),
                          }

    EXTENT              = {                          # identical to right
                              "caudal":  ("occipital_pole",),
                              "rostral": ("isthmus_of_cingulate_gyrus",
                                          "parieto_occipital_sulcus"),
                          }

    PRESENCE_PROBABILITY = 1.0
        # **The calcarine sulcus is reliably present in
        # essentially every human brain.** Unlike the lunate
        # sulcus (~0.5), the calcarine is not a probabilistic
        # structure. Its variants are geometric, not presence/
        # absence.

    RETINOTOPIC_ROLE     = "horizontal_meridian_upper_lower_banks_dorsal_ventral_v1"
        # The **fundus** represents the **horizontal meridian**.
        # The **upper bank** (cuneus) represents the **lower**
        # contralateral field. The **lower bank** (lingual gyrus)
        # represents the **upper** contralateral field. **On the
        # left, the lower RIGHT and upper RIGHT fields.**

    VISUAL_HEMIFIELD     = "right"
        # **The represented visual hemifield** — left calcarine
        # sulcus's V1 banks carry the RIGHT hemifield.

    VARIANTS            = (                          # DIFFERS from right
                              "continuous_~90%",
                              "interrupted_or_branching_~10%",
                              "rostral_extension_to_isthmus_~70%",
                              "lateral_drift_of_anterior_end",
                              "stria_of_gennari_visible_always",
                          )
        # **Byte-identical to the right sibling's** — the
        # calcarine sulcus's geometry is not strongly
        # lateralized, and the stria of Gennari's presence is
        # invariant across hemispheres.

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "left_calcarine_right_homonymous_"
                              "hemianopia",
                              "left_calcarine_right_macular_"
                              "sparing",
                              "cortical_blindness_bilateral",
                              "anton_syndrome",
                              "blindsight",
                              "left_calcarine_alexia_without_"
                              "agraphia",
                              "left_calcarine_hemianopic_alexia",
                              "left_calcarine_migraine_visual_"
                              "aura",
                              "left_calcarine_occipital_epilepsy_"
                              "visual_auras",
                              "left_calcarine_occipital_infarct_"
                              "pca_territory",
                              "left_calcarine_posterior_cortical_"
                              "atrophy",
                              "left_calcarine_pres_visual_"
                              "symptoms",
                          )

    CONNECTIVITY        = { ... }   # as specified above, with the
                                    # optic radiation as the sole
                                    # tract beneath the sulcus

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
computation that references the calcarine sulcus lives in
``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is one forward reference in this package's
BOUNDING_GYRI**: the **lingual gyrus** (lower bank) is a forward
reference in ``..gyri`` — it is not yet a package. **The cuneus
(upper bank) is a current package** — a parent-level gyral sibling
of ``..gyri``. **The parent inversion function must tolerate the
lingual gyrus's forward-reference status** for this sulcus, and the
eventual resolution of the lingual gyrus will close this forward
reference.

**The calcarine sulcus does NOT have a
`CUNEUS_EXCLUSION_NOTE`** — the cuneus is its upper bank, not an
excluded gyrus. The cuneus sits at the ``..occipital`` parent level
(not under ``..gyri``) because its primary functional identity is
the V1 upper-bank surface landmark, but it is the **bounding gyrus
for the calcarine sulcus** just as the lingual gyrus is. **The
cuneus's parent-level placement is a tree-structural choice, not a
claim that it is not a bounding gyrus of the calcarine sulcus.**

**The calcarine sulcus is the only sulcus in the cortex whose
forward-reference caveat is limited to ONE gyrus** (the lingual
gyrus) — because its other bounding gyrus (the cuneus) is a real
package. This is why the calcarine's forward-reference burden is
much smaller than the parent ``..sulci`` package's burden (which
also includes the parieto-occipital sulcus, the lateral
occipitotemporal sulcus, the angular gyrus, and the V1/V2 lateral
territories).

**All forward references are byte-identical to the right sibling's**
— the lingual gyrus's forward-reference status is a property of the
occipital lobe's gyral decomposition, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a calcarine segment becomes a package)
--------------------------------------------------------------------------------

The calcarine sulcus is **architectonically continuous** along its
full extent (the stria of Gennari runs unbroken along both banks),
and it is **not** a candidate for subdivision. **No SUBDIVISIONS
promotion is recommended for the calcarine sulcus.**

**The one conceivable subdivision is the upper-bank / lower-bank
split** — a hypothetical separation into a "cuneus bank calcarine
sulcus" and a "lingual bank calcarine sulcus." **This subdivision
would duplicate the cuneus / lingual gyrus decomposition** — the
upper-bank and lower-bank territories are already modelled as the
cuneus and the lingual gyrus, and splitting the calcarine sulcus
by bank would create two sulcus packages that each describe half a
groove. **This has no anatomical precedent in the tree** and is
**not recommended**.

**The recommended structural treatment is to keep the calcarine
sulcus as a single leaf sulcus package**, with the upper-bank and
lower-bank duality expressed through ``BOUNDING_GYRI`` and the
``cuneus`` / ``lingual_gyrus`` packages. **This preserves the
single-groove identity of the sulcus** (which is architectonically
a single continuous feature, marked by the continuous stria of
Gennari) while maintaining the duality with the two banks.

**When the lingual gyrus is created** (closing the forward
reference), it must declare the calcarine sulcus as its **dorsal
bounding sulcus**, and the calcarine sulcus package must remove the
``lingual_gyrus`` entry from its forward-reference caveat. **The
cuneus's upper-bank role is already fully declared** and requires
no change.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../calcarine_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME                  "calcarine_sulcus"
        LOBE                         "occipital"
        BOUNDING_GYRI                upper_bank (cuneus), lower_bank
                                     (lingual gyrus)
        BRODMANN_ADJACENCY           BA 17 on upper bank, lower
                                     bank, and fundus
        EXTENT                       occipital_pole / isthmus_of_
                                     cingulate_gyrus / parieto_
                                     occipital_sulcus
        PRESENCE_PROBABILITY         1.0 — the calcarine is reliably
                                     present
        RETINOTOPIC_ROLE             "horizontal_meridian_upper_
                                     lower_banks_dorsal_ventral_v1"
        VARIANTS                     continuous ~90%, interrupted
                                     ~10%, rostral extension ~70%,
                                     lateral drift, stria of
                                     Gennari always visible
        SUBDIVISIONS                 both empty
        CONNECTIVITY                 optic radiation, posterior
                                     thalamic radiation, callosal
                                     via splenium, short-range
                                     U-fibers

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        RETINOTOPIC_ROLE       the **represented hemifield** flips
                               — the upper bank (cuneus) represents
                               the lower RIGHT field on the left
                               and the lower LEFT field on the
                               right; the lower bank (lingual
                               gyrus) represents the upper RIGHT
                               on the left and upper LEFT on the
                               right.
        CLINICAL_ANCHORS       left: right homonymous hemianopia,
                               right macular sparing, cortical
                               blindness (bilateral), Anton
                               syndrome (bilateral), blindsight,
                               **left_calcarine_alexia_without_
                               agraphia**, hemianopic alexia,
                               migraine aura, occipital epilepsy,
                               PCA (left-lateralized subtype),
                               PRES, occipital infarct.
                               right: left homonymous hemianopia,
                               left macular sparing, cortical
                               blindness (bilateral), Anton
                               syndrome (bilateral), blindsight,
                               **NO alexia without agraphia**,
                               hemianopic alexia (milder, from
                               left-hemifield loss), migraine
                               aura, occipital epilepsy, PCA
                               (Benson syndrome), PRES, occipital
                               infarct.

**The visual-hemifield asymmetry is the sharpest single entry in
this contract.** The left calcarine sulcus's V1 banks carry the
RIGHT visual hemifield; the right's carry the LEFT. This is the
canonical contralateral visual field rule, applied to the calcarine
sulcus's V1 territory.

**The macular-sparing field label flips.** A **left calcarine
lesion** produces **right homonymous hemianopia with right macular
sparing**; a **right calcarine lesion** produces **left homonymous
hemianopia with left macular sparing**.

**The alexia-without-agraphia anchor is LEFT-ONLY.** The right
calcarine sulcus does **not** carry an `alexia_without_agraphia`
anchor — that syndrome is produced by a left calcarine + left
splenium lesion, and has no symmetric counterpart on the right.
The right's `hemianopic_alexia` anchor is the milder left-
hemifield reading deficit from left-hemifield loss, and it is
weaker than the left's `hemianopic_alexia_right`.

**The hemisphere-invariant anchors** — cortical blindness, Anton
syndrome, blindsight, migraine aura, occipital epilepsy, PCA (as a
syndrome, with the left/right subtype emphasis differing), PRES,
and occipital infarct — are **documented identically in both
siblings**, with the side-appropriate field label.

**The forward-reference caveat (the lingual gyrus) is
byte-identical on both sides.**

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "calcarine_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] BOUNDING_GYRI is byte-identical to the right sibling's:
    upper_bank (cuneus), lower_bank (lingual_gyrus).
[ ] BOUNDING_GYRI names the cuneus (parent-level gyral sibling)
    and the lingual gyrus (forward reference).
[ ] **The calcarine sulcus is documented as the only sulcus in
    the cortex whose two banks are both primary sensory cortex**
    (V1 on both sides).
[ ] BRODMANN_ADJACENCY is byte-identical to the right sibling's:
    BA 17 on upper_bank, lower_bank, and fundus.
[ ] **The fundus is documented as the horizontal meridian** —
    the only sulcus in the cortex whose depth carries a named
    retinotopic representation.
[ ] EXTENT is byte-identical to the right sibling's:
    - caudal: occipital pole
    - rostral: isthmus of cingulate gyrus + parieto-occipital
      sulcus
[ ] **PRESENCE_PROBABILITY = 1.0** is present — the calcarine
    sulcus is reliably present.
[ ] RETINOTOPIC_ROLE is
    "horizontal_meridian_upper_lower_banks_dorsal_ventral_v1"
    and documents the full retinotopic map:
    - upper bank (cuneus) → lower contralateral field
      (lower RIGHT on the left)
    - lower bank (lingual gyrus) → upper contralateral field
      (upper RIGHT on the left)
    - fundus → horizontal meridian
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] VARIANTS is byte-identical to the right sibling's and
    documents:
    - continuous ~90%
    - interrupted or branching ~10%
    - rostral extension to isthmus ~70%
    - lateral drift of anterior end
    - **stria of Gennari always visible** (the invariant across
      all variants)
[ ] **The stria of Gennari is documented as the architectonic
    signature** — visible on both banks, and its abrupt
    disappearance at the V1 / V2 border is the architectonic
    basis of the V1 / V2 boundary.
[ ] **The calcarine sulcus is documented as the surface
    landmark for V1's full extent** (both banks are BA 17, with
    the V1 / V2 border at the outer margins).
[ ] CONNECTIVITY documents:
    - **optic radiation** (the sole major white-matter bundle
      specifically associated with the calcarine sulcus —
      terminates in the calcarine banks)
    - **posterior thalamic radiation** (LGN and pulvinar to V1)
    - **callosal connections via the splenium** (left-right
      calcarine coordination, and the substrate of alexia
      without agraphia)
    - **short-range U-fibers** (V1 to V2 along the V1/V2 border)
[ ] CLINICAL_ANCHORS contains the left-specific anchors:
    - left_calcarine_right_homonymous_hemianopia
    - left_calcarine_right_macular_sparing
    - cortical_blindness_bilateral
    - anton_syndrome
    - blindsight
    - **left_calcarine_alexia_without_agraphia**
    - left_calcarine_hemianopic_alexia
    - left_calcarine_migraine_visual_aura
    - left_calcarine_occipital_epilepsy_visual_auras
    - left_calcarine_occipital_infarct_pca_territory
    - left_calcarine_posterior_cortical_atrophy
    - left_calcarine_pres_visual_symptoms
[ ] The **right homonymous hemianopia** is documented as the
    primary left calcarine sulcus anchor.
[ ] **Right macular sparing** is documented with its dual-blood-
    supply mechanism.
[ ] **Cortical blindness, Anton syndrome, and blindsight** are
    documented as the hemisphere-invariant bilateral-lesion
    syndromes.
[ ] **Alexia without agraphia** is documented as the
    **left-lateralized** calcarine + splenium syndrome.
[ ] **Hemianopic alexia** is documented as the milder left-
    hemifield reading deficit, **weaker than alexia without
    agraphia**.
[ ] **The calcarine sulcus's unique properties are documented**:
    - both banks are primary sensory cortex (V1 on both sides)
    - the fundus is the horizontal meridian
    - the stria of Gennari is architectonically visible on both
      banks
    - the V1 / V2 border is architectonically unambiguous
[ ] **The calcarine sulcus's relationship to BA 17 is
    documented** — both banks are BA 17, with the V1 / V2
    border at the outer margins. BA 17's territory is **exactly**
    the calcarine banks.
[ ] **The calcarine sulcus's relationship to V1 is documented**
    — V1's territory is exactly the calcarine banks, and the
    calcarine sulcus is the defining surface landmark for V1.
[ ] **The cuneus and lingual gyrus are documented as the
    bounding gyri**, with the cuneus being a parent-level
    gyral sibling and the lingual gyrus being a forward
    reference.
[ ] **The lingual gyrus forward reference is documented**, and
    the forward-reference caveat is byte-identical to the
    right sibling's.
[ ] **The calcarine sulcus is explicitly NOT subject to a
    cuneus-exclusion note** — the cuneus is its upper bank,
    not an excluded gyrus. The cuneus's parent-level placement
    in the tree is documented as a structural choice, not a
    claim that it is not a bounding gyrus of the calcarine
    sulcus.
[ ] No SUBDIVISIONS promotion is recommended — the calcarine
    sulcus is a single continuous groove, and a bank-based
    subdivision would duplicate the cuneus / lingual gyrus
    decomposition.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (SULCUS_NAME, LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY,
    EXTENT, PRESENCE_PROBABILITY, RETINOTOPIC_ROLE,
    VARIANTS, SUBDIVISIONS, CONNECTIVITY) match the right
    sibling; VISUAL_HEMIFIELD and CLINICAL_ANCHORS deliberately
    differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    calcarine sulcus's V1 banks carry the RIGHT hemifield; the
    right's carry the LEFT hemifield.
[ ] **The macular-sparing asymmetry is verified**: the left
    calcarine sulcus carries a **right** macular sparing
    anchor; the right carries a **left** macular sparing
    anchor.
[ ] **The alexia-without-agraphia anchor is verified to be
    left-only**: the right calcarine sulcus's
    `CLINICAL_ANCHORS` must **not** include an alexia-without-
    agraphia entry (that syndrome is left-lateralized).
[ ] Any downstream code querying "what does the left calcarine
    sulcus represent?" must receive "the horizontal meridian
    at the fundus, with the upper bank (cuneus) representing
    the lower RIGHT field and the lower bank (lingual gyrus)
    representing the upper RIGHT field."
[ ] Any downstream code querying "what is the calcarine
    sulcus's architectonic signature?" must receive "the
    stria of Gennari, visible on both banks, and its abrupt
    disappearance at the V1 / V2 border."
[ ] Any downstream code querying "why is the calcarine sulcus
    the most functionally load-bearing sulcus in the cortex?"
    must receive "because both of its banks are primary
    sensory cortex (V1 on both sides), its fundus is the
    horizontal meridian (the only named retinotopic meridian
    at a sulcal depth), and the stria of Gennari makes the
    V1 / V2 border architectonically unambiguous."
[ ] Any downstream code querying "what is the calcarine
    sulcus's relationship to BA 17?" must receive "the
    calcarine banks are BA 17, with the V1 / V2 border at
    the outer margins of the banks — BA 17's territory is
    exactly the calcarine banks."
[ ] Any downstream code assigning the left reading pathway
    must note that **the left calcarine sulcus's V1 banks
    are the input stage** — the right-hemifield V1 signal is
    the primary visual input to the left V4v → LOC → left
    VWFA chain.
[ ] Any downstream code assigning **alexia without
    agraphia** must route through the **left** calcarine
    sulcus + left splenium lesion — that syndrome is
    left-lateralized and is explicitly absent on the right.
[ ] Any downstream code assigning **right homonymous
    hemianopia** must route through the **left** calcarine
    sulcus (or left optic radiation, or left LGN) — the
    left-side lesion produces the right-sided deficit.
[ ] Any downstream code assigning **right macular sparing**
    must note the **dual blood supply** (PCA + MCA at the
    occipital pole) that spares the macula in a left
    calcarine lesion.
[ ] Any downstream code querying "is the cuneus an excluded
    gyrus of the calcarine sulcus?" must receive "**no** —
    the cuneus is the calcarine's upper bank. The cuneus is
    at the ``..occipital`` parent level rather than under
    ``..gyri`` because its primary functional identity is
    the V1 upper-bank surface landmark, but it is the
    calcarine sulcus's bounding gyrus just as the lingual
    gyrus is."
[ ] **The forward-reference caveat is byte-identical to the
    right sibling's** — the lingual gyrus's forward-reference
    status is a property of the occipital lobe's gyral
    decomposition, not of the hemisphere.
[ ] **The calcarine sulcus is documented as the only sulcus
    in the cortex whose forward-reference caveat is limited
    to ONE gyrus** (the lingual gyrus) — because its other
    bounding gyrus (the cuneus) is a real package.
"""