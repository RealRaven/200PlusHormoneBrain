"""
Brodmann Area 13 (Middle Insula) — Left Hemisphere
===================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_13_middle_insula   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 13** — the largest and most functionally diverse of
the six insular Brodmann areas. Unlike the primary gustatory cortex,
which is a functional *field* spanning multiple territories, BA 13 is a
single architectonic *territory*: the granular and dysgranular middle
insula.

Parent: ``..brodmann_areas`` (left insular BA registry) — sibling to
BA 14, BA 16, BA 41, BA 42, BA 43. **Sibling — not parent —** of
``...primary_gustatory_cortex``, which sits one level up under
``..insular``. The BA 13 / PGC relationship is overlap, not nesting.

This package is the **structural mirror** of
``../../right/cortex/insular/brodmann_areas/brodmann_area_13_middle_insula``.
The BA number, the region label, and the architectonic gradient are
identical on both sides; the **functional emphasis** and **clinical
significance** diverge substantially.

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
lobe**. In the left hemisphere it is bounded:

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
the insula supports.

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
            hedonic** processing of taste.
        salience network (anterior insula)
            BA 13's dorsal (granular) portion is part of the
            anterior insula's salience-network hub, though the
            densest salience-network territory lies in the
            anterior short gyri (BA 16 / anterior granular
            insula).
        middle short gyrus surgical corridor
            BA 13's dorsal aspect overlaps the middle short gyrus
            — the resection target for eating-reflex seizures.
        von Economo neuron territory
            BA 13 contains a subset of the VEN population; the
            densest VEN territory lies more anteriorly, but the
            BA 13 VENs contribute to social-emotional appraisal.

**This field is byte-identical to the right sibling's** — the
architectonic neighbourhoods and functional overlays are the same on
both sides. What differs is the **emphasis** within each overlay (see
the FUNCTIONAL DOMAINS section).

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

**This field is byte-identical to the right sibling's.** The adjacency
relationships are topological, not lateralized.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 13 participates in **five** canonical insular domains. On the left
hemisphere, the emphasis is as follows:

    interoception                              (left emphasis)
        BA 13 is part of the **middle insular interoceptive cortex**
        — the transition zone between the primary interoceptive
        cortex (posterior agranular insula) and the anterior
        re-representation (anterior insula). On the left, BA 13's
        interoceptive contribution is **weaker than on the right**:
        the right BA 13 is the BA most strongly associated with
        interoceptive accuracy and heartbeat-evoked potentials
        (Critchley et al. 2004), while the left BA 13 is more
        strongly weighted toward the gustatory and multimodal
        contributions described below.

    nociception_and_pain_affect                  (left emphasis)
        BA 13 contributes to the **affective-motivational**
        dimension of pain — the "how bad it feels" component that
        the anterior insula supports, as opposed to the primary
        nociceptive topography of the posterior insula. On the
        left, the affective-pain contribution is relatively less
        dominant than the gustatory / hedonic-valuation
        contribution; on the right, the affective-pain contribution
        is stronger.

    gustatory                                    (left emphasis — PRIMARY)
        **This is BA 13's dominant contribution on the left.** BA 13
        is the BA that most directly supports the **left PGC's
        hedonic-valuation interface** — the projection of the left
        gustatory field into the affective-value network. BA 13
        itself is not a primary gustatory recipient (VPMpc projects
        most densely to BA 43 and area G, not BA 13); instead, BA 13
        receives **secondary gustatory input** from the PGC and
        integrates it with interoceptive, affective, and
        reward-related signals. On the left, this integration is
        weighted toward the **recognition-linked and
        language-adjacent** aspects of taste valuation; on the
        right, it is weighted toward **intensity-linked** and
        **interoceptive-urge** aspects.

    multimodal_integration                       (left emphasis)
        BA 13 is a **convergence zone** for taste, smell,
        somatosensory (oral texture, temperature), visceral, and
        (on the right more than the left) vestibular signals. On
        the left, the integration is weighted toward **orally
        centered** signals (taste, texture, temperature) and
        language-adjacent evaluation; on the right, it is weighted
        toward **bodily-state** signals (visceral, vestibular,
        autonomic).

    social_emotional                             (left emphasis)
        BA 13 contributes to the **emotional-awareness** network —
        the "how do I feel?" component of emotion. On the left,
        the contribution is weighted toward **language-linked
        emotional awareness** (naming, narrating, and reflecting on
        emotion); on the right, toward **interoceptive-affective
        integration** (the "felt" component). BA 13's VENs
        contribute to both, with the left's VENs more strongly
        connected to language-adjacent cortex.

**Left-specific caveat on `speech_articulation`.** BA 13 does **not**
carry the `speech_articulation` domain. That domain belongs to the
insular lobe as a whole (see the parent registry's
`SPEECH_ARTICULATION_CAVEAT`) and the critical structure is the
**precentral gyrus of the insula**, which straddles BA 13, BA 16, and
the opercular transition. **BA 13 should not claim the domain
exclusively.** Its package's `FUNCTIONAL_DOMAINS` tuple must therefore
**exclude** `speech_articulation`, and its docstring must not describe
the apraxia-of-speech lesion literature as if it were BA 13's
signature — the lesion is *not* confined to BA 13.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → VMpo (posterior ventromedial nucleus, parvicellular part)
            The interoceptive and nociceptive thalamic relay.
            VMpo projects to the middle and posterior insula,
            including BA 13. On the left, VMpo → BA 13 is the
            substrate of the left BA 13's pain-affect and
            multimodal contributions; the interoceptive component
            is stronger on the right.
        → VPMpc (parvicellular ventroposteromedial nucleus)
            The gustatory thalamic relay. VPMpc projects most
            densely to BA 43 and area G, with a **secondary
            projection to BA 13** — the anatomical substrate of
            BA 13's secondary gustatory role. On the left, this
            secondary projection supports the left PGC's
            hedonic-valuation interface.

    cortical afferents
        → primary gustatory cortex (PGC), left
            The left PGC projects to left BA 13 as part of the
            hedonic-valuation interface. This is the **dominant
            left-specific cortical afferent** of BA 13.
        → anterior insula / BA 16
            Reciprocal connections with the anterior granular
            insula, supporting the salience-network transition.
        → orbitofrontal cortex (OFC), left
            The left BA 13 → left OFC projection carries the
            affective-value signal of taste and interoception
            forward to the secondary taste area and the reward
            network.

    subcortical afferents / efferents
        → amygdala (basolateral nuclei), left
            Reciprocal connections support the affective-valuation
            and interoceptive-affective integration functions.
            On the left, the amygdala → BA 13 projection is the
            substrate of the **language-linked emotional
            awareness** the left insula supports; the
            **interoceptive-affective integration** component is
            stronger on the right.
        → hypothalamus (lateral hypothalamus), left
            BA 13 → LH projections support autonomic and
            ingestive control. On the left, the emphasis is on
            **parasympathetic** outflow (depressor, bradycardic);
            on the right, **sympathetic** outflow (pressor,
            tachycardic).
        → ventral striatum / nucleus accumbens
            The BA 13 → OFC → ventral striatum pathway supports
            the reward value of taste and interoception.

    brainstem interactions
        → parabrachial nucleus (indirect via thalamus)
        → periaqueductal gray (indirect via hypothalamus)
            These pathways support the autonomic and ingestive
            functions BA 13 participates in. On the left, the
            emphasis is parasympathetic; on the right,
            sympathetic.

    callosal connections
        → right BA 13
            Interhemispheric coordination of the middle insula.
            The left BA 13 → right BA 13 traffic is weighted
            toward **recognition-linked** signals (the left
            recognizing taste) and **language-linked** emotional
            awareness; the right → left traffic is weighted
            toward **intensity-linked** and **interoceptive**
            signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in three respects:
(a) the PGC → BA 13 afferent is weighted toward recognition and
hedonic valuation rather than intensity;
(b) the BA 13 → hypothalamus projection is parasympathetic rather than
sympathetic;
(c) the callosal traffic carries recognition-linked rather than
intensity-linked signals.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_pgc_hedonic_valuation_interface
        **This is the left BA 13 anchor par excellence.** BA 13 is the
        architectonic territory most directly coupled to the left
        PGC's hedonic-valuation interface — the projection of the left
        gustatory field into the affective-value network. Lesions
        that damage the **left BA 13 / PGC interface** can produce
        **altered taste pleasantness** (foods that were previously
        liked become indifferent or aversive) without producing
        primary ageusia. This is a *left-specific* signature: the
        right PGC / BA 13 interface is more weighted toward
        **taste-intensity** processing, so right-sided lesions
        produce intensity deficits rather than hedonic shifts.

    left_insular_stroke_taste_dysfunction
        Left insular strokes produce an **ipsilateral intensity
        deficit but a bilateral recognition deficit** (see the PGC
        leaf package). BA 13 contributes to the **recognition and
        hedonic** components of this deficit pattern — its lesions
        degrade the brain's ability to assign affective value to a
        recognized taste, even when the taste is still recognized
        correctly.

    eating_reflex_seizures
        BA 13's dorsal aspect overlaps the **middle short gyrus** —
        the resection target for eating-reflex seizures. Left-sided
        eating-reflex seizures have been successfully treated by
        resection of the middle short gyrus, and the insulo-
        hippocampal epileptogenic circuit that sustains them passes
        through BA 13's territory.

    central_post_stroke_pain
        Insular lesions — including those involving BA 13 — can
        produce **central post-stroke pain** (thalamic pain
        syndrome with insular contribution). On the left, the
        affective-motivational component (the "how bad it feels"
        aspect) is more prominent in the clinical presentation;
        on the right, the primary sensory-discriminative
        component is more prominent.

    autonomic_dysfunction_left_parasympathetic
        Left BA 13 lesions can produce **parasympathetic
        dysregulation** — the mirror of the right BA 13's
        sympathetic contribution. Clinical signatures include
        **bradycardia, hypotension, and altered gastric motility**
        during or after left insular stroke. The right BA 13's
        sympathetic signature (pressor, tachycardic) is documented
        in the right sibling.

    language_linked_emotional_awareness
        BA 13's contribution to the **emotional-awareness network**
        is weighted toward **language-linked awareness** on the
        left — naming, narrating, and reflecting on emotion.
        Left BA 13 lesions can produce a **dissociation between
        felt and named emotion** — the patient can name what they
        should feel without the felt component, or vice versa.
        This is a left-specific anchor; the right BA 13's
        contribution is more weighted toward the **felt**
        component.

    salience_network_dysfunction
        BA 13's dorsal aspect participates in the salience
        network, and left BA 13 lesions can produce **task-switch
        deficits** and **reduced responsiveness to behaviourally
        relevant stimuli**. The salience-network contribution is
        weaker than the anterior insula's, but BA 13's position
        between the anterior hub and the posterior interoceptive
        cortex makes it a **relay node** whose lesions can
        disconnect the two.

    insular_glioma_resection
        Because BA 13 is a **buried territory** beneath the
        opercula, resecting an insular glioma in the left BA 13
        zone requires careful mapping of taste function, autonomic
        function, and language. Left BA 13 resections risk
        **altered taste pleasantness**, **parasympathetic
        dysregulation**, and **emotional-awareness deficits** —
        distinct from the risks of anterior short gyri resections
        (apraxia of speech) and posterior insula resections
        (primary interoceptive / pain deficits).

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 13 / PGC interface is weighted toward hedonic
valuation (right is intensity); (b) the left BA 13 autonomic
contribution is parasympathetic (right is sympathetic). The right
sibling's docstring carries the corresponding right-sided anchors.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left insular BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 13, and enforcer
    of the ``speech_articulation`` exclusion.

..brodmann_area_14
    Caudal / ventral neighbour. The granular-to-agranular transition
    from BA 13 to BA 14 is one of the two architectonic gradients
    within the middle insula.

..brodmann_area_16
    Rostral neighbour. The granular transition from BA 13 to BA 16
    is the other architectonic gradient within the middle insula.

..brodmann_area_41_posterior_insula
..brodmann_area_42_posterior_insula
    Caudal neighbours in the insular-opercular transition zone. The
    naming-collision contract at the parent registry applies.

..brodmann_area_43_anterior_insula
    The **classical primary gustatory area**. BA 13 is **not** BA 43;
    BA 13 receives **secondary** gustatory input and integrates it
    with affective and interoceptive signals. The BA 43 / BA 13
    boundary is a primary-to-secondary gustatory gradient, not a
    primary-to-primary one.

...primary_gustatory_cortex
    The **functional-field sibling** (one level up, under
    ``..insular``). BA 13 is the architectonic territory most
    directly coupled to the left PGC's hedonic-valuation
    interface. The overlap is functional, not nesting: the PGC
    spans BA 43 + area G + opercula + (conditionally) base of
    central sulcus + BA 13 (as the secondary / hedonic
    integration site).

..cortex.frontal
    The frontal operculum covers BA 13 dorsally. The frontal
    package must declare the insula as a hidden neighbour and
    must note the left BA 13 / PGC interface in its own
    cross-references.

..cortex.parietal
    The parietal operculum (area G) is adjacent to BA 13's caudal
    margin. The parietal package must declare the insula as a
    hidden neighbour.

..cortex.cingulate
    The dorsal anterior cingulate is the salience-network partner
    of the anterior insula; BA 13's dorsal aspect participates in
    the same network. The cingulate package must declare the
    anterior insula as its salience-network partner.

../../subcortical/medial_temporal_lobe/amygdala
    The left basolateral amygdala sends a projection to left BA 13
    that supports the **language-linked emotional awareness**
    function. The amygdala package must declare the left BA 13 as
    a cortical target.

../../subcortical/diencephalon/hypothalamus
    The left BA 13 → left hypothalamus projection supports
    **parasympathetic** autonomic control. The hypothalamus
    package must declare BA 13 as a cortical afferent.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The BA 13 → OFC → ventral striatum pathway supports the reward
    value of taste and interoception.

../../subcortical/diencephalon/thalamus
    The **VMpo** (interoceptive / nociceptive) and **VPMpc**
    (gustatory) thalamic nuclei project to BA 13, with VMpo
    primary and VPMpc secondary. The thalamus package must
    declare both as cortical afferents to BA 13.

../../right/cortex/insular/brodmann_areas/brodmann_area_13_middle_insula
    The right-hemisphere homologue. Structural fields (BA number,
    region label, architectonic neighbourhoods, BA-to-neighbour
    adjacency) MUST be byte-identical. Functional emphasis and
    clinical significance diverge — the left BA 13 is weighted
    toward the PGC hedonic-valuation interface, parasympathetic
    autonomic control, and language-linked emotional awareness;
    the right BA 13 is weighted toward interoceptive accuracy,
    vestibular self-location, sympathetic autonomic control, and
    the felt component of emotional awareness.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_13_middle_insula"
    HEMISPHERE          = "left"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 13
    INSULAR_REGION      = "middle_insular"
    CYTOTECTONIC_GRADIENT = "granular_to_dysgranular"

    NAMING_COLLISION_WITH = ()   # BA 13 has no naming collision

    FUNCTIONAL_DOMAINS  = (
                              "interoception",
                              "nociception_and_pain_affect",
                              "gustatory",             # secondary /
                                                       # hedonic
                              "multimodal_integration",
                              "social_emotional",
                              # NOTE: speech_articulation is
                              # intentionally EXCLUDED. The domain
                              # belongs to the insular lobe as a
                              # whole (see parent registry's
                              # SPEECH_ARTICULATION_CAVEAT) and the
                              # critical structure is the precentral
                              # gyrus of the insula, which straddles
                              # BA 13, BA 16, and the opercular
                              # transition. BA 13 does not claim it.
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "interoception":
                                  "middle_insular_secondary",
                              "nociception_and_pain_affect":
                                  "affective_motivational",
                              "gustatory":
                                  "secondary_hedonic_valuation_"
                                  "interface_with_left_PGC",
                              "multimodal_integration":
                                  "orally_centered_language_"
                                  "adjacent_evaluation",
                              "social_emotional":
                                  "language_linked_emotional_"
                                  "awareness",
                          }

    MODERN_CROSSWALK    = {   # BA 13 → modern parcellation labels
                              "HCP_180":       ("Ig", "Id"),
                              "Ongur_Price_2000": ("Iai", "Ial", "Ig"),
                              "Petrides_Pandya":  ("Ig", "Id"),
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_pgc_hedonic_valuation_interface",
                              "left_insular_stroke_taste_dysfunction",
                              "eating_reflex_seizures",
                              "central_post_stroke_pain",
                              "autonomic_dysfunction_left_"
                              "parasympathetic",
                              "language_linked_emotional_awareness",
                              "salience_network_dysfunction",
                              "insular_glioma_resection",
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
  4. Mirror the promotion on the right side in the same commit.

**The BA-to-modern-crosswalk caveat**: if BA 13 is split, the
``MODERN_CROSSWALK`` field must be updated to reflect the split —
HCP ``Ig`` overlaps the granular component, HCP ``Id`` overlaps the
dysgranular component, but the mapping is not clean. The parent
package remains the canonical answer to "what does BA 13 correspond
to in modern parcellations?"; the components are **refinements**,
not new architectonic entities with their own modern labels.

**No split should be performed while the PGC sibling's
`CORTICAL_TERRITORIES` still references BA 13 as a single unit.**
The PGC package's overlap with BA 13 is via the middle insular / area
G transition, which is not cleanly decomposable into granular and
dysgranular components. A BA 13 split would require a joint
revision of both the BA 13 package and the PGC package in the same
commit, in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_13_middle_insula``:

    MUST be identical (byte-for-byte):
        AREA_NAME              "brodmann_area_13_middle_insula"
        LOBE                   "insular"
        BRODMANN_NUMBER        13
        INSULAR_REGION         "middle_insular"
        CYTOTECTONIC_GRADIENT  "granular_to_dysgranular"
        NAMING_COLLISION_WITH  () — empty on both sides
        Bounding / overlapping territories (architectonic
                               neighbours and functional overlays)
        BA-to-neighbour adjacency
        MODERN_CROSSWALK       (the same HCP / Öngür-Price /
                               Petrides labels)
        SUBDIVISIONS           both empty (or both non-empty in
                               the same way, if a split is ever
                               done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        FUNCTIONAL_DOMAINS     both sides carry the same five
                               domains (interoception, nociception,
                               gustatory, multimodal_integration,
                               social_emotional) and both exclude
                               speech_articulation. The set is
                               identical.
        DOMAIN_EMPHASIS        left: interoception is
                               "middle_insular_secondary";
                               gustatory is
                               "secondary_hedonic_valuation_
                               interface_with_left_PGC";
                               multimodal_integration is
                               "orally_centered_language_adjacent_
                               evaluation"; social_emotional is
                               "language_linked_emotional_
                               awareness".
                               right: interoception is
                               "primary_interoceptive_accuracy_
                               heartbeat_evoked"; gustatory is
                               "secondary_intensity_concentration_
                               interface_with_right_PGC";
                               multimodal_integration is
                               "bodily_state_centered_visceral_
                               vestibular"; social_emotional is
                               "interoceptive_affective_
                               integration_felt_component".
        CONNECTIVITY           same bundle names; left: PGC → BA 13
                               is weighted toward recognition and
                               hedonic valuation; BA 13 → hypothalamus
                               is parasympathetic; callosal traffic
                               carries recognition-linked signals.
                               right: PGC → BA 13 is weighted toward
                               intensity; BA 13 → hypothalamus is
                               sympathetic; callosal traffic carries
                               intensity-linked signals.
        CLINICAL_ANCHORS       left: altered taste pleasantness
                               from left BA 13 / PGC interface
                               lesions; ipsilateral intensity /
                               bilateral recognition deficit;
                               eating-reflex seizure resection;
                               central post-stroke pain with
                               dominant affective component;
                               parasympathetic dysregulation
                               (bradycardia, hypotension, altered
                               gastric motility); dissociation
                               between felt and named emotion;
                               salience-network task-switch
                               deficits; insular glioma resection
                               with taste / autonomic / emotional
                               risks.
                               right: ipsilateral taste-intensity
                               deficit; interoceptive accuracy
                               deficit; body-ownership and
                               vestibular deficits
                               (asomatognosia, somatoparaphrenia);
                               sympathetic pressor / tachycardic
                               responses; smoking-addiction
                               disruption; right insula
                               taste-cognition hypometabolism in
                               Alzheimer's disease.

**The `DOMAIN_EMPHASIS` asymmetry is the sharpest single entry in this
contract.** Both hemispheres carry the same five domains and both
exclude `speech_articulation`, but the emphasis within each domain
points in opposite directions: the left BA 13 is the **hedonic-
valuation / language-linked** hemisphere, the right BA 13 is the
**interoceptive / intensity-linked** hemisphere. A right-hemisphere
package that copies the left's `DOMAIN_EMPHASIS` verbatim is a bug —
the two hemispheres are **not the same BA with different labels**, they
are **functionally distinct BAs under the same number**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_13_middle_insula".
[ ] HEMISPHERE is "left".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 13.
[ ] INSULAR_REGION is "middle_insular".
[ ] CYTOTECTONIC_GRADIENT is "granular_to_dysgranular".
[ ] NAMING_COLLISION_WITH is an empty tuple — BA 13 has no
    naming collision.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - interoception
    - nociception_and_pain_affect
    - gustatory
    - multimodal_integration
    - social_emotional
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation — BA 13
    does not claim the apraxia-of-speech domain.
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis** per domain:
    - interoception → middle_insular_secondary (weaker than right)
    - nociception → affective_motivational
    - gustatory → secondary_hedonic_valuation_interface_with_left_PGC
    - multimodal_integration → orally_centered_language_adjacent
    - social_emotional → language_linked_emotional_awareness
[ ] MODERN_CROSSWALK is present with HCP / Öngür-Price / Petrides
    mappings.
[ ] CONNECTIVITY documents:
    - VMpo (primary) and VPMpc (secondary) thalamic afferents
    - PGC → BA 13 afferent (left-specific, weighted toward
      recognition and hedonic valuation)
    - BA 13 → OFC projection (affective-value signal)
    - BA 13 → hypothalamus (parasympathetic, left-specific)
    - amygdala reciprocal connections
    - BA 13 → ventral striatum pathway
    - callosal traffic to right BA 13 (recognition-linked,
      left-specific)
[ ] CLINICAL_ANCHORS contains the eight left-specific anchors:
    - left_pgc_hedonic_valuation_interface
    - left_insular_stroke_taste_dysfunction
    - eating_reflex_seizures
    - central_post_stroke_pain
    - autonomic_dysfunction_left_parasympathetic
    - language_linked_emotional_awareness
    - salience_network_dysfunction
    - insular_glioma_resection
[ ] The **BA 13 ≠ BA 43** distinction is documented: BA 13 is the
    secondary / hedonic taste territory; BA 43 is the primary
    gustatory area.
[ ] The **BA 13 ≠ PGC** distinction is documented: BA 13 is the
    architectonic territory; PGC is the functional field that
    overlaps it as the secondary / hedonic integration site.
[ ] The **BA numbering caveat** is documented (Brodmann's scheme
    is conventional; modern parcellations use different labels).
[ ] The **eating-reflex seizure** anchor is documented — BA 13's
    dorsal aspect overlaps the middle short gyrus, the resection
    target.
[ ] The **left-specific parasympathetic autonomic emphasis** is
    documented and distinguished from the right's sympathetic
    emphasis.
[ ] The **left-specific language-linked emotional awareness**
    anchor is documented and distinguished from the right's felt
    component.
[ ] No forward-declaration caveat is needed — all neighbours and
    targets exist.
[ ] No SUBDIVISIONS promotion is performed without mirroring on
    the right and without a joint PGC package revision.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, neighbourhoods,
    modern crosswalk, FUNCTIONAL_DOMAINS set) match the right
    sibling; DOMAIN_EMPHASIS, CONNECTIVITY emphasis, and
    CLINICAL_ANCHORS deliberately differ.
[ ] Any downstream code assigning BA 13 function must route
    through DOMAIN_EMPHASIS, not through FUNCTIONAL_DOMAINS alone
    — the set is hemisphere-invariant but the emphasis is not.
"""