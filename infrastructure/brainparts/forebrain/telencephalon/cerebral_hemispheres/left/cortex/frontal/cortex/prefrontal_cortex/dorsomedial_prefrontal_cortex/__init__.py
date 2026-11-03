"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.prefrontal_cortex.dorsomedial_prefrontal_cortex
================================================================================================================================================

The DORSOMEDIAL PREFRONTAL CORTEX (DMPFC) — left hemisphere. A compute
sub-sub-region of prefrontal, and one of the two stateful children of the
prefrontal family.

DMPFC is the goal-management and self-referential core of the prefrontal
cortex. It maintains the goal stack (what the system is currently trying to
do, and what's queued behind it), generates new goals when the current one
completes or becomes impossible, prioritises competing goals, and computes
the self-referential and social-evaluative content that grounds the
system's representation of itself and its relations to others.

DMPFC is called FIRST in prefrontal's order. Its peer_input is empty; its
contribution is the first thing downstream sub-sub-regions can read.

DMPFC OWNS PERSISTENT STATE
----------------------------
Like DLPFC, DMPFC carries state across ticks:

    goal_stack    a prioritised stack of goals. The top of the stack is
                  the active goal (what the system is currently pursuing);
                  entries below are pending goals in priority order.
                  Contents persist across ticks; completed or abandoned
                  goals are popped; new goals are pushed when they become
                  relevant; existing goals' priorities may be updated by
                  this tick's evaluation.

The state is threaded by prefrontal's encode(): DMPFC receives its state
dict from last tick, returns a new one, and prefrontal stores it for the
next tick. The state-threading contract is identical to DLPFC's.

REGISTRY-AREA SOURCE (single source — different from DLPFC)
-----------------------------------------------------------
DMPFC has ONE frontal-registry area source:

    brodmann_area_8/        the "prefrontal_cortex" block, with
                            sub_region = "dorsomedial_prefrontal_cortex"

This is the ONLY frontal-tree Brodmann area explicitly assigned to DMPFC.
Its config block (in `brodmann_area_8.LEFT_CONFIG["prefrontal_cortex"]`)
provides the DMPFC feature weights: self_reference, mentalizing,
social_cognition, future_prospection, autobiographical,
self_other_distinction, plus the connectivity priors to the cingulate,
PCC, precuneus, vmPFC, hippocampus, amygdala, insula, and DLPFC.

Because there is only one area source, there is NO share weight — no
`dmpfc_weight` field, unlike DLPFC's `dlpfc_weight`. DMPFC's config for
composition is just `brodmann_area_8.LEFT_CONFIG["prefrontal_cortex"]`
plus `LEFT_DMPFC_CONFIG` (which carries the goal-stack state parameters
and goal-management thresholds, documented below).

DOCUMENTED CAVEATS (registry-adjacent, not registry sources)
------------------------------------------------------------
Three anatomical relationships need clarifying because they are DMPFC-
adjacent but not DMPFC registry-area sources. A future contributor might
wonder why they are not read as DMPFC inputs; the answer is here.

    AREA 10's MEDIAL PORTION
        Area 10 is anatomically continuous with DMPFC at its dorsal/medial
        margin. But in this project's frontal registry, area 10 is
        classified as VMPFC (its SUB_REGION is
        "ventromedial_prefrontal_cortex"). The medial continuity is
        documented as a caveat in area 10's ANATOMY, not as a separate
        config block. DMPFC therefore does NOT read any portion of area
        10's config. If area 10's medial portion ever needs to contribute
        to DMPFC specifically, that is a schema change (a documented
        sub-region overlap variant), not a silent config read.

    AREA 9's MEDIAL EXTENSION
        Same situation as area 10. Area 9 extends onto the medial surface
        at its dorsal margin, where its cytoarchitecture is continuous
        with DMPFC. But area 9 is classified as DLPFC (SUB_REGION =
        "dorsolateral_prefrontal_cortex"). The medial extension is
        documented as a caveat in area 9's ANATOMY, not as a separate
        config block. DMPFC does NOT read area 9's config.

    AREA 32 (CINGULATE'S DORSAL ACC)
        Area 32 is a cingulate area (it lives in the cingulate tree, not
        the frontal tree). DMPFC has strong reciprocal connectivity with
        area 32 — this is a real and important coupling — but it is
        expressed as a CONNECTIVITY PRIOR (see area 8's prefrontal block
        config, `to_anterior_cingulate`), not as a registry-area read.
        DMPFC does not read area 32's config; it receives area 32's
        ACC contribution via the salience slice (from the ACC's
        control_demand channel, through top_down["cingulate_control"]).
        This is the correct mechanism: the ACC's contribution is a
        computed signal, not a config read.

    PCC AND PRECUNEUS (DMN)
        Same as area 32: DMPFC has strong DMN-hub coupling with posterior
        cingulate and precuneus, expressed as connectivity priors in area
        8's prefrontal block config. Not a registry-area read.

The pattern: anatomical adjacency and functional coupling are expressed
as connectivity priors and top_down signals; only a frontal-registry area
with SUB_REGION == "dorsomedial_prefrontal_cortex" is a registry-area
source. This keeps the registry-area-to-config mapping one-to-one, and it
keeps cross-tree couplings (cingulate, DMN) as signals rather than as
registry reads.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

        1. Read peer_input — DMPFC is called FIRST, so peer_input is
           empty. DMPFC does not read any upstream sub-sub-region's
           contribution; its inputs are sensory_input, top_down, and
           its own goal_stack state.

        2. Extract DMPFC features from sensory_input and top_down (see
           FEATURE EXTRACTION below). On the left, self-reference and
           mentalizing are verbally weighted.

        3. Apply area 8's prefrontal block config to weight the features
           (the feature weights are in
           `brodmann_area_8.LEFT_CONFIG["prefrontal_cortex"]`).

        4. Manage the goal_stack (see GOAL-STACK MANAGEMENT below):
               a. Evaluate the active goal: is it complete? impossible?
                  still relevant? If any of these, pop it.
               b. If the stack is empty, generate a new goal from
                  sensory_input + self-referential context.
               c. Prioritise pending goals against the current active
                  goal; reorder if a higher-priority goal has emerged.
               d. If a new goal is urgent enough, push it.
               e. Update each goal's age and priority score.

        5. Compute DMPFC's contribution (the goal_stack's active goal,
           the pending goals list, plus the feature dict from step 3).

        6. Return (contribution, new_state).

GOAL-STACK MANAGEMENT (the DMPFC-specific operational pattern)
--------------------------------------------------------------
DMPFC's state is a goal_stack, and its tick-by-tick operation is stack
management. The operations:

    POP     the active goal is removed when:
              - goal_completion_threshold is exceeded (it succeeded),
              - goal_impossibility_signal is present (it can't succeed),
              - goal_abandonment_threshold is exceeded (it's been
                active too long without progress).
            On pop, the next-highest-priority pending goal becomes
            active.

    PUSH    a new goal is added when:
              - the stack is empty (a baseline goal is generated), OR
              - an urgent goal emerges from sensory_input/top_down
                (urgency above goal_urgency_threshold), OR
              - the current goal's evaluation generates a subgoal
                (a decomposition of the active goal into prerequisites).
            Pushed goals are inserted in priority order.

    REPRIORITISE
            every tick, each goal's priority score is updated based on:
              - its age (old goals lose priority slowly, via
                goal_prioritisation_decay),
              - its salience (from amygdala_salience and cingulate_control),
              - its goal-relevance (from the current sensory context).
            The stack is re-sorted after prioritisation if any score
            changed materially (above a small threshold). A goal that
            crosses priority_swap_threshold against the active goal
            becomes the new active goal.

    GENERATE
            when the stack is empty, DMPFC generates a new goal from
            the current sensory context and self-referential content.
            On the left, generation is verbally weighted ("what should
            I do next?" is evaluated verbally); on the right, it is
            spatially weighted ("where should I go next?").

The operational parameters (capacity, thresholds, decay rates) live in
LEFT_DMPFC_CONFIG, not in area 8's config. They are STATE MANAGEMENT
parameters, not FEATURE WEIGHTS — the distinction matters because they
would be wrong to put in the registry area (they aren't brain-region
parameters, they're goal-stack implementation parameters).

FEATURE EXTRACTION (the DMPFC's inputs)
---------------------------------------
DMPFC features come from two sources (not three — it has no peer input):

    From sensory_input:
        self_relevant_cues     — sensory content that refers to the
                                 system's own state, history, or
                                 identity
        social_cues            — other agents, faces, voices, social
                                 signals
        goal_cues              — stimuli that suggest a new goal or
                                 subgoal (e.g. an instruction, a
                                 problem that needs solving)
        autobiographical_cues  — content that triggers episodic recall

    From top_down:
        basal_forebrain_gain   — attention/arousal
        cingulate_control      — targeted control from ACC; on high
                                 conflict or error, ACC may bias
                                 toward goal re-evaluation (DMPFC
                                 responds by reprioritising or
                                 switching)
        amygdala_salience      — threat/salience bias on goal priority
        basal_ganglia_gate     — action-selection feedback; if a
                                 committed action fails or is vetoed,
                                 DMPFC may need to revise the goal

The DMPFC feature values (from area 8's prefrontal block config) are
then combined with these extracted features to produce the feature dict
in the contribution. The goal-management operations take the goal_stack
state and these features as inputs.

STATE STRUCTURE
---------------
    goal_stack = {
        "active":     {"goal_id": ..., "content": ...,
                       "priority": ..., "age": ...,
                       "created_tick": ...,
                       "subgoal_of": ... or None},
        "pending":    list of pending goal dicts, sorted by
                      priority (highest first); same fields as active,
        "capacity":   int, the maximum number of active+pending goals
                      (defaults to 5, from LEFT_DMPFC_CONFIG),
        "next_goal_id": int, monotonically increasing ID counter for
                      goal dicts,
    }

The active goal is stored separately from pending goals because it is
the one this tick operates on (its content is what downstream
sub-sub-regions consume). Pending goals are what may become active
later. When the active goal is popped, the highest-priority pending
goal is promoted to active.

The structure is DMPFC's internal business — the parent (PrefrontalCortex)
threads it opaquely. Consumers of DMPFC's contribution get the ACTIVE
goal (as the contribution's "goals" field) and the pending goals list,
not the internal bookkeeping (goal_id, created_tick).

LEFT-SPECIFIC BIAS
------------------
Same class as the right DMPFC; the LEFT config changes the weights
(via area 8's prefrontal block config):

    self_reference          verbally weighted (self-description via
                            words and narratives)
    mentalizing             verbally weighted (theory of mind via
                            explicit reasoning about others' beliefs)
    social_cognition        lower than the right (verbal social
                            cognition is less affectively nuanced)
    future_prospection      verbally weighted (future scenarios
                            described in words)
    to_amygdala             weaker than the right
    to_insula               weaker than the right
    to_hippocampus          stronger than the right (verbal
                            autobiographical retrieval)

The DMPFC-specific state parameters (goal_stack_capacity, thresholds,
decay rates) are STRUCTURAL — equal across hemispheres. The
lateralisation is entirely in the area 8 feature weights and
connectivity priors, not in the goal-stack machinery. A test that
assumed "left DMPFC has different goal-management parameters" would
fail; the goal-stack mechanics are the same on both sides, only the
CONTENT of the goals differs (verbal on the left, spatial/threat-
oriented on the right, as the sensory context and peer inputs bias
the goal generation).

CROSS-MIDLINE RULE
------------------
No import or read of the right DMPFC. Cross-midline goal exchange is a
subtle case that the commissures need to model:

    - Divergent goal stacks. When the two hemispheres' DMPFCs have
      different active goals (common — left's verbally-generated
      goals and right's spatially/threat-generated goals may differ),
      the divergence itself is a signal. The commissures surface it;
      neither DMPFC reads the other's stack directly.
    - Priority conflicts. When the left's goal and the right's goal
      are both urgent but incompatible, the commissures surface the
      conflict, and the ACC (via its control_demand channel) may bias
      toward resolution.
    - Goal handoff. When a goal generated by one hemisphere's DMPFC
      requires the other hemisphere's resources (e.g. a verbal goal
      requiring spatial manipulation), the handoff goes through the
      commissures.

All three are commissural. The "two DMPFCs disagreeing about the goal"
scenario is one of the most interesting cross-midline cases in the
project because the divergence is expected and informative, not a bug
to be suppressed.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not read peer_input in a way that assumes prior sub-sub-
      regions have run. DMPFC is called FIRST; peer_input is empty.
      If a future reorder puts DMPFC later, that is a config change
      in LEFT_PREFRONTAL_CORTEX_CONFIG["order"], not a code change
      in DMPFC's encode().
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not hold module-level mutable state. The goal_stack lives
      in the state dict returned by encode(), not in module globals.
    - Must not read area 10's medial portion, area 9's medial
      extension, or area 32 (cingulate). These are documented caveats
      (see DOCUMENTED CAVEATS above), not registry-area sources.
      Reading them directly would violate the registry-to-config
      one-to-one mapping.
    - Must not put goal-management parameters (capacity, thresholds,
      decay rates) into the registry area's config. Those belong in
      LEFT_DMPFC_CONFIG — they are state-management parameters, not
      brain-region parameters.
    - Must not add a `dmpfc_weight` field. DMPFC has a single registry-
      area source (area 8's prefrontal block), so there is no share
      to weight. The `dlpfc_weight` pattern (areas 9 and 46) does not
      apply here.
    - Must not import `brodmann_areas/` directly — the area 8
      prefrontal block config is passed in via `config`.
    - Must not import or reference the right DMPFC. Cross-midline
      exchange goes through the commissures, never through direct
      access.
    - Must not diverge in structure from the right DMPFC — same class,
      same encode() signature, same goal_stack state structure, same
      goal-management operations. Only the area 8 feature weights
      differ, and only by the directional mirror documented in area
      8's config.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_DMPFC_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_8",
        "source_block": "prefrontal_cortex",   # block key in area 8's
                                               # config (the DMPFC
                                               # block; sub_region =
                                               # "dorsomedial_
                                               # prefrontal_cortex")

        # Goal-stack state parameters (STRUCTURAL — equal across
        # hemispheres. These are implementation parameters, not
        # brain-region parameters, so they do NOT live in the
        # registry area's config.)
        "goal_stack_capacity":          5,
        "goal_prioritisation_decay":    0.05,  # per-tick priority
                                               # decay for old goals
        "goal_urgency_threshold":       0.6,   # above this, a new
                                               # goal pushes even if
                                               # the stack is full
        "goal_completion_threshold":    0.8,   # above this, the
                                               # active goal is
                                               # considered complete
                                               # and popped
        "goal_abandonment_threshold":   0.9,   # above this, the
                                               # active goal is
                                               # abandoned (too long
                                               # without progress)
        "priority_swap_threshold":      0.15,  # a pending goal must
                                               # outscore the active
                                               # by this much to
                                               # become the new
                                               # active goal (hysteresis
                                               # to prevent flapping)

        # Goal-generation threshold (STRUCTURAL). A new goal is
        # generated from sensory context only if its relevance score
        # is above this.
        "goal_generation_threshold":    0.4,
    }

    The area 8 prefrontal block config (brodmann_area_8.LEFT_CONFIG
    ["prefrontal_cortex"]) is supplied by PrefrontalCortex at
    construction time, not built here. It provides the DMPFC feature
    weights (self_reference, mentalizing, social_cognition,
    future_prospection, autobiographical, self_other_distinction) and
    the connectivity priors.

    RIGHT_DMPFC_CONFIG is IDENTICAL except that it names
    brodmann_area_8.RIGHT_CONFIG["prefrontal_cortex"] as the source
    block. The goal-stack parameters, thresholds, and hysteresis are
    STRUCTURAL — equal across hemispheres. Only the source block's
    feature weights differ.

EXPORTS
-------
    from .dorsomedial_prefrontal_cortex import DorsomedialPrefrontalCortex
    from .dorsomedial_prefrontal_cortex import LEFT_DMPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. It requires no dlpfc_weight-style
    precondition — DMPFC has a single area source and no share weight
    to verify.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  DorsomedialPrefrontalCortex class, import brodmann_area_8's
  LEFT_CONFIG, build LEFT_DMPFC_CONFIG, instantiate the class, expose
  the class and the config.
- The class implements the sub-sub-region encode() signature. The
  goal_stack state structure and the goal-management operations are
  documented above and implemented in the class.
- The class is STATEFUL — it carries goal_stack across ticks via the
  threaded state dict. It must NOT carry module-level mutable state.
- Goal-stack management is broken into documented, unit-testable
  functions: `_evaluate_active_goal`, `_pop_if_complete_or_abandoned`,
  `_generate_if_empty`, `_reprioritise_pending`,
  `_maybe_push_urgent_goal`. Each can be tested in isolation with
  synthetic state and inputs.
- Feature extraction is a documented, unit-testable function.
- The class does not import or access any peer sub-sub-region's state.
- The class does not read area 10, area 9, or area 32 as registry-
  area sources. Any reading of those is via top_down signals
  (cingulate_control), not via config.
- LEFT_DMPFC_CONFIG is structurally identical to RIGHT_DMPFC_CONFIG
  except for the source block reference (LEFT_CONFIG vs RIGHT_CONFIG).
  Goal-stack parameters are STRUCTURAL — equal across hemispheres.
  Two tests: (1) equality of the goal-stack parameters and (2)
  directionality of the source block's feature weights via the area 8
  mirror test.
- Goal-stack IDs must be monotonically increasing within a
  hemisphere's lifetime. Cross-hemisphere ID collisions are fine —
  the two stacks are independent, and the commissures don't need
  globally unique IDs (goal handoff creates a new ID in the receiving
  hemisphere).
- If a future change wants to give DMPFC additional registry-area
  sources (e.g. by giving area 10 a documented DMPFC portion), that
  is a substantive schema change — a new sub-region share pattern
  (analogous to `dlpfc_weight`) — not a config tweak.
- Must not import or reference the right DMPFC. Cross-midline
  exchange goes through `telencephalon/commissures/`.
"""