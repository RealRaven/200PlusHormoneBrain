"""
Brodmann Area 41 (Posterior Insula / Insular-Opercular Transition) — Right Hemisphere
======================================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── insular
                              └── brodmann_areas
                                    └── brodmann_area_41_posterior_insula   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the right
hemisphere's **BA 41 in its insular-opercular-transition sense** — the
cortex at the junction of the posterior insula and the temporal
operculum, across the circular sulcus. It is **not** the auditory
cortex, and the naming collision with ``temporal.brodmann_areas.
brodmann_area_41`` is the package's defining structural concern (see
below).

Parent: ``..brodmann_areas`` (right insular BA registry) — sibling to
BA 13, BA 14, BA 16, BA 42, BA 43.

This package is the **structural mirror** of
``../../left/cortex/insular/brodmann_areas/brodmann_area_41_posterior_insula``.
The BA number, the naming-collision field, the parcellation convention,
the MGB guard, the region label, and the insular-opercular-transition
gradient are identical on both sides; the **functional emphasis** and
**clinical significance** diverge — on the right, BA 41's
transition-zone territory is weighted toward the
**affective-motivational** nociceptive component, the
**thermoreceptive autonomic challenge** response, the **sympathetic**
autonomic coupling of pain and temperature, and the
**arrhythmogenic-weighted** SUDEP contribution.

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

The right BA 41 (insular-opercular transition) borders:

    rostrally     BA 42 (insular-opercular transition, more rostral
                  component) — forward reference if not yet built
    caudally      the agranular posterior insula and the planum
                  temporale (auditory territory, temporal BA 41/42 —
                  NAMING COLLISION)
    dorsally      the circular sulcus upper bank
    ventrally     the inferior limiting sulcus
    medially      the posterior insular long gyri

**Right-hemisphere specificity**: the right BA 41 is the posterior
insular transition territory most strongly coupled to the
**affective-motivational** dimension of pain, to the **sympathetic**
autonomic response to thermal challenge, and to the
**arrhythmogenic-weighted** SUDEP substrate. Right insular stimulation
produces **pressor and tachycardic** responses, and the right BA 41 →
hypothalamus, BA 41 → NST, and BA 41 → PAG projections are the
sympathetic substrate of pain- and temperature-evoked autonomic
arousal. On the nociceptive side, the right BA 41 is weighted toward
the **affective-motivational / arousal** component ("how bad it
feels"), while the left BA 41 is weighted toward the
**sensory-discriminative / language-linked** component ("where and how
intense"). This left-right split mirrors the split between the
posterior insula (primary sensory) and anterior insula (affective)
within each hemisphere, but the weighting of the residual
affective-motivational contribution that stays in the posterior insula
is **right-lateralized**.

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
            component. **On the right, the residual
            affective-motivational contribution within the
            posterior insula is larger than on the left** — the
            right BA 41 is more strongly engaged during pain
            anticipation and during the autonomic arousal that
            accompanies noxious stimulation.
        primary thermoreceptive cortex
            The posterior insula contains a **cool/warm
            topography** — distinct thermoreceptive subregions for
            innocuous cooling and warming. **On the right, the
            thermoreceptive representation is more strongly coupled
            to the autonomic response to thermal challenge** (cold
            pressor): right BA 41 activity tracks the sympathetic
            surge evoked by cooling, while the left BA 41's
            thermoreceptive activity is weighted toward the
            sensory-discriminative discrimination of cool versus
            warm.
        primary interoceptive cortex
            The posterior insula is the **primary interoceptive
            cortex** — the cortical recipient of lamina I
            spinothalamocortical and vagal afferents relayed via
            VMpo and other thalamic nuclei. On the right, the
            interoceptive contribution is weighted toward the
            **autonomic-affective** coupling (the interoceptive
            contribution to affective arousal), while the left's
            is weighted toward the sensory-discriminative
            component.
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
        autonomic coupling (sympathetic on the right)
            The posterior insula's nociceptive and thermoreceptive
            activity drives **autonomic responses** to pain and
            temperature. **On the right, the coupling is weighted
            toward sympathetic outflow** (pressor, tachycardic
            responses, and the peri-ictal sympathetic surge that
            contributes to SUDEP); on the left, toward
            parasympathetic (vagal bradycardia, depressor
            responses).

**This field is structurally identical to the left sibling's** — the
architectonic neighbours and functional overlays are the same on both
sides. What differs is the **emphasis** within the autonomic,
nociceptive-affective, and thermoreceptive overlays: the right BA 41 is
weighted toward **sympathetic** autonomic coupling and the
**affective-motivational / arousal** pain response; the left BA 41 is
weighted toward **parasympathetic** autonomic coupling and the
**sensory-discriminative / language-linked** pain evaluation.

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
                                           the posterior insula. **On
                                           the right, BA 13 is the
                                           interoceptive-accuracy
                                           node**, and BA 41's
                                           autonomic coupling is
                                           hierarchically downstream
                                           of BA 13's interoceptive
                                           re-representation
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

**This field is byte-identical to the left sibling's.** The adjacency
relationships are topological, not lateralized, and the naming-collision
neighbours (temporal BA 41/42) are the same on both sides.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 41 participates in **four** canonical insular domains on the right.
The emphasis is as follows:

    nociception_and_pain_affect                    (right emphasis — PRIMARY)
        **This is BA 41's dominant contribution on the right.** The
        posterior insula is the **primary nociceptive cortex**, and
        BA 41's transition-zone territory carries the residual
        **affective-motivational** component that stays in the
        posterior insula — the "how bad it feels" and
        "how arousing it is" of pain — while the primary
        sensory-discriminative component is more left-weighted. On
        the right, the emphasis is on the **affective-motivational /
        arousal** aspect: right BA 41 lesions produce
        **reduced affective pain responses** and impaired
        **sympathetic arousal to noxious stimuli**, and the right
        posterior insula is more strongly engaged during **pain
        anticipation and pain-related autonomic responses**. The
        sensory-discriminative / language-linked aspect is weighted
        more toward the left.

    thermoreception                                (right emphasis)
        The posterior insula contains a **cool/warm topography**,
        and BA 41's transition-zone territory participates in the
        thermoreceptive representation . On the
        right, the thermoreceptive contribution is weighted toward
        the **autonomic challenge** aspect — the sympathetic surge
        evoked by cold pressor and the affective response to
        thermal discomfort — while the sensory-discriminative
        discrimination of cool from warm is more left-weighted.

    interoception                                  (right emphasis — SECONDARY)
        BA 41's transition-zone territory participates in the
        **primary interoceptive cortex** of the posterior insula.
        On the right, the interoceptive contribution is weighted
        toward the **autonomic-affective coupling** — the
        interoceptive contribution to affective arousal. The
        **interoceptive-accuracy** component is more strongly
        right-weighted at BA 13 (see right BA 13), and BA 41 is
        hierarchically downstream of BA 13's interoceptive
        re-representation.

    autonomic_control (sympathetic)                (right emphasis)
        The posterior insula's nociceptive and thermoreceptive
        activity drives **autonomic responses** to pain and
        temperature. **On the right, the coupling is weighted
        toward sympathetic outflow** — pressor and tachycardic
        responses during pain or thermal challenge, and the
        peri-ictal sympathetic surge that contributes to SUDEP.
        The right BA 41 → hypothalamus, BA 41 → NST, and BA 41 →
        PAG projections are the sympathetic substrate. On the
        left, the same autonomic coupling is **parasympathetic**
        (vagal bradycardia, depressor responses).

**Right-specific caveat on `speech_articulation`.** The domain **does
not exist on the right**. No right BA carries it. Right insular
lesions do not produce apraxia of speech. The right BA 41 excludes it
not because it belongs to the lobe as a whole (that is the left's
rationale) but because it is absent from the right hemisphere
entirely. The right BA 41 also excludes it simply because BA 41 is
posterior to the critical speech-articulation territory (anterior
insula) — a second, independent reason.

**Right-specific caveat on `vestibular_and_self_location`.** This
domain is **BA-13-emphasized on the right** (see
``brodmann_area_13_middle_insula``), not BA-41-emphasized. The right
BA 41 does **not** carry it.

**Right-specific caveat on `gustatory`.** BA 41 is **not** a primary or
secondary taste area. The gustatory territory is anterior (BA 43, area
G, BA 14). BA 41's chemosensory contribution is **zero** — the
posterior insula does not participate in taste processing.

**Right-specific caveat on `salience_network` and `social_emotional`.**
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
            . On the right, the VMpo → BA 41 pathway
            is weighted toward the affective-autonomic coupling of
            pain and temperature; on the left, toward the
            sensory-discriminative component.
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
        → BA 42 (insular-opercular transition), right
            Reciprocal connections with the rostral half of the
            insular BA 41/42 pair.
        → BA 13 (middle insula), right
            The granular-to-agranular transition from BA 13 to the
            posterior insula projects caudally into BA 41's
            territory. On the right, BA 13 is the
            interoceptive-accuracy node, and the BA 13 → BA 41
            projection carries the interoceptive signal that BA 41
            couples to the sympathetic autonomic response.
        → secondary somatosensory cortex (S2), right
            The temporal-operculum component of BA 41's territory
            receives S2 input, supporting the opercular convergence
            of somatosensory and nociceptive signals.
        → anterior insula (via intrainsular connections)
            BA 41 projects rostrally to the anterior insula,
            carrying the affective-motivational / arousal signal
            that the anterior insula transforms into the full
            affective pain experience. **On the right, the BA 41 →
            anterior insula projection is weighted toward the
            affective-arousal content**; on the left, toward the
            sensory-discriminative content.

    subcortical efferents
        → hypothalamus (lateral hypothalamus), right
            **BA 41 → LH is part of the sympathetic efferent
            pathway.** On the right, this projection is weighted
            toward sympathetic outflow (pressor, tachycardic
            responses during pain or thermal challenge).
        → nucleus of the solitary tract (NST), right
            BA 41 projects to the NST, the brainstem relay for
            visceral afferents and the origin of autonomic outflow.
            On the right, the BA 41 → NST projection is part of the
            sympathetic substrate.
        → periaqueductal gray (PAG)
            BA 41 → PAG projections support the descending
            modulation of pain and the autonomic-defensive response
            to noxious stimuli. **On the right, the PAG projection
            is weighted toward the sympathetic defensive response**
            — ictal fear, autonomic auras, and the peri-ictal
            sympathetic surge that contributes to SUDEP. On the
            left, the PAG projection is weighted toward the
            parasympathetic / vagal defensive response.

    brainstem interactions
        → parabrachial nucleus (indirect via thalamus)
            The parabrachial → VMpo → BA 41 pathway is the
            anatomical substrate of the primary nociceptive and
            thermoreceptive relay. On the right, the
            parabrachial → BA 41 pathway is weighted toward the
            sympathetic autonomic response to noxious stimuli.

    callosal connections
        → left BA 41
            Interhemispheric coordination of the posterior insular
            transition. The right → left traffic is weighted toward
            **affective-motivational / arousal** pain signals and
            **sympathetic** autonomic signals; the left → right
            traffic is weighted toward **sensory-discriminative /
            language-linked** pain signals and **parasympathetic**
            autonomic signals.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the VMpo → BA 41 pathway carries affective-autonomic pain and
temperature signals that the right uses for **arousal** and
**defensive** responses;
(b) the BA 41 → hypothalamus, BA 41 → NST, and BA 41 → PAG projections
are **sympathetic** rather than parasympathetic;
(c) the callosal traffic carries affective-motivational / arousal and
sympathetic signals.

**The MGB entry is a naming-collision guard, not a real afferent.**
The medial geniculate body projects to the temporal BA 41 (auditory
cortex), not to the insular BA 41. The ``CONNECTIVITY`` dict documents
this only to prevent a downstream conflation, and must tag the entry as
``"naming_collision_boundary_not_insular_afferent"``. **This entry is
byte-identical to the left sibling's.**

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ba41_affective_motivational_pain
        **This is the right BA 41 anchor par excellence.** The
        posterior insula is the **primary nociceptive cortex**,
        and the **affective-motivational** component that stays in
        the posterior insula is **right-weighted**. Right BA 41
        lesions produce **reduced affective pain responses** and
        impaired **sympathetic arousal to noxious stimuli** — the
        patient may still locate and rate the intensity of pain
        (left-weighted) but no longer shows the normal autonomic
        arousal and affective response. The right BA 41 is more
        strongly engaged during **pain anticipation** and during
        **pain-related autonomic responses** than the left.

    right_insular_thermoreceptive_autonomic_challenge
        The posterior insula contains a **cool/warm topography**,
        and on the right the thermoreceptive contribution is
        weighted toward the **autonomic challenge** aspect: right
        BA 41 activity tracks the **sympathetic surge evoked by
        cold pressor**, and right BA 41 lesions impair the
        autonomic response to thermal challenge more than the
        sensory-discriminative discrimination of cool from warm
        (which is more left-weighted).

    right_posterior_insular_stroke_pain
        Posterior insular strokes — including those involving BA 41
        — can produce **central post-stroke pain** (thalamic pain
        syndrome with insular contribution). On the right, the
        **affective-motivational** component (the "how bad it
        feels" and "how arousing it is" aspect) is more prominent
        in the clinical presentation; on the left, the
        **sensory-discriminative** component (the "where and how
        intense" aspect) is more prominent.

    right_ba41_sympathetic_autonomic_coupling
        Right BA 41's nociceptive and thermoreceptive activity
        drives **sympathetic** autonomic responses — pressor and
        tachycardic responses, and the peri-ictal sympathetic
        surge that contributes to SUDEP. Right BA 41 lesions can
        produce **sympathetic dysregulation** in these responses,
        distinct from the left BA 41's parasympathetic signature
        (vagal bradycardia, depressor responses).

    right_insular_opercular_seizures_affective_autonomic
        Right BA 41 / posterior insular-opercular seizures can
        present with **ictal autonomic auras** (tachycardia,
        flushing, piloerection, mydriasis), **ictal fear**, and
        **painful somatosensory or thermal auras**. The
        right-specific semiological cluster reflects the right
        insula's sympathetic and affective-defensive weighting,
        and is the mirror of the left's language-linked and
        parasympathetic seizure semiology. **The naming collision
        with temporal BA 41 is a semiological hazard**: an
        insular-opercular seizure with an auditory aura (from
        spread to temporal BA 41) may be mistaken for a purely
        insular seizure, and vice versa. Pre-surgical workup must
        distinguish the two territories explicitly.

    insular_opercular_transition_glioma
        Because BA 41 is a **buried transition territory** at the
        junction of the posterior insula and the temporal operculum,
        resecting a right insular / opercular glioma in the BA 41
        zone requires careful mapping of nociceptive,
        thermoreceptive, autonomic, and auditory function. **The
        naming collision is a surgical hazard**: the surgeon must
        not confuse the insular-opercular BA 41 territory with the
        temporal BA 41 (Heschl's gyrus) territory, which is
        auditory cortex on the superior temporal plane. Right BA 41
        resections risk **affective pain deficits**,
        **thermoreceptive autonomic deficits**, and
        **sympathetic dysregulation**.

    right_ba41_sudep_arrhythmogenic_dominance
        **This is the right-specific SUDEP anchor.** Posterior
        insula dysfunction may contribute to **SUDEP** (sudden
        unexpected death in epilepsy) through the cortical control
        of cardio-respiratory autonomic function. On the **right**,
        the sympathetic weighting of BA 41's autonomic coupling —
        and the BA 41 → PAG projection that mediates the
        peri-ictal sympathetic surge — is **arrhythmogenic-
        weighted**: the right posterior insula is part of the
        cortical substrate whose peri-ictal activation can trigger
        fatal arrhythmia. **The left BA 41's parasympathetic
        weighting is protective rather than arrhythmogenic in the
        peri-ictal window**, as documented in the left sibling.
        This is the sharpest left-right asymmetry in the SUDEP
        literature, and the two anchors must not be copied
        verbatim between hemispheres.

    right_insula_thermoreceptive_autonomic_dysregulation
        **Right-emphasized.** Right BA 41 lesions can produce
        **thermoregulatory autonomic dysregulation** — impaired
        sympathetic vasoconstrictor and sudomotor responses to
        cooling, and impaired sympathetically-mediated sweating
        and piloerection in the contralateral body. This is the
        right-weighted clinical counterpart of the left BA 41's
        sensory-discriminative thermal contribution.

These anchors are **right-hemisphere-specific** in two senses:
(a) the right BA 41 autonomic contribution is sympathetic (left is
parasympathetic), and the right BA 41 is the hemisphere whose
sympathetic weighting is implicated in **SUDEP arrhythmogenesis**
(left is protective-weighted);
(b) the right BA 41's nociceptive and thermoreceptive contributions
are weighted toward the **affective-motivational / arousal** aspect
(left is sensory-discriminative / language-linked). The left
sibling's docstring carries the corresponding left-sided anchors.

**The naming-collision hazard is a left-and-right invariant** — it is
documented identically in both packages and in the parent registry's
``BA 41 / BA 42 NAMING-COLLISION CONTRACT``.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The right insular BA registry. This package's parent, source of
    the ``NAMING_COLLISIONS`` entry for BA 41, and enforcer of the
    ``speech_articulation`` exclusion (which on the right means the
    domain is not declared anywhere, not that it is assigned to the
    lobe as a whole).

..brodmann_area_42_posterior_insula
    Rostral neighbour — the other half of the insular BA 41/42 pair.

..brodmann_area_13_middle_insula
    Rostral / dorsal neighbour via the granular-to-agranular
    transition. **On the right, BA 13 is the interoceptive-accuracy
    node**, and BA 41's autonomic coupling is hierarchically
    downstream of BA 13's interoceptive re-representation.

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
    the right BA 41. It must **not** declare the medial geniculate
    body (MGB) as an afferent to the insular BA 41 — MGB projects
    to the temporal BA 41, not to the insular BA 41.

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem relay that feeds
    VMpo and thus BA 41. On the right, the parabrachial → BA 41
    pathway is weighted toward the sympathetic autonomic response
    to noxious stimuli.

../../subcortical/diencephalon/hypothalamus
    The right BA 41 → right hypothalamus projection supports
    **sympathetic** autonomic coupling to pain and thermal
    challenge. The hypothalamus package must declare the right
    BA 41 as a cortical afferent.

../../brainparts/hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
    The **nucleus of the solitary tract (NST)** receives right BA 41
    projections and is the origin of autonomic outflow. The NST
    package must declare the right BA 41 as a cortical afferent,
    noting the sympathetic weighting.

../../brainparts/midbrain/tegmentum/periaqueductal_gray
    The periaqueductal gray receives right BA 41 projections
    supporting descending pain modulation and the autonomic-
    defensive response. On the right, the PAG projection is
    weighted toward the **sympathetic defensive response** (ictal
    fear, autonomic auras, the peri-ictal sympathetic surge).

../../left/cortex/insular/brodmann_areas/brodmann_area_41_posterior_insula
    The left-hemisphere homologue. Structural fields (BA number,
    region label, **naming-collision field**, **parcellation-
    convention field**, **MGB guard entry**, architectonic
    neighbourhoods, BA-to-neighbour adjacency, FUNCTIONAL_DOMAINS
    set) MUST be byte-identical. Functional emphasis and clinical
    significance diverge — the right BA 41 is weighted toward
    affective-motivational / arousal pain, thermoreceptive
    autonomic challenge, sympathetic autonomic coupling, and
    arrhythmogenic-weighted SUDEP; the left BA 41 is weighted
    toward sensory-discriminative / language-linked pain,
    thermal discrimination, parasympathetic autonomic coupling,
    and protective-weighted SUDEP.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_41_posterior_insula"
    HEMISPHERE          = "right"
    LOBE                = "insular"

    BRODMANN_NUMBER     = 41   # IN THE INSULAR SENSE — not the
                               # auditory BA 41
    INSULAR_REGION      = "insular_opercular_transition"
    CYTOTECTONIC_GRADIENT = "agranular_to_dysgranular"

    NAMING_COLLISION_WITH = (
        "temporal.brodmann_areas.brodmann_area_41",
    )
        # **Byte-identical to the left sibling's.** The naming
        # collision is a property of the BA numbering scheme, not
        # of the hemisphere.

    PARCELATION_CONVENTION = (
        "Brodmann's classical scheme does not include an insular "
        "BA 41. The 'BA 41' label here is a modern parcellation "
        "convention for the insular-opercular transition zone at "
        "the posterior-insula / temporal-operculum junction. It is "
        "NOT the auditory BA 41 of the transverse temporal gyrus. "
        "Modern schemes (HCP 180-area, Ongur-Price, Petrides-"
        "Pandya) subdivide this region under different labels."
    )
        # **Byte-identical to the left sibling's.**

    MGB_AFFERENT_GUARD = (
        "The medial geniculate body (MGB) does NOT project to the "
        "insular BA 41. MGB projects to the temporal BA 41 (primary "
        "auditory cortex, Heschl's gyrus). The circular sulcus is "
        "the boundary. Any downstream code that queries auditory "
        "afferents to 'BA 41' must specify the lobe."
    )
        # **Byte-identical to the left sibling's.**

    FUNCTIONAL_DOMAINS  = (
                              "nociception_and_pain_affect",
                              "thermoreception",
                              "interoception",         # secondary /
                                                       # autonomic-
                                                       # affective
                                                       # coupling
                              "autonomic_control",     # right:
                                                       # sympathetic
                              # NOTE: speech_articulation does NOT
                              # exist on the right; additionally,
                              # BA 41 is posterior to the
                              # critical anterior insular
                              # territory regardless.
                              # NOTE: vestibular_and_self_location
                              # is BA-13-emphasized on the right.
                              # NOTE: gustatory is EXCLUDED (BA 41
                              # is not a taste area).
                              # NOTE: salience_network and
                              # social_emotional are EXCLUDED
                              # (anterior insular territories;
                              # BA 41 is posterior primary
                              # sensory cortex).
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "nociception_and_pain_affect":
                                  "affective_motivational_arousal_"
                                  "pain_response",
                              "thermoreception":
                                  "thermoreceptive_autonomic_"
                                  "challenge_sympathetic",
                              "interoception":
                                  "posterior_primary_interoceptive_"
                                  "autonomic_affective_coupling",
                              "autonomic_control":
                                  "sympathetic_pressor_tachycardic_"
                                  "pain_coupling",
                          }

    MODERN_CROSSWALK    = {   # BA 41 (insular) → modern labels
                              "HCP_180":       ("Ig", "Id", "OP4"),
                              "Ongur_Price_2000": ("Ial", "Iapm",
                                                   "Iapl"),
                              "Petrides_Pandya":  ("Ig", "Id", "OP4"),
                          }
        # **Byte-identical to the left sibling's.**

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_ba41_affective_motivational_"
                              "pain",
                              "right_insular_thermoreceptive_"
                              "autonomic_challenge",
                              "right_posterior_insular_stroke_"
                              "pain",
                              "right_ba41_sympathetic_autonomic_"
                              "coupling",
                              "right_insular_opercular_seizures_"
                              "affective_autonomic",
                              "insular_opercular_transition_"
                              "glioma",
                              "right_ba41_sudep_arrhythmogenic_"
                              "dominance",
                              "right_insula_thermoreceptive_"
                              "autonomic_dysregulation",
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

**All forward-declaration caveat text is byte-identical to the left
sibling's** — the BA 42 forward reference and the circular sulcus
dependency are properties of the cortex tree, not of the hemisphere.

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
  4. Mirror the promotion on the left side in the same commit.

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

**The right-specific SUDEP and thermoreceptive-autonomic-dysregulation
anchors are parent-level claims** and cannot be cleanly attributed to
either the insular or the opercular sub-component alone. A split
would require retaining these anchors at the parent level.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../brodmann_area_41_posterior_insula``:

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
        FUNCTIONAL_DOMAINS set         the same four domains, with
                                       the same exclusions
        SUBDIVISIONS                   both empty (or both non-empty
                                       in the same way, if a split
                                       is ever done)
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        DOMAIN_EMPHASIS        right: nociception is "affective_
                               motivational_arousal_pain_response";
                               thermoreception is "thermoreceptive_
                               autonomic_challenge_sympathetic";
                               interoception is "posterior_primary_
                               interoceptive_autonomic_affective_
                               coupling"; autonomic_control is
                               "sympathetic_pressor_tachycardic_
                               pain_coupling".
                               left: nociception is "sensory_
                               discriminative_language_linked_pain_
                               quality"; thermoreception is "sensory_
                               discriminative_cool_warm_topography_
                               left_weighted"; interoception is
                               "posterior_primary_interoceptive_
                               sensory_discriminative";
                               autonomic_control is "parasympathetic_
                               vagal_bradycardia_depressor_pain_
                               coupling".
        CONNECTIVITY           same bundle names; right: BA 41 →
                               hypothalamus / NST / PAG is
                               sympathetic; BA 41 → anterior
                               insula carries affective-arousal
                               content; BA 13 → BA 41 carries
                               interoceptive-accuracy → autonomic
                               coupling; callosal traffic carries
                               affective-motivational and
                               sympathetic signals.
                               left: BA 41 → hypothalamus / NST /
                               PAG is parasympathetic; BA 41 →
                               anterior insula carries
                               sensory-discriminative content;
                               callosal traffic carries
                               sensory-discriminative and
                               parasympathetic signals.
        CLINICAL_ANCHORS       right: eight anchors (affective-
                               motivational pain, thermoreceptive
                               autonomic challenge, posterior
                               insular stroke pain with affective
                               emphasis, sympathetic coupling,
                               affective-autonomic seizures,
                               glioma resection, **SUDEP
                               arrhythmogenic dominance**,
                               thermoreceptive autonomic
                               dysregulation).
                               left: seven anchors (sensory-
                               discriminative pain, thermal
                               discrimination, posterior insular
                               stroke pain with sensory-
                               discriminative emphasis,
                               parasympathetic coupling, glioma
                               resection, epilepsy naming-
                               collision hazard, **SUDEP
                               protective-weighted**).

**The `DOMAIN_EMPHASIS` asymmetry is the sharpest single entry in this
contract.** Both hemispheres carry the same four domains and both
exclude the same five, but the emphasis within every shared domain
points in opposite directions: the right BA 41 is the
**affective-motivational / sympathetic** territory, the left BA 41 is
the **sensory-discriminative / parasympathetic** territory.

**The SUDEP asymmetry is the second sharpest entry.** Both hemispheres
carry a SUDEP anchor, but they **point in opposite directions**: the
right BA 41 is **arrhythmogenic-weighted** (the right insula's
sympathetic weighting, via the BA 41 → PAG pathway, is implicated in
peri-ictal fatal arrhythmia), and the left BA 41 is
**protective-weighted** (the left insula's parasympathetic weighting
is protective in the peri-ictal window). A right package that copies
the left's SUDEP anchor verbatim — or that drops the SUDEP anchor
entirely — is a bug. The two hemispheres contribute
**opposite-direction** autonomic influences during the peri-ictal
window.

**The naming-collision fields, the MGB guard, and the parcellation
convention are byte-identical on both sides** and must not be allowed
to drift. They are properties of the BA numbering scheme, not of the
hemisphere, and any deviation is a bug.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_41_posterior_insula" (same
    as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "insular".
[ ] BRODMANN_NUMBER is 41 — the **insular** BA 41, not the
    auditory BA 41.
[ ] INSULAR_REGION is "insular_opercular_transition".
[ ] CYTOTECTONIC_GRADIENT is "agranular_to_dysgranular".
[ ] **NAMING_COLLISION_WITH** is
    ``("temporal.brodmann_areas.brodmann_area_41",)`` and is
    byte-identical to the left sibling's.
[ ] **PARCELATION_CONVENTION** is present and byte-identical to the
    left sibling's — the "BA 41" label here is a modern parcellation
    convention for the insular-opercular transition, not a classical
    architectonic entity.
[ ] **MGB_AFFERENT_GUARD** is present and byte-identical to the left
    sibling's — the medial geniculate body projects to the temporal
    BA 41 (auditory cortex), not to the insular BA 41.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - nociception_and_pain_affect
    - thermoreception
    - interoception
    - autonomic_control
[ ] FUNCTIONAL_DOMAINS **excludes** speech_articulation — the domain
    does not exist on the right (and, independently, BA 41 is
    posterior to the critical territory).
[ ] FUNCTIONAL_DOMAINS **excludes** vestibular_and_self_location
    (right-emphasized at BA 13, not BA 41).
[ ] FUNCTIONAL_DOMAINS **excludes** gustatory (BA 41 is not a
    taste area).
[ ] FUNCTIONAL_DOMAINS **excludes** salience_network and
    social_emotional (anterior insular territories; BA 41 is
    posterior primary sensory cortex).
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis** per domain:
    - nociception → affective_motivational_arousal_pain_response
    - thermoreception → thermoreceptive_autonomic_challenge_
      sympathetic
    - interoception → posterior_primary_interoceptive_autonomic_
      affective_coupling
    - autonomic_control → sympathetic_pressor_tachycardic_pain_
      coupling
[ ] MODERN_CROSSWALK is present, byte-identical to the left
    sibling's.
[ ] CONNECTIVITY documents:
    - VMpo thalamic afferent (primary nociceptive and
      thermoreceptive relay, weighted toward affective-autonomic
      coupling)
    - VPL / VPI thalamic afferent (somatosensory component)
    - **MGB entry with the "naming_collision_boundary_not_insular_
      afferent" tag** (guard against conflation; byte-identical to
      the left)
    - BA 42 and BA 13 intracortical afferents
    - BA 41 → anterior insula intrainsular afferent (affective-
      arousal → full affective experience transfer)
    - BA 41 → hypothalamus (sympathetic, right-specific)
    - BA 41 → NST (sympathetic, right-specific)
    - BA 41 → PAG (sympathetic-weighted on the right)
    - parabrachial → BA 41 pathway (weighted toward sympathetic
      response)
    - callosal traffic to left BA 41 (affective-motivational and
      sympathetic, right-specific)
[ ] CLINICAL_ANCHORS contains the eight right-specific anchors:
    - right_ba41_affective_motivational_pain
    - right_insular_thermoreceptive_autonomic_challenge
    - right_posterior_insular_stroke_pain
    - right_ba41_sympathetic_autonomic_coupling
    - right_insular_opercular_seizures_affective_autonomic
    - insular_opercular_transition_glioma
    - **right_ba41_sudep_arrhythmogenic_dominance**
    - right_insula_thermoreceptive_autonomic_dysregulation
[ ] The **right affective-motivational pain** is documented as the
    primary right BA 41 anchor, with pain anticipation and
    pain-related autonomic arousal as the right-weighted components.
[ ] The **SUDEP arrhythmogenic dominance** is documented as a
    right-emphasized SUDEP anchor — the right posterior insula's
    sympathetic weighting, via the BA 41 → PAG pathway, is
    implicated in peri-ictal fatal arrhythmia. **This anchor is the
    mirror-opposite of the left's `autonomic_stress_vulnerability_
    sudep` anchor, and the asymmetry must not be erased.**
[ ] The **right thermoreceptive autonomic dysregulation** is
    documented as a right-emphasized anchor — impaired sympathetic
    vasoconstrictor and sudomotor responses to cooling.
[ ] The **naming-collision hazard** is documented in the clinical
    anchors as a **surgical and semiological hazard** — the
    surgeon must not confuse the insular BA 41 with the temporal
    BA 41, and pre-surgical workup must distinguish them.
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
[ ] The **forward-declaration caveat text is byte-identical to the
    left sibling's**.
[ ] No SUBDIVISIONS promotion is performed while the circular
    sulcus boundary package does not yet exist.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, region, cytotectonic gradient, NAMING_COLLISION_
    WITH, PARCELATION_CONVENTION, MGB_AFFERENT_GUARD, architectonic
    neighbourhoods, modern crosswalk, FUNCTIONAL_DOMAINS set,
    forward-declaration caveat text) match the left sibling;
    DOMAIN_EMPHASIS, CONNECTIVITY emphasis, and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The SUDEP asymmetry is verified**: the right BA 41 carries an
    arrhythmogenic-weighted anchor, the left BA 41 carries a
    protective-weighted anchor, and neither has been copied
    verbatim from the other.
[ ] Any downstream code that queries "BA 41" must specify the lobe
    — the temporal and insular packages are never conflated, and
    no global BA index merges them.
[ ] Any downstream code that queries auditory afferents to "BA 41"
    must specify the temporal BA 41 — the MGB guard is enforced.
[ ] Any downstream code assigning BA 41 autonomic function must
    route through DOMAIN_EMPHASIS and must weight the right BA 41
    toward **sympathetic** and the left BA 41 toward
    **parasympathetic**.
[ ] Any downstream code querying BA 41 SUDEP contribution must
    weight the right BA 41 as **arrhythmogenic-weighted** and the
    left BA 41 as **protective-weighted** — the two hemispheres
    contribute opposite-direction autonomic influences, and
    averaging them would erase the lateralized signal.
"""