"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal
=========================================================================================

The FRONTAL LOBE of the right hemisphere — the intent and control module.

Mirror of the left frontal package. The frontal lobe is where the cortex
answers "what should I do, and how?". It houses executive function,
planning, working memory, voluntary motor output, and (on the right)
spatial/visuomotor control and emotional prosody. It publishes one slice
— `intent` — that the subcortical evaluation layer and the motor output
consume. The frontal lobe is the *controller* of the hemisphere: every
other lobe builds representations of what *is*, and frontal builds the
representation of what *to do*.

The four direct children fall into three categories, and this is important
to know before writing any code against them:

    cortex/             COMPUTE. Four functional sub-regions, each an
                        encode() producer. This is the actual frontal
                        lobe computation.

    brodmann_areas/     REGISTRY. Named constants and per-area config
                        that the cortex/ sub-regions import. Not compute
                        nodes.

    gyri/               ANNOTATION. Anatomical sub-regions (superior/
                        middle/inferior frontal gyri) as named constants.
                        No compute, no state, no config. Third-category
                        packages, like `cingulate/indusium_griseum/`.

    sulci/              ANNOTATION. Anatomical sulci (precentral, inferior
                        frontal, orbital, etc.) as named constants. No
                        compute, no state, no config.

Only `cortex/` computes. `brodmann_areas/` provides constants and config;
`gyri/` and `sulci/` provide anatomical addressing. Every file under this
package should know which category it is in; the category determines
whether it can have a `RIGHT_CONFIG`, an `encode()`, or neither. The
categorisation is identical to the left frontal lobe's — lateralisation
does not change what a package *is*, only what weights it carries.


COMPUTE LAYER: cortex/
----------------------
The frontal cortex is divided into four functional sub-regions, each of
which produces a portion of the `intent` slice:

    prefrontal_cortex/          goals, plans, working-memory contents,
                                action selection, reward evaluation,
                                response inhibition. The executive core.
                                Subdivided into five regions:
                                    dorsolateral_prefrontal_cortex
                                    dorsomedial_prefrontal_cortex
                                    orbitofrontal_cortex
                                    ventrolateral_prefrontal_cortex
                                    ventromedial_prefrontal_cortex

    premotor_cortex/            preparation of voluntary movement,
                                selection of movement parameters, motor
                                imagery. The bridge between the executive
                                (prefrontal) and the executive-output
                                (primary motor).

    primary_motor_cortex/       the final cortical motor output stage;
                                precentral_gyrus is its anatomical
                                implementation (Brodmann area 4). Produces
                                the motor commands that leave the lobe.

    supplementary_motor_cortex/  programming of complex, sequential,
                                internally-generated movements; sequence
                                planning; coordination of bimanual
                                actions. Distinct from premotor (which
                                prepares a single movement) — SMA
                                sequences a *series* of movements.

The four compute regions combine into the `intent` slice, which is the
frontal lobe's contribution to the cortical state. The per-region
functional specs live in the corresponding sub-package docstrings. On
the right, the four regions are the same four; the weights inside them
differ — see RIGHT-SPECIFIC BIAS.

REGISTRY LAYER: brodmann_areas/
-------------------------------
Twelve Brodmann areas, most of which are frontal proper (4, 6, 8, 9, 10,
11, 12, 46, 47) plus Broca's area (44, 45) as a sub-package. These are
named constants and per-area config blocks, imported by the four compute
sub-regions. They are not runtime objects.

