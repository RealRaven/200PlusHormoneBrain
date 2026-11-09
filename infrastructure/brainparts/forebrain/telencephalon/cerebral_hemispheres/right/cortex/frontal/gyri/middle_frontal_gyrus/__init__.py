"""
Middle Frontal Gyrus (MFG) — Right Hemisphere
==============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── frontal
                              └── gyri
                                    └── middle_frontal_gyrus   ← THIS PACKAGE

This is a **leaf gyrus** package: it has no child packages. Its internal
sub-structure is expressed through the ``BRODMANN_AREAS`` registry, not
through nested folders. If any Brodmann sub-region later grows enough
machinery to warrant its own package (e.g. frontal eye fields as a
separate ``frontal_eye_fields/``), it should be promoted to a sub-package
and listed in ``SUBDIVISIONS`` — see the promotion rule at the bottom.

Parent: ``..gyri`` — sibling to ``inferior_frontal_gyrus`` and
``superior_frontal_gyrus``.

This package is the **structural mirror** of
``../../left/cortex/frontal/gyri/middle_frontal_gyrus``. Structural
fields are identical by contract; functional fields diverge by design.

--------------------------------------------------------------------------------
WHAT THE MFG IS
--------------------------------------------------------------------------------

The middle frontal gyrus is the **intermediate frontal gyrus**, bounded:

    dorsally    by the superior frontal sulcus (separating it from SFG)
    ventrally   by the inferior frontal sulcus (separating it from IFG)
    caudally    by the precentral sulcus / superior precentral sulcus
    rostrally  merging with the frontopolar cortex toward the frontal pole

It is the largest of the three frontal gyri by cortical surface area, and
it is the folded cortical sheet that hosts the bulk of the **dorsolateral
prefrontal cortex (DLPFC)**. On the **right** hemisphere it is the dominant
node for **visuospatial** working memory, **sustained attention / vigilance**,
and **top-down spatial attention**. It does NOT carry verbal working
memory — that is left-MFG territory — but it does carry the spatial and
attentional envelope that lets the left hemisphere talk about *what* while
the right hemisphere tracks *where*.

--------------------------------------------------------------------------------
CYTOARCHITECTONIC PARCELLATION (BRODMANN AREAS)
--------------------------------------------------------------------------------

The MFG spans three Brodmann areas, running caudo-rostral. The BA numbers
are identical to the left hemisphere (Brodmann's map is numerically
symmetric); the functional annotations differ.

    BA 8    caudal MFG
        The caudal-most strip, abutting the precentral sulcus. Hosts the
        **right frontal eye fields (FEF)** — the cortical saccade-planning
        centre. The right FEF directs contralateral (leftward) saccades
        in the right hemisphere. Critically, the right FEF is the dominant
        node of the **ventral attention network** — the stimulus-driven
        "circuit breaker" that reorients attention to salient events in
        the environment. This right-lateralized FEF function is why right
        frontal damage produces **left hemispatial neglect**, the
        canonical right-hemisphere attentional deficit.
        NOTE: the FEF straddles the MFG / SFG boundary; BA 8 is listed
        under BOTH this package and the superior_frontal_gyrus package.
        See the cross-reference section for the canonical-home convention.

    BA 9    dorsal MFG
        The dorsal-prefrontal strip. Core of **task-set maintenance**,
        **rule representation**, and **prospective planning** — largely
        bilateral, but the right BA 9 is specifically engaged during
        **spatial rule** maintenance and during the maintenance of
        **attentional sets** across the hemifields.

    BA 46   mid-DLPFC
        The intermediate strip, often called the *principal sulcus*
        homologue (in macaques, area 46 is the principal sulcus cortex).
        In the right hemisphere this is the **visuospatial working-memory
        register** — the neural substrate of the *visuospatial
        sketchpad*. It is also the principal frontal node of the **dorsal
        attention network** (with FEF and intraparietal sulcus), driving
        top-down attentional gain across the visual field.

``BA 9 + BA 46 = right DLPFC proper``. BA 8 is FEF and is shared with SFG.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags (the
left sibling declares a *different* set — this is intentional):

    visuospatial_working_memory
        Maintaining and manipulating spatial locations, orientations,
        object shapes, and visual patterns across delays. This is the
        right MFG's canonical specialization; it is the neural substrate
        of the visuospatial sketchpad and of mental rotation. Right MFG
        damage selectively impairs spatial span while leaving verbal
        span intact.

    spatial_attention
        Top-down biasing of posterior visual cortex toward spatial
        locations. Right MFG is the dominant frontal node of the **dorsal
        attention network** (with FEF and intraparietal sulcus). Right
        posterior parietal and MFG lesions cause left hemispatial
        neglect because the right hemisphere monitors both hemifields
        while the left monitors only the contralateral (right) field.

    vigilance
        Sustained attention over minutes to hours. The right MFG (with
        right inferior frontal gyrus and right parietal cortex) forms the
        **right-lateralized vigilance network**; time-on-task
        decrements are largest after right MFG lesions, and right MFG
        activity tracks momentary lapses.

    spatial_set_shifting
        Switching between spatial rules, spatial reference frames, or
        spatial response mappings. The left MFG shifts *verbal/semantic*
        sets; the right MFG shifts *spatial* sets.

    spatial_prospective_memory
        Remembering to perform a spatially defined delayed intention
        ("remind me to check the mailbox when I pass it"). Overlaps with
        right SFG BA 10.

    saccade_planning
        Generating and controlling eye movements (BA 8 / FEF). In the
        right hemisphere, this includes contralateral (leftward)
        saccades and, via the ventral attention network, **reflexive
        saccades toward salient events**.

    mental_rotation
        Rotating objects in the mind's eye. Right MFG / superior parietal
        network; engaged during spatial-reasoning tasks and during
        navigation.

    reorienting_to_salience
        The "circuit breaker" function of the right ventral attention
        network: disengaging from the current task when a salient
        stimulus appears. This is the right MFG / FEF / temporoparietal
        junction network.

These tags map onto the memory subsystem as follows:

    visuospatial_working_memory  → memory/stores/short_term (visuospatial sketchpad)
    spatial_attention            → memory/stores/short_term (gain modulation)
    vigilance                    → memory/stores/short_term (sustained buffer)
    spatial_set_shifting         → memory/stores/long_term/implicit/procedural
    spatial_prospective_memory   → memory/stores/long_term/explicit/episodic
    saccade_planning             → memory/stores/long_term/implicit/motor_sensorimotor_adaptation
    mental_rotation              → memory/stores/long_term/explicit/semantic
    reorienting_to_salience      → memory/stores/short_term (interrupt-driven)

Note that four of the eight roles route to ``short_term`` — the right MFG
is the frontal lobe's **attentional workspace**, and the memory
architecture must reflect that its short-term traffic is spatial and
salience-driven rather than verbal. This mirrors (but does not duplicate)
the left MFG's short-term traffic, which is verbal and phonological.

--------------------------------------------------------------------------------
LONG-RANGE CONNECTIVITY
--------------------------------------------------------------------------------

The ``CONNECTIVITY`` dictionary must contain at minimum (bundle names
mirror the left sibling; targets are right-hemisphere):

    superior_longitudinal_fasciculus I (SLF I, right)
        → superior_parietal_lobule (right)
        → precuneus (right)
        Dorsal attention network; top-down spatial attention.

    superior_longitudinal_fasciculus II (SLF II, right)
        → inferior_parietal_lobule (right, angular gyrus + supramarginal)
        → intraparietal_sulcus (right)
        Spatial working-memory and dorsal-attention loop.

    superior_longitudinal_fasciculus III (SLF III, right)
        → inferior_parietal_lobule (right, supramarginal gyrus)
        → superior_temporal_gyrus (right, posterior)
        Spatial attention ↔ auditory spatial processing loop.

    arcuate_fasciculus (indirect segment, right)
        → middle_temporal_gyrus (right, posterior)
        → inferior_parietal_lobule (right)
        The right indirect arcuate — weaker than on the left, consistent
        with right-hemisphere DLPFC's non-dominant role in language.

    frontal_aslant_tract (right)
        → inferior_frontal_gyrus (right, pars opercularis)
        → supplementary_motor_area (right SFG)
        Carries task-set instructions from right DLPFC to prosody-motor
        cortex.

    uncinate_fasciculus (right)
        → anterior_temporal_lobe (right)
        → temporal_pole (right)
        Semantic-affective loop; supports the right MFG's role in
        socio-emotional valuation and coarse semantic coding.

    extreme_capsule (right)
        → insula (right, anterior)
        Interoceptive and salience gating.

    corticostriatal projections (right)
        → caudate_nucleus (right, head)
        → putamen (right)
        The right cognitive-associative fronto-striatal loop. Gates
        spatial working-memory updating.

    corticothalamic projections (right)
        → mediodorsal_nucleus (right MD)
        → ventrolateral_nucleus (right VL)
        → pulvinar (right)
        Executive, motor, and visual-attention thalamic relays. The
        right MFG ↔ pulvinar loop is a core node of the right-lateralized
        attentional network.

    cingulum bundle (right)
        → posterior_cingulate (right)
        → parahippocampal_gyrus (right)
        Task-relevance ↔ memory-retrieval loop, with right-hemisphere
        emphasis on spatial and scene memory.

    temporoparietal junction projections (via SLF)
        → right temporoparietal junction (angular gyrus / posterior
          superior temporal sulcus)
        The right MFG ↔ TPJ circuit is the substrate of the **ventral
        attention network** (reorienting to salience).

    intraparietal sulcus projections (via SLF II)
        → intraparietal_sulcus (right)
        The right MFG ↔ right IPS circuit is the substrate of the
        **dorsal attention network** (top-down spatial attention).

Cross-hemispheric:

    corpus_callosum (genu / body)
        → homotopic left MFG
        Carries the interhemispheric dialogue between right visuospatial
        and left verbal working memory.

--------------------------------------------------------------------------------
HORMONE / NEUROMODULATOR RECEPTORS
--------------------------------------------------------------------------------

The ``HORMONE_RECEPTORS`` dictionary must express which of the 12
hormone families in ``infrastructure/chemicals_hormones/`` modulate this
gyrus. For the right MFG the documented set is:

    noradrenaline       alpha-2A, alpha-1, beta
        05_neuro_modulators_mood — arousal, vigilance, and reorienting
        to salience. The right MFG's noradrenergic modulation is
        STRONGER than the left's, matching its role in sustained
        attention and in the ventral attention network. Locus coeruleus
        → right DLPFC projections are especially dense.

    dopamine            D1, D2, D4
        05_neuro_modulators_mood — spatial working memory and
        attentional gating. The inverted-U of D1 signalling applies
        here too, but the right MFG is relatively more sensitive to
        D2-mediated gating of spatial attention.

    serotonin           5-HT2A, 5-HT1A
        05_neuro_modulators_mood — spatial reversal learning and
        cognitive flexibility; the right MFG is more engaged than the
        left during spatial reversals.

    acetylcholine       M1, nicotinic alpha-7, alpha-4-beta-2
        05_neuro_modulators_mood — sustained attention and spatial
        encoding. Cholinergic projections from the basal forebrain
        gate right MFG vigilance.

    testosterone        AR
        01_hpg_axis_androgens_reproduction — **spatial ability and
        mental rotation are reliably associated with testosterone** on
        the right side; the right MFG / parietal network is
        testosterone-sensitive in a way the left verbal network is not.
        Organizational effects during development contribute to the
        sex difference in mental rotation.

    estrogen            ER-alpha, ER-beta
        01_hpg_axis_androgens_reproduction — modulates spatial ability
        in a cycle-dependent way; high estrogen (follicular phase)
        improves spatial performance, low estrogen (luteal) shifts
        toward verbal strategies.

    cortisol            GR, MR
        02_hpa_axis_stress_survival — stress impairs right MFG-dependent
        sustained attention and spatial working memory. Right MFG is
        especially sensitive to glucocorticoid effects on vigilance.

    insulin             IR
        04_satiety_gut_energy_signaling — insulin resistance impairs
        spatial working memory; right MFG insulin signalling modulates
        dopamine clearance.

    thyroid hormone     TR-alpha, TR-beta
        03_metabolic_thyroid_growth — hypothyroidism slows spatial
        processing and sustained attention.

    orexin / hypocretin OX1R, OX2R
        04_satiety_gut_energy_signaling — arousal and sustained
        attention; orexin projections to the right MFG support
        vigilance. The right MFG ↔ orexin loop is more critical for
        vigilance than the left's.

    vasopressin          V1a
        06_social_territorial_bonding — modulates spatial vigilance and
        territorial attentional orienting; right-lateralized.

    BDNF (growth factor, structural anchor family)
        09_structural_anchors_transporters_catalysts — synaptic
        plasticity in DLPFC; BDNF Val66Met modulates spatial
        working-memory capacity.

Compare with the left MFG: the right MFG's receptor profile is shifted
toward **noradrenergic**, **androgenergic**, and **orexinergic**
signalling, mirroring its roles in vigilance, spatial cognition, and
mental rotation. Estrogen remains present but is modulated differently —
estrogen *improves* spatial performance at high levels, whereas it
*improves* verbal fluency at high levels on the left. This apparent
paradox (estrogen helping both verbal and spatial tasks) is resolved by
the fact that estrogen improves the *efficiency* of whichever hemisphere
is currently engaged; the right MFG is engaged during spatial tasks
regardless of cycle phase, but its efficiency is cycle-modulated.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..sulci.superior_frontal_sulcus
    The dorsal boundary of this gyrus. Must exist as a sibling package
    and must declare this gyrus as one of its two bounding gyri.

..sulci.inferior_frontal_sulcus
    The ventral boundary of this gyrus. Must exist as a sibling package
    and must declare this gyrus as one of its two bounding gyri.

..sulci.precentral_sulcus
    Bounds BA 8 (FEF) caudally, separating it from the precentral
    gyrus.

..brodmann_areas
    The parent ``..gyri`` package maps BA 8, 9, and 46 back to this
    gyrus in its ``BRODMANN_TO_GYRUS`` index. BA 8 is shared with
    ``superior_frontal_gyrus``; the index maps it to the **superior**
    gyrus by convention (FEF is canonically listed under SFG), so this
    package's ``BRODMANN_AREAS`` must contain BA 8 but the parent
    index must list BA 8 → "superior_frontal_gyrus". This is the ONLY
    permitted deviation from the "BRODMANN_AREAS ⊆ index keys" rule,
    and the deviation must be documented at the parent level.

..cortex.prefrontal_cortex
    BA 9 and BA 46 are nodes of the DLPFC, which lives under the
    functional ``prefrontal_cortex`` package. That package must declare
    a dependency on this gyrus.

..cortex.premotor_cortex
    BA 8 (FEF) is adjacent to the premotor cortex and shares
    saccade-planning circuitry with it. The ``premotor_cortex``
    package must declare the FEF as an upstream saccade planner.

../../subcortical/basal_ganglia/striatum/dorsal_striatum/caudate_nucleus
    The corticostriatal loop from right MFG to right caudate head is
    the principal substrate of spatial working-memory updating. The
    caudate package must declare this gyrus as an upstream cortical
    input.

../../subcortical/medial_temporal_lobe/hippocampus
    The cingulum-bundle loop connects right MFG to parahippocampal
    cortex, supporting the task-relevance ↔ scene/spatial-memory
    interaction. The hippocampus package must declare a dependency on
    this loop, with right-lateralized emphasis.

../../subcortical/medial_temporal_lobe/amygdala
    The right MFG ↔ amygdala circuit supports the reorienting-to-
    salience function; emotionally salient stimuli capture the right
    ventral attention network. The amygdala package must declare a
    dependency on this circuit.

../../left/cortex/frontal/gyri/middle_frontal_gyrus
    The left-hemisphere homologue. Structural fields (GYRUS_NAME,
    LOBE, BRODMANN_AREAS, PARS, SUBDIVISIONS) MUST match this package
    exactly. Functional fields (FUNCTIONAL_ROLES, HORMONE_RECEPTORS,
    CONNECTIVITY targets) are EXPECTED to differ — left MFG carries
    verbal WM, verbal fluency, and phonological loop control; right MFG
    carries visuospatial WM, vigilance, spatial attention, and
    reorienting to salience.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "middle_frontal_gyrus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"
    BRODMANN_AREAS      = (8, 9, 46)                # identical to left
    PARS                = {}                        # MFG has no classical pars
    FUNCTIONAL_ROLES    = (                          # DIFFERS from left
                              "visuospatial_working_memory",
                              "spatial_attention",
                              "vigilance",
                              "spatial_set_shifting",
                              "spatial_prospective_memory",
                              "saccade_planning",
                              "mental_rotation",
                              "reorienting_to_salience",
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

Note: ``PARS`` is an empty dict — the MFG has no classical pars
parcellation. The field is kept for uniformity with sibling gyri and
must NOT be deleted; downstream code iterates ``PARS`` unconditionally.

No behaviour. This package is a declarative descriptor; all computation
that references the MFG lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
PROMOTION RULE (when a Brodmann area becomes a package)
--------------------------------------------------------------------------------

If any single Brodmann sub-region (e.g. BA 8 / FEF) later needs its own
substructure — separate connectivity tables, its own memory hooks, or a
distinct receptor profile that does not fit the parent — promote it to a
child package:

    middle_frontal_gyrus/
        __init__.py
        frontal_eye_fields/        # was BA 8
            __init__.py

Then:

  1. Add "frontal_eye_fields" to this package's ``SUBDIVISIONS``.
  2. Remove BA 8 from this package's ``BRODMANN_AREAS`` — it now belongs
     to the child.
  3. Update the parent ``..gyri``'s ``BRODMANN_TO_GYRUS`` to map BA 8 →
     "middle_frontal_gyrus.frontal_eye_fields" (or retain the SFG
     convention if the FEF package is nested under SFG — see below).
  4. Mirror the change on the left side in the same commit.

**The BA 8 canonical-home problem**: FEF straddles the MFG / SFG
boundary, so a promoted FEF package could live under EITHER parent. The
convention adopted must be identical in both hemispheres. The
recommended convention is to nest FEF under ``superior_frontal_gyrus``
(FEF is canonically listed under SFG in most atlases), which means the
right and left MFG both lose BA 8 in the same commit. If the decision is
made to nest FEF under MFG instead, both hemispheres must move together.
No asymmetric promotion is permitted.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../middle_frontal_gyrus``:

    MUST be identical:
        GYRUS_NAME
        LOBE
        BRODMANN_AREAS
        PARS (both empty)
        SUBDIVISIONS (including promotion state)

    MUST differ (and the difference must be documented here):
        HEMISPHERE                ("right" vs "left")
        FUNCTIONAL_ROLES          (visuospatial WM / vigilance / spatial
                                   attention / reorienting to salience vs
                                   verbal WM / fluency / phonology)
        CONNECTIVITY targets      (right-hemisphere structures)
        HORMONE_RECEPTORS profile (noradrenergic / androgenergic /
                                   orexinergic emphasis vs estrogen /
                                   cholinergic / verbal emphasis)

Any deviation from the "MUST be identical" list is a bug. Any unexpected
similarity in the "MUST differ" list is also a bug — if left and right
MFG end up with the same FUNCTIONAL_ROLES, the hemisphere split has
collapsed and the architecture no longer models lateralization.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "middle_frontal_gyrus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BRODMANN_AREAS is (8, 9, 46) — byte-identical to the left sibling.
[ ] PARS is an empty dict — byte-identical to the left sibling.
[ ] SUBDIVISIONS is empty (matches left sibling's promotion state).
[ ] FUNCTIONAL_ROLES contains all eight right-lateralized tags listed
    above and contains NONE of the left-lateralized tags
    (working_memory, verbal_fluency, phonological_loop_control,
    task_set_maintenance's verbal variant).
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY contains every bundle listed above, with
    right-hemisphere targets, including the TPJ / ventral-attention
    projections and the IPS / dorsal-attention projections.
[ ] Every CONNECTIVITY target names a real package in the tree.
[ ] The BA 8 → "superior_frontal_gyrus" convention in the parent
    BRODMANN_TO_GYRUS index is documented and consistent with the left
    side.
[ ] HORMONE_RECEPTORS keys are a subset of the 12 chemicals_hormones
    families, and the right profile documents its noradrenergic /
    androgenergic / orexinergic emphasis.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    left sibling; functional fields deliberately differ.
[ ] No PROMOTION has been done on one side without the other.
[ ] The right-MFG-specific clinical anchors (left hemispatial neglect,
    vigilance decrement, mental rotation) are noted in the docstring
    for cross-referencing from the tests/ directory.
"""