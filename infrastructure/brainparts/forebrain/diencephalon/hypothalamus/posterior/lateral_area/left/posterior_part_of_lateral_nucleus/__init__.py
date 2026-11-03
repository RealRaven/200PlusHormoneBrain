"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.lateral_area.left.posterior_part_of_lateral_nucleus
Anatomical Role:
    Left posterior part of the lateral hypothalamic area (LHA). The
    caudal-most portion of the left LHA orexin/MCH field: segment 3 of
    the three-segment continuum whose segment 1 is
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    (pattern exemplar) and whose segment 2 is
    tuberal/lateral_area/left/tuberal_part_of_lateral_nucleus/ (to be
    drafted).

    See ../../__init__.py (the posterior/lateral_area/left/ container)
    for the LHA continuum framing and the caudal-emphasis description;
    see anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py for the full anatomical description, the two-mode
    framing (ORX-dominant arousal/foraging vs. MCH-dominant
    rest/conservation), the intermingled orexin/MCH populations, and
    the hormone directions. This file is a delta of a delta; it does
    not restate that content.

    LHA CONTINUUM (critical — three segments, one field):
    Segment 1 (anterior) → Segment 2 (tuberal) → Segment 3 (this
    node). Stage 4 audit must treat the three segments as ONE
    neurochemical field; do NOT flag them as duplicates. Continuity
    edge, not structural-identity warning.

Functional Mode:
    Same two-mode function as the anterior pole: ORX-dominant
    (arousal/foraging) vs. MCH-dominant (rest/conservation). The
    posterior segment's caudal emphasis includes orexin projections to
    the same brainstem arousal centers the anterior pole targets
    (LC, VTA, raphe, basal forebrain) plus projections to the posterior
    thalamic arousal nuclei. See the anterior pole file § Functional
    Mode for the full description. No documented functional asymmetry
    between left and right posterior LHA segments. Do not fabricate
    one.

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
    No independent prompt fragment. The LHA arousal/feeding fragment
    is emitted by the anterior pole and augmented by the tuberal and
    posterior segments at the hypothalamic level. AGGREGATION RULE:
    aggregate at the hypothalamic level; do not emit a posterior-LHA
    fragment. See the anterior pole file § Model Integration for the
    MCH-dominance guardrail.

Reciprocal Connections (left-side; the container above lists the
LHA continuity edges and the shared arousal targets; this list adds
the segment-3-specific edges):

    LHA continuity (declared at container level; reproduced here for
    closure):
    - ↔ anterior/lateral_area/left/anterior_part_of_lateral_nucleus
      (segment 3 to segment 1; continuity edge, not duplicate).
    - ↔ tuberal/lateral_area/left/tuberal_part_of_lateral_nucleus
      (segment 3 to segment 2; continuity edge, not duplicate; tuberal
      LHA file to be drafted).

    Segment-3-specific (new in this nucleus):
    - ↔ posterior/medial_area/left/posterior_nucleus (complementary
      arousal drive vs. sympathetic output; distinct nodes; the
      posterior nucleus is the sympathetic output, the posterior LHA
      is the arousal drive; document the cooperation, not duplication).
    - ← tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus
      (circadian → DMH → posterior LHA arousal relay; the DMH
      reciprocates when drafted).
    - → thalamus/left/midline_nuclear_group/paraventricular_nucleus
      (posterior thalamic arousal relay; the thalamic PVT is DISTINCT
      from the hypothalamic PVN — do not conflate; the thalamic PVT
      node is documented under thalamus/*/midline_nuclear_group/ when
      drafted).

    Shared with the anterior pole (do not duplicate):
    - → LC, VTA, raphe, basal forebrain (orexin arousal targets) —
      full list in the anterior pole file.

Notes:
    - DELTA OF A DELTA. This is the nucleus-level leaf; the
      ../../__init__.py container carries the segment-level framing.
      Do not duplicate the container's content here.
    - LHA CONTINUUM CLOSURE: with this file and its right-side
      counterpart, segment 3 of the LHA field is documented on both
      hemispheres. The only remaining work for the field is the
      tuberal segment pair (tuberal/lateral_area/left|right/).
    - The thalamic PVT vs. hypothalamic PVN trap applies here: the
      posterior LHA → thalamic PVT edge is arousal relay, not
      endocrine. Do not conflate the thalamic PVT (midline
      intralaminar-adjacent arousal nucleus) with the hypothalamic PVN
      (CRH/TRH/oxytocin/vasopressin hub).
    - No independent fragment; no two-mode restatement; no hormone
      directions; no memory interfaces (all inherited). Strict delta
      discipline at the leaf level.
    - The DMH → posterior LHA edge (circadian-to-arousal gating) will
      be reciprocated by the DMH file when drafted
      (tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus/).
    - Vocabulary used above is defined in Stage 0 files; see the
      anterior pole file § Notes for the full list.
    - Connects upward to hypothalamus/posterior/lateral_area/left/.
"""