Two entries require special attention, and the notes are identical to the
left's because the situations are anatomical facts, not hemisphere-specific:

    brodmann_area_25/       CROSS-LOBE POINTER, not a frontal compute
                            area. Brodmann 25 is the subgenual ACC, which
                            lives anatomically at the frontal/cingulate
                            boundary and is placed in the tree under
                            BOTH lobes. The COMPUTE for area 25 lives in
                            `cingulate/subgenual_area_25/` — on this
                            hemisphere, the right `cingulate/subgenual_
                            area_25/` package. The entry here is a
                            registry annotation and a documented
                            cross-reference: code that imports area 25
                            for its affect computation should import
                            from the cingulate package, not from this
                            one.

    brodmann_area_33/       Present in the tree under frontal/brodmann_areas
                            but anatomically belongs to the cingulate
                            (area 33 is part of the anterior cingulate
                            cortex, adjacent to area 24). This is a tree
                            artifact — it should be treated as a
                            cingulate registry entry for cross-reference
                            purposes, not as a frontal compute area. If
                            the tree is ever renormalised, area 33 moves
                            to `cingulate/brodmann_areas/`; until then,
                            this entry documents the intended ownership.

    brocas_area/            SUB-PACKAGE containing brodmann_area_44 and
                            brodmann_area_45. On the right, Broca's area
                            still exists as a Brodmann-area label, but its
                            language-production compute is heavily
                            left-lateralised. The right Broca's area
                            contributes prosody, emotional tone, and
                            non-lexical speech features; the lexical
                            production role is minimal. The compute lives
                            in `cortex/prefrontal_cortex/ventrolateral_
                            prefrontal_cortex/` as it does on the left,
                            but with a different weight profile.

The REGISTRY-vs-COMPUTE relationship is: registry entries are constants
that COMPUTE sub-regions import. The registry is a labelling layer over
the compute layer, not a parallel compute layer.

ANNOTATION LAYER: gyri/ and sulci/
----------------------------------
Pure anatomical addressing, on the `cingulate/indusium_griseum/` model:

    gyri/    superior_frontal_gyrus, middle_frontal_gyrus,
             inferior_frontal_gyrus — named constants for anatomical
             cross-reference.
    sulci/   precentral_sulcus, inferior_frontal_sulcus, orbital_sulcus,
             paracentral_sulcus, superior_frontal_sulcus, olfactory_sulcus
             — named constants for anatomical cross-reference.

Neither package has a `RIGHT_CONFIG`, an `encode()`, or state. They exist
so that per-region metadata (hormone receptor distributions, connectivity
priors, lesion annotations) can reference an anatomical location by
canonical name. Do not give them a lifecycle. The annotation layer is
identical to the left's — anatomy does not lateralise.

STATE — WHAT MAKES FRONTAL DIFFERENT
------------------------------------
The frontal lobe carries persistent state that the cingulate's pure-function
compute sub-modules (PCC, RSC) do not:

    working_memory      the frontal lobe's working-memory buffer, held in
                        prefrontal_cortex/dorsolateral_prefrontal_cortex.
                        On the right, WM is weighted toward spatial/
                        visuospatial content rather than verbal content.

    goal_stack          the current goal hierarchy, held in
                        prefrontal_cortex/dorsomedial_prefrontal_cortex.
                        On the right, goal representations lean toward
                        spatially-situated and threat-avoidance goals.

    motor_programs      prepared but not-yet-executed movement programs,
                        held in premotor_cortex/ and
                        supplementary_motor_cortex/. On the right, motor
                        programs lean toward gross/proximal and whole-
                        body movements rather than fine distal movements.

All three are per-hemisphere state, carried by the cortex/ sub-regions,
not by this `__init__.py`. The frontal lobe instance returned here is
composed of the four compute sub-regions, each of which owns its state.
The lobe itself is stateless between ticks — `step()` calls the four
sub-regions with their own state, gathers their contributions, and
returns the `intent` slice plus whatever state the sub-regions emit for
the next tick.

RIGHT-SPECIFIC BIAS
-------------------
The frontal lobe is the most lateralised in the hemisphere, and the
RIGHT config makes that concrete:

    Broca's area (44/45, in VLPFC)    low weight on lexical production;
                                      moderate weight on prosody,
                                      emotional tone, and non-lexical
                                      speech features. The right's
                                      Broca's-area contribution is
                                      prosodic/affective, not linguistic.

    dorsolateral prefrontal           higher weight on spatial working
                                      memory (visuospatial sketchpad),
                                      lower on verbal working memory.

    premotor / primary motor          higher weight on gross, proximal
                                      movements (arms, legs, whole-body
                                      orientation); lower on fine, distal
                                      movements (fingers, speech
                                      articulators).

    supplementary motor               higher weight on spatial movement
                                      sequences and bimanual coordination;
                                      lower on language-articulatory
                                      sequences.

    orbitofrontal                     higher weight on negative-valence
                                      evaluation (threat/avoidance) and
                                      autonomic-threat coupling; lower
                                      on positive-valence approach. The
                                      mirror of the left's OFC bias.

    dorsomedial prefrontal            higher weight on spatial/situational
                                      planning and threat-relevant goals;
                                      lower on verbal self-reference.

    ventromedial prefrontal           higher weight on somatic-marker
                                      processing tied to autonomic state
                                      and threat learning; lower on
                                      verbal/lexical value representation.

