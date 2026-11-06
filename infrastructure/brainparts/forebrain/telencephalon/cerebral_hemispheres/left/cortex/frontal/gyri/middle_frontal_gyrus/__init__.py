"""
Middle Frontal Gyrus (MFG) — Left Hemisphere
=============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
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
``../../right/cortex/frontal/gyri/middle_frontal_gyrus``. Structural
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
prefrontal cortex (DLPFC)**. On the left hemisphere it is the dominant
node for **verbal** working memory, **task-set** maintenance, and
**top-down attentional gain**.

--------------------------------------------------------------------------------
CYTOARCHITECTONIC PARCELLATION (BRODMANN AREAS)
--------------------------------------------------------------------------------

The MFG spans three Brodmann areas, running caudo-rostral:

    BA 8    caudal MFG
        The caudal-most strip, abutting the precentral sulcus. Hosts the
        **frontal eye fields (FEF)** — the cortical saccade-planning
        centre. The left FEF directs contralateral (rightward) saccades
        in the left hemisphere. Also contributes to attentional
        orienting and to the premotor planning of visually guided
        reaching.
        NOTE: the FEF straddles the MFG / SFG boundary; BA 8 is listed
        under BOTH this package and the superior_frontal_gyrus package.
        The parent ``..gyri``'s ``BRODMANN_TO_GYRUS`` index must
        disambiguate — see the cross-reference section.

    BA 9    dorsal MFG
        The dorsal-prefrontal strip. Core of **task-set maintenance**,
        **rule representation**, and **prospective planning**. Together
        with BA 46 it forms the *dorsal* DLPFC subdivision that holds
        abstract task structure online across delays.

    BA 46   mid-DLPFC
        The intermediate strip, often called the *principal sulcus*
        homologue (in macaques, area 46 is the principal sulcus cortex).
        Core of **working memory** — both verbal (left-dominant) and
        spatial (right-dominant). The left BA 46 is the substrate of the
        phonological / verbal working-memory register; the right BA 46
        is the substrate of the visuospatial sketchpad. Hosts the
        **attentional gain controller** that biases posterior sensory
        cortex toward task-relevant features.

``BA 9 + BA 46 = DLPFC proper``. BA 8 is FEF and is shared with SFG.

--------------------------------------------------------------------------------
FUNCTIONAL ROLES (this architecture's tags)
--------------------------------------------------------------------------------

The constants in this package must declare the following role tags:

    working_memory
        Maintaining and manipulating task-relevant information across
        delays. Left MFG is the **verbal** register (letters, words,
        numbers, phonological codes); this is the left-lateralized
        component of the working-memory network.

    attentional_gain
        Top-down biasing of posterior sensory cortex toward
        task-relevant stimuli. The MFG sends gain-modulating signals to
        parietal and temporal cortex via SLF I and SLF II.

    task_set_maintenance
        Holding an abstract rule or task instruction online so that
        subsequent stimuli can be mapped to appropriate responses.

    set_shifting
        Switching between task rules or response mappings when the
        environment changes. Overlaps with the right MFG's spatial
        variant; left MFG shifts verbal / semantic sets.

    prospective_memory
        Remembering to perform a delayed intention ("remember to buy
        milk on the way home"). Overlaps with SFG BA 10 but the left
        MFG holds the *content* of the intention while SFG holds the
        *cue*.

    saccade_planning
        Generating and controlling eye movements (BA 8 / FEF). In the
        left hemisphere, this includes contralateral (rightward)
        saccades and reading-related saccades.

    verbal_fluency
        Rapid generation of words under phonological or semantic
        constraint. Left MFG is a core node; damage reduces letter and
        category fluency.

    phonological_loop_control
        The control process that refreshes the phonological loop
        (articulatory rehearsal). Interacts bidirectionally with left
        IFG's phonological assembly.

These tags map onto the memory subsystem as follows:

    working_memory            → memory/stores/short_term
    attentional_gain          → memory/stores/short_term (gain modulation)
    task_set_maintenance      → memory/stores/long_term/implicit/procedural
    set_shifting              → memory/stores/long_term/implicit/procedural
    prospective_memory        → memory/stores/long_term/explicit/episodic
    saccade_planning          → memory/stores/long_term/implicit/motor_sensorimotor_adaptation
    verbal_fluency            → memory/stores/long_term/explicit/semantic
    phonological_loop_control → memory/stores/short_term

Note that three of the eight roles route to ``short_term`` — the left
MFG is the frontal lobe's short-term-memory workbench, and the memory
architecture must reflect that.

--------------------------------------------------------------------------------
LONG-RANGE CONNECTIVITY
--------------------------------------------------------------------------------

The ``CONNECTIVITY`` dictionary must contain at minimum:

    superior_longitudinal_fasciculus I (SLF I)
        → superior_parietal_lobule
        → precuneus
        Dorsal attention network; top-down spatial and feature attention.

    superior_longitudinal_fasciculus II (SLF II)
        → inferior_parietal_lobule (angular gyrus, supramarginal gyrus)
        → intraparietal_sulcus
        Working-memory and attention-control loop with the dorsal
        attention network.

    superior_longitudinal_fasciculus III (SLF III)
        → inferior_parietal_lobule (supramarginal gyrus)
        → superior_temporal_gyrus (posterior)
        Language-related working-memory loop; links left MFG to
        Wernicke's area and the phonological store.

    arcuate_fasciculus (indirect segment)
        → middle_temporal_gyrus (posterior)
        → inferior_parietal_lobule
        The indirect arcuate segment that connects the DLPFC to the
        posterior language network.

    frontal_aslant_tract
        → inferior_frontal_gyrus (pars opercularis)
        → supplementary_motor_area (SFG)
        Speech-initiation pathway that carries task-set instructions
        from DLPFC to speech-motor cortex.

    uncinate_fasciculus
        → anterior_temporal_lobe
        → temporal_pole
        Semantic control loop: DLPFC ↔ semantic hub.

    extreme_capsule
        → insula (anterior)
        Interoceptive and task-relevance gating.

    corticostriatal projections
        → caudate_nucleus (left, head)
        → putamen (left)
        The cognitive-associative fronto-striatal loop. This loop gates
        working-memory updating — it decides when a task-set should be
        replaced.

    corticothalamic projections
        → mediodorsal_nucleus (left MD)
        → ventrolateral_nucleus (left VL)
        Executive and motor thalamic relays.

    cingulum bundle
        → posterior_cingulate
        → parahippocampal_gyrus
        The task-relevance ↔ memory-retrieval loop.

    posterior parietal projections (via SLF II)
        → intraparietal_sulcus (LIP / VIP homologues)
        The dorsal attention network's principal frontal node.

Cross-hemispheric:

    corpus_callosum (genu / body)
        → homotopic right MFG
        Carries the interhemispheric dialogue between left verbal and
        right visuospatial working memory.

--------------------------------------------------------------------------------
HORMONE / NEUROMODULATOR RECEPTORS
--------------------------------------------------------------------------------

The ``HORMONE_RECEPTORS`` dictionary must express which of the 12
hormone families in ``infrastructure/chemicals_hormones/`` modulate this
gyrus. For the left MFG the documented set is:

    dopamine            D1, D2, D4
        05_neuro_modulators_mood — working-memory maintenance and
        updating. The classic "inverted-U" of D1 signalling in DLPFC
        is well established: too little D1 → unstable WM; too much
        D1 → rigid WM. D4 is enriched in DLPFC and modulates
        attentional gating.

    noradrenaline       alpha-2A, alpha-1, beta
        05_neuro_modulators_mood — arousal, vigilance, and the
        stability-flexibility tradeoff. Alpha-2A agonism (guanfacine)
        improves working memory and attentional control. Locus
        coeruleus → DLPFC projections are dense.

    serotonin           5-HT2A, 5-HT1A
        05_neuro_modulators_mood — cognitive flexibility and
        reversal learning; 5-HT2A modulates DLPFC pyramidal-cell
        excitability.

    acetylcholine       M1, nicotinic alpha-7, alpha-4-beta-2
        05_neuro_modulators_mood — attention and working-memory
        encoding. Cholinergic projections from the basal forebrain to
        DLPFC are essential for WM maintenance.

    estrogen            ER-alpha, ER-beta
        01_hpg_axis_androgens_reproduction — verbal working memory
        and verbal fluency fluctuate with cycle phase; estrogen
        upregulates DLPFC dopamine synthesis and D1 receptor
        expression.

    progesterone        PR
        01_hpg_axis_androgens_reproduction — modulates the
        stability-flexibility tradeoff; high progesterone (luteal
        phase) shifts DLPFC toward stability.

    cortisol            GR, MR
        02_hpa_axis_stress_survival — stress impairs DLPFC-dependent
        working memory (the classic "stress shifts control to
        habit" phenomenon). DLPFC expresses dense glucocorticoid
        receptors.

    insulin             IR
        04_satiety_gut_energy_signaling — insulin resistance
        impairs working memory; DLPFC insulin signalling modulates
        dopamine clearance.

    thyroid hormone     TR-alpha, TR-beta
        03_metabolic_thyroid_growth — hypothyroidism slows working
        memory and verbal fluency.

    orexin / hypocretin OX1R, OX2R
        04_satiety_gut_energy_signaling — arousal and sustained
        attention; orexin projections to DLPFC are dense.

    BDNF (growth factor, structural anchor family)
        09_structural_anchors_transporters_catalysts — synaptic
        plasticity in DLPFC; BDNF Val66Met polymorphism modulates
        working-memory capacity.

This profile is left-lateralized in emphasis: verbal WM is more
estrogen- and cholinergic-sensitive on the left, while right MFG's
visuospatial WM is more noradrenergic and androgenergic (see the right
sibling).

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
    The corticostriatal loop from left MFG to left caudate head is the
    principal substrate of working-memory updating. The caudate
    package must declare this gyrus as an upstream cortical input.

../../subcortical/medial_temporal_lobe/hippocampus
    The cingulum-bundle loop connects left MFG to parahippocampal
    cortex, supporting the task-relevance ↔ memory-retrieval
    interaction. The hippocampus package must declare a dependency on
    this loop.

../../right/cortex/frontal/gyri/middle_frontal_gyrus
    The right-hemisphere homologue. Structural fields (GYRUS_NAME,
    LOBE, BRODMANN_AREAS, SUBDIVISIONS) MUST match this package exactly.
    Functional fields (FUNCTIONAL_ROLES, HORMONE_RECEPTORS,
    CONNECTIVITY targets) are EXPECTED to differ — left MFG carries
    verbal WM, verbal fluency, and phonological loop control; right MFG
    carries visuospatial WM, spatial attention, and vigilance.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "middle_frontal_gyrus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"
    BRODMANN_AREAS      = (8, 9, 46)                # identical to left
    PARS                = {}                        # MFG has no classical pars
    FUNCTIONAL_ROLES    = (
                              "working_memory",
                              "attentional_gain",
                              "task_set_maintenance",
                              "set_shifting",
                              "prospective_memory",
                              "saccade_planning",
                              "verbal_fluency",
                              "phonological_loop_control",
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
     "middle_frontal_gyrus.frontal_eye_fields".
  4. Mirror the change on the right side in the same commit.

The promotion rule must preserve the BA 8 → SFG convention noted above:
FEF lives on the MFG / SFG boundary, and the parent index must pick ONE
canonical home. Whatever convention is adopted must be adopted
identically in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../middle_frontal_gyrus``:

    MUST be identical:
        GYRUS_NAME
        LOBE
        BRODMANN_AREAS
        PARS (both empty)
        SUBDIVISIONS (including promotion state)

    MUST differ (and the difference must be documented here):
        HEMISPHERE                ("left" vs "right")
        FUNCTIONAL_ROLES          (verbal WM / fluency / phonology vs
                                   visuospatial WM / vigilance / spatial
                                   attention)
        CONNECTIVITY targets      (left-hemisphere structures)
        HORMONE_RECEPTORS profile (estrogen / cholinergic / verbal
                                   emphasis vs noradrenergic /
                                   androgenergic / spatial emphasis)

Any deviation from the "MUST be identical" list is a bug. Any unexpected
similarity in the "MUST differ" list is also a bug — if left and right
MFG end up with the same FUNCTIONAL_ROLES, the hemisphere split has
collapsed and the architecture no longer models lateralization.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "middle_frontal_gyrus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BRODMANN_AREAS is (8, 9, 46), sorted ascending, and byte-identical
    to the right sibling.
[ ] PARS is an empty dict (presence required, contents empty).
[ ] SUBDIVISIONS is empty (matches right sibling's promotion state).
[ ] FUNCTIONAL_ROLES contains all eight left-lateralized tags listed
    above and contains NONE of the right-lateralized tags
    (visuospatial_working_memory, vigilance, spatial_attention).
[ ] Every role tag maps to a real module under memory/stores/.
[ ] CONNECTIVITY contains every bundle listed above, with
    left-hemisphere targets.
[ ] Every CONNECTIVITY target names a real package in the tree.
[ ] The BA 8 → "superior_frontal_gyrus" convention in the parent
    BRODMANN_TO_GYRUS index is documented, and this package's
    BRODMANN_AREAS correctly includes BA 8 despite the index pointing
    elsewhere.
[ ] HORMONE_RECEPTORS keys are a subset of the 12 chemicals_hormones
    families, and the left profile documents its verbal / estrogen /
    cholinergic emphasis.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    right sibling; functional fields deliberately differ.
[ ] No PROMOTION has been done on one side without the other.
"""