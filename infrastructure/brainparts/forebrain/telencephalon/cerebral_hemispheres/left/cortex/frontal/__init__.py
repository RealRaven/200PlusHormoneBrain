"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal
========================================================================================

The FRONTAL LOBE of the left hemisphere — the intent and control module.

The frontal lobe is where the cortex answers "what should I do, and how?".
It houses executive function, planning, working memory, voluntary motor
output, and (on the left) language production. It publishes one slice —
`intent` — that the subcortical evaluation layer and the motor output
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
                        nodes. (See the "REGISTRY LAYER" section — one
                        registry entry, area 25, is a cross-lobe pointer
                        rather than a frontal compute area.)

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
whether it can have a `LEFT_CONFIG`, an `encode()`, or neither.


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
functional specs live in the corresponding sub-package docstrings.

REGISTRY LAYER: brodmann_areas/
-------------------------------
Twelve Brodmann areas, most of which are frontal proper (4, 6, 8, 9, 10,
11, 12, 46, 47) plus Broca's area (44, 45) as a sub-package. These are
named constants and per-area config blocks, imported by the four compute
sub-regions. They are not runtime objects.

Two entries require special attention:

    brodmann_area_25/       CROSS-LOBE POINTER, not a frontal compute
                            area. Brodmann 25 is the subgenual ACC, which
                            lives anatomically at the frontal/cingulate
                            boundary and is placed in the tree under
                            BOTH lobes. The COMPUTE for area 25 lives in
                            `cingulate/subgenual_area_25/` (that is where
                            the stateful affect channel is implemented).
                            The entry here is a registry annotation and a
                            documented cross-reference: code that imports
                            area 25 for its affect computation should
                            import from the cingulate package, not from
                            this one. This frontal copy exists so that
                            the tree matches the anatomical fact that
                            area 25 sits on the frontal surface, but it
                            is NOT the affect channel's compute node.

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
                            brodmann_area_45. Broca's area is grouped as
                            a sub-package rather than as two independent
                            areas because (a) the two areas are
                            functionally coupled (area 44 = pars
                            opercularis, area 45 = pars triangularis,
                            and together they implement language
                            production), and (b) the tree places them
                            together so the coupling is visible in the
                            import path. The compute that Broca's area
                            participates in lives in
                            `cortex/prefrontal_cortex/ventrolateral_
                            prefrontal_cortex/` — Broca's area is a
                            Brodmann-area-level labelling of a sub-region
                            of VLPFC, not a fifth compute sub-region.

The REGISTRY-vs-COMPUTE relationship is: registry entries are constants
that COMPUTE sub-regions import. The registry is a labelling layer over
the compute layer, not a parallel compute layer.

ANNOTATION LAYER: gyri/ and sulci/
----------------------------------
Pure anatomical addressing, on the `cingulate/indusium_griseum/` model:

    gyri/    superior_frontal_gyrus, middle_frontal_gyrus,
             inferior_frontal_gyrus — named constants for anatomical
             cross-reference. The gyri are the surface expression of the
             Brodmann areas beneath them; they are not compute nodes.
    sulci/   precentral_sulcus, inferior_frontal_sulcus, orbital_sulcus,
             paracentral_sulcus, superior_frontal_sulcus, olfactory_sulcus
             — named constants for anatomical cross-reference. Sulci are
             boundaries, not actors.

Neither package has a `LEFT_CONFIG`, an `encode()`, or state. They exist
so that per-region metadata (hormone receptor distributions, connectivity
priors, lesion annotations) can reference an anatomical location by
canonical name. Do not give them a lifecycle.

STATE — WHAT MAKES FRONTAL DIFFERENT
------------------------------------
The frontal lobe carries persistent state that the cingulate's compute
sub-modules (PCC, RSC) do not:

    working_memory      the frontal lobe's working-memory buffer, held in
                        prefrontal_cortex/dorsolateral_prefrontal_cortex.
                        Persistent across ticks; contents decay unless
                        refreshed by attention. The buffer is what makes
                        "hold this in mind while you do that" possible.

    goal_stack          the current goal hierarchy, held in
                        prefrontal_cortex/dorsomedial_prefrontal_cortex.
                        Persistent across ticks; the top of the stack is
                        the active goal, lower entries are pending. The
                        stack is what makes multi-step planning possible.

    motor_programs      prepared but not-yet-executed movement programs,
                        held in premotor_cortex/ and
                        supplementary_motor_cortex/. Persistent across
                        ticks; a program prepared this tick may be
                        executed next tick or discarded.

