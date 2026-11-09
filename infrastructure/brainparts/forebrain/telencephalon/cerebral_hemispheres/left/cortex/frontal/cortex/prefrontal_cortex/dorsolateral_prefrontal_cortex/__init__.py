"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.prefrontal_cortex.dorsolateral_prefrontal_cortex
================================================================================================================================================

The DORSOLATERAL PREFRONTAL CORTEX (DLPFC) — left hemisphere. A compute
sub-sub-region of prefrontal, and one of the two stateful children of the
prefrontal family.

DLPFC is the working-memory executive: it holds content online across a
delay, applies rules to that content, plans multi-step actions, and
implements cognitive control. It is the "effortful, deliberate" prefrontal
pole — the counterpart to VMPFC's automatic, value-based evaluator.

DLPFC OWNS PERSISTENT STATE
----------------------------
Unlike its sibling OFC, VMPFC, and VLPFC (all pure functions), DLPFC
carries state across ticks:

    working_memory    the working-memory buffer. A structured dict whose
                      slot organisation is documented below. Contents
                      persist across ticks; unrehearsed items decay
                      unless refreshed by attention; rehearsed or
                      goal-relevant items are held longer.

The state is threaded by prefrontal's encode(): DLPFC receives its state
dict from last tick, returns a new one, and prefrontal stores it for the
next tick. DLPFC never inspects or mutates other sub-sub-regions' state —
the state threading contract is uniform.

THE TWO REGISTRY AREAS AND THEIR SHARE
--------------------------------------
DLPFC is composed of two Brodmann areas:

    area 9    the HOLD-and-PLAN anchor — working-memory contents held
              online, plans constructed, goals maintained.
    area 46   the RULE-and-CONTROL anchor — task sets maintained, rules
              represented and applied, responses monitored against the
              rule, sustained attention over the task.

Each area contributes to DLPFC's computation via its `LEFT_CONFIG` in
`brodmann_areas/`. The per-area shares are `dlpfc_weight`:

    9 : 46 = 0.55 : 0.45 on both hemispheres.

The shares are STRUCTURAL (equal across hemispheres); only the feature
values inside each area's config lateralise.

PENDING AMENDMENT (HARD PRECONDITION)
-------------------------------------
This package depends on `brodmann_areas/brodmann_area_9/LEFT_CONFIG`
containing the field `"dlpfc_weight": 0.55`. At the time this docstring
was written, that field is PENDING — it is documented in both area-46
files' SCHEMA ADDITION sections but not yet applied to area 9's config.

