"""
Inferior Frontal Gyrus (IFG) — Right Hemisphere
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
                                    └── inferior_frontal_gyrus   ← THIS PACKAGE

This is a **leaf gyrus** package: it has no child packages. Its internal
sub-structure is expressed through the ``PARS`` registry (the three
classical *pars* of the IFG), not through nested folders. If any pars
later grows enough machinery to warrant its own package, it should be
promoted to a sub-package and listed in ``SUBDIVISIONS`` — see the
promotion rule at the bottom of this docstring.

Parent: ``..gyri`` — sibling to ``middle_frontal_gyrus`` and
``superior_frontal_gyrus``.

This package is the **structural mirror** of
``../../left/cortex/frontal/gyri/inferior_frontal_gyrus``. Structural
fields are identical by contract; functional fields diverge by design.

--------------------------------------------------------------------------------
WHAT THE IFG IS
--------------------------------------------------------------------------------

The inferior frontal gyrus is the **ventral-most frontal gyrus**, bounded:

    dorsally    by the inferior frontal sulcus (separating it from MFG)
    caudally    by the precentral sulcus / inferior precentral sulcus
    ventrally   by the lateral (Sylvian) fissure and the orbital surface
    rostrally  tapering toward the frontal pole and orbitofrontal cortex

It is the folded cortical sheet that wraps the anterior insula and
overhangs the lateral fissure. On the **right** hemisphere it houses the
**affective-prosody homologue** of Broca's area and the right-lateralized
inhibitory-control network. It does NOT carry speech production proper —
that is left-IFG territory — but it does carry the *emotional* and
*pragmatic* envelope around speech, and the *brake* on impulsive
responses.

--------------------------------------------------------------------------------
CLASSICAL PARCELLATION (PARS)
--------------------------------------------------------------------------------

The IFG is classically divided into three *pars* (Latin for "parts"),
running caudo-rostral along the gyrus. The pars *names* and their
Brodmann-area numbers are identical to the left hemisphere (Brodmann's
map is numerically symmetric); the *functional annotations* differ.

    pars opercularis      caudal,  BA 44
        The opercular (covering) part, adjacent to the ventral precentral
        gyrus. In the right hemisphere, together with BA 45, it forms the
        right Broca homologue — the *prosody* counterpart of left Broca's
        area. Strongly implicated in:
            • affective prosody production (intonation, stress, tempo)
            • response inhibition, especially in high-conflict or
              emotionally charged go/no-go and stop-signal tasks
            • vocal emotional expression (laughing, crying, exclamations)
        Damage produces *aprosodia* — flat, monotone speech with intact
        grammar and vocabulary.

    pars triangularis     middle,  BA 45
        Triangular in shape, between the ascending and horizontal rami
        of the lateral fissure. In the right hemisphere it is the
        anterior half of the right Broca homologue. Strongly implicated
        in:
            • non-literal language comprehension (sarcasm, irony,
              metaphor, indirect speech acts)
            • discourse coherence at the narrative level
            • semantic integration of distant concepts (coarse coding)

    pars orbitalis        rostral,  BA 47
        The orbital part, curling around the lateral orbital surface.
        Also called the *right ventrolateral prefrontal cortex* (vlPFC).
        Strongly implicated in:
            • humor detection and appreciation
            • affective valuation of social and linguistic stimuli
            • inhibitory control in reward/affective contexts
            • reappraisal and emotion regulation

``BA 44 + BA 45 = right Broca homologue`` — the prosody-and-pragmatics
counterpart of left Broca's area. BA 47 is the right vlPFC node for
humor, affective valuation, and reappraisal.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags
(the left sibling declares a *different* set — this is intentional):

    affective_prosody
        Production and perception of emotional intonation, stress, and
        tempo. This is the canonical right-IFG function; damage produces
        aprosodia.

    response_inhibition
        The right-lateralized inhibitory gate, especially under high
        conflict, emotional salience, or urgency. Core node of the
        right-IFG / pre-SMA stop-signal network.

    non_literal_language
        Sarcasm, irony, metaphor, indirect speech acts, idiom. Right IFG
        (especially BA 45) is required for the pragmatic inference that
        distinguishes literal from intended meaning.

    discourse_coherence
        Integrating sentences into a coherent narrative; tracking topic
        and reference across turns.

    humor_detection
        Detecting and appreciating jokes, puns, and incongruity-resolution
        humor. Right BA 47 is a core node.

    emotion_regulation
        Reappraisal and suppression of emotional responses; right vlPFC
        (BA 47) drives top-down down-regulation of amygdala reactivity.

    social_pragmatics
        Reading social intent from speech — tone, indirectness, politeness,
        implication. Overlaps with mentalizing (right SFG).

These tags map onto the memory subsystem as follows:

    affective_prosody       → memory/stores/long_term/implicit/emotional_valence
    response_inhibition     → memory/stores/long_term/implicit/stimulus_response_s_r_learning
    non_literal_language    → memory/stores/long_term/explicit/semantic
    discourse_coherence     → memory/stores/long_term/explicit/episodic
    humor_detection         → memory/stores/long_term/implicit/emotional_valence
    emotion_regulation      → memory/stores/long_term/implicit/emotional_valence
    social_pragmatics       → memory/stores/long_term/implicit/implicit_social_cognitive

Note that four of the seven right-IFG roles route to
``emotional_valence`` — the right IFG is the affective gateway of the
frontal lobe, and the memory architecture must reflect that.

--------------------------------------------------------------------------------
LONG-RANGE CONNECTIVITY
--------------------------------------------------------------------------------

The ``CONNECTIVITY`` dictionary must contain at minimum (bundle names
mirror the left sibling; targets are right-hemisphere):

    arcuate_fasciculus (right)
        → superior_temporal_gyrus (right, posterior)
        → middle_temporal_gyrus (right)
        The right dorsal pathway: acoustic-to-prosodic mapping. Right
        arcuate is thicker in subjects with better prosody perception.

    uncinate_fasciculus (right)
        → anterior_temporal_lobe (right)
        → temporal_pole (right)
        The right ventral pathway: socio-emotional meaning to word.

    frontal_aslant_tract (right)
        → supplementary_motor_area (right SFG)
        → pre_supplementary_motor_area (right)
        Prosody-initiation and vocal-sequence timing.

    inferior_longitudinal_fasciculus (right)
        → occipitotemporal_cortex (right)
        Visual / facial-affect integration with prosody.

    extreme_capsule (right)
        → insula (right, anterior)
        Interoceptive and autonomic feedback — the substrate of
        "feeling" the emotion you are producing.

    superior_longitudinal_fasciculus (right, SLF III)
        → inferior_parietal_lobule (right)
        Right-hemisphere attentional and prosodic working-memory loop.

    corticostriatal projections (right)
        → caudate_nucleus (right, head)
        → putamen (right)
        The right fronto-striatal loop that gates impulsive responses
        and affective outbursts.

    corticothalamic projections (right)
        → ventrolateral_nucleus (right VL)
        → mediodorsal_nucleus (right MD)
        Motor and executive thalamic relays.

    amygdala projections (right)
        → basolateral_nuclei (right)
        → central_nucleus (right)
        The right IFG ↔ amygdala circuit is the substrate of explicit
        emotion regulation (reappraisal). This projection is far denser
        on the right than on the left and is the anatomical reason
        right-IFG lesions impair emotion regulation.

Cross-hemispheric:

    corpus_callosum (genu / rostrum)
        → homotopic left IFG
        Carries the interhemispheric dialogue between right affective
        prosody and left speech production.

--------------------------------------------------------------------------------
HORMONE / NEUROMODULATOR RECEPTORS
--------------------------------------------------------------------------------

The ``HORMONE_RECEPTORS`` dictionary must express which of the 12
hormone families in ``infrastructure/chemicals_hormones/`` modulate this
gyrus. For the right IFG the documented set is:

    dopamine            D1, D2
        05_neuro_modulators_mood — reward and affective salience
        modulation; right-lateralized approach/withdrawal signaling.

    noradrenaline       alpha-1, alpha-2, beta
        05_neuro_modulators_mood — arousal and urgency for the
        inhibitory gate. The right IFG is more noradrenergically
        modulated than the left, matching its role in stopping under
        high arousal.

    serotonin           5-HT1A, 5-HT2A
        05_neuro_modulators_mood — mood-congruent prosody and
        impulsivity control; low 5-HT is linked to right-IFG
        disinhibition and reactive aggression.

    acetylcholine       M1, nicotinic alpha-7
        05_neuro_modulators_mood — attention to socio-emotional cues.

    estrogen            ER-alpha, ER-beta
        01_hpg_axis_androgens_reproduction — modulates emotion
        regulation and prosody perception; right-IFG activity varies
        with cycle phase.

    testosterone        AR
        01_hpg_axis_androgens_reproduction — modulates reactive
        aggression and dominance-related prosody; organizational and
        activational effects on right-IFG inhibitory control.

    oxytocin            OXTR
        06_social_territorial_bonding — the right IFG is a core node
        of the oxytocin-modulated social-pragmatics network;
        intranasal oxytocin increases right-IFG activity during
        mentalizing and prosody tasks.

    vasopressin          V1a
        06_social_territorial_bonding — modulates territorial and
        threat-related prosody; right-lateralized.

    cortisol            GR, MR
        02_hpa_axis_stress_survival — stress impairs emotion
        regulation and prosody decoding; right IFG is especially
        sensitive to glucocorticoid effects on inhibitory control.

    insulin             IR
        04_satiety_gut_energy_signaling — insulin resistance is
        associated with reduced emotion regulation and increased
        impulsivity.

    thyroid hormone     TR-alpha, TR-beta
        03_metabolic_thyroid_growth — hypothyroidism flattens prosody
        and slows affective processing.

Compare with the left IFG: the right IFG's receptor profile is shifted
toward **noradrenergic**, **oxytocinergic**, and **androgenergic**
signaling, mirroring its roles in urgency-inhibition, social affiliation,
and dominance-related prosody. This divergence is the whole reason the
hemispheres are modelled separately in the architecture.

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
    sync with ``BRODMANN_AREAS`` here, and must be identical to the
    left-hemisphere index.

..cortex.prefrontal_cortex
    BA 47 (pars orbitalis) is a node of the right vlPFC, which lives
    under the functional ``prefrontal_cortex`` package. That package
    must declare a dependency on this gyrus.

..cortex.primary_motor_cortex
    BA 44 (pars opercularis) is adjacent to the right primary motor
    cortex and shares the vocal-motor output pathway. The
    ``primary_motor_cortex`` package must declare the right IFG's pars
    opercularis as an upstream prosody-motor planner.

../../subcortical/medial_temporal_lobe/amygdala
    The right IFG ↔ amygdala circuit (basolateral + central nuclei) is
    the anatomical substrate of explicit emotion regulation. The
    amygdala package must declare this gyrus as a top-down regulator.

../../left/cortex/frontal/gyri/inferior_frontal_gyrus
    The left-hemisphere homologue. Structural fields (GYRUS_NAME,
    LOBE, BRODMANN_AREAS, PARS, SUBDIVISIONS) MUST match this package
    exactly. Functional fields (FUNCTIONAL_ROLES, HORMONE_RECEPTORS,
    CONNECTIVITY targets) are EXPECTED to differ — left IFG carries
    speech production, syntax, and semantic control; right IFG carries
    affective prosody, inhibition under high conflict, non-literal
    language, humor, and emotion regulation.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "inferior_frontal_gyrus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"
    BRODMANN_AREAS      = (44, 45, 47)              # identical to left
    PARS                = {                          # keys identical to left
                              "pars_opercularis":  (44,),
                              "pars_triangularis": (45,),
                              "pars_orbitalis":    (47,),
                          }
    FUNCTIONAL_ROLES    = (                          # DIFFERS from left
                              "affective_prosody",
                              "response_inhibition",
                              "non_literal_language",
                              "discourse_coherence",
                              "humor_detection",
                              "emotion_regulation",
                              "social_pragmatics",
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

**Symmetry constraint**: the SAME promotion must happen on the left
side, in the same commit. The right IFG cannot have a
``pars_opercularis/`` sub-package while the left IFG has only a flat
``PARS`` entry — the cross-hemisphere symmetry test will fail.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../inferior_frontal_gyrus``:

    MUST be identical:
        GYRUS_NAME
        LOBE
        BRODMANN_AREAS
        PARS keys (and values — BA numbering is symmetric)
        SUBDIVISIONS (including promotion state)

    MUST differ (and the difference must be documented here):
        HEMISPHERE                    ("right" vs "left")
        FUNCTIONAL_ROLES              (prosody/humor/inhibition vs
                                       language/syntax/semantics)
        CONNECTIVITY targets          (right-hemisphere structures)
        HORMONE_RECEPTORS profile     (noradrenergic/oxytocinergic
                                       emphasis vs dopaminergic/estrogenic
                                       emphasis)

Any deviation from the "MUST be identical" list is a bug. Any unexpected
similarity in the "MUST differ" list is also a bug — if left and right
IFG end up with the same FUNCTIONAL_ROLES, the hemisphere split has
collapsed and the architecture no longer models lateralization.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "inferior_frontal_gyrus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BRODMANN_AREAS is (44, 45, 47) — byte-identical to the left sibling.
[ ] PARS keys and values are byte-identical to the left sibling.
[ ] SUBDIVISIONS is empty (matches left sibling's promotion state).
[ ] FUNCTIONAL_ROLES contains all seven right-lateralized tags listed
    above and contains NONE of the left-lateralized tags.
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY contains every bundle listed, with right-hemisphere
    targets, plus the right-amygdala projection.
[ ] Every CONNECTIVITY target names a real package in the tree.
[ ] HORMONE_RECEPTORS keys are a subset of the 12 chemicals_hormones
    families, and the right profile documents its divergence from the
    left (noradrenergic, oxytocinergic, androgenergic emphasis).
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    left sibling; functional fields deliberately differ.
[ ] No PROMOTION has been done on one side without the other.
"""