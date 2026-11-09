"""
Inferior Frontal Gyrus (IFG) — Left Hemisphere
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
                                    └── inferior_frontal_gyrus   ← THIS PACKAGE

This is a **leaf gyrus** package: it has no child packages. Its internal
sub-structure is expressed through the ``PARS`` registry (the three
classical *pars* of the IFG), not through nested folders. If any pars
later grows enough machinery to warrant its own package, it should be
promoted to a sub-package and listed in ``SUBDIVISIONS`` — see the
promotion rule at the bottom of this docstring.

Parent: ``..gyri`` — sibling to ``middle_frontal_gyrus`` and
``superior_frontal_gyrus``.

--------------------------------------------------------------------------------
WHAT THE IFG IS
--------------------------------------------------------------------------------

The inferior frontal gyrus is the **ventral-most frontal gyrus**, bounded:

    dorsally    by the inferior frontal sulcus (separating it from MFG)
    caudally    by the precentral sulcus / inferior precentral sulcus
    ventrally   by the lateral (Sylvian) fissure and the orbital surface
    rostrally  tapering toward the frontal pole and orbitofrontal cortex

It is the folded cortical sheet that wraps the anterior insula and
overhangs the lateral fissure. On the left hemisphere it houses
**Broca's area** and the surrounding language-production network.

--------------------------------------------------------------------------------
CLASSICAL PARCELLATION (PARS)
--------------------------------------------------------------------------------

The IFG is classically divided into three *pars* (Latin for "parts"),
running caudo-rostral along the gyrus:

    pars opercularis      caudal,  BA 44
        The opercular (covering) part, adjacent to the ventral precentral
        gyrus. In the left hemisphere, together with BA 45, it forms
        Broca's area. Strongly implicated in:
            • phonological assembly
            • articulatory / speech-motor planning
            • speech production output
        Heavy connectivity via the frontal aslant tract to the SMA and
        via the arcuate fasciculus to posterior temporal cortex.

    pars triangularis     middle,  BA 45
        Triangular in shape, between the ascending and horizontal rami
        of the lateral fissure. In the left hemisphere it is the
        anterior half of Broca's area. Strongly implicated in:
            • syntactic processing (parsing, phrase-structure building)
            • semantic control (selecting among competing meanings)
            • verbal fluency
        Connectivity to anterior temporal lobe (semantic hub) via the
        uncinate fasciculus, and to posterior temporal cortex via the
        arcuate fasciculus.

    pars orbitalis        rostral,  BA 47
        The orbital part, curling around the lateral orbital surface.
        Also called the *ventrolateral prefrontal cortex* (vlPFC).
        Strongly implicated in:
            • semantic retrieval
            • reward-guided decision-making
            • inhibitory control in affective contexts
        Connectivity to orbitofrontal cortex, amygdala, and ventral
        striatum — this is the par that most directly couples language
        to affect and valuation.

``BA 44 + BA 45 = Broca's area`` (left-hemisphere dominant). BA 47 is
often treated separately from "Broca's area proper" but is part of the
same gyrus and, functionally, part of the same language-control system.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags:

    language_production
        Speech-motor output; the final common path from language
        intention to articulation.

    syntactic_processing
        Building phrase structure; parsing word order and agreement.

    semantic_control
        Selecting the context-appropriate meaning of ambiguous words;
        resolving semantic competition.

    phonological_assembly
        Assembling phoneme sequences for output; the buffer that feeds
        the motor articulators.

    response_inhibition
        The go/no-go and stop-signal inhibitory gate — especially for
        verbal and manual responses in linguistic contexts.

    mirror_observation
        Action-observation / mirror-neuron-adjacent responses, especially
        for observed speech and hand gestures (overlaps with ventral
        premotor cortex).

    verbal_working_memory_buffer
        A short-lived phonological / articulatory rehearsal store that
        interacts with MFG's working-memory register.

These tags map onto the memory subsystem as follows:

    language_production       → memory/stores/long_term/implicit/procedural
    syntactic_processing       → memory/stores/long_term/implicit/temporal_sequence_learning
    semantic_control           → memory/stores/long_term/explicit/semantic
    phonological_assembly      → memory/stores/short_term (phonological loop)
    response_inhibition        → memory/stores/long_term/implicit/stimulus_response_s_r_learning
    mirror_observation         → memory/stores/long_term/implicit/motor_sensorimotor_adaptation
    verbal_working_memory_buffer → memory/stores/short_term

Declaring these links here means the memory layer can query the gyrus
for its admissible memory types without hard-coding.

--------------------------------------------------------------------------------
LONG-RANGE CONNECTIVITY
--------------------------------------------------------------------------------

The ``CONNECTIVITY`` dictionary must contain at minimum:

    arcuate_fasciculus
        → superior_temporal_gyrus (posterior)
        → middle_temporal_gyrus
        The dorsal language pathway: sound-to-articulation mapping.

    uncinate_fasciculus
        → anterior_temporal_lobe
        → temporal_pole
        The ventral language pathway: meaning-to-word mapping.

    frontal_aslant_tract
        → supplementary_motor_area (on SFG)
        → pre_supplementary_motor_area
        Speech-initiation and sequence-timing pathway.

    inferior_longitudinal_fasciculus
        → occipitotemporal_cortex (fusiform / visual word form area)
        Reading and visual-word recognition pathway.

    extreme_capsule
        → insula (anterior)
        Interoceptive and articulatory feedback.

    superior_longitudinal_fasciculus (SLF III)
        → inferior_parietal_lobule
        Phonological short-term memory loop.

    corticostriatal projections
        → caudate_nucleus (head, left)
        → putamen (left)
        The fronto-striatal loop that gates verbal output; lesion or
        dysfunction here contributes to stuttering and to verbal tics.

    corticothalamic projections
        → ventrolateral_nucleus (VL)
        → mediodorsal_nucleus (MD)
        Motor and executive thalamic relays.

Cross-hemispheric:

    corpus_callosum (genu / rostrum)
        → homotopic right IFG
        Carries the interhemispheric dialogue between left speech
        production and right affective prosody.

--------------------------------------------------------------------------------
HORMONE / NEUROMODULATOR RECEPTORS
--------------------------------------------------------------------------------

The ``HORMONE_RECEPTORS`` dictionary must express which of the 12
hormone families in ``infrastructure/chemicals_hormones/`` modulate this
gyrus. For the left IFG the documented set is:

    dopamine            D1, D2
        05_neuro_modulators_mood — frontal-striatal reward and
        verbal-fluency modulation. D2 loss in fronto-striatal loops is
        linked to reduced verbal fluency in Parkinson's disease.

    noradrenaline       alpha-1, alpha-2, beta
        05_neuro_modulators_mood — arousal and vigilance for speech
        production; locus coeruleus → IFG projections.

    serotonin           5-HT1A, 5-HT2A
        05_neuro_modulators_mood — mood-dependent modulation of verbal
        output; implicated in stuttering and in verbal tics.

    acetylcholine       M1, nicotinic alpha-7
        05_neuro_modulators_mood — attention and verbal encoding;
        basal-forebrain cholinergic projections to IFG.

    estrogen            ER-alpha, ER-beta
        01_hpg_axis_androgens_reproduction — verbal fluency fluctuates
        with the menstrual cycle; estrogen supports verbal working
        memory.

    testosterone        AR
        01_hpg_axis_androgens_reproduction — modulates language
        lateralization during development; organizational effects.

    oxytocin            OXTR
        06_social_territorial_bonding — social speech and affiliative
        vocalization.

    cortisol            GR, MR
        02_hpa_axis_stress_survival — stress impairs verbal fluency and
        syntactic processing; glucocorticoid receptors are dense in
        prefrontal cortex.

    insulin             IR
        04_satiety_gut_energy_signaling — insulin resistance is
        associated with reduced verbal fluency; IFG expresses insulin
        receptors.

    thyroid hormone     TR-alpha, TR-beta
        03_metabolic_thyroid_growth — hypothyroidism slows speech and
        word retrieval.

This list is not exhaustive but establishes the contract: every hormone
family that the architecture claims to model must be able to ask "does
the left IFG respond to me?" and get a machine-readable answer.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..sulci.inferior_frontal_sulcus
    The dorsal boundary of this gyrus. Must exist as a sibling package
    and must declare this gyrus as one of its two bounding gyri.

..sulci.olfactory_sulcus
    Runs along the orbital surface, bounding pars orbitalis ventrally.

..sulci.precentral_sulcus
    Bounds pars opercularis caudally, separating it from the precentral
    gyrus.

..brodmann_areas
    The parent ``..gyri`` package maps BA 44, 45, and 47 back to this
    gyrus in its ``BRODMANN_TO_GYRUS`` index. That index must stay in
    sync with ``BRODMANN_AREAS`` here.

..cortex.prefrontal_cortex
    BA 47 (pars orbitalis) is a node of the vlPFC, which lives under
    the functional ``prefrontal_cortex`` package. That package must
    declare a dependency on this gyrus.

..cortex.primary_motor_cortex
    BA 44 (pars opercularis) is adjacent to the primary motor cortex
    and shares the speech-motor output pathway with it. The
    ``primary_motor_cortex`` package must declare the IFG's pars
    opercularis as an upstream speech-motor planner.

../../right/cortex/frontal/gyri/inferior_frontal_gyrus
    The right-hemisphere homologue. Structural fields (GYRUS_NAME,
    LOBE, BRODMANN_AREAS, PARS, SUBDIVISIONS) MUST match this package
    exactly. Functional fields (FUNCTIONAL_ROLES, HORMONE_RECEPTORS,
    CONNECTIVITY targets) are EXPECTED to differ — right IFG carries
    affective prosody, inhibition under high conflict, non-literal
    language, and humor, not speech production proper.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "inferior_frontal_gyrus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"
    BRODMANN_AREAS      = (44, 45, 47)
    PARS                = {
                              "pars_opercularis":  (44,),
                              "pars_triangularis": (45,),
                              "pars_orbitalis":    (47,),
                          }
    FUNCTIONAL_ROLES    = (
                              "language_production",
                              "syntactic_processing",
                              "semantic_control",
                              "phonological_assembly",
                              "response_inhibition",
                              "mirror_observation",
                              "verbal_working_memory_buffer",
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

No behaviour. This package is a declarative descriptor; all computation
that references the IFG lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
PROMOTION RULE (when a pars becomes a package)
--------------------------------------------------------------------------------

If any single pars (e.g. ``pars_opercularis``) later needs its own
substructure — separate Brodmann sub-fields, separate connectivity
tables, or its own memory hooks — promote it to a child package:

    inferior_frontal_gyrus/
        __init__.py
        pars_opercularis/
            __init__.py

Then add "pars_opercularis" to this package's ``SUBDIVISIONS`` and
remove that pars from the ``PARS`` dict (the dict is the flat registry;
once a pars is a package, its own ``__init__.py`` owns its BA numbers).
Mirror the change on the right side to preserve the symmetry contract.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "inferior_frontal_gyrus".
[ ] HEMISPHERE is "left".
[ ] BRODMANN_AREAS is (44, 45, 47), sorted ascending.
[ ] PARS keys are exactly the three classical pars, in caudo-rostral
    order as documented above.
[ ] FUNCTIONAL_ROLES contains all seven tags listed above.
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY contains every bundle listed in the long-range
    connectivity section.
[ ] Every CONNECTIVITY target names a real sibling or cousin package
    in the tree.
[ ] HORMONE_RECEPTORS keys are a subset of the 12 chemicals_hormones
    families, and every receptor listed is documented in the relevant
    hormones.yaml.
[ ] SUBDIVISIONS is empty (no promotion yet).
[ ] Structural fields (GYRUS_NAME, LOBE, BRODMANN_AREAS, PARS,
    SUBDIVISIONS) are IDENTICAL to the right-hemisphere sibling.
[ ] Functional fields (FUNCTIONAL_ROLES, HORMONE_RECEPTORS,
    CONNECTIVITY targets) are DELIBERATELY DIFFERENT and the differences
    are documented in the right-hemisphere sibling's docstring.
"""