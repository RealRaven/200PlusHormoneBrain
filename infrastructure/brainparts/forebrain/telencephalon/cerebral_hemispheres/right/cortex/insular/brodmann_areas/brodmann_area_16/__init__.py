"""
Brodmann Area 16 (Anterior Inconstant Insula) — Right Hemisphere
=================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_16   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the right
hemisphere's **BA 16** — the **anterior inconstant insula**, the most
rostral and most undifferentiated of the insular Brodmann areas. It is
one of the three **anterior agranular** insular areas (BA 14, BA 15,
BA 16) and sits at the extreme rostral pole of the insula, where the
insular cortex approaches the claustrum and the prepyriform allocortex
.

Parent: ``..brodmann_areas`` (right insular BA registry) — sibling to
BA 13, BA 14, BA 41, BA 42, BA 43.

This package is the **structural mirror** of
``../../left/cortex/insular/brodmann_areas/brodmann_area_16``. The BA
number, the region label, and the **presence probability** are
identical on both sides; the **functional emphasis** and **clinical
significance** diverge — on the right, BA 16's sparse territory is
weighted toward the **sympathetic** pole of the insular autonomic
lateralization and toward the **affective-salience** and
**interoceptive-affective integration** components of the anterior
insula's network functions.

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
rather than by the BA 16 label. **BA 16 is therefore a conventional
label whose human presence is probabilistic, not a reliably identifiable
architectonic entity**. The package must carry an explicit
``PRESENCE_PROBABILITY`` field and must not be treated by downstream
code as a guaranteed territory.

BA 16 borders:

    caudally     BA 14 (ventral anterior insula) and BA 15 (inconstant
                 intermediate anterior insula) via the agranular
                 anterior insular field
    laterally    the claustrum and the extreme capsule
    medially     the prepyriform allocortex and the ventral agranular
                 orbitofrontal cortex at the limen insulae
    dorsally     the anterior short gyri of the anterior insula

**Right-hemisphere specificity**: when present, the right BA 16 is the
rostralmost territory of the **right anterior agranular insula**,
which is the **sympathetic pole** of the insular autonomic
lateralization and the **affective-salience** node of the anterior
insular salience network. Right insular stimulation produces **pressor
and tachycardic** responses, and the right BA 16 → hypothalamus and
BA 16 → NST projections are part of the sympathetic substrate. On the
salience side, the right BA 16 is weighted toward **stimulus-driven
reorienting** and **affective salience detection**, rather than the
left's language-linked salience.

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
            between default-mode and executive networks. **On the
            right, the salience weighting is toward
            stimulus-driven reorienting and affective salience
            detection** — the "circuit breaker" function that the
            right anterior insula (with the right FEF and right
            temporoparietal junction) supports.
        anterior insula interoception and emotional awareness
            The anterior insula is implicated in **interoceptive
            awareness** — the conscious sense of the body's internal
            state — and in **core affective feelings**
            . On the right,
            the anterior insula's contribution is weighted toward
            the **felt** component of emotional awareness — the
            subjective experience of an affective state — rather
            than the left's language-linked naming and narrating
            of emotion. BA 16, as the rostralmost anterior insular
            territory, is at the **associative edge** of this
            network.
        autonomic / viscero-autonomic cortex (conditional)
            The anterior agranular insula (BA 14–16) is associated
            with **viscero-autonomic, homeostatic, and limbic
            functions** . On the
            right, the autonomic weighting is **sympathetic** —
            pressor and tachycardic responses, and cardiovascular
            arousal to stress . BA 16's
            contribution is at the **rostral associative edge** of
            this sympathetic field.
        von Economo neuron territory (conditional)
            BA 16r (the rostral extension into the medial prefrontal
            cortex, when present) has been included in VEN
            morphometric studies; VENs are confined to the anterior
            cingulate and frontoinsular cortices
            . The insular portion of BA 16
            contains a small VEN subset; the densest VEN territory
            lies more dorsally in the anterior short gyri. **On the
            right, VEN-related connectivity is weighted toward
            interoceptive-affective integration** — the rapid
            appraisal of bodily states that supports the felt
            component of emotion.
        right caudolateral OFC secondary taste area (right-emphasized)
            **Right-emphasized overlay.** The right BA 16 is
            adjacent to and reciprocally connected with the **right
            caudolateral orbitofrontal cortex**, which meta-analysis
            shows is the more consistently right-lateralized
            secondary taste area . This
            is a right-emphasized overlay that the left BA 16 does
            not carry at the same weighting, though BA 16's
            contribution to it is smaller than BA 14's because of
            BA 16's marginal territory.

**This field is structurally identical to the left sibling's**, with
one right-emphasized functional overlay added: the **right caudolateral
OFC secondary taste area**. The architectonic neighbourhoods and the
olfactory-limbic / salience / interoception / autonomic / VEN overlays
are the same on both sides; what differs is the **emphasis** within
each.

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

**This field is byte-identical to the left sibling's**, with one
forward reference: **BA 15** (the inconstant intermediate anterior
insular area) is not yet a package in this tree. When it is built out,
BA 16's adjacency to BA 15 must be declared on both sides.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 16's **sparse and inconstant territory** means it does **not** carry
the full set of anterior insular domains. On the right, the emphasis is
as follows:

    autonomic_control (sympathetic)                (right emphasis — PRIMARY)
        **This is BA 16's dominant contribution on the right.** The
        right anterior agranular insula is part of the
        **sympathetic** autonomic network: right insular
        stimulation produces **pressor and tachycardic** responses
        . BA 16,
        as the rostralmost anterior insular territory, is at the
        **associative edge** of this sympathetic field. The right
        BA 16 → hypothalamus and BA 16 → NST projections are part
        of the sympathetic substrate. On the left, the mirror is
        parasympathetic (bradycardia, depressor); on the right,
        sympathetic (pressor, tachycardic).

    interoception                              (right emphasis — SECONDARY)
        BA 16 is at the **rostral associative edge** of the anterior
        insular interoceptive network. It integrates interoceptive
        signals with olfactory and bodily-state information, but does
        not carry the primary interoceptive representation (which is
        posterior insula). The right BA 16's interoceptive
        contribution is **at the same associative-edge weighting as
        the left's**, but weighted toward **bodily-state / visceral**
        integration rather than the left's **olfactory-contextual /
        language-linked** integration. The right BA 13 is the
        canonical interoceptive-accuracy node (Critchley et al.
        2004); BA 16 is hierarchically downstream.

    salience_network                               (right emphasis)
        BA 16, when present, is part of the **anterior insula
        salience-network hub** . On
        the right, the salience weighting is toward
        **stimulus-driven reorienting** and **affective salience
        detection** — the detection of behaviourally relevant
        stimuli that are emotionally or biologically salient. The
        right anterior insula is the more strongly engaged node of
        the salience network during stimulus-driven reorienting.
        The right BA 16's contribution is **smaller than BA 14's**
        but is at the same network node.

    social_emotional                                (right emphasis)
        BA 16 contributes to the **emotional-awareness** network
        through its olfactory-limbic and salience-network
        connections. On the right, the contribution is weighted
        toward **interoceptive-affective integration** — the
        "felt" component of emotion. The right BA 16 is at the
        associative edge of this function, integrating
        interoceptive and olfactory signals into **bodily felt
        affective states** rather than the left's linguistically
        expressible emotional content.

    multimodal_integration                          (right emphasis)
        BA 16 is a **convergence zone** for olfactory,
        interoceptive, and socio-emotional signals at the rostral
        pole of the insula. On the right, the integration is
        weighted toward the **bodily-state / affective** aspect of
        the convergence — the "what does this smell/feel do to my
        body right now?" question — rather than the left's
        contextual and language-linked integration.

**Right-specific caveat on `speech_articulation`.** The domain **does
not exist on the right**. No right BA carries it. Right insular lesions
do not produce apraxia of speech. The right BA 16 excludes it not
because it belongs to the lobe as a whole (that is the left's
rationale) but because it is absent from the right hemisphere entirely.

**Right-specific caveat on `vestibular_and_self_location`.** This
domain is **BA-13-emphasized on the right** (see
``brodmann_area_13_middle_insula``), not BA-16-emphasized. The right
BA 16 does **not** carry it.

**Right-specific caveat on `gustatory`.** BA 16 is **not** the primary
gustatory area (BA 43) and is **not** a secondary gustatory area at
the same weighting as BA 14. Its chemosensory contribution is via the
**olfactory-limbic** interface (peripaleocortical claustral), not via
the taste pathway. `gustatory` is therefore **omitted** from the right
BA 16 `FUNCTIONAL_DOMAINS` tuple.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    olfactory-limbic afferents
        → prepyriform area (primary olfactory cortex), right
        → periamygdaloid cortex, right
            BA 16's **defining input**. The peripaleocortical
            claustral territory is continuous with the prepyriform
            allocortex at the rostral insular pole
            . This is the anatomical
            basis of BA 16's participation in the olfactory-limbic
            interface. On the right, this afferent is weighted
            toward the **affective / autonomic** aspect of the
            olfactory-limbic convergence — the rapid bodily
            response to a smell — rather than the left's
            language-linked / contextual aspect.

    claustral connections
        → claustrum, right
            BA 16 is cytoarchitectonically defined by its relation
            to the claustrum (layer VI merges with the claustral
            capsule). The claustrum → BA 16 projection is part of
            the **claustrocortical** system that coordinates
            cortical areas across modalities.

    thalamic afferents
        → VPMpc (gustatory relay, weak / tertiary projection)
            VPMpc projects most densely to BA 43 and area G, with a
            secondary projection to BA 14, and a **weak tertiary
            projection to BA 16**.
        → VMpo (interoceptive relay, weak / tertiary projection)
            The interoceptive thalamic relay has a weak projection
            to the rostral anterior insula, including BA 16. On the
            right, this projection is part of the sympathetic
            autonomic substrate.

    cortical afferents
        → BA 14 (ventral anterior insula), right
            The dominant intracortical afferent to BA 16. BA 14
            projects rostrally to BA 16, carrying the
            olfactory-gustatory-autonomic signal to the rostral
            pole. On the right, this signal is weighted toward
            sympathetic autonomic and flavor-intensity content.
        → anterior short gyri of the anterior insula
            Reciprocal connections with the anterior granular
            insula, supporting the salience-network transition. On
            the right, the salience weighting is toward
            stimulus-driven reorienting.
        → orbitofrontal cortex (OFC), right
            Reciprocal connections with the right OFC support the
            olfactory-limbic interface, the socio-emotional
            integration functions, and (right-emphasized) the
            **right caudolateral OFC secondary taste network**.

    subcortical efferents
        → hypothalamus (lateral hypothalamus), right
            **BA 16 → LH is part of the sympathetic efferent
            pathway.** On the right, this projection is weighted
            toward sympathetic outflow (pressor, tachycardic
            responses) .
        → nucleus of the solitary tract (NST), right
            BA 16 projects to the NST, the brainstem relay for
            visceral afferents and the origin of autonomic outflow.
            On the right, the BA 16 → NST projection is part of
            the sympathetic substrate.
        → amygdala (basolateral nuclei), right
            **Right-emphasized.** The reciprocal connections
            support the olfactory-limbic interface and the
            **interoceptive-affective integration** (the felt
            component of emotion). The right amygdala → BA 16
            projection is denser than the left's, though BA 16's
            amygdala input is smaller than BA 14's because of
            BA 16's marginal territory.

    callosal connections
        → left BA 16 (when present)
            Interhemispheric coordination of the rostralmost
            anterior insula. The right → left traffic is weighted
            toward **affective-salience** and **sympathetic**
            autonomic signals; the left → right traffic is weighted
            toward **language-linked salience** and
            **parasympathetic** autonomic signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the olfactory-limbic afferent is weighted toward the
**affective / autonomic** aspect of the convergence;
(b) the BA 16 → hypothalamus and BA 16 → NST projections are
**sympathetic** rather than parasympathetic;
(c) the amygdala → BA 16 projection is denser than the left's, and the
callosal traffic carries affective-salience and sympathetic signals.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ba16_sympathetic_associative_edge
        **This is the right BA 16 anchor par excellence.** Right
        insular stimulation produces **pressor and tachycardic**
        responses, and the right insula is the **sympathetic** pole
        of the insular autonomic lateralization
        . BA 16, as the
        rostralmost anterior insular territory, is at the
        **associative edge** of this sympathetic field. Right BA 16
        lesions can contribute to **sympathetic dysregulation** —
        pressor and tachycardic responses, altered cardiovascular
        reactivity to stress — though the effect is **weaker than a
        BA 14 lesion** because BA 16's territory is small and
        inconstant.

    right_insula_sudep_arrhythmogenic_dominance
        **This is the right-specific SUDEP anchor.** Anterior
        insula dysfunction may be **particularly relevant under
        autonomic stress** , and the
        right insula's **sympathetic weighting** is the side that
        has been specifically implicated in the **cardio-respiratory
        derangements that contribute to SUDEP** (sudden unexpected
        death in epilepsy) . The right
        BA 16 is part of the cortical substrate whose peri-ictal
        sympathetic surge can trigger fatal arrhythmia, and the
        right BA 16's contribution — though small because of the
        territory's inconstancy — is at the **arrhythmogenic edge**
        of the sympathetic field. **The left BA 16's
        parasympathetic weighting is protective rather than
        arrhythmogenic in the peri-ictal window.** This is the
        sharpest left-right asymmetry in the SUDEP literature, and
        the right BA 16 must carry the **arrhythmogenic-weighted**
        anchor while the left BA 16 carries the **protective-
        weighted** anchor.

    right_anterior_insular_affective_salience_dysfunction
        Right BA 16, when present, is part of the **anterior insula
        salience network** . Right
        anterior insular lesions can produce **task-switch
        deficits** and **reduced responsiveness to affectively
        salient stimuli** — the stimulus-driven reorienting
        function is right-weighted. The contribution of BA 16
        specifically is **smaller than BA 14's** but is at the
        same network node. Right BA 16 lesions can contribute to
        **affective blunting** and **reduced salience-driven
        reorienting**, distinct from the left BA 16's
        language-linked salience dysfunction.

    right_insula_caudolateral_ofc_secondary_taste_network
        **Right-emphasized.** The right BA 16 → right caudolateral
        OFC projection is part of the **right-lateralized
        secondary taste network** — the network whose caudolateral
        OFC peaks were found to be exclusively right-lateralized
        in human functional neuroimaging meta-analysis
        . Right BA 16 lesions
        can disconnect this network and produce combined
        flavor-intensity and hedonic-valuation deficits, though
        BA 16's contribution is smaller than BA 14's because of
        its marginal territory.

    olfactory_limbic_seizure_semiology
        The **uncinate fit** — an olfactory aura (often
        unpleasant, "burning" or "rotten" smells) followed by
        automatisms and impaired awareness — reflects spread to
        the **olfactory-limbic interface** at the ventral insular
        pole. Right BA 16 / prepyriform / periamygdaloid
        involvement is part of the substrate. Uncinate fits are
        more commonly reported in left temporal lobe epilepsy,
        but the right anterior insular involvement carries the
        **affective-autonomic** weighting — ictal fear,
        tachycardia, and autonomic auras are more prominent in
        right-sided uncinate semiology.

    right_insular_glioma_resection
        Because BA 16 is a **buried rostral territory** adjacent
        to the limen insulae and the claustrum, resecting a right
        insular glioma in the BA 16 zone requires careful mapping
        of olfactory, autonomic, and salience function. Right BA
        16 resections risk **sympathetic dysregulation**,
        **olfactory-limbic deficits**, and **affective-salience
        dysfunction** — distinct from the risks of anterior short
        gyri resections (prosody and inhibition on the right) and
        posterior insula resections (primary interoceptive / pain
        deficits).

    human_presence_probability_clinical_uncertainty
        **BA 16 is inconstant in humans**, and its presence
        probability is lower than BA 14's or BA 13's. Clinical
        lesion studies that report "anterior insular" deficits do
        **not** reliably isolate BA 16, and downstream code must
        not treat BA 16 as a guaranteed clinical target. The
        ``PRESENCE_PROBABILITY`` field is the canonical reference
        for how much weight to give BA 16-specific findings. This
        caveat is **byte-identical on the left and right** —
        presence is a species-level property, not a hemisphere-
        level one.

These anchors are **right-hemisphere-specific** in two senses:
(a) the right BA 16 autonomic contribution is sympathetic (left is
parasympathetic), and the right BA 16 is the hemisphere whose
sympathetic weighting is implicated in **SUDEP arrhythmogenesis**
(left is protective-weighted);
(b) the right BA 16's olfactory-limbic and salience contributions are
weighted toward **affective-salience and interoceptive-affective
integration** (left is language-linked). The left sibling's docstring
carries the corresponding left-sided anchors.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The right insular BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 16 (which on the
    right is ``("salience_network", "social_emotional")`` with
    BA 16's **reduced territory** noted), and enforcer of the
    ``speech_articulation`` exclusion (which on the right means the
    domain is not declared anywhere, not that it is assigned to the
    lobe as a whole).

..brodmann_area_14
    Caudal neighbour. The agranular anterior insular field is shared
    between BA 14 and BA 16; BA 14 is the larger and more constant
    component, BA 16 the smaller and inconstant one. On the right,
    BA 14's autonomic emphasis is sympathetic, and BA 16's is at the
    associative edge of the same sympathetic field.

..brodmann_area_15  (forward reference)
    The inconstant intermediate anterior insular area. **BA 15 is not
    yet a package in this tree.** When it is built out, BA 16's
    adjacency to BA 15 must be declared on both sides.

..brodmann_area_13_middle_insula
    Caudal / dorsal neighbour via the agranular-to-dysgranular
    transition. **On the right, BA 13 is the interoceptive-accuracy
    and vestibular/body-ownership node**, and BA 16's contribution
    is hierarchically downstream of BA 13's interoceptive
    re-representation.

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
    olfactory-limbic interface, and on the right it is weighted
    toward the affective / autonomic response rather than flavour
    identification.

..cortex.frontal
    The frontal operculum and the ventral agranular orbitofrontal
    cortex (area OFa) border BA 16. The frontal package must declare
    the insula as a hidden neighbour and must note the BA 16r
    (rostral BA 16) territory that extends into the medial prefrontal
    cortex, and the right BA 16 → right caudolateral OFC secondary
    taste projection.

..cortex.parietal
    The parietal operculum (area G) is adjacent to the dorsal margin
    of the anterior insula, but **not** directly to BA 16 — BA 16 is
    rostral to the area G transition. Recorded here to pre-empt a
    false cross-reference.

..cortex.cingulate
    The dorsal anterior cingulate is the salience-network partner of
    the anterior insula. BA 16 contributes to the salience-network
    transition, and on the right the salience weighting is toward
    stimulus-driven reorienting and affective salience detection.

../../subcortical/medial_temporal_lobe/amygdala
    The **right** basolateral amygdala → right BA 16 projection is
    the more strongly engaged substrate of
    **interoceptive-affective integration** (the "felt" component of
    emotion). The amygdala package must declare the right BA 16 as
    a cortical target, noting that the right projection is **denser**
    than the left's but that BA 16 is still a **smaller and less
    reliable** target than BA 14.

../../subcortical/medial_temporal_lobe/hippocampus
    The prepyriform and entorhinal cortices project to BA 16 as part
    of the primary olfactory pathway. The hippocampus package must
    declare the right BA 16 as a cortical target and must note that
    the olfactory → BA 16 route is at the **associative edge** of
    the hippocampal formation's olfactory interface.

../../subcortical/diencephalon/hypothalamus
    The right BA 16 → right hypothalamus projection supports
    **sympathetic** autonomic control. The hypothalamus package
    must declare the right BA 16 as a cortical afferent, noting that
    BA 16's contribution is **weaker than BA 14's** but is
    sympathetic-weighted.

../../subcortical/diencephalon/thalamus
    The **VPMpc** (gustatory) and **VMpo** (interoceptive) thalamic
    nuclei project to right BA 16 only weakly / tertiarily. The
    thalamus package must declare both as **weak** cortical
    afferents to right BA 16.

../../brainparts/hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
    The **nucleus of the solitary tract (NST)** receives right BA 16
    projections and is the origin of autonomic outflow. The NST
    package must declare the right BA 16 as a **weak** cortical
    afferent, noting that BA 16's NST projection is at the
    associative edge of the sympathetic field.

../../brainparts/forebrain/telencephalon/cerebral_hemispheres/right/cortex/insular/brodmann_areas/brodmann_area_15  (forward reference)
    The inconstant intermediate anterior insular area. When built out,
    it must carry the same ``PRESENCE_PROBABILITY`` discipline as
    BA 16 and must declare the adjacency to BA 16 on both sides.

../../left/cortex/insular/brodmann_areas/brodmann_area_16
    The left-hemisphere homologue. Structural fields (BA number,
    region label, **presence probability**, agranular /
    peripaleocortical claustral gradient, architectonic
    neighbourhoods, BA-to-neighbour adjacency) MUST be
    byte-identical. Functional emphasis and clinical significance
    diverge — the right BA 16 is weighted toward sympathetic
    autonomic control, affective-salience detection, and
    interoceptive-affective integration; the left BA 16 is weighted
    toward parasympathetic autonomic control, language-linked
    salience, and language-linked emotional awareness. **The SUDEP
    asymmetry is the sharpest divergence**: the right BA 16 is
    arrhythmogenic-weighted, the left BA 16 is protective-weighted.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_16"
    HEMISPHERE          = "right"
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
        # **This field is byte-identical on the left and right —
        # presence is a species-level property, not a hemisphere-
        # level one.**

    NAMING_COLLISION_WITH = ()   # BA 16 has no naming collision

    FUNCTIONAL_DOMAINS  = (
                              "interoception",         # secondary /
                                                       # associative edge
                              "autonomic_control",     # right:
                                                       # sympathetic
                              "salience_network",
                              "social_emotional",
                              "multimodal_integration",
                              # NOTE: speech_articulation does NOT
                              # exist on the right. Excluded
                              # entirely.
                              # NOTE: vestibular_and_self_location
                              # is BA-13-emphasized on the right
                              # (see brodmann_area_13_middle_insula),
                              # not BA-16-emphasized. Excluded.
                              # NOTE: gustatory is EXCLUDED (BA 16
                              # is not a primary or secondary taste
                              # area; its chemosensory contribution
                              # is olfactory-limbic).
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "interoception":
                                  "rostral_associative_edge_"
                                  "bodily_state_visceral_integration",
                              "autonomic_control":
                                  "sympathetic_pressor_tachycardic_"
                                  "associative_edge",
                              "salience_network":
                                  "affective_salience_detection_"
                                  "stimulus_driven_reorienting",
                              "social_emotional":
                                  "interoceptive_affective_"
                                  "integration_felt_component",
                              "multimodal_integration":
                                  "olfactory_limbic_bodily_state_"
                                  "centered_affective_integration",
                          }

    MODERN_CROSSWALK    = {   # BA 16 → modern parcellation labels
                              "HCP_180":       ("AAIC",),   # partial
                              "Ongur_Price_2000": ("Iai", "Ial"),  # partial
                              "Petrides_Pandya":  ("Iam",),  # partial
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_ba16_sympathetic_associative_"
                              "edge",
                              "right_insula_sudep_arrhythmogenic_"
                              "dominance",
                              "right_anterior_insular_affective_"
                              "salience_dysfunction",
                              "right_insula_caudolateral_ofc_"
                              "secondary_taste_network",
                              "olfactory_limbic_seizure_"
                              "semiology",
                              "right_insular_glioma_resection",
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
dropped. **This caveat text is byte-identical to the left sibling's**
— presence is a species-level property, not a hemisphere property, and
the two hemispheres must not diverge in their handling of BA 16's
inconstancy.

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
  4. Mirror the promotion on the left side in the same commit.

**The presence-probability caveat propagates to any sub-package.** A
BA 16r package would also be inconstant (the medial prefrontal
continuation is not consistently distinguishable), and it must carry
its own ``PRESENCE_PROBABILITY`` field. The parent's
``PRESENCE_PROBABILITY`` is the **product** of the insular and medial
prefrontal probabilities, not the maximum of the two.

**The right-specific SUDEP anchor is a parent-level claim** and cannot
be cleanly attributed to the insular sub-component alone. The right
BA 16's arrhythmogenic-weighted contribution to SUDEP depends on both
the insular autonomic efferents and the medial prefrontal
continuation's role in peri-ictal autonomic control. A split would
require retaining the SUDEP anchor at the parent level.

**No split should be performed while the BA 15 forward reference is
unresolved.** Splitting BA 16 while BA 15 does not yet exist would
multiply unresolved references and make the anterior agranular
insular field harder to reconcile.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../brodmann_area_16``:

    MUST be identical (byte-for-byte):
        AREA_NAME              "brodmann_area_16"
        LOBE                   "insular"
        BRODMANN_NUMBER        16
        INSULAR_REGION         "anterior_inconstant"
        CYTOTECTONIC_GRADIENT  "agranular"
        ALTERNATE_NAMES        ("peripaleocortical_claustral",
                               "insula_olfactoria")
        PRESENCE_PROBABILITY   0.5 — presence is a species-level
                               property, not a hemisphere-level one
        NAMING_COLLISION_WITH  () — empty on both sides
        Architectonic neighbourhoods
        BA-to-neighbour adjacency (including the BA 15 forward
                               reference)
        MODERN_CROSSWALK       (the same HCP / Öngür-Price /
                               Petrides labels)
        SUBDIVISIONS           both empty (or both non-empty in
                               the same way, if a split is ever
                               done)
        The forward-declaration caveat text (byte-identical — the
                               BA 15 and BA 16r forward references
                               are species-level, not hemisphere-
                               level)

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
        DOMAIN_EMPHASIS        right: autonomic_control is
                               "sympathetic_pressor_tachycardic_
                               associative_edge"; salience_network
                               is "affective_salience_detection_
                               stimulus_driven_reorienting";
                               social_emotional is "interoceptive_
                               affective_integration_felt_
                               component"; interoception is
                               "rostral_associative_edge_bodily_
                               state_visceral_integration";
                               multimodal_integration is
                               "olfactory_limbic_bodily_state_
                               centered_affective_integration".
                               left: autonomic_control is
                               "parasympathetic_vagal_bradycardia_
                               depressor_associative_edge";
                               salience_network is "language_
                               linked_salience_detection";
                               social_emotional is "language_
                               linked_emotional_awareness_
                               olfactory_limbic"; interoception is
                               "rostral_associative_edge_olfactory_
                               contextual_integration";
                               multimodal_integration is
                               "olfactory_limbic_contextual_
                               language_linked_integration".
        CONNECTIVITY           same bundle names; right: BA 16 →
                               hypothalamus is sympathetic; BA 16 →
                               NST is sympathetic; amygdala → BA 16
                               is denser; BA 16 → right caudolateral
                               OFC is the right-lateralized
                               secondary taste network; callosal
                               traffic carries affective-salience
                               and sympathetic signals.
                               left: BA 16 → hypothalamus is
                               parasympathetic; BA 16 → NST is
                               parasympathetic; callosal traffic
                               carries language-linked salience and
                               parasympathetic signals.
        CLINICAL_ANCHORS       right: seven anchors (sympathetic
                               associative edge, **SUDEP
                               arrhythmogenic dominance**, affective-
                               salience dysfunction, caudolateral OFC
                               secondary taste network, olfactory-
                               limbic seizure semiology with
                               affective-autonomic weighting, glioma
                               resection, presence-probability
                               uncertainty).
                               left: six anchors (parasympathetic
                               associative edge, olfactory-limbic
                               seizure semiology with language-
                               linked weighting, language-linked
                               salience dysfunction, glioma
                               resection, **SUDEP protective-
                               weighted**, presence-probability
                               uncertainty).

**The SUDEP asymmetry is the sharpest single entry in this contract.**
Both hemispheres carry a SUDEP anchor, but they **point in opposite
directions**: the right BA 16 is **arrhythmogenic-weighted** (the
right insula's sympathetic weighting is implicated in peri-ictal fatal
arrhythmia), and the left BA 16 is **protective-weighted** (the left
insula's parasympathetic weighting is protective in the peri-ictal
window). A right package that copies the left's "SUDEP vulnerability"
anchor verbatim — or that drops the SUDEP anchor entirely — is a bug.
The two hemispheres contribute **opposite-direction** autonomic
influences during the peri-ictal window, and the SUDEP anchors must
reflect that.

**The `DOMAIN_EMPHASIS` asymmetry is the second sharpest entry.**
Both hemispheres carry the same five domains and both exclude the same
three, but the emphasis within every shared domain points in opposite
directions: the right BA 16 is the **sympathetic / affective-salience**
territory, the left BA 16 is the **parasympathetic / language-linked**
territory.

**The `PRESENCE_PROBABILITY` and forward-declaration caveats are
byte-identical on both sides** — they are species-level properties,
not hemisphere-level ones. Any deviation is a bug.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_16" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 16.
[ ] INSULAR_REGION is "anterior_inconstant".
[ ] CYTOTECTONIC_GRADIENT is "agranular".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's
    ("peripaleocortical_claustral", "insula_olfactoria").
[ ] **PRESENCE_PROBABILITY is set** (approximately 0.5) and is
    byte-identical to the left sibling's — presence is a
    species-level property.
[ ] NAMING_COLLISION_WITH is an empty tuple — BA 16 has no naming
    collision.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - interoception
    - autonomic_control
    - salience_network
    - social_emotional
    - multimodal_integration
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation — the domain
    does not exist on the right.
[ ] FUNCTIONAL_DOMAINS **excludes** vestibular_and_self_location —
    the domain is BA-13-emphasized on the right, not BA-16.
[ ] FUNCTIONAL_DOMAINS **excludes** gustatory — BA 16 is not a
    primary or secondary taste area; chemosensory contribution is
    olfactory-limbic.
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis** per domain:
    - interoception → rostral_associative_edge_bodily_state_
      visceral_integration
    - autonomic_control → sympathetic_pressor_tachycardic_
      associative_edge
    - salience_network → affective_salience_detection_stimulus_
      driven_reorienting
    - social_emotional → interoceptive_affective_integration_felt_
      component
    - multimodal_integration → olfactory_limbic_bodily_state_
      centered_affective_integration
[ ] MODERN_CROSSWALK is present, byte-identical to the left
    sibling's.
[ ] CONNECTIVITY documents:
    - prepyriform / periamygdaloid olfactory afferents (weighted
      toward the affective / autonomic aspect)
    - claustrum connections
    - VPMpc and VMpo thalamic afferents (weak / tertiary)
    - BA 14 → BA 16 intracortical afferent (weighted toward
      sympathetic / intensity content)
    - BA 16 → hypothalamus (sympathetic, right-specific)
    - BA 16 → NST (sympathetic, right-specific)
    - amygdala reciprocal connections (denser than the left's,
      supporting interoceptive-affective integration)
    - BA 16 → right caudolateral OFC (right-lateralized secondary
      taste network)
    - callosal traffic to left BA 16 (affective-salience and
      sympathetic, right-specific)
[ ] CLINICAL_ANCHORS contains the seven right-specific anchors:
    - right_ba16_sympathetic_associative_edge
    - **right_insula_sudep_arrhythmogenic_dominance**
    - right_anterior_insular_affective_salience_dysfunction
    - right_insula_caudolateral_ofc_secondary_taste_network
    - olfactory_limbic_seizure_semiology (affective-autonomic
      weighting)
    - right_insular_glioma_resection
    - human_presence_probability_clinical_uncertainty
[ ] The **right sympathetic associative edge** is documented as the
    primary right BA 16 anchor, citing right insular stimulation →
    pressor / tachycardic responses
    .
[ ] The **SUDEP arrhythmogenic dominance** is documented as a
    right-emphasized SUDEP anchor — the right insula's sympathetic
    weighting is implicated in peri-ictal arrhythmogenesis, whereas
    the left's parasympathetic weighting is protective in the
    peri-ictal window. **This anchor is the mirror-opposite of the
    left's `autonomic_stress_vulnerability_sudep` anchor, and the
    asymmetry must not be erased.**
[ ] The **right caudolateral OFC secondary taste network** is
    documented as a right-emphasized connectivity–clinical anchor
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
    the domain does not exist on the right, not merely that it is
    unassigned.
[ ] The **vestibular_and_self_location exclusion rationale** is
    documented: the domain is BA-13-emphasized on the right, and the
    right BA 13 is the canonical reference.
[ ] The **gustatory exclusion rationale** is documented: BA 16 is
    not a taste area.
[ ] The **forward-declaration caveat text is byte-identical to the
    left sibling's** — the BA 15 and BA 16r forward references are
    species-level, not hemisphere-level.
[ ] No SUBDIVISIONS promotion is performed while the BA 15 forward
    reference is unresolved.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, alternate names,
    PRESENCE_PROBABILITY, architectonic neighbourhoods, modern
    crosswalk, FUNCTIONAL_DOMAINS set, forward-declaration caveat
    text) match the left sibling; DOMAIN_EMPHASIS, CONNECTIVITY
    emphasis, and CLINICAL_ANCHORS deliberately differ.
[ ] **The SUDEP asymmetry is verified**: the right BA 16 carries an
    arrhythmogenic-weighted anchor, the left BA 16 carries a
    protective-weighted anchor, and neither has been copied verbatim
    from the other.
[ ] Any downstream code querying BA 16 must receive the
    PRESENCE_PROBABILITY field and must treat BA 16-specific results
    as conditional — this is the only insular BA package whose
    presence is probabilistic.
[ ] Any downstream code assigning BA 16 autonomic function must
    route through DOMAIN_EMPHASIS and must weight the right BA 16
    toward **sympathetic** and the left BA 16 toward
    **parasympathetic**.
[ ] Any downstream code querying BA 16 SUDEP contribution must
    weight the right BA 16 as **arrhythmogenic-weighted** and the
    left BA 16 as **protective-weighted** — the two hemispheres
    contribute opposite-direction autonomic influences, and averaging
    them would erase the lateralized signal.
"""