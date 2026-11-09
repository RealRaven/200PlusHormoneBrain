"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.lateral_area.right.posterior_part_of_lateral_nucleus
Anatomical Role:
    Right posterior part of the lateral hypothalamic area (LHA). The
    caudal-most portion of the right LHA orexin/MCH field: segment 3 of
    the three-segment continuum whose segment 1 is
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/
    (pattern exemplar) and whose segment 2 is
    tuberal/lateral_area/right/tuberal_part_of_lateral_nucleus/ (to be
    drafted).

    See ../../left/posterior_part_of_lateral_nucleus/__init__.py (this
    file's delta parent) and anterior/lateral_area/right/
    anterior_part_of_lateral_nucleus/__init__.py (the pattern exemplar)
    for the full anatomical description, the two-mode framing, the
    intermingled orexin/MCH populations, the hormone directions, and
    the memory interfaces. This file is a delta of a delta; it does not
    restate that content.

    LHA CONTINUUM (critical — three segments, one field):
    Segment 1 (anterior) → Segment 2 (tuberal) → Segment 3 (this node).
    Stage 4 audit must treat the three segments as ONE neurochemical
    field; do NOT flag them as duplicates. Continuity edge, not
    structural-identity warning.

Functional Mode:
    Same two-mode function as the left posterior LHA and the anterior
    pole: ORX-dominant (arousal/foraging) vs. MCH-dominant
    (rest/conservation). The posterior segment's caudal emphasis
    includes orexin projections to the same brainstem arousal centers
    the anterior pole targets (LC, VTA, raphe, basal forebrain) plus
    projections to the posterior thalamic arousal nuclei. No documented
    functional asymmetry between left and right posterior LHA segments.
    Do not fabricate one. See ../../left/posterior_part_of_lateral_
    nucleus/__init__.py § Functional Mode.

Hormonal Modulation:
    Same as ../../left/. See anterior/lateral_area/right/
    anterior_part_of_lateral_nucleus/__init__.py § Hormonal Modulation
    for the ghrelin/leptin/glucose/estrogen/NPY directions. Do not
    restate.

Memory Interfaces:
    Same as ../../left/. Reads short_term,
    reinforcement_value_based_learning, temporal_sequence_learning,
    emotional_valence; writes no stored content directly. See the
    anterior pole file § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The LHA arousal/feeding fragment
    is emitted by the anterior pole and augmented by the tuberal and
    posterior segments at the hypothalamic level. AGGREGATION RULE:
    aggregate the right posterior LHA contribution at the hypothalamic
    level; do not emit an independent posterior-LHA fragment. See the
    anterior pole file § Model Integration for the MCH-dominance
    guardrail (MCH-dominance is a state bias, not impairment).

Right-specific reciprocal connections to enforce in Stage 4:

    LHA continuity (declared at container level; reproduced here for
    closure):
    - ↔ anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (segment 3 to segment 1; continuity edge, not duplicate;
      right-side).
    - ↔ tuberal/lateral_area/right/tuberal_part_of_lateral_nucleus
      (segment 3 to segment 2; continuity edge, not duplicate;
      right-side; tuberal LHA file to be drafted).

    Segment-3-specific (new in this nucleus):
    - ↔ posterior/medial_area/right/posterior_nucleus (complementary
      arousal drive vs. sympathetic output; distinct nodes; the
      posterior nucleus is the sympathetic output, the posterior LHA
      is the arousal drive; document the cooperation, not duplication;
      right-side).
    - ← tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus
      (circadian → DMH → posterior LHA arousal relay; the DMH
      reciprocates when drafted; right-side).
    - → thalamus/right/midline_nuclear_group/paraventricular_nucleus
      (posterior thalamic arousal relay; the thalamic PVT is DISTINCT
      from the hypothalamic PVN — do not conflate; the thalamic PVT
      node is documented under thalamus/*/midline_nuclear_group/ when
      drafted; right-side).

    Shared with the anterior pole (do not duplicate):
    - → LC, VTA, raphe, basal forebrain (orexin arousal targets) —
      full list in the anterior pole file.

    - ↔ ../../left/posterior_part_of_lateral_nucleus/ (hemisphere
      counterpart; no functional asymmetry assumed).

Notes:
    - DELTA OF A DELTA, right side. Mirror of ../../left/
      posterior_part_of_lateral_nucleus/. Do not duplicate the
      container's content or the anterior pole's full content.
    - LHA CONTINUUM CLOSURE — BOTH HEMISPHERES NOW COMPLETE for
      segment 3: with this file, the third and final segment of the
      LHA field is documented on both hemispheres. The trap opened in
      anterior_part_of_lateral_nucleus/left/ (and its right
      counterpart) is now CLOSED on both sides: three continuity edges
      per hemisphere, no duplicates. The only remaining work for the
      LHA field is the TUBERAL segment pair (tuberal/lateral_area/
      left|right/), which must declare its own continuity edges to
      both the anterior pole and this posterior segment when drafted.
    - The thalamic PVT vs. hypothalamic PVN trap is reproduced above
      because it applies on the right identically. The right posterior
      LHA → right thalamic PVT edge is arousal relay, not endocrine;
      do not conflate the thalamic PVT (midline intralaminar-adjacent
      arousal nucleus) with the hypothalamic PVN
      (CRH/TRH/oxytocin/vasopressin hub).
    - No independent fragment; no two-mode restatement; no hormone
      directions; no memory interfaces (all inherited). Strict delta
      discipline at the leaf level.
    - The DMH → posterior LHA edge (circadian-to-arousal gating) will
      be reciprocated by the DMH file when drafted
      (tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus/).
    - Vocabulary used above is defined in Stage 0 files; see the
      anterior pole file § Notes for the full list.
    - Connects upward to hypothalamus/posterior/lateral_area/right/.
"""