This package treats the amendment as a HARD PRECONDITION, not as
something to work around:

    - If `brodmann_area_9.LEFT_CONFIG["dlpfc_weight"]` is present and
      equals 0.55, the composition proceeds normally.
    - If it is absent, the DLPFC class raises a documented error at
      construction time ("DLPFC requires brodmann_area_9.LEFT_CONFIG
      ['dlpfc_weight']; see the pending amendment documented in
      brodmann_area_46's SCHEMA ADDITION section"). It does NOT
      silently default the share, does NOT compute a partial
      composition from area 46 alone, and does NOT infer the share
      from any other field.
    - If it is present but not 0.55, the DLPFC class raises a
      documented error ("brodmann_area_9.LEFT_CONFIG['dlpfc_weight']
      must be 0.55; found <value>. The DLPFC shares are structural
      (equal across hemispheres) and must sum to 1.0 across 9 and
      46.").

The reason for the hard precondition: the DLPFC composition is only
correct when both areas' `dlpfc_weight` fields are present and sum to
1.0. A silent fallback would let a partially-amended registry produce a
subtly wrong DLPFC contribution, which is worse than a loud construction
failure. The amendment is small and documented; failing loudly until
it's applied is the correct behaviour.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

        1. Read peer_input — DLPFC is called second in prefrontal's order
           (after DMPFC), so it has access to:
               peer_input["dorsomedial_prefrontal_cortex"]
                   — the current goals (top of the goal stack)
        2. Extract DLPFC features from sensory_input, top_down, and
           peer_input (see FEATURE EXTRACTION below).
        3. For each area A in {9, 46}:
               for each feature f that A provides:
                   area_contrib_A[f] = extract(f) * A.LEFT_CONFIG[f]
        4. Combine across areas using the per-area shares:
               for each feature f:
                   contribution[f] = (
                       A9.dlpfc_weight  * area_contrib_9[f]
                     + A46.dlpfc_weight * area_contrib_46[f]
                   )
           (features are NOT disjoint between 9 and 46 — both areas
           provide overlapping features at different weights. The
           blend combines them. See THE OVERLAP-AND-SPECIFIC FEATURES
           section below.)
        5. Update working_memory state:
               - refresh the contents flagged by this tick's attention
                 (from top_down["basal_forebrain"]["attention"])
               - decay unrefreshed contents by a documented rate
               - insert any new content from sensory_input that passes
                 the goal-relevance gate
               - evict items that exceed capacity
        6. Compute DLPFC's contribution (the working-memory contents as
           this tick's output, plus the feature dict from step 4).
        7. Return (contribution, new_state).

The overlap-and-specific features structure is the DLPFC-specific
composition mechanism; documented in that section.

THE OVERLAP-AND-SPECIFIC FEATURES
---------------------------------
DLPFC's two areas OVERLAP on core features but each carries additional
area-specific features. The composition must handle both kinds
correctly:

    OVERLAPPING FEATURES (both 9 and 46 provide):
        verbal_working_memory, spatial_working_memory, planning,
        cognitive_control, response_inhibition, rule_representation,
        task_switching, abstract_reasoning, goal_maintenance,
        distraction_resistance.
        These are combined via the dlpfc_weight blend (step 4 above).
        The blend produces a weighted average of the two areas'
        feature values, which is correct because both areas are
        contributing to the SAME feature — the blend says "how much
        of this feature's value comes from 9's weighting vs 46's".

    AREA-9-ONLY FEATURES (only area 9 provides):
        (none at the feature-key level; area 9's distinguishing
        content is its specific values on the overlapping features —
        higher WM/plan weights — not a set of unique feature keys.)

    AREA-46-ONLY FEATURES (only area 46 provides):
        rule_maintenance_over_delay, sustained_attention,
        response_monitoring, task_set_binding, verbal_rule_content,
        spatial_rule_content.
        These are NOT blended — they are area 46's contribution
        alone, and they appear in DLPFC's contribution directly
        (weighted by whatever area-46-specific weight applies; see
        below).

    The rule: features present in BOTH areas' configs are blended via
    dlpfc_weight; features present in ONLY ONE area's config pass
    through from that area without blending (no "0 weight from the
    other area" — that would be a false blend of a feature the other
    area doesn't provide).

    This is a genuinely different composition pattern from OFC's (11,
    12, area 47-OFC) and from PCC's (23, 31). OFC's areas were
    disjoint (each provided distinct outcome features); PCC's areas
    overlapped but had no area-specific additions. DLPFC is the first
    composition in the project that has BOTH overlap and additions,
    and the blend rule above is what handles it. It is documented as
    a DLPFC-specific pattern that future composities with the same
    structure (overlap + additions) will reuse.

FEATURE EXTRACTION (the DLPFC's inputs)
---------------------------------------
Features are extracted from the three input sources:

    From sensory_input (via the other lobes):
        content               — the current sensory content, broken
                                into verbal/symbolic vs spatial/
                                visual components (verbal on the
                                left, spatial on the right;
                                both present, weighted by the
                                hemisphere's bias)
        rule_cues             — task-rule signals present in the
                                current stimuli (e.g. a task
                                instruction, a rule-indicating
                                stimulus)

    From top_down (via subcortical):
        basal_forebrain_gain  — global attention/arousal
                                modulator; sets the working-memory
                                refresh and decay rates
        cingulate_control     — targeted control demand from the
                                ACC (via the salience slice); biases
                                which working-memory contents are
                                rehearsed this tick
        amygdala_salience     — threat/salience bias on content;
                                high-salience content is held
                                longer
        basal_ganglia_gate    — action-selection feedback; the
                                previous tick's gating decision
                                (approved/vetoed) is available as
                                feedback for working-memory updating

    From peer_input (via DMPFC):
        goals                 — the current goal from the goal
                                stack; DLPFC uses it to determine
                                which content is goal-relevant
                                (goal-relevant items are rehearsed;
                                irrelevant items decay faster)

The full feature-extraction rules are documented in the DLPFC class
implementation. This docstring defines what features exist and where
they come from; the class defines how they are extracted from the raw
input dicts.

WORKING_MEMORY STATE STRUCTURE
------------------------------
    working_memory = {
        "slots":       list of currently held items, each:
                       {"content": <representation>,
                        "age":     <ticks held, incremented per tick>,
                        "salience": <from amygdala_salience>,
                        "rehearsed": <bool, refreshed this tick>},
        "capacity":    int, the maximum number of slots
                       (defaults to 7, from LEFT_DLPFC_CONFIG; the
                       "magic number" is a prior, not a hard constraint),
        "decay_rate":  float per-tick decay probability for unrehearsed
                       items (defaults to 0.15; modulated by
                       basal_forebrain_gain),
    }

The structure is DLPFC's internal business — the parent (PrefrontalCortex)
does not inspect or mutate it, only threads it. Consumers of DLPFC's
contribution get the working-memory CONTENTS (as the contribution's
"working_memory" field), not the internal slot bookkeeping.

LEFT-SPECIFIC BIAS
------------------
Same class as the right DLPFC; the LEFT config changes the weights
(via the two area configs):

    verbal_working_memory    higher weight (via area 9's anchor and
                             area 46's verbal_rule_content coupling)
    spatial_working_memory   lower weight
    rule content             verbal/symbolic (via area 46's
                             verbal_rule_content weight)
    temporal coupling        stronger (via area 9's to_temporal and
                             area 46's to_temporal)
    parietal coupling        weaker (via area 9's to_parietal and
                             area 46's to_parietal)
    dlpfc_weight             structural (0.55 : 0.45) — same on
                             both hemispheres

The class, the state structure, the composition logic, the blend rule
for overlapping vs area-specific features, and the feature extraction
pipeline are IDENTICAL across hemispheres. Only the config values
inside the two area configs differ. RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right DLPFC. Cross-midline working-memory
exchange goes through `telencephalon/commissures/`, never through direct
access. The canonical left-DLPFC case: a verbal WM task may need spatial
content from the right DLPFC (e.g. holding a word while visualising its
referent); the exchange is commissural.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not inspect or mutate peer sub-sub-regions' state. DLPFC
      reads peer CONTRIBUTIONS (published output), not peer STATE.
    - Must not bypass the dlpfc_weight blend by hardcoding a share,
      inferring a share from feature values, or defaulting when the
      area-9 amendment is absent. The hard precondition (see above)
      is the contract.
    - Must not silently blend area-46-only features as if area 9 were
      providing them at weight 0. The "overlap-and-specific" rule is
      explicit: overlap features blend, area-specific features pass
      through.
    - Must not add a sixth contribution to prefrontal. DLPFC is a
      contributing sub-sub-region, not a composite.
    - Must not hold module-level mutable state. The working_memory
      lives in the state dict returned by encode(), not in module
      globals.
    - Must not import `brodmann_areas/` directly — the areas' configs
      are passed in via `config` (built by PrefrontalCortex at
      construction, from the areas' LEFT_CONFIG exports). DLPFC does
      not reach into the registry at runtime; it reads from the config
      dict it was given.
    - Must not import or reference the right DLPFC. Cross-midline
      exchange goes through the commissures, never through direct
      access.
    - Must not diverge in structure from the right DLPFC — same class,
      same encode() signature, same state structure (working_memory
      with slots/capacity/decay_rate), same overlap-and-specific
      composition rule. Only the two area configs' values differ.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_DLPFC_CONFIG = {
        # Composition-level config (structural; identical to the
        # right's apart from the values inherited from area configs).
        "areas":               ["brodmann_area_9", "brodmann_area_46"],
        "share_field":         "dlpfc_weight",
        "expected_shares": {
            "brodmann_area_9":  0.55,
            "brodmann_area_46": 0.45,
        },

        # Working-memory parameters (state-structure, not lateralised;
        # both hemispheres use the same defaults).
        "working_memory_capacity":      7,
        "working_memory_decay_rate":    0.15,
        "rehearsal_threshold":          0.5,   # above this
                                               # attention/control
                                               # value, content is
                                               # rehearsed (not
                                               # decayed) this tick

        # Goal-relevance gate: content is inserted into working
        # memory only if its goal-relevance score (computed from
        # peer_input["dorsomedial_prefrontal_cortex"]["goals"]) is
        # above this threshold. Structural; same on both sides.
        "goal_relevance_gate":          0.4,
    }

    The two area configs (brodmann_area_9.LEFT_CONFIG and
    brodmann_area_46.LEFT_CONFIG) are supplied by PrefrontalCortex at
    construction time, not built here. They are the source of the
    per-feature values that the blend combines; this package's config
    is only the composition-level parameters and the working-memory
    state parameters.

    The `expected_shares` field is used by the hard-precondition check
    (see above). If either area's `dlpfc_weight` disagrees with the
    expected value, the class raises at construction.

    RIGHT_DLPFC_CONFIG is IDENTICAL except that it names the
    RIGHT_CONFIG exports of the two areas. The working-memory
    parameters and the goal-relevance gate are structural (equal
    across hemispheres) — spatial-vs-verbal content differs, but the
    capacity, decay rate, and gate threshold are the same machinery
    on both sides.

EXPORTS
-------
    from .dorsolateral_prefrontal_cortex import DorsolateralPrefrontalCortex
    from .dorsolateral_prefrontal_cortex import LEFT_DLPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects: encode(sensory_input, top_down,
    peer_input, state, config) -> (contribution, new_state).

    The class raises a construction-time error if the area-9
    `dlpfc_weight` amendment has not been applied (see the pending-
    amendment section above).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  DorsolateralPrefrontalCortex class (from a neutral location shared
  with the right hemisphere), import the two registry areas' LEFT_CONFIG
  exports, verify the dlpfc_weight precondition, build
  LEFT_DLPFC_CONFIG, instantiate the class, expose the class and the
  config. No computation lives here.
- The class implements the sub-sub-region encode() signature. The
  state structure (working_memory with slots/capacity/decay_rate) is
  documented above and implemented in the class.
- The class is STATEFUL — it carries working_memory across ticks via
  the threaded state dict. It must NOT carry module-level mutable
  state (the state lives in the dicts).
- The overlap-and-specific composition rule (blend overlap features
  via dlpfc_weight; pass area-specific features through without
  blending) is a documented, unit-testable function
  (`_combine_areas(area_contributions, shares)`), tested with
  synthetic feature dicts to confirm the blend rule is applied
  correctly.
- The hard precondition on `dlpfc_weight` is checked at construction.
  If the amendment is applied, the class builds normally; if not, it
  raises with a message pointing at the SCHEMA ADDITION section of
  area-46's docstring. Do NOT add a fallback path — the precondition
  is the contract.
- Feature extraction (step 2) is a documented, unit-testable function
  (`_extract_features(...)`), independent of the composition step.
- Working-memory update (step 5) is a documented, unit-testable
  function (`_update_working_memory(...)`), tested with synthetic
  state dicts and tick inputs to confirm decay, rehearsal, insertion,
  and eviction work as specified.
- The class does not import or access any peer sub-sub-region's state
  — it reads peer contributions from peer_input only. A direct access
  to a peer's state would violate the state-threading contract and is
  a bug.
- LEFT_DLPFC_CONFIG is structurally identical to RIGHT_DLPFC_CONFIG
  except for the values inherited from the two area configs.
  Working-memory parameters, goal-relevance gate, expected_shares,
  and the area list are STRUCTURAL — equal across hemispheres. A test
  should assert this, separately from the area configs' directional
  mirror tests.
- If a future change wants to add a third DLPFC registry area (unlikely
  — 9 and 46 are the DLPFC pair), the `areas` list gains an entry, the
  expected_shares map gains an entry, and the shares must still sum to
  1.0. This is a substantive modeling decision, not a config tweak.
"""