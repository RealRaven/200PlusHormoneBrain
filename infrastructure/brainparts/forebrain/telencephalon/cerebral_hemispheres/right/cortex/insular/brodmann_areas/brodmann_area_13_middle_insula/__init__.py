"""
Brodmann Area 13 (Middle Insula) — Right Hemisphere
====================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_13_middle_insula   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the right
hemisphere's **BA 13** — the largest and most functionally diverse of
the six insular Brodmann areas. Unlike the primary gustatory cortex,
which is a functional *field* spanning multiple territories, BA 13 is a
single architectonic *territory*: the granular and dysgranular middle
insula.

Parent: ``..brodmann_areas`` (right insular BA registry) — sibling to
BA 14, BA 16, BA 41, BA 42, BA 43. **Sibling — not parent —** of
``...primary_gustatory_cortex``, which sits one level up under
``..insular``. The BA 13 / PGC relationship is overlap, not nesting.

This package is the **structural mirror** of
``../../left/cortex/insular/brodmann_areas/brodmann_area_13_middle_insula``.
The BA number, the region label, and the architectonic gradient are
identical on both sides; the **functional emphasis** and **clinical
significance** diverge substantially. **On the right, BA 13 is the
hemisphere's principal interoceptive-accuracy node** — the architectonic
territory whose activity best predicts heartbeat-evoked potentials and
interoceptive sensitivity (Critchley et al. 2004). The left BA 13 is
weighted instead toward the PGC's hedonic-valuation interface.

--------------------------------------------------------------------------------
WHAT BA 13 IS
--------------------------------------------------------------------------------

BA 13 occupies the **middle third of the insular lobe**, running from
the anterior short gyri caudally toward the central insular sulcus. It
spans the **granular-to-dysgranular cytoarchitectonic transition** that
marks the middle insula: granular (dorsally) where it borders the
anterior insula, dysgranular (ventrally and caudally) as it approaches
the agranular posterior insula.

BA 13 is the **largest single architectonic territory in the insular
lobe**. In the right hemisphere it is bounded:

    rostrally    by BA 16 (anterior inconstant insula) and the
                 anterior short gyri
    caudally     by BA 14 (ventral anterior insula) ventrally, and by
                 the agranular posterior insula dorsocaudally
    dorsally     by the circular sulcus (upper bank)
    ventrally    by the inferior limiting sulcus and the claustrum

BA 13 **overlaps with the middle short gyrus** on its dorsal aspect —
the gyral territory whose resection is documented as a treatment for
eating-reflex seizures. It therefore carries both an
**architectonic** identity (the granular/dysgranular middle insula) and
a **surgical** identity (the middle short gyrus corridor).

BA 13 also contains a subset of the **von Economo neurons (VENs)** that
concentrate in the anterior insula and anterior cingulate. VEN density
within BA 13 is lower than in the anterior short gyri, but the VENs that
are present contribute to the fast social-emotional appraisal functions
the insula supports. **On the right, VEN-related functional
connectivity is weighted toward interoceptive and affective salience,
whereas on the left it is weighted toward language-adjacent appraisal.**

**A caution about the BA 13 label.** As the parent ``..brodmann_areas``
docstring notes, Brodmann's original 1–52 scheme did not include a
dedicated insular series. BA 13 was delineated by later anatomists
working within his numbering, and modern parcellations (Öngür & Price
2000; Petrides & Pandya; the HCP 180-area scheme) use different labels
and boundaries for the same territory — HCP areas ``Ig`` (granular),
``Id`` (dysgranular), and ``AAIC`` (anterior agranular insular complex)
collectively cover what BA 13 denotes here. **Downstream code must not
treat "BA 13" as a stand-in for any single modern parcel**; it must
route through the ``MODERN_CROSSWALK`` field described below.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

BA 13 has both **architectonic neighbours** (the other insular BAs) and
**functional overlays** (the domains whose processing it participates
in):

    Architectonic neighbours
        rostrally    BA 16 (anterior inconstant insula)
        caudally     BA 14 (ventral anterior insula)
                     agranular posterior insula
        dorsally     circular sulcus / upper bank
        ventrally    inferior limiting sulcus / claustrum

    Functional overlays
        primary gustatory cortex (PGC)
            BA 13 overlaps the **posterior margin of the PGC's
            cortical territories** — the area G / middle insular
            transition. BA 13 is NOT the primary gustatory area
            (BA 43 is), but it participates in the **higher-order /
            intensity-linked** processing of taste on the right
            (the mirror of the left's hedonic processing).
        interoceptive accuracy network
            **On the right, BA 13 is a core node of the
            interoceptive-accuracy network** — the territory whose
            activity best predicts heartbeat-evoked potentials and
            interoceptive sensitivity. This is a right-emphasized
            overlay; the left BA 13 participates in the same
            network but at a lower weighting.
        salience network (anterior insula)
            BA 13's dorsal (granular) portion is part of the
            anterior insula's salience-network hub, though the
            densest salience-network territory lies in the
            anterior short gyri (BA 16 / anterior granular
            insula). On the right, the salience-network
            contribution is weighted toward **stimulus-driven
            reorienting and affective-salience detection**.
        middle short gyrus surgical corridor
            BA 13's dorsal aspect overlaps the middle short gyrus
            — the resection target for eating-reflex seizures.
        von Economo neuron territory
            BA 13 contains a subset of the VEN population; the
            densest VEN territory lies more anteriorly, but the
            BA 13 VENs contribute to social-emotional appraisal,
            with a **rightward emphasis on interoceptive-affective
            integration**.
        vestibular_and_self_location
            **Right-emphasized overlay.** The right middle insula
            (including BA 13) contributes to the vestibular and
            body-ownership representations that the left BA 13
            does not emphasize to the same degree. Right BA 13
            lesions can produce asomatognosia and
            somatoparaphrenia, and right BA 13 is engaged during
            vestibular and body-ownership challenges.

**This field is structurally identical to the left sibling's**, with
two right-emphasized functional overlays added: the
**interoceptive-accuracy network** and **vestibular_and_self_location**.
The architectonic neighbourhoods and the gustatory / salience /
eating-reflex / VEN overlays are the same on both sides; what differs
is the **emphasis** within each.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 14 (ventral anterior insula)        caudal / ventral neighbour;
                                           shares the agranular
                                           transition
    BA 16 (anterior inconstant)            rostral neighbour; shares
                                           the granular transition
    BA 43 (anterior insula / postcentral   rostromedial neighbour on the
    operculum)                             lateral bank; BA 13 sits
                                           between BA 16 and BA 43 in
                                           the gustatory hierarchy
    BA 41 / BA 42 (insular-opercular       caudal neighbours in the
    transition)                            insular-opercular transition
                                           zone (see the naming-
                                           collision contract at the
                                           parent registry)
    agranular posterior insula             caudal neighbour (not a
                                           distinct BA in the
                                           conventional scheme)

**This field is byte-identical to the left sibling's.** The adjacency
relationships are topological, not lateralized.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 13 participates in **six** canonical insular domains on the right
(the left has five; the right adds `vestibular_and_self_location` as a
BA-13-emphasized domain). On the right hemisphere, the emphasis is as
follows:

    interoception                              (right emphasis — PRIMARY)
        **This is BA 13's dominant contribution on the right.** BA 13
        is the architectonic territory whose activity best predicts
        **heartbeat-evoked potentials (HEPs)** and **interoceptive
        accuracy** (Critchley et al. 2004). The right BA 13 is the
        node whose lesion most reliably impairs **heartbeat
        detection**, and whose activity correlates with subjective
        interoceptive sensitivity across individuals. This is the
        single strongest right-BA-13 functional claim, and it has
        no left counterpart at the same weighting: the left BA 13
        participates in interoception but at secondary rather than
        primary emphasis.

    nociception_and_pain_affect                  (right emphasis)
        BA 13 contributes to the **affective-motivational**
        dimension of pain. On the right, the contribution is
        **stronger** than on the left: right BA 13 is more strongly
        engaged during **pain anticipation**, **sympathetic
        responses to noxious stimuli**, and **pain-related
        autonomic arousal**. The left BA 13's pain contribution is
        comparatively weaker; the left's affective-pain signal is
        carried more heavily by the anterior insula and the
        orbitofrontal interface.

    gustatory                                    (right emphasis — SECONDARY)
        BA 13's gustatory contribution is **secondary** — BA 13 is
        not a primary gustatory recipient (VPMpc projects most
        densely to BA 43 and area G, not BA 13). On the right, the
        secondary gustatory integration is weighted toward
        **intensity / concentration** processing — the mirror of
        the left's recognition / hedonic-valuation weighting. BA 13
        integrates the right PGC's intensity signal with
        interoceptive and autonomic signals (e.g., the "how
        strong" of a taste combined with the sympathetic arousal
        it produces).

    multimodal_integration                       (right emphasis)
        BA 13 is a **convergence zone** for taste, smell,
        somatosensory (oral texture, temperature), visceral, and
        vestibular signals. On the right, the integration is
        weighted toward **bodily-state** signals — visceral,
        vestibular, autonomic — rather than the left's orally
        centered, language-adjacent evaluation. The right BA 13
        is the site where the "body-state" representation of a
        taste is integrated with the intensity signal.

    social_emotional                             (right emphasis)
        BA 13 contributes to the **emotional-awareness** network.
        On the right, the contribution is weighted toward
        **interoceptive-affective integration** — the "felt"
        component of emotion, as opposed to the left's
        "named/narrated" component. Right BA 13 activity
        correlates with the subjective intensity of felt emotion
        during interoceptive challenges (e.g., the valence of a
        heartbeat-tracking task), and right insular lesions are
        more likely to produce **alexithymia-like** affective
        flattening than left insular lesions.

    vestibular_and_self_location                (right emphasis — RIGHT-ONLY)
        **This domain is BA-13-emphasized on the right and is not
        present at the same weighting on the left.** The right
        middle insula (including BA 13) is engaged during
        **vestibular stimulation**, during **body-ownership
        illusions** (the rubber-hand illusion, the full-body
        illusion), and during **self-location tasks**. Right BA 13
        lesions — especially right posterior-insular-adjacent
        lesions that extend into BA 13 — can produce
        **asomatognosia** and **somatoparaphrenia** (denial of
        ownership of the contralateral limb). This is the
        right-specific anchor par excellence for BA 13, and it
        has no counterpart of comparable weighting on the left.

**Right-specific caveat on `speech_articulation`.** Right BA 13 does
**not** carry the `speech_articulation` domain, and the domain **does
not exist on the right at all**. Right insular lesions do not produce
apraxia of speech. No right BA declares the domain. The right BA 13's
`FUNCTIONAL_DOMAINS` tuple must therefore **exclude** it, and the
package's docstring must not describe the apraxia-of-speech literature
— that is a left-only clinical concern documented in the left
sibling's package and the parent registry's
`SPEECH_ARTICULATION_CAVEAT`.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → VMpo (posterior ventromedial nucleus, parvicellular part)
            The interoceptive and nociceptive thalamic relay.
            **On the right, VMpo → BA 13 is the primary
            interoceptive substrate** — the pathway whose
            integrity is indexed by heartbeat-evoked potentials.
            This is the anatomical basis of the right BA 13's
            interoceptive-accuracy role.
        → VPMpc (parvicellular ventroposteromedial nucleus)
            The gustatory thalamic relay. VPMpc projects most
            densely to BA 43 and area G, with a **secondary
            projection to BA 13** — the anatomical substrate of
            BA 13's secondary gustatory role. On the right, this
            secondary projection supports the right PGC's
            intensity-processing interface.

    cortical afferents
        → primary gustatory cortex (PGC), right
            The right PGC projects to right BA 13 as part of the
            intensity-processing interface. This is the
            **right-emphasized cortical afferent** of BA 13; on
            the left, the PGC → BA 13 projection is weighted
            toward recognition and hedonic valuation.
        → anterior insula / BA 16
            Reciprocal connections with the anterior granular
            insula, supporting the salience-network transition.
            On the right, the salience-network weighting is
            toward stimulus-driven reorienting and affective
            salience detection.
        → orbitofrontal cortex (OFC), right
            The right BA 13 → right OFC projection carries the
            affective-value signal of taste and interoception
            forward to the secondary taste area and the reward
            network. On the right, the OFC's caudolateral
            secondary-taste territory is more consistently
            right-lateralized (see the PGC sibling), so the
            BA 13 → OFC → reward network loop is weighted toward
            the right's caudolateral OFC.

    subcortical afferents / efferents
        → amygdala (basolateral nuclei), right
            Reciprocal connections support the affective-valuation
            and interoceptive-affective integration functions.
            **On the right, the amygdala → BA 13 projection is
            the substrate of interoceptive-affective integration
            (the felt component of emotion)**, whereas the left's
            projection supports language-linked emotional
            awareness.
        → hypothalamus (lateral hypothalamus), right
            BA 13 → LH projections support autonomic and
            ingestive control. **On the right, the emphasis is
            on sympathetic outflow** (pressor, tachycardic);
            on the left, parasympathetic outflow (depressor,
            bradycardic).
        → ventral striatum / nucleus accumbens
            The BA 13 → OFC → ventral striatum pathway supports
            the reward value of taste and interoception. On the
            right, this pathway is the dominant
            interoceptive-urge substrate (the basis of
            smoking-addiction disruption from right insular
            damage).

    brainstem interactions
        → parabrachial nucleus (indirect via thalamus)
        → periaqueductal gray (indirect via hypothalamus)
            These pathways support the autonomic and ingestive
            functions BA 13 participates in. On the right, the
            emphasis is sympathetic; the PAG projection is
            associated with **affective defensive behaviour**
            (ictal fear, autonomic auras in right insular
            epilepsy).

    vestibular afferents
        → vestibular nuclei (via thalamic and direct brainstem
          relays)
            **Right-emphasized.** The right middle insula (BA 13
            included) receives vestibular input supporting the
            body-ownership and self-location functions. The
            anatomical basis of the right BA 13's
            vestibular_and_self_location domain.

    callosal connections
        → left BA 13
            Interhemispheric coordination of the middle insula.
            **On the right, the callosal traffic is weighted
            toward intensity-linked and interoceptive signals**;
            the left → right traffic carries recognition-linked
            and language-linked signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in four respects:
(a) the VMpo → BA 13 afferent is the primary interoceptive substrate
rather than a secondary one;
(b) the BA 13 → hypothalamus projection is sympathetic rather than
parasympathetic;
(c) the right BA 13 receives vestibular afferents at a higher
weighting, supporting the vestibular_and_self_location domain;
(d) the callosal traffic carries intensity-linked and interoceptive
signals rather than recognition-linked ones.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ba13_interoceptive_accuracy
        **This is the right BA 13 anchor par excellence.** The right
        BA 13 is the architectonic territory whose activity best
        predicts **heartbeat-evoked potentials (HEPs)** and
        **interoceptive accuracy** — the ability to accurately
        count one's own heartbeats (Critchley et al. 2004). Right
        insular lesions that include BA 13 reliably impair
        heartbeat detection, whereas left insular lesions do so
        less consistently. This is the strongest single
        right-lateralized functional claim in the human insula,
        and it has no left counterpart at the same weighting.

    right_insular_stroke_ipsilateral_taste_deficit
        Right insular strokes produce an **ipsilateral taste
        recognition and intensity deficit** — a unilateral
        pattern, in contrast to the left insula's bilateral
        recognition deficit. BA 13 contributes to the
        **intensity** component of this deficit pattern: right
        BA 13 lesions degrade the brain's ability to track *how
        strong* a taste is, while leaving *what* the taste is
        relatively intact. This is the mirror of the left BA 13's
        hedonic-recognition contribution.

    right_insula_autonomic_sympathetic_dysfunction
        Right BA 13 lesions can produce **sympathetic
        dysregulation** — pressor and tachycardic responses during
        or after right insular stroke, and altered
        cardiovascular reactivity to stress. This is the
        mirror of the left's parasympathetic signature
        (bradycardia, hypotension, altered gastric motility).

    right_insular_body_ownership_deficits
        Right BA 13 lesions — especially those that extend into
        the middle/posterior insula — can produce
        **asomatognosia** (failure to recognize one's own
        contralateral limb) and **somatoparaphrenia** (denial of
        ownership of the contralateral limb). These are
        right-lateralized syndromes; they are far less common
        after left insular lesions.

    right_insular_vestibular_syndrome
        Right BA 13 / middle insular lesions can produce
        **vestibular symptoms** — vertigo, subjective visual
        vertical tilt, and body-schema distortions — that are
        more prominent than the corresponding left-sided
        symptoms. This is the clinical counterpart of the
        right-emphasized vestibular_and_self_location domain.

    right_insula_smoking_addiction_disruption
        **Right insular damage — especially to the anterior
        portion including BA 13 — can disrupt smoking addiction**
        (Naqvi et al. 2007). Patients with right insular lesions
        report that their urge to smoke is abolished or markedly
        reduced, without conscious effort. The right BA 13 is
        part of the interoceptive-urge substrate that underlies
        this effect. This is a right-specific clinical anchor
        with no left counterpart of comparable strength.

    right_insular_seizures_affective_and_autonomic
        Right BA 13 / middle insular seizures can present with
        **ictal fear, autonomic auras, and dysgeusia** — the
        right-specific semiological cluster that reflects the
        right insula's sympathetic and affective-defensive
        weighting. This is the mirror of the left's
        language-adjacent and parasympathetic seizure semiology.

    right_eating_reflex_seizures
        **Eating-reflex seizures** have been successfully treated
        by **resection of the middle short gyrus of the right
        insula** — the dorsal BA 13 territory. The
        insulo-hippocampal epileptogenic circuit passes through
        BA 13's territory on the right as well as the left, and
        the right middle short gyrus is a documented resection
        target.

    right_insula_taste_cognition_alzheimers
        In Alzheimer's disease, **glucose metabolism in the right
        insula is lower in the low taste-cognition subgroup**,
        linking the right insula specifically to **taste
        cognition** — the memory-linked, food-recognition aspect
        of taste processing. The right BA 13 contributes to this
        right-emphasized function.

    right_insula_bulimia_bitter_sensitivity
        fMRI studies in bulimia nervosa patients show **reduced
        sensitivity to bitter stimuli in the right insular
        cortex**, indicating that right insular dysfunction in
        taste processing may contribute to the disorder's
        altered food reward processing. The right BA 13 is part
        of the intensity-sensitive substrate where this
        alteration is detectable.

    right_insular_glioma_resection
        Because BA 13 is a **buried territory** beneath the
        opercula, resecting a right insular glioma in the right
        BA 13 zone requires careful mapping of interoception,
        autonomic function, and body ownership. Right BA 13
        resections risk **interoceptive-accuracy deficits**,
        **sympathetic dysregulation**, and **body-ownership
        deficits** — distinct from the risks of anterior short
        gyri resections (prosody and inhibition on the right,
        speech articulation on the left) and posterior insula
        resections (primary interoceptive / pain deficits).

These anchors are **right-hemisphere-specific** in two senses:
(a) the right BA 13 / interoceptive-accuracy network is the dominant
interoceptive substrate (left is secondary); (b) the right BA 13
autonomic contribution is sympathetic (left is parasympathetic), and
the right BA 13 is the hemisphere where body-ownership and
smoking-addiction findings are documented. The left sibling's
docstring carries the corresponding left-sided anchors (PGC hedonic
interface, parasympathetic dysregulation, language-linked emotional
awareness).

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The right insular BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 13, and
    enforcer of the ``speech_articulation`` **exclusion** (which on
    the right means the domain is not declared anywhere, not that
    it is assigned to the lobe as a whole).

..brodmann_area_14
    Caudal / ventral neighbour. The granular-to-agranular transition
    from BA 13 to BA 14 is one of the two architectonic gradients
    within the middle insula. On the right, BA 14's autonomic
    emphasis is sympathetic; on the left, parasympathetic.

..brodmann_area_16
    Rostral neighbour. The granular transition from BA 13 to BA 16
    is the other architectonic gradient within the middle insula.

..brodmann_area_41_posterior_insula
..brodmann_area_42_posterior_insula
    Caudal neighbours in the insular-opercular transition zone. The
    naming-collision contract at the parent registry applies. On
    the right, the transition zone is more strongly engaged during
    thermoreceptive autonomic challenge and body-ownership
    violations.

..brodmann_area_43_anterior_insula
    The **classical primary gustatory area**. BA 13 is **not** BA 43;
    BA 13 receives **secondary** gustatory input and integrates it
    with interoceptive and autonomic signals. On the right, the
    BA 43 → BA 13 gustatory gradient is primary-intensity to
    secondary-intensity, not primary-recognition to
    secondary-recognition.

...primary_gustatory_cortex
    The **functional-field sibling** (one level up, under
    ``..insular``). BA 13 is the architectonic territory most
    directly coupled to the right PGC's intensity-processing
    interface. The overlap is functional, not nesting: the PGC
    spans BA 43 + area G + opercula + (conditionally) base of
    central sulcus + BA 13 (as the secondary / intensity
    integration site).

..cortex.frontal
    The frontal operculum covers BA 13 dorsally. The frontal
    package must declare the insula as a hidden neighbour and must
    note the right BA 13's interoceptive-accuracy role in its own
    cross-references.

..cortex.parietal
    The parietal operculum (area G) is adjacent to BA 13's caudal
    margin. The parietal package must declare the insula as a
    hidden neighbour.

..cortex.cingulate
    The dorsal anterior cingulate is the salience-network partner
    of the anterior insula; BA 13's dorsal aspect participates in
    the same network. On the right, the salience weighting is
    toward stimulus-driven reorienting.

../../subcortical/medial_temporal_lobe/amygdala
    The **right** basolateral amygdala → right BA 13 projection is
    the more strongly engaged substrate of
    **interoceptive-affective integration** (the "felt" component
    of emotion). The amygdala package must declare the right BA 13
    as a cortical target.

../../subcortical/diencephalon/hypothalamus
    The right BA 13 → right hypothalamus projection supports
    **sympathetic** autonomic control. The hypothalamus package
    must declare the right BA 13 as a cortical afferent.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The BA 13 → OFC → ventral striatum pathway supports the reward
    value of taste and interoception. On the right, this pathway
    is the dominant interoceptive-urge substrate.

../../subcortical/diencephalon/thalamus
    The **VMpo** (interoceptive / nociceptive) and **VPMpc**
    (gustatory) thalamic nuclei project to right BA 13, with VMpo
    primary (the anatomical basis of the right's
    interoceptive-accuracy role) and VPMpc secondary.

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem gustatory and
    visceral relay. On the right, the parabrachial → BA 13 pathway
    is weighted toward sympathetic autonomic control.

../../right/cortex/insular/brodmann_areas (this package's
    sibling registry) — not a separate cross-reference target,
    included for clarity.

../../left/cortex/insular/brodmann_areas/brodmann_area_13_middle_insula
    The left-hemisphere homologue. Structural fields (BA number,
    region label, cytotectonic gradient, architectonic
    neighbourhoods, BA-to-neighbour adjacency, modern crosswalk)
    MUST be byte-identical. Functional emphasis and clinical
    significance diverge — the right BA 13 is weighted toward
    interoceptive accuracy, vestibular self-location, sympathetic
    autonomic control, intensity-linked gustatory processing, and
    the felt component of emotional awareness; the left BA 13 is
    weighted toward the PGC's hedonic-valuation interface,
    parasympathetic autonomic control, recognition-linked
    gustatory processing, and language-linked emotional
    awareness.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_13_middle_insula"
    HEMISPHERE          = "right"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 13
    INSULAR_REGION      = "middle_insular"
    CYTOTECTONIC_GRADIENT = "granular_to_dysgranular"

    NAMING_COLLISION_WITH = ()   # BA 13 has no naming collision

    FUNCTIONAL_DOMAINS  = (
                              "interoception",
                              "nociception_and_pain_affect",
                              "gustatory",             # secondary /
                                                       # intensity
                              "multimodal_integration",
                              "social_emotional",
                              "vestibular_and_self_location",
                              # NOTE: speech_articulation does NOT
                              # exist on the right. It is excluded
                              # entirely — see the parent registry's
                              # SPEECH_ARTICULATION_CAVEAT, which on
                              # the right states the domain is
                              # absent, not merely unassigned.
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "interoception":
                                  "primary_interoceptive_accuracy_"
                                  "heartbeat_evoked",
                              "nociception_and_pain_affect":
                                  "affective_motivational_sympathetic_"
                                  "anticipatory",
                              "gustatory":
                                  "secondary_intensity_concentration_"
                                  "interface_with_right_PGC",
                              "multimodal_integration":
                                  "bodily_state_centered_visceral_"
                                  "vestibular",
                              "social_emotional":
                                  "interoceptive_affective_"
                                  "integration_felt_component",
                              "vestibular_and_self_location":
                                  "body_ownership_self_location_"
                                  "right_emphasized",
                          }

    MODERN_CROSSWALK    = {   # BA 13 → modern parcellation labels
                              "HCP_180":       ("Ig", "Id"),
                              "Ongur_Price_2000": ("Iai", "Ial", "Ig"),
                              "Petrides_Pandya":  ("Ig", "Id"),
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_ba13_interoceptive_accuracy",
                              "right_insular_stroke_ipsilateral_"
                              "taste_deficit",
                              "right_insula_autonomic_sympathetic_"
                              "dysfunction",
                              "right_insular_body_ownership_"
                              "deficits",
                              "right_insular_vestibular_syndrome",
                              "right_insula_smoking_addiction_"
                              "disruption",
                              "right_insular_seizures_affective_"
                              "and_autonomic",
                              "right_eating_reflex_seizures",
                              "right_insula_taste_cognition_"
                              "alzheimers",
                              "right_insula_bulimia_bitter_"
                              "sensitivity",
                              "right_insular_glioma_resection",
                          )

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "AREA_NAME",
        "HEMISPHERE",
        "LOBE",
        "BRODMANN_NUMBER",
        "INSULAR_REGION",
        "CYTOTECTONIC_GRADIENT",
        "NAMING_COLLISION_WITH",
        "FUNCTIONAL_DOMAINS",
        "DOMAIN_EMPHASIS",
        "MODERN_CROSSWALK",
        "CONNECTIVITY",
        "CLINICAL_ANCHORS",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references BA 13 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this package.** BA 13 is
an architectonic territory, and its neighbours (BA 14, BA 16, BA 41,
BA 42, BA 43) all exist as packages under ``..brodmann_areas``. Its
functional-field sibling ``...primary_gustatory_cortex`` exists under
``..insular``. Its cortical and subcortical targets exist or are being
built out in parallel. The package does not depend on any unresolved
name.

**The one conditional reference** is the **base of the central
sulcus**, which some MEG studies place as a short-latency taste
activation site. BA 13 does **not** extend to the base of the central
sulcus — that conditional territory belongs to the PGC. BA 13's
overlap with the PGC is confined to the **middle insular / area G
transition**, which is already fully resolvable through the PGC
sibling.

**The vestibular afferent reference** is worth flagging as
**partially conditional** — vestibular afferents to the insula are
documented in both anatomical and functional-imaging studies, but the
specific thalamic relay is less well localized than the VMpo and VPMpc
relays. The ``CONNECTIVITY`` entry for vestibular afferents should
therefore be tagged as ``"vestibular_via_thalamic_and_direct_brainstem_
relays"`` rather than as a single named tract.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 13 is genuinely **large and heterogeneous** — granular dorsally,
dysgranular ventrally and caudally. If a future parcellation decides
that the granular and dysgranular components should be separate
packages (some atlases do split BA 13 into ``BA 13a`` and ``BA 13b``),
the promotion takes this form:

    brodmann_area_13_middle_insula/
        __init__.py
        granular_component/
            __init__.py
        dysgranular_component/
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the left side in the same commit.

**The right-specific promotion caveat**: the right BA 13's
interoceptive-accuracy role and its vestibular_and_self_location role
are **not cleanly decomposable into granular and dysgranular
components**. Interoceptive accuracy is thought to depend on the
dysgranular middle insula (the more posterior portion), while
vestibular and body-ownership functions may extend across both
components. A BA 13 split on the right would therefore require a
**joint revision** of the right BA 13 package, the right PGC package,
and the parent right ``..insular`` registry in the same commit. No
right-side BA 13 split should be performed while the interoceptive-
accuracy and vestibular entries are still tagged at the parent level.

**The BA-to-modern-crosswalk caveat**: if BA 13 is split, the
``MODERN_CROSSWALK`` field must be updated to reflect the split —
HCP ``Ig`` overlaps the granular component, HCP ``Id`` overlaps the
dysgranular component, but the mapping is not clean. The parent
package remains the canonical answer to "what does BA 13 correspond
to in modern parcellations?"; the components are **refinements**,
not new architectonic entities with their own modern labels.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../brodmann_area_13_middle_insula``:

    MUST be identical (byte-for-byte):
        AREA_NAME              "brodmann_area_13_middle_insula"
        LOBE                   "insular"
        BRODMANN_NUMBER        13
        INSULAR_REGION         "middle_insular"
        CYTOTECTONIC_GRADIENT  "granular_to_dysgranular"
        NAMING_COLLISION_WITH  () — empty on both sides
        Bounding / overlapping territories (architectonic
                               neighbours)
        BA-to-neighbour adjacency
        MODERN_CROSSWALK       (the same HCP / Öngür-Price /
                               Petrides labels)
        SUBDIVISIONS           both empty (or both non-empty in
                               the same way, if a split is ever
                               done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        FUNCTIONAL_DOMAINS     right has **six** domains (the left's
                               five PLUS `vestibular_and_self_
                               location`). Both exclude
                               `speech_articulation`. The right
                               domain set is NOT a strict superset
                               of the left's at the emphasis level
                               — see DOMAIN_EMPHASIS — but it IS
                               a strict superset at the domain-set
                               level.
        DOMAIN_EMPHASIS        right: interoception is
                               "primary_interoceptive_accuracy_
                               heartbeat_evoked"; gustatory is
                               "secondary_intensity_concentration_
                               interface_with_right_PGC";
                               multimodal_integration is
                               "bodily_state_centered_visceral_
                               vestibular"; social_emotional is
                               "interoceptive_affective_
                               integration_felt_component";
                               vestibular_and_self_location is
                               "body_ownership_self_location_
                               right_emphasized".
                               left: interoception is
                               "middle_insular_secondary";
                               gustatory is
                               "secondary_hedonic_valuation_
                               interface_with_left_PGC";
                               multimodal_integration is
                               "orally_centered_language_
                               adjacent_evaluation";
                               social_emotional is
                               "language_linked_emotional_
                               awareness"; vestibular_and_self_
                               location is ABSENT.
        CONNECTIVITY           same bundle names; right: VMpo → BA 13
                               is primary (the substrate of
                               interoceptive accuracy); BA 13 →
                               hypothalamus is sympathetic;
                               vestibular afferents are present
                               at high weighting; callosal traffic
                               carries intensity-linked and
                               interoceptive signals.
                               left: VMpo → BA 13 is secondary;
                               PGC → BA 13 is weighted toward
                               recognition and hedonic valuation;
                               BA 13 → hypothalamus is
                               parasympathetic; callosal traffic
                               carries recognition-linked and
                               language-linked signals.
        CLINICAL_ANCHORS       right: eleven anchors (interoceptive
                               accuracy, ipsilateral taste-intensity
                               deficit, sympathetic dysregulation,
                               body-ownership deficits, vestibular
                               syndrome, smoking-addiction
                               disruption, affective / autonomic
                               seizures, eating-reflex seizures,
                               taste-cognition hypometabolism in
                               AD, bulimia bitter-sensitivity,
                               glioma resection risks).
                               left: eight anchors (PGC hedonic
                               interface, insular stroke taste
                               dysfunction, eating-reflex
                               seizures, central post-stroke
                               pain, parasympathetic dysregulation,
                               language-linked emotional
                               awareness, salience-network
                               dysfunction, glioma resection
                               risks).

**The `DOMAIN_EMPHASIS` asymmetry and the extra sixth domain are the
sharpest entries in this contract.** The right BA 13 carries six
functional domains, including `vestibular_and_self_location` which the
left does not carry at BA-13 emphasis. The right BA 13's
`DOMAIN_EMPHASIS` for every shared domain points in the opposite
direction from the left's: the right is interoceptive-accuracy /
intensity / bodily-state / felt-component; the left is
secondary-interoception / hedonic / orally-centered /
language-linked. A right-hemisphere package that copies the left's
`FUNCTIONAL_DOMAINS` set verbatim (five domains) or the left's
`DOMAIN_EMPHASIS` values is a bug — the two hemispheres are **not the
same BA with different labels**, they are **functionally distinct BAs
under the same number**.

**The `speech_articulation` asymmetry is reinforced here**: the right
BA 13 excludes the domain because it does **not exist on the right**,
whereas the left BA 13 excludes it because the domain belongs to the
**lobe as a whole**, not to any BA. Both packages exclude it from
their `FUNCTIONAL_DOMAINS` tuple, but the reason is different, and
the parent registry's `SPEECH_ARTICULATION_CAVEAT` records the
distinction. A right package that copies the left's reasoning
verbatim is a bug.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_13_middle_insula" (same as
    left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 13.
[ ] INSULAR_REGION is "middle_insular".
[ ] CYTOTECTONIC_GRADIENT is "granular_to_dysgranular".
[ ] NAMING_COLLISION_WITH is an empty tuple — BA 13 has no naming
    collision.
[ ] FUNCTIONAL_DOMAINS contains **six** domains:
    - interoception
    - nociception_and_pain_affect
    - gustatory
    - multimodal_integration
    - social_emotional
    - **vestibular_and_self_location** (right-only)
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation — the domain
    does not exist on the right.
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis** per domain:
    - interoception → primary_interoceptive_accuracy_heartbeat_evoked
    - nociception → affective_motivational_sympathetic_anticipatory
    - gustatory → secondary_intensity_concentration_interface_with_
      right_PGC
    - multimodal_integration → bodily_state_centered_visceral_vestibular
    - social_emotional → interoceptive_affective_integration_felt_
      component
    - vestibular_and_self_location → body_ownership_self_location_
      right_emphasized
[ ] MODERN_CROSSWALK is present with HCP / Öngür-Price / Petrides
    mappings, byte-identical to the left sibling's.
[ ] CONNECTIVITY documents:
    - VMpo (primary, interoceptive-accuracy substrate) and VPMpc
      (secondary) thalamic afferents
    - PGC → BA 13 afferent (right-specific, weighted toward intensity)
    - BA 13 → right caudolateral OFC projection (affective-value
      signal, right-emphasized)
    - BA 13 → hypothalamus (sympathetic, right-specific)
    - amygdala reciprocal connections (interoceptive-affective
      integration)
    - BA 13 → ventral striatum pathway (interoceptive-urge substrate)
    - vestibular afferents (via thalamic and direct brainstem relays,
      right-emphasized)
    - callosal traffic to left BA 13 (intensity-linked and
      interoceptive, right-specific)
[ ] CLINICAL_ANCHORS contains the eleven right-specific anchors:
    - right_ba13_interoceptive_accuracy
    - right_insular_stroke_ipsilateral_taste_deficit
    - right_insula_autonomic_sympathetic_dysfunction
    - right_insular_body_ownership_deficits
    - right_insular_vestibular_syndrome
    - right_insula_smoking_addiction_disruption
    - right_insular_seizures_affective_and_autonomic
    - right_eating_reflex_seizures
    - right_insula_taste_cognition_alzheimers
    - right_insula_bulimia_bitter_sensitivity
    - right_insular_glioma_resection
[ ] The **Critchley et al. 2004 interoceptive-accuracy** anchor is
    documented for BA 13 as the primary right-side anchor.
[ ] The **Naqvi et al. 2007 smoking-addiction** anchor is documented
    for right BA 13.
[ ] The **BA 13 ≠ BA 43** distinction is documented: BA 13 is the
    secondary / intensity taste territory on the right; BA 43 is the
    primary gustatory area.
[ ] The **BA 13 ≠ PGC** distinction is documented: BA 13 is the
    architectonic territory; PGC is the functional field that
    overlaps it as the secondary / intensity integration site.
[ ] The **BA numbering caveat** is documented (byte-identical to the
    left sibling's).
[ ] The **vestibular afferent conditional status** is documented —
    vestibular afferents are tagged as coming via thalamic and direct
    brainstem relays rather than through a single named tract.
[ ] The **speech-articulation exclusion rationale** is documented:
    the domain does not exist on the right, not merely that it is
    unassigned.
[ ] No forward-declaration caveat is needed — all neighbours and
    targets exist.
[ ] No SUBDIVISIONS promotion is performed without mirroring on the
    left and without a joint PGC package revision, given the
    right-specific interoceptive-accuracy and
    vestibular_and_self_location roles.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, architectonic
    neighbourhoods, modern crosswalk) match the left sibling;
    FUNCTIONAL_DOMAINS set (right has one extra domain), DOMAIN_
    EMPHASIS, CONNECTIVITY emphasis, and CLINICAL_ANCHORS deliberately
    differ.
[ ] Any downstream code assigning BA 13 function must route
    through DOMAIN_EMPHASIS, not through FUNCTIONAL_DOMAINS alone
    — the domain set is nearly hemisphere-invariant but the
    emphasis is not.
[ ] Any downstream code querying BA 13 interoceptive accuracy must
    weight the right BA 13 more heavily — the left is secondary.
[ ] Any downstream code querying BA 13 taste function must weight
    the right BA 13 toward intensity and the left BA 13 toward
    hedonic valuation.
"""