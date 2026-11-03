"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.retrosplenial_cortex
==============================================================================================================

The RETROSPLENIAL CORTEX (RSC) of the right hemisphere — spatial context,
heading, and scene recognition.

Mirror of the left RSC package. Where the PCC answers "do I recognise this?",
the RSC answers "where am I in this, and how is it laid out?". It produces
one output — the `spatial_context` vector — that encodes the current scene's
spatial framing well enough to be used by memory (to bind episodes to
places) and by attention (to bias navigation and scene-driven exploration).

    spatial_context   dict with six named dimensions (see below), each a
                      scalar 0..1 (or, where noted, a unit-normalised
                      direction component):

        heading             the current facing/orientation, relative to the
                            scene's canonical frame. 0 = facing away from
                            the remembered scene centre, 1 = facing toward.
        scene_identity      how strongly the current visual scene matches a
                            recognised scene class (kitchen / forest / face
                            / corridor etc.). Identity, not layout.
        egocentric_frame    how strongly the current scene is represented
                            in body-relative coordinates (left-of-me,
                            ahead-of-me).
        allocentric_frame   how strongly the current scene is represented
                            in world-relative coordinates (north-of-building,
                            left-of-room).
        landmark_binding    how strongly the current scene is anchored to
                            named/recognised landmarks (the clock, the tree,
                            the door).
        spatial_layout      how strongly the current scene's *overall*
                            layout — relative positions of multiple objects —
                            is represented, as opposed to one object at a
                            time.

The vector is the RSC's contribution to the cortex's `salience` slice. It is
*representational* (unlike PCC's `familiarity`/`self_relevance`, which are
evaluative): it says what the spatial context *is*, not how the system feels
about it. Downstream consumers use the vector to tag episodes with place
(MTL), to bias navigation (parietal/motor), and to gate attention toward the
scene representation (occipital).

