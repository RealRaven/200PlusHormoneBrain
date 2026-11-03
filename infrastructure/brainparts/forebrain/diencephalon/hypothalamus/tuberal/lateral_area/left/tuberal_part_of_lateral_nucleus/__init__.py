"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.lateral_area.left.tuberal_part_of_lateral_nucleus
Anatomical Role:
    Left tuberal part of the lateral hypothalamic area (LHA). The
    MIDDLE segment of the left LHA orexin/MCH field: segment 2 of the
    three-segment continuum whose segment 1 is
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    (pattern exemplar) and whose segment 3 is
    posterior/lateral_area/left/posterior_part_of_lateral_nucleus/.

    See ../../../left/__init__.py (the left lateral-area container) for
    the middle-segment/connector framing, the distinctive arcuate
    feeding input, and the two-mode context; see
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py for the full anatomical description, the two-mode
    framing, the intermingled orexin/MCH populations, the hormone
    directions, the memory interfaces, and the MCH-dominance guardrail.
    This file is a delta of a delta; it does not restate that content.

    UNIQUE ROLE — MIDDLE SEGMENT / CONNECTOR (the defining feature):
    Unlike segment 1 (start) and segment 3 (end), segment 2 is the
    MIDDLE LINK of the field. It declares continuity to BOTH neighbors:
        - ↔ segment 1 (anterior pole) — chain start.
        - ↔ segment 3 (posterior segment) — chain end.
    The anterior pole has already declared its side of segment 1 ↔
    segment 2 (in anterior/lateral_area/left/
    anterior_part_of_lateral_nucleus/). The posterior segment has
    already declared its side of segment 2 ↔ segment 3 (in
    posterior/lateral_area/left/posterior_part_of_lateral_nucleus/).
    THIS FILE closes the middle: it declares segment 2's side of both
    continuity edges.

    LHA CONTINUUM (critical — three segments of ONE field):
    Segment 1 (anterior) → Segment 2 (THIS FILE) → Segment 3
    (posterior). Stage 4 audit must treat the three segments as ONE
    neurochemical field; do NOT flag them as duplicates. Continuity
    edges, not structural-identity warnings.

    DISTINCTIVE INPUT — ARCUATE FEEDING PROJECTIONS (the tuberal
    segment's signature): the tuberal segment is the most metabolically
    driven of the three LHA segments, because the arcuate feeding hub
    (tuberal/medial_area/left/arcuate_nucleus/) projects DIRECTLY onto
    it:
        - Arcuate NPY/AgRP neurons → tuberal MCH neurons (hunger →
          rest/conservation mode).
        - Arcuate-adjacent leptin/ghrelin signals → tuberal ORX
          neurons (satiety/hunger → arousal/foraging mode).
    This direct feeding input is densest at the tuberal segment (the
    arcuate is in the same division). Segments 1 and 3 receive
    feeding-driven modulation more indirectly. This is the tuberal
    segment's distinctive metabolic weighting.

Functional Mode:
    Same two-mode function as the anterior pole (ORX-dominant
    arousal/foraging vs. MCH-dominant rest/conservation), with the
    tuberal segment's distinctive weighting toward FEEDING. The
    arcuate → tuberal LHA projections make feeding outcomes the
    dominant reinforcement signal at this segment. See the anterior
    pole file § Functional Mode for the full two-mode description. No
    documented functional asymmetry between left and right tuberal LHA
    segments. Do not fabricate one.

Hormonal Modulation:
    Same as the anterior pole, with the arcuate feeding input added as
    the tuberal segment's distinctive feature. See the anterior pole
    file § Hormonal Modulation for the full ghrelin/leptin/glucose/
    estrogen/NPY direction list. The tuberal segment's distinctive
    hormonal context:
        - Ghrelin (via arcuate-adjacent circuit) ↑ ORX and ↑ MCH
          (hunger drives both modes depending on context).
        - Leptin (via arcuate-adjacent circuit) ↓ ORX and ↓ MCH
          (satiety suppresses both feeding modes).
        - NPY/AgRP (arcuate) → MCH (directed projection; the densest
          of the three segments).

Memory Interfaces:
    Same as the anterior pole: reads short_term,
    reinforcement_value_based_learning, temporal_sequence_learning,
    emotional_valence; writes no stored content directly. The
    reinforcement_value_based_learning read is the most heavily
    weighted of the three segments (feeding outcomes are the dominant
    reinforcement signal here). See the anterior pole file § Memory
    Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The LHA arousal/feeding fragment
    is emitted by the anterior pole (pattern exemplar) and augmented
    by the tuberal and posterior segments at the hypothalamic level.
    AGGREGATION RULE (mandatory): the tuberal LHA segment's
    contribution aggregates at the hypothalamic level; do not emit an
    independent tuberal-LHA fragment. See the anterior pole file
    § Model Integration for the fragment shape and the MCH-dominance
    guardrail.

Reciprocal Connections (left-side; the right side is in ../right/;
the full shared LHA edge list is in the anterior pole file; this
list adds the tuberal-specific edges):

    LHA continuity (the critical edges — THIS SEGMENT'S DEFINING
    FEATURE):
    - ↔ anterior/lateral_area/left/anterior_part_of_lateral_nucleus
      (SAME LHA field, segment 2 to segment 1; continuity edge, not
      duplicate; the anterior pole has already declared its side).
    - ↔ posterior/lateral_area/left/posterior_part_of_lateral_nucleus
      (SAME LHA field, segment 2 to segment 3; continuity edge, not
      duplicate; the posterior segment has already declared its side).

    Tuberal-specific (new in this segment):
    - ← tuberal/medial_area/left/arcuate_nucleus (arcuate NPY/AgRP →
      tuberal MCH; arcuate-adjacent leptin/ghrelin → tuberal ORX; the
      tuberal segment's distinctive direct feeding input; the arcuate
      leaf reciprocates when drafted).
    - ← tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus
      (DMH → tuberal LHA; circadian relay to feeding-arousal; the DMH
      reciprocates when drafted).

    Shared with the anterior pole (do not duplicate):
    - → LC, VTA, raphe, basal forebrain (orexin arousal targets) — full
      list in the anterior pole file.

    Adjacency (not signaling):
    - ↔ ../lateral_tuberal_nuclei/ (anatomically adjacent within the
      left lateral tuberal region; the LHA segment 2 is the
      well-characterized orexin/MCH field; the lateral tuberal nuclei
      are a small, unrelated neighbor; do not merge; no documented
      signaling edge beyond adjacency).

Notes:
    - DELTA OF A DELTA, middle segment, left side. The connector
      segment's defining content is the TWO continuity edges. Do not
      draft as a full leaf; do not restate the two-mode framing,
      hormone directions, memory interfaces, or model fragment.
    - LHA CONTINUUM MIDDLE-LINK CLOSURE ON THE LEFT: with this file,
      the left hemisphere's LHA chain is fully connected:
      segment 1 ↔ segment 2 ↔ segment 3. Both continuity edges exist
      on the left side. The right delta (../right/) closes the
      middle-link on the right; with that file, the LHA continuum is
      fully closed on both hemispheres.
    - The arcuate → tuberal LHA edge is the tuberal segment's
      distinctive input (direct feeding projection). The arcuate leaf
      will reciprocate when drafted
      (tuberal/medial_area/left/arcuate_nucleus/).
    - The DMH → tuberal LHA edge is the circadian-to-feeding-arousal
      relay; the DMH reciprocates when drafted
      (tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus/).
    - The lateral_tuberal_nuclei adjacency edge is recorded as
      ADJACENCY (not signaling): the two structures share the lateral
      tuberal region but are anatomically and functionally distinct.
      The Stage 4 audit should not expect a signaling edge between
      them.
    - The tuberal segment has no structural-identity trap with the
      anterior or posterior segments; continuity edges declare the
      field relationship. Do not flag as duplicates in Stage 4.
    - No independent fragment; no two-mode restatement; no hormone
      directions; no memory interfaces (all inherited from the anterior
      pole). Strict delta discipline.
    - Vocabulary used above is defined in Stage 0 files; see the
      anterior pole file § Notes for the full list.
    - Connects upward to hypothalamus/tuberal/lateral_area/left/.
"""