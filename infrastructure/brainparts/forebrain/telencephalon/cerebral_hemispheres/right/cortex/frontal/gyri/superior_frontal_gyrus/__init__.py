"""
Superior Frontal Gyrus (SFG) — Right Hemisphere
================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── frontal
                              └── gyri
                                    └── superior_frontal_gyrus   ← THIS PACKAGE

This is a **leaf gyrus** package: it has no child packages. Its internal
sub-structure is expressed through the ``BRODMANN_AREAS`` registry, not
through nested folders. If any Brodmann sub-region later grows enough
machinery to warrant its own package (e.g. the supplementary motor area
as a separate ``supplementary_motor_area/``), it should be promoted to a
sub-package and listed in ``SUBDIVISIONS`` — see the promotion rule at
the bottom.

Parent: ``..gyri`` — sibling to ``inferior_frontal_gyrus`` and
``middle_frontal_gyrus``.

This package is the **structural mirror** of
``../../left/cortex/frontal/gyri/superior_frontal_gyrus``. Structural
fields are identical by contract; functional fields diverge by design.

--------------------------------------------------------------------------------
WHAT THE SFG IS
--------------------------------------------------------------------------------

The superior frontal gyrus is the **dorsal-most frontal gyrus**, bounded:

    dorsally    by the superior margin of the hemisphere, where the gyrus
                curves over onto the medial surface
    ventrally   by the superior frontal sulcus (separating it from MFG)
    caudally    by the precentral sulcus / superior precentral sulcus
    rostrally  continuing onto the medial frontal pole (frontopolar
                cortex, BA 10)

Unlike the IFG and MFG, the SFG is **not confined to the lateral
surface**. It wraps dorsally over the hemisphere and continues onto the
**medial frontal wall**, where it hosts the supplementary motor area
(SMA), the pre-supplementary motor area (pre-SMA), and the medial
frontopolar cortex (part of the default-mode network). The right SFG is
therefore the anatomical bridge between the right lateral frontal
convexity and the right medial frontal wall — the **mirror** of the left
bridge, but with **affective and visuospatial** emphasis rather than
verbal-propositional emphasis.

Clinically, right SFG damage produces **left-hand apraxia / loss of
self-initiated left-hand movement** (if right SMA is involved),
**spatial neglect** (especially with right FEF / right pre-SMA
involvement), **affective aprosodia of gesture**, **impaired
autobiographical memory retrieval**, **reduced affective theory of
mind**, and **disrupted spatial prospective memory**. The cluster is
distinct from the left SFG's "loss of will to act verbally" — right SFG
damage is better described as "loss of spatial / affective self-
initiation."

--------------------------------------------------------------------------------
CYTOARCHITECTONIC PARCELLATION (BRODMANN AREAS)
--------------------------------------------------------------------------------

The SFG spans four Brodmann areas. The BA numbers are identical to the
left hemisphere (Brodmann's map is numerically symmetric); the functional
annotations differ.

    BA 6    medial SFG (and lateral premotor strip along the dorsal
            convexity)
        Hosts the **right supplementary motor area (SMA)** and the
        **right pre-supplementary motor area (pre-SMA)** on its medial
        aspect, plus the dorsal premotor strip on its lateral aspect.
        The right SMA is the substrate of **self-initiated left-hand
        movement**, **bimanual coordination** (subordinate to left
        SMA, but critical for the **left hand's contribution** to
        bimanual tasks), **postural stabilization** during movement,
        and **spatial action sequencing** (e.g. navigating around an
        obstacle). The right pre-SMA sits just rostral to SMA proper
        and is the node of **spatial action planning**, **conflict
        anticipation in spatial tasks**, and **reorienting to
        spatially salient events** (overlapping with the right
        ventral attention network).
        NOTE: BA 6 also covers the premotor cortex, which extends onto
        the precentral gyrus and MFG. The parent index resolves BA 6
        to this package by convention (see cross-references).

    BA 8    caudal SFG (dorsal half of the FEF region)
        The superior half of the **right frontal eye fields**. BA 8
        straddles the SFG / MFG boundary; the parent index resolves it
        to this package by convention. The **right FEF is the dominant
        node of the ventral attention network** — the stimulus-driven
        "circuit breaker" that reorients attention to salient events.
        This right-lateralized FEF function is why right FEF damage
        (with right posterior parietal damage) produces **left
        hemispatial neglect**. The right FEF also drives contralateral
        (leftward) saccades and reflexive saccades toward salient
        stimuli.

    BA 9    dorsal SFG (dorsal half of the DLPFC region)
        The superior half of the dorsal prefrontal cortex. Together
        with BA 46 (which lives under MFG) it forms the **dorsal DLPFC
        subdivision** — task-set maintenance, rule representation,
        prospective planning. Right BA 9 is specifically engaged
        during **spatial rule maintenance**, during **attentional-set
        maintenance across hemifields**, and during **emotional
        reappraisal** (via its connectivity to medial BA 10 and the
        amygdala). BA 9 straddles the SFG / MFG boundary; the parent
        index resolves BA 9 to MFG by convention. This package's
        ``BRODMANN_AREAS`` includes BA 9 despite the parent index
        pointing elsewhere — the same "permitted deviation" pattern
        as in the left sibling.

    BA 10   frontopolar / medial SFG
        The **frontopolar cortex** — the most rostral part of the
        frontal lobe, wrapping around the frontal pole onto the medial
        wall. In the **right** hemisphere this hosts the **spatial /
        social-affective component** of the frontopolar cortex,
        engaged in **cognitive branching in spatial and social
        contexts** (holding a primary spatial or social task online
        while a secondary task is performed), **spatial prospective
        memory** (remembering to perform a spatially defined delayed
        intention), **metacognition** (confidence judgments, though
        largely bilateral, right BA 10 is more engaged during
        confidence judgments about perceptual / spatial decisions),
        and the **affective / visuospatial component of theory of
        mind** (ToM is largely bilateral, but the right SFG's BA 10
        contributes the empathy-scaffolded and mental-imagery-
        scaffolded variant). BA 10 is also a node of the
        **default-mode network** via its medial aspect (mPFC), with
        right-lateralized emphasis on **autobiographical memory
        retrieval** and **future episodic simulation** (imagining
        future scenes).

``BA 6 + BA 8 + BA 9 + BA 10 = right SFG``.

**Exclusion note — BA 24 and BA 32**: the anterior cingulate cortex
(ACC) borders the medial SFG along the cingulate sulcus, but the ACC
*proper* — BA 24 (dorsal ACC), BA 32 (pregenual ACC), BA 25 (subgenual
ACC) — belongs to ``cortex/cingulate/anterior_cingulate/``, NOT to
this package. Conflict detection, error monitoring, and pain affect
are ACC functions and must be cross-referenced to the cingulate
package rather than claimed here. What right SFG claims on the medial
wall is the **right pre-SMA / SMA** (BA 6) and the **right medial
frontopolar cortex** (BA 10 medial) — the spatially-salient
action-initiation and affective-self-referential nodes, not the
conflict-monitoring node.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags
(the left sibling declares a *different* set — this is intentional):

    left_hand_motor_planning
        Planning and sequencing self-initiated movements of the **left
        hand**. The right SMA drives the left hand (contralateral) and
        coordinates the left hand's contribution to bimanual tasks.
        Right SMA lesions produce the classic "loss of self-initiated
        left-hand movement" syndrome, even when the left hand can be
        used when externally cued.

    bimanual_coordination_support
        Supporting the left hand's contribution to bimanual tasks.
        Unlike the left SMA — which is the *dominant* bimanual
        coordinator — the right SMA is *subordinate*: it coordinates
        the left hand's role in a bimanual sequence the left SMA has
        planned. Right SMA damage impairs the left hand's timing and
        posture during bimanual tasks without abolishing the overall
        sequence.

    spatial_action_planning
        Right pre-SMA's role in selecting, preparing, and updating
        **spatial** action plans — navigating around obstacles,
        reaching for objects in space, preparing spatially guided
        movements. Distinct from the left pre-SMA's verbal /
        sequential action planning.

    spatial_set_shifting
        Switching between spatial action rules or spatial reference
        frames. The left pre-SMA shifts verbal / sequential sets;
        the right pre-SMA shifts spatial sets.

    spatial_prospective_memory
        Remembering to perform a **spatially defined** delayed
        intention ("remind me to check the mailbox when I pass it").
        Right SFG holds the spatial cue that triggers the intention;
        right MFG holds the spatial content of the intention.

    spatial_cognitive_branching
        Maintaining a primary spatial or social task while a
        secondary task is performed. Right BA 10's variant of
        branching.

    affective_theory_of_mind
        Mental-state reasoning scaffolded by empathy and mental
        imagery. ToM is largely bilateral, but the right SFG's BA 10
        contributes the empathy-driven variant (reasoning about
        others' feelings via simulation and affective resonance),
        while the left SFG contributes the verbal-propositional
        variant.

    autobiographical_memory_retrieval
        Retrieving episodic memories of one's own past. Right medial
        BA 10 is a core node of the default-mode network's
        autobiographical-memory retrieval subsystem. Right SFG
        damage impairs the *vividness* and *episodic richness* of
        autobiographical recall (left damage impairs the *verbal
        narrative coherence* of the same recall).

    future_episodic_simulation
        Imagining future personal scenarios with spatial and
        sensory detail. Right medial BA 10 is the substrate of
        "episodic future thinking"; overlaps with spatial prospective
        memory.

    affective_self_referential_processing
        Reflecting on one's own emotional traits, memories, and
        future. Medial BA 10 is a core node of the default-mode
        network; the right variant is **affective and imagistic**
        (the left variant is verbal-narrative).

    metacognition
        Confidence judgments, error awareness, and monitoring of
        one's own cognitive performance — with right-lateralized
        emphasis during perceptual and spatial decisions.

    saccade_planning
        BA 8 (FEF) — shared with MFG. Right FEF drives leftward
        saccades and reflexive saccades toward salient stimuli. As
        the dominant node of the ventral attention network, the
        right FEF is *the* cortical centre for reorienting to
        salience.

    reorienting_to_salience
        The "circuit breaker" function of the right ventral attention
        network. Right FEF, right pre-SMA, and right temporoparietal
        junction form the reorienting network. This is a
        **right-dominant** function; left FEF contributes only
        weakly.

    action_outcome_prediction
        Predicting the sensory consequences of one's own left-hand
        movements. Right SMA / pre-SMA generate the forward-model
        prediction; right-lateralized emphasis on spatial and
        postural predictions.

These tags map onto the memory subsystem as follows:

    left_hand_motor_planning          → memory/stores/long_term/implicit/procedural
    bimanual_coordination_support     → memory/stores/long_term/implicit/motor_sensorimotor_adaptation
    spatial_action_planning           → memory/stores/long_term/implicit/procedural
    spatial_set_shifting              → memory/stores/long_term/implicit/procedural
    spatial_prospective_memory        → memory/stores/long_term/explicit/episodic
    spatial_cognitive_branching       → memory/stores/short_term (multitask buffer)
    affective_theory_of_mind          → memory/stores/long_term/implicit/implicit_social_cognitive
    autobiographical_memory_retrieval → memory/stores/long_term/explicit/episodic
    future_episodic_simulation        → memory/stores/long_term/explicit/episodic
    affective_self_referential_processing → memory/stores/long_term/explicit/episodic (autobiographical-affective)
    metacognition                     → memory/stores/long_term/explicit/semantic (self-model)
    saccade_planning                  → memory/stores/long_term/implicit/motor_sensorimotor_adaptation
    reorienting_to_salience           → memory/stores/short_term (interrupt-driven)
    action_outcome_prediction         → memory/stores/long_term/implicit/motor_sensorimotor_adaptation

Five roles route to ``long_term/explicit/episodic`` — the right SFG is
the frontal lobe's **autobiographical and future-imagining workbench**.
Four more route to procedural / sensorimotor stores — the right SFG is
also the **left-hand motor planner and spatial-action sequencer**. This
dual character (autobiographical simulation + left-hand motor planning)
mirrors the left SFG's dual character (motor planning + verbal self-
model) but with **affective-spatial** content replacing **verbal-
propositional** content.

Compared with the left SFG's routing:

    Left SFG  emphasis: procedural (motor) + semantic (self-model)
    Right SFG emphasis: episodic (autobiographical + future) + procedural
                        (left-hand motor)

The right SFG is thus the *episodic* half of the pair; the left is the
*semantic / verbal* half.

--------------------------------------------------------------------------------
LONG-RANGE CONNECTIVITY
--------------------------------------------------------------------------------

The ``CONNECTIVITY`` dictionary must contain at minimum (bundle names
mirror the left sibling; targets are right-hemisphere):

    frontal_aslant_tract (right)
        → inferior_frontal_gyrus (right, pars opercularis)
        → supplementary_motor_area (this gyrus, medial BA 6)
        The prosody-initiation pathway; carries task-set instructions
        from right DLPFC (MFG) to prosody-motor cortex (right IFG) via
        the right pre-SMA.

    cingulum bundle (right)
        → posterior_cingulate (right)
        → parahippocampal_gyrus (right)
        The default-mode-network loop connecting medial BA 10 to the
        posterior DMN hub and to parahippocampal scene memory.
        Right-lateralized emphasis on **scene construction** and
        **autobiographical retrieval**.

    superior_longitudinal_fasciculus II (SLF II, right)
        → inferior_parietal_lobule (right)
        → intraparietal_sulcus (right)
        The dorsal attention network's right SFG node; supports
        attentional orienting and the right FEF ↔ right IPS circuit.

    corticospinal_tract (via right SMA)
        → spinal_cord (contralateral, left-hand motor neurons)
        The right SMA's descending motor output — the substrate of
        self-initiated left-hand movement. Right SMA lesions produce
        "loss of self-initiated left-hand movement" even when the
        left-hand corticospinal tract from M1 is intact.

    cortico-reticular projections (right)
        → reticular formation (brainstem)
        The right SMA's projections to the reticular formation that
        support the "readiness" and postural preparation for
        self-initiated left-hand movement.

    corticostriatal projections (right)
        → caudate_nucleus (right, head)
        → putamen (right)
        → nucleus_accumbens (right)
        The associative and limbic fronto-striatal loops; medial
        BA 10 projects to the ventral striatum (self-relevant
        affective valuation), while dorsal BA 6/9 projects to the
        dorsal striatum (motor and cognitive sequencing).

    corticothalamic projections (right)
        → ventrolateral_nucleus (right VL)
        → ventroanterior_nucleus (right VA)
        → mediodorsal_nucleus (right MD)
        → pulvinar (right)
        The right SMA ↔ VL/VA thalamic loop is the substrate of
        left-hand motor sequence learning. The medial BA 10 ↔ MD
        loop supports self-referential processing. The right SFG ↔
        pulvinar loop supports spatially guided action.

    amygdala projections (right)
        → basolateral_nuclei (right)
        → central_nucleus (right)
        The right medial prefrontal ↔ amygdala circuit supports
        extinction learning and **explicit emotion regulation via
        reappraisal**. This projection is **denser on the right than
        on the left**, which is the anatomical reason right-SFG
        lesions impair emotion regulation more severely than
        left-SFG lesions.

    hippocampus projections (right, via cingulum)
        → parahippocampal_gyrus (right)
        → entorhinal_cortex (right)
        The right medial BA 10 ↔ hippocampal loop supports
        **autobiographical memory retrieval** and **future episodic
        simulation** (right-lateralized for the spatial / sensory
        vividness of the memory).

    temporoparietal junction projections (right, via SLF)
        → right temporoparietal junction (angular gyrus / posterior
          superior temporal sulcus)
        The right SFG ↔ TPJ circuit is part of the **ventral
        attention network** (reorienting to salience) and of the
        **theory-of-mind network** (right TPJ is a core ToM node).

Cross-hemispheric:

    corpus_callosum (genu / body)
        → homotopic left SFG
        Carries the interhemispheric dialogue between right affective-
        imagistic and left verbal-narrative self-referential
        processing, and between right left-hand and left right-hand
        motor planning.

--------------------------------------------------------------------------------
HORMONE / NEUROMODULATOR RECEPTORS
--------------------------------------------------------------------------------

The ``HORMONE_RECEPTORS`` dictionary must express which of the 12
hormone families in ``infrastructure/chemicals_hormones/`` modulate this
gyrus. For the right SFG the documented set is:

    noradrenaline       alpha-2A, alpha-1, beta
        05_neuro_modulators_mood — arousal, vigilance, and the
        readiness to reorient to salient events. The right SFG's
        noradrenergic modulation is **stronger than the left's**,
        matching its role in the right ventral attention network
        and in sustained vigilance. Locus coeruleus → right medial
        prefrontal projections are especially dense.

    dopamine            D1, D2
        05_neuro_modulators_mood — left-hand motor-sequence learning
        (right SMA ↔ striatum loop) and spatial cognitive branching
        (right BA 10). D2 loss in the right fronto-striatal loop
        contributes to the left-sided akinesia of Parkinson's
        disease.

    serotonin           5-HT1A, 5-HT2A
        05_neuro_modulators_mood — behavioural inhibition, patience,
        and **affective** self-regulation. Low 5-HT is linked to
        impulsive affective outbursts and reduced right-SFG-mediated
        reappraisal.

    acetylcholine       M1, nicotinic alpha-7
        05_neuro_modulators_mood — attention and motor preparation;
        cholinergic projections to the right SMA support left-hand
        action readiness.

    oxytocin            OXTR
        06_social_territorial_bonding — **self-other distinction**
        and affective theory of mind. The right SFG is a core node
        of the oxytocin-modulated social-affective network;
        intranasal oxytocin increases right medial prefrontal
        activity during self-referential and mentalizing tasks.
        **Stronger than on the left.**

    vasopressin          V1a
        06_social_territorial_bonding — social vigilance and
        territorial self-assertion; modulates right pre-SMA action
        preparation in socially competitive contexts.
        **Right-lateralized.**

    testosterone        AR
        01_hpg_axis_androgens_reproduction — spatial ability,
        mental rotation, and social dominance-related self-assertion.
        The right SFG / parietal network is testosterone-sensitive
        in a way the left verbal network is not.

    estrogen            ER-alpha, ER-beta
        01_hpg_axis_androgens_reproduction — modulates affective
        self-reference and spatial ability in a cycle-dependent
        way. High estrogen improves spatial performance and
        enhances right medial prefrontal activity during
        autobiographical retrieval.

    progesterone        PR
        01_hpg_axis_androgens_reproduction — modulates the
        stability-flexibility tradeoff in spatial cognitive
        branching; high progesterone shifts toward stability.

    cortisol            GR, MR
        02_hpa_axis_stress_survival — stress impairs **affective
        reappraisal** and **autobiographical retrieval**; right
        medial BA 10 expresses dense glucocorticoid receptors and
        is especially sensitive to chronic stress.

    insulin             IR
        04_satiety_gut_energy_signaling — insulin resistance
        impairs spatial prospective memory and affective
        regulation; right BA 10 expresses insulin receptors.

    thyroid hormone     TR-alpha, TR-beta
        03_metabolic_thyroid_growth — hypothyroidism slows left-
        hand motor initiation and affective self-reference.

    orexin / hypocretin OX1R, OX2R
        04_satiety_gut_energy_signaling — arousal and the readiness
        to initiate action; orexin projections to the right SMA
        and pre-SMA support wakeful self-initiation. The right
        SFG ↔ orexin loop is more critical for vigilance than the
        left's.

Compare with the left SFG: the right SFG's receptor profile is shifted
toward **noradrenergic**, **oxytocinergic**, **androgenergic**, and
**orexinergic** signalling, mirroring its roles in vigilance, social-
affective self-reference, spatial cognition, and arousal-driven
reorienting. Dopamine and serotonin remain present (motor and
inhibitory signalling), but the profile's centre of gravity differs —
motor sequencing on both sides, but *social-affective* and
*spatial-vigilance* signalling only on the right.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..sulci.superior_frontal_sulcus
    The ventral boundary of this gyrus. Must exist as a sibling package
    and must declare this gyrus as one of its two bounding gyri.

..sulci.precentral_sulcus
    Bounds BA 6 and BA 8 caudally, separating them from the precentral
    gyrus (primary motor cortex, BA 4).

..brodmann_areas
    The parent ``..gyri`` package maps BA 6, 8, 9, and 10 in its
    ``BRODMANN_TO_GYRUS`` index. The canonical-home conventions are
    (identical left ↔ right):
        BA 6  → "superior_frontal_gyrus"   (SMA / pre-SMA here)
        BA 8  → "superior_frontal_gyrus"   (FEF here; shared with MFG)
        BA 9  → "middle_frontal_gyrus"     (dorsal DLPFC; shared here)
        BA 10 → "superior_frontal_gyrus"   (frontopolar; medial SFG)
    This package's ``BRODMANN_AREAS`` includes BA 9 despite the parent
    index pointing BA 9 → MFG. This is the same "permitted deviation"
    pattern documented in the MFG package (BA 8 shared with SFG) and
    in the left SFG package (BA 9 shared with MFG).

..brodmann_areas.brodmann_area_6
    The SMA / pre-SMA package under ``frontal/brodmann_areas``. Must
    declare this gyrus as its anatomical substrate.

..brodmann_areas.brodmann_area_10
    The frontopolar package. Must declare this gyrus as its anatomical
    substrate (on the medial aspect of SFG) and cross-reference the
    cortical/mPFC functional package.

..cortex.prefrontal_cortex
    BA 9 (shared with MFG) and BA 10 (medial frontopolar) are nodes of
    the prefrontal cortex. The ``prefrontal_cortex`` package must
    declare a dependency on this gyrus.

..cortex.supplementary_motor_cortex
    The functional SMA package. Must declare this gyrus (medial BA 6)
    as its anatomical substrate. BA 6 is the SFG's principal motor
    contribution; the functional SMA package lives under
    ``cortex/supplementary_motor_cortex/``.

..cortex.premotor_cortex
    BA 6 on the dorsal lateral surface is the premotor strip. The
    ``premotor_cortex`` package must declare this gyrus's dorsal BA 6
    as an anatomical substrate (shared with MFG).

..cortex.primary_motor_cortex
    BA 4 (precentral gyrus) is the primary motor cortex and is NOT on
    SFG. The right SFG ↔ right M1 relationship is functional (right
    SMA drives right M1) and is mediated by short-range cortico-
    cortical U-fibres.

..cingulate.anterior_cingulate
    The ACC (BA 24, BA 32, BA 25) abuts the medial SFG but is NOT
    included in this package's BRODMANN_AREAS. Conflict detection,
    error monitoring, and pain affect are ACC functions. The right
    SFG's pre-SMA handles **spatial** conflict anticipation and
    action updating — a complementary but distinct function. Cross-
    reference this distinction in both packages.

..default_mode_network (functional, not a folder)
    Medial BA 10 (and medial BA 9) is a node of the default-mode
    network. The DMN is a functional network, not an anatomical
    package; it is represented implicitly by cross-references
    between medial SFG, posterior cingulate, precuneus, and angular
    gyrus. Document the DMN membership in this package's
    FUNCTIONAL_ROLES under "autobiographical_memory_retrieval" and
    "future_episodic_simulation".

../../subcortical/basal_ganglia/striatum/dorsal_striatum
    The corticostriatal loop from right SFG (BA 6, 9) to right dorsal
    striatum is the substrate of left-hand motor-sequence learning
    and spatial action sequencing. The striatum package must declare
    this gyrus as an upstream cortical input.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The medial BA 10 → right nucleus accumbens projection carries
    self-relevant affective valuation signals. The ventral striatum
    package must declare this loop.

../../subcortical/medial_temporal_lobe/hippocampus
    The right medial BA 10 ↔ right hippocampal loop supports
    autobiographical memory and future episodic simulation. The
    hippocampus package must declare a dependency on this gyrus,
    with right-lateralized emphasis on **scene construction** and
    **episodic vividness**.

../../subcortical/medial_temporal_lobe/amygdala
    The right SFG ↔ amygdala circuit supports explicit emotion
    regulation via reappraisal. The amygdala package must declare
    a dependency on this gyrus, and must note that the right-SFG
    projection is **denser** than the left-SFG projection.

../../left/cortex/frontal/gyri/superior_frontal_gyrus
    The left-hemisphere homologue. Structural fields (GYRUS_NAME,
    LOBE, BRODMANN_AREAS, PARS, SUBDIVISIONS) MUST match this package
    exactly. Functional fields (FUNCTIONAL_ROLES, HORMONE_RECEPTORS,
    CONNECTIVITY targets) are EXPECTED to differ — left SFG carries
    right-hand motor planning, bimanual coordination, verbal
    theory-of-mind, and verbal self-referential processing; right SFG
    carries left-hand motor planning, spatial / affective
    theory-of-mind, and autobiographical / visuospatial self-
    referential processing.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "superior_frontal_gyrus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"
    BRODMANN_AREAS      = (6, 8, 9, 10)             # identical to left
    PARS                = {}                        # SFG has no classical pars
    FUNCTIONAL_ROLES    = (                          # DIFFERS from left
                              "left_hand_motor_planning",
                              "bimanual_coordination_support",
                              "spatial_action_planning",
                              "spatial_set_shifting",
                              "spatial_prospective_memory",
                              "spatial_cognitive_branching",
                              "affective_theory_of_mind",
                              "autobiographical_memory_retrieval",
                              "future_episodic_simulation",
                              "affective_self_referential_processing",
                              "metacognition",
                              "saccade_planning",
                              "reorienting_to_salience",
                              "action_outcome_prediction",
                          )
    CONNECTIVITY        = { ... }   # as specified above (right targets)
    HORMONE_RECEPTORS   = { ... }   # as specified above (right profile)
    SUBDIVISIONS        = ()        # no nested packages yet

    __all__ = [
        "GYRUS_NAME",
        "HEMISPHERE",
        "LOBE",
        "BRODMANN_AREAS",
        "PARS",
        "FUNCTIONAL_ROLES",
        "CONNECTIVITY",
        "HORMONE_RECEPTORS",
        "SUBDIVISIONS",
    ]

Note: ``PARS`` is an empty dict — the SFG has no classical pars
parcellation. The field is kept for uniformity with sibling gyri and
must NOT be deleted.

No behaviour. This package is a declarative descriptor; all computation
that references the SFG lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
PROMOTION RULE (when a Brodmann area becomes a package)
--------------------------------------------------------------------------------

If any single Brodmann sub-region later needs its own substructure —
separate connectivity tables, its own memory hooks, or a distinct
receptor profile that does not fit the parent — promote it to a child
package. The two candidates for right SFG are:

    superior_frontal_gyrus/
        __init__.py
        supplementary_motor_area/   # medial BA 6
            __init__.py
        frontopolar_cortex/         # medial BA 10
            __init__.py

SMA is currently represented functionally under
``cortex/supplementary_motor_cortex/``. If SMA becomes an anatomical
package under SFG, the functional package must be retargeted to point
at the new anatomical package rather than at SFG directly. The
promotion is a **three-way coordination** between:

    1. superior_frontal_gyrus.BRODMANN_AREAS  (remove the promoted BA)
    2. ..gyri.BRODMANN_TO_GYRUS               (retarget the BA)
    3. cortex.supplementary_motor_cortex      (retarget dependencies)

Mirror the promotion on the left side in the same commit. No asymmetric
promotion is permitted.

**Medial-vs-lateral split caveat**: BA 6 and BA 10 both span the lateral
and medial surfaces of SFG. If either is promoted, the promotion must
decide whether the package is *lateral-only*, *medial-only*, or *both*.
The right SFG's dual character (lateral motor strip + medial SMA/self-
model) means a single BA 6 package cannot cleanly represent both unless
it declares an explicit lateral/medial submapping. Adopt a convention
identical in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../superior_frontal_gyrus``:

    MUST be identical:
        GYRUS_NAME
        LOBE
        BRODMANN_AREAS
        PARS (both empty)
        SUBDIVISIONS (including promotion state)

    MUST differ (and the difference must be documented here):
        HEMISPHERE                ("right" vs "left")
        FUNCTIONAL_ROLES          (left-hand motor planning / spatial
                                   ToM / autobiographical self-
                                   reference / reorienting to salience
                                   vs right-hand motor planning /
                                   bimanual coordination / verbal ToM /
                                   verbal self-reference)
        CONNECTIVITY targets      (right-hemisphere structures)
        HORMONE_RECEPTORS profile (noradrenergic / oxytocinergic /
                                   androgenergic / orexinergic
                                   emphasis vs dopaminergic /
                                   serotonergic motor-inhibitory
                                   emphasis)

Any deviation from the "MUST be identical" list is a bug. Any unexpected
similarity in the "MUST differ" list is also a bug — if left and right
SFG end up with the same FUNCTIONAL_ROLES, the hemisphere split has
collapsed and the architecture no longer models lateralization.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "superior_frontal_gyrus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BRODMANN_AREAS is (6, 8, 9, 10) — byte-identical to the left sibling.
[ ] PARS is an empty dict — byte-identical to the left sibling.
[ ] SUBDIVISIONS is empty (matches left sibling's promotion state).
[ ] FUNCTIONAL_ROLES contains all fourteen right-lateralized tags
    listed above and contains NONE of the left-lateralized tags
    (motor_sequence_planning, bimanual_coordination, pre_sma_action_
    planning, executive_scheduler, cognitive_branching, prospective_
    memory, verbal_theory_of_mind, self_referential_processing) —
    except "metacognition", "saccade_planning", and "action_outcome_
    prediction", which are bilateral and appear on BOTH sides.
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY contains every bundle listed above, with
    right-hemisphere targets, including SMA → corticospinal (left
    hand), medial BA 10 → hippocampus, medial BA 10 → ventral
    striatum, medial BA 10 → amygdala (reappraisal), and right SFG
    → right TPJ (ventral attention + ToM).
[ ] Every CONNECTIVITY target names a real package in the tree.
[ ] BA 24 and BA 32 are NOT in BRODMANN_AREAS — ACC belongs to
    cortex/cingulate/anterior_cingulate/, not to this package.
[ ] The parent BRODMANN_TO_GYRUS index maps BA 6, 8, 10 → SFG and
    BA 9 → MFG, and this package's BRODMANN_AREAS documents the BA 9
    deviation.
[ ] HORMONE_RECEPTORS keys are a subset of the 12 chemicals_hormones
    families, and the right profile documents its noradrenergic /
    oxytocinergic / androgenergic / orexinergic emphasis (and its
    denser amygdala projection relative to the left).
[ ] Cross-hemisphere symmetry test passes: structural fields match
    the left sibling; functional fields deliberately differ.
[ ] No PROMOTION has been done on one side without the other.
[ ] The SMA dependency is declared in cortex/supplementary_motor_cortex
    and points back to this gyrus.
[ ] The ACC exclusion is documented in both this package and
    cortex/cingulate/anterior_cingulate.
[ ] The right-SFG-specific clinical anchors (left-hand apraxia,
    left hemispatial neglect, affective aprosodia of gesture,
    impaired autobiographical retrieval, reduced affective ToM,
    impaired spatial prospective memory) are noted for cross-
    referencing from tests/.
"""