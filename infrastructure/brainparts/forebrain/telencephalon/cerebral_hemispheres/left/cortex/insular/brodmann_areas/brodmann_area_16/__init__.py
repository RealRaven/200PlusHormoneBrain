"""
Brodmann Area 16 (Anterior Inconstant Insula) — Left Hemisphere
================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_16   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 16** — the **anterior inconstant insula**, the most
rostral and most undifferentiated of the insular Brodmann areas. It is
one of the three **anterior agranular** insular areas (BA 14, BA 15,
BA 16) and sits at the extreme rostral pole of the insula, where the
insular cortex approaches the claustrum and the prepyriform allocortex
.

Parent: ``..brodmann_areas`` (left insular BA registry) — sibling to
BA 13, BA 14, BA 41, BA 42, BA 43.

This package is the **structural mirror** of
``../../right/cortex/insular/brodmann_areas/brodmann_area_16``. The BA
number, the region label, and the **presence probability** are identical
on both sides; the **functional emphasis** and **clinical
significance** diverge — on the left, BA 16's sparse territory is
weighted toward the **parasympathetic** pole of the insular autonomic
lateralization and toward the **language-linked** component of the
anterior insula's salience and emotional-awareness functions.

--------------------------------------------------------------------------------
WHAT BA 16 IS
--------------------------------------------------------------------------------

BA 16 is the **rostralmost subdivision of the insular cortex**, defined
by Brodmann (1909) in the guenon (Old World monkey) on cytoarchitectonic
grounds. It is a **relatively undifferentiated cortical area** that
Brodmann regarded as part of the insula because of the relation of its
innermost multiform layer (VI) with the claustrum (VICl)
. The laminar organization of the cortex is
**almost totally lacking**: the molecular layer (I) is wide, the space
between layer I and layer VI is composed of a mixture of pyramidal and
spindle cells with **no significant number of granule cells**, and
pyramidal cells clump in the outer part to form **glomeruli similar to
those seen in some of the primary olfactory areas**
.

This term also refers to an area known as **peripaleocortical
claustral** — a cytoarchitecturally defined (**agranular**) portion of
the insula at its rostral extreme where it approaches most closely the
**claustrum** and the **prepyriform area**
. BA 16 is therefore structurally the
**most allocortex-like** of the insular BA territories — more so than
BA 14, which is also agranular but less extreme in its loss of laminar
organization.

**A critical caveat: BA 16 is inconstant in humans.** Brodmann
identified four areas (BA 13–BA 16) in the insular cortex of **lower
primates**, but **not in the human brain**; in humans he only identified
a **posterior granular** and an **anterior agranular** region separated
by the central sulcus of the insula
. Modern parcellations do not
consistently recover BA 16 as a discrete human territory — the anterior
agranular insula is often treated as a single field (BA 14–16) or
subdivided by modern schemes (HCP ``AAIC``, Öngür-Price ``Iai``/``Ial``)
rather than by the BA 16 label
. **BA 16 is therefore a conventional label whose human presence is
probabilistic, not a reliably identifiable architectonic entity**.
The package must carry an explicit ``PRESENCE_PROBABILITY`` field and
must not be treated by downstream code as a guaranteed territory.

BA 16 borders:

    caudally     BA 14 (ventral anterior insula) and BA 15 (inconstant
                 intermediate anterior insula) via the agranular
                 anterior insular field
    laterally    the claustrum and the extreme capsule
    medially     the prepyriform allocortex and the ventral agranular
                 orbitofrontal cortex at the limen insulae
    dorsally     the anterior short gyri of the anterior insula

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours
        caudally               BA 14 / BA 15 (agranular anterior insula)
        laterally              claustrum / extreme capsule
        medially               prepyriform allocortex /
                               ventral agranular orbitofrontal cortex
        dorsally               anterior short gyri of the anterior
                               insula

    Functional overlays
        peripaleocortical claustral interface
            BA 16's defining cytoarchitectonic feature is its
            relation to the **claustrum** and the **prepyriform
            area** — the allocortical olfactory territory
            . This is the anatomical
            substrate of BA 16's participation in the
            **olfactory-limbic** interface of the anterior insula.
        anterior insula salience network (conditional)
            When BA 16 is present, it is part of the **anterior
            granular / dysgranular insula** that, with the dorsal
            anterior cingulate, forms the **salience network**
            . The
            anterior insula is the cortical hub that detects
            behaviourally relevant stimuli and switches the brain
            between default-mode and executive networks. BA 16's
            contribution is **smaller than BA 14's** because of its
            inconstant and rostral position, but it participates in
            the same network.
        anterior insula interoception and emotional awareness
            The anterior insula is implicated in **interoceptive
            awareness** — the conscious sense of the body's internal
            state — and in **core affective feelings**
            . BA 16, as the
            rostralmost anterior insular territory, is at the
            **associative edge** of this network: it is more
            involved in integrating interoceptive signals with
            contextual and socio-emotional information than in
            primary interoceptive representation.
        autonomic / viscero-autonomic cortex (conditional)
            The anterior agranular insula (BA 14–16) is associated
            with **viscero-autonomic, homeostatic, and limbic
            functions** . On the
            left, the autonomic weighting is **parasympathetic** —
            bradycardia and depressor responses
            . BA 16's
            contribution is at the **rostral associative edge** of
            this autonomic field.
        von Economo neuron territory (conditional)
            BA 16r (the rostral extension into the medial prefrontal
            cortex, when present) has been included in VEN
            morphometric studies; VENs are confined to the anterior
            cingulate and frontoinsular cortices
            . The insular portion of BA 16
            contains a small VEN subset; the densest VEN territory
            lies more dorsally in the anterior short gyri.

**This field is structurally identical to the right sibling's**, with
one right-emphasized functional overlay added: the **right caudolateral
OFC secondary taste network** (see the right BA 16 package). The
architectonic neighbourhoods and the olfactory-limbic / salience /
interoception / autonomic / VEN overlays are the same on both sides;
what differs is the **emphasis** within each.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 14 (ventral anterior insula)        caudal neighbour; shares the
                                           agranular anterior insular
                                           field
    BA 15 (inconstant intermediate         caudal neighbour when
    anterior insula)                       present; the BA 15 package
                                           is not yet built out in this
                                           tree — forward reference
    BA 13 (middle insula)                  caudal / dorsal neighbour via
                                           the agranular-to-dysgranular
                                           transition
    BA 43 (anterior insula / postcentral   rostroventral neighbour;
    operculum)                             BA 16 is NOT BA 43 but
                                           participates in the
                                           chemosensory convergence
                                           zone
    claustrum / prepyriform area           lateral / medial neighbours;
                                           the defining allocortical
                                           interface of the
                                           peripaleocortical claustral
                                           territory

**This field is structurally identical to the right sibling's**, with
one forward reference: **BA 15** (the inconstant intermediate anterior
insular area) is not yet a package in this tree. When it is built out,
BA 16's adjacency to BA 15 must be declared on both sides.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 16's **sparse and inconstant territory** means it does **not** carry
the full set of anterior insular domains. On the left, the emphasis is
as follows:

    interoception                              (left emphasis — SECONDARY)
        BA 16 is at the **rostral associative edge** of the anterior
        insular interoceptive network. It integrates interoceptive
        signals with olfactory and contextual information, but does
        not carry the primary interoceptive representation (which is
        posterior insula). The left BA 16's interoceptive
        contribution is **weaker than the right BA 13's** and
        **weaker than the left BA 14's**.

    autonomic_control (parasympathetic)            (left emphasis)
        **This is BA 16's dominant contribution on the left.** The
        left anterior agranular insula is part of the
        **parasympathetic** autonomic network: left insular
        stimulation produces **bradycardia and depressor** responses
        . BA 16,
        as the rostralmost anterior insular territory, is at the
        **associative edge** of this parasympathetic field — it
        contributes to the cortical control of vagal outflow at the
        rostral pole of the insula. The left BA 16 → hypothalamus
        and BA 16 → NST projections are the substrate.

    salience_network                               (left emphasis)
        BA 16, when present, is part of the **anterior insula
        salience-network hub** . On
        the left, the salience weighting is toward **language-linked
        salience detection** — the detection of behaviourally
        relevant stimuli that are linguistically or socially
        meaningful. The left BA 16's salience contribution is
        smaller than BA 14's but is at the same network node.

    social_emotional                                (left emphasis)
        BA 16 contributes to the **emotional-awareness** network
        through its olfactory-limbic and salience-network
        connections. On the left, the contribution is weighted
        toward **language-linked emotional awareness** — the
        naming and narrating of affective states. The left BA 16 is
        at the associative edge of this function, integrating
        interoceptive and olfactory signals into linguistically
        expressible emotional content.

    multimodal_integration                          (left emphasis)
        BA 16 is a **convergence zone** for olfactory,
        interoceptive, and socio-emotional signals at the rostral
        pole of the insula. On the left, the integration is weighted
        toward the **language-linked / contextual** aspect of the
        convergence — the "what does this smell/feel mean in my
        current social and linguistic context?" question.

**Left-specific caveat on `speech_articulation`.** BA 16 does **not**
carry the `speech_articulation` domain. The domain belongs to the
insular lobe as a whole (see the parent registry's
`SPEECH_ARTICULATION_CAVEAT`), and the critical structure is the
**precentral gyrus of the insula**, which straddles BA 13, BA 16, and
the opercular transition. **BA 16 should not claim the domain** — it
is at the rostral edge of the critical territory, not its centre.

**Left-specific caveat on `vestibular_and_self_location`.** This
domain is **right-emphasized at BA 13** (see the right BA 13 package).
The left BA 16 does **not** carry it.

**Left-specific caveat on `gustatory`.** BA 16 is **not** the primary
gustatory area (BA 43) and is **not** a secondary gustatory area at
the same weighting as BA 14. Its chemosensory contribution is via the
**olfactory-limbic** interface (peripaleocortical claustral), not via
the taste pathway. `gustatory` is therefore **omitted** from the left
BA 16 `FUNCTIONAL_DOMAINS` tuple.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    olfactory-limbic afferents
        → prepyriform area (primary olfactory cortex), left
        → periamygdaloid cortex, left
            BA 16's **defining input**. The peripaleocortical
            claustral territory is continuous with the prepyriform
            allocortex at the rostral insular pole
            . This is the anatomical
            basis of BA 16's participation in the olfactory-limbic
            interface.

    claustral connections
        → claustrum, left
            BA 16 is cytoarchitectonically defined by its relation
            to the claustrum (layer VI merges with the claustral
            capsule). The claustrum → BA 16 projection is part of
            the **claustrocortical** system that coordinates
            cortical areas across modalities
            .

    thalamic afferents
        → VPMpc (gustatory relay, weak / tertiary projection)
            VPMpc projects most densely to BA 43 and area G, with a
            secondary projection to BA 14, and a **weak tertiary
            projection to BA 16**.
        → VMpo (interoceptive relay, weak / tertiary projection)
            The interoceptive thalamic relay has a weak projection
            to the rostral anterior insula, including BA 16.

    cortical afferents
        → BA 14 (ventral anterior insula), left
            The dominant intracortical afferent to BA 16. BA 14
            projects rostrally to BA 16, carrying the
            olfactory-gustatory-autonomic signal to the rostral
            pole.
        → anterior short gyri of the anterior insula
            Reciprocal connections with the anterior granular
            insula, supporting the salience-network transition.
        → orbitofrontal cortex (OFC), left
            Reciprocal connections with the left OFC support the
            olfactory-limbic interface and the socio-emotional
            integration functions.

    subcortical efferents
        → hypothalamus (lateral hypothalamus), left
            **BA 16 → LH is part of the parasympathetic efferent
            pathway.** On the left, this projection is weighted
            toward parasympathetic outflow (bradycardia, depressor
            responses) .
        → nucleus of the solitary tract (NST), left
            BA 16 projects to the NST, the brainstem relay for
            visceral afferents and the origin of vagal
            parasympathetic outflow.
        → amygdala (basolateral nuclei), left
            Reciprocal connections support the olfactory-limbic
            interface and the emotional tagging of olfactory
            stimuli.

    callosal connections
        → right BA 16 (when present)
            Interhemispheric coordination of the rostralmost
            anterior insula. The left → right traffic is weighted
            toward **language-linked salience** and
            **parasympathetic** autonomic signals; the right → left
            traffic is weighted toward **affective-salience** and
            **sympathetic** autonomic signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in three respects:
(a) the olfactory-limbic afferent is weighted toward the
**language-linked / contextual** aspect of the convergence;
(b) the BA 16 → hypothalamus and BA 16 → NST projections are
**parasympathetic** rather than sympathetic;
(c) the callosal traffic carries language-linked salience and
parasympathetic signals.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_ba16_parasympathetic_associative_edge
        **This is the left BA 16 anchor par excellence.** Left
        insular stimulation produces **bradycardia and depressor**
        responses, and the left insula is the **parasympathetic**
        pole of the insular autonomic lateralization
        . BA 16, as the
        rostralmost anterior insular territory, is at the
        **associative edge** of this parasympathetic field. Left
        BA 16 lesions can contribute to **parasympathetic
        dysregulation** — bradycardia, hypotension, and altered
        gastric motility — though the effect is **weaker than a
        BA 14 lesion** because BA 16's territory is small and
        inconstant.

    olfactory_limbic_seizure_semiology
        The **uncinate fit** — an olfactory aura (often
        unpleasant, "burning" or "rotten" smells) followed by
        automatisms and impaired awareness — reflects spread to
        the **olfactory-limbic interface** at the ventral insular
        pole. Left BA 16 / prepyriform / periamygdaloid
        involvement is part of the substrate. This is a
        left-relevant anchor because the left temporal lobe is the
        more common seizure-onset zone for uncinate fits.

    left_anterior_insular_salience_dysfunction
        Left BA 16, when present, is part of the **anterior insula
        salience network** . Left
        anterior insular lesions can produce **task-switch
        deficits** and **reduced responsiveness to behaviourally
        relevant stimuli**, and the language-linked component of
        salience detection is weighted toward the left. The
        contribution of BA 16 specifically is **smaller than BA
        14's** but is at the same network node.

    left_insular_glioma_resection
        Because BA 16 is a **buried rostral territory** adjacent
        to the limen insulae and the claustrum, resecting a left
        insular glioma in the BA 16 zone requires careful mapping
        of olfactory, autonomic, and salience function. Left BA 16
        resections risk **parasympathetic dysregulation**,
        **olfactory-limbic deficits**, and **salience-network
        dysfunction** — distinct from the risks of anterior short
        gyri resections (apraxia of speech) and posterior insula
        resections (primary interoceptive / pain deficits).

    autonomic_stress_vulnerability_sudep
        Anterior insula dysfunction may be **particularly relevant
        under autonomic stress** , and the
        insula's involvement in seizure-related autonomic
        dysfunction is suspected in **SUDEP** (sudden unexpected
        death in epilepsy) . The left
        BA 16's parasympathetic weighting makes it part of the
        cortical substrate for the cardio-respiratory autonomic
        derangements that contribute to SUDEP — but the
        **sympathetic** right insula is the more directly
        arrhythmogenic side. The left BA 16's SUDEP contribution
        is therefore **protective-weighted** rather than
        arrhythmogenic.

    human_presence_probability_clinical_uncertainty
        **BA 16 is inconstant in humans**, and its presence
        probability is lower than BA 14's or BA 13's. Clinical
        lesion studies that report "anterior insular" deficits do
        **not** reliably isolate BA 16, and downstream code must
        not treat BA 16 as a guaranteed clinical target. The
        ``PRESENCE_PROBABILITY`` field is the canonical reference
        for how much weight to give BA 16-specific findings.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 16 autonomic contribution is parasympathetic (right
is sympathetic), and the left BA 16's SUDEP contribution is
protective-weighted rather than arrhythmogenic;
(b) the left BA 16's olfactory-limbic and salience contributions are
weighted toward language-linked awareness (right is affective-salience).
The right sibling's docstring carries the corresponding right-sided
anchors.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left insular BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 16 (which on the
    left is ``("salience_network", "social_emotional")`` with
    BA 16's **reduced territory** noted), and enforcer of the
    ``speech_articulation`` exclusion.

..brodmann_area_14
    Caudal neighbour. The agranular anterior insular field is shared
    between BA 14 and BA 16; BA 14 is the larger and more constant
    component, BA 16 the smaller and inconstant one.

..brodmann_area_15  (forward reference)
    The inconstant intermediate anterior insular area. **BA 15 is not
    yet a package in this tree.** When it is built out, BA 16's
    adjacency to BA 15 must be declared on both sides. Until then,
    the adjacency is a forward reference.

..brodmann_area_13_middle_insula
    Caudal / dorsal neighbour via the agranular-to-dysgranular
    transition. **On the left, BA 13 is the interoceptive-accuracy
    and vestibular/body-ownership node** (right-emphasized), and
    BA 16's contribution is hierarchically downstream of BA 13's
    interoceptive re-representation.

..brodmann_area_43_anterior_insula
    The **classical primary gustatory area**. BA 16 is **not** BA 43;
    BA 16's chemosensory contribution is via the **olfactory-limbic**
    pathway, not the taste pathway.

...primary_gustatory_cortex
    The **functional-field sibling** (one level up, under
    ``..insular``). BA 16 is **not** part of the PGC's cortical
    territories — the PGC spans BA 43, area G, the opercula, and
    (conditionally) the base of the central sulcus, but **not**
    BA 16. BA 16's contribution to flavour is indirect, via the
    olfactory-limbic interface.

..cortex.frontal
    The frontal operculum and the ventral agranular orbitofrontal
    cortex (area OFa) border BA 16. The frontal package must declare
    the insula as a hidden neighbour and must note the BA 16r
    (rostral BA 16) territory that extends into the medial prefrontal
    cortex.

..cortex.parietal
    The parietal operculum (area G) is adjacent to the dorsal margin
    of the anterior insula, but **not** directly to BA 16 — BA 16 is
    rostral to the area G transition. Recorded here to pre-empt a
    false cross-reference.

..cortex.cingulate
    The dorsal anterior cingulate is the salience-network partner of
    the anterior insula. BA 16 contributes to the salience-network
    transition, and on the left the salience weighting is toward
    language-linked salience detection.

../../subcortical/medial_temporal_lobe/amygdala
    The left basolateral amygdala sends a projection to left BA 16
    that supports the **olfactory-limbic interface** and the
    emotional tagging of olfactory stimuli. The amygdala package
    must declare the left BA 16 as a cortical target, noting that
    BA 16 is a **smaller and less reliable** target than BA 14.

../../subcortical/medial_temporal_lobe/hippocampus
    The prepyriform and entorhinal cortices project to BA 16 as part
    of the primary olfactory pathway. The hippocampus package must
    declare the left BA 16 as a cortical target and must note that
    the olfactory → BA 16 route is at the **associative edge** of
    the hippocampal formation's olfactory interface.

../../subcortical/diencephalon/hypothalamus
    The left BA 16 → left hypothalamus projection supports
    **parasympathetic** autonomic control. The hypothalamus package
    must declare the left BA 16 as a cortical afferent, noting that
    BA 16's contribution is **weaker than BA 14's**.

../../subcortical/diencephalon/thalamus
    The **VPMpc** (gustatory) and **VMpo** (interoceptive) thalamic
    nuclei project to left BA 16 only weakly / tertiarily. The
    thalamus package must declare both as **weak** cortical
    afferents to left BA 16.

../../brainparts/hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
    The **nucleus of the solitary tract (NST)** receives left BA 16
    projections and is the origin of vagal parasympathetic outflow.
    The NST package must declare the left BA 16 as a **weak**
    cortical afferent, noting that BA 16's NST projection is at the
    associative edge of the parasympathetic field.

../../brainparts/forebrain/telencephalon/cerebral_hemispheres/left/cortex/insular/brodmann_areas/brodmann_area_15  (forward reference)
    The inconstant intermediate anterior insular area. When built out,
    it must carry the same ``PRESENCE_PROBABILITY`` discipline as
    BA 16 and must declare the adjacency to BA 16 on both sides.

../../right/cortex/insular/brodmann_areas/brodmann_area_16
    The right-hemisphere homologue. Structural fields (BA number,
    region label, **presence probability**, agranular /
    peripaleocortical claustral gradient, architectonic
    neighbourhoods, BA-to-neighbour adjacency) MUST be
    byte-identical. Functional emphasis and clinical significance
    diverge — the left BA 16 is weighted toward parasympathetic
    autonomic control, language-linked salience, and
    language-linked emotional awareness; the right BA 16 is weighted
    toward sympathetic autonomic control, affective-salience, and
    interoceptive-affective integration.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_16"
    HEMISPHERE          = "left"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 16
    INSULAR_REGION      = "anterior_inconstant"
    CYTOTECTONIC_GRADIENT = "agranular"
    ALTERNATE_NAMES     = ("peripaleocortical_claustral",
                           "insula_olfactoria")

    PRESENCE_PROBABILITY = 0.5
        # BA 16 is inconstant in humans; Brodmann defined it in the
        # guenon but not in the human brain. The exact human
        # probability varies by parcellation scheme and individual.
        # Downstream code must treat this as a **soft** territory
        # and must not assume BA 16 is present in any given subject.

    NAMING_COLLISION_WITH = ()   # BA 16 has no naming collision

    FUNCTIONAL_DOMAINS  = (
                              "interoception",         # secondary /
                                                       # associative edge
                              "autonomic_control",     # left:
                                                       # parasympathetic
                              "salience_network",
                              "social_emotional",
                              "multimodal_integration",
                              # NOTE: speech_articulation is
                              # EXCLUDED (lobe-level domain; see
                              # parent registry).
                              # NOTE: vestibular_and_self_location
                              # is EXCLUDED (right-emphasized at
                              # BA 13; see right BA 13 package).
                              # NOTE: gustatory is EXCLUDED (BA 16
                              # is not a primary or secondary taste
                              # area; its chemosensory contribution
                              # is olfactory-limbic).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "interoception":
                                  "rostral_associative_edge_"
                                  "olfactory_contextual_integration",
                              "autonomic_control":
                                  "parasympathetic_vagal_"
                                  "bradycardia_depressor_"
                                  "associative_edge",
                              "salience_network":
                                  "language_linked_salience_"
                                  "detection",
                              "social_emotional":
                                  "language_linked_emotional_"
                                  "awareness_olfactory_limbic",
                              "multimodal_integration":
                                  "olfactory_limbic_contextual_"
                                  "language_linked_integration",
                          }

    MODERN_CROSSWALK    = {   # BA 16 → modern parcellation labels
                              "HCP_180":       ("AAIC",),   # partial
                              "Ongur_Price_2000": ("Iai", "Ial"),  # partial
                              "Petrides_Pandya":  ("Iam",),  # partial
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_ba16_parasympathetic_"
                              "associative_edge",
                              "olfactory_limbic_seizure_"
                              "semiology",
                              "left_anterior_insular_salience_"
                              "dysfunction",
                              "left_insular_glioma_resection",
                              "autonomic_stress_vulnerability_"
                              "sudep",
                              "human_presence_probability_"
                              "clinical_uncertainty",
                          )

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "AREA_NAME",
        "HEMISPHERE",
        "LOBE",
        "BRODMANN_NUMBER",
        "INSULAR_REGION",
        "CYTOTECTONIC_GRADIENT",
        "ALTERNATE_NAMES",
        "PRESENCE_PROBABILITY",
        "NAMING_COLLISION_WITH",
        "FUNCTIONAL_DOMAINS",
        "DOMAIN_EMPHASIS",
        "MODERN_CROSSWALK",
        "CONNECTIVITY",
        "CLINICAL_ANCHORS",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references BA 16 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT (unique to this package)
--------------------------------------------------------------------------------

**There are two forward-declaration caveats for BA 16 — more than for
any other insular BA package.**

1. **BA 15 is not yet a package in this tree.** BA 16's adjacency to
   BA 15 (the inconstant intermediate anterior insular area) is a
   forward reference. When BA 15 is built out, the adjacency must be
   declared on both sides in the same commit.

2. **The BA 16r medial prefrontal continuation** is a
   **non-insular territory** — it extends into the medial prefrontal
   cortex and is the territory included in VEN morphometric studies.
   The package should cross-reference the medial prefrontal cortex
   package (once it exists) rather than claiming BA 16r as an
   insular sub-field. Until then, BA 16r is a forward reference.

**The presence-probability caveat is the more consequential of the
two.** BA 16 is **inconstant in humans**, and Brodmann himself did not
identify it in the human brain — he identified only a posterior
granular and an anterior agranular region in humans, and the BA 13–16
scheme was defined in the guenon. Downstream code that queries
"BA 16" must therefore receive the ``PRESENCE_PROBABILITY`` field and
must treat any BA 16-specific result as **conditional** rather than
as a reliable anatomical anchor. This is the **only insular BA package**
whose presence is probabilistic, and the caveat must not be silently
dropped.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 16 is **small and inconstant**, so the standard promotion pressures
do not apply in the usual way. If a future parcellation nevertheless
decides to split BA 16 into its **insular** and **medial prefrontal
(BA 16r)** components, the promotion takes this form:

    brodmann_area_16/
        __init__.py
        insular_component/
            __init__.py
        medial_prefrontal_component/   # BA 16r
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The presence-probability caveat propagates to any sub-package.** A
BA 16r package would also be inconstant (the medial prefrontal
continuation is not consistently distinguishable), and it must carry
its own ``PRESENCE_PROBABILITY`` field. The parent's
``PRESENCE_PROBABILITY`` is the **product** of the insular and medial
prefrontal probabilities, not the maximum of the two.

**No split should be performed while the BA 15 forward reference is
unresolved.** Splitting BA 16 while BA 15 does not yet exist would
multiply unresolved references and make the anterior agranular
insular field harder to reconcile.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_16``:

    MUST be identical (byte-for-byte):
        AREA_NAME              "brodmann_area_16"
        LOBE                   "insular"
        BRODMANN_NUMBER        16
        INSULAR_REGION         "anterior_inconstant"
        CYTOTECTONIC_GRADIENT  "agranular"
        ALTERNATE_NAMES        ("peripaleocortical_claustral",
                               "insula_olfactoria")
        PRESENCE_PROBABILITY   0.5 (the same on both sides — presence
                               is a property of the human species, not
                               of the hemisphere)
        NAMING_COLLISION_WITH  () — empty on both sides
        Architectonic neighbourhoods
        BA-to-neighbour adjacency (including the BA 15 forward
                               reference)
        MODERN_CROSSWALK       (the same HCP / Öngür-Price /
                               Petrides labels)
        SUBDIVISIONS           both empty (or both non-empty in
                               the same way, if a split is ever
                               done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        FUNCTIONAL_DOMAINS     both sides carry the same five
                               domains (interoception,
                               autonomic_control, salience_network,
                               social_emotional,
                               multimodal_integration) and both
                               exclude speech_articulation,
                               vestibular_and_self_location, and
                               gustatory. The set is identical.
        DOMAIN_EMPHASIS        left: autonomic_control is
                               "parasympathetic_vagal_bradycardia_
                               depressor_associative_edge";
                               salience_network is
                               "language_linked_salience_detection";
                               social_emotional is "language_linked_
                               emotional_awareness_olfactory_limbic";
                               interoception is "rostral_associative_
                               edge_olfactory_contextual_integration";
                               multimodal_integration is "olfactory_
                               limbic_contextual_language_linked_
                               integration".
                               right: autonomic_control is
                               "sympathetic_pressor_tachycardic_
                               associative_edge"; salience_network is
                               "affective_salience_detection";
                               social_emotional is "interoceptive_
                               affective_integration_felt_component";
                               interoception is "rostral_associative_
                               edge_bodily_state_integration";
                               multimodal_integration is "olfactory_
                               limbic_bodily_state_centered_
                               integration".
        CONNECTIVITY           same bundle names; left: BA 16 →
                               hypothalamus is parasympathetic; BA 16
                               → NST is parasympathetic; callosal
                               traffic carries language-linked
                               salience and parasympathetic signals.
                               right: BA 16 → hypothalamus is
                               sympathetic; BA 16 → NST is
                               sympathetic; callosal traffic carries
                               affective-salience and sympathetic
                               signals.
        CLINICAL_ANCHORS       left: parasympathetic associative edge;
                               olfactory-limbic seizure semiology;
                               language-linked salience dysfunction;
                               glioma resection risks with
                               parasympathetic emphasis; SUDEP
                               protective-weighted; presence-
                               probability clinical uncertainty.
                               right: sympathetic associative edge;
                               affective-salience dysfunction;
                               glioma resection risks with sympathetic
                               emphasis; SUDEP arrhythmogenic-
                               weighted; presence-probability clinical
                               uncertainty.

**The `DOMAIN_EMPHASIS` asymmetry is the sharpest single entry in this
contract.** Both hemispheres carry the same five domains and both
exclude the same three, but the emphasis within every shared domain
points in opposite directions: the left BA 16 is the
**parasympathetic / language-linked** territory, the right BA 16 is the
**sympathetic / affective-salience** territory. A right-hemisphere
package that copies the left's `DOMAIN_EMPHASIS` verbatim is a bug —
the two hemispheres are **functionally distinct BAs under the same
number**.

**The `PRESENCE_PROBABILITY` field is byte-identical on both sides** —
presence is a species-level property, not a hemisphere-level one. If a
future study finds a hemisphere difference in BA 16 presence, the field
must be split into ``PRESENCE_PROBABILITY_LEFT`` and
``PRESENCE_PROBABILITY_RIGHT`` in the same commit, on both sides.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_16".
[ ] HEMISPHERE is "left".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 16.
[ ] INSULAR_REGION is "anterior_inconstant".
[ ] CYTOTECTONIC_GRADIENT is "agranular".
[ ] ALTERNATE_NAMES includes "peripaleocortical_claustral" and
    "insula_olfactoria".
[ ] **PRESENCE_PROBABILITY is set** (approximately 0.5) and the
    docstring documents the BA 16 inconstancy in humans
    .
[ ] NAMING_COLLISION_WITH is an empty tuple — BA 16 has no naming
    collision.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - interoception
    - autonomic_control
    - salience_network
    - social_emotional
    - multimodal_integration
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation (lobe-level
    domain; see parent registry).
[ ] FUNCTIONAL_DOMAINS **excludes** vestibular_and_self_location
    (right-emphasized at BA 13).
[ ] FUNCTIONAL_DOMAINS **excludes** gustatory (BA 16 is not a
    primary or secondary taste area; chemosensory contribution is
    olfactory-limbic).
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis** per domain:
    - interoception → rostral_associative_edge_olfactory_contextual_
      integration
    - autonomic_control → parasympathetic_vagal_bradycardia_
      depressor_associative_edge
    - salience_network → language_linked_salience_detection
    - social_emotional → language_linked_emotional_awareness_
      olfactory_limbic
    - multimodal_integration → olfactory_limbic_contextual_
      language_linked_integration
[ ] MODERN_CROSSWALK is present with HCP / Öngür-Price / Petrides
    mappings (noting that BA 16 is only partially captured by any
    modern scheme).
[ ] CONNECTIVITY documents:
    - prepyriform / periamygdaloid olfactory afferents (the defining
      peripaleocortical claustral input)
    - claustrum connections
    - VPMpc and VMpo thalamic afferents (weak / tertiary)
    - BA 14 → BA 16 intracortical afferent
    - BA 16 → hypothalamus (parasympathetic, left-specific)
    - BA 16 → NST (parasympathetic, left-specific)
    - amygdala reciprocal connections (olfactory-limbic)
    - callosal traffic to right BA 16 (language-linked salience and
      parasympathetic, left-specific)
[ ] CLINICAL_ANCHORS contains the six left-specific anchors:
    - left_ba16_parasympathetic_associative_edge
    - olfactory_limbic_seizure_semiology
    - left_anterior_insular_salience_dysfunction
    - left_insular_glioma_resection
    - autonomic_stress_vulnerability_sudep
    - human_presence_probability_clinical_uncertainty
[ ] The **left parasympathetic associative edge** is documented as
    the primary left BA 16 anchor, citing left insular stimulation →
    bradycardia / depressor responses 
    .
[ ] The **SUDEP contribution of the left BA 16 is protective-
    weighted**, not arrhythmogenic — the right insula's sympathetic
    weighting is the more directly arrhythmogenic side
    .
[ ] The **BA 16 ≠ BA 14** distinction is documented: BA 16 is the
    smaller, more rostral, more inconstant agranular territory;
    BA 14 is the larger, more constant, more ventral agranular
    territory.
[ ] The **BA 16 ≠ PGC** distinction is documented: BA 16 is not part
    of the PGC's cortical territories; its chemosensory contribution
    is olfactory-limbic, not gustatory.
[ ] The **BA numbering caveat** is documented (Brodmann defined
    BA 16 in the guenon; human BA 16 is inconstant).
[ ] The **BA 16r medial prefrontal continuation** is documented as a
    non-insular territory that should be cross-referenced from the
    medial prefrontal cortex package, not claimed as an insular
    sub-field.
[ ] The **BA 15 forward reference** is documented (BA 15 is not yet
    a package in this tree).
[ ] The **speech-articulation exclusion rationale** is documented:
    the domain belongs to the insular lobe as a whole, not to BA 16.
[ ] The **gustatory exclusion rationale** is documented: BA 16 is
    not a taste area.
[ ] No SUBDIVISIONS promotion is performed while the BA 15 forward
    reference is unresolved.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, alternate names,
    PRESENCE_PROBABILITY, architectonic neighbourhoods, modern
    crosswalk, FUNCTIONAL_DOMAINS set) match the right sibling;
    DOMAIN_EMPHASIS, CONNECTIVITY emphasis, and CLINICAL_ANCHORS
    deliberately differ.
[ ] Any downstream code querying BA 16 must receive the
    PRESENCE_PROBABILITY field and must treat BA 16-specific results
    as conditional — this is the only insular BA package whose
    presence is probabilistic.
""" 