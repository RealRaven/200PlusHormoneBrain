"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.lateral_area
Anatomical Role:
    The lateral area of the posterior hypothalamus. It contains the
    posterior part of the lateral hypothalamic area (LHA): the third and
    final segment of the LHA orexin/MCH field. The three segments are:
        - Anterior pole: anterior/lateral_area/left|right/
          anterior_part_of_lateral_nucleus/ (the pattern exemplar).
        - Tuberal segment: tuberal/lateral_area/left|right/
          tuberal_part_of_lateral_nucleus/ (the middle segment).
        - Posterior segment: this node's children
          (posterior_part_of_lateral_nucleus/left|right/).
    The posterior segment is the caudal pole of the same neurochemical
    field: the same intermingled orexin/hypocretin and MCH populations
    extend caudally into the posterior division, with the same
    two-mode functional structure documented in the anterior pole.

    The posterior LHA is anatomically adjacent to the posterior
    hypothalamic nucleus (posterior/medial_area/left|right/
    posterior_nucleus/), which drives sympathetic arousal. The two are
    functionally complementary: the posterior nucleus is the
    sympathetic output, and the posterior LHA contributes arousal drive
    via orexin projections to the same brainstem arousal centers. They
    are distinct nodes; document the cooperation without merging.

    LHA CONTINUUM CLOSURE (critical — reproduces the trap first declared
    in anterior_part_of_lateral_nucleus/ and continued in
    tuberal/lateral_area/):
    The posterior segment is the THIRD and FINAL segment of the LHA
    field. Stage 4 audit must treat the three segments as ONE
    neurochemical field split by the tree's rostrocaudal divisions; do
    not merge the nodes; document the continuity explicitly. When the
    children (posterior_part_of_lateral_nucleus/left|right/) are
    drafted, they must declare reciprocal continuity edges to BOTH the
    anterior pole and the tuberal segment. The posterior segment does
    not open any new trap: it closes the field.

Functional Mode:
    Same two-mode function as the anterior pole: ORX-dominant
    (arousal/foraging) vs. MCH-dominant (rest/conservation). The
    posterior segment's caudal emphasis includes orexin projections to
    the same brainstem arousal centers (LC, VTA, raphe, basal forebrain)
    that the anterior pole targets, plus projections to the posterior
    thalamic arousal nuclei. See
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py § Functional Mode for the full two-mode description.
    Do not restate the full functional content here; the children point
    to the anterior pole for it.

Hormonal Modulation:
    Same as the anterior pole. See
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py § Hormonal Modulation for the ghrelin/leptin/glucose/
    estrogen/NPY directions. Do not restate.

Memory Interfaces:
    Same as the anterior pole: reads short_term,
    reinforcement_value_based_learning, temporal_sequence_learning,
    emotional_valence; writes no stored content directly (orexin-
    mediated reward modulation is indirect). See
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No sub-container-level fragment. The LHA arousal/feeding fragment
    is emitted by the anterior pole (the pattern exemplar) and is
    augmented by the tuberal and posterior segments at the hypothalamic
    level. AGGREGATION RULE (mandatory): the posterior LHA segment's
    contribution to the arousal/feeding aggregate is aggregated at the
    hypothalamic level; do not emit an independent posterior-LHA
    fragment. See anterior/lateral_area/left/
    anterior_part_of_lateral_nucleus/__init__.py § Model Integration
    for the fragment shape and guardrail (MCH-dominance is a state
    bias, not impairment).

Children (two children — both deltas of the anterior pole):
    - left/    ★ Left posterior LHA segment. Delta of
                 anterior/lateral_area/left/anterior_part_of_lateral_
                 nucleus/. Declares the continuity edge to the anterior
                 pole and the tuberal segment, and adds the
                 posterior-specific reciprocal edges (posterior nucleus,
                 DMH relay, posterior thalamic arousal targets).
    - right/   ★ Right posterior LHA segment. Delta of the left delta.
                 Same shape; right-side edges. No functional asymmetry
                 documented.

Notes:
    - Sub-container file. Short by design. The full LHA content lives
      in the anterior pole (pattern exemplar); the tuberal and posterior
      segments are deltas. Do not duplicate the two-mode framing,
      hormone directions, memory interfaces, or model fragment here.
    - LHA CONTINUUM CLOSURE is the defining content: this container is
      where the field's third segment is declared. The children must
      point to the anterior pole AND the tuberal segment when drafted;
      the three-segment continuity is the trap.
    - Do not create a full leaf for posterior_part_of_lateral_nucleus/.
      It is a delta of the anterior pole, not an independent pattern
      exemplar. The anterior pole is the pattern; this is a segment.
    - The posterior LHA ↔ posterior nucleus relationship is
      complementary (arousal drive vs. sympathetic output), not
      duplicate. Document the cooperation; do not merge.
    - The DMH relay edge (SCN → DMH → posterior LHA) is part of the
      circadian-to-arousal gating; when the DMH file is drafted
      (tuberal/medial_area/left|right/dorsomedial_hypothalamic_
      nucleus/), it will reciprocate the posterior-LHA edge declared
      here.
    - The posterior LHA has no structural-identity trap with the
      anterior or tuberal segments — they are three segments of ONE
      field, and the continuity edges (not a duplicate-structure
      warning) declare the relationship. Do not flag them as
      duplicates in Stage 4.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin, MCH, ghrelin, leptin),
      05_* (monoamines, orexin), 10_* (circadian); memory/stores/
      (short_term, reinforcement_value_based_learning,
      temporal_sequence_learning, emotional_valence); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus/ ↔ anterior/lateral_area/
          left|right/anterior_part_of_lateral_nucleus (SAME LHA field,
          third segment to first segment; continuity edge, not
          duplicate).
        * posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus/ ↔ tuberal/lateral_area/
          left|right/ (SAME LHA field, third segment to second segment;
          continuity edge, not duplicate; tuberal LHA file to be
          drafted).
        * posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus/ ↔ posterior/medial_area/
          left|right/posterior_nucleus (complementary arousal drive vs.
          sympathetic output; distinct nodes).
        * posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus/ ↔ tuberal/medial_area/
          left|right/dorsomedial_hypothalamic_nucleus (circadian →
          DMH → arousal relay; DMH reciprocates when drafted).
    - Connects upward to hypothalamus/posterior/.
"""