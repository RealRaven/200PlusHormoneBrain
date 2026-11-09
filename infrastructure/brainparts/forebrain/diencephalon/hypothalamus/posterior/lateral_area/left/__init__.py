"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.lateral_area.left
Anatomical Role:
    Left hemisphere of the posterior part of the lateral hypothalamic
    area (LHA). The third and final segment of the LHA orexin/MCH field
    in the left hemisphere: the caudal pole of the same neurochemical
    field whose anterior pole is documented in anterior/lateral_area/
    left/anterior_part_of_lateral_nucleus/ and whose tuberal segment is
    documented in tuberal/lateral_area/left/tuberal_part_of_lateral_
    nucleus/ (when drafted).

    See anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py for the full anatomical description, the two-mode
    framing (ORX-dominant arousal/foraging vs. MCH-dominant
    rest/conservation), the intermingled orexin/MCH populations, and
    the continuum trap. This file is a delta of the anterior pole; it
    does not restate that content.

    LHA CONTINUUM (critical — three segments of ONE field, not three
    nuclei):
    - Segment 1 (anterior): anterior/lateral_area/left/
      anterior_part_of_lateral_nucleus/ — pattern exemplar.
    - Segment 2 (tuberal): tuberal/lateral_area/left/
      tuberal_part_of_lateral_nucleus/ — to be drafted.
    - Segment 3 (posterior, THIS FILE): caudal pole; closes the field.
    Stage 4 audit must treat the three segments as ONE neurochemical
    field split by the tree's rostrocaudal divisions; do NOT flag them
    as duplicates. Do not merge the nodes; document the continuity
    explicitly. This is a continuity edge, not a structural-identity
    warning.

Functional Mode:
    Same two-mode function as the anterior pole: ORX-dominant
    (arousal/foraging) vs. MCH-dominant (rest/conservation). The
    posterior segment's caudal emphasis includes orexin projections to
    the same brainstem arousal centers the anterior pole targets, plus
    projections to the posterior thalamic arousal nuclei. See the
    anterior pole file § Functional Mode for the full description.
    No documented functional asymmetry between left and right posterior
    LHA segments. Do not fabricate one.

Hormonal Modulation:
    Same as the anterior pole. See anterior/lateral_area/left/
    anterior_part_of_lateral_nucleus/__init__.py § Hormonal Modulation
    for the ghrelin/leptin/glucose/estrogen/NPY directions. Do not
    restate.

Memory Interfaces:
    Same as the anterior pole: reads short_term,
    reinforcement_value_based_learning, temporal_sequence_learning,
    emotional_valence; writes no stored content directly. See the
    anterior pole file § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The LHA arousal/feeding fragment is
    emitted by the anterior pole (the pattern exemplar) and is
    augmented by the tuberal and posterior segments at the hypothalamic
    level. AGGREGATION RULE (mandatory): the posterior LHA segment's
    contribution aggregates at the hypothalamic level; do not emit an
    independent posterior-LHA fragment. See the anterior pole file
    § Model Integration for the fragment shape and the MCH-dominance
    guardrail (MCH-dominance is a state bias, not impairment).

Reciprocal Connections (left-side; the right side is in ../right/;
the full edge list for the LHA field lives in the anterior pole file;
this list adds the posterior-specific edges):
    LHA continuity (the critical edges):
    - ↔ anterior/lateral_area/left/anterior_part_of_lateral_nucleus
      (SAME LHA field, segment 3 to segment 1; continuity edge, not
      duplicate).
    - ↔ tuberal/lateral_area/left/tuberal_part_of_lateral_nucleus
      (SAME LHA field, segment 3 to segment 2; continuity edge, not
      duplicate; tuberal LHA file to be drafted).

    Posterior-specific (new in this segment):
    - ↔ posterior/medial_area/left/posterior_nucleus (complementary
      arousal drive vs. sympathetic output; distinct nodes; the
      posterior nucleus is the sympathetic output, the posterior LHA is
      the arousal drive — document the cooperation, not duplication).
    - ← tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus
      (circadian → DMH → posterior LHA arousal relay; the DMH
      reciprocates when drafted).
    - → thalamus/left/midline_nuclear_group/paraventricular_nucleus
      (posterior thalamic arousal relay; the thalamic PVT is distinct
      from the hypothalamic PVN — do not conflate; the thalamic PVT
      node is documented under thalamus/*/midline_nuclear_group/
      when drafted).

    Shared with the anterior pole (do not duplicate):
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus,
      midbrain/tegmentum/ventral_tegmental_area,
      midbrain/tegmentum/dorsal_raphe_nucleus,
      telencephalon/.../basal_forebrain — orexin arousal targets; the
      full list is in the anterior pole file. This file's posterior
      segment contributes projections to the same targets but does not
      re-enumerate them.

Notes:
    - DELTA OF A DELTA (new pattern in the tree): this file is a delta
      of the anterior pole, inherited THROUGH the tuberal segment. It
      is not a full leaf, and it is not a delta of an adjacent parent.
      It is the third segment of a three-segment continuum. The full
      content lives in the anterior pole; this segment records only its
      position in the field and its posterior-specific edges.
    - LHA CONTINUUM CLOSURE: with this file and ../right/, the third
      and final segment of the LHA field is documented. The trap that
      was opened in anterior_part_of_lateral_nucleus/left/ is now
      CLOSED on both hemispheres: three segments, one field, three
      continuity edges, no duplicates.
    - The thalamic PVT (paraventricular thalamic nucleus) is a
      DIFFERENT structure from the hypothalamic PVN. Do not conflate
      them; the thalamic PVT node will be documented under
      thalamus/*/midline_nuclear_group/paraventricular_nucleus/ when
      drafted. This file's edge to the thalamic PVT is the posterior
      LHA → thalamic arousal relay.
    - No independent fragment; no two-mode restatement; no hormone
      directions; no memory interfaces (all inherited from the anterior
      pole). The delta discipline is strict here because the content
      genuinely lives in the anterior pole.
    - The DMH → posterior LHA edge is the circadian-to-arousal gating
      pathway; when the DMH file is drafted (tuberal/medial_area/
      left|right/dorsomedial_hypothalamic_nucleus/), it will
      reciprocate this edge.
    - Vocabulary used above is defined in Stage 0 files; see the
      anterior pole file § Notes for the full list.
    - Connects upward to hypothalamus/posterior/lateral_area/.
"""