These are weights, not branches. The same FrontalLobe class runs both
sides. The mirror test should check these DIRECTIONALLY — Broca down,
spatial WM up, gross motor up, OFC threat up, etc. — not just for
numerical complementarity.

INPUT / OUTPUT CONTRACT
-----------------------
    frontal.step(sensory_input, top_down, state) -> (intent, new_state)

    sensory_input  : the sensory representations from the other lobes
                     (occipital/temporal/parietal/insular), passed in
                     from the Cortex base class
    top_down       : subcortical modulators (basal forebrain gain,
                     basal ganglia action-selection feedback, amygdala
                     salience bias)
    state          : the frontal lobe's persistent state (working_memory,
                     goal_stack, motor_programs)
    returns        : (intent, new_state)

    Order within step() is identical to the left's:
        1. Apply top-down gain
        2. prefrontal_cortex computes goals, plans, WM contents, and
           value estimates (updating working_memory and goal_stack state)
        3. premotor_cortex prepares candidate movement programs
        4. supplementary_motor_cortex sequences multi-step programs
        5. primary_motor_cortex produces the final motor output commands
        6. assemble `intent` from all four sub-regions, return with
           updated state

    The frontal lobe never commits an action itself — the basal ganglia
    gate the motor output downstream. Frontal proposes; subcortical
    evaluates and commits. This is true on both hemispheres; lateralisation
    changes *what* is proposed, not *whether* the proposal is gated.

CROSS-MIDLINE RULE
------------------
No import or read of the left hemisphere's frontal lobe. Interhemispheric
motor and language exchange (e.g. bimanual coordination, cross-midline
verbal-motor coupling) goes through `telencephalon/commissures/`. On the
right specifically, the classic cross-midline case is bimanual
coordination: the right frontal lobe proposes the gross/positional
component of a movement while the left proposes the fine/distal component,
and the two have to be combined into a coherent bimanual action. That
combination is the commissures' job, not the frontal lobes' — neither
hemisphere reads the other's motor programs directly. Within the right
frontal lobe, the four compute sub-regions may read each other's
*published* contributions for binding, but not each other's internal
state.


Programming contract for this package
-------------------------------------
- Declarative __init__.py: import the four compute sub-regions, build
  RIGHT_FRONTAL_CONFIG, instantiate one shared FrontalLobe class,
  expose it. No per-sub-region logic lives here.
- Each compute sub-region exposes `encode(inputs, top_down, state, config)
  -> (contribution, new_state)`. The FrontalLobe class composes their
  contributions into the `intent` slice and threads their states.
- The FrontalLobe class owns the `step()` orchestration (the six-step
  order above) but not the per-sub-region computations.
- The persistent state (working_memory, goal_stack, motor_programs)
  lives in the respective sub-region packages, not in this file. The
  FrontalLobe class holds references but does not know the state's
  internal structure.
- gyri/ and sulci/ are imported by nothing at runtime.
- brodmann_areas/ is imported by the four compute sub-regions only.
  `brodmann_area_25` in this registry is a cross-lobe pointer — code
  that needs the area-25 affect computation imports from the right
  `cingulate/subgenual_area_25/`, not from here. `brodmann_area_33` is a
  documented tree artifact (cingulate area living under
  frontal/brodmann_areas).
- RIGHT_FRONTAL_CONFIG mirrors LEFT_FRONTAL_CONFIG with directional
  biases (Broca down/up, verbal-WM down/up, fine-motor down/up, etc.).
  The mirror test should check direction, not just numerical
  complementarity, for the lateralised weights.
- The `step()` contract, the state structure, and the orchestration order
  are IDENTICAL across hemispheres. Only the weights and the directional
  bias differ. If a future change wants to alter the state structure or
  orchestration order on one side, that is a signal that the shared
  FrontalLobe class needs extending on both sides — not that the right
  hemisphere needs a forked implementation.
"""