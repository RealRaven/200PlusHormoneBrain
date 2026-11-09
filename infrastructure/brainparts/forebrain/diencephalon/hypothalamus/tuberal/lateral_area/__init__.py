"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.lateral_area
Anatomical Role:
    The lateral area of the tuberal hypothalamus. It contains the middle
    segment of the LHA orexin/MCH field: the tuberal segment, between the
    anterior pole (segment 1) and the posterior segment (segment 3). The
    three segments are ONE neurochemical field:
        - Segment 1 (anterior): anterior/lateral_area/left|right/
          anterior_part_of_lateral_nucleus/ (the pattern exemplar).
        - Segment 2 (tuberal, THIS SUB-TREE): tuberal_part_of_lateral_
          nucleus/left|right/ — the middle segment.
        - Segment 3 (posterior): posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus/ (documented).
    The tuberal segment contains the same intermingled orexin/hypocretin
    and MCH populations as the anterior pole, with the same two-mode
    functional structure (ORX-dominant arousal/foraging vs. MCH-dominant
    rest/conservation).

    UNIQUE ROLE — THE MIDDLE SEGMENT: the tuberal segment is the
    CONNECTOR between segments 1 and 3. It must declare continuity to
    BOTH:
        - ↔ anterior pole (segment 1)
        - ↔ posterior segment (segment 3)
    The anterior pole's reciprocity is direct (segment 1 ↔ segment 2).
    The posterior segment's reciprocity is also direct (segment 3 ↔
    segment 2). The tuberal segment is the only segment that declares
    two continuity edges; it is what makes the field a *chain* rather
    than two disconnected ends.

    Anatomically, the tuberal LHA is adjacent to the arcuate nucleus
    and the VMH within the tuberal division, and receives strong
    metabolic input from the arcuate (NPY/AgRP → MCH; leptin/ghrelin
    → ORX). This metabolic input is the reason the tuberal LHA segment
    is the most feeding-relevant of the three segments: the arcuate
    feeding hub projects directly onto it.

    LHA CONTINUUM (critical — three segments of ONE field):
    Stage 4 audit must treat segments 1/2/3 as ONE neurochemical field
    split by the tree's rostrocaudal divisions. Do NOT flag them as
    duplicates. Do not merge the nodes. Continuity edges, not
    structural-identity warnings. The tuberal segment is the middle
    link; the field's chain is complete when both of its continuity
    edges exist.

Functional Mode:
    Same two-mode function as the anterior pole: ORX-dominant
    (arousal/foraging) vs. MCH-dominant (rest/conservation). The
    tuberal segment's distinctive emphasis is FEEDING: the arcuate
    feeding hub projects directly onto it, making it the most
    metabolically driven of the three segments. See
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py § Functional Mode for the full two-mode description.
    Do not restate the full functional content here; the children
    point to the anterior pole for it.

Hormonal Modulation:
    Same as the anterior pole, plus the strongest feeding input of the
    three segments. See anterior/lateral_area/left/
    anterior_part_of_lateral_nucleus/__init__.py § Hormonal Modulation
    for the ghrelin/leptin/glucose/estrogen/NPY directions. The
    tuberal segment's distinctive hormonal context is that the arcuate
    → tuberal LHA projections (NPY/AgRP → MCH; leptin/ghrelin → ORX)
    are the densest of the three segments. Do not restate the full
    direction list.

Memory Interfaces:
    Same as the anterior pole: reads short_term,
    reinforcement_value_based_learning, temporal_sequence_learning,
    emotional_valence; writes no stored content directly. The tuberal
    segment's reinforcement_value_based_learning read is the most
    heavily weighted of the three segments (feeding outcomes are the
    dominant reinforcement signal here). See
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No sub-container-level fragment. The LHA arousal/feeding fragment
    is emitted by the anterior pole (the pattern exemplar) and is
    augmented by the tuberal and posterior segments at the hypothalamic
    level. AGGREGATION RULE (mandatory): the tuberal LHA segment's
    contribution is aggregated at the hypothalamic level; do not emit
    an independent tuberal-LHA fragment. See
    anterior/lateral_area/left/anterior_part_of_lateral_nucleus/
    __init__.py § Model Integration for the fragment shape and the
    MCH-dominance guardrail.

Children (two children — both deltas of the anterior pole):
    - left/    ★ Left tuberal LHA segment. Delta of
                 anterior/lateral_area/left/anterior_part_of_lateral_
                 nucleus/. Declares continuity to BOTH segment 1 and
                 segment 3, and adds the tuberal-specific reciprocal
                 edges (arcuate feeding input; strong metabolic
                 weighting).
    - right/   ★ Right tuberal LHA segment. Delta of the left delta.
                 Same shape; right-side edges. No functional asymmetry
                 documented.

Notes:
    - Sub-container file. Short by design. The full LHA content lives
      in the anterior pole (pattern exemplar); the tuberal and
      posterior segments are deltas. Do not duplicate the two-mode
      framing, hormone directions, memory interfaces, or model
      fragment here.
    - LHA CONTINUUM MIDDLE-LINK: this sub-container is the tree
      location where the field's middle continuity edges are declared
      (segment 2 ↔ segment 1, and segment 2 ↔ segment 3). The children
      reproduce these at the leaf level.
    - Do not create a full leaf for tuberal_part_of_lateral_nucleus/.
      It is a delta of the anterior pole, not an independent pattern
      exemplar. Same discipline as the posterior segment.
    - The arcuate → tuberal LHA edge (arcuate NPY/AgRP → MCH;
      arcuate-adjacent leptin/ghrelin → ORX) is the tuberal segment's
      distinctive metabolic input. The arcuate leaf (in
      tuberal/medial_area/) will reciprocate this edge when drafted.
    - The tuberal LHA segment has no structural-identity trap with the
      anterior or posterior segments — they are three segments of ONE
      field, and the continuity edges (not a duplicate-structure
      warning) declare the relationship. Do not flag them as
      duplicates in Stage 4.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin, MCH, ghrelin, leptin,
      NPY, AgRP), 05_* (monoamines, orexin), 10_* (circadian);
      memory/stores/ (short_term, reinforcement_value_based_learning,
      temporal_sequence_learning, emotional_valence); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus ↔ anterior/lateral_area/left|right/
          anterior_part_of_lateral_nucleus (LHA segment 2 ↔ segment 1;
          continuity edge, not duplicate).
        * tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus ↔ posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus (LHA segment 2 ↔ segment 3;
          continuity edge, not duplicate).
        * tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus ↔ tuberal/medial_area/left|right/arcuate_nucleus
          (arcuate NPY/AgRP → tuberal MCH; arcuate-adjacent
          leptin/ghrelin → tuberal ORX; the tuberal segment's
          distinctive feeding input; the arcuate leaf reciprocates).
        * tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus ↔ tuberal/medial_area/left|right/
          dorsomedial_hypothalamic_nucleus (DMH → tuberal LHA; circadian
          relay to feeding-arousal; the DMH reciprocates when drafted).
    - Connects upward to hypothalamus/tuberal/.
"""