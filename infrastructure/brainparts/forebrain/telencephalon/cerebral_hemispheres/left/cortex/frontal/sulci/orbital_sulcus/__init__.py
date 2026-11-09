"""
Orbital Sulcus (OS) — Left Hemisphere
======================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── frontal
                              └── sulci
                                    └── orbital_sulcus   ← THIS PACKAGE

This is a **compound sulcus** package. Unlike every other sulcus in the
frontal lobe, which is a single groove with two banks, the orbital
sulcus is a **family of intersecting grooves** — the medial orbital
sulcus, the lateral orbital sulcus, and the transverse orbital sulcus —
that together parcellate the orbital surface into four orbital gyri. The
term "orbital sulcus" in the singular is a **collective noun** for this
complex, and this package treats it as one anatomical object with
multiple boundary pairs.

Parent: ``..sulci`` — sibling to ``inferior_frontal_sulcus``,
``olfactory_sulcus``, ``paracentral_sulcus``, ``precentral_sulcus``, and
``superior_frontal_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/frontal/sulci/orbital_sulcus``. Structural fields
(SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, SUBDIVISIONS) are
identical by contract; geometric and clinical fields (VARIANTS,
CLINICAL_ANCHORS, CONNECTIVITY) diverge by design.

--------------------------------------------------------------------------------
WHAT THE OS IS
--------------------------------------------------------------------------------

The orbital sulcus occupies the **orbital (ventral) surface of the
frontal lobe, lateral to the olfactory sulcus**. It is not a single
groove but a **sulcal complex** with three named components:

    medial orbital sulcus (MOS)
        Runs longitudinally, rostrocaudally, in the medial half of the
        lateral orbital surface — between the medial orbital gyrus and
        the anterior / posterior orbital gyri.

    lateral orbital sulcus (LOS)
        Runs longitudinally, rostrocaudally, in the lateral half of the
        orbital surface — between the anterior / posterior orbital gyri
        and the lateral orbital gyrus.

    transverse orbital sulcus (TOS)
        Runs transversely, connecting the MOS and the LOS, and
        separating the anterior orbital gyrus (rostral) from the
        posterior orbital gyrus (caudal).

These three grooves intersect to form a pattern that **often resembles
an "H," an "X," or a "K"** . The H-shape is
the most commonly described configuration and appears to be **specific
to humans** among anthropoids . The
intersection point of the H (the "crossbar") is the transverse orbital
sulcus; the two vertical limbs are the medial and lateral orbital sulci.

A **fourth, inconstant component** — the **intermediate orbital
sulcus** — is described in some anatomical series as a short
longitudinal groove between the MOS and the LOS, and is treated here as
a **variant** rather than as a canonical component. When present, it
subdivides the anterior or posterior orbital gyrus further.

The OS complex is the surface landmark for the **orbitofrontal cortex
(OFC)** — the ventral prefrontal region that mediates reward valuation,
reversal learning, affective decision-making, and socio-emotional
regulation. The OFC is not coextensive with any one orbital gyrus; it
spans the medial, anterior, lateral, and posterior orbital gyri plus the
gyrus rectus, and the OS complex is the set of grooves that parcellates
it.

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

Because the orbital sulcus is a **compound** structure, its
``BOUNDING_GYRI`` dict has **multiple boundary pairs**, not the two
entries of a simple sulcus. The four canonical orbital gyri are the
bounding partners:

    Component              Boundary pair
    ---------------------  ------------------------------------------
    medial orbital sulcus  medial_orbital_gyrus ↔ anterior_orbital_gyrus
                           medial_orbital_gyrus ↔ posterior_orbital_gyrus

    lateral orbital       anterior_orbital_gyrus ↔ lateral_orbital_gyrus
    sulcus                posterior_orbital_gyrus ↔ lateral_orbital_gyrus

    transverse orbital    anterior_orbital_gyrus ↔ posterior_orbital_gyrus
    sulcus

In dict form, this is best expressed as a **per-component** mapping
rather than a simple direction→gyrus mapping:

    BOUNDING_GYRI = {
        "medial_orbital_sulcus": {
            "medial":  ("medial_orbital_gyrus",),
            "lateral": ("anterior_orbital_gyrus",
                        "posterior_orbital_gyrus"),
        },
        "lateral_orbital_sulcus": {
            "medial":  ("anterior_orbital_gyrus",
                        "posterior_orbital_gyrus"),
            "lateral": ("lateral_orbital_gyrus",),
        },
        "transverse_orbital_sulcus": {
            "rostral": ("anterior_orbital_gyrus",),
            "caudal":  ("posterior_orbital_gyrus",),
        },
    }

**Four of the five bounding gyri are not yet modelled as packages.**
Only ``pars_orbitalis_of_inferior_frontal_gyrus`` (via the IFG package)
resolves today. The four orbital gyri — ``medial_orbital_gyrus``,
``anterior_orbital_gyrus``, ``lateral_orbital_gyrus``, and
``posterior_orbital_gyrus`` — are **forward references**. See the
FORWARD-DECLARATION CAVEAT below.

**Note on the medial orbital gyrus and the olfactory sulcus.** The
medial orbital gyrus lies between the **olfactory sulcus** (medially)
and the **medial orbital sulcus** (laterally). It is therefore bounded
by two sulci, not one. The olfactory sulcus package already declares
the medial orbital gyrus as its lateral boundary; this package declares
it as the medial boundary of the MOS. Both declarations must coexist
when the gyrus package is created.

**Note on the lateral orbital gyrus and the IFG.** The lateral orbital
gyrus transitions caudolaterally into the **pars orbitalis of the
inferior frontal gyrus** (BA 47). The lateral orbital sulcus is
therefore the boundary between the OFC proper and the ventrolateral
prefrontal cortex. The IFG package already declares the **olfactory
sulcus** as a boundary; it does not yet declare the lateral orbital
sulcus, but should once the orbital gyri packages are built out.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Component              Brodmann areas abutting the sulcus
    ---------------------  ----------------------------------------
    medial orbital sulcus  BA 11, BA 13, BA 14
    lateral orbital       BA 11, BA 13, BA 47
    sulcus
    transverse orbital    BA 11, BA 13
    sulcus

Interpretation (left-hemisphere functional annotations):

    BA 11   rostral / lateral orbital gyri and medial orbital gyrus
            — medial orbitofrontal cortex, reward valuation,
            hedonic processing

    BA 13   caudal orbital gyri and posterior orbital region —
            visceral / autonomic integration, olfactory-gustatory
            convergence

    BA 14   caudomedial orbital cortex (inconstant in humans;
            present in some parcellations) — interoceptive
            integration

    BA 47   lateral orbital gyrus → pars orbitalis of the IFG —
            semantic retrieval / affective valuation (left);
            the left BA 47 is the semantic-control node of the
            ventrolateral prefrontal cortex

**A caution about orbital Brodmann boundaries.** As with the olfactory
sulcus, the BA boundaries on the orbital surface are **architectonically
subtle and do not always coincide with the visible sulci**. Brodmann's
own map did not parcellate the OFC in detail , and
modern cytoarchitectonic studies (Öngür, Ferry & Price 2003; Petrides &
Mackey 2006) use different schemes. The ``BRODMANN_ADJACENCY`` dict is
therefore **set-valued per component** and must be read as "which areas
may abut this component somewhere along its length," not as a precise
one-to-one mapping.

A useful empirical anchor from the literature: the **transverse orbital
sulcus corresponds roughly to the transition between the rostral
(anterior) and caudal (posterior) subdivisions of the OFC**
. This makes the TOS the most functionally
meaningful component of the complex — it is the surface marker of the
anterior/posterior OFC boundary.

--------------------------------------------------------------------------------
EXTENT (landmarks and topology)
--------------------------------------------------------------------------------

Because the OS is a compound, the EXTENT dict records the **topological
connectivity** of its components rather than two endpoint landmarks:

    medial orbital sulcus
        Rostral end: fades into the medial orbital gyrus near the
        frontal pole, lateral to the olfactory sulcus.
        Caudal end: approaches the posterior orbital region; may fuse
        with the transverse orbital sulcus or terminate independently.

    lateral orbital sulcus
        Rostral end: fades into the lateral orbital gyrus / pars
        orbitalis region.
        Caudal end: approaches the posterior orbital region, near the
        caudal boundary of the OFC.

    transverse orbital sulcus
        Medial end: joins the medial orbital sulcus.
        Lateral end: joins the lateral orbital sulcus.
        The TOS is the **crossbar of the H** — it is defined by its
        junctions with the two longitudinal components, not by free
        endpoints.

The **H-shape** arises when both longitudinal sulci are continuous and
the TOS connects them in the middle. The **X-shape** arises when the
longitudinal sulci cross or when the TOS is oblique. The **K-shape**
arises when one longitudinal sulcus is discontinuous and the TOS meets
the other at an angle.

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

The orbital sulcus is the **most morphologically variable sulcus in the
frontal lobe**. Unlike the IFS or the olfactory sulcus, whose variants
are minor deviations from a canonical form, the OS has **three major
canonical patterns** (H, X, K) and **three pattern types (Type I, II,
III)** that are used in the clinical literature as risk markers.

    H_pattern                   most common in humans
        The medial and lateral orbital sulci are both continuous and
        are connected by a transverse orbital sulcus, forming an
        "H." This pattern appears to be **specific to humans** among
        anthropoids and is the most frequently described
        configuration in anatomical series.

    X_pattern                   ~10 %
        The longitudinal sulci cross, or the transverse sulcus is
        oblique, forming an "X." Reported at approximately **9.7 %**
        in one large anatomical series.

    K_pattern                   less common
        One longitudinal sulcus is discontinuous and the transverse
        sulcus meets the other at an angle, forming a "K."

    Type_I_pattern              most common; "common" OFC pattern
        The canonical H-shaped configuration with a continuous medial
        orbital sulcus and a continuous lateral orbital sulcus. This
        is the **most prevalent** pattern in healthy populations and
        is the reference pattern against which atypical patterns are
        compared.

    Type_II_pattern             intermediate
        Discontinuity of the medial orbital sulcus, with continuity
        of the lateral orbital sulcus. Associated with **low
        Surgency, high Negative Affectivity (in girls), and higher
        depressive symptoms** in temperamental-risk studies
        .

    Type_III_pattern            atypical; risk-associated
        A discontinuous or absent medial orbital sulcus with a
        continuous lateral orbital sulcus, or other atypical
        configurations. Associated with **increased risk for
        schizophrenia, bipolar disorder, and substance abuse**
        . The Type III pattern is the most
        clinically studied variant of the OS complex.

    intermediate_orbital_sulcus  inconstant; ~additional sulcus
        A short longitudinal groove between the MOS and the LOS,
        described in some anatomical series as a fifth main orbital
        sulcus . When present, it
        further subdivides the anterior or posterior orbital gyrus.
        It is not part of the canonical H/X/K complex and is treated
        here as a variant.

    left_right_asymmetry         marked individual and hemispheric
                                 differences
        The OS pattern differs **between hemispheres within the same
        brain** as well as between individuals. The
        left and right OS complexes are not mirror images; pattern
        type can differ across hemispheres. This is one of the
        reasons the left and right OS packages must each carry their
        own VARIANTS list rather than sharing one.

These variants are **geometric and topological**, not merely metric.
Unlike the depth variants of the olfactory sulcus, the OS variants
change the **number and connectivity of the grooves** — an H has one
topology, an X has another, and a K has a third. The
``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` fields must therefore be
read as the **canonical** boundary set, with the understanding that in
atypical patterns one or more boundaries may be absent or fused.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    schizophrenia_sulcogyral_risk
        Atypical OS patterns — especially **Type III** (discontinuous
        or absent medial orbital sulcus) — are associated with
        **increased risk for schizophrenia** and with quantitative
        schizophrenia-related traits such as anhedonia
        . Decreased prevalence of the
        common Type I pattern is observed in both schizophrenia and
        bipolar disorder, making OS morphology a **transdiagnostic
        indicator of brain dysfunction** . This is
        the most robust clinical anchor for the OS complex and is
        present on both hemispheres, though the specific pattern
        frequencies may differ.

    substance_use_risk
        Type III OS pattern is associated with **increased risk of
        long-term cannabis use** and of substance abuse disorders
        more broadly . The
        mechanism is thought to involve altered OFC-mediated
        reward valuation and impulse control.

    temperament_and_depressive_symptoms
        Type II OS pattern (medial orbital sulcus discontinuity) is
        associated with **low Surgency, high Negative Affectivity in
        girls, and higher depressive symptoms** in developmental
        studies . This is a
        dimensional/temperamental risk marker rather than a
        categorical diagnosis.

    orbitofrontal_epilepsy
        The OS complex is the surface landmark for **orbitofrontal
        epilepsy (OFE)**. Lateral OFE (seizure onset lateral to the
        lateral orbital sulcus) and medial OFE (onset within the
        medial orbital sulcus) are semiologically and network-wise
        distinct . Lateral OFE
        propagates to the dorsolateral frontal lobe; medial OFE
        propagates to medial frontal–cingulate/insular regions
        . The OS
        components are the surgical landmarks for OFE resection.

    neurosurgical_corridor
        The OS is a **surgical corridor** for reaching the orbital
        surface and the subjacent white matter. The trans-sulcal
        approach through the orbital sulcus preserves the orbital
        gyral surfaces while accessing the underlying
        uncinate fasciculus and fronto-orbital tracts. This is
        relevant for OFE surgery and for resections of orbital
        surface lesions.

    psychiatric_disorder_biomarker
        Beyond schizophrenia and bipolar disorder, OFC sulcogyral
        pattern has been proposed as a **morphological biomarker**
        for multiple psychiatric conditions — major depression,
        obsessive-compulsive disorder, and addiction
        . The OS complex
        is the most accessible surface marker of OFC
        development.

    left_lateralization_note
        Functional imaging suggests that the **left OFC** is more
        engaged in **gustatory perception and working-memory**
        components of OFC function, while the right OFC is more
        engaged in **reward** processing
        . This is a
        left-hemisphere functional emphasis, not a
        left-exclusive function — both hemispheres participate in
        both, but the balance differs.

These anchors are **left-hemisphere-specific only in emphasis**: the
schizophrenia, substance-use, and temperament findings are reported for
the OFC generally and are not strictly lateralized, but the left OFC's
gustatory/working-memory emphasis and the left lateral orbital sulcus's
role in semantic-control-adjacent BA 47 give the left OS a distinct
functional profile. The right sibling's docstring carries the
right-lateralized reward-processing emphasis.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus complex)
--------------------------------------------------------------------------------

    uncinate_fasciculus (left)
        → traverses_beneath_lateral_orbital_sulcus
        → left_anterior_temporal_lobe
        The uncinate's orbital origin lies beneath the lateral orbital
        sulcus, connecting the lateral OFC to the anterior temporal
        lobe. On the left it carries semantic and verbal OFC content.

    fronto_orbital_tract / short orbitofrontal U-fibres
        → connects_medial_orbital_gyrus_to_lateral_orbital_gyrus
        → connects_anterior_orbital_gyrus_to_posterior_orbital_gyrus
        Short-range U-fibres cross beneath the MOS and LOS, coupling
        the orbital gyri. These are the anatomical substrate of the
        functional integration of the OFC across its sulcal
        subdivisions.

    amygdala projections (left, via posterior orbital region)
        → left_basolateral_nuclei
        → left_central_nucleus
        The left posterior orbital region (BA 13) projects to the left
        amygdala, passing beneath the caudal OS. This circuit supports
        affective valuation and emotion regulation. The projection is
        present on both sides but the right is denser (see the right
        sibling).

    mediodorsal_thalamic projections
        → left_mediodorsal_nucleus
        The OFC's principal thalamic relay is the mediodorsal nucleus;
        the projection passes beneath the orbital surface and through
        the anterior limb of the internal capsule.

    orbitofrontal_radiation (to hypothalamus / brainstem)
        → traverses_beneath_posterior_orbital_sulcus
        → hypothalamus / periaqueductal_gray
        Caudal OFC projections to autonomic and visceral targets pass
        beneath the posterior orbital region.

    superior_longitudinal_fasciculus (ventral components)
        → traverses_beneath_lateral_orbital_sulcus
        → lateral_parietal_cortex
        Ventral SLF components connect the lateral OFC to posterior
        association cortex, supporting OFC-mediated attentional and
        valuation interactions.

Note the relative absence of a single large dorsal association bundle
directly beneath the OS complex: unlike the IFS (arcuate, SLF III) or
the precentral sulcus (corticospinal), the OS is not the surface
landmark for one dominant fasciculus. Its white-matter relationships
are **distributed** — uncinate laterally, short U-fibres between gyri,
amygdala caudally, thalamic medially.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri  (FORWARD REFERENCES — see the caveat below)
    The four orbital gyri — ``medial_orbital_gyrus``,
    ``anterior_orbital_gyrus``, ``lateral_orbital_gyrus``, and
    ``posterior_orbital_gyrus`` — are **not yet packages** under
    ``..gyri``. When they are created, each must declare the orbital
    sulcus components as boundaries, and the duality contract will then
    apply fully. Until then, this package's BOUNDING_GYRI names are
    forward-declared strings.

..gyri.inferior_frontal_gyrus
    The pars orbitalis (BA 47) transitions from the lateral orbital
    gyrus at the caudolateral end of the OS complex. The IFG package
    already declares the **olfactory sulcus** as a boundary; it
    should also declare the **lateral orbital sulcus** once the
    orbital gyri packages exist.

..sulci.olfactory_sulcus
    The OS's medial neighbour. The medial orbital gyrus lies between
    the olfactory sulcus (medial) and the medial orbital sulcus
    (lateral). Both sulci declare the medial orbital gyrus as a
    boundary; the two declarations must coexist.

..sulci.inferior_frontal_sulcus
    The IFS's rostral end often fuses with the **lateral orbital
    sulcus** (a component of this compound). When that fusion is
    present, the IFS and the lateral orbital sulcus form a single
    continuous groove, and the boundary between the lateral frontal
    convexity and the orbital surface is shared.

..brodmann_areas.brodmann_area_11
..brodmann_areas.brodmann_area_13
..brodmann_areas.brodmann_area_14
..brodmann_areas.brodmann_area_47
    The four BAs abutting the OS components. Each must declare the
    relevant OS component as a boundary once the BA packages exist.
    (Note: these packages are not yet modelled in
    ``frontal/brodmann_areas/``; the forward references are reserved
    so they can be wired up when the BA packages are created.)

..cortex.prefrontal_cortex
    The OS complex parcellates the **orbitofrontal cortex**, which is
    a major subdivision of the prefrontal cortex. The
    prefrontal_cortex package must declare the OS as the **surface
    parcellation** of the OFC's medial/lateral and anterior/posterior
    subdivisions. On the left, the lateral OFC's BA 47 is the
    semantic-control node; on the right it is the affective-valuation
    node.

../../subcortical/medial_temporal_lobe/amygdala
    The left posterior orbital region (BA 13) projects to the left
    amygdala, passing beneath the caudal OS. The amygdala package
    must declare the caudal OS as one of its cortical afferent
    corridors, with left-side semantic/affective emphasis and
    right-side denser affective valuation.

../../subcortical/medial_temporal_lobe/hippocampus
    The uncinate fasciculus, which originates beneath the lateral
    orbital sulcus, connects the OFC to the anterior temporal lobe
    and thence to the hippocampal formation. The hippocampus package
    must declare this route.

../../right/cortex/frontal/sulci/orbital_sulcus
    The right-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, SUBDIVISIONS) MUST be
    byte-identical to this package. Geometric and clinical fields
    (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED to differ
    — the left OFC's gustatory/working-memory emphasis and the left
    BA 47's semantic-control role contrast with the right OFC's
    reward-processing emphasis and the right amygdala's denser
    projection.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "orbital_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to right
                              "medial_orbital_sulcus": {
                                  "medial":  ("medial_orbital_gyrus",),
                                  "lateral": ("anterior_orbital_gyrus",
                                              "posterior_orbital_gyrus"),
                              },
                              "lateral_orbital_sulcus": {
                                  "medial":  ("anterior_orbital_gyrus",
                                              "posterior_orbital_gyrus"),
                                  "lateral": ("lateral_orbital_gyrus",),
                              },
                              "transverse_orbital_sulcus": {
                                  "rostral": ("anterior_orbital_gyrus",),
                                  "caudal":  ("posterior_orbital_gyrus",),
                              },
                          }

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "medial_orbital_sulcus": (11, 13, 14),
                              "lateral_orbital_sulcus": (11, 13, 47),
                              "transverse_orbital_sulcus": (11, 13),
                          }

    EXTENT              = {
                              "medial_orbital_sulcus": {
                                  "rostral": ("frontal_pole",
                                              "medial_orbital_gyrus"),
                                  "caudal":  ("posterior_orbital_region",),
                              },
                              "lateral_orbital_sulcus": {
                                  "rostral": ("lateral_orbital_gyrus",),
                                  "caudal":  ("posterior_orbital_region",),
                              },
                              "transverse_orbital_sulcus": {
                                  "medial":  ("medial_orbital_sulcus",),
                                  "lateral": ("lateral_orbital_sulcus",),
                              },
                          }

    VARIANTS            = (                          # DIFFERS from right
                              "H_pattern_most_common_human_specific",
                              "X_pattern_~10%",
                              "K_pattern_less_common",
                              "Type_I_pattern_most_prevalent_healthy",
                              "Type_II_pattern_medial_discontinuity_"
                              "temperament_risk",
                              "Type_III_pattern_atypical_"
                              "psychiatric_risk",
                              "intermediate_orbital_sulcus_inconstant",
                              "left_right_asymmetry_pattern_type_"
                              "may_differ_across_hemispheres",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "schizophrenia_sulcogyral_risk",
                              "substance_use_risk",
                              "temperament_and_depressive_symptoms",
                              "orbitofrontal_epilepsy",
                              "neurosurgical_corridor",
                              "psychiatric_disorder_biomarker",
                              "left_gustatory_working_memory_emphasis",
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

Note: ``SUBDIVISIONS`` is an empty tuple — the OS is a leaf sulcus. The
three named components (MOS, LOS, TOS) are **not** sub-packages; they
are captured inside ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and
``EXTENT`` as per-component keys. If a future parcellation promotes
them to sub-packages, see the PROMOTION RULE below.

No behaviour. This package is a declarative descriptor; all computation
that references the OS lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT (unique to this sulcus)
--------------------------------------------------------------------------------

The parent ``..sulci`` duality contract states: *every gyrus named in
any BOUNDING_GYRI MUST exist in ``..gyri.GYRI``.* **The orbital sulcus
is the sulcus for which this holds least well.**

Of the five gyrus names in this package's BOUNDING_GYRI:

    pars_orbitalis_of_inferior_frontal_gyrus   → resolves today (the
                                                 IFG package exists)
    medial_orbital_gyrus                       → forward reference
    anterior_orbital_gyrus                     → forward reference
    lateral_orbital_gyrus                      → forward reference
    posterior_orbital_gyrus                    → forward reference

**Four of the five bounding gyri are unresolvable.** The parent
inversion function must be explicitly parameterised to tolerate
unresolvable gyrus names for the ``orbital_sulcus`` entry, alongside
the ``olfactory_sulcus`` entry (which has three unresolvable names).

This is the **largest forward-declaration burden** in the frontal sulci
set. The orbital gyri packages should be built out **before** the
right-hemisphere orbital sulcus is written, so that the right side can
be authored without carrying the same caveat. If the right side is
written first, it must carry the identical caveat text — the two
hemispheres must not diverge in their handling of unresolved
references.

--------------------------------------------------------------------------------
PROMOTION RULE (when a sulcus component becomes a package)
--------------------------------------------------------------------------------

A sulcus is an **edge**, not a **node**, so the standard promotion rule
does not directly apply. For the orbital sulcus, the most natural
promotion is to split the **three components** into sub-packages:

    orbital_sulcus/
        __init__.py
        medial_orbital_sulcus/
            __init__.py
        lateral_orbital_sulcus/
            __init__.py
        transverse_orbital_sulcus/
            __init__.py

Then:

  1. Add the three component names to ``SUBDIVISIONS``.
  2. Keep ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and ``EXTENT`` at
     the parent level as the **union** of the components.
  3. Each component package declares its own restricted
     ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and ``EXTENT``.
  4. Mirror the promotion on the right side in the same commit.

**Duality caveat**: the orbital gyri declare the OS *as a whole* (or,
once they exist, may declare specific components). A component split
does not break the duality contract as long as the parent remains the
canonical answer to "what does the orbital sulcus bound?" and the
components refine *which part* bounds what. If the gyri are later
updated to declare components directly, that is a joint change across
all five packages (four gyri + OS) and must be made in the same commit,
in both hemispheres.

**No split should be performed while the FORWARD-DECLARATION CAVEAT is
in force.** Splitting a compound sulcus whose four bounding gyri do not
yet exist multiplies unresolved references and makes the eventual
duality reconciliation substantially harder.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../orbital_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME          "orbital_sulcus"
        LOBE                 "frontal"
        BOUNDING_GYRI        the same four-gyrus boundary set, with
                             the same per-component mapping
        BRODMANN_ADJACENCY   the same BA 11/13/14 ↔ 11/13/47 ↔ 11/13
                             adjacency
        EXTENT               the same component topology
                             (MOS/LOS longitudinal; TOS crossbar)
        SUBDIVISIONS         both empty (or both non-empty in the same
                             way, if a component split is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "left" vs "right"
        VARIANTS             same H/X/K and Type I/II/III taxonomy;
                             pattern-type frequencies may differ;
                             left-right asymmetry is itself a variant
                             entry on both sides
        CLINICAL_ANCHORS     left: gustatory / working-memory OFC
                             emphasis, left lateral OFC's semantic-
                             control role; right: reward-processing
                             emphasis, denser right amygdala
                             projection
        CONNECTIVITY         same bundle names; left uncinate carries
                             semantic / verbal content; left amygdala
                             projection is sparser than the right's

**The pattern-type taxonomy is hemisphere-invariant** — Type I, II, and
III mean the same thing on both sides. What may differ is the
**frequency** of each type and the **functional correlate** of a given
type, and those differences belong in VARIANTS and CLINICAL_ANCHORS,
not in the structural contract.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "orbital_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BOUNDING_GYRI is **compound** — a per-component dict with keys
    "medial_orbital_sulcus", "lateral_orbital_sulcus", and
    "transverse_orbital_sulcus", not a simple direction→gyrus mapping.
[ ] BOUNDING_GYRI names the four orbital gyri as the primary bounding
    partners (medial, anterior, lateral, posterior), with the IFG's
    pars orbitalis only as the caudolateral transition.
[ ] BRODMANN_ADJACENCY is compound, per-component, and set-valued.
[ ] The BA-boundary caution is documented: orbital BA boundaries are
    architectonically subtle and do not always coincide with visible
    sulci; the TOS is the best surface marker of the
    anterior/posterior OFC boundary.
[ ] EXTENT records the component topology: MOS and LOS longitudinal,
    TOS as the crossbar connecting them.
[ ] SUBDIVISIONS is empty and byte-identical to the right sibling.
[ ] VARIANTS documents the H/X/K morphological patterns AND the
    Type I/II/III clinical pattern taxonomy, with the H-shape noted as
    the human-specific common form and the X-shape at ~9.7 % in one
    anatomical series.
[ ] VARIANTS documents the **intermediate orbital sulcus** as an
    inconstant fourth component and the left-right asymmetry in
    pattern type.
[ ] CLINICAL_ANCHORS contains the seven left-specific anchors:
    schizophrenia_sulcogyral_risk, substance_use_risk,
    temperament_and_depressive_symptoms, orbitofrontal_epilepsy,
    neurosurgical_corridor, psychiatric_disorder_biomarker,
    left_gustatory_working_memory_emphasis.
[ ] CONNECTIVITY contains the six entries (uncinate, short U-fibres,
    amygdala, mediodorsal thalamic, orbitofrontal radiation, ventral
    SLF), with left-side semantic emphasis.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.inferior_frontal_gyrus`` is the one duality link that
    resolves today (via pars orbitalis / olfactory sulcus, not via the
    lateral orbital sulcus yet).
[ ] The FORWARD-DECLARATION CAVEAT is present and specifies that
    **four** of five bounding gyri are unresolvable — the largest
    forward-declaration burden in the frontal sulci set.
[ ] The recommendation to build out the orbital gyri packages before
    the right-hemisphere OS is recorded.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (compound BOUNDING_GYRI, compound BRODMANN_ADJACENCY, component
    topology, SUBDIVISIONS) match the right sibling; VARIANTS
    frequencies, CLINICAL_ANCHORS emphasis, and CONNECTIVITY content
    deliberately differ.
"""