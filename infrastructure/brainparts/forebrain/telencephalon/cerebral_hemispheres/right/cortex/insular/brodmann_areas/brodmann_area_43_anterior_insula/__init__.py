"""
Brodmann Area 43 (Anterior Insula / Postcentral Operculum) — Right Hemisphere
==============================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_43_anterior_insula   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the right
hemisphere's **BA 43** — the **anterior insula / postcentral operculum**
territory that Brodmann identified as the **subcentral area** and that
modern gustatory neuroscience identifies as the **primary gustatory
cortex** . It is the **only insular BA
with a classical Brodmann number that maps cleanly to a specific
functional region**, and it is the **architectonic core of the primary
gustatory cortex (PGC)** — the functional field that spans BA 43 plus
area G, the opercula, and (conditionally) the base of the central
sulcus.

Parent: ``..brodmann_areas`` (right insular BA registry) — sibling to
BA 13, BA 14, BA 16, BA 41, BA 42.

This package is the **structural mirror** of
``../../left/cortex/insular/brodmann_areas/brodmann_area_43_anterior_insula``.
The BA number, the **dual cytoarchitectonic character** (gustatory +
oral somatosensory), the **PARCELATION_AMBIGUITY** field (postcentral
vs insular), the **BA 43 ↔ BA 44 boundary guard**, and the **BA 43 ↔
PGC overlap** relationship are identical on both sides; the
**functional emphasis** and **clinical significance** diverge — on the
right, BA 43's gustatory territory is weighted toward **taste intensity
/ concentration**, the **intensity-linked hedonic valuation**
interface with the right PGC, the **sympathetic** autonomic coupling of
taste, and the **ipsilateral taste-intensity deficit** that follows
right insular damage.

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
non-taste cells.

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
the PGC. They are siblings under ``..insular``, and downstream code
must query the **PGC** for functional taste processing and BA 43 for
architectonic territory.

The right BA 43 borders:

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
                      BA 44 (pars opercularis of the IFG — prosody /
                      inhibition operculum on the right, speech-motor
                      operculum on the left) — **the gustatory vs
                      prosody-inhibition boundary on the right**

**Right-hemisphere specificity**: the right BA 43 is the hemisphere
whose gustatory territory is **dominant for taste intensity and
concentration**. fMRI studies show that **taste concentration
processing dominates in the right insular cortex**, and the right
insula is **more sensitive to intensity variations** across
concentrations, albeit with a nonlinear response profile
. Right insular damage produces an
**ipsilateral taste recognition and intensity deficit** — a
**unilateral** pattern, in contrast to the left insula's bilateral
recognition deficit . The right
BA 43 is the hemisphere that **tracks the strength of a taste**, while
the left BA 43 is the hemisphere that **identifies what the taste is**
. This is the single sharpest
asymmetry in the human gustatory system, and it has no symmetric
counterpart on the left (see the left sibling).

The right BA 43 is also the hemisphere whose **caudolateral
orbitofrontal cortex** is the more consistently right-lateralized
secondary taste area — meta-analysis of human functional neuroimaging
studies found that **only two taste-related peaks in the caudolateral
OFC were observed, and both were in the right hemisphere**
. The right BA 43 → right caudolateral OFC
projection is therefore the more prominent secondary-taste pathway.

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
                               BA 43 from BA 44 (right pars
                               opercularis — prosody / inhibition
                               operculum; gustatory vs
                               prosody-inhibition boundary)

    Functional overlays
        primary gustatory cortex (PGC) — OVERLAP, NOT NESTING
            BA 43 is the **architectonic core** of the PGC. The PGC
            leaf package under ``..insular`` describes the
            functional gustatory field; BA 43 describes the
            architectonic territory at its core. On the **right**,
            BA 43's gustatory contribution is weighted toward the
            **intensity / concentration** aspect — the "how
            strong is this food?" question — and toward the
            **intensity-linked hedonic valuation** interface with
            the right PGC.
        multimodal intraoral integration (dual character)
            BA 43's dual cytoarchitectonic character — gustatory
            fundus + somatosensory opercular crown — is the
            anatomical basis for the **taste-plus-texture-plus-
            temperature** integration that underlies flavour. On
            the right, the integration is weighted toward the
            **flavour-intensity** aspect; on the left, toward the
            **flavour-identity / recognition** aspect.
        hedonic valuation interface
            BA 43 is the cortical locus where taste identity
            meets affective value. The right BA 43 → right OFC
            projection carries the hedonic value of taste to the
            **right caudolateral OFC**, which is the more
            consistently right-lateralized secondary taste area in
            humans . On
            the right, the hedonic interface is weighted toward
            the **intensity-linked / arousal** valuation aspect;
            on the left, toward the **recognition-linked /
            language-adjacent** aspect.
        autonomic coupling (sympathetic on the right)
            Taste stimuli drive **autonomic responses** — salivation,
            gastric acid secretion, insulin release, and
            cardiovascular changes — through BA 43's projections
            to the hypothalamus and the NST. On the **right**, the
            coupling is weighted toward **sympathetic** outflow —
            pressor and tachycardic responses, and the
            anticipatory arousal that accompanies food
            expectation. On the left, toward parasympathetic
            (vagal bradycardia, depressor responses, cephalic-phase
            insulin release).
        social-emotional (marginal)
            BA 43's contribution to the social-emotional network is
            **marginal** — it operates through the affective
            valuation of food and the commensality aspects of
            eating, not through the anterior insular hub's core
            social-emotional functions. On the right, the marginal
            contribution is weighted toward **affective-salience
            food-related arousal**; on the left, toward
            **language-linked food-related emotion**.
        gustatory-somatosensory frontier (BA 43 ↔ BA 44 boundary)
            BA 43 is at the **gustatory pole** of the operculum;
            BA 44 (right pars opercularis of the IFG) is at the
            **prosody-inhibition pole**. The two are separated by
            the inferior precentral sulcus / inferior frontal
            sulcus junction. **This is a structural boundary, not
            a naming collision** — BA 43 and BA 44 are different
            territories in the same lobe, and downstream code must
            specify which one it means when querying "opercular
            cortex." On the right, the BA 44 side is the
            prosody-inhibition operculum, not the speech-motor
            operculum.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours and functional overlays are the same on both
sides. What differs is the **emphasis** within the gustatory,
multimodal, hedonic, and autonomic overlays: the right BA 43 is
weighted toward **intensity / flavour-intensity / sympathetic**
aspects; the left BA 43 is weighted toward **recognition /
flavour-identity / parasympathetic** aspects.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 13 (middle insula)                  ventromedial neighbour via
                                           the granular transition.
                                           **On the right, BA 13 is
                                           the interoceptive-accuracy
                                           node**, and BA 43's
                                           gustatory intensity
                                           processing is
                                           hierarchically downstream
                                           of BA 13's interoceptive
                                           re-representation
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
    BA 44 (right pars opercularis of the   lateral neighbour across
    IFG)                                   the inferior precentral /
                                           inferior frontal sulcus
                                           junction — **gustatory
                                           operculum vs prosody-
                                           inhibition operculum
                                           boundary on the right**
                                           (speech-motor on the
                                           left); downstream code
                                           must specify which
                                           opercular territory it
                                           means
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
BA-numbered neighbours, with the **BA 44 side note** updated to reflect
the right BA 44's prosody-inhibition role (vs the left's speech-motor
role). The **BA 3** and **area G** entries are notably **not** BA
numbering collisions — BA 3 is the somatosensory component of BA 43
itself, and area G is a functional designation.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 43 participates in **five** canonical insular domains on the right.
The emphasis is as follows:

    gustatory                                    (right emphasis — PRIMARY)
        **This is BA 43's defining contribution on both hemispheres,
        but the right weighting is toward intensity.** BA 43 is the
        architectonic core of the primary gustatory cortex, and the
        right BA 43 is the hemisphere whose gustatory territory
        supports **taste intensity and concentration** processing.
        Right insular damage produces an **ipsilateral taste
        recognition and intensity deficit** — a **unilateral**
        pattern, in contrast to the left insula's bilateral
        recognition deficit . The right
        BA 43 is weighted toward the **intensity / concentration**
        aspect of taste; the left BA 43 is weighted toward the
        **recognition / flavour-identity** aspect.

    multimodal_intraoral_integration                (right emphasis — PRIMARY)
        **This is BA 43's second primary contribution on the right.**
        BA 43's dual cytoarchitectonic character — gustatory fundus
        + somatosensory opercular crown — is the anatomical basis
        for the **taste-plus-texture-plus-temperature**
        integration that underlies flavour. On the right, the
        integration is weighted toward the **flavour-intensity**
        aspect — the "how strong is this food?" question.

    hedonic_valuation_interface                    (right emphasis — SECONDARY)
        BA 43 is the cortical locus where taste identity meets
        affective value. The right BA 43 → right caudolateral OFC
        projection carries the hedonic value of taste to the
        secondary taste area. **The right caudolateral OFC is the
        more consistently right-lateralized secondary taste area
        in humans** — meta-analysis found that only two
        taste-related peaks in the caudolateral OFC were observed,
        and both were in the right hemisphere. On the right, the
        hedonic interface is weighted toward the
        **intensity-linked / arousal** valuation aspect — the
        affective response to how strong a food is.

    autonomic_control (sympathetic)                (right emphasis — SECONDARY)
        Taste stimuli drive **autonomic responses** — salivation,
        gastric acid secretion, insulin release, and
        cardiovascular changes — through BA 43's projections to
        the hypothalamus and the NST. On the right, the coupling is
        weighted toward **sympathetic** outflow — pressor and
        tachycardic responses, and the anticipatory arousal that
        accompanies food expectation. The right BA 43 →
        hypothalamus and BA 43 → NST projections are part of this
        sympathetic substrate.

    social_emotional (marginal)                    (right emphasis — MARGINAL)
        BA 43's contribution to the social-emotional network is
        **marginal** — it operates through the affective valuation
        of food and the commensality aspects of eating. On the
        right, the marginal contribution is weighted toward
        **affective-salience food-related arousal** — the somatic
        and autonomic component of food-related emotion.

**Right-specific caveat on `speech_articulation`.** The domain **does
not exist on the right**. No right BA carries it. Right insular
lesions do not produce apraxia of speech. The right BA 43 excludes it
not because it belongs to the lobe as a whole (that is the left's
rationale) but because it is absent from the right hemisphere
entirely. Additionally, BA 43 is at the gustatory pole, not the
anterior insular hub, so the speech-articulation territory (BA 13 /
BA 16 / opercular transition) is far from BA 43 regardless of
hemisphere.

**Right-specific caveat on `vestibular_and_self_location`.** This
domain is **BA-13-emphasized on the right** (see
``brodmann_area_13_middle_insula``), not BA-43-emphasized. The right
BA 43 does **not** carry it.

**Right-specific caveat on `nociception_and_pain_affect` and
`thermoreception`.** These domains belong to the **posterior**
insular territory (BA 41 / BA 42), not to BA 43. BA 43's chemosensory
territory is gustatory and oral somatosensory, not nociceptive or
thermoreceptive. BA 43 **does** participate in oral **thermal**
sensation — the temperature of food is part of the multimodal
intraoral integration — but this is a **somatosensory** thermal
signal, not a **primary thermoreceptive** one. It belongs to
`multimodal_intraoral_integration`, not to a distinct
`thermoreception` domain.

**Right-specific caveat on `interoception`.** BA 43's interoceptive
contribution is **marginal** — it participates in the visceral
responses to food (cephalic-phase insulin release, gastric acid
secretion) through its autonomic projections, but the primary
interoceptive territory is the **posterior insula** (BA 13 / BA 41 /
BA 42). The **interoceptive-accuracy** component is more strongly
right-weighted at BA 13 (see right BA 13). `interoception` is
**omitted** from the right BA 43 `FUNCTIONAL_DOMAINS` tuple; the
autonomic coupling that BA 43 contributes is captured under
`autonomic_control`.

**Right-specific caveat on `salience_network`.** This domain is the
**anterior insular hub** — BA 16 / BA 14 territory, not BA 43. BA 43
is at the gustatory pole, not the salience pole. `salience_network` is
**omitted** from the right BA 43 `FUNCTIONAL_DOMAINS` tuple. **The
right BA 43's "affective-salience" emphasis in `social_emotional`
should not be confused with the `salience_network` domain** — the
latter is an anterior-insular network-level property, while the former
is a gustatory-pole food-related-affect weighting.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → VPMpc (parvicellular ventroposteromedial nucleus)
            **BA 43's primary thalamic afferent.** The VPMpc relays
            gustatory input from the rostral NST (directly in
            primates, via the parabrachial nucleus in rodents) to
            the anterior insula. BA 43 is at the **core** of the
            VPMpc projection zone . On the
            right, the VPMpc → BA 43 pathway is weighted toward
            **intensity / concentration** processing — the right
            insula is more sensitive to intensity variations
            across concentrations.
        → VPL / VPI (ventroposterior lateral / inferior)
            Somatosensory thalamic nuclei with a projection to the
            **postcentral opercular crown** of BA 43's territory —
            the oral somatosensory component of BA 43's dual
            character. On the right, this projection is weighted
            toward the **flavour-intensity** aspect of texture and
            temperature processing.

    cortical afferents
        → BA 13 (middle insula), right
            The granular transition from BA 13 to the anterior
            insula projects into BA 43's territory. On the right,
            BA 13 is the interoceptive-accuracy node, and the
            BA 13 → BA 43 projection carries the interoceptive
            signal that BA 43 couples to the gustatory intensity
            processing.
        → BA 3 (postcentral somatosensory), right
            BA 43's postcentral opercular crown is **continuous**
            with BA 3's oral somatosensory representation. The
            BA 3 → BA 43 projection carries the texture and
            temperature content that BA 43 integrates with taste.
        → primary gustatory cortex (PGC), right
            **The BA 43 ↔ PGC relationship is overlap, not
            nesting.** BA 43 is the architectonic core of the PGC;
            the PGC is the functional gustatory field that spans
            BA 43 + area G + opercula + (conditionally) base of
            central sulcus + right-emphasized caudolateral OFC.
            On the right, the PGC → BA 43 projection is weighted
            toward **intensity / concentration** processing.
        → anterior insula (via intrainsular connections)
            BA 43 projects rostrally to the anterior insular hub,
            carrying the gustatory signal that the hub transforms
            into the full salience and affective response.

    subcortical efferents
        → orbitofrontal cortex (OFC), right
            **BA 43 → right caudolateral OFC is the dominant
            secondary-taste pathway.** The right caudolateral OFC
            is the more consistently right-lateralized secondary
            taste area in humans — meta-analysis found that only
            two taste-related peaks in the caudolateral OFC were
            observed, and both were in the right hemisphere
            . On the right, the BA 43 → OFC
            projection carries the **intensity-linked** hedonic
            content.
        → hypothalamus (lateral hypothalamus), right
            **BA 43 → LH is part of the sympathetic efferent
            pathway.** On the right, this projection is weighted
            toward sympathetic outflow — pressor and tachycardic
            responses, and the anticipatory arousal that
            accompanies food expectation.
        → nucleus of the solitary tract (NST), right
            BA 43 projects to the NST, the brainstem relay for
            gustatory and visceral afferents and the origin of
            autonomic outflow. On the right, the BA 43 → NST
            projection is part of the sympathetic substrate.
        → amygdala (basolateral nuclei), right
            **Right-emphasized.** Reciprocal connections support
            the **affective valuation** of taste and the
            **conditioned taste aversion** memory. On the right,
            the BA 43 → amygdala projection is weighted toward the
            **intensity-linked / arousal** affective content.
        → ventral striatum / nucleus accumbens
            The BA 43 → OFC → ventral striatum pathway supports
            the **reward value** of taste and the **ingestive
            decision-making** that follows taste intensity
            processing. On the right, this pathway is the
            dominant reward-intensity substrate.

    brainstem interactions
        → parabrachial nucleus (indirect via VPMpc)
            The parabrachial → VPMpc → BA 43 pathway is the
            anatomical substrate of the primary gustatory relay.
        → dorsal motor nucleus of the vagus (DMV)
            BA 43 → hypothalamus → DMV projections support the
            **cephalic-phase** autonomic responses to food
            anticipation and consumption. On the right, the
            emphasis is on sympathetic anticipation (arousal),
            not parasympathetic gastric priming.

    callosal connections
        → left BA 43
            Interhemispheric coordination of the gustatory
            operculum. The right → left traffic carries the
            **intensity-linked** taste signal and **sympathetic**
            autonomic signals; the left → right traffic carries
            the **recognition-linked** taste signal (the left's
            dominant contribution to bilateral taste recognition)
            and **parasympathetic** autonomic signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the VPMpc → BA 43 pathway carries gustatory signals that the
right uses for **intensity / concentration** processing;
(b) the BA 43 → hypothalamus, BA 43 → NST, and BA 43 → DMV
projections are **sympathetic** rather than parasympathetic;
(c) the BA 43 → right caudolateral OFC projection carries
**intensity-linked** hedonic content, and the callosal traffic carries
intensity-linked and sympathetic signals.

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
itself), but this is a component-level continuity, not an
inter-package S2-style boundary. There is no
`S2_FUNCTIONAL_CONTINUITY_NOTE` field in this package.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ba43_ipsilateral_taste_intensity
        **This is the right BA 43 anchor par excellence.** Right
        insular damage produces an **ipsilateral taste recognition
        and intensity deficit** — a **unilateral** pattern, in
        contrast to the left insula's bilateral recognition
        deficit . The right BA 43 is
        the hemisphere whose gustatory territory is **dominant for
        taste intensity and concentration**; the left BA 43 is
        weighted toward recognition. Any downstream code that
        computes a "taste intensity score" must weight the right
        BA 43 more heavily and must not average left and right —
        averaging would erase the lateralized signal.

    right_ba43_intensity_linked_hedonic_valuation
        Right BA 43's hedonic interface with the right PGC supports
        the **intensity-linked / arousal** evaluation of food
        pleasantness. Right BA 43 lesions can produce **reduced
        food-related arousal** — the patient may still identify
        food pleasantness on the left-recognition basis, but the
        affective arousal associated with intense taste is
        blunted. This is the mirror of the left BA 43's
        recognition-linked / language-adjacent hedonic valuation.

    right_ba43_flavour_intensity_deficit
        BA 43's dual character — gustatory fundus + somatosensory
        opercular crown — supports the **flavour-intensity**
        integration (taste + texture + temperature → "how strong
        is this food?"). Right BA 43 lesions can produce
        **flavour-intensity deficits** — the patient can still
        identify what the food is but cannot judge how strong the
        combined sensory pattern is. This is a **right-weighted**
        anchor: the left BA 43's chemosensory contribution is
        more weighted toward **flavour identity**.

    right_ba43_sympathetic_autonomic_coupling
        Right BA 43's gustatory activity drives **sympathetic**
        autonomic responses — pressor and tachycardic responses,
        and the anticipatory arousal that accompanies food
        expectation. Right BA 43 lesions can produce
        **sympathetic dysregulation** in these responses, distinct
        from the left BA 43's parasympathetic signature (vagal
        bradycardia, depressor responses, cephalic-phase insulin
        release).

    right_ba43_caudolateral_ofc_secondary_taste_pathway
        **Right-emphasized.** The right BA 43 → right caudolateral
        OFC projection is part of the **right-lateralized
        secondary taste network** — meta-analysis found that only
        two taste-related peaks in the caudolateral OFC were
        observed, and both were in the right hemisphere
        . Right BA 43 lesions can
        disconnect this network and produce combined
        taste-intensity and intensity-linked hedonic deficits.

    gustatory_hallucination_and_insular_lesions
        **Gustatory hallucinations** — the phantom perception of
        taste — are a recognized symptom of **insular lesions**
        involving the gustatory cortex. Right BA 43 / PGC lesions
        can produce gustatory hallucinations, though the
        left-lateralized gustatory aura literature is more
        extensive (see left sibling).

    gustatory_aura_in_temporal_lobe_epilepsy
        **Gustatory auras** — brief, stereotyped taste sensations
        preceding a seizure — are a classic symptom of **temporal
        lobe epilepsy** and are attributed to the spread of
        epileptiform activity to the insular gustatory cortex.
        Right BA 43 involvement is part of the substrate, and the
        right-sided gustatory aura semiology is weighted toward
        the **affective / arousal** component.

    eating_reflex_seizures
        **Eating-reflex seizures** — seizures triggered by food or
        syrup intake — have been successfully treated by
        **resection of the middle short gyrus of the right
        insula** (BA 13 territory, more rostral than BA 43). The
        broader gustatory network includes BA 43. On the right,
        the eating-reflex seizure semiology is weighted toward
        the **affective / arousal** aspects; on the left, toward
        the **gustatory / language-linked** aspects.

    conditioned_taste_aversion_therapy
        BA 43 / PGC's role in **CTA memory** has clinical
        implications for **aversion therapy** (e.g., in alcohol
        use disorder) and for understanding **taste aversions**
        that develop during chemotherapy or radiation therapy.
        The right BA 43 is the hemisphere whose gustatory territory
        supports the **intensity-linked / autonomic** CTA memory;
        the left BA 43 supports the **recognition-linked** CTA
        memory. The combined left-right gustatory system is the
        cortical substrate of CTA.

    right_insular_glioma_resection_taste_mapping
        Because BA 43 is a **buried transition territory** at the
        gustatory pole of the operculum, resecting a right insular
        / opercular glioma in the BA 43 zone requires careful
        mapping of taste, autonomic, and oral somatosensory
        function. **Awake surgery with direct electrical
        stimulation** is the standard approach. Right BA 43
        resections risk **ipsilateral taste-intensity deficits**,
        **flavour-intensity deficits**, and **sympathetic
        dysregulation** — distinct from the risks of anterior
        short gyri resections (prosody and inhibition on the
        right) and posterior insula resections (primary
        interoceptive / pain deficits).

    gustatory_operculum_vs_prosody_inhibition_operculum_hazard
        **The BA 43 ↔ BA 44 boundary is a surgical hazard.**
        BA 43 (gustatory operculum) is separated from BA 44
        (right pars opercularis of the IFG — prosody-inhibition
        operculum on the right, speech-motor on the left) by the
        inferior precentral sulcus / inferior frontal sulcus
        junction. Downstream code that queries "opercular cortex"
        must specify which BA it means, and pre-surgical workup
        must distinguish the gustatory from the prosody-inhibition
        operculum on the right. This is a **structural hazard, not
        a naming collision**.

    right_insular_stroke_taste_dysfunction
        Right insular strokes — including those involving BA 43 —
        produce an **ipsilateral taste intensity and recognition
        deficit**. Taste disturbance occurs in **4 % of right
        insular strokes** versus **19 % of left insular strokes**
        , consistent with the left's
        dominant role in recognition. The right BA 43 is the
        gustatory architectonic territory whose lesion produces
        the intensity component of this deficit pattern.

    right_ba43_taste_cognition_alzheimers
        **Right-emphasized.** In Alzheimer's disease, **glucose
        metabolism in the right insula is lower in the low
        taste-cognition subgroup**, linking the right insula
        specifically to **taste cognition** — the memory-linked,
        food-recognition aspect of taste processing. The right
        BA 43 contributes to this right-emphasized function
        through its intensity-linked gustatory processing.

    right_ba43_bulimia_bitter_sensitivity
        **Right-emphasized.** fMRI studies in bulimia nervosa
        patients show **reduced sensitivity to bitter stimuli in
        the right insular cortex**, indicating that right insular
        dysfunction in taste processing may contribute to the
        disorder's altered food reward processing. The right
        BA 43 is part of the intensity-sensitive substrate where
        this alteration is detectable.

These anchors are **right-hemisphere-specific** in two senses:
(a) the right BA 43 is the hemisphere whose gustatory territory is
**dominant for taste intensity**, and right insular damage produces an
**ipsilateral** intensity and recognition deficit; (b) the right
BA 43's gustatory and autonomic contributions are weighted toward the
**intensity / flavour-intensity / sympathetic** aspect (left is
recognition / flavour-identity / parasympathetic). The left sibling's
docstring carries the corresponding left-sided anchors (bilateral
taste recognition, flavour-identity deficit, parasympathetic coupling,
language-linked hedonic valuation).

**The BA 43 ↔ PGC relationship and the BA 43 ↔ BA 44 boundary hazard
are hemisphere-invariant** — they are documented identically in both
packages.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The right insular BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 43 (which on
    the right is ``("gustatory",
    "multimodal_intraoral_integration",
    "hedonic_valuation_interface")``), and enforcer of the
    ``speech_articulation`` exclusion (which on the right means
    the domain is not declared anywhere, not that it is assigned
    to the lobe as a whole).

..brodmann_area_13_middle_insula
    Ventromedial neighbour via the granular transition. **On the
    right, BA 13 is the interoceptive-accuracy node** (Critchley
    et al. 2004), and BA 43's gustatory intensity processing is
    hierarchically downstream of BA 13's interoceptive
    re-representation.

..brodmann_area_14
    Rostral / anterior short gyri neighbour. **On the right,
    BA 14 is the sympathetic autonomic and flavour-intensity
    territory**, and BA 43's gustatory intensity contribution is
    functionally continuous with BA 14's intensity-linked
    chemosensory territory.

..brodmann_area_16
    Rostral / anterior short gyri neighbour. **BA 16's primary
    peak is `vestibular_and_self_location` in the parent registry,
    not gustatory**, and BA 43's gustatory territory is distinct.

..brodmann_area_41_posterior_insula
    Distant caudal neighbour — no direct adjacency (BA 13 and the
    agranular posterior insula intervene). BA 41 is the
    affective-motivational / sympathetic nociceptive and
    thermoreceptive transition territory on the right; BA 43 is
    the gustatory intensity territory. **Different functional
    territories within the insular lobe.**

..brodmann_area_42_posterior_insula
    Distant caudal neighbour — no direct adjacency. BA 42 is the
    affective-salience opercular convergence territory on the
    right; BA 43 is the gustatory intensity operculum. **Different
    functional territories within the insular lobe.**

...primary_gustatory_cortex
    The **functional-field sibling** (one level up, under
    ``..insular``). **The BA 43 ↔ PGC relationship is overlap, not
    nesting.** BA 43 is the architectonic territory; PGC is the
    functional gustatory field that spans BA 43 + area G +
    opercula + (conditionally) base of central sulcus +
    right-emphasized caudolateral OFC. The two packages must be
    created / updated together, and the PGC package's
    `BRODMANN_AREAS` field must reference BA 43.

..cortex.frontal.brodmann_areas.brodmann_area_44
    **The prosody-inhibition operculum on the right** (vs the
    speech-motor operculum on the left). BA 44 (right pars
    opercularis of the IFG) is separated from BA 43 by the
    inferior precentral sulcus / inferior frontal sulcus
    junction. **Downstream code must specify which BA it means
    when querying "opercular cortex."** This is a **structural
    boundary, not a naming collision** — BA 43 and BA 44 are
    different territories in the same lobe.

..cortex.frontal
    The frontal operculum (including BA 44) is adjacent to BA 43
    across the opercular boundary. The frontal package must
    declare the insula as a hidden neighbour, must note the
    **BA 43 ↔ BA 44 gustatory vs prosody-inhibition boundary on
    the right** (speech-motor on the left), and must not conflate
    the two opercular territories.

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
    cortical afferent to the right BA 43, and must **not** declare
    the medial geniculate body (MGB) as an afferent to BA 43 —
    MGB projects to the temporal BA 41 / BA 42, not to BA 43.

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem relay that feeds
    VPMpc and thus BA 43. On the right, the parabrachial → BA 43
    pathway is weighted toward intensity / concentration
    processing.

../../brainparts/hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
    The **nucleus of the solitary tract (NST)** is the brainstem
    gustatory relay that feeds VPMpc and thus BA 43. The NST
    package must declare the right BA 43 as a cortical target
    (via the VPMpc relay), noting the sympathetic weighting.

../../subcortical/diencephalon/hypothalamus
    The right BA 43 → right hypothalamus projection supports
    **sympathetic** autonomic coupling to food anticipation and
    consumption. The hypothalamus package must declare the right
    BA 43 as a cortical afferent.

../../subcortical/medial_temporal_lobe/amygdala
    The right basolateral amygdala receives BA 43 projections
    supporting the **affective valuation** of taste and the
    **conditioned taste aversion** memory. On the right, the
    projection is weighted toward the **intensity-linked /
    arousal** affective content. The amygdala package must
    declare the right BA 43 as a cortical afferent.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The BA 43 → OFC → ventral striatum pathway supports the
    **reward value** of taste and **ingestive decision-making**.
    On the right, this pathway is the dominant reward-intensity
    substrate.

../../left/cortex/insular/brodmann_areas/brodmann_area_43_anterior_insula
    The left-hemisphere homologue. Structural fields (BA number,
    region label, **dual cytoarchitectonic character**,
    **PARCELATION_AMBIGUITY field**, **BA 43 ↔ PGC overlap
    relationship**, **BA 43 ↔ BA 44 boundary guard**,
    architectonic neighbourhoods, BA-to-neighbour adjacency,
    FUNCTIONAL_DOMAINS set) MUST be byte-identical. Functional
    emphasis and clinical significance diverge — the right BA 43
    is weighted toward taste intensity, flavour intensity,
    intensity-linked hedonic valuation, sympathetic autonomic
    control, and ipsilateral taste-intensity deficit; the left
    BA 43 is weighted toward taste recognition, flavour identity,
    recognition-linked / language-adjacent hedonic valuation,
    parasympathetic autonomic control, and bilateral
    taste-recognition deficit.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_43_anterior_insula"
    HEMISPHERE          = "right"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 43
    INSULAR_REGION      = "anterior_opercular"
    CYTOTECTONIC_GRADIENT = "agranular_to_dysgranular"
    ALTERNATE_NAMES     = ("subcentral_area",
                           "opercular_part_of_postcentral_gyrus")

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** BA 43 is unique to this region.
        # Unlike BA 41 and BA 42, there is no MGB guard, no
        # parcellation convention for the BA number, and no
        # circular-sulcus boundary at a naming level. The BA 43 ↔
        # BA 44 boundary is a **structural** boundary (gustatory vs
        # prosody-inhibition operculum on the right; speech-motor
        # on the left), not a naming collision, and it is
        # documented separately in the CROSS-REFERENCES. **Byte-
        # identical to the left sibling's.**

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
        # **Byte-identical to the left sibling's.**

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
        # **Byte-identical to the left sibling's.**

    BA44_OPERClULAR_BOUNDARY_GUARD = (
        "BA 43 (gustatory operculum) is separated from BA 44 "
        "(right pars opercularis of the IFG — prosody-inhibition "
        "operculum on the right; speech-motor operculum on the "
        "left) by the inferior precentral sulcus / inferior frontal "
        "sulcus junction. Downstream code that queries 'opercular "
        "cortex' must specify which BA it means. This is a "
        "structural boundary, not a naming collision. BA 44 is "
        "under cortex/frontal, not cortex/insular."
    )
        # **Byte-identical to the left sibling's** — the guard text
        # is the same on both sides; the right-vs-left BA 44 role
        # divergence is captured in the CROSS-REFERENCES, not in
        # the guard text.

    PGC_OVERLAP_RELATIONSHIP = (
        "The BA 43 ↔ PGC relationship is overlap, not nesting. "
        "BA 43 is the architectonic territory. The primary "
        "gustatory cortex (PGC, under ..insular) is the functional "
        "gustatory field that spans BA 43 + area G + opercula + "
        "(conditionally) base of central sulcus + right-emphasized "
        "caudolateral OFC. The PGC package's BRODMANN_AREAS field "
        "must reference BA 43. Neither is a child of the other."
    )
        # **Byte-identical to the left sibling's**, with the
        # right-emphasized caudolateral OFC component noted (the
        # left sibling's text omits the caudolateral OFC component
        # because it is right-emphasized; the right sibling's text
        # includes it because it is part of the right PGC's
        # cortical territories). **This is the only divergence in
        # this field, and it is required by the symmetry contract.**

    FUNCTIONAL_DOMAINS  = (
                              "gustatory",             # PRIMARY
                              "multimodal_intraoral_integration",
                                                       # PRIMARY
                              "hedonic_valuation_interface",
                              "autonomic_control",     # right:
                                                       # sympathetic
                              "social_emotional",      # marginal
                              # NOTE: speech_articulation does NOT
                              # exist on the right; additionally,
                              # BA 43 is at the gustatory pole,
                              # not the anterior insular hub.
                              # NOTE: vestibular_and_self_location
                              # is BA-13-emphasized on the right.
                              # NOTE: nociception_and_pain_affect
                              # and thermoreception are EXCLUDED
                              # (BA 41 / BA 42 territory).
                              # NOTE: interoception is EXCLUDED
                              # (BA 13 / BA 41 / BA 42 territory;
                              # BA 43's marginal visceral
                              # contribution is under
                              # autonomic_control).
                              # NOTE: salience_network is
                              # EXCLUDED (BA 16 / BA 14 territory;
                              # BA 43 is at the gustatory pole).
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "gustatory":
                                  "taste_intensity_concentration_"
                                  "ipsilateral_dominant",
                              "multimodal_intraoral_integration":
                                  "flavour_intensity_arousal_linked",
                              "hedonic_valuation_interface":
                                  "intensity_linked_arousal_hedonic_"
                                  "evaluation",
                              "autonomic_control":
                                  "sympathetic_pressor_tachycardic_"
                                  "anticipatory_food_arousal",
                              "social_emotional":
                                  "affective_salience_food_related_"
                                  "emotion_marginal",
                          }

    MODERN_CROSSWALK    = {   # BA 43 → modern parcellation labels
                              "HCP_180":       ("OP4", "Ig", "Id"),
                              "Ongur_Price_2000": ("G", "Iai", "Ial"),
                              "Petrides_Pandya":  ("G", "Ig", "Id"),
                          }
        # **Byte-identical to the left sibling's.**

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_ba43_ipsilateral_taste_"
                              "intensity",
                              "right_ba43_intensity_linked_hedonic_"
                              "valuation",
                              "right_ba43_flavour_intensity_"
                              "deficit",
                              "right_ba43_sympathetic_autonomic_"
                              "coupling",
                              "right_ba43_caudolateral_ofc_"
                              "secondary_taste_pathway",
                              "gustatory_hallucination_and_"
                              "insular_lesions",
                              "gustatory_aura_in_temporal_lobe_"
                              "epilepsy",
                              "eating_reflex_seizures",
                              "conditioned_taste_aversion_"
                              "therapy",
                              "right_insular_glioma_resection_"
                              "taste_mapping",
                              "gustatory_operculum_vs_prosody_"
                              "inhibition_operculum_hazard",
                              "right_insular_stroke_taste_"
                              "dysfunction",
                              "right_ba43_taste_cognition_"
                              "alzheimers",
                              "right_ba43_bulimia_bitter_"
                              "sensitivity",
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
(the precentral gyrus) and its postcentral continuation.

**The BA 43 ↔ PGC relationship is a required cross-package reference,
not a forward reference.** The PGC leaf package under ``..insular``
must declare BA 43 in its ``CORTICAL_TERRITORIES`` and its
``BRODMANN_AREAS``. Both packages must be created / updated in the
same commit — the BA 43 ↔ PGC overlap must not be left
half-declared.

**The BA 44 cross-package reference is a structural boundary, not a
forward reference.** BA 44 is a real package under
``cortex/frontal/brodmann_areas/``, and the BA 43 ↔ BA 44 boundary is
documented in both packages as a structural boundary (gustatory vs
prosody-inhibition operculum on the right; speech-motor on the left),
not a naming collision.

**All forward-declaration caveat text is byte-identical to the left
sibling's** except for the BA 44 role description ("prosody-
inhibition operculum on the right; speech-motor on the left" vs
"speech-motor operculum") — the divergence is required by the
hemisphere-specific BA 44 role.

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
  4. Mirror the promotion on the left side in the same commit.

**The gustatory component must remain the PGC's architectonic core.**
Any split must preserve the PGC's ``BRODMANN_AREAS`` reference to the
gustatory component. The PGC's ``CORTICAL_TERRITORIES`` field must be
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

**The right-specific caudolateral OFC entry in
`PGC_OVERLAP_RELATIONSHIP` must be preserved through any split.** The
right PGC's cortical territories include the right-emphasized
caudolateral OFC; the left PGC's do not carry this component at the
same weighting. Any split must maintain this asymmetry — the
caudolateral OFC reference cannot be dropped or averaged.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../brodmann_area_43_anterior_insula``:

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
        BA44_OPERClULAR_BOUNDARY_GUARD     byte-identical (the guard
                                           text is the same on both
                                           sides; the right-vs-left
                                           BA 44 role divergence is
                                           captured in CROSS-
                                           REFERENCES, not in the
                                           guard text)
        Architectonic neighbourhoods
        BA-to-neighbour adjacency (with the BA 44 side note
                                           diverging — prosody-
                                           inhibition on the right,
                                           speech-motor on the left)
        MODERN_CROSSWALK                   byte-identical
        FUNCTIONAL_DOMAINS set             the same five domains,
                                           with the same exclusions
        SUBDIVISIONS                       both empty (or both
                                           non-empty in the same way,
                                           if a split is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        PGC_OVERLAP_RELATIONSHIP
                               The right sibling's text includes
                               the **right-emphasized caudolateral
                               OFC** component in the PGC's
                               cortical territories; the left
                               sibling's text omits it (because
                               caudolateral OFC is right-emphasized).
                               **This is the only divergence in this
                               field, and it is required by the
                               symmetry contract.**
        DOMAIN_EMPHASIS        right: gustatory is "taste_intensity_
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
                               left: gustatory is "taste_recognition_
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
        CONNECTIVITY           same bundle names; right: VPMpc → BA 43
                               is weighted toward intensity /
                               concentration; BA 43 → hypothalamus /
                               NST / DMV is sympathetic; BA 43 →
                               right caudolateral OFC is the
                               dominant secondary-taste pathway;
                               callosal traffic carries intensity-
                               linked and sympathetic signals.
                               left: VPMpc → BA 43 is weighted
                               toward bilateral recognition;
                               BA 43 → hypothalamus / NST / DMV is
                               parasympathetic; BA 43 → left OFC
                               carries recognition-linked hedonic
                               content; callosal traffic carries
                               recognition-linked and
                               parasympathetic signals.
        CLINICAL_ANCHORS       right: fourteen anchors (ipsilateral
                               taste intensity, intensity-linked
                               hedonic valuation, flavour intensity
                               deficit, sympathetic coupling,
                               caudolateral OFC secondary taste
                               pathway, gustatory hallucinations,
                               gustatory auras, eating-reflex
                               seizures, CTA therapy, glioma taste-
                               mapping, gustatory vs prosody-
                               inhibition operculum hazard,
                               insular stroke taste dysfunction,
                               **taste cognition in Alzheimer's**,
                               **bulimia bitter sensitivity**).
                               left: eleven anchors (see left
                               sibling).

**The `DOMAIN_EMPHASIS` asymmetry is the sharpest single entry in this
contract.** Both hemispheres carry the same five domains and both
exclude the same four, but the emphasis within every shared domain
points in opposite directions: the right BA 43 is the
**intensity / flavour-intensity / sympathetic** territory, the left
BA 43 is the **recognition / flavour-identity / parasympathetic**
territory.

**The bilateral-vs-ipsilateral asymmetry is the second sharpest
entry.** Left insular damage produces a **bilateral** taste-recognition
deficit (the left hemisphere is dominant for recognition); right
insular damage produces an **ipsilateral** taste-intensity deficit
(the right hemisphere is dominant for intensity). This is the cleanest
double dissociation in the human gustatory system, and it must not be
averaged.

**The `PGC_OVERLAP_RELATIONSHIP` field diverges from the left sibling's
in exactly one respect** — the right side includes the right-emphasized
caudolateral OFC component in the PGC's cortical territories; the left
side omits it. This is the **only divergence in this field**, and it is
required by the symmetry contract because the caudolateral OFC is
right-emphasized in the human secondary-taste network.

**The structural fields — `PARCELATION_AMBIGUITY`,
`DUAL_CYTOARCHITECTONIC_CHARACTER`, and
`BA44_OPERClULAR_BOUNDARY_GUARD` — are byte-identical on both
sides.** They are properties of the BA 43 territory itself, not of the
hemisphere. The `BA44_OPERClULAR_BOUNDARY_GUARD`'s right-vs-left BA 44
role divergence is captured in the CROSS-REFERENCES, not in the guard
text.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_43_anterior_insula" (same as
    left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 43.
[ ] INSULAR_REGION is "anterior_opercular".
[ ] CYTOTECTONIC_GRADIENT is "agranular_to_dysgranular".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's.
[ ] **NAMING_COLLISION_WITH** is an empty tuple — BA 43 has **no**
    naming collision with any temporal or frontal BA. There is no
    MGB guard and no circular-sulcus naming-collision boundary.
[ ] **PARCELATION_AMBIGUITY** is present and byte-identical to the
    left sibling's.
[ ] **DUAL_CYTOARCHITECTONIC_CHARACTER** is present and
    byte-identical to the left sibling's.
[ ] **BA44_OPERClULAR_BOUNDARY_GUARD** is present and
    byte-identical to the left sibling's (the guard text is the
    same; the right-vs-left BA 44 role divergence is in the
    CROSS-REFERENCES).
[ ] **PGC_OVERLAP_RELATIONSHIP** is present and **differs from the
    left sibling's in exactly one respect**: the right side
    includes the right-emphasized caudolateral OFC component in
    the PGC's cortical territories. This divergence is required
    by the symmetry contract and must be documented.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - gustatory (PRIMARY)
    - multimodal_intraoral_integration (PRIMARY)
    - hedonic_valuation_interface
    - autonomic_control
    - social_emotional (marginal)
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation — the
    domain does not exist on the right (and, independently, BA 43
    is at the gustatory pole).
[ ] FUNCTIONAL_DOMAINS **excludes** vestibular_and_self_location
    (BA-13-emphasized on the right).
[ ] FUNCTIONAL_DOMAINS **excludes** nociception_and_pain_affect and
    thermoreception (BA 41 / BA 42 territory).
[ ] FUNCTIONAL_DOMAINS **excludes** interoception (BA 13 / BA 41 /
    BA 42 territory; BA 43's marginal visceral contribution is
    under autonomic_control).
[ ] FUNCTIONAL_DOMAINS **excludes** salience_network (BA 16 / BA 14
    territory; BA 43 is at the gustatory pole). **The right BA
    43's "affective-salience" emphasis in `social_emotional` must
    not be confused with the `salience_network` domain.**
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis** per domain:
    - gustatory → taste_intensity_concentration_ipsilateral_dominant
    - multimodal_intraoral_integration → flavour_intensity_arousal_
      linked
    - hedonic_valuation_interface → intensity_linked_arousal_
      hedonic_evaluation
    - autonomic_control → sympathetic_pressor_tachycardic_
      anticipatory_food_arousal
    - social_emotional → affective_salience_food_related_emotion_
      marginal
[ ] MODERN_CROSSWALK is present, byte-identical to the left
    sibling's.
[ ] CONNECTIVITY documents:
    - VPMpc thalamic afferent (primary, gustatory, weighted toward
      intensity / concentration on the right)
    - VPL / VPI thalamic afferent (postcentral opercular crown)
    - BA 13 granular-transition afferent (carrying interoceptive-
      accuracy signal on the right)
    - BA 3 postcentral somatosensory afferent
    - **PGC → BA 43 overlap afferent** (weighted toward intensity
      on the right)
    - BA 43 → anterior insula intrainsular afferent
    - **BA 43 → right caudolateral OFC secondary-taste pathway**
      (right-emphasized; the dominant secondary-taste pathway)
    - BA 43 → hypothalamus (sympathetic, right-specific)
    - BA 43 → NST (sympathetic, right-specific)
    - BA 43 → amygdala (intensity-linked affective valuation /
      CTA)
    - BA 43 → ventral striatum (reward-intensity substrate)
    - parabrachial → VPMpc → BA 43 (gustatory brainstem relay)
    - BA 43 → hypothalamus → DMV (cephalic-phase autonomic
      response, sympathetic anticipation on the right)
    - callosal traffic to left BA 43 (intensity-linked and
      sympathetic, right-specific)
[ ] CLINICAL_ANCHORS contains the fourteen right-specific anchors:
    - right_ba43_ipsilateral_taste_intensity
    - right_ba43_intensity_linked_hedonic_valuation
    - right_ba43_flavour_intensity_deficit
    - right_ba43_sympathetic_autonomic_coupling
    - right_ba43_caudolateral_ofc_secondary_taste_pathway
    - gustatory_hallucination_and_insular_lesions
    - gustatory_aura_in_temporal_lobe_epilepsy
    - eating_reflex_seizures
    - conditioned_taste_aversion_therapy
    - right_insular_glioma_resection_taste_mapping
    - gustatory_operculum_vs_prosody_inhibition_operculum_hazard
    - right_insular_stroke_taste_dysfunction
    - **right_ba43_taste_cognition_alzheimers**
    - **right_ba43_bulimia_bitter_sensitivity**
[ ] The **ipsilateral taste-intensity deficit** from right insular
    damage is documented as the primary right BA 43 anchor — the
    right hemisphere is dominant for intensity, and downstream
    code must weight the right BA 43 more heavily for intensity
    and must not average left and right.
[ ] The **intensity-linked hedonic valuation** is documented as a
    right-weighted anchor — the affective arousal associated with
    intense taste.
[ ] The **flavour-intensity deficit** is documented as a right-
    weighted anchor — the inability to judge how strong the
    combined sensory pattern is.
[ ] The **sympathetic autonomic coupling** is documented as a
    right-weighted anchor — pressor and tachycardic responses,
    anticipatory arousal.
[ ] The **right caudolateral OFC secondary taste pathway** is
    documented as a right-emphasized anchor — meta-analysis found
    that only two taste-related peaks in the caudolateral OFC were
    observed, and both were in the right hemisphere.
[ ] The **right-only taste-cognition-in-Alzheimer's anchor** is
    documented — right insula glucose hypometabolism in the low
    taste-cognition subgroup.
[ ] The **right-only bulimia bitter-sensitivity anchor** is
    documented — reduced right insular sensitivity to bitter
    stimuli in bulimia nervosa.
[ ] The **BA 43 ↔ BA 44 boundary hazard** is documented as a
    **surgical hazard** — the surgeon must not confuse the
    gustatory operculum with the prosody-inhibition operculum on
    the right (speech-motor on the left). This is a structural
    boundary, not a naming collision, and the
    BA44_OPERClULAR_BOUNDARY_GUARD field must be present and
    byte-identical to the left sibling's.
[ ] The **BA 43 ↔ PGC overlap** is documented in the
    PGC_OVERLAP_RELATIONSHIP field, which includes the right-
    emphasized caudolateral OFC component (the only divergence
    from the left sibling's field).
[ ] The **BA 43 ≠ BA 44** distinction is documented — the
    gustatory operculum (BA 43) vs the prosody-inhibition
    operculum (BA 44) on the right (speech-motor on the left),
    separated by the inferior precentral / inferior frontal
    sulcus junction.
[ ] The **BA 43 ≠ BA 13 / BA 14 / BA 16 / BA 41 / BA 42**
    distinction is documented — BA 43 is the gustatory pole,
    distinct from the multimodal (BA 13), olfactory-gustatory
    (BA 14), salience (BA 16), and nociceptive/thermoreceptive/
    opercular (BA 41 / BA 42) poles.
[ ] The **no-MGB-guard** is explicitly noted — BA 43 has no
    naming collision with the temporal auditory cortex.
[ ] The **no-S2-continuity-note** is explicitly noted — BA 43 has
    a BA 43 ↔ BA 3 (postcentral somatosensory) structural
    continuity, which is a component-level continuity, not a
    S2-style inter-package boundary.
[ ] No SUBDIVISIONS promotion is performed while the PGC sibling's
    CORTICAL_TERRITORIES still references BA 43 as a single unit.
[ ] The **caudolateral OFC asymmetry in PGC_OVERLAP_RELATIONSHIP**
    is verified — the right sibling's text includes the right-
    emphasized caudolateral OFC component; the left sibling's does
    not. This is the only divergence in this field and it is
    required by the symmetry contract.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, ALTERNATE_NAMES,
    NAMING_COLLISION_WITH, PARCELATION_AMBIGUITY, DUAL_
    CYTOARCHITECTONIC_CHARACTER, BA44_OPERClULAR_BOUNDARY_GUARD,
    architectonic neighbourhoods, modern crosswalk, FUNCTIONAL_
    DOMAINS set) match the left sibling; PGC_OVERLAP_RELATIONSHIP
    (caudolateral OFC component), DOMAIN_EMPHASIS, CONNECTIVITY
    emphasis, and CLINICAL_ANCHORS deliberately differ.
[ ] **The bilateral-vs-ipsilateral asymmetry is verified**: the
    right BA 43 carries an ipsilateral taste-intensity anchor, the
    left BA 43 carries a bilateral taste-recognition anchor, and
    neither has been copied verbatim from the other.
[ ] Any downstream code assigning BA 43 gustatory function must
    route through DOMAIN_EMPHASIS and must weight the right BA 43
    toward **intensity** and the left BA 43 toward
    **recognition** — averaging left and right would erase the
    lateralized signal.
[ ] Any downstream code querying "opercular cortex" must specify
    the BA — BA 43 (gustatory operculum) and BA 44 (prosody-
    inhibition operculum on the right; speech-motor on the left)
    are different territories separated by the inferior precentral
    / inferior frontal sulcus junction.
[ ] Any downstream code querying BA 43's gustatory function must
    also query the PGC (under ..insular) — BA 43 is the
    architectonic core; the PGC is the functional field that
    spans BA 43 plus area G plus opercula plus (conditionally)
    base of central sulcus plus right-emphasized caudolateral OFC.
"""