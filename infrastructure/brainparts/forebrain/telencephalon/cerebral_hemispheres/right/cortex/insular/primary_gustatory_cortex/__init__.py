"""
Primary Gustatory Cortex (PGC) — Right Hemisphere
==================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── insular
                              └── primary_gustatory_cortex   ← THIS PACKAGE

This is a **leaf cortical-area package** buried within the **insular
operculum** — the region of cortex that lies at the junction of the
anterior insula and the overlying opercula (frontal, parietal, and
temporal). It is the **primary cortical recipient of taste
information** from the thalamic gustatory relay, the parvicellular
division of the ventroposteromedial nucleus (VPMpc).

Unlike the gyri and sulci packages, which describe *folds* and
*grooves*, this package describes a **functional cortical field** that
spans several classical anatomical territories. It is therefore not a
child of ``..gyri`` or ``..sulci`` but a direct child of ``..insular``
— the functional package for the insular lobe.

Parent: ``..insular`` — sibling to ``..insular/insula`` (the broader
insular cortex package) and to the other insular functional fields
(interoceptive, autonomic, social-emotional).

This package is the **structural mirror** of
``../../left/cortex/insular/primary_gustatory_cortex``. The anatomical
fields and the general connectivity plan are broadly symmetric, but the
**functional lateralization**, **clinical signature**, and
**intensity-processing emphasis** diverge substantially between
hemispheres.

--------------------------------------------------------------------------------
WHAT THE PGC IS
--------------------------------------------------------------------------------

The primary gustatory cortex is the **cortical area that receives the
most direct projections from the specialized sensory relay nucleus in
the thalamus** for taste — VPMpc. It is the first cortical
stage of the gustatory pathway, the analogue for taste of what V1 is
for vision or A1 for audition.

The PGC is **not a single, sharply delimited cytoarchitectonic area**.
It is a **functional field** that spans:

    anterior insula (dorsal / granular part)
        The most extensive VPMpc projection zone in Old World
        monkeys is to the **dorsal (superior) part of the anterior
        insular cortex** and the adjacent frontal–parietal
        opercula. The projection zone is centred on
        **granular insular cortex** and extends ventrally into
        dysgranular insular cortex and dorsally/laterally into
        dysgranular opercular cortex.

    parietal operculum (transitional insula–operculum cortex,
    "area G")
        MEG studies in humans identify the **transition area between
        the parietal operculum and the insula (area G)** as a
        short-latency activation site for taste. Area G
        activation latency differs among tastants, and its magnitude
        scales with tastant concentration.

    frontal operculum
        The frontal operculum and anterior insula are activated after
        longer latencies than area G, suggesting they are downstream
        of the primary gustatory response.

    base of the central sulcus
        Some MEG studies place a second short-latency activation
        site at the **bottom of the central sulcus (CS)**.
        Clinical and physiological studies of patients with ageusia
        or gustatory hallucination suggest the primary gustatory area
        (area G) lies at the **anterior insula or at the base of the
        central sulcus**.

    caudolateral orbitofrontal cortex (secondary taste area)
        **This is a right-hemisphere-specific emphasis.** A
        meta-analysis of human functional neuroimaging studies found
        that **only two peaks, both in the right hemisphere, were
        observed in the caudolateral orbitofrontal cortex** — the
        region likely homologous to the secondary taste area
        described in monkeys. Overall, **significantly more
        taste-related peaks originated from the right hemisphere**,
        suggesting an asymmetrical cortical representation of taste
        favouring the right hemisphere at the secondary
        (orbitofrontal) stage.

**A crucial caveat**: **less than 10 % of neurons in the PGC respond
to taste stimuli**; many others respond to other intraoral stimuli.
The PGC and adjacent higher-order areas sensitive to gustatory stimuli
cover a large region of cortex, but gustatory neurons contribute to but
do not dominate the processing taking place in these regions.
Taste-responsive neurons in the PGC are **intermingled among non-taste
neurons**, unlike what is seen in other sensory modalities. The PGC is
therefore **not a pure taste processor** — it is a **multimodal
intraoral cortex** in which taste is one input among many.

**Right-hemisphere specificity**: the right PGC is the hemisphere in
which **taste intensity and concentration processing is dominant**.
fMRI studies show that **representations of the presence of a taste
stimulus and its pleasantness dominate in the left insular cortex,
whereas taste concentration processing dominates in the right insular
cortex**. The right insula is **more sensitive to intensity variations**
across concentrations, albeit with a **nonlinear response profile**.
The right PGC therefore complements the left: the left recognizes
*what* a taste is, the right tracks *how strong* it is.

The clinical consequence is equally specific: **damage to the right
insula produces ipsilateral taste recognition and intensity
deficits** — a **unilateral** pattern, not the bilateral recognition
deficit seen after left insular damage. Right insular strokes are
less frequently associated with taste disturbance overall
(**4 % of right IS vs 19 % of left IS**), consistent with the
left’s dominant role in recognition, but when the right PGC is
affected, the deficit is a **pure ipsilateral intensity/recognition
loss**.

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
gustatory region**. Other sources identify the PGC with
the **anterior insula** or the **transitional cortex between the
insula and the parietal operculum**. The field is
genuinely **distributed** across these territories, and the package
must not pretend to a single crisp boundary.

**Right-specific territory note**: the **caudolateral
orbitofrontal cortex** is more strongly associated with the right
PGC than with the left. The meta-analytic finding that
taste-related peaks in the caudolateral OFC are **right-lateralized**
means the right PGC’s downstream territory extends into a region that
the left PGC’s downstream territory does not emphasize to the same
degree. This is captured in ``CORTICAL_TERRITORIES`` as a
right-emphasized entry.

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
    caudolateral orbitofrontal cortex           BA 11 / BA 47
    (secondary taste area, right-emphasized)    (orbitofrontal)

**BA 43** is the **only classically numbered Brodmann area** associated
with the primary gustatory region. The insular
components of the PGC are **not BA-numbered** in Brodmann's original
map — they belong to the insular allocortex / mesocortex, which
Brodmann did not include in his 1–52 scheme. Modern parcellations
(e.g., the Human Connectome Project's 180-area scheme) assign distinct
insular area labels (e.g., "Ig," "Id," "AAIC") that are not BA
numbers.

**This field is broadly conserved across hemispheres**, but the
**caudolateral OFC entry** carries a right-specific emphasis: the
meta-analytic right-lateralization of OFC taste peaks means the right
PGC’s BA 11/47 downstream territory is more consistently engaged than
the left’s.

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
        cortex. **Right-specific note**: the right middle–posterior
        insula is one of the two clusters specialized for **taste
        intensity processing**, exhibiting a highly nonlinear profile
        across concentrations. The right PGC’s intensity-related
        activity therefore extends slightly more posteriorly into the
        middle–posterior insula than the left’s.

    dorsal / lateral boundary
        The **opercula** (frontal, parietal, temporal) form the roof
        of the insula. The PGC extends dorsally and laterally into the
        dysgranular opercular cortex and the parietal operculum
        (area G).

    ventral / medial boundary
        The **inferior agranular insula** and the **claustrum** form
        the ventral/medial limit of the PGC proper. The inferior
        agranular insula contains secondary or higher-order gustatory
        areas.

The PGC is therefore a **deep, buried cortical field** — it is not
visible on the lateral surface of the brain. It lies beneath the
opercula, at the junction of the insula and the opercular cortex. This
is why **awake surgery for insular lesions** requires careful mapping of
taste function, and why **insular strokes** are the most common cause of
central gustatory dysfunction.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags.
The **right-specific emphasis** is on **intensity / concentration
processing** and **ipsilateral recognition**, not on the bilateral
recognition role that dominates the left package.

    taste_intensity_encoding          ← PRIMARY RIGHT ROLE
        Encoding the concentration / intensity of tastants. **Taste
        concentration processing dominates in the right insular
        cortex**, and the right insula is **more sensitive to
        intensity variations** across concentrations, albeit with a
        nonlinear response profile. Area G activation
        magnitude increases with tastant concentration.

    taste_quality_encoding
        Encoding the identity of tastants (sweet, salty, sour, bitter,
        umami). The PGC shows **chemotopical organization** — different
        taste qualities are represented in partially distinct
        subregions. The **Labelled-Line Model** of
        peripheral taste encoding is supported by PGC responses that
        depend on taste quality. On the right, quality encoding is
        **ipsilateral** to the stimulated tongue side.

    taste_recognition_ipsilateral     ← RIGHT-SPECIFIC VARIANT
        Recognizing and identifying tastes **on the ipsilateral side
        only**. Damage to the right insula produces an **ipsilateral
        taste recognition deficit**, not a bilateral one.
        This is the mirror-image of the left PGC’s **bilateral**
        recognition role.

    taste_memory
        Encoding and retrieving taste memories, especially **conditioned
        taste aversion (CTA)**. The PGC / insular cortex is a critical
        structure for encoding and retrieving CTA memory.
        Persistent activity in taste cortex functions as
        a **short-term memory trace** of recent taste experience.
        Protein synthesis in the gustatory cortex is
        required for the **consolidation** of taste memory.
        **Right-specific emphasis**: right insula glucose metabolism is
        lower in the **low taste-cognition subgroup** of Alzheimer’s
        disease patients, suggesting the right insula is the more
        sensitive side for **taste cognition** (the memory-linked
        aspect of taste processing).

    taste_novelty_detection
        Detecting unfamiliar tastes. Cholinergic activity in the
        insular (gustatory) cortex is related to **taste novelty**, and
        cholinergic signals initiated by novelty are crucial for taste
        memory formation.

    multimodal_intraoral_integration
        Integrating taste with **texture, temperature, and
        somatosensory** information from the oral cavity. Combined
        chemoreception in primary gustatory cortex and general sensation
        in adjacent somatosensory cortex provides overall taste in terms
        of texture and temperature of the food.
        The PGC is adjacent to the somatosensory representation of the
        tongue.

    ingestive_decision_making
        Guiding consummatory decisions based on taste. The gustatory
        cortex regulates taste information processing and
        **consummatory decision-making**.

    hedonic_valuation_interface
        Interfacing with the orbitofrontal cortex (OFC) and amygdala for
        the **affective valuation** of taste. The right PGC projects
        ipsilaterally to the **right caudolateral OFC**, which is the
        more consistently right-lateralized secondary taste area.
        The basolateral amygdala (BLA) sends direct input to the PGC
        carrying **hedonic value** and **anticipatory predictive cues**.

    anticipatory_taste_response
        Neurons in the PGC show **anticipatory activity**, encoding
        expected taste identity and palatability. The BLA input to the
        PGC is a major source of this anticipatory signal.

These tags map onto the memory subsystem as follows:

    taste_intensity_encoding          → memory/stores/short_term (sensory buffer)
    taste_quality_encoding            → memory/stores/short_term (sensory buffer)
    taste_recognition_ipsilateral     → memory/stores/long_term/explicit/semantic
    taste_memory                      → memory/stores/long_term/implicit/classical_associative_conditioning (CTA)
    taste_novelty_detection           → memory/stores/long_term/implicit/priming
    multimodal_intraoral_integration  → memory/stores/short_term (multisensory buffer)
    ingestive_decision_making         → memory/stores/long_term/implicit/reinforcement_value_based_learning
    hedonic_valuation_interface       → memory/stores/long_term/implicit/emotional_valence
    anticipatory_taste_response       → memory/stores/short_term (prospective buffer)

Note that **taste_intensity_encoding** is the first-listed and
dominant routing on the right, whereas on the left the first-listed
role is **taste_recognition**. This reflects the right PGC’s
specialization for concentration processing and the left PGC’s
specialization for identity/recognition.

--------------------------------------------------------------------------------
CONNECTIVITY (thalamic input and cortical/subcortical outputs)
--------------------------------------------------------------------------------

    thalamic input
        → VPMpc (parvicellular ventroposteromedial nucleus of the
          thalamus), **ipsilateral**
        The VPMpc receives gustatory input from the rostral nucleus of
        the solitary tract (NST) — directly in primates, via the
        parabrachial nucleus (PbN) in rodents. The VPMpc projects to
        the **ipsilateral** PGC. The projection zone is centred on
        granular insular cortex and extends into dysgranular insular
        and opercular cortex. **The PbN projects bilaterally to the
        VPMpc**, which is why each hemisphere receives taste
        information from both sides of the tongue even though the
        thalamocortical projection is ipsilateral.

    limbic input (right-emphasized)
        → basolateral amygdala (BLA) → right PGC
        The BLA sends a **direct projection** to the PGC carrying
        information on the **hedonic value** of a taste stimulus as
        well as **anticipatory predictive cues**. Thalamic (VPMpc)
        and limbic (BLA) inputs **converge onto the same PGC
        neurons**, allowing the right PGC to integrate chemosensory
        identity with affective value. This limbic input is a
        core component of the PGC’s role in CTA and hedonic
        valuation.

    brainstem input (indirect)
        → NST → VPMpc → PGC
        Taste afferents from cranial nerves VII (facial), IX
        (glossopharyngeal), and X (vagus) synapse in the NST in the
        medulla. In primates, the NST projects directly to
        the VPMpc; in rodents, there is an obligate relay in the
        pontine parabrachial nucleus (PbN).

    cortical outputs
        → right caudolateral orbitofrontal cortex (OFC),
          **ipsilateral**
            The right PGC projects ipsilaterally to the right OFC.
            **The caudolateral OFC is the more consistently right-
            lateralized secondary taste area**: meta-analysis shows
            that only two taste-related peaks in the caudolateral OFC
            were observed, and **both were in the right hemisphere**.
            This makes the right PGC → right caudolateral OFC
            projection the more prominent secondary-taste pathway.
        → anterior insula (adjacent higher-order gustatory areas)
        → frontal operculum

    subcortical outputs
        → amygdala (basolateral nuclei)
            The amygdala has connections with gustatory cortex in
            insula and overlying operculum. This circuit
            supports the **affective valuation** of taste and the
            **conditioned taste aversion** memory.
        → hypothalamus (lateral hypothalamus)
            The PGC → OFC → LH pathway supports **feeding behaviour**
            and **ingestive decision-making**.
        → ventral striatum / nucleus accumbens
            The PGC → OFC → ventral striatum pathway supports the
            **reward value** of taste.

    callosal connections
        → left PGC
        Interhemispheric connections coordinate the two PGCs. **On
        the right, the callosal route is the less behaviourally
        consequential direction**: taste information from the right
        tongue crosses to the left PGC for bilateral recognition,
        but the right PGC does not reciprocally support bilateral
        recognition. The right PGC’s callosal traffic is therefore
        primarily **modulatory** rather than **recognition-critical**.

    hippocampal / parahippocampal connections
        → via the insulo-hippocampal epileptogenic circuit
        The gustatory cortex has interconnections with an
        **insulo-hippocampal circuit**, which supports
        taste memory consolidation and is the substrate of
        **eating-reflex seizures**. Right insular eating-reflex
        seizures have been successfully resected from the right
        middle short gyrus.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_insular_stroke_ipsilateral_taste_deficit
        **This is the right-PGC anchor par excellence.** Damage to the
        **right insula produces ipsilateral taste recognition and
        intensity deficits** — a **unilateral** pattern, in contrast
        to the left insula’s bilateral recognition deficit. This
        is the cleanest double dissociation in the human gustatory
        system: left insula → bilateral recognition, right insula →
        ipsilateral recognition and intensity. The right PGC is
        therefore the hemisphere that **tracks the strength of a taste
        on the same side of the tongue**, while the left is the
        hemisphere that **identifies what the taste is regardless of
        side**.

    right_taste_disturbance_lower_prevalence
        Taste disturbance occurs in **4 % of right insular strokes**
        versus **19 % of left insular strokes**. The
        lower prevalence on the right is consistent with the left’s
        dominant role in recognition, but it also means that
        **right-sided taste deficits are more likely to be
        under-recognized** — a patient with a right insular stroke may
        have a subtle ipsilateral intensity loss that never reaches
        clinical attention.

    right_insular_seizures_dysgeusia
        **Right insular seizures** can present with **dysgeusia**
        (distorted taste) together with **contralateral somatosensory
        phenomena**. Intracranial recording has documented simple
        partial seizures originating in the right insula and
        characterized by this pattern. This is a
        right-specific semiology: the dysgeusia is the taste
        manifestation of an insular-onset seizure, and its
        co-occurrence with contralateral somatosensory symptoms
        points to the right insula’s proximity to the somatosensory
        operculum.

    right_eating_reflex_seizures
        **Eating-reflex seizures** — seizures triggered by food or
        syrup intake — have been successfully treated by **resection
        of the middle short gyrus of the right insula**. This
        is a right-specific surgical anchor: the right gustatory
        cortex is a documented seizure-onset zone for this rare
        reflex epilepsy, and the right middle short gyrus is the
        resection target.

    right_caudolateral_ofc_secondary_taste_area
        Meta-analysis of human functional neuroimaging studies found
        that **taste-related peaks in the caudolateral
        orbitofrontal cortex are right-lateralized** — only two peaks
        were observed, and both were in the right hemisphere. This
        makes the **right caudolateral OFC the dominant secondary
        taste area** in humans, and the right PGC → right caudolateral
        OFC projection the more prominent secondary-taste pathway.
        This is a right-specific connectivity–clinical anchor with no
        symmetric left counterpart.

    right_insula_taste_cognition_alzheimers
        In Alzheimer’s disease, **glucose metabolism in the right
        insula is lower in the low taste-cognition subgroup**. This
        links the right insula specifically to **taste cognition** —
        the memory-linked, food-recognition aspect of taste
        processing — rather than to raw taste perception. The right
        PGC is therefore the more sensitive side for the **cognitive
        complications of taste** in dementia.

    right_insula_bulimia_bitter_sensitivity
        fMRI studies in bulimia nervosa patients show **reduced
        sensitivity to bitter stimuli in the right insular cortex**,
        indicating that right insular dysfunction in taste processing
        may contribute to the disorder’s altered food reward
        processing. This is a right-specific
        psychiatric anchor: the right insula’s intensity-processing
        role makes it the side where bitter-sensitivity changes are
        most detectable in eating disorders.

These anchors are **right-hemisphere-specific** in two senses: (a) the
right insula produces an **ipsilateral** taste deficit, not the
bilateral recognition deficit of the left; (b) the right caudolateral
OFC, right insular dysgeusia/eating-reflex seizures, and right insular
taste-cognition hypometabolism are right-lateralized findings with no
symmetric left counterpart. The left sibling’s docstring carries the
bilateral recognition deficit and the left-dominant salt/hedonic
judgment findings.

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
    cortex, receiving ipsilateral projections from the right PGC.
    The **right caudolateral OFC** is the more consistently right-
    lateralized secondary taste area in humans. The
    prefrontal_cortex package must declare the PGC as an upstream
    afferent and must note the right-lateralized OFC emphasis.

../../subcortical/medial_temporal_lobe/amygdala
    The **basolateral amygdala (BLA)** sends a **direct projection**
    to the PGC carrying hedonic value and anticipatory predictive
    cues. Thalamic and limbic inputs converge onto the same PGC
    neurons. The amygdala package must declare the PGC as a
    cortical target and must note the BLA → PGC hedonic-value
    pathway.

../../subcortical/medial_temporal_lobe/hippocampus
    The gustatory cortex is interconnected with an **insulo-
    hippocampal circuit** that supports taste memory
    consolidation and is the substrate of eating-reflex seizures.
    Right insular eating-reflex seizures have been resected from the
    right middle short gyrus.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The PGC → OFC → ventral striatum pathway supports the **reward
    value** of taste and **ingestive decision-making**.

../../subcortical/diencephalon/hypothalamus
    The PGC → OFC → lateral hypothalamus pathway supports **feeding
    behaviour**.

../../left/cortex/insular/primary_gustatory_cortex
    The left-hemisphere homologue. The anatomical fields and the
    general connectivity plan are broadly symmetric, but the
    **functional lateralization** diverges — the left PGC is dominant
    for **taste recognition** (bilateral), the right PGC is dominant
    for **taste intensity/concentration** (ipsilateral). The left
    sibling’s docstring carries the left-specific clinical emphases
    (bilateral recognition deficit, salt/hedonic judgment deficits,
    left posterior insula release-from-inhibition).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "primary_gustatory_cortex"
    HEMISPHERE          = "right"
    LOBE                = "insular"

    CORTICAL_TERRITORIES = {
                              "anterior_insula_granular":   True,
                              "parietal_operculum_area_G":  True,
                              "frontal_operculum":          True,
                              "base_of_central_sulcus":     True,
                              "postcentral_BA43":           True,
                              "caudolateral_OFC_right_emphasized": True,
                          }

    BRODMANN_AREAS      = (43,)   # BA 43 is the only classically
                                  # numbered BA associated with the
                                  # PGC; the insular components are
                                  # not BA-numbered. The caudolateral
                                  # OFC entry is BA 11/47 but is a
                                  # downstream secondary area, not the
                                  # PGC proper.

    THALAMIC_RELAY      = "VPMpc"   # parvicellular ventroposteromedial
                                    # nucleus

    FUNCTIONAL_ROLES    = (
                              "taste_intensity_encoding",   # PRIMARY
                              "taste_quality_encoding",
                              "taste_recognition_ipsilateral",
                              "taste_memory",
                              "taste_novelty_detection",
                              "multimodal_intraoral_integration",
                              "ingestive_decision_making",
                              "hedonic_valuation_interface",
                              "anticipatory_taste_response",
                          )

    CONNECTIVITY        = { ... }   # as specified above, including
                                    # the BLA → PGC limbic input and
                                    # the right-caudolateral-OFC
                                    # emphasis

    LATERALIZATION      = "right_dominant_for_taste_intensity_concentration"

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
sulcus-bounded territory, so its “bounding” structures are cortical
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
studies) rather than as a canonical component.

The **right caudolateral OFC** entry is **not** a forward reference: the
prefrontal cortex package already exists, and the OFC is described
there. The PGC package should cross-reference the OFC package and flag
the right-lateralized secondary-taste emphasis.

--------------------------------------------------------------------------------
PROMOTION RULE (when a functional sub-field becomes a package)
--------------------------------------------------------------------------------

If any single territory within the PGC later needs its own
sub-package — for example, if the **right middle–posterior insula**
intensity cluster is found to have a distinct connectivity profile or
a distinct clinical signature — the promotion takes this form:

    primary_gustatory_cortex/
        __init__.py
        middle_posterior_insula_intensity/
            __init__.py
        anterior_insula_granular/
            __init__.py

Then:

  1. Add the sub-field names to ``SUBDIVISIONS``.
  2. Keep ``CORTICAL_TERRITORIES``, ``BRODMANN_AREAS``, and
     ``CONNECTIVITY`` at the parent level as the **union** of the
     sub-fields.
  3. Each sub-field package declares its own restricted versions.
  4. Mirror the promotion on the left side in the same commit.

**The distributed-field caveat**: the PGC is genuinely distributed
across the anterior insula, parietal operculum, and frontal operculum.
A sub-field promotion must **not** imply that the sub-fields are
anatomically separable in the way that gyri are separable by sulci.
The parent remains the canonical answer to “what is the primary
gustatory cortex?”; the sub-fields are **functional refinements**, not
new anatomical boundaries.

**Right-specific promotion note**: if the **middle–posterior insula
intensity cluster** is promoted, it is a **right-emphasized** sub-field.
The left middle insula also contains an intensity cluster, but the
right cluster is the one more strongly associated with **concentration
processing** and **nonlinear intensity response**. The promotion must
not imply that the left lacks an intensity sub-field — it must
represent the right as the **dominant** intensity sub-field.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../primary_gustatory_cortex``:

    MUST be identical (broadly):
        The set of cortical territories (anterior insula, parietal
        operculum, frontal operculum, base of central sulcus,
        BA 43).
        The thalamic relay (VPMpc).
        The general connectivity pattern (VPMpc → PGC → OFC;
        PGC → amygdala; PGC → insulo-hippocampal circuit; BLA → PGC).
        The functional-role taxonomy (quality, recognition, memory,
        novelty, multimodal integration, ingestive decision-making,
        hedonic valuation, anticipatory response).

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "right" vs "left"
        LATERALIZATION       right: **dominant for taste intensity /
                             concentration**; right insular damage →
                             **ipsilateral** recognition and intensity
                             deficits; left: dominant for **taste
                             recognition** (bilateral); left insular
                             damage → ipsilateral intensity but
                             **bilateral** recognition deficit.
        PRIMARY_ROLE         right: taste_intensity_encoding (first-
                             listed role); left: taste_recognition
                             (first-listed role).
        CLINICAL_ANCHORS     right: ipsilateral recognition/intensity
                             deficit, lower stroke prevalence (4 % vs
                             19 %), right insular dysgeusia seizures,
                             right eating-reflex seizures (resection of
                             middle short gyrus), right caudolateral
                             OFC secondary taste area, right insula
                             taste-cognition hypometabolism in AD,
                             right insula bitter-sensitivity change in
                             bulimia; left: bilateral recognition
                             deficit, salt/hedonic judgment deficits,
                             left posterior insula release-from-
                             inhibition, left-dominant CTA memory.
        CONNECTIVITY         same bundle names; the right PGC →
                             **right caudolateral OFC** pathway is the
                             more consistently right-lateralized
                             secondary-taste projection; the **BLA →
                             right PGC** limbic input is the substrate
                             of hedonic-value and anticipatory
                             signaling; the callosal traffic from the
                             right PGC is primarily **modulatory**
                             rather than recognition-critical.

**The right-dominance for taste intensity/concentration is the single
most important entry in this contract.** The right PGC is not merely
the mirror of the left — it is the **dominant hemisphere** for tracking
*how strong* a taste is, even though both hemispheres receive
ipsilateral thalamic input. Any downstream code that assigns taste-
intensity function must weight the right PGC more heavily, and any code
that computes a “taste intensity score” must not average left and right
PGC function — averaging would destroy the lateralized signal. The
mirror-image rule applies to taste *recognition*: the left PGC is
dominant for *what* the taste is, and must be weighted more heavily for
recognition.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "primary_gustatory_cortex".
[ ] HEMISPHERE is "right".
[ ] LOBE is "insular".
[ ] CORTICAL_TERRITORIES correctly lists the anterior insula
    (granular), parietal operculum (area G), frontal operculum, base
    of central sulcus, postcentral BA 43, and the **right-emphasized
    caudolateral OFC**.
[ ] BRODMANN_AREAS is (43,) — BA 43 is the only classically numbered
    BA associated with the PGC proper; the caudolateral OFC entry is
    downstream and not part of the PGC proper.
[ ] THALAMIC_RELAY is "VPMpc".
[ ] FUNCTIONAL_ROLES lists **taste_intensity_encoding first** — the
    right PGC’s primary specialization — followed by
    taste_quality_encoding, **taste_recognition_ipsilateral**,
    taste_memory, taste_novelty_detection,
    multimodal_intraoral_integration, ingestive_decision_making,
    hedonic_valuation_interface, anticipatory_taste_response.
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY documents the **ipsilateral VPMpc input**, the
    **BLA → PGC limbic input** (hedonic value and anticipatory cues),
    the **ipsilateral right caudolateral OFC output** (right-
    lateralized secondary taste area), the **amygdala** projection,
    the **insulo-hippocampal circuit**, and the **callosal**
    connection to the left PGC (modulatory rather than recognition-
    critical).
[ ] LATERALIZATION is "right_dominant_for_taste_intensity_concentration".
[ ] CLINICAL_ANCHORS contains the seven right-specific anchors:
    right_insular_stroke_ipsilateral_taste_deficit,
    right_taste_disturbance_lower_prevalence (4 % vs 19 %),
    right_insular_seizures_dysgeusia,
    right_eating_reflex_seizures (middle short gyrus resection),
    right_caudolateral_ofc_secondary_taste_area,
    right_insula_taste_cognition_alzheimers,
    right_insula_bulimia_bitter_sensitivity.
[ ] The **ipsilateral taste recognition and intensity deficit** from
    right insular damage is explicitly documented as the mirror-image
    of the left’s bilateral recognition deficit.
[ ] The **lower prevalence of taste disturbance after right insular
    stroke (4 %)** is documented, together with the under-recognition
    caveat.
[ ] The **right-lateralized caudolateral OFC secondary taste area**
    is documented as a right-specific connectivity–clinical anchor.
[ ] The **right insula taste-cognition hypometabolism in Alzheimer’s**
    is documented as a right-specific dementia anchor.
[ ] The **conditional** status of the base-of-central-sulcus
    territory is documented as an open question, not as a canonical
    component.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (territories, thalamic relay, connectivity pattern, functional-
    role taxonomy) match the left sibling; the lateralization, primary
    role ordering, clinical anchors, and right-caudolateral-OFC
    emphasis deliberately differ.
[ ] Any downstream code assigning taste-intensity function is
    required to weight the right PGC more heavily; any downstream code
    assigning taste-recognition function is required to weight the
    left PGC more heavily. Averaging left and right would erase both
    lateralized signals.
"""