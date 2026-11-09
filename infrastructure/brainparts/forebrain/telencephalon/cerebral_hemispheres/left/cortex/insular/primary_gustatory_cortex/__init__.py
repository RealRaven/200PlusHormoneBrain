"""
Primary Gustatory Cortex (PGC) — Left Hemisphere
=================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── insular
                              └── primary_gustatory_cortex   ← THIS PACKAGE

This is a **leaf cortical-area package** buried within the **insular
operculum** — the region of cortex that lies at the junction of the
anterior insula and the overlying opercula (frontal, parietal, and
temporal). It is the **primary cortical recipient of taste
information** from the thalamic gustatory relay, the parvicellular
division of the ventroposteromedial nucleus (VPMpc)[reference:0].

Unlike the gyri and sulci packages, which describe *folds* and
*grooves*, this package describes a **functional cortical field** that
spans several classical anatomical territories. It is therefore not a
child of ``..gyri`` or ``..sulci`` but a direct child of ``..insular``
— the functional package for the insular lobe.

Parent: ``..insular`` — sibling to ``..insular/insula`` (the broader
insular cortex package) and to the other insular functional fields
(interoceptive, autonomic, social-emotional).

This package is the **structural mirror** of
``../../right/cortex/insular/primary_gustatory_cortex``. The anatomical
fields are broadly symmetric, but the **functional lateralization** and
**clinical significance** diverge substantially between hemispheres.

--------------------------------------------------------------------------------
WHAT THE PGC IS
--------------------------------------------------------------------------------

The primary gustatory cortex is the **cortical area that receives the
most direct projections from the specialized sensory relay nucleus in
the thalamus** for taste — VPMpc[reference:1]. It is the first cortical
stage of the gustatory pathway, the analogue for taste of what V1 is
for vision or A1 for audition.

The PGC is **not a single, sharply delimited cytoarchitectonic area**.
It is a **functional field** that spans:

    anterior insula (dorsal / granular part)
        The most extensive VPMpc projection zone in Old World
        monkeys is to the **dorsal (superior) part of the anterior
        insular cortex** and the adjacent frontal–parietal
        opercula[reference:2]. The projection zone is centred on
        **granular insular cortex** and extends ventrally into
        dysgranular insular cortex and dorsally/laterally into
        dysgranular opercular cortex[reference:3].

    parietal operculum (transitional insula–operculum cortex,
    "area G")
        MEG studies in humans identify the **transition area between
        the parietal operculum and the insula (area G)** as a
        short-latency activation site for taste[reference:4]. Area G
        activation latency differs among tastants, and its magnitude
        scales with tastant concentration[reference:5].

    frontal operculum
        The frontal operculum and anterior insula are activated after
        longer latencies than area G, suggesting they are downstream
        of the primary gustatory response[reference:6].

    base of the central sulcus
        Some MEG studies place a second short-latency activation
        site at the **bottom of the central sulcus (CS)**[reference:7].
        Clinical and physiological studies of patients with ageusia
        or gustatory hallucination suggest the primary gustatory area
        (area G) lies at the **anterior insula or at the base of the
        central sulcus**[reference:8].

The PGC therefore has **overlapping, partially separable
representations** in the anterior insula, parietal operculum (area G),
and possibly the base of the central sulcus. Modern neuroimaging
localizes human primary cortical gustatory areas in the general region
of the **anterior to middle insular cortex and the frontal
operculum**[reference:9].

**A crucial caveat**: **less than 10 % of neurons in the PGC respond to
taste stimuli**; many others respond to other intraoral stimuli[reference:10].
The PGC and adjacent higher-order areas sensitive to gustatory stimuli
cover a large region of cortex, but gustatory neurons contribute to but
do not dominate the processing taking place in these regions
[reference:11]. Taste-responsive neurons in the PGC are **intermingled
among non-taste neurons**, unlike what is seen in other sensory
modalities[reference:12]. The PGC is therefore **not a pure taste
processor** — it is a **multimodal intraoral cortex** in which taste is
one input among many.

**Left-hemisphere specificity**: the left PGC is the hemisphere in
which **taste information from both sides of the tongue converges**.
Damage to the left insula causes an **ipsilateral deficit in taste
intensity but a bilateral deficit in taste recognition**, suggesting
that taste information from both sides of the tongue passes through the
left insula[reference:13]. Left-sided insula strokes appear to be **more
clinically relevant** for taste dysfunction than right-sided
strokes. There is also evidence for a
**predominant left ipsilateral pathway** from the left PGC to the
orbitofrontal cortex under certain conditions (salt taste, right-handed
subjects)[reference:16].

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING GYRI AND CORTICAL TERRITORIES
--------------------------------------------------------------------------------

The PGC is not bounded by sulci in the classical sense — it is a
**functional field** that overlaps several gyral and insular
territories:

    anterior insula (dorsal granular part)   → primary VPMpc
                                               projection zone
    parietal operculum (area G)              → short-latency taste
                                               activation site
    frontal operculum                         → longer-latency taste
                                               activation site
    base of the central sulcus               → possible short-latency
                                               taste site
    postcentral gyrus, most ventral
    (opercular) part — BA 43                 → classical cortical
                                               primary gustatory region
                                               in some parcellations

**BA 43** is the most ventral (opercular) part of the postcentral
gyrus and is identified in some sources as **the cortical primary
gustatory region**[reference:17]. Other sources identify the PGC with
the **anterior insula** or the **transitional cortex between the
insula and the parietal operculum**[reference:18]. The field is
genuinely **distributed** across these territories, and the package
must not pretend to a single crisp boundary.

**Parent-package note**: this package does **not** duplicate the
``..insular/insula`` package. The ``insula`` package describes the
insular lobe's gross anatomy (gyri, sulci, subregions). This package
describes the **functional gustatory field** that spans the insula and
the opercula. The two packages are complementary, not nested.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Territory                                   Brodmann areas
    ------------------------------------------  ------------------
    anterior insula (granular / dysgranular)    (insular areas,
                                                 not BA-numbered
                                                 in classical map)
    parietal operculum / area G                 BA 43 (classical
                                                 gustatory area)
    frontal operculum                           BA 44 / BA 45
                                                 (opercular cortex)
    base of central sulcus                      BA 3b / BA 4
                                                 (transitional)

**BA 43** is the **only classically numbered Brodmann area** associated
with the primary gustatory region[reference:19]. The insular
components of the PGC are **not BA-numbered** in Brodmann's original
map — they belong to the insular allocortex / mesocortex, which
Brodmann did not include in his 1–52 scheme. Modern parcellations
(e.g., the Human Connectome Project's 180-area scheme) assign distinct
insular area labels (e.g., "Ig," "Id," "AAIC") that are not BA
numbers.

**This field is broadly conserved across hemispheres.** BA 43 is
present on both sides, and the insular projection zone is present on
both sides. What differs is the **laterality of the functional
deficit** (see CLINICAL SIGNIFICANCE).

--------------------------------------------------------------------------------
EXTENT (anatomical landmarks and trajectory)
--------------------------------------------------------------------------------

    anterior boundary
        The **limen insulae** — the threshold of the insula, where the
        insular cortex meets the orbitofrontal and temporal cortex.
        The PGC's anterior insular component lies just posterior to
        the limen.

    posterior boundary
        The **posterior insula** is **not** primary gustatory cortex.
        Earlier MEG and EEG studies had located the PGC in more
        posterior parts of the insula, but most recent studies conclude
        that gustatory-evoked signals are **delayed slightly relative
        to those in the middle insula**, implicating the posterior
        insula as an **association area** rather than the primary
        cortex[reference:20].

    dorsal / lateral boundary
        The **opercula** (frontal, parietal, temporal) form the roof
        of the insula. The PGC extends dorsally and laterally into the
        dysgranular opercular cortex and the parietal operculum
        (area G)[reference:21].

    ventral / medial boundary
        The **inferior agranular insula** and the **claustrum** form
        the ventral/medial limit of the PGC proper. The inferior
        agranular insula contains secondary or higher-order gustatory
        areas[reference:22].

The PGC is therefore a **deep, buried cortical field** — it is not
visible on the lateral surface of the brain. It lies beneath the
opercula, at the junction of the insula and the opercular cortex. This
is why **awake surgery for insular lesions** requires careful mapping of
taste function, and why **insular strokes** are the most common cause of
central gustatory dysfunction.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags:

    taste_quality_encoding
        Encoding the identity of tastants (sweet, salty, sour, bitter,
        umami). The PGC shows **chemotopical organization** — different
        taste qualities are represented in partially distinct
        subregions[reference:23]. The **Labelled-Line Model** of
        peripheral taste encoding is supported by PGC responses that
        depend on taste quality[reference:24].

    taste_intensity_encoding
        Encoding the concentration / intensity of tastants. Area G
        activation magnitude increases with tastant concentration
        [reference:25].

    taste_recognition
        Recognizing and identifying tastes. The **left insula** is
        critical for taste recognition **bilaterally** — left insular
        damage produces a bilateral recognition deficit even though
        intensity deficit is ipsilateral[reference:26].

    taste_memory
        Encoding and retrieving taste memories, especially **conditioned
        taste aversion (CTA)**. The PGC / insular cortex is a critical
        structure for encoding and retrieving CTA memory
        [reference:27]. Persistent activity in taste cortex functions as
        a **short-term memory trace** of recent taste experience
        . Protein synthesis in the gustatory cortex is
        required for the **consolidation** of taste memory
        [reference:29].

    taste_novelty_detection
        Detecting unfamiliar tastes. Cholinergic activity in the
        insular (gustatory) cortex is related to **taste novelty**, and
        cholinergic signals initiated by novelty are crucial for taste
        memory formation[reference:30].

    multimodal_intraoral_integration
        Integrating taste with **texture, temperature, and
        somatosensory** information from the oral cavity. Combined
        chemoreception in primary gustatory cortex and general sensation
        in adjacent somatosensory cortex provides overall taste in terms
        of texture and temperature of the food
        [reference:31]. The PGC is adjacent to the somatosensory
        representation of the tongue[reference:32].

    ingestive_decision_making
        Guiding consummatory decisions based on taste. The gustatory
        cortex regulates taste information processing and
        **consummatory decision-making**[reference:33].

    hedonic_valuation_interface
        Interfacing with the orbitofrontal cortex (OFC) and amygdala for
        the **affective valuation** of taste. The left PGC projects
        ipsilaterally to the OFC[reference:34], and the amygdala has
        connections with gustatory cortex in insula and overlying
        operculum[reference:35].

    anticipatory_taste_response
        Neurons in the PGC show **anticipatory activity**, encoding
        expected taste identity and palatability.

These tags map onto the memory subsystem as follows:

    taste_quality_encoding            → memory/stores/short_term (sensory buffer)
    taste_intensity_encoding          → memory/stores/short_term (sensory buffer)
    taste_recognition                 → memory/stores/long_term/explicit/semantic
    taste_memory                      → memory/stores/long_term/implicit/classical_associative_conditioning (CTA)
    taste_novelty_detection           → memory/stores/long_term/implicit/priming
    multimodal_intraoral_integration  → memory/stores/short_term (multisensory buffer)
    ingestive_decision_making         → memory/stores/long_term/implicit/reinforcement_value_based_learning
    hedonic_valuation_interface       → memory/stores/long_term/implicit/emotional_valence
    anticipatory_taste_response       → memory/stores/short_term (prospective buffer)

Note that **taste_memory routes to classical_associative_conditioning**
— the PGC is the cortical substrate of conditioned taste aversion, one
of the most robust forms of associative learning. This is a
**left-hemisphere-specific** routing, because the left insula is the
side that supports bilateral taste recognition and therefore the side
whose CTA memory is most consequential.

--------------------------------------------------------------------------------
CONNECTIVITY (thalamic input and cortical/subcortical outputs)
--------------------------------------------------------------------------------

    thalamic input
        → VPMpc (parvicellular ventroposteromedial nucleus of the
          thalamus), **ipsilateral**
        The VPMpc receives gustatory input from the rostral nucleus of
        the solitary tract (NST) — directly in primates, via the
        parabrachial nucleus (PbN) in rodents
        [reference:37]. The VPMpc projects to the **ipsilateral** PGC
        [reference:38]. The projection zone is centred on granular insular
        cortex and extends into dysgranular insular and opercular
        cortex[reference:39].

    brainstem input (indirect)
        → NST (nucleus of the solitary tract) → VPMpc → PGC
        Taste afferents from cranial nerves VII (facial), IX
        (glossopharyngeal), and X (vagus) synapse in the NST in the
        medulla[reference:40]. In primates, the NST projects directly to
        the VPMpc; in rodents, there is an obligate relay in the
        pontine parabrachial nucleus (PbN)[reference:41].

    cortical outputs
        → orbitofrontal cortex (OFC), **ipsilateral** (left)
            The left PGC projects ipsilaterally to the left OFC
            [reference:42]. This is the **secondary gustatory cortex**,
            where taste identity is combined with reward value and
            cognitive context.
        → anterior insula (adjacent higher-order gustatory areas)
        → frontal operculum

    subcortical outputs
        → amygdala (basolateral nuclei)
            The amygdala has connections with gustatory cortex in
            insula and overlying operculum[reference:43]. This circuit
            supports the **affective valuation** of taste and the
            **conditioned taste aversion** memory.
        → hypothalamus (lateral hypothalamus)
            The PbN projects to the lateral hypothalamus (LH)
            [reference:44], and the PGC → OFC → LH pathway supports
            **feeding behaviour** and **ingestive decision-making**.
        → ventral striatum / nucleus accumbens
            The PGC → OFC → ventral striatum pathway supports the
            **reward value** of taste.

    callosal connections
        → right PGC
        Interhemispheric connections coordinate the two PGCs, which is
        why **left insular damage produces a bilateral taste
        recognition deficit** even though the thalamic input is
        ipsilateral[reference:45]. The left PGC appears to be the
        **dominant hemisphere** for taste recognition.

    hippocampal / parahippocampal connections
        → via the insulo-hippocampal epileptogenic circuit
        The gustatory cortex has interconnections with an
        **insulo-hippocampal circuit**[reference:46], which supports
        taste memory consolidation and is the substrate of
        **eating-reflex seizures**.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_insular_stroke_taste_dysfunction
        **This is the left-PGC anchor par excellence.** Left-sided
        insula strokes are **more clinically relevant** for taste
        dysfunction than right-sided strokes. Damage to
        the left insula causes an **ipsilateral deficit in taste
        intensity but a bilateral deficit in taste recognition**
        [reference:48]. The unexpected bilateral recognition deficit
        suggests that taste information from **both sides of the
        tongue passes through the left insula** — the left PGC is the
        dominant hemisphere for taste recognition[reference:49]. Taste
        dysfunction is significantly associated with **insula
        involvement** (OR = 3.5) and with **left hemisphere lesion**
        (OR = 2.4) in acute and chronic stroke patients[reference:50].

    left_posterior_insula_lesion_taste_and_olfactory_sensitivity
        A **left posterior insula lesion** may affect taste and
        olfactory perception similarly by **increasing sensitivity
        contralateral to the lesion**, possibly via **release from
        inhibition** at the cortical level[reference:51]. This is a
        left-specific pattern; right posterior insula lesions do not
        show the same taste-sensitivity effect.

    gustatory_hallucination_and_insular_lesions
        Gustatory hallucinations — the phantom perception of taste —
        are a recognized symptom of **insular lesions**, especially
        in the context of **epileptic foci**[reference:52]. The PGC is
        the cortical substrate of these hallucinations.

    eating_reflex_seizures
        **Eating-reflex seizures** — seizures triggered by food or
        syrup intake — can arise from the **gustatory cortex**. The
        overlap of the gustatory cortex and the preictal/ictal onset
        zone, defined by early **gamma changes**, has motivated
        successful **resective surgery of the middle short gyrus of
        the insula**[reference:53][reference:54]. The gustatory cortex
        is interconnected with an **insulo-hippocampal epileptogenic
        circuit**[reference:55]. This is a left-hemisphere-relevant
        anchor — the left insula is the more common seizure-onset
        zone for gustatory auras.

    gustatory_aura_in_temporal_lobe_epilepsy
        **Gustatory auras** — brief, stereotyped taste sensations
        preceding a seizure — are a classic symptom of **temporal
        lobe epilepsy** and are attributed to the spread of
        epileptiform activity to the insular gustatory cortex. The
        left PGC is the cortical substrate of these auras.

    surgical_mapping_of_taste_function
        Because the PGC is **buried beneath the opercula**, it is
        not visible during standard cortical mapping. **Awake surgery
        for insular lesions** (tumours, cavernomas, epileptogenic
        zones) requires **direct electrical stimulation** or
        **functional MRI** to identify and preserve the gustatory
        cortex. The left PGC is the more critical side to preserve
        because of its bilateral taste-recognition role.

    conditioned_taste_aversion_therapy
        The PGC's role in **CTA memory** has clinical implications
        for **aversion therapy** (e.g., in alcohol use disorder) and
        for understanding **taste aversions** that develop during
        chemotherapy or radiation therapy. The left PGC is the
        hemisphere in which CTA memory is most strongly encoded.

These anchors are **left-hemisphere-specific** in two senses: (a) the
left insula is the **dominant hemisphere for taste recognition**, and
left insular damage produces a **bilateral** recognition deficit rather
than an ipsilateral one; (b) the left posterior insula lesion produces
a **contralateral increase in taste sensitivity**, a release-from-
inhibition pattern that has not been documented on the right. The right
sibling's docstring carries the right-sided surgical and clinical
emphases.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..insular
    The parent package for the insular lobe. This package is a
    **functional field** within the insular lobe, not a duplicate of
    the lobe's gross anatomy. The ``insula`` package describes the
    insular gyri and sulci; this package describes the gustatory
    functional field that spans the anterior insula and the opercula.

..cortex.prefrontal_cortex
    The **orbitofrontal cortex (OFC)** is the secondary gustatory
    cortex, receiving ipsilateral projections from the left PGC
    [reference:56]. The prefrontal_cortex package must declare the PGC
    as an upstream afferent.

../../subcortical/medial_temporal_lobe/amygdala
    The amygdala (basolateral nuclei) receives projections from the
    gustatory cortex[reference:57]. This circuit supports the
    **affective valuation** of taste and **CTA memory**. The amygdala
    package must declare the PGC as a cortical afferent.

../../subcortical/medial_temporal_lobe/hippocampus
    The gustatory cortex is interconnected with an **insulo-
    hippocampal circuit**[reference:58] that supports taste memory
    consolidation and is the substrate of eating-reflex seizures.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The PGC → OFC → ventral striatum pathway supports the **reward
    value** of taste and **ingestive decision-making**.

../../subcortical/diencephalon/hypothalamus
    The PGC → OFC → lateral hypothalamus pathway supports **feeding
    behaviour**.

../../right/cortex/insular/primary_gustatory_cortex
    The right-hemisphere homologue. The anatomical fields (anterior
    insula, parietal operculum, frontal operculum) are broadly
    symmetric, but the **functional lateralization** diverges — the
    left PGC is dominant for taste recognition, the right PGC does
    not show the same bilateral-recognition effect. The right
    sibling's docstring carries the right-sided clinical emphases.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "primary_gustatory_cortex"
    HEMISPHERE          = "left"
    LOBE                = "insular"

    CORTICAL_TERRITORIES = {
                              "anterior_insula_granular":   True,
                              "parietal_operculum_area_G":  True,
                              "frontal_operculum":          True,
                              "base_of_central_sulcus":     True,
                              "postcentral_BA43":           True,
                          }

    BRODMANN_AREAS      = (43,)   # BA 43 is the only classically
                                  # numbered BA associated with the
                                  # PGC; the insular components are
                                  # not BA-numbered

    THALAMIC_RELAY      = "VPMpc"   # parvicellular ventroposteromedial
                                    # nucleus

    FUNCTIONAL_ROLES    = (
                              "taste_quality_encoding",
                              "taste_intensity_encoding",
                              "taste_recognition",
                              "taste_memory",
                              "taste_novelty_detection",
                              "multimodal_intraoral_integration",
                              "ingestive_decision_making",
                              "hedonic_valuation_interface",
                              "anticipatory_taste_response",
                          )

    CONNECTIVITY        = { ... }   # as specified above

    LATERALIZATION      = "left_dominant_for_taste_recognition"

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "AREA_NAME",
        "HEMISPHERE",
        "LOBE",
        "CORTICAL_TERRITORIES",
        "BRODMANN_AREAS",
        "THALAMIC_RELAY",
        "FUNCTIONAL_ROLES",
        "CONNECTIVITY",
        "LATERALIZATION",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all computation
that references the PGC lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this package in the sense
used by the sulci packages.** The PGC is a functional field, not a
sulcus-bounded territory, so its "bounding" structures are cortical
territories (anterior insula, opercula) rather than gyri. Those
territories are described by the parent ``..insular`` package and by
the frontal/parietal/temporal gyrus packages, all of which already
exist or are being built out in parallel. The PGC package does **not**
depend on any unresolved gyrus name.

The one **open anatomical question** is whether the **base of the
central sulcus** should be treated as a distinct PGC sub-territory.
Current evidence is mixed — some MEG studies identify short-latency
taste activation there, others do not. The package should treat this
as a **conditional territory** (present in some individuals / some
studies) rather than as a canonical component. When the
``..gyri/precentral_gyrus`` and ``..gyri/postcentral_gyrus`` packages
are built out, they should cross-reference the PGC as a **possible
functional overlay** on the base of the central sulcus, not as a
gyral boundary.

--------------------------------------------------------------------------------
PROMOTION RULE (when a functional sub-field becomes a package)
--------------------------------------------------------------------------------

If any single territory within the PGC later needs its own
sub-package — for example, if the **parietal operculum (area G)**
component is found to have a distinct connectivity profile or a
distinct clinical signature — the promotion takes this form:

    primary_gustatory_cortex/
        __init__.py
        parietal_operculum_area_g/
            __init__.py
        anterior_insula_granular/
            __init__.py

Then:

  1. Add the sub-field names to ``SUBDIVISIONS``.
  2. Keep ``CORTICAL_TERRITORIES``, ``BRODMANN_AREAS``, and
     ``CONNECTIVITY`` at the parent level as the **union** of the
     sub-fields.
  3. Each sub-field package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The distributed-field caveat**: the PGC is genuinely distributed
across the anterior insula, parietal operculum, and frontal operculum.
A sub-field promotion must **not** imply that the sub-fields are
anatomically separable in the way that gyri are separable by sulci.
The parent remains the canonical answer to "what is the primary
gustatory cortex?"; the sub-fields are **functional refinements**, not
new anatomical boundaries.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../primary_gustatory_cortex``:

    MUST be identical (broadly):
        The set of cortical territories (anterior insula, parietal
        operculum, frontal operculum, base of central sulcus,
        BA 43).
        The thalamic relay (VPMpc).
        The general connectivity pattern (VPMpc → PGC → OFC;
        PGC → amygdala; PGC → insulo-hippocampal circuit).
        The functional-role taxonomy (taste quality, intensity,
        recognition, memory, novelty, multimodal integration,
        ingestive decision-making, hedonic valuation, anticipatory
        response).

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "left" vs "right"
        LATERALIZATION       left: **dominant for taste recognition**;
                             left insular damage → **bilateral**
                             recognition deficit; right: not dominant
                             for recognition; right insular damage →
                             ipsilateral intensity deficit only.
        CLINICAL_ANCHORS     left: left insular stroke → bilateral
                             recognition deficit; left posterior
                             insula lesion → contralateral sensitivity
                             increase; left insula → dominant CTA
                             memory substrate; right: right-sided
                             surgical and clinical emphases (see
                             right sibling).
        CONNECTIVITY         same bundle names; the left PGC has
                             **ipsilateral projection to OFC** (left
                             PGC → left OFC), and the left insula
                             receives **bilateral** taste information
                             via callosal connections.

**The left-dominance for taste recognition is the single most
important entry in this contract.** The left PGC is not merely the
mirror of the right — it is the **dominant hemisphere** for recognizing
what a taste is, even though both hemispheres receive ipsilateral
thalamic input. Any downstream code that assigns taste-recognition
function must weight the left PGC more heavily, and any code that
computes a "taste recognition score" must not average left and right
PGC function — averaging would destroy the lateralized signal.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "primary_gustatory_cortex".
[ ] HEMISPHERE is "left".
[ ] LOBE is "insular".
[ ] CORTICAL_TERRITORIES correctly lists the anterior insula
    (granular), parietal operculum (area G), frontal operculum, base
    of central sulcus, and postcentral BA 43.
[ ] BRODMANN_AREAS is (43,) — BA 43 is the only classically numbered
    BA associated with the PGC; the insular components are not
    BA-numbered.
[ ] THALAMIC_RELAY is "VPMpc".
[ ] FUNCTIONAL_ROLES contains all nine left-specific tags:
    taste_quality_encoding, taste_intensity_encoding,
    taste_recognition, taste_memory, taste_novelty_detection,
    multimodal_intraoral_integration, ingestive_decision_making,
    hedonic_valuation_interface, anticipatory_taste_response.
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY documents the **ipsilateral VPMpc input**, the
    **ipsilateral OFC output**, the **amygdala** projection, the
    **insulo-hippocampal circuit**, and the **callosal** connection
    to the right PGC.
[ ] LATERALIZATION is "left_dominant_for_taste_recognition".
[ ] CLINICAL_ANCHORS contains the seven left-specific anchors:
    left_insular_stroke_taste_dysfunction,
    left_posterior_insula_lesion_taste_and_olfactory_sensitivity,
    gustatory_hallucination_and_insular_lesions,
    eating_reflex_seizures, gustatory_aura_in_temporal_lobe_epilepsy,
    surgical_mapping_of_taste_function,
    conditioned_taste_aversion_therapy.
[ ] The **bilateral taste-recognition deficit** from left insular
    damage is explicitly documented — this is the left-specific
    functional asymmetry.
[ ] The **conditional** status of the base-of-central-sulcus
    territory is documented as an open question, not as a canonical
    component.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (territories, thalamic relay, connectivity pattern, functional
    roles) match the right sibling; the lateralization, clinical
    anchors, and callosal connectivity deliberately differ.
[ ] Any downstream code assigning taste-recognition function is
    required to weight the left PGC more heavily — averaging left and
    right would erase the lateralized signal.
"""