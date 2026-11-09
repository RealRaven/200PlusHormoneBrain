"""
Superior Frontal Gyrus (SFG) — Left Hemisphere
===============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
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
``../../right/cortex/frontal/gyri/superior_frontal_gyrus``. Structural
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
frontopolar cortex (part of the default-mode network). The left SFG is
therefore the anatomical bridge between the left lateral frontal
convexity and the left medial frontal wall.

Clinically, left SFG damage produces **akinetic mutism** (if bilateral
SMA is involved), **ideomotor apraxia** of the right hand, **impaired
verbal fluency**, **reduced self-initiated action**, and **disrupted
prospective memory** — the cluster of deficits classically described as
"loss of the will to act" plus "loss of the ability to remember to act."

--------------------------------------------------------------------------------
CYTOARCHITECTONIC PARCELLATION (BRODMANN AREAS)
--------------------------------------------------------------------------------

The SFG spans four Brodmann areas:

    BA 6    medial SFG (and lateral premotor strip along the dorsal
            convexity)
        Hosts the **supplementary motor area (SMA)** and the
        **pre-supplementary motor area (pre-SMA)** on its medial aspect,
        plus the dorsal premotor strip on its lateral aspect. The SMA is
        the cortical substrate of **self-initiated movement**, **motor
        sequence learning**, **bimanual coordination**, and **sequencing
        of internally generated actions**. The pre-SMA sits just rostral
        to the SMA proper and is the human homologue of the monkey
        pre-SMA — the node of **action planning, task-set switching, and
        conflict anticipation** (distinct from conflict *detection*,
        which is ACC territory — see the exclusion note below).
        NOTE: BA 6 also covers the premotor cortex, which extends onto
        the precentral gyrus and MFG. BA 6 is listed under BOTH this
        package and (indirectly, via premotor_cortex) the MFG package's
        functional annotations. The parent index resolves BA 6 to this
        package by convention (see cross-references).

    BA 8    caudal SFG (dorsal half of the FEF region)
        The superior half of the **frontal eye fields**. BA 8 straddles
        the SFG / MFG boundary; the parent index resolves it to this
        package by convention (see the BA 8 canonical-home note in the
        MFG docstring). Left BA 8 drives rightward saccades and
        contributes to attentional orienting and reading-related
        saccades.

    BA 9    dorsal SFG (dorsal half of the DLPFC region)
        The superior half of the dorsal prefrontal cortex. Together with
        BA 46 (which lives under MFG) it forms the **dorsal DLPFC
        subdivision** — task-set maintenance, rule representation,
        prospective planning. BA 9 straddles the SFG / MFG boundary;
        the parent index resolves BA 9 to MFG by convention (see the
        MFG docstring). This package's ``BRODMANN_AREAS`` includes BA 9
        even though the parent index points elsewhere — the same
        "permitted deviation" pattern as MFG's inclusion of BA 8.

    BA 10   frontopolar / medial SFG
        The **frontopolar cortex** — the most rostral part of the
        frontal lobe, wrapping around the frontal pole onto the medial
        wall. In the left hemisphere this hosts the **verbal /
        propositional component** of the frontopolar cortex, engaged in
        **cognitive branching** (Koechlin's model: holding a primary
        task online while a secondary task is performed), **prospective
        memory** (the cue-side of delayed intentions), **metacognition**
        (confidence judgments and error awareness), and the **left-
        lateralized verbal component of theory of mind** (ToM is
        largely bilateral, but verbal ToM — mental-state reasoning
        conducted in language — leans left). BA 10 is also a node of
        the **default-mode network** via its medial aspect (mPFC).

``BA 6 + BA 8 + BA 9 + BA 10 = left SFG``.

**Exclusion note — BA 24 and BA 32**: the anterior cingulate cortex
(ACC) borders the medial SFG along the cingulate sulcus, but the ACC
*proper* — BA 24 (dorsal ACC), BA 32 (pregenual ACC), BA 25 (subgenual
ACC) — belongs to ``cortex/cingulate/anterior_cingulate/``, NOT to
this package. The SFG's medial wall *abuts* the ACC but does not
*include* it. Conflict detection, error monitoring, and pain affect
are ACC functions and must be cross-referenced to the cingulate
package rather than claimed here. What SFG claims on the medial wall
is the **pre-SMA / SMA** (BA 6) and the **medial frontopolar cortex**
(BA 10 medial) — the motor-initiation and self-referential nodes,
not the conflict-monitoring node.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags
(the right sibling declares a *different* set — this is intentional):

    motor_sequence_planning
        Planning and sequencing self-initiated movements. Left SMA
        drives the **right hand** (contralateral) and coordinates
        bimanual sequences. Damage produces the classic SMA syndrome:
        the hand can still be used when cued externally but not when
        the patient must self-initiate the movement.

    bimanual_coordination
        Coordinating the two hands in a single temporally structured
        action (e.g. tying a shoe). The left SMA is the dominant node;
        the right SMA is largely subordinate. This is a **left-
        lateralized** SFG function.

    pre_sma_action_planning
        Pre-SMA's role in selecting, preparing, and updating action
        plans — especially under conditions of response conflict or
        task-set uncertainty. Distinct from ACC's conflict *detection*.

    executive_scheduler
        Holding task structure, ordering sub-goals, and gating the
        transition from one subtask to the next. BA 9 and BA 10
        jointly.

    cognitive_branching
        Maintaining a primary task while a secondary task is performed
        (Koechlin's "branching" function of BA 10). The left BA 10 is
        the verbal-propositional variant of branching; the right BA 10
        is the spatial / social variant.

    prospective_memory
        Remembering to execute a delayed intention. Left SFG holds the
        **cue** that triggers the intention; left MFG holds the
        **content** of the intention. Damage to left SFG produces
        cue-triggered prospective-memory failures even when the
        intention is still represented.

    metacognition
        Confidence judgments, error awareness, and monitoring of one's
        own cognitive performance. BA 10 medial is a core node;
        distinct from ACC's conflict-detection role (metacognition is
        *about* performance, ACC is *of* the moment of conflict).

    verbal_theory_of_mind
        Mental-state reasoning conducted in propositional / verbal
        form. ToM is largely bilateral, but the left SFG's BA 10
        contributes the language-scaffolded variant (reasoning about
        beliefs via verbal inference). The right SFG contributes the
        affective / visuospatial variant.

    self_referential_processing
        Reflecting on one's own traits, memories, and future. Medial
        BA 10 is a core node of the default-mode network; the left
        variant is more verbal-narrative, the right more
        visual-autobiographical.

    saccade_planning
        BA 8 (FEF) — shared with MFG. Left FEF drives rightward
        saccades and reading-related saccades.

    action_outcome_prediction
        Predicting the sensory consequences of one's own actions
        (efference-copy / forward-model territory). SMA and pre-SMA
        generate the prediction; this is the substrate of the sense
        of agency.

These tags map onto the memory subsystem as follows:

    motor_sequence_planning        → memory/stores/long_term/implicit/procedural
    bimanual_coordination          → memory/stores/long_term/implicit/motor_sensorimotor_adaptation
    pre_sma_action_planning        → memory/stores/long_term/implicit/procedural
    executive_scheduler            → memory/stores/short_term (task structure)
    cognitive_branching            → memory/stores/short_term (multitask buffer)
    prospective_memory             → memory/stores/long_term/explicit/episodic
    metacognition                  → memory/stores/long_term/explicit/semantic (self-model)
    verbal_theory_of_mind          → memory/stores/long_term/implicit/implicit_social_cognitive
    self_referential_processing    → memory/stores/long_term/explicit/episodic (autobiographical)
    saccade_planning               → memory/stores/long_term/implicit/motor_sensorimotor_adaptation
    action_outcome_prediction      → memory/stores/long_term/implicit/motor_sensorimotor_adaptation

Four roles route to ``long_term/implicit/procedural`` or
``motor_sensorimotor_adaptation`` — the left SFG is the frontal lobe's
**motor-planning workbench** and the procedural-memory training ground.
Four more route to episodic/semantic long-term stores — the same gyrus
is also the **self-model workbench** via its medial BA 10. This dual
character (motor + self-referential) is unique to SFG and is the
anatomical reason the "self" and the "will to act" are often impaired
together after medial frontal damage.

--------------------------------------------------------------------------------
LONG-RANGE CONNECTIVITY
--------------------------------------------------------------------------------

The ``CONNECTIVITY`` dictionary must contain at minimum:

    frontal_aslant_tract
        → inferior_frontal_gyrus (pars opercularis)
        → supplementary_motor_area (this gyrus, medial BA 6)
        The speech-initiation pathway; carries task-set instructions
        from DLPFC (MFG) to speech-motor cortex (IFG) via the pre-SMA.

    cingulum bundle
        → posterior_cingulate
        → parahippocampal_gyrus
        The default-mode-network loop connecting medial BA 10 to the
        posterior DMN hub and to parahippocampal scene memory.

    superior_longitudinal_fasciculus II (SLF II)
        → inferior_parietal_lobule
        → intraparietal_sulcus
        The dorsal attention network's SFG node; supports attentional
        orienting and the FEF ↔ IPS circuit.

    corticospinal_tract (via SMA)
        → spinal_cord (contralateral, right-hand motor neurons)
        The SMA's descending motor output — the substrate of
        self-initiated right-hand movement. SMA lesions produce the
        classic "alien hand" or "loss of self-initiated movement"
        syndrome even when the corticospinal tract from M1 is intact.

    cortico-reticular projections
        → reticular formation (brainstem)
        The SMA's projections to the reticular formation that support
        the "readiness" and postural preparation for self-initiated
        movement.

    corticostriatal projections
        → caudate_nucleus (left, head)
        → putamen (left)
        → nucleus_accumbens (left)
        The associative and limbic fronto-striatal loops; medial BA 10
        projects to the ventral striatum (reward and self-relevant
        valuation), while dorsal BA 6/9 projects to the dorsal
        striatum (motor and cognitive sequencing).

    corticothalamic projections
        → ventrolateral_nucleus (left VL)
        → ventroanterior_nucleus (left VA)
        → mediodorsal_nucleus (left MD)
        The SMA ↔ VL/VA thalamic loop is the substrate of motor
        sequence learning. The medial BA 10 ↔ MD loop supports
        self-referential and metacognitive processing.

    amygdala projections (left)
        → basolateral_nuclei (left)
        → central_nucleus (left)
        The medial prefrontal ↔ amygdala circuit supports extinction
        learning and emotion regulation via reappraisal. Weaker on the
        left than on the right (see the right sibling).

    hippocampus projections (left, via cingulum)
        → parahippocampal_gyrus (left)
        → entorhinal_cortex (left)
        The medial BA 10 ↔ hippocampal loop supports autobiographical
        memory retrieval and prospective imagining (the same circuit
        that supports "remembering the past" and "imagining the
        future").

    corpus_callosum (genu / body)
        → homotopic right SFG
        Carries the interhemispheric dialogue between left verbal and
        right affective / visuospatial self-referential processing.

--------------------------------------------------------------------------------
HORMONE / NEUROMODULATOR RECEPTORS
--------------------------------------------------------------------------------

The ``HORMONE_RECEPTORS`` dictionary must express which of the 12
hormone families in ``infrastructure/chemicals_hormones/`` modulate this
gyrus. For the left SFG the documented set is:

    dopamine            D1, D2
        05_neuro_modulators_mood — motor-sequence learning (SMA ↔
        striatum loop) and cognitive branching (BA 10). D2 loss in
        the fronto-striatal loop underlies the akinesia and reduced
        self-initiation of Parkinson's disease.

    noradrenaline       alpha-2A, alpha-1, beta
        05_neuro_modulators_mood — arousal, effortful control, and
        vigilance during sustained self-initiated action. The SMA is
        noradrenergically modulated during motor preparation.

    serotonin           5-HT1A, 5-HT2A
        05_neuro_modulators_mood — behavioural inhibition, patience,
        and the capacity to *wait* before initiating action (a
        pre-SMA function). Low 5-HT is linked to impulsive
        self-initiation.

    acetylcholine       M1, nicotinic alpha-7
        05_neuro_modulators_mood — attention and motor preparation;
        cholinergic projections from the basal forebrain to SMA
        support action readiness.

    estrogen            ER-alpha, ER-beta
        01_hpg_axis_androgens_reproduction — verbal fluency (the
        left SFG contributes to verbal-fluency generation), verbal
        ToM, and self-referential narrative. Estrogen upregulates
        left SFG activity during verbal-fluency tasks.

    progesterone        PR
        01_hpg_axis_androgens_reproduction — modulates the
        stability-flexibility tradeoff in cognitive branching;
        high progesterone shifts toward stability.

    cortisol            GR, MR
        02_hpa_axis_stress_survival — stress impairs metacognition
        and prospective memory; medial BA 10 expresses dense
        glucocorticoid receptors.

    oxytocin            OXTR
        06_social_territorial_bonding — self-referential and
        self-other distinction; oxytocin modulates medial BA 10
        activity during self-referential processing.

    vasopressin          V1a
        06_social_territorial_bonding — social vigilance and
        territorial self-assertion; modulates pre-SMA action
        preparation in social contexts.

    insulin             IR
        04_satiety_gut_energy_signaling — insulin resistance
        impairs prospective memory and executive control; BA 10
        expresses insulin receptors.

    thyroid hormone     TR-alpha, TR-beta
        03_metabolic_thyroid_growth — hypothyroidism slows motor
        initiation and verbal fluency.

    orexin / hypocretin OX1R, OX2R
        04_satiety_gut_energy_signaling — arousal and the readiness
        to initiate action; orexin projections to the SMA and pre-SMA
        support wakeful self-initiation.

This profile emphasizes **dopaminergic** motor-sequence signalling and
**serotonergic** behavioural-inhibition signalling, matching the left
SFG's dual role as motor planner and self-model node. The right SFG
shifts emphasis toward noradrenergic and oxytocinergic signalling (see
the right sibling).

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
    ``BRODMANN_TO_GYRUS`` index. The canonical-home conventions are:
        BA 6  → "superior_frontal_gyrus"   (SMA / pre-SMA here)
        BA 8  → "superior_frontal_gyrus"   (FEF here; shared with MFG)
        BA 9  → "middle_frontal_gyrus"     (dorsal DLPFC; shared here)
        BA 10 → "superior_frontal_gyrus"   (frontopolar; medial SFG)
    This package's ``BRODMANN_AREAS`` includes BA 9 despite the parent
    index pointing BA 9 → MFG. This is the same "permitted deviation"
    pattern documented in the MFG package (BA 8 shared with SFG).

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
    SFG. The SFG ↔ M1 relationship is functional (SMA drives M1) and
    is mediated by short-range cortico-cortical U-fibres. Note this in
    the primary_motor_cortex package.

..cingulate.anterior_cingulate
    The ACC (BA 24, BA 32, BA 25) abuts the medial SFG but is NOT
    included in this package's BRODMANN_AREAS. Conflict detection,
    error monitoring, and pain affect are ACC functions. The SFG's
    pre-SMA handles conflict *anticipation* and action *updating* —
    a complementary but distinct function. Cross-reference this
    distinction in both packages.

..default_mode_network (functional, not a folder)
    Medial BA 10 (and medial BA 9) is a node of the default-mode
    network. The DMN is a functional network, not an anatomical
    package; it is represented implicitly by cross-references between
    medial SFG, posterior cingulate, precuneus, and angular gyrus.
    Document the DMN membership in this package's FUNCTIONAL_ROLES
    under "self_referential_processing".

../../subcortical/basal_ganglia/striatum/dorsal_striatum
    The corticostriatal loop from left SFG (BA 6, 9) to left dorsal
    striatum is the substrate of motor-sequence learning and cognitive
    sequencing. The striatum package must declare this gyrus as an
    upstream cortical input.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The medial BA 10 → nucleus accumbens projection carries self-
    relevant valuation signals. The ventral striatum package must
    declare this loop.

../../subcortical/medial_temporal_lobe/hippocampus
    The medial BA 10 ↔ hippocampal loop supports autobiographical
    memory and prospective imagining. The hippocampus package must
    declare a dependency on this gyrus.

../../right/cortex/frontal/gyri/superior_frontal_gyrus
    The right-hemisphere homologue. Structural fields (GYRUS_NAME,
    LOBE, BRODMANN_AREAS, PARS, SUBDIVISIONS) MUST match this package
    exactly. Functional fields (FUNCTIONAL_ROLES, HORMONE_RECEPTORS,
    CONNECTIVITY targets) are EXPECTED to differ — left SFG carries
    right-hand motor planning, bimanual coordination, verbal
    theory-of-mind, and verbal self-referential processing; right SFG
    carries left-hand motor planning, spatial / affective
    theory-of-mind, and autobiographical / visuospatial
    self-referential processing.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "superior_frontal_gyrus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"
    BRODMANN_AREAS      = (6, 8, 9, 10)             # identical to left
    PARS                = {}                        # SFG has no classical pars
    FUNCTIONAL_ROLES    = (
                              "motor_sequence_planning",
                              "bimanual_coordination",
                              "pre_sma_action_planning",
                              "executive_scheduler",
                              "cognitive_branching",
                              "prospective_memory",
                              "metacognition",
                              "verbal_theory_of_mind",
                              "self_referential_processing",
                              "saccade_planning",
                              "action_outcome_prediction",
                          )
    CONNECTIVITY        = { ... }   # as specified above
    HORMONE_RECEPTORS   = { ... }   # as specified above
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
parcellation (the SMA/pre-SMA division is functional, not anatomical
in the classical sense; see the promotion rule). The field is kept for
uniformity with sibling gyri and must NOT be deleted.

No behaviour. This package is a declarative descriptor; all computation
that references the SFG lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
PROMOTION RULE (when a Brodmann area becomes a package)
--------------------------------------------------------------------------------

If any single Brodmann sub-region later needs its own substructure —
separate connectivity tables, its own memory hooks, or a distinct
receptor profile that does not fit the parent — promote it to a child
package. The two candidates for SFG are:

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
promotion is therefore a **three-way coordination** between:

    1. superior_frontal_gyrus.BRODMANN_AREAS  (remove the promoted BA)
    2. ..gyri.BRODMANN_TO_GYRUS               (retarget the BA)
    3. cortex.supplementary_motor_cortex      (retarget dependencies)

Mirror the promotion on the right side in the same commit. No
asymmetric promotion is permitted.

**Medial-vs-lateral split caveat**: BA 6 and BA 10 both span the lateral
and medial surfaces of SFG. If either is promoted, the promotion must
decide whether the package is *lateral-only*, *medial-only*, or *both*.
The SFG's dual character (lateral motor strip + medial SMA/self-model)
means a single BA 6 package cannot cleanly represent both unless it
declares an explicit lateral/medial submapping. Adopt a convention
identical in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../superior_frontal_gyrus``:

    MUST be identical:
        GYRUS_NAME
        LOBE
        BRODMANN_AREAS
        PARS (both empty)
        SUBDIVISIONS (including promotion state)

    MUST differ (and the difference must be documented here):
        HEMISPHERE                ("left" vs "right")
        FUNCTIONAL_ROLES          (right-hand motor planning /
                                   bimanual coordination / verbal ToM /
                                   verbal self-reference vs left-hand
                                   motor planning / spatial ToM /
                                   affective self-reference)
        CONNECTIVITY targets      (left-hemisphere structures)
        HORMONE_RECEPTORS profile (dopaminergic / serotonergic motor
                                   emphasis vs noradrenergic /
                                   oxytocinergic self-other emphasis)

Any deviation from the "MUST be identical" list is a bug. Any unexpected
similarity in the "MUST differ" list is also a bug — if left and right
SFG end up with the same FUNCTIONAL_ROLES, the hemisphere split has
collapsed and the architecture no longer models lateralization.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "superior_frontal_gyrus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BRODMANN_AREAS is (6, 8, 9, 10), sorted ascending, and
    byte-identical to the right sibling.
[ ] PARS is an empty dict (presence required, contents empty).
[ ] SUBDIVISIONS is empty (matches right sibling's promotion state).
[ ] FUNCTIONAL_ROLES contains all eleven left-lateralized tags listed
    above and contains NONE of the right-lateralized tags
    (left_hand_motor_planning, spatial_theory_of_mind,
    affective_self_referential_processing).
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY contains every bundle listed above, with
    left-hemisphere targets, including SMA → corticospinal, medial
    BA 10 → hippocampus, and medial BA 10 → ventral striatum.
[ ] Every CONNECTIVITY target names a real package in the tree.
[ ] BA 24 and BA 32 are NOT in BRODMANN_AREAS — ACC belongs to
    cortex/cingulate/anterior_cingulate/, not to this package.
[ ] The parent BRODMANN_TO_GYRUS index maps BA 6, 8, 10 → SFG and
    BA 9 → MFG, and this package's BRODMANN_AREAS documents the BA 9
    deviation.
[ ] HORMONE_RECEPTORS keys are a subset of the 12 chemicals_hormones
    families, and the left profile documents its dopaminergic /
    serotonergic motor emphasis.
[ ] Cross-hemisphere symmetry test passes: structural fields match
    the right sibling; functional fields deliberately differ.
[ ] No PROMOTION has been done on one side without the other.
[ ] The SMA dependency is declared in cortex/supplementary_motor_cortex
    and points back to this gyrus.
[ ] The ACC exclusion is documented in both this package and
    cortex/cingulate/anterior_cingulate.
"""