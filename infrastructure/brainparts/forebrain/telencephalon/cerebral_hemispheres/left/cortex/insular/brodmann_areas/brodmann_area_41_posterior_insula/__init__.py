"""
Brodmann Area 41 (Posterior Insula / Insular-Opercular Transition) — Left Hemisphere
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
                                    └── brodmann_area_41_posterior_insula   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 41 in its insular-opercular-transition sense** — the
cortex at the junction of the posterior insula and the temporal
operculum, across the circular sulcus. It is **not** the auditory
cortex, and the naming collision with ``temporal.brodmann_areas.
brodmann_area_41`` is the package's defining structural concern (see
below).

Parent: ``..brodmann_areas`` (left insular BA registry) — sibling to
BA 13, BA 14, BA 16, BA 42, BA 43.

This package is the **structural mirror** of
``../../right/cortex/insular/brodmann_areas/brodmann_area_41_posterior_insula``.
The BA number, the naming-collision field, the region label, and the
insular-opercular-transition gradient are identical on both sides; the
**functional emphasis** and **clinical significance** diverge — on the
left, BA 41's transition-zone territory is weighted toward the
**sensory-discriminative** nociceptive and thermoreceptive components,
the **parasympathetic** autonomic coupling of pain and temperature, and
the **language-linked** evaluation of pain quality.

--------------------------------------------------------------------------------
WHAT BA 41 IS — IN THE INSULAR CONTEXT
--------------------------------------------------------------------------------

Classically, **BA 41 is the primary auditory cortex** — the transverse
temporal gyrus (Heschl's gyrus) on the superior surface of the temporal
lobe. That is the temporal BA 41 package's territory.

In **this** tree, ``brodmann_area_41_posterior_insula`` names the
**insular-opercular transition zone** — the cortex where the posterior
insula meets the temporal operculum across the circular sulcus. The
choice to reuse the "BA 41" label for this territory is a
**parcellation convention**, not a claim that the two territories are
the same. They are not:

    temporal BA 41      = primary auditory cortex (Heschl's gyrus)
    insular BA 41       = insular-opercular transition (posterior
                          insula + temporal operculum junction)

The two packages must never be merged, and no global BA index may
resolve "BA 41" without a lobe qualifier. The parent registry's
``BA 41 / BA 42 NAMING-COLLISION CONTRACT`` is the governing rule.

**The insular-opercular transition is not a classical BA territory.**
Brodmann's own scheme did not include an insular BA 41 or BA 42; the
labels used here are a modern mapping convention for the
posterior-insula / operculum junction. Modern parcellations (HCP
180-area, Öngür-Price, Petrides-Pandya) subdivide this region under
different labels (HCP: ``Ig``/``Id`` at the insular edge plus ``OP``
series in the operculum; Öngür-Price: no discrete BA-41 analogue in the
insula). **The package must therefore carry an explicit
``PARCELATION_CONVENTION`` field** documenting that "BA 41" here is a
tree-architecture label, not a classical architectonic entity.

The territory this package describes **overlaps** the posterior
insula proper — the granular/dysgranular cortex behind the central
insular sulcus, which is the **primary interoceptive and nociceptive
cortex** . It also extends
laterally across the circular sulcus into the temporal operculum,
where it meets the auditory and secondary somatosensory territories of
the superior temporal plane. The **transition character** is the
package's defining feature: this is cortex at the intersection of
interoception, nociception, thermoreception, and audition, not cortex
belonging cleanly to any one of them.

The left BA 41 (insular-opercular transition) borders:

    rostrally     BA 42 (insular-opercular transition, more rostral
                  component) — forward reference if not yet built
    caudally      the agranular posterior insula and the planum
                  temporale (auditory territory, temporal BA 41/42 —
                  NAMING COLLISION)
    dorsally      the circular sulcus upper bank
    ventrally     the inferior limiting sulcus
    medially      the posterior insular long gyri

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours
        rostrally              BA 42 (insular-opercular transition)
        caudally               agranular posterior insula
        dorsally               circular sulcus upper bank
        ventrally              inferior limiting sulcus
        laterally              temporal operculum (auditory and
                               secondary somatosensory territories —
                               NAMING COLLISION with temporal BA 41)

    Functional overlays
        primary nociceptive cortex
            The posterior insula — including this transition
            territory — is the **primary nociceptive cortex**
            . Nociceptive-specific
            neurons are concentrated here, and the posterior
            insula's activity scales with **pain intensity**
            (the sensory-discriminative component), while the
            anterior insula carries the affective-motivational
            component. BA 41's transition-zone location means it
            participates in the **sensory-discriminative** side of
            this split.
        primary thermoreceptive cortex
            The posterior insula contains a **cool/warm
            topography** — distinct thermoreceptive subregions for
            innocuous cooling and warming. BA 41's transition-zone
            territory participates in this thermoreceptive
            representation.
        primary interoceptive cortex
            The posterior insula is the **primary interoceptive
            cortex** — the cortical recipient of lamina I
            spinothalamocortical and vagal afferents relayed via
            VMpo and other thalamic nuclei. BA 41's transition-zone
            location means it participates in the
            interoceptive-nociceptive convergence.
        secondary somatosensory / opercular transition
            The temporal operculum component of BA 41's territory
            borders the **secondary somatosensory cortex (S2)** and
            participates in the opercular convergence of
            somatosensory, nociceptive, and auditory signals.
        auditory transition (naming-collision boundary)
            The temporal-operculum border of BA 41's territory is
            adjacent to the **primary and secondary auditory
            cortex** (temporal BA 41/42). This is the **naming-
            collision boundary** — the insular BA 41 package ends
            where the temporal BA 41 package begins. Downstream
            code must not conflate the two.
        autonomic coupling (parasympathetic on the left)
            The posterior insula's nociceptive and thermoreceptive
            activity drives **autonomic responses** to pain and
            temperature. On the **left**, the coupling is weighted
            toward **parasympathetic** outflow (vagal
            bradycardia, depressor responses); on the right, toward
            sympathetic (pressor, tachycardic).

**This field is structurally identical to the right sibling's** — the
architectonic neighbours and functional overlays are the same on both
sides. What differs is the **emphasis** within the autonomic,
nociceptive-affective, and thermoreceptive overlays: the left BA 41 is
weighted toward **parasympathetic** autonomic coupling and the
**sensory-discriminative / language-linked** pain evaluation; the right
BA 41 is weighted toward **sympathetic** autonomic coupling and the
**affective-motivational / arousal** pain response.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 42 (insular-opercular transition)   rostral neighbour; the other
                                           half of the insular BA 41/42
                                           pair
    BA 13 (middle insula)                  rostral / dorsal neighbour;
                                           the granular-to-agranular
                                           transition from BA 13 to
                                           the posterior insula
    BA 14                                  distant rostral neighbour;
                                           no direct adjacency (BA 13
                                           and BA 16 intervene)
    agranular posterior insula             caudal neighbour (not a
                                           distinct BA in the
                                           conventional scheme)
    temporal BA 41 (primary auditory       lateral neighbour across the
    cortex)                                circular sulcus — NAMING
                                           COLLISION; must not be
                                           conflated
    temporal BA 42 (secondary auditory     lateral neighbour across the
    cortex)                                circular sulcus — NAMING
                                           COLLISION; must not be
                                           conflated

**This field is structurally identical to the right sibling's.** The
adjacency relationships are topological, not lateralized, and the
naming-collision neighbours (temporal BA 41/42) are the same on both
sides.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 41 participates in **four** canonical insular domains on the left.
The emphasis is as follows:

    nociception_and_pain_affect                    (left emphasis — PRIMARY)
        **This is BA 41's dominant contribution on the left.** The
        posterior insula is the **primary nociceptive cortex**, and
        BA 41's transition-zone territory carries the
        **sensory-discriminative** component — the
        "where and how intense" of pain — while the anterior
        insula carries the affective-motivational component. On the
        left, the emphasis is on the **sensory-discriminative /
        language-linked** aspect: left BA 41 lesions produce
        **impaired pain localization and quality discrimination**,
        and the left posterior insula is more strongly engaged
        during **verbal pain-rating tasks**. The affective-
        motivational / arousal aspect is weighted more toward the
        right.

    thermoreception                                (left emphasis)
        The posterior insula contains a **cool/warm topography**,
        and BA 41's transition-zone territory participates in the
        thermoreceptive representation . On the
        left, the thermoreceptive contribution is weighted toward
        the **sensory-discriminative** aspect of temperature
        perception, while the autonomic response to thermal
        challenge (cold pressor) is more strongly right-weighted.

    interoception                                  (left emphasis — SECONDARY)
        BA 41's transition-zone territory participates in the
        **primary interoceptive cortex** of the posterior insula.
        On the left, the interoceptive contribution is weighted
        toward the **sensory-discriminative** aspect of visceral
        sensation, while the **interoceptive-accuracy** component
        is more strongly right-weighted (see right BA 13).

    autonomic_control (parasympathetic)            (left emphasis)
        The posterior insula's nociceptive and thermoreceptive
        activity drives **autonomic responses** to pain and
        temperature. On the left, the coupling is weighted toward
        **parasympathetic** outflow — vagal bradycardia and
        depressor responses during pain or thermal challenge. The
        left BA 41 → hypothalamus and BA 41 → NST projections are
        part of this parasympathetic substrate. On the right, the
        same autonomic coupling is **sympathetic** (pressor,
        tachycardic).

**Left-specific caveat on `speech_articulation`.** BA 41 does **not**
carry the domain. The apraxia-of-speech territory is the anterior
insula (BA 13 / BA 16 / opercular transition), which is **rostral**
to BA 41's posterior transition zone. BA 41 is at the posterior pole
of the insula, far from the critical speech-articulation territory.

**Left-specific caveat on `vestibular_and_self_location`.** This
domain is **right-emphasized at BA 13**. The left BA 41 does **not**
carry it.

**Left-specific caveat on `gustatory`.** BA 41 is **not** a primary or
secondary taste area. The gustatory territory is anterior (BA 43, area
G, BA 14). BA 41's chemosensory contribution is **zero** — the
posterior insula does not participate in taste processing.

**Left-specific caveat on `salience_network` and `social_emotional`.**
These domains are **anterior insular** on both sides. The posterior
insula (including BA 41) is the primary sensory cortex, not the
salience hub. BA 41 does not carry them.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → VMpo (posterior ventromedial nucleus, parvicellular part)
            **BA 41's primary thalamic afferent.** VMpo relays
            lamina I spinothalamocortical nociceptive and
            thermoreceptive input to the posterior insula
            . This is the anatomical
            substrate of BA 41's primary nociceptive and
            thermoreceptive roles.
        → VPL / VPI (ventroposterior lateral / inferior)
            Somatosensory thalamic nuclei with a projection to the
            opercular component of the transition zone, supporting
            the secondary somatosensory overlay.
        → auditory thalamus (medial geniculate body, MGB)
            **The naming-collision afferent.** The MGB projects to
            the **temporal** BA 41 territory (primary auditory
            cortex), NOT to the insular BA 41 territory. The
            auditory thalamic projection does not enter the
            insular BA 41 package — the circular sulcus is the
            boundary. This entry is documented here only to
            pre-empt the conflation: **insular BA 41 does not
            receive MGB input; the auditory input terminates at the
            temporal BA 41 boundary.**

    cortical afferents
        → BA 42 (insular-opercular transition), left
            Reciprocal connections with the rostral half of the
            insular BA 41/42 pair.
        → BA 13 (middle insula), left
            The granular-to-agranular transition from BA 13 to the
            posterior insula projects caudally into BA 41's
            territory, carrying the middle insular multimodal
            integration signal.
        → secondary somatosensory cortex (S2), left
            The temporal-operculum component of BA 41's territory
            receives S2 input, supporting the opercular convergence
            of somatosensory and nociceptive signals.
        → anterior insula (via intrainsular connections)
            BA 41 projects rostrally to the anterior insula,
            carrying the sensory-discriminative pain signal that
            the anterior insula transforms into the affective-
            motivational response.

    subcortical efferents
        → hypothalamus (lateral hypothalamus), left
            **BA 41 → LH is part of the parasympathetic efferent
            pathway.** On the left, this projection is weighted
            toward parasympathetic outflow (vagal bradycardia,
            depressor responses during pain or thermal challenge).
        → nucleus of the solitary tract (NST), left
            BA 41 projects to the NST, the brainstem relay for
            visceral afferents and the origin of vagal
            parasympathetic outflow.
        → periaqueductal gray (PAG)
            BA 41 → PAG projections support the descending
            modulation of pain and the autonomic-defensive response
            to noxious stimuli. On the left, the PAG projection is
            weighted toward the parasympathetic / vagal defensive
            response; on the right, toward the sympathetic
            defensive response (ictal fear, autonomic auras).

    brainstem interactions
        → parabrachial nucleus (indirect via thalamus)
            The parabrachial → VMpo → BA 41 pathway is the
            anatomical substrate of the primary nociceptive and
            thermoreceptive relay.

    callosal connections
        → right BA 41
            Interhemispheric coordination of the posterior insular
            transition. The left → right traffic is weighted toward
            **sensory-discriminative / language-linked** pain
            signals and **parasympathetic** autonomic signals; the
            right → left traffic is weighted toward
            **affective-motivational / arousal** pain signals and
            **sympathetic** autonomic signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in three respects:
(a) the VMpo → BA 41 pathway carries sensory-discriminative pain and
temperature signals that the left uses for **language-linked**
evaluation;
(b) the BA 41 → hypothalamus, BA 41 → NST, and BA 41 → PAG projections
are **parasympathetic** rather than sympathetic;
(c) the callosal traffic carries sensory-discriminative /
language-linked and parasympathetic signals.

**The MGB entry is a naming-collision guard, not a real afferent.**
The medial geniculate body projects to the temporal BA 41 (auditory
cortex), not to the insular BA 41. The ``CONNECTIVITY`` dict documents
this only to prevent a downstream conflation, and must tag the entry as
``"naming_collision_boundary_not_insular_afferent"``.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_ba41_sensory_discriminative_pain
        **This is the left BA 41 anchor par excellence.** The
        posterior insula is the **primary nociceptive cortex**,
        and left BA 41 lesions produce **impaired pain localization
        and quality discrimination** — the patient can feel that
        something hurts but cannot say exactly where or what kind
        of pain it is. The left BA 41 is more strongly engaged
        during **verbal pain-rating tasks**; the right BA 41
        is more strongly engaged during **pain anticipation and
        autonomic arousal**.

    left_insular_thermoreceptive_discrimination
        The posterior insula contains a **cool/warm topography**,
        and left BA 41 lesions can produce **impaired thermal
        discrimination** — reduced ability to distinguish cool
        from warm stimuli. The autonomic response to thermal
        challenge (cold pressor) is more strongly right-weighted,
        but the sensory-discriminative thermal processing is
        left-weighted.

    left_posterior_insular_stroke_pain
        Posterior insular strokes — including those involving BA 41
        — can produce **central post-stroke pain** (thalamic pain
        syndrome with insular contribution). On the left, the
        **sensory-discriminative** component (the "where and how
        intense" aspect) is more prominent in the clinical
        presentation; on the right, the **affective-motivational**
        component (the "how bad it feels" aspect) is more
        prominent.

    left_ba41_parasympathetic_autonomic_coupling
        Left BA 41's nociceptive and thermoreceptive activity
        drives **parasympathetic** autonomic responses — vagal
        bradycardia, depressor responses, and altered gastric
        motility during pain or thermal challenge. Left BA 41
        lesions can produce **parasympathetic dysregulation** in
        these responses, distinct from the right BA 41's
        sympathetic signature (pressor, tachycardic).

    insular_opercular_transition_glioma
        Because BA 41 is a **buried transition territory** at the
        junction of the posterior insula and the temporal operculum,
        resecting a left insular / opercular glioma in the BA 41
        zone requires careful mapping of nociceptive,
        thermoreceptive, and auditory function. **The naming
        collision is a surgical hazard**: the surgeon must not
        confuse the insular-opercular BA 41 territory with the
        temporal BA 41 (Heschl's gyrus) territory, which is
        auditory cortex on the superior temporal plane. Left BA 41
        resections risk **sensory-discriminative pain deficits**,
        **thermal discrimination deficits**, and
        **parasympathetic dysregulation**.

    insular_opercular_epilepsy_naming_collision_hazard
        Seizures arising from the insular-opercular transition zone
        can present with **painful somatosensory auras** or
        **thermal auras** that the patient may describe as coming
        from the contralateral body. **The naming collision with
        temporal BA 41 is a semiological hazard**: an
        insular-opercular seizure with an auditory aura (from
        spread to temporal BA 41) may be mistaken for a purely
        insular seizure, and vice versa. Pre-surgical workup must
        distinguish the two territories explicitly.

    autonomic_stress_vulnerability_sudep
        Posterior insula dysfunction may contribute to **SUDEP**
        (sudden unexpected death in epilepsy) through the
        cortical control of cardio-respiratory autonomic function.
        On the **left**, the parasympathetic weighting of BA 41's
        autonomic coupling is **protective-weighted** rather than
        arrhythmogenic — the right BA 41's sympathetic weighting
        is the more directly arrhythmogenic side, as documented
        in the right sibling.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 41 autonomic contribution is parasympathetic (right
is sympathetic), and the left BA 41's SUDEP contribution is
protective-weighted rather than arrhythmogenic;
(b) the left BA 41's nociceptive and thermoreceptive contributions
are weighted toward the **sensory-discriminative / language-linked**
aspect (right is affective-motivational / arousal). The right
sibling's docstring carries the corresponding right-sided anchors.

**The naming-collision hazard is a left-and-right invariant** — it is
documented identically in both packages and in the parent registry's
``BA 41 / BA 42 NAMING-COLLISION CONTRACT``.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left insular BA registry. This package's parent, source of
    the ``NAMING_COLLISIONS`` entry for BA 41, and enforcer of the
    ``speech_articulation`` exclusion.

..brodmann_area_42_posterior_insula
    Rostral neighbour — the other half of the insular BA 41/42 pair.

..brodmann_area_13_middle_insula
    Rostral / dorsal neighbour via the granular-to-agranular
    transition. BA 13's multimodal integration signal is carried
    caudally into BA 41's nociceptive/thermoreceptive territory.

..brodmann_area_14
    Distant rostral neighbour — no direct adjacency (BA 13 and
    BA 16 intervene).

..brodmann_area_16
    Distant rostral neighbour — no direct adjacency.

..brodmann_area_43_anterior_insula
    Rostroventral neighbour — no direct adjacency (the middle
    insula intervenes). BA 41 is **not** a taste area.

...primary_gustatory_cortex
    The **functional-field sibling** (one level up, under
    ``..insular``). BA 41 is **not** part of the PGC's cortical
    territories — the PGC is anterior, BA 41 is posterior. There is
    no overlap between the two.

..cortex.temporal.brodmann_areas.brodmann_area_41
    **The naming-collision source.** The temporal BA 41 package
    describes the primary auditory cortex (Heschl's gyrus). It is
    a **different territory**, and both packages must carry a
    ``NAMING_COLLISION_WITH`` field naming the other. **No
    downstream code may resolve "BA 41" without a lobe qualifier.**

..cortex.temporal.brodmann_areas.brodmann_area_42
    The **naming-collision source for the temporal side** of the
    insular BA 42 package (not this one, but cross-referenced here
    for completeness).

..cortex.temporal
    The temporal lobe parent. Its ``..sulci.circular_sulcus``
    (or the equivalent limiting sulcus package) is the anatomical
    boundary between the insular BA 41 territory and the temporal
    BA 41 territory. The temporal parent must document the
    naming collision on its side.

..cortex.frontal
    The frontal operculum covers the anterior insula, not the
    posterior transition zone. BA 41 does not border the frontal
    operculum directly. Recorded here to pre-empt a false
    cross-reference.

..cortex.parietal
    The parietal operculum is adjacent to the dorsal margin of the
    posterior insula, near the transition zone. The parietal
    package must declare the insula as a hidden neighbour.

../../subcortical/diencephalon/thalamus
    The **VMpo** thalamic nucleus is BA 41's primary afferent. The
    thalamus package must declare VMpo as a cortical afferent to
    the left BA 41. It must **not** declare the medial geniculate
    body (MGB) as an afferent to the insular BA 41 — MGB projects
    to the temporal BA 41, not to the insular BA 41.

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem relay that feeds
    VMpo and thus BA 41. It is part of the nociceptive and
    thermoreceptive ascending pathway.

../../subcortical/diencephalon/hypothalamus
    The left BA 41 → left hypothalamus projection supports
    **parasympathetic** autonomic coupling to pain and thermal
    challenge. The hypothalamus package must declare the left
    BA 41 as a cortical afferent.

../../brainparts/hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
    The **nucleus of the solitary tract (NST)** receives left BA 41
    projections and is the origin of vagal parasympathetic outflow.
    The NST package must declare the left BA 41 as a cortical
    afferent.

../../brainparts/midbrain/tegmentum/periaqueductal_gray
    The periaqueductal gray receives left BA 41 projections
    supporting descending pain modulation and the autonomic-
    defensive response. On the left, the PAG projection is
    weighted toward parasympathetic / vagal defensive responses.

../../right/cortex/insular/brodmann_areas/brodmann_area_41_posterior_insula
    The right-hemisphere homologue. Structural fields (BA number,
    region label, **naming-collision field**, **parcellation-
    convention field**, architectonic neighbourhoods, BA-to-
    neighbour adjacency, MGB-guard entry) MUST be byte-identical.
    Functional emphasis and clinical significance diverge — the
    left BA 41 is weighted toward sensory-discriminative /
    language-linked pain, thermal discrimination,
    parasympathetic autonomic coupling, and protective-weighted
    SUDEP; the right BA 41 is weighted toward affective-
    motivational / arousal pain, thermoreceptive autonomic
    challenge, sympathetic autonomic coupling, and
    arrhythmogenic-weighted SUDEP.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_41_posterior_insula"
    HEMISPHERE          = "left"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 41   # IN THE INSULAR SENSE — not the
                               # auditory BA 41
    INSULAR_REGION      = "insular_opercular_transition"
    CYTOTECTONIC_GRADIENT = "agranular_to_dysgranular"

    NAMING_COLLISION_WITH = (
        "temporal.brodmann_areas.brodmann_area_41",
    )
        # **This field is the package's defining structural
        # concern.** It is byte-identical to the right sibling's.
        # It names the temporal BA 41 package (primary auditory
        # cortex), which is a DIFFERENT territory. Both packages
        # must carry the reciprocal cross-reference.

    PARCELATION_CONVENTION = (
        "Brodmann's classical scheme does not include an insular "
        "BA 41. The 'BA 41' label here is a modern parcellation "
        "convention for the insular-opercular transition zone at "
        "the posterior-insula / temporal-operculum junction. It is "
        "NOT the auditory BA 41 of the transverse temporal gyrus. "
        "Modern schemes (HCP 180-area, Ongur-Price, Petrides-"
        "Pandya) subdivide this region under different labels."
    )
        # **This field must be present and must be byte-identical
        # to the right sibling's.** The convention is a
        # numbering-scheme artifact, not a hemisphere-specific
        # fact.

    MGB_AFFERENT_GUARD = (
        "The medial geniculate body (MGB) does NOT project to the "
        "insular BA 41. MGB projects to the temporal BA 41 (primary "
        "auditory cortex, Heschl's gyrus). The circular sulcus is "
        "the boundary. Any downstream code that queries auditory "
        "afferents to 'BA 41' must specify the lobe."
    )
        # **This guard is byte-identical to the right sibling's**
        # and is required by the parent registry's naming-
        # collision contract.

    FUNCTIONAL_DOMAINS  = (
                              "nociception_and_pain_affect",
                              "thermoreception",
                              "interoception",         # secondary /
                                                       # primary
                                                       # interoceptive
                                                       # contribution
                              "autonomic_control",     # left:
                                                       # parasympathetic
                              # NOTE: speech_articulation is
                              # EXCLUDED (anterior insular
                              # territory; BA 41 is posterior).
                              # NOTE: vestibular_and_self_location
                              # is EXCLUDED (right-emphasized at
                              # BA 13).
                              # NOTE: gustatory is EXCLUDED (BA 41
                              # is not a taste area).
                              # NOTE: salience_network and
                              # social_emotional are EXCLUDED
                              # (anterior insular territories;
                              # BA 41 is posterior primary
                              # sensory cortex).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "nociception_and_pain_affect":
                                  "sensory_discriminative_language_"
                                  "linked_pain_quality",
                              "thermoreception":
                                  "sensory_discriminative_cool_warm_"
                                  "topography_left_weighted",
                              "interoception":
                                  "posterior_primary_interoceptive_"
                                  "sensory_discriminative",
                              "autonomic_control":
                                  "parasympathetic_vagal_bradycardia_"
                                  "depressor_pain_coupling",
                          }

    MODERN_CROSSWALK    = {   # BA 41 (insular) → modern labels
                              "HCP_180":       ("Ig", "Id", "OP4"),
                              "Ongur_Price_2000": ("Ial", "Iapm",
                                                   "Iapl"),
                              "Petrides_Pandya":  ("Ig", "Id", "OP4"),
                          }
        # **The crosswalk must be present and must be byte-
        # identical to the right sibling's.** It documents that
        # the insular-opercular transition is captured by modern
        # labels like Ig, Id, and the OP series, not by "BA 41".

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_ba41_sensory_discriminative_"
                              "pain",
                              "left_insular_thermoreceptive_"
                              "discrimination",
                              "left_posterior_insular_stroke_pain",
                              "left_ba41_parasympathetic_autonomic_"
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
        "FUNCTIONAL_DOMAINS",
        "DOMAIN_EMPHASIS",
        "MODERN_CROSSWALK",
        "CONNECTIVITY",
        "CLINICAL_ANCHORS",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references BA 41 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**The BA 42 package is a forward reference for the cross-package
interface, not for this package's own structure.** BA 41's neighbour
BA 42 (``brodmann_area_42_posterior_insula``) must exist as a sibling
package for the insular BA 41/42 pair to be complete, but BA 41's own
dependency on BA 42 is only the reciprocal-adjacency declaration. If
BA 42 is not yet built when BA 41 is finalised, BA 41's adjacency to
BA 42 is a forward reference until BA 42 is created, on both sides in
the same commit.

**The temporal BA 41 package is a required cross-package reference,
not a forward reference.** The temporal BA 41 (Heschl's gyrus) package
exists or will exist under ``temporal/brodmann_areas/``, and the
naming-collision contract requires both packages to carry reciprocal
``NAMING_COLLISION_WITH`` fields. If the temporal BA 41 does not yet
exist when this package is created, the temporal package must be
created with the reciprocal field in the same commit — **the collision
must not be left half-declared**.

**The circular sulcus package is a required cross-package reference.**
The anatomical boundary between the insular BA 41 territory and the
temporal BA 41 territory is the **circular sulcus** (limiting sulcus,
sulcus circularis). The circular sulcus package — either
``..sulci.circular_sulcus`` under the insular parent, or a shared
sulcus package if the sulcus is modelled at the cortex level — must
declare itself as the naming-collision boundary. This is the
**anatomically correct locus** for the boundary, and the two BA 41
packages (insular, temporal) must cross-reference it on both sides.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 41 is a **transition territory** and is not internally subdivided
in the classical scheme. If a future parcellation nevertheless decides
to split it into an **insular component** and an **opercular
component** (following the territory's cross-circular-sulcus extent),
the promotion takes this form:

    brodmann_area_41_posterior_insula/
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
BA 41 or BA 42 packages.** The opercular component of insular BA 41
is the *operculum* of the insular-opercular transition, not the
superior temporal plane's auditory cortex. The temporal packages
describe the auditory cortex on the superior surface; the insular
BA 41 opercular component describes the cortex on the opercular
surface. They are adjacent across the circular sulcus but distinct.

**No split should be performed while the circular sulcus boundary
package does not yet exist.** Splitting the insular BA 41 into
insular and opercular components without an explicit boundary
package would multiply unresolved references and make the
naming-collision contract harder to enforce.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_41_posterior_insula``:

    MUST be identical (byte-for-byte):
        AREA_NAME                      "brodmann_area_41_posterior_insula"
        LOBE                           "insular"
        BRODMANN_NUMBER                41 (insular sense)
        INSULAR_REGION                 "insular_opercular_transition"
        CYTOTECTONIC_GRADIENT          "agranular_to_dysgranular"
        NAMING_COLLISION_WITH          ("temporal.brodmann_areas."
                                       "brodmann_area_41",) —
                                       byte-identical; the naming
                                       collision is a numbering-
                                       scheme artifact, not a
                                       hemisphere artifact
        PARCELATION_CONVENTION         the parcellation-convention
                                       text — byte-identical
        MGB_AFFERENT_GUARD             the auditory-afferent guard
                                       — byte-identical
        Architectonic neighbourhoods
        BA-to-neighbour adjacency (including the circular-sulcus
                                       boundary)
        MODERN_CROSSWALK               (the same HCP / Öngür-Price /
                                       Petrides labels)
        SUBDIVISIONS                   both empty (or both non-empty
                                       in the same way, if a split
                                       is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        FUNCTIONAL_DOMAINS     both sides carry the same four
                               domains (nociception_and_pain_affect,
                               thermoreception, interoception,
                               autonomic_control) and both exclude
                               speech_articulation,
                               vestibular_and_self_location,
                               gustatory, salience_network, and
                               social_emotional. The set is
                               identical.
        DOMAIN_EMPHASIS        left: nociception is "sensory_
                               discriminative_language_linked_pain_
                               quality"; thermoreception is "sensory_
                               discriminative_cool_warm_topography_
                               left_weighted"; interoception is
                               "posterior_primary_interoceptive_
                               sensory_discriminative";
                               autonomic_control is "parasympathetic_
                               vagal_bradycardia_depressor_pain_
                               coupling".
                               right: nociception is "affective_
                               motivational_arousal_pain_response";
                               thermoreception is "thermoreceptive_
                               autonomic_challenge_sympathetic";
                               interoception is "posterior_primary_
                               interoceptive_autonomic_coupling";
                               autonomic_control is "sympathetic_
                               pressor_tachycardic_pain_coupling".
        CONNECTIVITY           same bundle names; left: BA 41 →
                               hypothalamus / NST / PAG is
                               parasympathetic; callosal traffic
                               carries sensory-discriminative and
                               parasympathetic signals; right: BA 41
                               → hypothalamus / NST / PAG is
                               sympathetic; callosal traffic
                               carries affective-motivational and
                               sympathetic signals.
        CLINICAL_ANCHORS       left: seven anchors (sensory-
                               discriminative pain, thermal
                               discrimination, posterior insular
                               stroke pain with sensory-
                               discriminative emphasis,
                               parasympathetic coupling, glioma
                               resection, epilepsy naming-
                               collision hazard, SUDEP protective-
                               weighted).
                               right: seven anchors (affective-
                               motivational pain, thermoreceptive
                               autonomic challenge, posterior
                               insular stroke pain with affective
                               emphasis, sympathetic coupling,
                               glioma resection, epilepsy naming-
                               collision hazard, SUDEP
                               arrhythmogenic-weighted).

**The `DOMAIN_EMPHASIS` asymmetry is the sharpest single entry in this
contract.** Both hemispheres carry the same four domains and both
exclude the same five, but the emphasis within every shared domain
points in opposite directions: the left BA 41 is the
**sensory-discriminative / parasympathetic** territory, the right
BA 41 is the **affective-motivational / sympathetic** territory. A
right-hemisphere package that copies the left's `DOMAIN_EMPHASIS`
verbatim is a bug.

**The naming-collision fields and the MGB guard are byte-identical
on both sides** and must not be allowed to drift. They are properties
of the BA numbering scheme, not of the hemisphere, and any deviation
is a bug.

**The SUDEP anchors point in opposite directions.** The left BA 41's
SUDEP anchor is **protective-weighted** (parasympathetic coupling);
the right BA 41's is **arrhythmogenic-weighted** (sympathetic
coupling). The two anchors must not be copied verbatim between the
packages — they make **opposite claims** about the hemisphere's SUDEP
contribution.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_41_posterior_insula".
[ ] HEMISPHERE is "left".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 41 — the **insular** BA 41, not the
    auditory BA 41.
[ ] INSULAR_REGION is "insular_opercular_transition".
[ ] CYTOTECTONIC_GRADIENT is "agranular_to_dysgranular".
[ ] **NAMING_COLLISION_WITH** is
    ``("temporal.brodmann_areas.brodmann_area_41",)`` and is
    byte-identical to the right sibling's.
[ ] **PARCELATION_CONVENTION** is present and documents that the
    "BA 41" label here is a modern parcellation convention for the
    insular-opercular transition, not a classical architectonic
    entity.
[ ] **MGB_AFFERENT_GUARD** is present and documents that the
    medial geniculate body projects to the temporal BA 41 (auditory
    cortex), not to the insular BA 41.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - nociception_and_pain_affect
    - thermoreception
    - interoception
    - autonomic_control
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation
    (anterior insular; BA 41 is posterior).
[ ] FUNCTIONAL_DOMAINS **excludes** vestibular_and_self_location
    (right-emphasized at BA 13).
[ ] FUNCTIONAL_DOMAINS **excludes** gustatory (BA 41 is not a
    taste area).
[ ] FUNCTIONAL_DOMAINS **excludes** salience_network and
    social_emotional (anterior insular territories; BA 41 is
    posterior primary sensory cortex).
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis** per domain:
    - nociception → sensory_discriminative_language_linked_pain_
      quality
    - thermoreception → sensory_discriminative_cool_warm_topography_
      left_weighted
    - interoception → posterior_primary_interoceptive_sensory_
      discriminative
    - autonomic_control → parasympathetic_vagal_bradycardia_
      depressor_pain_coupling
[ ] MODERN_CROSSWALK is present, byte-identical to the right
    sibling's, and documents that the insular-opercular transition
    is captured by modern labels like Ig, Id, and the OP series.
[ ] CONNECTIVITY documents:
    - VMpo thalamic afferent (primary nociceptive and
      thermoreceptive relay)
    - VPL / VPI thalamic afferent (somatosensory component)
    - **MGB entry with the "naming_collision_boundary_not_insular_
      afferent" tag** (guard against conflation)
    - BA 42 and BA 13 intracortical afferents
    - BA 41 → anterior insula intrainsular afferent (sensory-
      discriminative → affective-motivational transfer)
    - BA 41 → hypothalamus (parasympathetic, left-specific)
    - BA 41 → NST (parasympathetic, left-specific)
    - BA 41 → PAG (parasympathetic-weighted on the left)
    - callosal traffic to right BA 41 (sensory-discriminative and
      parasympathetic, left-specific)
[ ] CLINICAL_ANCHORS contains the seven left-specific anchors:
    - left_ba41_sensory_discriminative_pain
    - left_insular_thermoreceptive_discrimination
    - left_posterior_insular_stroke_pain
    - left_ba41_parasympathetic_autonomic_coupling
    - insular_opercular_transition_glioma
    - insular_opercular_epilepsy_naming_collision_hazard
    - autonomic_stress_vulnerability_sudep (protective-weighted)
[ ] The **left sensory-discriminative pain** is documented as the
    primary left BA 41 anchor, with the language-linked pain-
    quality evaluation as the left-weighted component.
[ ] The **naming-collision hazard** is documented in the clinical
    anchors as a **surgical and semiological hazard** — the
    surgeon must not confuse the insular BA 41 with the temporal
    BA 41, and pre-surgical workup must distinguish them.
[ ] The **SUDEP protective weighting** on the left is documented
    as the mirror of the right's arrhythmogenic weighting, and
    the two anchors are not copied verbatim between the packages.
[ ] The **BA 41 ≠ BA 13 / BA 14 / BA 16 / BA 43** distinction is
    documented: BA 41 is the posterior primary sensory territory,
    not an anterior insular associative territory.
[ ] The **BA 41 ≠ PGC** distinction is documented: BA 41 is
    posterior (nociceptive / thermoreceptive / interoceptive);
    the PGC is anterior (gustatory). No overlap.
[ ] The **BA 41 (insular) ≠ BA 41 (temporal)** distinction is
    documented exhaustively: parcellation convention, MGB guard,
    naming-collision field, circular-sulcus boundary, surgical
    hazard, semiological hazard.
[ ] The **reciprocal NAMING_COLLISION_WITH field** is expected on
    the temporal BA 41 package, and the two packages must be
    created / updated in the same commit — the collision must not
    be left half-declared.
[ ] The **circular sulcus boundary package** is cross-referenced
    as the anatomical locus of the naming-collision boundary.
[ ] The **BA 42 forward reference** is documented (the sibling
    insular BA 42 package must exist for the pair to be complete).
[ ] No SUBDIVISIONS promotion is performed while the circular
    sulcus boundary package does not yet exist.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, NAMING_COLLISION_
    WITH, PARCELATION_CONVENTION, MGB_AFFERENT_GUARD, architectonic
    neighbourhoods, modern crosswalk, FUNCTIONAL_DOMAINS set) match
    the right sibling; DOMAIN_EMPHASIS, CONNECTIVITY emphasis, and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The SUDEP asymmetry is verified**: the left BA 41 carries a
    protective-weighted anchor, the right BA 41 carries an
    arrhythmogenic-weighted anchor, and neither has been copied
    verbatim from the other.
[ ] Any downstream code that queries "BA 41" must specify the lobe
    — the temporal and insular packages are never conflated, and
    no global BA index merges them.
[ ] Any downstream code that queries auditory afferents to "BA 41"
    must specify the temporal BA 41 — the MGB guard is enforced.
[ ] Any downstream code assigning BA 41 autonomic function must
    route through DOMAIN_EMPHASIS and must weight the left BA 41
    toward **parasympathetic** and the right BA 41 toward
    **sympathetic**.
"""