"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.posterior_cingulate
=============================================================================================================

The POSTERIOR CINGULATE CORTEX (PCC) of the right hemisphere — contextual
evaluation and self-referential signalling.

Mirror of the left PCC package. Where the ACC answers "am I doing this well?",
the PCC answers "do I recognise this, and does it matter to me?". It produces
two scalars every tick:

    familiarity      scalar 0..1. How well the current situation matches
                     previously experienced contexts. High familiarity means
                     the incoming scene/context is recognised; low familiarity
                     means it is novel and may warrant encoding.

    self_relevance   scalar 0..1. How much the current situation is
                     self-referential — about the system's own state, goals,
                     history, or identity. High self_relevance biases
                     attention toward the stimulus; low self_relevance
                     deprioritises it.

These two signals are the PCC's contribution to the cortex's `salience`
slice. They are *evaluative*, not *representational*: PCC does not encode
what the scene is, nor where it is; it encodes how *familiar* and how
*self-relevant* the current configuration is. Downstream consumers use these
scalars to gate memory encoding (familiarity drives the MTL's
decide-to-encode signal) and attention allocation (self_relevance drives
targeted gain on the lobes representing the stimulus).

COMPUTATION
-----------
The PCC is assembled from two Brodmann areas — 23 and 31 — whose per-area
configs live in `cingulate/brodmann_areas/`. Each area contributes the same
five features (verbal_context, autobiographical, scene_construction,
self_reference, subjective_familiarity) with different emphases, and the two
areas' contributions are combined via their `pcc_weight` shares (which sum
to 1.0 on each hemisphere; on the right, 23: 0.45, 31: 0.55 — the split is
the mirror of the left's 0.55/0.45).

    encode(inputs, config):
        1. Extract the five features from the current context (see INPUTS).
        2. For each area A in {23, 31}:
             for each feature f:
                 contrib_A[f] = extract(f) * A.RIGHT_CONFIG[f]
             area_familiarity_A = combine(
                 contrib_A["subjective_familiarity"],
                 contrib_A["verbal_context"],
                 contrib_A["autobiographical"],
                 contrib_A["scene_construction"],
             )
             area_self_relevance_A = contrib_A["self_reference"]
        3. Combine across areas using pcc_weight:
             familiarity    = Σ_A  A.pcc_weight * area_familiarity_A
             self_relevance = Σ_A  A.pcc_weight * area_self_relevance_A
        4. Return {"familiarity": ..., "self_relevance": ...}

The intra-area `combine()` for familiarity is a weighted sum with per-area
weights internal to the area config; the cross-area combination is a
straight `pcc_weight` blend. Both are documented per-area; the PCC class
just performs the combination.

