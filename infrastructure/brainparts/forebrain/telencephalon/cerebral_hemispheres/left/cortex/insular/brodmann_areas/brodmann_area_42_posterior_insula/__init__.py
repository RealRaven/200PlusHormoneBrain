"""
Brodmann Area 42 (Posterior Insula / Insular-Opercular Transition) — Left Hemisphere
=====================================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_42_posterior_insula   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 42 in its insular-opercular-transition sense** — the
more **rostral** component of the cortex at the junction of the
posterior insula and the operculum, across the circular sulcus. It is
the sibling of ``brodmann_area_41_posterior_insula`` — together they
form the insular BA 41/42 pair. It is **not** the secondary auditory
cortex, and the naming collision with ``temporal.brodmann_areas.
brodmann_area_42`` is the package's defining structural concern (see
below).

Parent: ``..brodmann_areas`` (left insular BA registry) — sibling to
BA 13, BA 14, BA 16, BA 41, BA 43.

This package is the **structural mirror** of
``../../right/cortex/insular/brodmann_areas/brodmann_area_42_posterior_insula``.
The BA number, the naming-collision field, the parcellation convention,
the MGB/auditory guard, the region label, and the
insular-opercular-transition gradient are identical on both sides; the
**functional emphasis** and **clinical significance** diverge — on the
left, BA 42's territory is weighted toward the **multimodal opercular
convergence** (somatosensory / nociceptive / thermoreceptive /
secondary-somatosensory), the **language-linked** evaluation of
opercular somatosensory content, the **parasympathetic** autonomic
coupling of opercular input, and the **protective-weighted** SUDEP
contribution.

--------------------------------------------------------------------------------
WHAT BA 42 IS — IN THE INSULAR CONTEXT
--------------------------------------------------------------------------------

Classically, **BA 42 is the secondary auditory cortex** — the planum
temporale, on the superior temporal plane just caudal to Heschl's
gyrus (temporal BA 41). That is the temporal BA 42 package's territory.

In **this** tree, ``brodmann_area_42_posterior_insula`` names the
**more rostral component of the insular-opercular transition zone** —
the cortex at the junction of the posterior insula and the
**parietal / temporal operculum**, across the circular sulcus. Where
the insular BA 41 territory is the more caudal transition component
(adjacent to the planum temporale and the primary
nociceptive/thermoreceptive cortex), the insular BA 42 territory is
the more **rostral** transition component (adjacent to the parietal
operculum and the secondary somatosensory cortex, S2).

The two territories are **not** the same:

    temporal BA 42      = secondary auditory cortex (planum temporale)
    insular BA 42       = insular-opercular transition, more rostral
                          component (posterior insula + parietal /
                          temporal operculum junction)

The two packages must never be merged, and no global BA index may
resolve "BA 42" without a lobe qualifier. The parent registry's
``BA 41 / BA 42 NAMING-COLLISION CONTRACT`` is the governing rule.

**The insular-opercular transition is not a classical BA territory.**
Brodmann's own scheme did not include an insular BA 42; the label used
here is a modern mapping convention for the more rostral posterior-
insula / operculum junction, extending the same convention that gives
us the insular BA 41. Modern parcellations (HCP 180-area, Öngür-Price,
Petrides-Pandya) subdivide this region under different labels (HCP:
``Ig``/``Id`` at the insular edge plus the ``OP`` series in the
operculum, with the rostral portion overlapping ``OP1``–``OP3``;
Öngür-Price: no discrete BA-42 analogue in the insula). **The package
must therefore carry an explicit ``PARCELATION_CONVENTION`` field**
documenting that "BA 42" here is a tree-architecture label, not a
classical architectonic entity.

The left BA 42 (insular-opercular transition) borders:

    caudally      BA 41 (insular-opercular transition, more caudal
                  component) — the other half of the insular
                  BA 41/42 pair
    rostrally     the posterior insular long gyri and the caudal
                  margin of BA 13 (middle insula)
    dorsally      the circular sulcus upper bank, and across it the
                  parietal operculum (S2 territory — NAMING
                  COLLISION boundary for the secondary somatosensory
                  cortex, but NOT a BA label collision)
    ventrally     the inferior limiting sulcus
    laterally     the temporal / parietal operculum (secondary
                  auditory and secondary somatosensory territories —
                  NAMING COLLISION with temporal BA 42)

**Left-hemisphere specificity**: the left BA 42 is the more rostral
insular-opercular transition territory most strongly coupled to
**multimodal opercular convergence** (somatosensory / nociceptive /
thermoreceptive / S2), the **language-linked evaluation** of
opercular somatosensory content, and the **parasympathetic** autonomic
coupling of opercular input. Left insular-opercular lesions can
produce **somatosensory-opercular integration deficits** — impaired
ability to name and describe opercular somatic sensations — which is
the language-linked mirror of the right's **affective-salience
opercular integration deficits**. On the nociceptive side, the left
BA 42 is weighted toward the **sensory-discriminative / language-
linked** aspect of opercular pain and temperature, while the right
BA 42 is weighted toward the **affective-motivational / arousal**
aspect.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours
        caudally               BA 41 (insular-opercular transition)
        rostrally              posterior insular long gyri / caudal
                               margin of BA 13
        dorsally               circular sulcus upper bank and parietal
                               operculum (S2 territory)
        ventrally              inferior limiting sulcus
        laterally              temporal / parietal operculum
                               (secondary auditory and secondary
                               somatosensory territories — NAMING
                               COLLISION with temporal BA 42)

    Functional overlays
        multimodal opercular convergence
            BA 42's **defining functional overlay** is the
            convergence of **somatosensory, nociceptive,
            thermoreceptive, and secondary-somatosensory (S2)**
            signals at the opercular transition. The territory is
            the insular-opercular analogue of the PGC's multimodal
            intraoral convergence — but for the **body surface**
            rather than the oral cavity. On the left, the
            convergence is weighted toward the **language-linked /
            naming** aspect of opercular somatic content; on the
            right, toward the **affective-salience / arousal**
            aspect.
        secondary somatosensory / opercular transition (primary)
            The parietal / temporal operculum component of BA 42's
            territory is **adjacent to and continuous with the
            secondary somatosensory cortex (S2)**, and BA 42 is the
            insular-opercular corridor through which S2 somatic
            signals reach the posterior insula. On the left, the
            S2 → BA 42 projection is weighted toward **verbal
            somatosensory discrimination**; on the right, toward
            **affective somatosensory appraisal**.
        primary nociceptive cortex (secondary)
            The posterior insula is the **primary nociceptive
            cortex**, and BA 42 is the more rostral transition
            component that extends the nociceptive representation
            toward the parietal operculum. On the left, BA 42's
            nociceptive contribution is weighted toward the
            **sensory-discriminative / language-linked** aspect of
            opercular pain; on the right, toward the
            **affective-motivational / arousal** aspect.
        primary thermoreceptive cortex (secondary)
            The posterior insula's **cool/warm topography** extends
            into BA 42's more rostral territory. On the left, the
            thermoreceptive contribution is weighted toward the
            **sensory-discriminative** discrimination of opercular
            thermal content; on the right, toward the
            **autonomic challenge** response.
        primary interoceptive cortex (secondary)
            The posterior insula's primary interoceptive territory
            extends into BA 42. On the left, the interoceptive
            contribution is weighted toward **sensory-discriminative
            opercular visceral content**; on the right, toward
            **autonomic-affective coupling**.
        auditory transition (naming-collision boundary)
            The temporal-operculum border of BA 42's territory is
            adjacent to the **secondary auditory cortex** (temporal
            BA 42, planum temporale). This is the **naming-collision
            boundary** — the insular BA 42 package ends where the
            temporal BA 42 package begins. Downstream code must not
            conflate the two.
        autonomic coupling (parasympathetic on the left)
            The opercular component of BA 42's territory drives
            **autonomic responses** to somatic and thermal input.
            On the **left**, the coupling is weighted toward
            **parasympathetic** outflow (vagal bradycardia,
            depressor responses, gastric modulation); on the right,
            toward sympathetic (pressor, tachycardic, peri-ictal
            sympathetic surge).

**This field is structurally identical to the right sibling's** — the
architectonic neighbours and functional overlays are the same on both
sides. What differs is the **emphasis** within the multimodal,
nociceptive, thermoreceptive, and autonomic overlays: the left BA 42
is weighted toward the **language-linked / sensory-discriminative /
parasympathetic** aspect; the right BA 42 is weighted toward the
**affective-salience / arousal / sympathetic** aspect.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 41 (insular-opercular transition)   caudal neighbour; the other
                                           half of the insular BA 41/42
                                           pair
    BA 13 (middle insula)                  rostral / dorsal neighbour;
                                           the granular-to-agranular
                                           transition from BA 13 to
                                           the posterior insula
    BA 14                                  distant rostral neighbour;
                                           no direct adjacency
    BA 16                                  distant rostral neighbour;
                                           no direct adjacency
    agranular posterior insula             ventromedial neighbour (not
                                           a distinct BA in the
                                           conventional scheme)
    temporal BA 42 (secondary auditory     lateral neighbour across the
    cortex)                                circular sulcus — NAMING
                                           COLLISION; must not be
                                           conflated
    temporal BA 41 (primary auditory       ventrolateral neighbour
    cortex)                                across the circular sulcus
                                           — NAMING COLLISION; must
                                           not be conflated
    parietal operculum / S2                dorsal neighbour across the
                                           circular sulcus; S2 is
                                           functionally continuous with
                                           BA 42's territory (the
                                           somatosensory-opercular
                                           transition) but is **not**
                                           a BA-numbered collision —
                                           the S2 territory is named
                                           functionally, not by BA
                                           number

**This field is byte-identical to the left sibling's** at the level of
BA-numbered neighbours. The **S2 / parietal operculum** entry is
notably **not** a BA numbering collision — S2 is a functional
designation, and the BA 42 label is only applied to the insular and
temporal territories, not to the S2 opercular territory.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 42 participates in **four** canonical insular domains on the left.
The emphasis is as follows:

    multimodal_integration                         (left emphasis — PRIMARY)
        **This is BA 42's dominant contribution on the left.** BA 42
        is the more rostral component of the insular-opercular
        transition — the territory where **somatosensory,
        nociceptive, thermoreceptive, and secondary-somatosensory
        (S2) signals** converge with insular input. On the left, the
        convergence is weighted toward the **language-linked /
        naming** aspect of opercular somatic content: left BA 42 is
        more strongly engaged during **verbal somatosensory
        discrimination tasks** and during the **naming of opercular
        somatic sensations**. The right BA 42 is weighted toward the
        **affective-salience / arousal** aspect of the same
        convergence.

    nociception_and_pain_affect                    (left emphasis — SECONDARY)
        BA 42 extends the primary nociceptive representation of the
        posterior insula toward the parietal operculum. On the left,
        the nociceptive contribution is weighted toward the
        **sensory-discriminative / language-linked** aspect of
        opercular pain — the "where and how intense" of pain that
        reaches the opercular surface. The left BA 42 is more
        strongly engaged during **verbal pain-rating tasks** and
        during the **localization of opercular pain**. The right
        BA 42 is weighted toward the **affective-motivational /
        arousal** aspect.

    thermoreception                                (left emphasis — SECONDARY)
        The posterior insula's **cool/warm topography** extends into
        BA 42's more rostral territory. On the left, the
        thermoreceptive contribution is weighted toward the
        **sensory-discriminative** discrimination of opercular
        thermal content. The right BA 42 is weighted toward the
        **autonomic challenge** aspect (cold pressor sympathetic
        surge).

    autonomic_control (parasympathetic)            (left emphasis)
        The opercular component of BA 42's territory drives
        **autonomic responses** to somatic and thermal input. On
        the left, the coupling is weighted toward **parasympathetic**
        outflow — vagal bradycardia, depressor responses, and gastric
        modulation during opercular somatic or thermal stimulation.
        The left BA 42 → hypothalamus and BA 42 → NST projections
        are part of this parasympathetic substrate. On the right,
        the same autonomic coupling is **sympathetic** (pressor,
        tachycardic, peri-ictal sympathetic surge).

**Left-specific caveat on `speech_articulation`.** BA 42 does **not**
carry the domain. The apraxia-of-speech territory is the **anterior**
insula (BA 13 / BA 16 / opercular transition), which is rostral to
BA 42's posterior transition zone. BA 42 is far from the critical
speech-articulation territory.

**Left-specific caveat on `vestibular_and_self_location`.** This
domain is **right-emphasized at BA 13**. The left BA 42 does **not**
carry it.

**Left-specific caveat on `gustatory`.** BA 42 is **not** a primary or
secondary taste area. The gustatory territory is anterior (BA 43,
area G, BA 14). BA 42's chemosensory contribution is **zero** — the
posterior transition zone does not participate in taste processing.

**Left-specific caveat on `salience_network` and `social_emotional`.**
These domains are **anterior insular** on both sides. The posterior
transition zone (including BA 42) is the **multimodal opercular
convergence** territory, not the salience hub. BA 42 does not carry
them.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → VPL / VPI (ventroposterior lateral / inferior)
            **BA 42's principal thalamic afferent.** The
            ventroposterior somatosensory nuclei relay the
            somatosensory and nociceptive input that BA 42
            integrates with the posterior insula's primary
            interoceptive and nociceptive territory.
        → VMpo (posterior ventromedial nucleus, parvicellular part)
            The VMpo → BA 42 projection is **weaker than the
            VMpo → BA 41 projection** — BA 42 is more rostral, and
            the primary nociceptive and thermoreceptive territory is
            concentrated in BA 41. On the left, the VMpo → BA 42
            contribution is weighted toward the sensory-
            discriminative / language-linked aspect of the
            nociceptive and thermoreceptive signals.
        → auditory thalamus (medial geniculate body, MGB)
            **The naming-collision afferent.** The MGB projects to
            the **temporal** BA 42 territory (secondary auditory
            cortex, planum temporale), NOT to the insular BA 42
            territory. The auditory thalamic projection does not
            enter the insular BA 42 package — the circular sulcus
            is the boundary. This entry is documented here only to
            pre-empt the conflation: **insular BA 42 does not
            receive MGB input; the auditory input terminates at the
            temporal BA 42 boundary.**

    cortical afferents
        → BA 41 (insular-opercular transition), left
            Reciprocal connections with the more caudal half of the
            insular BA 41/42 pair.
        → BA 13 (middle insula), left
            The granular-to-agranular transition from BA 13 to the
            posterior insula projects caudally into BA 42's
            territory, carrying the middle insular multimodal
            integration signal.
        → secondary somatosensory cortex (S2), left
            **BA 42's most distinctive cortical afferent.** The
            parietal operculum component of BA 42's territory
            receives S2 input, supporting the opercular convergence
            of somatosensory and nociceptive signals. On the left,
            the S2 → BA 42 projection is weighted toward verbal
            somatosensory discrimination.
        → primary somatosensory cortex (S1, area 3b/1/2), left
            Weak direct projections from S1 to BA 42 contribute to
            the opercular somatosensory convergence.
        → anterior insula (via intrainsular connections)
            BA 42 projects rostrally to the anterior insula,
            carrying the opercular multimodal signal that the
            anterior insula transforms into the full salience and
            affective response.

    subcortical efferents
        → hypothalamus (lateral hypothalamus), left
            **BA 42 → LH is part of the parasympathetic efferent
            pathway.** On the left, this projection is weighted
            toward parasympathetic outflow (vagal bradycardia,
            depressor responses during opercular somatic or thermal
            stimulation).
        → nucleus of the solitary tract (NST), left
            BA 42 projects to the NST, the brainstem relay for
            visceral afferents and the origin of vagal
            parasympathetic outflow.
        → periaqueductal gray (PAG)
            BA 42 → PAG projections support the descending
            modulation of pain and the autonomic-defensive response
            to opercular somatic input. On the left, the PAG
            projection is weighted toward the parasympathetic /
            vagal defensive response; on the right, toward the
            sympathetic defensive response.

    brainstem interactions
        → parabrachial nucleus (indirect via thalamus)
            The parabrachial → VPL/VPI → BA 42 pathway is the
            anatomical substrate of the opercular somatosensory
            convergence.

    callosal connections
        → right BA 42
            Interhemispheric coordination of the more rostral
            insular-opercular transition. The left → right traffic
            is weighted toward **language-linked / sensory-
            discriminative** opercular signals and
            **parasympathetic** autonomic signals; the right → left
            traffic is weighted toward **affective-salience** and
            **sympathetic** autonomic signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in three respects:
(a) the S2 → BA 42 and VPL/VPI → BA 42 pathways carry somatosensory
signals that the left uses for **language-linked** evaluation;
(b) the BA 42 → hypothalamus, BA 42 → NST, and BA 42 → PAG projections
are **parasympathetic** rather than sympathetic;
(c) the callosal traffic carries language-linked and parasympathetic
signals.

**The MGB entry is a naming-collision guard, not a real afferent.**
The medial geniculate body projects to the temporal BA 42 (secondary
auditory cortex), not to the insular BA 42. The ``CONNECTIVITY`` dict
documents this only to prevent a downstream conflation, and must tag
the entry as ``"naming_collision_boundary_not_insular_afferent"``.
**This entry is byte-identical to the left sibling's.**

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_ba42_multimodal_opercular_convergence
        **This is the left BA 42 anchor par excellence.** BA 42 is
        the more rostral component of the insular-opercular
        transition — the territory where somatosensory, nociceptive,
        thermoreceptive, and secondary-somatosensory (S2) signals
        converge with insular input. Left BA 42 is more strongly
        engaged during **verbal somatosensory discrimination tasks**
        and during the **naming of opercular somatic sensations**.
        Left BA 42 lesions can produce **somatosensory-opercular
        integration deficits** — impaired ability to name and
        describe opercular somatic content — while the underlying
        sensory detection is intact.

    left_ba42_sensory_discriminative_opercular_pain
        BA 42 extends the primary nociceptive representation of
        the posterior insula toward the parietal operculum. On the
        left, BA 42's nociceptive contribution is weighted toward
        the **sensory-discriminative / language-linked** aspect of
        opercular pain. Left BA 42 lesions can produce **impaired
        localization and verbal description** of opercular pain,
        while the affective response remains intact. This is the
        more rostral analogue of the left BA 41's sensory-
        discriminative pain anchor.

    left_ba42_operculo_insular_stroke
        Posterior insular-opercular strokes involving BA 42 can
        produce **central post-stroke pain** with the
        **sensory-discriminative** component more prominent on the
        left. The combination of opercular somatosensory loss with
        insular pain may produce a **dissociated opercular sensory
        syndrome** — the patient can still feel that something is
        wrong but cannot describe what — and this presentation is
        more common after left BA 42 lesions than right.

    left_ba42_parasympathetic_autonomic_coupling
        Left BA 42's opercular somatic and thermal activity drives
        **parasympathetic** autonomic responses — vagal
        bradycardia, depressor responses, and gastric modulation
        during opercular stimulation. Left BA 42 lesions can
        produce **parasympathetic dysregulation** in these
        responses, distinct from the right BA 42's sympathetic
        signature (pressor, tachycardic).

    insular_opercular_transition_glioma
        Because BA 42 is a **buried transition territory** at the
        junction of the posterior insula and the parietal /
        temporal operculum, resecting a left insular / opercular
        glioma in the BA 42 zone requires careful mapping of
        somatosensory, nociceptive, thermoreceptive, autonomic,
        and auditory function. **The naming collision is a
        surgical hazard**: the surgeon must not confuse the
        insular-opercular BA 42 territory with the temporal BA 42
        (secondary auditory cortex, planum temporale) territory.
        Left BA 42 resections risk **somatosensory-opercular
        integration deficits**, **sensory-discriminative pain
        deficits**, and **parasympathetic dysregulation**.

    insular_opercular_epilepsy_naming_collision_hazard
        Seizures arising from the insular-opercular transition zone
        can present with **opercular somatosensory auras** or
        **thermal auras** that the patient may describe as
        originating from the contralateral body surface. **The
        naming collision with temporal BA 42 is a semiological
        hazard**: an insular-opercular seizure with an auditory
        aura (from spread to temporal BA 42, planum temporale) may
        be mistaken for a purely insular seizure, and vice versa.
        Pre-surgical workup must distinguish the two territories
        explicitly.

    autonomic_stress_vulnerability_sudep
        Posterior insular-opercular dysfunction may contribute to
        **SUDEP** (sudden unexpected death in epilepsy) through the
        cortical control of cardio-respiratory autonomic function.
        On the **left**, the parasympathetic weighting of BA 42's
        autonomic coupling is **protective-weighted** rather than
        arrhythmogenic — the right BA 42's sympathetic weighting
        is the more directly arrhythmogenic side, as documented
        in the right sibling.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 42 autonomic contribution is parasympathetic (right
is sympathetic), and the left BA 42's SUDEP contribution is
protective-weighted rather than arrhythmogenic;
(b) the left BA 42's multimodal, nociceptive, and thermoreceptive
contributions are weighted toward the **language-linked /
sensory-discriminative** aspect (right is affective-salience /
arousal). The right sibling's docstring carries the corresponding
right-sided anchors.

**The naming-collision hazard is a left-and-right invariant** — it is
documented identically in both packages and in the parent registry's
``BA 41 / BA 42 NAMING-COLLISION CONTRACT``.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left insular BA registry. This package's parent, source of
    the ``NAMING_COLLISIONS`` entry for BA 42, and enforcer of the
    ``speech_articulation`` exclusion.

..brodmann_area_41_posterior_insula
    Caudal neighbour — the other half of the insular BA 41/42 pair.
    Where BA 41 is the more caudal transition component (adjacent to
    the planum temporale and the primary nociceptive/thermoreceptive
    territory), BA 42 is the more rostral component (adjacent to the
    parietal operculum and S2).

..brodmann_area_13_middle_insula
    Rostral / dorsal neighbour via the granular-to-agranular
    transition. BA 13's multimodal integration signal is carried
    caudally into BA 42's opercular convergence territory.

..brodmann_area_14
    Distant rostral neighbour — no direct adjacency.

..brodmann_area_16
    Distant rostral neighbour — no direct adjacency.

..brodmann_area_43_anterior_insula
    Rostroventral neighbour — no direct adjacency (the middle
    insula intervenes). BA 42 is **not** a taste area.

...primary_gustatory_cortex
    The **functional-field sibling** (one level up, under
    ``..insular``). BA 42 is **not** part of the PGC's cortical
    territories — the PGC is anterior, BA 42 is posterior. There is
    no overlap between the two.

..cortex.temporal.brodmann_areas.brodmann_area_42
    **The naming-collision source.** The temporal BA 42 package
    describes the secondary auditory cortex (planum temporale). It
    is a **different territory**, and both packages must carry a
    ``NAMING_COLLISION_WITH`` field naming the other. **No
    downstream code may resolve "BA 42" without a lobe qualifier.**

..cortex.temporal.brodmann_areas.brodmann_area_41
    The other temporal auditory territory — cross-referenced here
    for completeness (the temporal BA 41 / insular BA 41 collision
    is documented in the sibling insular BA 41 package, not here).

..cortex.parietal
    The parietal operculum (S2 territory) is functionally continuous
    with BA 42's opercular component across the circular sulcus.
    The parietal package must declare the insula as a hidden
    neighbour, and must note that **the S2 territory is named
    functionally, not by BA number** — there is no BA numbering
    collision between the insular BA 42 and the S2 opercular
    territory.

..cortex.temporal
    The temporal lobe parent. Its ``..sulci.circular_sulcus`` (or the
    equivalent limiting sulcus package) is the anatomical boundary
    between the insular BA 42 territory and the temporal BA 42
    territory. The temporal parent must document the naming
    collision on its side.

..cortex.frontal
    The frontal operculum covers the anterior insula, not the
    posterior transition zone. BA 42 does not border the frontal
    operculum directly. Recorded here to pre-empt a false
    cross-reference.

../../subcortical/diencephalon/thalamus
    The **VPL / VPI** thalamic nuclei are BA 42's principal
    afferents (somatosensory). The thalamus package must declare
    VPL / VPI as cortical afferents to the left BA 42. It must
    **not** declare the medial geniculate body (MGB) as an
    afferent to the insular BA 42 — MGB projects to the temporal
    BA 42, not to the insular BA 42.

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem relay that feeds
    VPL / VPI and thus BA 42. It is part of the somatosensory and
    nociceptive ascending pathway.

../../subcortical/diencephalon/hypothalamus
    The left BA 42 → left hypothalamus projection supports
    **parasympathetic** autonomic coupling to opercular somatic
    and thermal input. The hypothalamus package must declare the
    left BA 42 as a cortical afferent.

../../brainparts/hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
    The **nucleus of the solitary tract (NST)** receives left BA 42
    projections and is the origin of vagal parasympathetic outflow.
    The NST package must declare the left BA 42 as a cortical
    afferent.

../../brainparts/midbrain/tegmentum/periaqueductal_gray
    The periaqueductal gray receives left BA 42 projections
    supporting descending pain modulation and the autonomic-
    defensive response. On the left, the PAG projection is
    weighted toward the parasympathetic / vagal defensive
    response.

../../right/cortex/insular/brodmann_areas/brodmann_area_42_posterior_insula
    The right-hemisphere homologue. Structural fields (BA number,
    region label, **naming-collision field**, **parcellation-
    convention field**, **MGB guard entry**, architectonic
    neighbourhoods, BA-to-neighbour adjacency, FUNCTIONAL_DOMAINS
    set) MUST be byte-identical. Functional emphasis and clinical
    significance diverge — the left BA 42 is weighted toward
    language-linked opercular convergence, sensory-discriminative
    opercular pain, parasympathetic autonomic coupling, and
    protective-weighted SUDEP; the right BA 42 is weighted toward
    affective-salience opercular convergence,
    affective-motivational opercular pain, sympathetic autonomic
    coupling, and arrhythmogenic-weighted SUDEP.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_42_posterior_insula"
    HEMISPHERE          = "left"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 42   # IN THE INSULAR SENSE — not the
                               # auditory BA 42
    INSULAR_REGION      = "insular_opercular_transition"
    CYTOTECTONIC_GRADIENT = "agranular_to_dysgranular"

    NAMING_COLLISION_WITH = (
        "temporal.brodmann_areas.brodmann_area_42",
    )
        # **Byte-identical to the right sibling's.** The naming
        # collision is a property of the BA numbering scheme, not
        # of the hemisphere.

    PARCELATION_CONVENTION = (
        "Brodmann's classical scheme does not include an insular "
        "BA 42. The 'BA 42' label here is a modern parcellation "
        "convention for the more rostral insular-opercular "
        "transition zone at the posterior-insula / parietal-"
        "temporal-operculum junction. It is NOT the secondary "
        "auditory BA 42 of the planum temporale. Modern schemes "
        "(HCP 180-area, Ongur-Price, Petrides-Pandya) subdivide "
        "this region under different labels."
    )
        # **Byte-identical to the right sibling's.**

    MGB_AFFERENT_GUARD = (
        "The medial geniculate body (MGB) does NOT project to the "
        "insular BA 42. MGB projects to the temporal BA 42 "
        "(secondary auditory cortex, planum temporale). The "
        "circular sulcus is the boundary. Any downstream code that "
        "queries auditory afferents to 'BA 42' must specify the "
        "lobe."
    )
        # **Byte-identical to the right sibling's.**

    S2_FUNCTIONAL_CONTINUITY_NOTE = (
        "The parietal operculum (S2 territory) is functionally "
        "continuous with BA 42's opercular component across the "
        "circular sulcus, but S2 is named functionally, not by BA "
        "number. There is NO BA numbering collision between the "
        "insular BA 42 and the S2 opercular territory. The S2 "
        "label is a functional designation; the BA 42 label is "
        "applied only to the insular and temporal territories."
    )
        # **Byte-identical to the right sibling's.** Documents
        # that the S2 adjacency is functional, not a numbering
        # collision.

    FUNCTIONAL_DOMAINS  = (
                              "multimodal_integration",   # primary
                              "nociception_and_pain_affect",
                              "thermoreception",
                              "interoception",         # secondary
                              "autonomic_control",     # left:
                                                       # parasympathetic
                              # NOTE: speech_articulation is
                              # EXCLUDED (anterior insular
                              # territory; BA 42 is posterior).
                              # NOTE: vestibular_and_self_location
                              # is EXCLUDED (right-emphasized at
                              # BA 13).
                              # NOTE: gustatory is EXCLUDED (BA 42
                              # is not a taste area).
                              # NOTE: salience_network and
                              # social_emotional are EXCLUDED
                              # (anterior insular territories;
                              # BA 42 is posterior multimodal
                              # opercular convergence).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "multimodal_integration":
                                  "language_linked_somatosensory_"
                                  "opercular_convergence_naming",
                              "nociception_and_pain_affect":
                                  "sensory_discriminative_language_"
                                  "linked_opercular_pain",
                              "thermoreception":
                                  "sensory_discriminative_opercular_"
                                  "thermal_left_weighted",
                              "interoception":
                                  "posterior_opercular_interoceptive_"
                                  "sensory_discriminative",
                              "autonomic_control":
                                  "parasympathetic_vagal_bradycardia_"
                                  "depressor_opercular_coupling",
                          }

    MODERN_CROSSWALK    = {   # BA 42 (insular) → modern labels
                              "HCP_180":       ("Ig", "Id", "OP1",
                                                "OP3"),
                              "Ongur_Price_2000": ("Ial", "Iapm",
                                                   "Iapl"),
                              "Petrides_Pandya":  ("Ig", "Id", "OP1",
                                                   "OP3"),
                          }
        # **Byte-identical to the right sibling's.**

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_ba42_multimodal_opercular_"
                              "convergence",
                              "left_ba42_sensory_discriminative_"
                              "opercular_pain",
                              "left_ba42_operculo_insular_stroke",
                              "left_ba42_parasympathetic_autonomic_"
                              "coupling",
                              "insular_opercular_transition_"
                              "glioma",
                              "insular_opercular_epilepsy_naming_"
                              "collision_hazard",
                              "autonomic_stress_vulnerability_"
                              "sudep",
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
        "PARCELATION_CONVENTION",
        "MGB_AFFERENT_GUARD",
        "S2_FUNCTIONAL_CONTINUITY_NOTE",
        "FUNCTIONAL_DOMAINS",
        "DOMAIN_EMPHASIS",
        "MODERN_CROSSWALK",
        "CONNECTIVITY",
        "CLINICAL_ANCHORS",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references BA 42 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are no forward-declaration caveats for this package's own
structural fields.** BA 42 is a sibling of BA 41, and its BA-numbered
neighbours (BA 41, BA 13, BA 14, BA 16, BA 43) all exist as packages
under ``..brodmann_areas``. Its functional-field sibling ``...
primary_gustatory_cortex`` exists under ``..insular``. Its cortical
and subcortical targets exist or are being built out in parallel.

**The temporal BA 42 package is a required cross-package reference,
not a forward reference.** The temporal BA 42 (planum temporale)
package exists or will exist under ``temporal/brodmann_areas/``, and
the naming-collision contract requires both packages to carry
reciprocal ``NAMING_COLLISION_WITH`` fields. If the temporal BA 42
does not yet exist when this package is created, the temporal package
must be created with the reciprocal field in the same commit — **the
collision must not be left half-declared**.

**The circular sulcus package is a required cross-package reference.**
The anatomical boundary between the insular BA 42 territory and the
temporal BA 42 territory (and the boundary between BA 42's opercular
component and the S2 parietal operculum) is the **circular sulcus**
(limiting sulcus, sulcus circularis). The circular sulcus package —
either ``..sulci.circular_sulcus`` under the insular parent, or a
shared sulcus package if the sulcus is modelled at the cortex level —
must declare itself as the naming-collision boundary. The two BA 42
packages (insular, temporal) must cross-reference it on both sides.

**The S2 continuity note is a structural field, not a forward
reference.** S2 is functionally continuous with BA 42's opercular
component but is named functionally, not by BA number. The
``S2_FUNCTIONAL_CONTINUITY_NOTE`` field must be present and
byte-identical to the right sibling's, and the ``cortex.parietal``
package must cross-reference it from its own side.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 42 is a **transition territory** and is not internally subdivided
in the classical scheme. If a future parcellation nevertheless decides
to split it into an **insular component** and an **opercular
component** (following the territory's cross-circular-sulcus extent),
the promotion takes this form:

    brodmann_area_42_posterior_insula/
        __init__.py
        insular_component/
            __init__.py
        opercular_component/
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The opercular component must not be merged with the temporal
BA 41 / BA 42 packages.** The opercular component of insular BA 42
is the *operculum* of the insular-opercular transition, not the
planum temporale's secondary auditory cortex. The temporal packages
describe the auditory cortex on the superior surface; the insular
BA 42 opercular component describes the cortex on the opercular
surface. They are adjacent across the circular sulcus but distinct.

**The opercular component's S2 adjacency must be preserved through
any split.** The S2 functional continuity note (`S2_FUNCTIONAL_
CONTINUITY_NOTE`) must be carried at the parent level and, if the
opercular component is promoted, must also be declared by the
opercular sub-package. The S2 territory is not BA-numbered and is
not a naming collision — the note documents that fact.

**No split should be performed while the circular sulcus boundary
package does not yet exist.** Splitting the insular BA 42 into
insular and opercular components without an explicit boundary
package would multiply unresolved references and make the
naming-collision contract harder to enforce.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_42_posterior_insula``:

    MUST be identical (byte-for-byte):
        AREA_NAME                      "brodmann_area_42_posterior_insula"
        LOBE                           "insular"
        BRODMANN_NUMBER                42 (insular sense)
        INSULAR_REGION                 "insular_opercular_transition"
        CYTOTECTONIC_GRADIENT          "agranular_to_dysgranular"
        NAMING_COLLISION_WITH          ("temporal.brodmann_areas."
                                       "brodmann_area_42",) —
                                       byte-identical
        PARCELATION_CONVENTION         byte-identical
        MGB_AFFERENT_GUARD             byte-identical
        S2_FUNCTIONAL_CONTINUITY_NOTE  byte-identical — S2 is a
                                       functional designation, not a
                                       BA-numbered territory
        Architectonic neighbourhoods
        BA-to-neighbour adjacency (including the circular-sulcus
                                       boundary)
        MODERN_CROSSWALK               byte-identical
        FUNCTIONAL_DOMAINS set         the same five domains, with
                                       the same exclusions
        SUBDIVISIONS                   both empty (or both non-empty
                                       in the same way, if a split
                                       is ever done)
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        DOMAIN_EMPHASIS        left: multimodal_integration is
                               "language_linked_somatosensory_
                               opercular_convergence_naming";
                               nociception is "sensory_discriminative_
                               language_linked_opercular_pain";
                               thermoreception is "sensory_
                               discriminative_opercular_thermal_
                               left_weighted"; interoception is
                               "posterior_opercular_interoceptive_
                               sensory_discriminative";
                               autonomic_control is "parasympathetic_
                               vagal_bradycardia_depressor_
                               opercular_coupling".
                               right: multimodal_integration is
                               "affective_salience_opercular_
                               convergence_arousal"; nociception is
                               "affective_motivational_arousal_
                               opercular_pain"; thermoreception is
                               "opercular_thermal_autonomic_
                               challenge_sympathetic"; interoception
                               is "posterior_opercular_interoceptive_
                               autonomic_affective_coupling";
                               autonomic_control is "sympathetic_
                               pressor_tachycardic_opercular_
                               coupling".
        CONNECTIVITY           same bundle names; left: S2 → BA 42 is
                               weighted toward verbal somatosensory
                               discrimination; BA 42 → hypothalamus /
                               NST / PAG is parasympathetic; callosal
                               traffic carries language-linked and
                               parasympathetic signals.
                               right: S2 → BA 42 is weighted toward
                               affective somatosensory appraisal;
                               BA 42 → hypothalamus / NST / PAG is
                               sympathetic; callosal traffic carries
                               affective-salience and sympathetic
                               signals.
        CLINICAL_ANCHORS       left: seven anchors (multimodal
                               opercular convergence with language-
                               linked emphasis, sensory-discriminative
                               opercular pain, operculo-insular
                               stroke with sensory-discriminative
                               emphasis, parasympathetic coupling,
                               glioma resection, epilepsy naming-
                               collision hazard, **SUDEP protective-
                               weighted**).
                               right: seven or eight anchors
                               (affective-salience opercular
                               convergence, affective-motivational
                               opercular pain, operculo-insular stroke
                               with affective emphasis, sympathetic
                               coupling, glioma resection, epilepsy
                               naming-collision hazard, **SUDEP
                               arrhythmogenic-weighted**, and possibly
                               thermoreceptive autonomic challenge).

**The `DOMAIN_EMPHASIS` asymmetry is the sharpest single entry in this
contract.** Both hemispheres carry the same five domains and both
exclude the same four, but the emphasis within every shared domain
points in opposite directions: the left BA 42 is the
**language-linked / sensory-discriminative / parasympathetic**
territory, the right BA 42 is the **affective-salience / arousal /
sympathetic** territory.

**The SUDEP asymmetry is the second sharpest entry.** Both hemispheres
carry a SUDEP anchor, but they **point in opposite directions**: the
left BA 42 is **protective-weighted** (parasympathetic coupling);
the right BA 42 is **arrhythmogenic-weighted** (sympathetic coupling).
The two anchors must not be copied verbatim between the packages.

**The naming-collision fields, the MGB guard, the parcellation
convention, and the S2 continuity note are byte-identical on both
sides** and must not be allowed to drift. They are properties of the
BA numbering scheme and the opercular anatomy, not of the hemisphere.

**The BA 42 FUNCTIONAL_DOMAINS set is NOT identical to BA 41's.**
BA 42 adds `multimodal_integration` as its primary domain, reflecting
its more rostral position adjacent to S2 and the parietal operculum.
BA 41's primary domain is `nociception_and_pain_affect`, reflecting
its more caudal position adjacent to the primary nociceptive and
thermoreceptive territory. The two siblings are functionally distinct
even though both are "insular-opercular transition" packages.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_42_posterior_insula".
[ ] HEMISPHERE is "left".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 42 — the **insular** BA 42, not the
    auditory BA 42.
[ ] INSULAR_REGION is "insular_opercular_transition".
[ ] CYTOTECTONIC_GRADIENT is "agranular_to_dysgranular".
[ ] **NAMING_COLLISION_WITH** is
    ``("temporal.brodmann_areas.brodmann_area_42",)`` and is
    byte-identical to the right sibling's.
[ ] **PARCELATION_CONVENTION** is present, byte-identical to the
    right sibling's — the "BA 42" label here is a modern
    parcellation convention for the more rostral
    insular-opercular transition, not a classical architectonic
    entity.
[ ] **MGB_AFFERENT_GUARD** is present, byte-identical to the right
    sibling's — the medial geniculate body projects to the temporal
    BA 42 (planum temporale), not to the insular BA 42.
[ ] **S2_FUNCTIONAL_CONTINUITY_NOTE** is present, byte-identical to
    the right sibling's — S2 is named functionally, not by BA
    number, and there is no numbering collision between insular
    BA 42 and the S2 parietal operculum.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - multimodal_integration  (PRIMARY on BA 42, not on BA 41)
    - nociception_and_pain_affect
    - thermoreception
    - interoception
    - autonomic_control
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation
    (anterior insular; BA 42 is posterior).
[ ] FUNCTIONAL_DOMAINS **excludes** vestibular_and_self_location
    (right-emphasized at BA 13, not BA 42).
[ ] FUNCTIONAL_DOMAINS **excludes** gustatory (BA 42 is not a
    taste area).
[ ] FUNCTIONAL_DOMAINS **excludes** salience_network and
    social_emotional (anterior insular territories; BA 42 is
    posterior multimodal opercular convergence).
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis** per domain:
    - multimodal_integration → language_linked_somatosensory_
      opercular_convergence_naming
    - nociception → sensory_discriminative_language_linked_
      opercular_pain
    - thermoreception → sensory_discriminative_opercular_thermal_
      left_weighted
    - interoception → posterior_opercular_interoceptive_sensory_
      discriminative
    - autonomic_control → parasympathetic_vagal_bradycardia_
      depressor_opercular_coupling
[ ] MODERN_CROSSWALK is present, byte-identical to the right
    sibling's, and documents that the insular-opercular transition
    is captured by modern labels like Ig, Id, and the OP series.
[ ] CONNECTIVITY documents:
    - VPL / VPI thalamic afferent (primary somatosensory relay)
    - VMpo thalamic afferent (secondary, weaker than BA 41's)
    - **MGB entry with the "naming_collision_boundary_not_insular_
      afferent" tag** (guard against conflation; byte-identical to
      the right)
    - BA 41 and BA 13 intracortical afferents
    - S2 → BA 42 afferent (weighted toward verbal somatosensory
      discrimination on the left)
    - S1 → BA 42 weak afferent (opercular somatosensory
      convergence)
    - BA 42 → anterior insula intrainsular afferent
    - BA 42 → hypothalamus (parasympathetic, left-specific)
    - BA 42 → NST (parasympathetic, left-specific)
    - BA 42 → PAG (parasympathetic-weighted on the left)
    - parabrachial → BA 42 pathway
    - callosal traffic to right BA 42 (language-linked and
      parasympathetic, left-specific)
[ ] CLINICAL_ANCHORS contains the seven left-specific anchors:
    - left_ba42_multimodal_opercular_convergence
    - left_ba42_sensory_discriminative_opercular_pain
    - left_ba42_operculo_insular_stroke
    - left_ba42_parasympathetic_autonomic_coupling
    - insular_opercular_transition_glioma
    - insular_opercular_epilepsy_naming_collision_hazard
    - autonomic_stress_vulnerability_sudep (protective-weighted)
[ ] The **left multimodal opercular convergence** is documented as
    the primary left BA 42 anchor — the language-linked naming of
    opercular somatic content — and is distinguished from BA 41's
    primary nociceptive/thermoreceptive role.
[ ] The **naming-collision hazard** is documented as a **surgical
    and semiological hazard** — the surgeon must not confuse the
    insular BA 42 with the temporal BA 42 (planum temporale), and
    pre-surgical workup must distinguish them.
[ ] The **SUDEP protective weighting** on the left is documented as
    the mirror of the right's arrhythmogenic weighting, and the two
    anchors are not copied verbatim between the packages.
[ ] The **BA 42 ≠ BA 41** distinction is documented: BA 41 is the
    more caudal transition component (primary nociceptive /
    thermoreceptive / interoceptive), BA 42 is the more rostral
    component (multimodal opercular convergence adjacent to S2 and
    the parietal operculum). The FUNCTIONAL_DOMAINS sets differ
    (BA 42 adds `multimodal_integration` as primary).
[ ] The **BA 42 ≠ BA 13 / BA 14 / BA 16 / BA 43** distinction is
    documented: BA 42 is the posterior transition territory, not an
    anterior insular associative territory.
[ ] The **BA 42 ≠ PGC** distinction is documented: BA 42 is
    posterior (somatosensory / nociceptive / thermoreceptive /
    interoceptive); the PGC is anterior (gustatory). No overlap.
[ ] The **BA 42 (insular) ≠ BA 42 (temporal)** distinction is
    documented exhaustively: parcellation convention, MGB guard,
    naming-collision field, circular-sulcus boundary, surgical
    hazard, semiological hazard.
[ ] The **S2 functional continuity** is documented — S2 is not a
    BA numbering collision, and the S2_FUNCTIONAL_CONTINUITY_NOTE
    field is present and byte-identical to the right sibling's.
[ ] The **reciprocal NAMING_COLLISION_WITH field** is expected on
    the temporal BA 42 package, and the two packages must be
    created / updated in the same commit — the collision must not
    be left half-declared.
[ ] The **circular sulcus boundary package** is cross-referenced
    as the anatomical locus of the naming-collision boundary.
[ ] No SUBDIVISIONS promotion is performed while the circular
    sulcus boundary package does not yet exist.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, NAMING_COLLISION_
    WITH, PARCELATION_CONVENTION, MGB_AFFERENT_GUARD, S2_
    FUNCTIONAL_CONTINUITY_NOTE, architectonic neighbourhoods,
    modern crosswalk, FUNCTIONAL_DOMAINS set, forward-declaration
    caveat text) match the right sibling; DOMAIN_EMPHASIS,
    CONNECTIVITY emphasis, and CLINICAL_ANCHORS deliberately differ.
[ ] **The SUDEP asymmetry is verified**: the left BA 42 carries a
    protective-weighted anchor, the right BA 42 carries an
    arrhythmogenic-weighted anchor, and neither has been copied
    verbatim from the other.
[ ] Any downstream code that queries "BA 42" must specify the lobe
    — the temporal and insular packages are never conflated, and
    no global BA index merges them.
[ ] Any downstream code that queries auditory afferents to "BA 42"
    must specify the temporal BA 42 — the MGB guard is enforced.
[ ] Any downstream code that queries opercular somatosensory
    afferents must route through the S2 functional designation, not
    through a BA number — the S2_FUNCTIONAL_CONTINUITY_NOTE is
    enforced.
[ ] Any downstream code assigning BA 42 autonomic function must
    route through DOMAIN_EMPHASIS and must weight the left BA 42
    toward **parasympathetic** and the right BA 42 toward
    **sympathetic**.
[ ] Any downstream code querying BA 42 SUDEP contribution must
    weight the left BA 42 as **protective-weighted** and the right
    BA 42 as **arrhythmogenic-weighted** — the two hemispheres
    contribute opposite-direction autonomic influences, and
    averaging them would erase the lateralized signal.
"""