All three are per-hemisphere state, carried by the cortex/ sub-regions,
not by this `__init__.py`. The frontal lobe instance returned here is
composed of the four compute sub-regions, each of which owns its state.
The lobe itself is stateless between ticks — `step()` calls the four
sub-regions with their own state, gathers their contributions, and
returns the `intent` slice plus whatever state the sub-regions emit for
the next tick.

LEFT-SPECIFIC BIAS
------------------
The frontal lobe is the most lateralised in the hemisphere, and the
LEFT config makes that concrete:

    Broca's area (44/45, in VLPFC)    high weight — language production
                                      is dominantly left-lateralised.
                                      The left VLPFC's language-output
                                      component is the strongest single
                                      lateralisation in the lobe.
    dorsolateral prefrontal           higher weight on verbal working
                                      memory (phonological loop), lower
                                      on spatial working memory.
    premotor / primary motor          higher weight on fine, distal
                                      movements (fingers, speech
                                      articulators); lower on gross,
                                      proximal movements.
    supplementary motor               higher weight on sequential,
                                      language-articulatory sequence
                                      planning; lower on spatial
                                      movement sequences.
    orbitofrontal                     mildly higher weight on
                                      positive-valence evaluation
                                      (approach); lower on
                                      negative-valence (threat) — the
                                      opposite of the right's OFC bias.
    dorsomedial prefrontal            higher weight on self-referential
                                      and verbal planning.

The RIGHT config mirrors: Broca's weight drops, spatial working memory
rises, gross motor rises, SMA shifts toward spatial sequences, OFC
shifts toward threat/avoidance.

These are weights, not branches. The same Cortex class runs both sides.

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
                     intent     — the frontal contribution to the cortical
                                  state: goals, plans, working-memory
                                  contents, motor intentions
                     new_state  — the updated persistent state

    Order within step():
        1. Apply top-down gain (basal forebrain, amygdala salience)
        2. prefrontal_cortex computes goals, plans, WM contents, and
           value estimates (updating working_memory and goal_stack state)
        3. premotor_cortex prepares candidate movement programs
        4. supplementary_motor_cortex sequences multi-step programs
        5. primary_motor_cortex produces the final motor output commands
        6. assemble `intent` from all four sub-regions, return with
           updated state

    The frontal lobe never commits an action itself — the basal ganglia
    gate the motor output downstream. Frontal proposes; subcortical
    evaluates and commits.

CROSS-MIDLINE RULE
------------------
No import or read of the right hemisphere's frontal lobe. Interhemispheric
motor and language exchange (e.g. bimanual coordination, cross-midline
verbal-motor coupling) goes through `telencephalon/commissures/`. Within
the left frontal lobe, the four compute sub-regions may read each other's
*published* contributions for binding, but not each other's internal state.


Programming contract for this package
-------------------------------------
- Declarative __init__.py: import the four compute sub-regions, build
  LEFT_FRONTAL_CONFIG, instantiate one shared FrontalLobe class,
  expose it. No per-sub-region logic lives here.
- Each compute sub-region exposes `encode(inputs, top_down, state, config)
  -> (contribution, new_state)`. The FrontalLobe class composes their
  contributions into the `intent` slice and threads their states.
- The FrontalLobe class owns the `step()` orchestration (the six-step
  order above) but not the per-sub-region computations. Each sub-region
  is independently unit-testable with fixed inputs and state.
- The persistent state (working_memory, goal_stack, motor_programs)
  lives in the respective sub-region packages, not in this file. The
  FrontalLobe class holds references but does not know the state's
  internal structure.
- gyri/ and sulci/ are imported by nothing at runtime. They may be
  referenced by docstrings, by the chemicals/hormones config layer, and
  by per-region annotation metadata. Never by compute code.
- brodmann_areas/ is imported by the four compute sub-regions only.
  `brodmann_area_25` in this registry is a cross-lobe pointer — if any
  code actually needs the area-25 affect computation, it imports from
  `cingulate/subgenual_area_25/`, not from here. Document this in the
  relevant sub-region if it ever comes up.
- `brodmann_area_33` is a documented tree artifact (cingulate area living
  under frontal/brodmann_areas). Treat its registry entry as cingulate
  for ownership purposes; if the tree is normalised, it moves.
- LEFT_FRONTAL_CONFIG mirrors RIGHT_FRONTAL_CONFIG with directional
  biases (Broca up/down, verbal-WM up/down, fine-motor up/down, etc.).
  The mirror test should check direction, not just numerical
  complementarity, for the lateralised weights.
"""