FEATURE EXTRACTION (the PCC's inputs)
-------------------------------------
The five features are not raw sensory signals — they are already-computed
quantities from other lobes:

    verbal_context          from temporal/  — how strongly the current
                            context is tagged as verbal/linguistic
    autobiographical        from temporal/  — how strongly the current
                            context cues autobiographical recall
    scene_construction      from occipital/ — how strongly the visual scene
                            matches a constructed/scene representation
    self_reference          from frontal/   — how strongly the current
                            situation refers to the system's own goals/state
    subjective_familiarity  from temporal/  — the medial-temporal-lobe's
                            own familiarity estimate, used as an input

As on the left, the PCC reads the MTL's familiarity rather than recomputing
it; PCC's role is to *integrate* that estimate with contextual features and
to *publish* a single value. On the right, the contextual features that
matter most are scene/spatial — see LEFT-SPECIFIC BIAS below.

WHAT PCC DOES NOT DO
--------------------
    - Does not encode or retrieve memories. It publishes familiarity and
      self_relevance; the actual encode/recall happens in
      `medial_temporal_lobe/hippocampus/` (subcortical). PCC is a *cue*
      to the memory system, not the memory system itself.
    - Does not represent the scene. Scene/object identity is
      occipital/temporal; PCC's `scene_construction` input is a summary
      from those lobes, not a representation of its own.
    - Does not direct attention. It publishes self_relevance; the Cortex
      base class applies targeted gain on the next tick. PCC cannot mutate
      other lobes.

RIGHT-SPECIFIC BIAS
-------------------
Same code as the left PCC; the RIGHT config (via the two area configs)
changes the weights:

    familiarity     higher weight on scene/visuospatial and subjective
                    familiarity inputs (area 31's contributions dominate
                    the blend at 0.55, and area 31's scene_construction
                    feature is weighted up)
    self_relevance  higher weight on scene/spatially-mediated
                    self-reference (the right hemisphere's self-model is
                    more spatial/situational than lexical)

The PCC itself does not carry a separate RIGHT_CONFIG — its config is
the *combination* of its two area configs. Anything that needs to be
configured at the PCC level (e.g. the intra-area `combine()` weighting)
is a small per-hemisphere dict, documented below and stored alongside the
class in the shared module.

    RIGHT_PCC_CONFIG = {
        # intra-area familiarity combine weights (same keys as the area
        # feature names, applied to the per-area contributions before the
        # cross-area blend). These are small — most of the weighting
        # lives in the area configs; these tune how the four familiarity
        # features combine within each area.
        "familiarity_combine": {
            "subjective_familiarity": 0.40,   # same as left
            "scene_construction":     0.30,   # right: up from 0.15
            "verbal_context":         0.15,   # right: down from 0.25
            "autobiographical":       0.15,   # right: down from 0.20
        },
        # sum-to-1 invariant on familiarity_combine
    }

    The mirror shape is clean: subjective_familiarity stays put (it is
    the MTL-driven anchor on both sides), while the scene vs. verbal/
    autobiographical balance swaps — scene up on the right, verbal and
    autobiographical down.

INPUT / OUTPUT CONTRACT
-----------------------
    pcc.encode(extracted_features, config) -> dict

    extracted_features : dict with the five feature names above, each a
                         scalar 0..1 (already extracted by the cortex's
                         cross-lobe feature pass)
    config             : the area configs (imported from brodmann_areas)
                         plus the RIGHT_PCC_CONFIG dict above
    returns            : {"familiarity": float, "self_relevance": float}

    No side effects, no mutation of inputs, no state retained between
    calls. The PCC is a pure function of its inputs and its two area
    configs.

CROSS-MIDLINE RULE
------------------
No import or read of the left hemisphere's PCC. The PCC's inputs are
intra-hemispheric; interhemispheric context exchange (e.g. when the two
hemispheres disagree about familiarity) goes through
`telencephalon/commissures/`, not by direct access. The two hemispheres
publishing different familiarity values for the same scene is a real and
expected signal, and it is the commissures' job to surface that
disagreement, not the PCC's.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the two area
  configs and the shared PosteriorCingulate class, build RIGHT_PCC_CONFIG,
  expose the instance. No encode() logic lives here; the class lives in a
  neutral shared location.
- The class exposes `encode(extracted_features, config) -> dict` returning
  the two channels. Pure function; no state.
- The intra-area familiarity combine and the cross-area pcc_weight blend
  are each implemented as small private methods (`_combine_familiarity`,
  `_blend_across_areas`) so each can be unit-tested independently.
- The `familiarity_combine` weights must sum to 1.0. This is a
  per-hemisphere invariant, checked by the config tests.
- The PCC does not read any other lobe's internal state; it reads only
  the five extracted features passed to encode(). Any other read is a
  layering bug.
- RIGHT_PCC_CONFIG mirrors LEFT_PCC_CONFIG: identical keys, complementary
  feature weights for scene_construction vs. verbal/autobiographical,
  with subjective_familiarity unchanged across hemispheres. Assert this
  in tests, including the sum-to-1 invariant on each side.
- Area configs are imported, never duplicated. If a feature weight needs
  to differ between PCC areas, it lives in the area config, not here.
"""