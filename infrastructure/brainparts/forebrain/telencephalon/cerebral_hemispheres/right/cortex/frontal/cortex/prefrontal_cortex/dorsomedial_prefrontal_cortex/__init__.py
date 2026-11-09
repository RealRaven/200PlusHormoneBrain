"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.prefrontal_cortex.dorsomedial_prefrontal_cortex
=================================================================================================================================================

The DORSOMEDIAL PREFRONTAL CORTEX (DMPFC) — right hemisphere. A compute
sub-sub-region of prefrontal, and one of the two stateful children of the
prefrontal family.

Mirror of the left DMPFC package. DMPFC is the goal-management and
self-referential core of the prefrontal cortex. On the RIGHT, the
self-referential content is more affectively and socially anchored (bodily
self-state, threat-relevant self-representation, affective social
cognition), and the goals the stack holds are more spatially-situated and
threat-relevant. The goal-management mechanics are the same as on the
left; the content and its affective colour are mirrored.

DMPFC is called FIRST in prefrontal's order. Its peer_input is empty; its
contribution is the first thing downstream sub-sub-regions can read.

DMPFC OWNS PERSISTENT STATE
----------------------------
Identical to the left. DMPFC carries state across ticks:

    goal_stack    a prioritised stack of goals. On the right, the goals
                  held are more spatially-situated and threat-relevant
                  than the left's verbal/narrative goals; the stack
                  structure itself is identical.

The state is threaded by prefrontal's encode(): DMPFC receives its state
dict from last tick, returns a new one, and prefrontal stores it for the
next tick. The state-threading contract is identical to the left's and to
DLPFC's.

REGISTRY-AREA SOURCE (single source — same structure as the left)
-----------------------------------------------------------------
DMPFC has ONE frontal-registry area source on the right, as on the left:

    brodmann_area_8/        the "prefrontal_cortex" block, with
                            sub_region = "dorsomedial_prefrontal_cortex"

This is the ONLY frontal-tree Brodmann area explicitly assigned to DMPFC
on the right. Its config block (in
`brodmann_area_8.RIGHT_CONFIG["prefrontal_cortex"]`) provides the DMPFC
feature weights: self_reference, mentalizing, social_cognition,
future_prospection, autobiographical, self_other_distinction, plus the
connectivity priors to the cingulate, PCC, precuneus, vmPFC, hippocampus,
amygdala, insula, and DLPFC. On the right, the weights lean toward
affective/social self-reference (social_cognition 0.70,
self_reference 0.55) rather than the left's verbal/mentalizing lean
(mentalizing 0.75, self_reference 0.70); the connectivity priors reflect
the right's stronger amygdala and insula coupling.

Because there is only one area source, there is NO share weight — no
`dmpfc_weight` field. DMPFC's config for composition is just
`brodmann_area_8.RIGHT_CONFIG["prefrontal_cortex"]` plus
`RIGHT_DMPFC_CONFIG` (which carries the goal-stack state parameters and
goal-management thresholds).