COMPUTATION
-----------
The RSC is assembled from three Brodmann areas — 26, 29, and 30 — whose
per-area configs live in `cingulate/brodmann_areas/`. Each area contributes
the same six dimensions with different emphases, and the three areas'
contributions are combined via their `rsc_weight` shares (which sum to 1.0
on each hemisphere; on the right, 26: 0.35, 29: 0.325, 30: 0.325 — the
mirror of the left's 0.30 / 0.35 / 0.35).

    encode(inputs, config):
        1. Extract the six dimensions from the current context (see INPUTS).
        2. For each area A in {26, 29, 30}:
             for each dimension d:
                 contrib_A[d] = extract(d) * A.RIGHT_CONFIG[d]
             area_vec_A = contrib_A   # already a 6-d vector
        3. Combine across areas using rsc_weight:
             spatial_context[d] = Σ_A  A.rsc_weight * area_vec_A[d]
        4. Return spatial_context as a dict keyed by the six dimension names.

The cross-area combination is a straight `rsc_weight` blend, dim-by-dim;
there is no intra-area combine step, because the six dimensions are already
the primitive features that each area scores. Areas differ in *how strongly*
they weight each dimension, not in how they internally combine them.

FEATURE EXTRACTION (the RSC's inputs)
-------------------------------------
The six dimensions are not raw sensory signals — they are already-computed
quantities from other lobes and from the MTL:

    heading             from parietal/  — current orientation estimate
                        (integrated from vestibular, visual flow, and
                        self-motion cues by the parietal lobe)
    scene_identity      from occipital/ + temporal/ — recognised scene
                        class from ventral visual stream
    egocentric_frame    from parietal/  — body-relative coordinate
                        encoding of the scene
    allocentric_frame   from parietal/ + hippocampus/ — world-relative
                        coordinate encoding (depends on MTL place-cell
                        state; the RSC reads it, does not compute it)
    landmark_binding    from temporal/  — identification of named
                        landmarks in the current scene
    spatial_layout      from occipital/ + parietal/ — multi-object
                        relative-position encoding

As on the left, the RSC does not compute the underlying spatial
representations itself; it reads them and *combines* them into a single
published vector. On the right, the dimensions it weights most heavily are
heading, egocentric_frame, and spatial_layout — see RIGHT-SPECIFIC BIAS.

WHAT RSC DOES NOT DO
--------------------
    - Does not compute place-cell or grid-cell representations. Those
      live in `medial_temporal_lobe/hippocampus/` (subcortical) and in
      `parietal/`. RSC reads their outputs.
    - Does not compute heading from raw vestibular/visual input. That is
      parietal's job.
    - Does not encode memories. It publishes `spatial_context`; the MTL
      binds it to the episode. RSC is a *tag* for memory, not a memory
      store.
    - Does not direct navigation. It publishes the vector; parietal and
      frontal act on it, gated by the basal ganglia.

RIGHT-SPECIFIC BIAS
-------------------
Same code as the left RSC; the RIGHT config (via the three area configs)
changes the weights. On the right, the RSC's vector is *embodied spatial
layout* weighted:

    heading             higher weight than the left (the right RSC is the
                        dominant heading/orientation node)
    egocentric_frame    higher weight than the left (body-relative
                        coordinates are more strongly encoded on the right)
    spatial_layout      higher weight than the left (whole-scene layout
                        processing is right-lateralised)
    scene_identity      lower weight than the left (scene identity is more
                        often carried by the left's verbal scene tagging)
    landmark_binding    lower weight than the left (landmark naming is more
                        lexical, and therefore more left-leaning)
    allocentric_frame   mildly lower weight than the left (the "map" view
                        is a bit more left-lateralised than the
                        body-relative view)

The RSC itself does not carry a separate RIGHT_CONFIG for the six feature
weights (those live in the area configs). It carries one small per-hemisphere
dict for the vector-level configuration:

    RIGHT_RSC_CONFIG = {
        # normalisation: how the published vector is scaled before it goes
        # into the cortex's salience slice. The vector is not normalised
        # to unit length; each dimension is independently clipped to
        # [0, 1]. This dict sets the clip bounds and the "floor" values
        # (minimum published value for each dimension, so a known-zero
        # signal is distinguishable from an absent one).
        #
        # STRUCTURAL — identical to the left. Lateralisation lives in the
        # area configs, not here. The right hemisphere's vector carries
        # more detail on heading/egocentric/layout because the *area
        # configs* weight those dimensions up, not because the clip
        # bounds differ.
        "floor": {
            "heading":          0.00,
            "scene_identity":   0.00,
            "egocentric_frame": 0.00,
            "allocentric_frame":0.00,
            "landmark_binding": 0.00,
            "spatial_layout":   0.00,
        },
        "ceil": {
            "heading":          1.00,
            "scene_identity":   1.00,
            "egocentric_frame": 1.00,
            "allocentric_frame":1.00,
            "landmark_binding": 1.00,
            "spatial_layout":   1.00,
        },
    }

    LEFT_RSC_CONFIG and RIGHT_RSC_CONFIG are IDENTICAL — the only place
    lateralisation appears is in the three area configs. This is a
    different mirror pattern from the PCC's `familiarity_combine`, which
    does mirror. The config tests must assert:
      - for RSC: LEFT_RSC_CONFIG == RIGHT_RSC_CONFIG (structural keys,
        identical on both sides)
      - for PCC: familiarity_combine weights are complementary across
        hemispheres, with subjective_familiarity identical

INPUT / OUTPUT CONTRACT
-----------------------
    rsc.encode(extracted_dimensions, config) -> dict

    extracted_dimensions : dict with the six dimension names above, each
                           a scalar (0..1 for most; `heading` may be a
                           unit-normalised direction component, in which
                           case it is already in [-1, 1] and the RSC
                           preserves the sign through the blend)
    config               : the three area configs (imported from
                           brodmann_areas) plus the RIGHT_RSC_CONFIG dict
    returns              : dict with the six dimension names, each a
                           scalar in the RSC's published range

    No side effects, no mutation of inputs, no state retained between
    calls. The RSC is a pure function of its inputs and its three area
    configs — like the PCC, and unlike the ACC.

CROSS-MIDLINE RULE
------------------
No import or read of the left hemisphere's RSC. Interhemispheric spatial
context exchange — e.g. when the two hemispheres' heading estimates
disagree, which is common and informative — goes through
`telencephalon/commissures/`, not by direct access. The two hemispheres
publishing different `heading` values for the same scene is an expected
signal, and on the right that disagreement often takes the form "right
hemisphere has a confident heading, left has a confident scene identity"
— the commissures surface both, and the downstream consumer decides.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the three area
  configs and the shared RetrosplenialCortex class, build RIGHT_RSC_CONFIG,
  expose the instance. No encode() logic lives here; the class lives in a
  neutral shared location.
- The class exposes `encode(extracted_dimensions, config) -> dict`
  returning the six-dimension vector. Pure function; no state.
- The cross-area blend is implemented as a small private method
  (`_blend_across_areas`) so it can be unit-tested independently: given
  three area configs and three per-area weight dicts, produce the blended
  vector.
- The `heading` dimension preserves sign: if the extracted value is in
  [-1, 1], the blend must also be in [-1, 1], not clipped to [0, 1].
  Document this in the class implementation; it is the one dimension that
  is not non-negative.
- The three `rsc_weight` shares must sum to 1.0 on each hemisphere. This
  is a per-hemisphere invariant, checked by the config tests.
- The RSC does not read any other lobe's internal state; it reads only
  the six extracted dimensions passed to encode(). Any other read is a
  layering bug.
- RIGHT_RSC_CONFIG is IDENTICAL to LEFT_RSC_CONFIG: same keys, same
  floors, same ceils. The lateralisation lives entirely in the three
  area configs (`brodmann_area_26/29/30.RIGHT_CONFIG` vs `.LEFT_CONFIG`).
  This is the opposite of the PCC pattern, where `familiarity_combine`
  mirrors. Config tests must check the correct pattern for each
  sub-module, not assume "mirror" means one thing across the cingulate.
- Area configs are imported, never duplicated. If a dimension weight
  needs to differ between RSC areas, it lives in the area config, not
  here.
"""