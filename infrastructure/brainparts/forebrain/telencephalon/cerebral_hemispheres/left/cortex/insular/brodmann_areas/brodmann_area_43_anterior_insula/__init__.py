"""
Brodmann Area 43 (Anterior Insula / Postcentral Operculum) — Left Hemisphere
=============================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_43_anterior_insula   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 43** — the **anterior insula / postcentral
operculum** territory that Brodmann identified as the **subcentral
area** and that modern gustatory neuroscience identifies as the
**primary gustatory cortex** . It is
the **only insular BA with a classical Brodmann number that maps
cleanly to a specific functional region**, and it is the **architectonic
core of the primary gustatory cortex (PGC)** — the functional field
that spans BA 43 plus area G, the opercula, and (conditionally) the base
of the central sulcus.

Parent: ``..brodmann_areas`` (left insular BA registry) — sibling to
BA 13, BA 14, BA 16, BA 41, BA 42.

This package is the **structural mirror** of
``../../right/cortex/insular/brodmann_areas/brodmann_area_43_anterior_insula``.
The BA number, the **dual cytoarchitectonic character** (gustatory +
oral somatosensory), the **PARCELATION_AMBIGUITY** field (postcentral
vs insular), and the **BA 43 ↔ PGC overlap** relationship are identical
on both sides; the **functional emphasis** and **clinical significance**
diverge — on the left, BA 43's gustatory territory is weighted toward
**taste recognition / flavour identity**, the **hedonic valuation
interface** with the left PGC, the **parasympathetic** autonomic
coupling of taste, and the **bilateral taste-recognition deficit**
that follows left insular damage.

--------------------------------------------------------------------------------
WHAT BA 43 IS — IN THE INSULAR CONTEXT
--------------------------------------------------------------------------------

BA 43 is the **most directly gustatory** of the six insular Brodmann
areas. It is the cortical territory at the **fundus of the circular
sulcus and the adjacent opercular surface** — the frontier between
the **anterior insula** and the **postcentral operculum** — and it is
the territory that the **VPMpc thalamic nucleus** (the parvicellular
ventroposteromedial gustatory relay) projects to most densely
. In Old World monkeys the VPMpc projection
zone is centred on the **dorsal (superior) part of the anterior
insular cortex and the adjacent frontal–parietal opercula**, and the
projection zone extends ventrally into dysgranular insular cortex and
dorsally/laterally into dysgranular opercular cortex . BA 43
is at the **core** of this zone.

**The defining cytoarchitectonic feature is BA 43's dual character.**
BA 43 is **not** a pure gustatory territory in the way that BA 41 is a
pure primary auditory territory or BA 17 is a pure primary visual
territory. BA 43 contains:

    anterior insular fundus           gustatory cells, receiving
                                      VPMpc input — the primary
                                      gustatory component
    postcentral opercular crown       somatosensory cells, receiving
                                      VPL/VPI input — the oral
                                      somatosensory component

The **same BA 43 territory** contains both populations, and this dual
character is the **anatomical basis for the multimodal intraoral
integration** that underlies flavour — taste plus oral somatosensory
(texture, temperature) convergence at the same cortical locus
. The classical name *subcentral area*
captures the somatosensory component; the modern gustatory literature
captures the gustatory component; **both are BA 43**.

**A crucial caveat about BA 43's gustatory purity.** As the PGC leaf
package documents, **less than 10 % of neurons in the gustatory
cortex respond to taste stimuli**; many others respond to other
intraoral stimuli . BA 43 is
**not a pure taste processor** — it is a **multimodal intraoral
cortex** in which taste is one input among many, and the taste cells
are intermingled with somatosensory, thermoreceptive, and other
non-taste cells. The gustatory literature calls BA 43 the "primary
gustatory cortex" because it is the **densest VPMpc recipient zone**
and the **first cortical stage** of the taste pathway; the
somatosensory literature calls BA 43 the "subcentral area" because it
is the **opercular continuation of the postcentral strip**. Both
descriptions are correct, and the package must carry both.

**A second crucial caveat: BA 43 is inconstant in its boundaries.**
Some parcellations treat BA 43 as a component of the postcentral gyrus
(the *opercular part of the postcentral gyrus*); others treat it as
an anterior insular territory. Modern parcellations (HCP 180-area,
Öngür-Price, Petrides-Pandya) subdivide the gustatory operculum under
different labels (HCP: ``OP4`` plus ``Ig``/``Id`` at the insular
edge; Öngür-Price: ``G`` and the adjacent granular areas;
Petrides-Pandya: ``G`` plus ``Ig``). **The package must therefore
carry an explicit ``PARCELATION_AMBIGUITY`` field** documenting that
BA 43 is simultaneously a postcentral-operculum territory and an
anterior-insula territory, and that both descriptions are correct.

**The BA 43 ↔ PGC relationship is the most consequential overlap in
the whole insular BA registry.** The PGC leaf package (under
``..insular``) describes the **functional gustatory field** — the
cortical recipient of VPMpc taste information, spanning BA 43, area G,
the frontal and parietal opercula, and (conditionally) the base of the
central sulcus. The BA 43 package describes the **architectonic
territory** at the core of that field. They are **overlap, not
nesting**:

    BA 43        = architectonic territory (this package)
    PGC          = functional gustatory field that spans BA 43 + area G
                   + opercula + (conditionally) base of central sulcus
                   + (functionally) BA 14 / BA 13 secondary territory

The PGC is **not** a parent of BA 43 and BA 43 is **not** a child of
the PGC. They are siblings under ``..insular``, and the downstream
code must query the **PGC** for functional taste processing and BA 43
for architectonic territory.

The left BA 43 borders:

    ventromedially    BA 13 (middle insula) via the granular
                      transition
    rostrally         the anterior short gyri (BA 16 / BA 14 region)
    caudally          the parietal operculum / area G (functional
                      continuation of the gustatory field; NAMING
                      COLLISION boundary for the **secondary
                      somatosensory** cortex, NOT a BA label collision)
    dorsally          the postcentral opercular crown (BA 3
                      somatosensory component of BA 43 itself —
                      dual character)
    laterally         the inferior precentral sulcus / inferior
                      frontal sulcus junction, separating BA 43 from
                      BA 44 (pars opercularis of the IFG — speech-
                      motor operculum) — **the gustatory vs speech-
                      motor boundary**

**Left-hemisphere specificity**: the left BA 43 is the hemisphere whose
gustatory territory is **dominant for taste recognition**. Left
insular damage produces an **ipsilateral deficit in taste intensity
but a bilateral deficit in taste recognition** — taste information
from both sides of the tongue passes through the left insula, and the
left BA 43 is part of the substrate for that bilateral recognition
. This is the single
sharpest asymmetry in the human gustatory system, and it has no
symmetric counterpart on the right (see the right sibling).

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours
        ventromedially         BA 13 (middle insula)
        rostrally              BA 16 / BA 14 region (anterior short
                               gyri)
        caudally               parietal operculum / area G
                               (functional continuation of the
                               gustatory field)
        dorsally               postcentral opercular crown (BA 3
                               somatosensory — dual character of
                               BA 43 itself)
        laterally              inferior precentral sulcus / inferior
                               frontal sulcus junction, separating
                               BA 43 from BA 44 (speech-motor
                               operculum — gustatory vs speech-motor
                               boundary)

    Functional overlays
        primary gustatory cortex (PGC) — OVERLAP, NOT NESTING
            BA 43 is the **architectonic core** of the PGC. The PGC
            leaf package under ``..insular`` describes the
            functional gustatory field; BA 43 describes the
            architectonic territory at its core. On the **left**,
            BA 43's gustatory contribution is weighted toward the
            **recognition / flavour-identity** aspect — the
            "what is this food?" question — and toward the
            **hedonic valuation** interface with the left PGC.
        multimodal intraoral integration (dual character)
            BA 43's dual cytoarchitectonic character — gustatory
            fundus + somatosensory opercular crown — is the
            anatomical basis for the **taste-plus-texture-plus-
            temperature** integration that underlies flavour. On
            the left, the integration is weighted toward the
            **flavour-identity / recognition** aspect; on the
            right, toward the **flavour-intensity** aspect.
        hedonic valuation interface
            BA 43 is the cortical locus where taste identity
            meets affective value. The left BA 43 → left OFC
            projection carries the hedonic value of taste to the
            secondary taste area (right-lateralized at caudolateral
            OFC — see right BA 43). On the left, the hedonic
            interface is weighted toward the
            **recognition-linked / language-adjacent** valuation
            aspect; on the right, toward the **intensity-linked**
            aspect.
        autonomic coupling (parasympathetic on the left)
            Taste stimuli drive **autonomic responses** — salivation,
            gastric acid secretion, insulin release, and vagal
            bradycardia — through BA 43's projections to the
            hypothalamus and the NST. On the **left**, the coupling
            is weighted toward **parasympathetic** outflow (vagal
            bradycardia, depressor responses, cephalic-phase
            insulin release); on the right, toward sympathetic
            (pressor, tachycardic, and the anticipatory arousal
            that accompanies food expectation).
        social-emotional (marginal)
            BA 43's contribution to the social-emotional network is
            **marginal** — it operates through the affective
            valuation of food and the commensality aspects of
            eating, not through the anterior insular hub's core
            social-emotional functions. On the left, the marginal
            contribution is weighted toward **language-linked
            food-related emotion**; on the right, toward
            **affective-salience food-related arousal**.
        gustatory-somatosensory frontier (BA 43 ↔ BA 44 boundary)
            BA 43 is at the **gustatory pole** of the operculum;
            BA 44 (pars opercularis of the IFG) is at the
            **speech-motor pole**. The two are separated by the
            inferior precentral sulcus / inferior frontal sulcus
            junction. **This is a structural boundary, not a
            naming collision** — BA 43 and BA 44 are different
            territories in the same lobe, and downstream code must
            specify which one it means when querying "opercular
            cortex."

**This field is structurally identical to the right sibling's** — the
architectonic neighbours and functional overlays are the same on both
sides. What differs is the **emphasis** within the gustatory,
multimodal, hedonic, and autonomic overlays: the left BA 43 is
weighted toward **recognition / flavour-identity / parasympathetic**
aspects; the right BA 43 is weighted toward **intensity /
flavour-intensity / sympathetic** aspects.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 13 (middle insula)                  ventromedial neighbour via
                                           the granular transition;
                                           BA 13 carries the multimodal
                                           integration signal that
                                           BA 43 differentiates into
                                           gustatory and oral
                                           somatosensory content
    BA 16 / BA 14 (anterior short gyri)    rostral neighbours; the
                                           anterior insular territory
                                           whose PGC projection is
                                           secondary rather than
                                           primary
    BA 3 (postcentral somatosensory)       dorsal neighbour — **not a
                                           distinct BA from BA 43's
                                           somatosensory component**;
                                           BA 43's postcentral
                                           opercular crown is
                                           continuous with BA 3's
                                           oral somatosensory
                                           representation
    area G / parietal operculum            caudal neighbour — the
                                           gustatory transition zone;
                                           **NAMED FUNCTIONALLY, NOT
                                           BY BA NUMBER** — there is
                                           no BA numbering collision
                                           between BA 43 and area G
    BA 44 (pars opercularis of the IFG)    lateral neighbour across
                                           the inferior precentral /
                                           inferior frontal sulcus
                                           junction — **gustatory
                                           operculum vs speech-motor
                                           operculum boundary**;
                                           downstream code must
                                           specify which opercular
                                           territory it means
    BA 41 / BA 42 (insular-opercular       distant caudal neighbours;
    transition)                            no direct adjacency —
                                           BA 13 and the agranular
                                           posterior insula intervene
    BA 42 (temporal, planum temporale)     distant neighbour across
                                           the circular sulcus —
                                           **NAMING COLLISION, but
                                           documented in the
                                           BA 41 / BA 42 packages,
                                           not here**

**This field is byte-identical to the left sibling's** at the level of
BA-numbered neighbours. The **BA 3** and **area G** entries are
notably **not** BA numbering collisions — BA 3 is the somatosensory
component of BA 43 itself, and area G is a functional designation.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 43 participates in **five** canonical insular domains on the left.
The emphasis is as follows:

    gustatory                                    (left emphasis — PRIMARY)
        **This is BA 43's defining contribution on both hemispheres,
        but the left weighting is toward recognition.** BA 43 is the
        architectonic core of the primary gustatory cortex, and the
        left BA 43 is the hemisphere whose gustatory territory
        supports **bilateral taste recognition**. Left insular
        damage produces an **ipsilateral intensity deficit but a
        bilateral recognition deficit** — taste information from
        both sides of the tongue passes through the left insula.
        The left BA 43 is weighted toward the
        **recognition / flavour-identity** aspect of taste; the
        right BA 43 is weighted toward the **intensity /
        concentration** aspect.

    multimodal_intraoral_integration                (left emphasis — PRIMARY)
        **This is BA 43's second primary contribution on the left.**
        BA 43's dual cytoarchitectonic character — gustatory fundus
        + somatosensory opercular crown — is the anatomical basis
        for the **taste-plus-texture-plus-temperature**
        integration that underlies flavour. On the left, the
        integration is weighted toward the **flavour-identity /
        recognition** aspect — the "what is this food?" question.

    hedonic_valuation_interface                    (left emphasis — SECONDARY)
        BA 43 is the cortical locus where taste identity meets
        affective value. The left BA 43 → left OFC projection
        carries the hedonic value of taste to the secondary taste
        area. On the left, the hedonic interface is weighted
        toward the **recognition-linked / language-adjacent**
        valuation aspect — the verbal evaluation of food
        pleasantness.

    autonomic_control (parasympathetic)            (left emphasis — SECONDARY)
        Taste stimuli drive **autonomic responses** — salivation,
        gastric acid secretion, insulin release, and vagal
        bradycardia — through BA 43's projections to the
        hypothalamus and the NST. On the left, the coupling is
        weighted toward **parasympathetic** outflow — vagal
        bradycardia, depressor responses, and cephalic-phase
        insulin release. The left BA 43 → hypothalamus and
        BA 43 → NST projections are part of this parasympathetic
        substrate.

    social_emotional (marginal)                    (left emphasis — MARGINAL)
        BA 43's contribution to the social-emotional network is
        **marginal** — it operates through the affective valuation
        of food and the commensality aspects of eating. On the
        left, the marginal contribution is weighted toward
        **language-linked food-related emotion** — the social and
        verbal framing of food experience.

**Left-specific caveat on `speech_articulation`.** BA 43 does **not**
carry the domain. The apraxia-of-speech territory is the **anterior
insular hub** (BA 13 / BA 16 / opercular transition), which is
**rostral** to BA 43's gustatory pole. BA 43 is at the gustatory
operculum, not the speech-motor operculum. The speech-motor
operculum is **BA 44** (pars opercularis of the IFG), which is a
different territory on the frontal side of the opercular boundary.

**Left-specific caveat on `vestibular_and_self_location`.** This
domain is **right-emphasized at BA 13**. The left BA 43 does **not**
carry it.

**Left-specific caveat on `nociception_and_pain_affect` and
`thermoreception`.** These domains belong to the **posterior**
insular territory (BA 41 / BA 42), not to BA 43. BA 43's chemosensory
territory is gustatory and oral somatosensory, not nociceptive or
thermoreceptive. It is worth noting that BA 43 **does** participate
in oral **thermal** sensation — the temperature of food is part of
the multimodal intraoral integration — but this is a **somatosensory**
thermal signal, not a **primary thermoreceptive** one. It belongs
to `multimodal_intraoral_integration`, not to a distinct
`thermoreception` domain.

**Left-specific caveat on `interoception`.** BA 43's interoceptive
contribution is **marginal** — it participates in the visceral
responses to food (cephalic-phase insulin release, gastric acid
secretion) through its autonomic projections, but the primary
interoceptive territory is the **posterior insula** (BA 13 / BA 41 /
BA 42). `interoception` is **omitted** from the left BA 43
`FUNCTIONAL_DOMAINS` tuple; the autonomic coupling that BA 43
contributes is captured under `autonomic_control`.

**Left-specific caveat on `salience_network`.** This domain is the
**anterior insular hub** — BA 16 / BA 14 territory, not BA 43. BA 43
is at the gustatory pole, not the salience pole. `salience_network` is
**omitted** from the left BA 43 `FUNCTIONAL_DOMAINS` tuple.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → VPMpc (parvicellular ventroposteromedial nucleus)
            **BA 43's primary thalamic afferent.** The VPMpc relays
            gustatory input from the rostral NST (directly in
            primates, via the parabrachial nucleus in rodents) to
            the anterior insula. BA 43 is at the **core** of the
            VPMpc projection zone . This is
            the anatomical substrate of BA 43's primary gustatory
            role.
        → VPL / VPI (ventroposterior lateral / inferior)
            Somatosensory thalamic nuclei with a projection to the
            **postcentral opercular crown** of BA 43's territory —
            the oral somatosensory component of BA 43's dual
            character. This is the anatomical substrate of the
            multimodal intraoral integration.

    cortical afferents
        → BA 13 (middle insula), left
            The granular transition from BA 13 to the anterior
            insula projects into BA 43's territory, carrying the
            multimodal integration signal that BA 43 differentiates
            into gustatory and oral somatosensory content.
        → BA 3 (postcentral somatosensory), left
            BA 43's postcentral opercular crown is **continuous**
            with BA 3's oral somatosensory representation. The
            BA 3 → BA 43 projection carries the texture and
            temperature content that BA 43 integrates with taste.
        → primary gustatory cortex (PGC), left
            **The BA 43 ↔ PGC relationship is overlap, not
            nesting.** BA 43 is the architectonic core of the PGC;
            the PGC is the functional gustatory field that spans
            BA 43 + area G + opercula + (conditionally) base of
            central sulcus. The PGC → BA 43 projection (via
            intrainsular connections) represents the functional-
            field context that BA 43 operates within.
        → anterior insula (via intrainsular connections)
            BA 43 projects rostrally to the anterior insular hub,
            carrying the gustatory signal that the hub transforms
            into the full salience and affective response.

    subcortical efferents
        → orbitofrontal cortex (OFC), left
            **BA 43 → OFC is the principal secondary-taste
            pathway.** The left BA 43 projects ipsilaterally to
            the left OFC, carrying the hedonic value of taste.
            The OFC's caudolateral secondary-taste territory is
            right-lateralized in humans (see right BA 43), but the
            left BA 43 → left OFC projection exists and carries
            the **recognition-linked** hedonic content on the
            left.
        → hypothalamus (lateral hypothalamus), left
            **BA 43 → LH is part of the parasympathetic efferent
            pathway.** On the left, this projection is weighted
            toward parasympathetic outflow (cephalic-phase insulin
            release, gastric acid secretion, and vagal bradycardia
            during food anticipation and consumption).
        → nucleus of the solitary tract (NST), left
            BA 43 projects to the NST, the brainstem relay for
            gustatory and visceral afferents and the origin of
            vagal parasympathetic outflow.
        → amygdala (basolateral nuclei), left
            Reciprocal connections support the **affective
            valuation** of taste and the **conditioned taste
            aversion** memory. On the left, the BA 43 → amygdala
            projection is weighted toward the
            **recognition-linked / language-adjacent** affective
            content; on the right, toward the **intensity-linked /
            arousal** content.
        → ventral striatum / nucleus accumbens
            The BA 43 → OFC → ventral striatum pathway supports the
            **reward value** of taste and the **ingestive
            decision-making** that follows taste recognition.

    brainstem interactions
        → parabrachial nucleus (indirect via VPMpc)
            The parabrachial → VPMpc → BA 43 pathway is the
            anatomical substrate of the primary gustatory relay.
        → dorsal motor nucleus of the vagus (DMV)
            BA 43 → hypothalamus → DMV projections support the
            **cephalic-phase** autonomic responses to food
            anticipation and consumption.

    callosal connections
        → right BA 43
            Interhemispheric coordination of the gustatory operculum.
            The left → right traffic carries the **recognition-
            linked** taste signal (the left hemisphere's dominant
            contribution to bilateral taste recognition) and
            **parasympathetic** autonomic signals; the right →
            left traffic carries **intensity-linked** taste signals
            and **sympathetic** autonomic signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in three respects:
(a) the VPMpc → BA 43 pathway carries gustatory signals that the
left uses for **recognition** — the bilateral taste-recognition
effect;
(b) the BA 43 → hypothalamus, BA 43 → NST, and BA 43 → DMV
projections are **parasympathetic** rather than sympathetic;
(c) the BA 43 → OFC projection carries **recognition-linked**
hedonic content, and the callosal traffic carries recognition-linked
and parasympathetic signals.

**Note: BA 43 has no MGB guard.** Unlike the BA 41 and BA 42 packages,
BA 43 has **no naming collision with any temporal-lobe territory**.
The medial geniculate body (MGB) does **not** project to BA 43 — the
gustatory thalamic relay is VPMpc, and the auditory thalamic relay is
MGB projecting to the **temporal** BA 41 / BA 42. There is no
`MGB_AFFERENT_GUARD` field in this package.

**Note: BA 43 has no S2 continuity note.** Unlike the BA 42 package,
BA 43 has **no opercular S2 functional-continuity note in the same
sense** — S2 is adjacent to the **parietal** operculum, which is
**caudal** to BA 43's gustatory pole. There is a **BA 43 ↔ BA 3**
structural continuity (the oral somatosensory component of BA 43
itself), but this is a component-level continuity, not an inter-package
S2-style boundary. There is no `S2_FUNCTIONAL_CONTINUITY_NOTE` field
in this package.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_ba43_bilateral_taste_recognition
        **This is the left BA 43 anchor par excellence.** Left
        insular damage produces an **ipsilateral intensity deficit
        but a bilateral recognition deficit** — taste information
        from both sides of the tongue passes through the left
        insula, and the left BA 43 is part of the substrate for
        that bilateral recognition . The
        left BA 43 is the hemisphere whose gustatory territory is
        **dominant for taste recognition**; the right BA 43 is
        weighted toward intensity / concentration. Any downstream
        code that computes a "taste recognition score" must
        weight the left BA 43 more heavily and must not average
        left and right — averaging would erase the lateralized
        signal.

    left_ba43_hedonic_valuation_of_food
        Left BA 43's hedonic interface with the left PGC supports
        the **recognition-linked / language-adjacent** evaluation
        of food pleasantness. Left BA 43 lesions can produce
        **altered taste pleasantness** — foods that were previously
        liked may become indifferent, or the patient may find it
        difficult to name and describe food pleasantness — distinct
        from the right BA 43's intensity-linked hedonic
        contribution.

    left_ba43_flavour_identity_deficit
        BA 43's dual character — gustatory fundus + somatosensory
        opercular crown — supports the **flavour-identity**
        integration (taste + texture + temperature → "what is this
        food?"). Left BA 43 lesions can produce **flavour-
        identification deficits** — the patient can detect sweet
        and salty but cannot identify the food from its combined
        sensory pattern. This is a **left-weighted** anchor: the
        right BA 43's chemosensory contribution is more weighted
        toward **flavour intensity**.

    left_ba43_parasympathetic_autonomic_coupling
        Left BA 43's gustatory activity drives **parasympathetic**
        autonomic responses — salivation, gastric acid secretion,
        cephalic-phase insulin release, and vagal bradycardia
        during food anticipation and consumption. Left BA 43
        lesions can produce **parasympathetic dysregulation** in
        these responses, distinct from the right BA 43's
        sympathetic signature (pressor, tachycardic, anticipatory
        arousal).

    gustatory_hallucination_and_insular_lesions
        **Gustatory hallucinations** — the phantom perception of
        taste — are a recognized symptom of **insular lesions**
        involving the gustatory cortex. Left BA 43 / PGC lesions
        can produce gustatory hallucinations, and the gustatory
        cortex is the cortical substrate of these hallucinations.

    gustatory_aura_in_temporal_lobe_epilepsy
        **Gustatory auras** — brief, stereotyped taste sensations
        preceding a seizure — are a classic symptom of **temporal
        lobe epilepsy** and are attributed to the spread of
        epileptiform activity to the insular gustatory cortex.
        The left BA 43 / PGC is the cortical substrate of these
        auras, and the left temporal lobe is the more common
        seizure-onset zone for gustatory auras.

    eating_reflex_seizures
        **Eating-reflex seizures** — seizures triggered by food or
        syrup intake — can arise from the gustatory cortex. The
        middle short gyrus of the insula (BA 13 territory, more
        rostral than BA 43) has been the resection target for
        these seizures, but the broader gustatory network includes
        BA 43. On the left, the eating-reflex seizure semiology is
        weighted toward the **gustatory / language-linked**
        aspects (the patient may describe a specific taste
        trigger); on the right, toward the **affective / arousal**
        aspects.

    conditioned_taste_aversion_therapy
        BA 43 / PGC's role in **CTA memory** has clinical
        implications for **aversion therapy** (e.g., in alcohol
        use disorder) and for understanding **taste aversions**
        that develop during chemotherapy or radiation therapy.
        The left BA 43 is the hemisphere whose gustatory territory
        supports the **recognition-linked** CTA memory; the right
        BA 43 supports the **intensity-linked / autonomic** CTA
        memory. The combined left-right gustatory system is the
        cortical substrate of CTA.

    left_insular_glioma_resection_taste_mapping
        Because BA 43 is a **buried transition territory** at the
        gustatory pole of the operculum, resecting a left insular
        / opercular glioma in the BA 43 zone requires careful
        mapping of taste, autonomic, and oral somatosensory
        function. **Awake surgery with direct electrical
        stimulation** is the standard approach for identifying
        and preserving the gustatory cortex. Left BA 43
        resections risk **bilateral taste-recognition deficits**,
        **flavour-identity deficits**, and **parasympathetic
        dysregulation** — distinct from the risks of anterior
        short gyri resections (apraxia of speech) and posterior
        insula resections (primary interoceptive / pain deficits).

    gustatory_operculum_vs_speech_motor_operculum_hazard
        **The BA 43 ↔ BA 44 boundary is a surgical hazard.**
        BA 43 (gustatory operculum) is separated from BA 44
        (pars opercularis of the IFG — speech-motor operculum) by
        the inferior precentral sulcus / inferior frontal sulcus
        junction. Downstream code that queries "opercular cortex"
        must specify which BA it means, and pre-surgical workup
        must distinguish the gustatory from the speech-motor
        operculum. This is a **structural hazard, not a naming
        collision** — BA 43 and BA 44 are different territories
        in the same lobe.

    left_insular_stroke_taste_dysfunction
        Left insular strokes — including those involving BA 43 —
        produce an **ipsilateral intensity deficit but a bilateral
        recognition deficit**. Taste dysfunction is significantly
        associated with **insula involvement** (OR = 3.5) and with
        **left hemisphere lesion** (OR = 2.4) in acute and
        chronic stroke patients. The left BA 43 is the
        gustatory architectonic territory whose lesion produces
        the recognition component of this deficit pattern.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 43 is the hemisphere whose gustatory territory is
**dominant for taste recognition**, and left insular damage produces
a **bilateral** recognition deficit; (b) the left BA 43's gustatory
and autonomic contributions are weighted toward the **recognition /
flavour-identity / parasympathetic** aspect (right is intensity /
flavour-intensity / sympathetic). The right sibling's docstring
carries the corresponding right-sided anchors.

**The BA 43 ↔ PGC relationship and the BA 43 ↔ BA 44 boundary hazard
are hemisphere-invariant** — they are documented identically in both
packages.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left insular BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 43 (which on
    the left is ``("gustatory",
    "multimodal_intraoral_integration",
    "hedonic_valuation_interface")``), and enforcer of the
    ``speech_articulation`` exclusion.

..brodmann_area_13_middle_insula
    Ventromedial neighbour via the granular transition. BA 13's
    multimodal integration signal is differentiated by BA 43 into
    gustatory and oral somatosensory content.

..brodmann_area_14
    Rostral / anterior short gyri neighbour. BA 14's
    olfactory-gustatory contribution is functionally continuous
    with BA 43's gustatory territory.

..brodmann_area_16
    Rostral / anterior short gyri neighbour. **BA 16's primary
    peak is `vestibular_and_self_location` in the parent registry,
    not gustatory**, and BA 43's gustatory territory is distinct.

..brodmann_area_41_posterior_insula
    Distant caudal neighbour — no direct adjacency (BA 13 and the
    agranular posterior insula intervene). BA 41 is the
    nociceptive / thermoreceptive transition territory; BA 43 is
    the gustatory territory. **Different functional territories
    within the insular lobe.**

..brodmann_area_42_posterior_insula
    Distant caudal neighbour — no direct adjacency. BA 42 is the
    multimodal opercular convergence territory; BA 43 is the
    gustatory operculum. **Different functional territories
    within the insular lobe.**

...primary_gustatory_cortex
    The **functional-field sibling** (one level up, under
    ``..insular``). **The BA 43 ↔ PGC relationship is overlap, not
    nesting.** BA 43 is the architectonic territory; PGC is the
    functional gustatory field that spans BA 43 + area G +
    opercula + (conditionally) base of central sulcus. The two
    packages must be created / updated together, and the PGC
    package's `BRODMANN_AREAS` field must reference BA 43.

..cortex.frontal.brodmann_areas.brodmann_area_44
    **The speech-motor operculum, NOT the gustatory operculum.**
    BA 44 (pars opercularis of the IFG) is separated from BA 43 by
    the inferior precentral sulcus / inferior frontal sulcus
    junction. **Downstream code must specify which BA it means
    when querying "opercular cortex."** This is a **structural
    boundary, not a naming collision** — BA 43 and BA 44 are
    different territories in the same lobe.

..cortex.frontal
    The frontal operculum (including BA 44) is adjacent to BA 43
    across the opercular boundary. The frontal package must
    declare the insula as a hidden neighbour, must note the
    **BA 43 ↔ BA 44 gustatory vs speech-motor boundary**, and
    must not conflate the two opercular territories.

..cortex.parietal
    The parietal operculum (area G) is adjacent to BA 43's
    caudal margin. **Area G is named functionally, not by BA
    number** — there is no BA numbering collision between BA 43
    and area G. The parietal package must declare the insula as a
    hidden neighbour and must note the area G gustatory
    transition.

..cortex.temporal
    The temporal operculum is separated from BA 43 by the more
    caudal insular territory. BA 43 has no temporal-lobe naming
    collision — **there is no MGB guard for BA 43** (see the
    CONNECTIVITY section).

..cortex.cingulate
    The dorsal anterior cingulate is the salience-network partner
    of the anterior insula. BA 43's contribution to the salience
    network is **marginal** — it operates through the affective
    valuation of food, not through the anterior insular hub's
    core salience functions. The cingulate package must declare
    the anterior insula as its salience-network partner.

../../subcortical/diencephalon/thalamus
    The **VPMpc** thalamic nucleus is BA 43's primary afferent
    (gustatory). The thalamus package must declare VPMpc as a
    cortical afferent to the left BA 43, and must **not** declare
    the medial geniculate body (MGB) as an afferent to BA 43 —
    MGB projects to the temporal BA 41 / BA 42, not to BA 43.

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem relay that feeds
    VPMpc and thus BA 43.

../../brainparts/hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
    The **nucleus of the solitary tract (NST)** is the brainstem
    gustatory relay that feeds VPMpc and thus BA 43. The NST
    package must declare BA 43 as a cortical target (via the
    VPMpc relay).

../../subcortical/diencephalon/hypothalamus
    The left BA 43 → left hypothalamus projection supports
    **parasympathetic** autonomic coupling to food anticipation
    and consumption. The hypothalamus package must declare the
    left BA 43 as a cortical afferent.

../../subcortical/medial_temporal_lobe/amygdala
    The left basolateral amygdala receives BA 43 projections
    supporting the **affective valuation** of taste and the
    **conditioned taste aversion** memory. The amygdala package
    must declare the left BA 43 as a cortical afferent.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The BA 43 → OFC → ventral striatum pathway supports the
    **reward value** of taste and **ingestive decision-making**.

../../right/cortex/insular/brodmann_areas/brodmann_area_43_anterior_insula
    The right-hemisphere homologue. Structural fields (BA number,
    region label, **dual cytoarchitectonic character**,
    **PARCELATION_AMBIGUITY field**, **BA 43 ↔ PGC overlap
    relationship**, **BA 43 ↔ BA 44 boundary**, architectonic
    neighbourhoods, BA-to-neighbour adjacency,
    FUNCTIONAL_DOMAINS set) MUST be byte-identical. Functional
    emphasis and clinical significance diverge — the left BA 43
    is weighted toward taste recognition, flavour identity,
    hedonic valuation / language-adjacent, parasympathetic
    autonomic control, and bilateral taste-recognition deficit;
    the right BA 43 is weighted toward taste intensity, flavour
    intensity, intensity-linked hedonic valuation, sympathetic
    autonomic control, and ipsilateral taste-intensity deficit.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_43_anterior_insula"
    HEMISPHERE          = "left"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 43
    INSULAR_REGION      = "anterior_opercular"
    CYTOTECTONIC_GRADIENT = "agranular_to_dysgranular"
    ALTERNATE_NAMES     = ("subcentral_area",
                           "opercular_part_of_postcentral_gyrus")

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** BA 43 is unique to this region —
        # it does not collide with any temporal-lobe or
        # frontal-lobe BA label. Unlike BA 41 and BA 42, there is
        # no MGB guard, no parcellation convention for the BA
        # number, and no circular-sulcus boundary at a naming
        # level. The BA 43 ↔ BA 44 boundary is a **structural**
        # boundary (gustatory vs speech-motor operculum), not a
        # naming collision, and it is documented separately in
        # the CROSS-REFERENCES.

    PARCELATION_AMBIGUITY = (
        "BA 43 (Brodmann's subcentral area) is simultaneously "
        "described as a postcentral-operculum territory and as an "
        "anterior-insula territory. Both descriptions are correct: "
        "BA 43 contains an anterior insular gustatory fundus and a "
        "postcentral opercular somatosensory crown. Modern "
        "parcellations (HCP 180-area, Ongur-Price, Petrides-"
        "Pandya) subdivide the territory under labels like OP4, "
        "G, Ig, and Id, and do not preserve BA 43 as a single "
        "discrete entity. The BA 43 label is a tree-architecture "
        "convention for the gustatory opercular transition, and "
        "downstream code must not treat 'BA 43' as a stand-alone "
        "modern parcel."
    )
        # **Byte-identical to the right sibling's.** Documents
        # that BA 43 is simultaneously postcentral and insular.

    DUAL_CYTOARCHITECTONIC_CHARACTER = (
        "BA 43 has a dual cytoarchitectonic character: gustatory "
        "fundus (VPMpc-recipient, primary taste) plus postcentral "
        "opercular crown (VPL/VPI-recipient, oral somatosensory). "
        "The two components are anatomically continuous within "
        "BA 43 and are the substrate of multimodal intraoral "
        "integration (taste + texture + temperature → flavour). "
        "Downstream code that queries 'BA 43' must be prepared "
        "for the dual character — there is no pure-gustatory "
        "sub-territory that can be cleanly separated."
    )
        # **Byte-identical to the right sibling's.**

    BA44_OPERClULAR_BOUNDARY_GUARD = (
        "BA 43 (gustatory operculum) is separated from BA 44 "
        "(pars opercularis of the IFG — speech-motor operculum) by "
        "the inferior precentral sulcus / inferior frontal sulcus "
        "junction. Downstream code that queries 'opercular cortex' "
        "must specify which BA it means. This is a structural "
        "boundary, not a naming collision. BA 44 is under "
        "cortex/frontal, not cortex/insular."
    )
        # **Byte-identical to the right sibling's.**

    PGC_OVERLAP_RELATIONSHIP = (
        "The BA 43 ↔ PGC relationship is overlap, not nesting. "
        "BA 43 is the architectonic territory. The primary "
        "gustatory cortex (PGC, under ..insular) is the functional "
        "gustatory field that spans BA 43 + area G + opercula + "
        "(conditionally) base of central sulcus. The PGC package's "
        "BRODMANN_AREAS field must reference BA 43. Neither is a "
        "child of the other."
    )
        # **Byte-identical to the right sibling's.**

    FUNCTIONAL_DOMAINS  = (
                              "gustatory",             # PRIMARY
                              "multimodal_intraoral_integration",
                                                       # PRIMARY
                              "hedonic_valuation_interface",
                              "autonomic_control",     # left:
                                                       # parasympathetic
                              "social_emotional",      # marginal
                              # NOTE: speech_articulation is
                              # EXCLUDED (BA 43 is at the
                              # gustatory pole, not the speech-
                              # motor pole; the apraxia-of-speech
                              # territory is the anterior
                              # insular hub — BA 13 / BA 16 /
                              # opercular transition).
                              # NOTE: vestibular_and_self_
                              # location is EXCLUDED (right-
                              # emphasized at BA 13).
                              # NOTE: nociception_and_pain_affect
                              # and thermoreception are EXCLUDED
                              # (BA 41 / BA 42 territory; BA 43's
                              # oral thermal contribution is
                              # captured under multimodal_intraoral
                              # _integration as somatosensory,
                              # not as primary thermoreception).
                              # NOTE: interoception is EXCLUDED
                              # (BA 13 / BA 41 / BA 42 territory;
                              # BA 43's marginal visceral
                              # contribution is captured under
                              # autonomic_control).
                              # NOTE: salience_network is
                              # EXCLUDED (BA 16 / BA 14
                              # territory; BA 43 is at the
                              # gustatory pole, not the salience
                              # pole).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "gustatory":
                                  "taste_recognition_flavour_"
                                  "identity_bilateral_recognition_"
                                  "dominant",
                              "multimodal_intraoral_integration":
                                  "flavour_identity_recognition_"
                                  "language_linked",
                              "hedonic_valuation_interface":
                                  "recognition_linked_language_"
                                  "adjacent_hedonic_evaluation",
                              "autonomic_control":
                                  "parasympathetic_vagal_"
                                  "bradycardia_cephalic_phase_"
                                  "insulin_secretion",
                              "social_emotional":
                                  "language_linked_food_related_"
                                  "emotion_marginal",
                          }

    MODERN_CROSSWALK    = {   # BA 43 → modern parcellation labels
                              "HCP_180":       ("OP4", "Ig", "Id"),
                              "Ongur_Price_2000": ("G", "Iai", "Ial"),
                              "Petrides_Pandya":  ("G", "Ig", "Id"),
                          }
        # **Byte-identical to the right sibling's.**

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_ba43_bilateral_taste_"
                              "recognition",
                              "left_ba43_hedonic_valuation_of_"
                              "food",
                              "left_ba43_flavour_identity_deficit",
                              "left_ba43_parasympathetic_"
                              "autonomic_coupling",
                              "gustatory_hallucination_and_"
                              "insular_lesions",
                              "gustatory_aura_in_temporal_lobe_"
                              "epilepsy",
                              "eating_reflex_seizures",
                              "conditioned_taste_aversion_"
                              "therapy",
                              "left_insular_glioma_resection_"
                              "taste_mapping",
                              "gustatory_operculum_vs_speech_"
                              "motor_operculum_hazard",
                              "left_insular_stroke_taste_"
                              "dysfunction",
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
        "NAMING_COLLISION_WITH",
        "PARCELATION_AMBIGUITY",
        "DUAL_CYTOARCHITECTONIC_CHARACTER",
        "BA44_OPERClULAR_BOUNDARY_GUARD",
        "PGC_OVERLAP_RELATIONSHIP",
        "FUNCTIONAL_DOMAINS",
        "DOMAIN_EMPHASIS",
        "MODERN_CROSSWALK",
        "CONNECTIVITY",
        "CLINICAL_ANCHORS",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references BA 43 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are no forward-declaration caveats for this package.** BA 43 is
a sibling of BA 13, BA 14, BA 16, BA 41, and BA 42 under
``..brodmann_areas``. Its functional-field sibling ``...
primary_gustatory_cortex`` exists under ``..insular``. Its cortical
and subcortical targets exist or are being built out in parallel. The
BA 44 neighbour is a real package under ``cortex/frontal`` (not a
forward reference). BA 3 is a real package under ``cortex/frontal``
(the precentral gyrus) and its postcentral continuation — no forward
reference is needed for the BA 43 ↔ BA 3 structural continuity.

**The BA 43 ↔ PGC relationship is a required cross-package reference,
not a forward reference.** The PGC leaf package under ``..insular``
must declare BA 43 in its ``CORTICAL_TERRITORIES`` and its
``BRODMANN_AREAS``. Both packages must be created / updated in the
same commit — the BA 43 ↔ PGC overlap must not be left half-declared.

**The BA 44 cross-package reference is a structural boundary, not a
forward reference.** BA 44 is a real package under
``cortex/frontal/brodmann_areas/``, and the BA 43 ↔ BA 44 boundary is
documented in both packages as a structural boundary (gustatory vs
speech-motor operculum), not a naming collision.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 43 is **dual-character** (gustatory + somatosensory) and its
postcentral component is sometimes treated as part of the postcentral
gyrus. If a future parcellation decides to split BA 43 into its
**gustatory** and **somatosensory** components, the promotion takes
this form:

    brodmann_area_43_anterior_insula/
        __init__.py
        gustatory_component/
            __init__.py
        somatosensory_component/
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The gustatory component must remain the PGC's architectonic core.**
Any split must preserve the PGC's ``BRODMANN_AREAS`` reference to the
gustatory component. The PGC's `CORTICAL_TERRITORIES` field must be
updated to reference the gustatory component rather than the parent
BA 43, in the same commit.

**The somatosensory component must NOT be merged with BA 3.** BA 3
(postcentral somatosensory) is a different BA territory. The
somatosensory component of BA 43 is the **opercular** continuation of
BA 3, not a replacement for it. The two are continuous but distinct.

**No split should be performed while the PGC sibling's
`CORTICAL_TERRITORIES` still references BA 43 as a single unit.** The
BA 43 ↔ PGC overlap is the primary structural relationship of this
package, and a split would require a joint revision of the BA 43
package and the PGC package in the same commit, in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_43_anterior_insula``:

    MUST be identical (byte-for-byte):
        AREA_NAME                          "brodmann_area_43_anterior_insula"
        LOBE                               "insular"
        BRODMANN_NUMBER                    43
        INSULAR_REGION                     "anterior_opercular"
        CYTOTECTONIC_GRADIENT              "agranular_to_dysgranular"
        ALTERNATE_NAMES                    ("subcentral_area",
                                           "opercular_part_of_
                                           postcentral_gyrus")
        NAMING_COLLISION_WITH              () — empty on both sides
        PARCELATION_AMBIGUITY              byte-identical
        DUAL_CYTOARCHITECTONIC_CHARACTER   byte-identical
        BA44_OPERClULAR_BOUNDARY_GUARD     byte-identical
        PGC_OVERLAP_RELATIONSHIP           byte-identical
        Architectonic neighbourhoods
        BA-to-neighbour adjacency
        MODERN_CROSSWALK                   byte-identical
        FUNCTIONAL_DOMAINS set             the same five domains,
                                           with the same exclusions
        SUBDIVISIONS                       both empty (or both
                                           non-empty in the same way,
                                           if a split is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        DOMAIN_EMPHASIS        left: gustatory is "taste_recognition_
                               flavour_identity_bilateral_
                               recognition_dominant"; multimodal_
                               intraoral_integration is "flavour_
                               identity_recognition_language_
                               linked"; hedonic_valuation_interface
                               is "recognition_linked_language_
                               adjacent_hedonic_evaluation";
                               autonomic_control is "parasympathetic_
                               vagal_bradycardia_cephalic_phase_
                               insulin_secretion"; social_emotional
                               is "language_linked_food_related_
                               emotion_marginal".
                               right: gustatory is "taste_intensity_
                               concentration_ipsilateral_dominant";
                               multimodal_intraoral_integration is
                               "flavour_intensity_arousal_linked";
                               hedonic_valuation_interface is
                               "intensity_linked_arousal_hedonic_
                               evaluation"; autonomic_control is
                               "sympathetic_pressor_tachycardic_
                               anticipatory_food_arousal";
                               social_emotional is "affective_
                               salience_food_related_emotion_
                               marginal".
        CONNECTIVITY           same bundle names; left: VPMpc → BA 43
                               is weighted toward bilateral
                               recognition; BA 43 → hypothalamus /
                               NST is parasympathetic; BA 43 → OFC
                               carries recognition-linked hedonic
                               content; callosal traffic carries
                               recognition-linked and
                               parasympathetic signals.
                               right: VPMpc → BA 43 is weighted
                               toward intensity / concentration;
                               BA 43 → hypothalamus / NST is
                               sympathetic; BA 43 → OFC carries
                               intensity-linked hedonic content;
                               callosal traffic carries intensity-
                               linked and sympathetic signals.
        CLINICAL_ANCHORS       left: eleven anchors (bilateral taste
                               recognition, hedonic valuation of
                               food, flavour identity deficit,
                               parasympathetic coupling, gustatory
                               hallucinations, gustatory auras,
                               eating-reflex seizures, CTA
                               therapy, glioma taste-mapping,
                               gustatory vs speech-motor
                               operculum hazard, insular stroke
                               taste dysfunction).
                               right: sees right sibling for the
                               right-specific anchors (ipsilateral
                               taste-intensity deficit, intensity-
                               linked hedonic valuation,
                               flavour-intensity deficit,
                               sympathetic coupling, and the
                               right-only anchors documented
                               there).

**The `DOMAIN_EMPHASIS` asymmetry is the sharpest single entry in this
contract.** Both hemispheres carry the same five domains and both
exclude the same four, but the emphasis within every shared domain
points in opposite directions: the left BA 43 is the
**recognition / flavour-identity / parasympathetic** territory, the
right BA 43 is the **intensity / flavour-intensity / sympathetic**
territory.

**The bilateral taste-recognition asymmetry is the second sharpest
entry.** Left insular damage produces a **bilateral** taste-recognition
deficit (the left hemisphere is dominant for recognition); right
insular damage produces an **ipsilateral** taste-intensity deficit (the
right hemisphere is dominant for intensity). This is the cleanest
double dissociation in the human gustatory system, and it must not be
averaged.

**The structural fields — `PARCELATION_AMBIGUITY`,
`DUAL_CYTOARCHITECTONIC_CHARACTER`, `BA44_OPERClULAR_BOUNDARY_GUARD`,
`PGC_OVERLAP_RELATIONSHIP` — are byte-identical on both sides** and
must not be allowed to drift. They are properties of the BA 43
territory itself, not of the hemisphere.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_43_anterior_insula".
[ ] HEMISPHERE is "left".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 43.
[ ] INSULAR_REGION is "anterior_opercular".
[ ] CYTOTECTONIC_GRADIENT is "agranular_to_dysgranular".
[ ] ALTERNATE_NAMES includes "subcentral_area" and
    "opercular_part_of_postcentral_gyrus".
[ ] **NAMING_COLLISION_WITH** is an empty tuple — BA 43 has **no**
    naming collision with any temporal or frontal BA. Unlike BA 41
    and BA 42, there is no MGB guard and no circular-sulcus
    naming-collision boundary.
[ ] **PARCELATION_AMBIGUITY** is present and byte-identical to the
    right sibling's — BA 43 is simultaneously postcentral and
    insular, and modern parcellations subdivide it under different
    labels.
[ ] **DUAL_CYTOARCHITECTONIC_CHARACTER** is present and
    byte-identical to the right sibling's — gustatory fundus +
    postcentral opercular crown, with taste cells intermingled
    with somatosensory cells.
[ ] **BA44_OPERClULAR_BOUNDARY_GUARD** is present and
    byte-identical to the right sibling's — the BA 43 ↔ BA 44
    boundary is a structural boundary, not a naming collision.
[ ] **PGC_OVERLAP_RELATIONSHIP** is present and byte-identical to
    the right sibling's — BA 43 is the architectonic territory;
    PGC is the functional gustatory field; overlap, not nesting.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - gustatory (PRIMARY)
    - multimodal_intraoral_integration (PRIMARY)
    - hedonic_valuation_interface
    - autonomic_control
    - social_emotional (marginal)
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation (BA 43 is
    at the gustatory pole, not the speech-motor pole; the
    apraxia-of-speech territory is BA 13 / BA 16 / opercular
    transition).
[ ] FUNCTIONAL_DOMAINS **excludes** vestibular_and_self_location
    (right-emphasized at BA 13, not BA 43).
[ ] FUNCTIONAL_DOMAINS **excludes** nociception_and_pain_affect and
    thermoreception (BA 41 / BA 42 territory; BA 43's oral
    thermal contribution is under multimodal_intraoral_
    integration).
[ ] FUNCTIONAL_DOMAINS **excludes** interoception (BA 13 / BA 41 /
    BA 42 territory; BA 43's marginal visceral contribution is
    under autonomic_control).
[ ] FUNCTIONAL_DOMAINS **excludes** salience_network (BA 16 / BA 14
    territory; BA 43 is at the gustatory pole).
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis** per domain:
    - gustatory → taste_recognition_flavour_identity_bilateral_
      recognition_dominant
    - multimodal_intraoral_integration → flavour_identity_
      recognition_language_linked
    - hedonic_valuation_interface → recognition_linked_language_
      adjacent_hedonic_evaluation
    - autonomic_control → parasympathetic_vagal_bradycardia_
      cephalic_phase_insulin_secretion
    - social_emotional → language_linked_food_related_emotion_
      marginal
[ ] MODERN_CROSSWALK is present, byte-identical to the right
    sibling's, and documents that the gustatory operculum is
    captured by modern labels like OP4, G, Ig, and Id.
[ ] CONNECTIVITY documents:
    - VPMpc thalamic afferent (primary, gustatory)
    - VPL / VPI thalamic afferent (postcentral opercular crown —
      the somatosensory component of BA 43's dual character)
    - BA 13 granular-transition afferent
    - BA 3 postcentral somatosensory afferent (the BA 43 ↔ BA 3
      oral somatosensory continuity)
    - **PGC → BA 43 overlap afferent** (the PGC is the functional
      field context that BA 43 operates within)
    - BA 43 → anterior insula intrainsular afferent
    - BA 43 → left OFC secondary-taste pathway (recognition-
      linked hedonic content on the left)
    - BA 43 → hypothalamus (parasympathetic, left-specific)
    - BA 43 → NST (parasympathetic, left-specific)
    - BA 43 → amygdala (affective valuation / CTA)
    - BA 43 → ventral striatum (reward value / ingestive
      decision-making)
    - **parabrachial → VPMpc → BA 43** (the gustatory brainstem
      relay)
    - **BA 43 → hypothalamus → DMV** (cephalic-phase autonomic
      response)
    - callosal traffic to right BA 43 (recognition-linked and
      parasympathetic, left-specific)
[ ] CLINICAL_ANCHORS contains the eleven left-specific anchors:
    - left_ba43_bilateral_taste_recognition
    - left_ba43_hedonic_valuation_of_food
    - left_ba43_flavour_identity_deficit
    - left_ba43_parasympathetic_autonomic_coupling
    - gustatory_hallucination_and_insular_lesions
    - gustatory_aura_in_temporal_lobe_epilepsy
    - eating_reflex_seizures
    - conditioned_taste_aversion_therapy
    - left_insular_glioma_resection_taste_mapping
    - gustatory_operculum_vs_speech_motor_operculum_hazard
    - left_insular_stroke_taste_dysfunction
[ ] The **bilateral taste-recognition deficit** from left insular
    damage is documented as the primary left BA 43 anchor — the
    left hemisphere is dominant for recognition, and downstream
    code must weight the left BA 43 more heavily for recognition
    and must not average left and right.
[ ] The **hedonic valuation of food** is documented as a left-
    weighted anchor — the recognition-linked / language-adjacent
    evaluation of food pleasantness.
[ ] The **flavour-identity deficit** is documented as a left-
    weighted anchor — the inability to identify food from its
    combined sensory pattern.
[ ] The **parasympathetic autonomic coupling** is documented as a
    left-weighted anchor — salivation, gastric acid secretion,
    cephalic-phase insulin release, and vagal bradycardia during
    food anticipation and consumption.
[ ] The **BA 43 ↔ BA 44 boundary hazard** is documented as a
    **surgical hazard** — the surgeon must not confuse the
    gustatory operculum with the speech-motor operculum. This is
    a structural boundary, not a naming collision, and the
    BA44_OPERClULAR_BOUNDARY_GUARD field must be present and
    byte-identical to the right sibling's.
[ ] The **BA 43 ↔ PGC overlap** is documented in the
    PGC_OVERLAP_RELATIONSHIP field, which must be present and
    byte-identical to the right sibling's. The PGC leaf package
    must reference BA 43 in its CORTICAL_TERRITORIES and
    BRODMANN_AREAS.
[ ] The **BA 43 ≠ BA 44** distinction is documented — the gustatory
    operculum (BA 43) vs the speech-motor operculum (BA 44),
    separated by the inferior precentral / inferior frontal
    sulcus junction.
[ ] The **BA 43 ≠ BA 13 / BA 14 / BA 16 / BA 41 / BA 42**
    distinction is documented — BA 43 is the gustatory pole,
    distinct from the multimodal (BA 13), olfactory-gustatory
    (BA 14), salience (BA 16), and nociceptive/thermoreceptive/
    opercular (BA 41 / BA 42) poles.
[ ] The **no-MGB-guard** is explicitly noted — BA 43 has no
    naming collision with the temporal auditory cortex, so unlike
    BA 41 and BA 42 there is no MGB_AFFERENT_GUARD field.
[ ] The **no-S2-continuity-note** is explicitly noted — BA 43 has
    a BA 43 ↔ BA 3 (postcentral somatosensory) structural
    continuity, which is a component-level continuity, not a
    S2-style inter-package boundary, so unlike BA 42 there is no
    S2_FUNCTIONAL_CONTINUITY_NOTE field.
[ ] No SUBDIVISIONS promotion is performed while the PGC sibling's
    CORTICAL_TERRITORIES still references BA 43 as a single unit.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, ALTERNATE_NAMES,
    NAMING_COLLISION_WITH, PARCELATION_AMBIGUITY, DUAL_
    CYTOARCHITECTONIC_CHARACTER, BA44_OPERClULAR_BOUNDARY_GUARD,
    PGC_OVERLAP_RELATIONSHIP, architectonic neighbourhoods,
    modern crosswalk, FUNCTIONAL_DOMAINS set) match the right
    sibling; DOMAIN_EMPHASIS, CONNECTIVITY emphasis, and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The bilateral-vs-ipsilateral asymmetry is verified**: the
    left BA 43 carries a bilateral taste-recognition anchor, the
    right BA 43 carries an ipsilateral taste-intensity anchor, and
    neither has been copied verbatim from the other.
[ ] Any downstream code assigning BA 43 gustatory function must
    route through DOMAIN_EMPHASIS and must weight the left BA 43
    toward **recognition** and the right BA 43 toward
    **intensity** — averaging left and right would erase the
    lateralized signal.
[ ] Any downstream code querying "opercular cortex" must specify
    the BA — BA 43 (gustatory operculum) and BA 44 (speech-motor
    operculum) are different territories separated by the
    inferior precentral / inferior frontal sulcus junction, and
    the BA44_OPERClULAR_BOUNDARY_GUARD is enforced.
[ ] Any downstream code querying BA 43's gustatory function must
    also query the PGC (under ..insular) — BA 43 is the
    architectonic core; the PGC is the functional field that
    spans BA 43 plus area G plus opercula plus (conditionally)
    base of central sulcus.
"""