"""
Orbital Sulcus (OS) — Right Hemisphere
=======================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
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
``../../left/cortex/frontal/sulci/orbital_sulcus``. Structural fields
(SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
are identical by contract; geometric and clinical fields (VARIANTS,
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

**Right-hemisphere specificity**: the right OFC is the **dominant node
for reward processing** and for the **affective valuation of outcomes**
, in contrast to the left OFC's gustatory and working-memory emphasis
 . The right amygdala–OFC projection is
**denser than the left's**, and right OFC damage produces more severe
affective disinhibition, impaired reversal learning, and social
inappropriateness than left OFC damage of comparable size
 . This functional asymmetry is what the right-hemisphere VARIANTS,
CLINICAL_ANCHORS, and CONNECTIVITY fields are built around.

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

**This field is byte-identical to the left-hemisphere sibling.** The
topology of which gyrus lies on which side of which component is
hemisphere-invariant.

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
prefrontal cortex. On the right, the lateral orbital gyrus and its
caudal transition into BA 47 are the substrate of **affective
valuation and emotion regulation**; on the left, the same transition
supports semantic control.

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

Interpretation (right-hemisphere functional annotations):

    BA 11   rostral / lateral orbital gyri and medial orbital gyrus
            — medial orbitofrontal cortex, reward valuation,
            hedonic processing

    BA 13   caudal orbital gyri and posterior orbital region —
            visceral / autonomic integration, olfactory-gustatory
            convergence, punishment / reversal learning

    BA 14   caudomedial orbital cortex (inconstant in humans;
            present in some parcellations) — interoceptive
            integration

    BA 47   lateral orbital gyrus → pars orbitalis of the IFG —
            **affective valuation / emotion regulation / humor**
            (right); the right BA 47 is the affective-valuation node
            of the ventrolateral prefrontal cortex

**This field is byte-identical to the left-hemisphere sibling.** The
Brodmann-area adjacency is numerically symmetric across hemispheres;
the functional annotations above differ (right BA 47 carries affective
valuation and emotion regulation rather than the left's semantic
control) but the BA numbers do not.

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
anterior/posterior OFC boundary, and on the right this boundary is
where reward valuation (anterior) gives way to punishment/reversal
learning (posterior).

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

**This field is byte-identical to the left-hemisphere sibling.** The
component topology is hemisphere-invariant.

The **H-shape** arises when both longitudinal sulci are continuous and
the TOS connects them in the middle. The **X-shape** arises when the
longitudinal sulci cross or when the TOS is oblique. The **K-shape**
arises when one longitudinal sulcus is discontinuous and the TOS meets
the other at an angle.

--------------------------------------------------------------------------------
VARIANTS (right-hemisphere specific)
--------------------------------------------------------------------------------

The orbital sulcus is the **most morphologically variable sulcus in the
frontal lobe**. Unlike the IFS or the olfactory sulcus, whose variants
are minor deviations from a canonical form, the OS has **three major
canonical patterns** (H, X, K) and **three pattern types (Type I, II,
III)** that are used in the clinical literature as risk markers.

The right OS carries the same pattern taxonomy as the left — Type I, II,
and III mean the same thing on both sides — but the **frequency
distribution** and the **functional correlate** of each type differ.

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
        . The effect sizes are reported
        for the OFC generally; the right lateralization is not
        established.

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
        brain** as well as between individuals. Pattern
        type can differ across hemispheres — this is the reason the
        left and right OS packages each carry their own VARIANTS
        list rather than sharing one. **On the right, the H-pattern
        with a continuous lateral orbital sulcus is more strongly
        associated with intact reward-based reversal learning**,
        consistent with the right OFC's role in outcome updating
        .

These variants are **geometric and topological**, not merely metric.
Unlike the depth variants of the olfactory sulcus, the OS variants
change the **number and connectivity of the grooves** — an H has one
topology, an X has another, and a K has a third. The
``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` fields must therefore be
read as the **canonical** boundary set, with the understanding that in
atypical patterns one or more boundaries may be absent or fused.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ofc_affective_dominance
        **This is the right-OS anchor par excellence.** The right OFC
        is the **dominant node for reward processing and affective
        valuation** . Right OFC
        lesions produce more severe **affective disinhibition,
        impaired reversal learning, and social inappropriateness**
        than left OFC lesions of comparable size
        . The right lateral
        orbital sulcus and the right posterior orbital region are
        the surface landmarks for the circuits whose damage produces
        the classic "orbitofrontal syndrome."

    schizophrenia_sulcogyral_risk
        Atypical OS patterns — especially **Type III** (discontinuous
        or absent medial orbital sulcus) — are associated with
        **increased risk for schizophrenia** and with quantitative
        schizophrenia-related traits such as anhedonia
        . Decreased prevalence of the
        common Type I pattern is observed in both schizophrenia and
        bipolar disorder, making OS morphology a **transdiagnostic
        indicator of brain dysfunction** . The
        finding is reported for the OFC generally; the right side
        contributes the affective-valuation circuit that is most
        relevant to anhedonia.

    substance_use_risk
        Type III OS pattern is associated with **increased risk of
        long-term cannabis use** and of substance abuse disorders
        more broadly . The right OFC's
        role in **reward-prediction error** and **outcome updating**
        makes the right OS pattern a plausible morphological
        marker of addiction vulnerability.

    temperament_and_depressive_symptoms
        Type II OS pattern (medial orbital sulcus discontinuity) is
        associated with **low Surgency, high Negative Affectivity in
        girls, and higher depressive symptoms** in developmental
        studies . The right OFC's
        affective-valuation emphasis is consistent with this
        association, though the study did not lateralize the effect.

    orbitofrontal_epilepsy
        The OS complex is the surface landmark for **orbitofrontal
        epilepsy (OFE)**. Lateral OFE (seizure onset lateral to the
        lateral orbital sulcus) and medial OFE (onset within the
        medial orbital sulcus) are semiologically and network-wise
        distinct . Lateral OFE
        propagates to the dorsolateral frontal lobe; medial OFE
        propagates to medial frontal–cingulate/insular regions
        . The right OS
        components are the surgical landmarks for right OFE
        resection, and right OFE has a distinct affective
        semiology (ictal fear, autonomic auras) from left OFE.

    neurosurgical_corridor
        The OS is a **surgical corridor** for reaching the orbital
        surface and the subjacent white matter. The trans-sulcal
        approach through the orbital sulcus preserves the orbital
        gyral surfaces while accessing the underlying
        uncinate fasciculus and fronto-orbital tracts. On the right
        this is the approach used for right OFE surgery and for
        resections of orbital surface lesions that must preserve
        affective regulation.

    psychiatric_disorder_biomarker
        Beyond schizophrenia and bipolar disorder, OFC sulcogyral
        pattern has been proposed as a **morphological biomarker**
        for multiple psychiatric conditions — major depression,
        obsessive-compulsive disorder, and addiction
        . The right OS
        complex is the more directly relevant surface marker for
        the affective-valuation component of these conditions.

    right_amygdala_density
        The right posterior orbital region (BA 13) projects to the
        right amygdala with **greater density than the left's
        projection**. The right OS complex is therefore the surface
        landmark for the denser **OFC–amygdala** circuit that
        supports affective valuation and explicit emotion
        regulation. This is a right-only anchor; it has no
        equivalent on the left.

These anchors are **right-hemisphere-specific** in two senses: (a) the
right OFC's affective dominance and the right amygdala's denser
projection are right-lateralized facts, not general OFC facts; (b) the
right OFE semiology (ictal fear, autonomic auras) differs from the
left's. The left sibling's docstring carries the left OFC's
gustatory/working-memory emphasis and the left lateral OFC's
semantic-control role.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus complex)
--------------------------------------------------------------------------------

    uncinate_fasciculus (right)
        → traverses_beneath_lateral_orbital_sulcus
        → right_anterior_temporal_lobe
        The uncinate's orbital origin lies beneath the lateral orbital
        sulcus, connecting the lateral OFC to the right anterior
        temporal lobe. On the right it carries **affective and
        socio-emotional** OFC content (rather than the left's semantic
        / verbal content).

    fronto_orbital_tract / short orbitofrontal U-fibres
        → connects_medial_orbital_gyrus_to_lateral_orbital_gyrus
        → connects_anterior_orbital_gyrus_to_posterior_orbital_gyrus
        Short-range U-fibres cross beneath the MOS and LOS, coupling
        the orbital gyri. These are the anatomical substrate of the
        functional integration of the OFC across its sulcal
        subdivisions.

    amygdala projections (right, via posterior orbital region)
        → right_basolateral_nuclei
        → right_central_nucleus
        The right posterior orbital region (BA 13) projects to the
        right amygdala, passing beneath the caudal OS. **This
        projection is denser on the right than on the left** and is
        the anatomical substrate of the right OFC's affective-
        valuation and emotion-regulation role. The right OS complex
        is therefore the surface landmark for the denser OFC–amygdala
        circuit.

    mediodorsal_thalamic projections
        → right_mediodorsal_nucleus
        The OFC's principal thalamic relay is the mediodorsal nucleus;
        the projection passes beneath the orbital surface and through
        the anterior limb of the internal capsule. The right OFC ↔ MD
        loop is more strongly engaged during **affective** valuation
        than the left's.

    orbitofrontal_radiation (to hypothalamus / brainstem)
        → traverses_beneath_posterior_orbital_sulcus
        → hypothalamus / periaqueductal_gray
        Caudal OFC projections to autonomic and visceral targets pass
        beneath the posterior orbital region. The right OFC's
        projections to the periaqueductal gray are more strongly
        associated with **affective defensive behaviour** (ictal
        fear, autonomic auras in right OFE) than the left's.

    superior_longitudinal_fasciculus (ventral components, right)
        → traverses_beneath_lateral_orbital_sulcus
        → right_lateral_parietal_cortex
        Ventral SLF components connect the right lateral OFC to right
        posterior association cortex, supporting OFC-mediated
        affective attention and valuation interactions.

Note the relative absence of a single large dorsal association bundle
directly beneath the OS complex: unlike the IFS (arcuate, SLF III) or
the precentral sulcus (corticospinal), the OS is not the surface
landmark for one dominant fasciculus. Its white-matter relationships
are **distributed** — uncinate laterally, short U-fibres between gyri,
amygdala caudally, thalamic medially. On the right the **amygdala
component of this distribution is denser**, which is the anatomical
basis of the right OS's clinical distinctiveness.

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
    gyrus at the caudolateral end of the OS complex. On the right, this
    transition is the substrate of **affective valuation and emotion
    regulation**. The right IFG package already declares the
    **olfactory sulcus** as a boundary; it should also declare the
    **lateral orbital sulcus** once the orbital gyri packages exist.

..sulci.olfactory_sulcus
    The OS's medial neighbour. The medial orbital gyrus lies between
    the olfactory sulcus (medial) and the medial orbital sulcus
    (lateral). Both sulci declare the medial orbital gyrus as a
    boundary; the two declarations must coexist. The right olfactory
    sulcus package carries the **schizophrenia right medial orbital
    sulcus** anchor, which is adjacent to but distinct from the OS
    pattern-type anchors documented here.

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
    subdivisions. On the right, the lateral OFC's BA 47 is the
    affective-valuation node; the posterior orbital region's BA 13 is
    the punishment / reversal-learning node.

../../subcortical/medial_temporal_lobe/amygdala
    The right posterior orbital region (BA 13) projects to the right
    amygdala with **greater density than the left's**. The amygdala
    package must declare the caudal right OS as one of its cortical
    afferent corridors, and must note that the right projection is
    denser than the left's. This is the anatomical substrate of the
    right OS's affective-valuation and emotion-regulation role.

../../subcortical/medial_temporal_lobe/hippocampus
    The uncinate fasciculus, which originates beneath the lateral
    orbital sulcus, connects the right OFC to the right anterior
    temporal lobe and thence to the hippocampal formation. The
    hippocampus package must declare this route; on the right it
    carries affective / socio-emotional content rather than the left's
    semantic content.

../../left/cortex/frontal/sulci/orbital_sulcus
    The left-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
    MUST be byte-identical to this package. Geometric and clinical
    fields (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED to
    differ — the right OFC's reward/affective dominance, the right
    amygdala's denser projection, and the right OFE's affective
    semiology contrast with the left OFC's gustatory/working-memory
    emphasis and the left BA 47's semantic-control role.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "orbital_sulcus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to left
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

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "medial_orbital_sulcus": (11, 13, 14),
                              "lateral_orbital_sulcus": (11, 13, 47),
                              "transverse_orbital_sulcus": (11, 13),
                          }

    EXTENT              = {                          # identical to left
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

    VARIANTS            = (                          # DIFFERS from left
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
                              "right_H_pattern_associated_with_intact_"
                              "reward_based_reversal_learning",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from left
                              "right_ofc_affective_dominance",
                              "schizophrenia_sulcogyral_risk",
                              "substance_use_risk",
                              "temperament_and_depressive_symptoms",
                              "orbitofrontal_epilepsy_right_affective_"
                              "semiology",
                              "neurosurgical_corridor",
                              "psychiatric_disorder_biomarker",
                              "right_amygdala_density",
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
                                                 right IFG package
                                                 exists)
    medial_orbital_gyrus                       → forward reference
    anterior_orbital_gyrus                     → forward reference
    lateral_orbital_gyrus                      → forward reference
    posterior_orbital_gyrus                    → forward reference

**Four of the five bounding gyri are unresolvable.** The parent
inversion function must be explicitly parameterised to tolerate
unresolvable gyrus names for the ``orbital_sulcus`` entry, alongside
the ``olfactory_sulcus`` entry (which has three unresolvable names).

**This caveat text is byte-identical to the left sibling's.** Both
hemispheres carry it until the orbital gyri packages are created; the
right side must not silently drop it or implement a different
tolerance policy.

Once the orbital gyri packages (``medial_orbital_gyrus``,
``anterior_orbital_gyrus``, ``lateral_orbital_gyrus``, and
``posterior_orbital_gyrus``) are created under ``..gyri``, this caveat
must be removed **from both hemispheres in the same commit** and the
duality test tightened to apply uniformly.

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
  4. Mirror the promotion on the left side in the same commit.

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

Compared to ``../../left/.../orbital_sulcus``:

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
        HEMISPHERE           "right" vs "left"
        VARIANTS             same H/X/K and Type I/II/III taxonomy;
                             right carries the additional entry
                             "right_H_pattern_associated_with_intact_
                             reward_based_reversal_learning"; pattern-
                             type frequencies may differ
        CLINICAL_ANCHORS     right: reward/affective dominance,
                             denser amygdala projection, right OFE's
                             affective semiology (ictal fear,
                             autonomic auras); left: gustatory /
                             working-memory emphasis, left lateral
                             OFC's semantic-control role
        CONNECTIVITY         same bundle names; right uncinate carries
                             affective / socio-emotional content; the
                             right amygdala projection is **denser**
                             than the left's — this asymmetry is
                             intentional and is documented in both
                             packages

**The pattern-type taxonomy is hemisphere-invariant** — Type I, II, and
III mean the same thing on both sides. What may differ is the
**frequency** of each type, the **functional correlate** of a given
type, and the **density of the OFC–amygdala projection**, and those
differences belong in VARIANTS, CLINICAL_ANCHORS, and CONNECTIVITY, not
in the structural contract.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "orbital_sulcus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BOUNDING_GYRI is **compound** — a per-component dict with keys
    "medial_orbital_sulcus", "lateral_orbital_sulcus", and
    "transverse_orbital_sulcus" — and is byte-identical to the left
    sibling's BOUNDING_GYRI.
[ ] BOUNDING_GYRI names the four orbital gyri as the primary bounding
    partners (medial, anterior, lateral, posterior), with the IFG's
    pars orbitalis only as the caudolateral transition.
[ ] BRODMANN_ADJACENCY is compound, per-component, set-valued, and
    byte-identical to the left sibling's.
[ ] The BA-boundary caution is documented: orbital BA boundaries are
    architectonically subtle; the TOS is the best surface marker of
    the anterior/posterior OFC boundary.
[ ] EXTENT records the component topology (MOS and LOS longitudinal,
    TOS as the crossbar), and is byte-identical to the left sibling's.
[ ] SUBDIVISIONS is empty and byte-identical to the left sibling.
[ ] VARIANTS documents the H/X/K morphological patterns, the
    Type I/II/III clinical pattern taxonomy, the intermediate orbital
    sulcus, and the **right-specific** entry
    "right_H_pattern_associated_with_intact_reward_based_reversal_
    learning".
[ ] CLINICAL_ANCHORS contains the eight right-specific anchors:
    right_ofc_affective_dominance, schizophrenia_sulcogyral_risk,
    substance_use_risk, temperament_and_depressive_symptoms,
    orbitofrontal_epilepsy_right_affective_semiology,
    neurosurgical_corridor, psychiatric_disorder_biomarker,
    **right_amygdala_density** (the last being right-only).
[ ] CONNECTIVITY contains the six entries with right-side emphasis:
    right uncinate (affective / socio-emotional), short U-fibres,
    right amygdala (denser), right mediodorsal thalamic, right
    orbitofrontal radiation (defensive behaviour), right ventral SLF.
[ ] The right amygdala projection is documented as **denser than the
    left's** — this asymmetry is intentional and must be present in
    both packages' CONNECTIVITY notes.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.inferior_frontal_gyrus`` is the one duality link that
    resolves today (via pars orbitalis / olfactory sulcus, not yet via
    the lateral orbital sulcus).
[ ] The FORWARD-DECLARATION CAVEAT is present and is byte-identical to
    the left sibling's — four of five bounding gyri are unresolvable.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields (compound
    BOUNDING_GYRI, compound BRODMANN_ADJACENCY, component topology,
    SUBDIVISIONS) match the left sibling; VARIANTS
    (right-specific reversal-learning entry), CLINICAL_ANCHORS
    (affective dominance, right amygdala density), and CONNECTIVITY
    (denser amygdala projection) deliberately differ.
[ ] The right-only amygdala-density asymmetry is documented in the
    CONNECTIVITY section and required by the checklist — it must not
    be silently averaged away.
"""