DOCUMENTED CAVEATS (registry-adjacent, not registry sources)
------------------------------------------------------------
Identical structure to the left's caveats, restated for the right
because a reader who only sees this file needs the same context:

    AREA 10's MEDIAL PORTION
        Area 10's medial margin is anatomically continuous with DMPFC,
        but area 10 is classified as VMPFC on the right as on the left.
        DMPFC does NOT read any portion of area 10's config. A future
        schema change would be needed if the medial portion ever
        required a separate DMPFC block.

    AREA 9's MEDIAL EXTENSION
        Same situation: area 9 is classified as DLPFC, not DMPFC. The
        medial extension is documented in area 9's ANATOMY as a
        caveat, not as a configurable input to DMPFC.

    AREA 32 (CINGULATE'S DORSAL ACC)
        Expressed as a connectivity prior
        (`to_anterior_cingulate`), not a registry-area read. The
        ACC's control_demand arrives via top_down["cingulate_control"],
        which is a computed signal, not a config read.

    PCC AND PRECUNEUS (DMN)
        Strong DMN-hub coupling on the right (via area 8's prefrontal
        block config's `to_posterior_cingulate` and `to_precuneus`
        priors, both structurally equal to the left's), expressed as
        connectivity priors, not registry-area reads.

The pattern is the same on both sides: anatomical adjacency and
functional coupling are expressed as connectivity priors and top_down
signals; only a frontal-registry area with SUB_REGION ==
"dorsomedial_prefrontal_cortex" is a registry-area source.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

Identical to the left's. Steps:

        1. Read peer_input — DMPFC is called FIRST, so peer_input is
           empty.

        2. Extract DMPFC features from sensory_input and top_down. On
           the right, self-reference and social cues are more
           affectively weighted: bodily self-state, threat signals,
           and affective social cues contribute more strongly than on
           the left.

        3. Apply area 8's prefrontal block config to weight the
           features (via `brodmann_area_8.RIGHT_CONFIG
           ["prefrontal_cortex"]`).

        4. Manage the goal_stack (see GOAL-STACK MANAGEMENT below).

        5. Compute DMPFC's contribution (active goal, pending goals,
           plus the feature dict from step 3).

        6. Return (contribution, new_state).

GOAL-STACK MANAGEMENT (the DMPFC-specific operational pattern)
--------------------------------------------------------------
Identical operations to the left, with the right's content:

    POP     the active goal is removed when it completes, becomes
            impossible, or is abandoned. On the right, the abandonment
            threshold may be crossed faster for threat-relevant goals
            (fear-related goals can trigger rapid goal switching).

    PUSH    new goals are inserted in priority order. On the right,
            threat-relevant goals emerge more readily from top_down's
            amygdala_salience (a threat cue can push a "handle this"
            goal immediately, whereas on the left a verbal cue has
            to pass through more evaluation).

    REPRIORITISE
            priority scores are updated based on age, salience, and
            relevance. On the right, the amygdala_salience term is
            weighted more heavily — a threatening goal gains priority
            faster than a neutral one.

    GENERATE
            when the stack is empty, DMPFC generates a new goal. On
            the right, generation is spatially/threat-weighted
            ("where should I go / what should I avoid?") rather than
            verbally weighted.

The operations (pop/push/reprioritise/generate), the priority-score
components (age × salience × relevance), the threshold structure, and
the hysteresis all match the left's. Only the weightings within each
component differ. The parameters (capacity, thresholds, decay rates)
are STRUCTURAL — equal across hemispheres — see the note under
RIGHT-HEMISPHERE CONFIG below.

FEATURE EXTRACTION (the DMPFC's inputs)
---------------------------------------
Same sources as the left, with the right's emphasis:

    From sensory_input:
        self_relevant_cues     — sensory content referring to the
                                 system's own state. On the right,
                                 more strongly weighted for
                                 affective/bodily content (interoceptive
                                 state, autonomic cues) than verbal
                                 self-description.
        social_cues            — other agents, faces, voices. On the
                                 right, faces and affective vocal
                                 signals are more salient than on the
                                 left (which weights verbal social
                                 content higher).
        goal_cues              — stimuli suggesting a new goal.
                                 On the right, spatially-situated
                                 goal cues and threat cues are more
                                 salient.
        autobiographical_cues  — episodic recall triggers. On the
                                 right, affectively-toned episodes
                                 are more readily recalled (via the
                                 stronger area 8 to_amygdala prior);
                                 on the left, verbosely-described
                                 episodes are (via the stronger
                                 to_hippocampus prior).

    From top_down:
        basal_forebrain_gain   — attention/arousal
        cingulate_control      — targeted control from ACC
        amygdala_salience      — threat/salience bias on goal
                                 priority. On the right this is
                                 weighted more strongly; a threat cue
                                 gets more of a priority boost than
                                 on the left.
        basal_ganglia_gate     — action-selection feedback

The DMPFC feature values (from area 8's prefrontal block config) are
then combined with the extracted features to produce the feature dict
in the contribution. The extraction emphasises right-specific content
(affective self-reference, social cognition, autonomic cues) as area 8's
prefrontal block config specifies.

STATE STRUCTURE
---------------
    goal_stack = {
        "active":     {"goal_id": ..., "content": ...,
                       "priority": ..., "age": ...,
                       "created_tick": ...,
                       "subgoal_of": ... or None},
        "pending":    list of pending goal dicts, sorted by
                      priority (highest first); same fields as active,
        "capacity":   int, from RIGHT_DMPFC_CONFIG,
        "next_goal_id": int, monotonically increasing ID counter,
    }

The structure is IDENTICAL to the left's. The capacity, the priority
components, the hysteresis, and the threshold structure are STRUCTURAL
— equal across hemispheres. Only the CONTENT held (spatial/threat-
oriented goals vs verbal/narrative goals) and the weighting of the
salience component differ; the goal_stack machinery itself is the
same on both sides.

A test that assumed "right DMPFC has a different goal_stack structure
or different capacity" would fail. The lateralisation is entirely in
(a) the CONTENT of the goals held, (b) the weightings within the
priority score (amygdala_salience contribution is larger on the
right), and (c) the extraction weightings — not in the state structure
or its parameters.

RIGHT-SPECIFIC BIAS
------------------
Same class as the left DMPFC; the RIGHT config changes the weights
(via area 8's prefrontal block config):

    self_reference          affectively weighted (self-description
                            via feeling and body state)
    mentalizing             affectively weighted (theory of mind via
                            affective inference about others, not
                            explicit verbal reasoning)
    social_cognition        higher than the left (affective social
                            cognition is the right's anchor)
    future_prospection      affectively weighted (future scenarios
                            felt rather than described)
    to_amygdala             stronger than the left (affective and
                            threat self-representation)
    to_insula               stronger than the left (interoceptive
                            self-state)
    to_hippocampus          weaker than the left (affective over
                            verbal autobiographical recall)

The DMPFC-specific state parameters are STRUCTURAL — equal across
hemispheres. Only the area 8 feature weights and connectivity priors
mirror directionally.

CROSS-MIDLINE RULE
------------------
No import or read of the left DMPFC. Cross-midline goal exchange is
the most interesting DMPFC case in the project, and on the right it is
emphasised more strongly than on the left, because the right's
threat/spatial goals diverge from the left's verbal/narrative goals
more often than the reverse:

    - Divergent goal stacks. The left's DMPFC generates verbally
      mediated goals ("respond to this question"), the right's
      generates spatially/threat-mediated goals ("track that moving
      object" or "avoid that threat"). The divergence is expected and
      common — the two hemispheres are pursuing related but
      distinct goals. The commissures surface the divergence; neither
      DMPFC reads the other's stack directly.

    - Priority conflicts. When the left's active goal and the right's
      active goal are both urgent but incompatible, the ACC (via its
      control_demand channel) may bias toward resolution. The
      commissures carry the conflict signal.

    - Threat-handoff. The right's threat-relevant goals often need to
      bias the left's verbal reasoning ("attend to this — it's
      dangerous"), and the left's verbal goals often need to bias the
      right's spatial attention ("look over there and describe what
      you see"). Both handoffs go through the commissures.

All three are commissural. The right DMPFC's threat/goal divergence
from the left's verbal goals is the most frequently exercised cross-
midline case in the frontal lobe, and getting the commissure
modelling right for this case has outsized impact on the model's
behaviour.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not read peer_input in a way that assumes prior sub-sub-
      regions have run. DMPFC is called FIRST; peer_input is empty.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not hold module-level mutable state.
    - Must not read area 10's medial portion, area 9's medial
      extension, or area 32 as registry-area sources.
    - Must not put goal-management parameters into the registry area's
      config. Those belong in RIGHT_DMPFC_CONFIG.
    - Must not add a `dmpfc_weight` field. DMPFC has a single
      registry-area source; the `dlpfc_weight` pattern does not apply.
    - Must not change the goal_stack parameters (capacity, thresholds,
      decay rates, hysteresis) on the right. These are STRUCTURAL —
      equal across hemispheres. The right's "threat-oriented goals"
      character lives in the CONTENT weighting (extraction and
      salience contribution), not in the state-management
      parameters.
    - Must not import `brodmann_areas/` directly — the area 8
      prefrontal block config is passed in via `config`.
    - Must not import or reference the left DMPFC. Cross-midline
      exchange goes through the commissures, never through direct
      access. The right's threat-goal-to-left-verbal-goal handoff and
      the divergence-detection case are both examples where direct
      import would silently erase the commissural delay that makes
      the divergence signal informative.
    - Must not diverge in structure from the left DMPFC — same class,
      same encode() signature, same goal_stack state structure, same
      goal-management operations. Only the area 8 feature weights
      differ, and only by the directional mirror documented in area
      8's RIGHT_CONFIG.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_DMPFC_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_8",
        "source_block": "prefrontal_cortex",   # block key in area 8's
                                               # RIGHT_CONFIG; sub_region
                                               # = "dorsomedial_
                                               # prefrontal_cortex"

        # Goal-stack state parameters (STRUCTURAL — identical to the
        # left's. These are implementation parameters, not brain-
        # region parameters.)
        "goal_stack_capacity":          5,
        "goal_prioritisation_decay":    0.05,
        "goal_urgency_threshold":       0.6,
        "goal_completion_threshold":    0.8,
        "goal_abandonment_threshold":   0.9,
        "priority_swap_threshold":      0.15,

        # Goal-generation threshold (STRUCTURAL).
        "goal_generation_threshold":    0.4,
    }

    The area 8 prefrontal block config
    (brodmann_area_8.RIGHT_CONFIG["prefrontal_cortex"]) is supplied by
    PrefrontalCortex at construction time. It provides the DMPFC
    feature weights and connectivity priors, with the right's emphasis
    on affective self-reference and social cognition.

    RIGHT_DMPFC_CONFIG is IDENTICAL to LEFT_DMPFC_CONFIG except that
    it names brodmann_area_8.RIGHT_CONFIG["prefrontal_cortex"] as the
    source block. The goal-stack parameters, thresholds, and hysteresis
    are STRUCTURAL — equal across hemispheres. The lateralisation lives
    in the source block's feature weights, not here.

    Two separate tests are needed:
        1. RIGHT_DMPFC_CONFIG == LEFT_DMPFC_CONFIG on the goal-stack
           parameters, thresholds, and hysteresis (structural equality).
        2. The area 8 RIGHT_CONFIG prefrontal block's feature weights
           are a directional mirror of the left's (feature directionality).
    A test that conflated these — e.g. checked goal_stack_capacity for
    directionality — would fail spuriously, because capacity is
    structural, not lateralised.

EXPORTS
-------
    from .dorsomedial_prefrontal_cortex import DorsomedialPrefrontalCortex
    from .dorsomedial_prefrontal_cortex import RIGHT_DMPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. It requires no dlpfc_weight-style
    precondition — DMPFC has a single area source and no share weight
    to verify.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  DorsomedialPrefrontalCortex class, import brodmann_area_8's
  RIGHT_CONFIG, build RIGHT_DMPFC_CONFIG, instantiate the class,
  expose the class and the config.
- The class implements the sub-sub-region encode() signature. The
  goal_stack state structure and the goal-management operations are
  documented above and implemented in the class.
- The class is STATEFUL — it carries goal_stack across ticks. No
  module-level mutable state.
- Goal-stack management is broken into documented, unit-testable
  functions: `_evaluate_active_goal`, `_pop_if_complete_or_abandoned`,
  `_generate_if_empty`, `_reprioritise_pending`,
  `_maybe_push_urgent_goal`.
- Feature extraction is a documented, unit-testable function. On the
  right, extraction weights affective/bodily content higher than
  verbal content; the extraction function reads this from the config,
  not from hardcoded weights.
- The class does not import or access any peer sub-sub-region's state.
- The class does not read area 10, area 9, or area 32 as registry-
  area sources.
- RIGHT_DMPFC_CONFIG is structurally identical to LEFT_DMPFC_CONFIG
  except for the source block reference (RIGHT_CONFIG vs LEFT_CONFIG).
  Goal-stack parameters are STRUCTURAL.
- Goal-stack IDs must be monotonically increasing within a
  hemisphere's lifetime. Cross-hemisphere ID collisions are fine.
- The right's priority score emphasises the amygdala_salience
  contribution more heavily than the left's. This is expressed via a
  feature weight in the extraction (area 8's prefrontal block config's
  `to_amygdala` and the salience contribution), not via a change to
  the priority-score formula. The formula is structural; the input
  weightings are lateralised.
- Must not import or reference the left DMPFC. Cross-midline exchange
  goes through `telencephalon/commissures/`.
"""