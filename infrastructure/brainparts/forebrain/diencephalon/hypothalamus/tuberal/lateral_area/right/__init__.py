"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.lateral_area.right
Anatomical Role:
    Right hemisphere of the tuberal part of the lateral hypothalamic
    area (LHA). The MIDDLE segment of the right LHA orexin/MCH field:
    segment 2 of the three-segment continuum whose segment 1 is
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/
    (pattern exemplar) and whose segment 3 is
    posterior/lateral_area/right/posterior_part_of_lateral_nucleus/.

    See ../left/__init__.py (this file's delta parent) and
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/
    __init__.py (the pattern exemplar) for the full anatomical
    description, the two-mode framing, the hormone directions, the
    memory interfaces, and the MCH-dominance guardrail. This file is a
    delta of a delta; it does not restate that content.

    UNIQUE ROLE — MIDDLE SEGMENT / CONNECTOR (reproduced):
    Unlike segment 1 (start) and segment 3 (end), segment 2 is the
    MIDDLE LINK of the field. It must declare continuity to BOTH:
        - ↔ anterior pole (segment 1) — the start of the chain.
        - ↔ posterior segment (segment 3) — the end of the chain.
    The posterior segment has already declared its side of segment 2 ↔
    segment 3 (in posterior/lateral_area/right/
    posterior_part_of_lateral_nucleus/). The anterior pole has already
    declared its side of segment 1 ↔ segment 2 (in
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/).
    This file closes the middle on the right.

    DISTINCTIVE INPUT — ARCUATE FEEDING PROJECTIONS (reproduced):
    The tuberal segment is the most metabolically driven of the three
    LHA segments; the right arcuate feeding hub
    (tuberal/medial_area/right/arcuate_nucleus/) projects DIRECTLY
    onto it:
        - Arcuate NPY/AgRP neurons → tuberal MCH neurons (hunger →
          rest/conservation).
        - Arcuate-adjacent leptin/ghrelin signals → tuberal ORX
          neurons (satiety/hunger → arousal/foraging).

    LHA CONTINUUM (critical — three segments of ONE field):
    Segment 1 (anterior) → Segment 2 (THIS FILE) → Segment 3
    (posterior). Stage 4 audit must treat the three segments as ONE
    neurochemical field; do NOT flag them as duplicates. Continuity
    edges, not structural-identity warnings.

Functional Mode:
    Same two-mode function as ../left/ and the anterior pole
    (ORX-dominant arousal/foraging vs. MCH-dominant rest/conservation),
    with the tuberal segment's distinctive weighting toward FEEDING
    (arcuate → tuberal LHA projections). No documented functional
    asymmetry between left and right tuberal LHA segments. Do not
    fabricate one. See ../left/__init__.py § Functional Mode.

Hormonal Modulation:
    Same as ../left/. Ghrelin ↑ ORX and ↑ MCH (hunger drives both
    modes depending on context); leptin ↓ ORX and ↓ MCH (satiety
    suppresses); NPY/AgRP (arcuate) → MCH (directed projection; densest
    of the three segments). See ../left/__init__.py § Hormonal
    Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term,
    reinforcement_value_based_learning (most heavily weighted of the
    three segments — feeding outcomes dominant), temporal_sequence_
    learning, emotional_valence; writes no stored content directly.
    See ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The LHA arousal/feeding fragment is
    emitted by the anterior pole (pattern exemplar) and augmented by
    the tuberal and posterior segments at the hypothalamic level.
    AGGREGATION RULE: aggregate the right tuberal LHA contribution at
    the hypothalamic level; do not emit an independent tuberal-LHA
    fragment. See the anterior pole file § Model Integration for the
    MCH-dominance guardrail.

Right-specific reciprocal connections to enforce in Stage 4:

    LHA continuity (the critical edges — THIS SEGMENT'S DEFINING
    FEATURE):
    - ↔ anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (SAME LHA field, segment 2 to segment 1; continuity edge, not
      duplicate; right-side).
    - ↔ posterior/lateral_area/right/posterior_part_of_lateral_nucleus
      (SAME LHA field, segment 2 to segment 3; continuity edge, not
      duplicate; right-side).

    Tuberal-specific (new in this segment):
    - ← tuberal/medial_area/right/arcuate_nucleus (arcuate NPY/AgRP →
      tuberal MCH; arcuate-adjacent leptin/ghrelin → tuberal ORX; the
      tuberal segment's distinctive direct feeding input; the arcuate
      leaf reciprocates when drafted; right-side).
    - ← tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus
      (DMH → tuberal LHA; circadian relay to feeding-arousal; the DMH
      reciprocates when drafted; right-side).

    Shared with the anterior pole (do not duplicate):
    - → LC, VTA, raphe, basal forebrain (orexin arousal targets) — full
      list in the anterior pole file.

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - DELTA OF A DELTA, middle segment, right side. Mirror of ../left/.
      Do not duplicate the two-mode framing, hormone directions,
      memory interfaces, or model fragment.
    - LHA CONTINUUM FULLY CLOSED — BOTH HEMISPHERES NOW COMPLETE: with
      this file, the middle segment of the LHA field is declared on
      both hemispheres, and its continuity edges to both segments 1
      and 3 exist on both sides. The three-segment LHA chain is now
      FULLY CONNECTED across the entire tree:
        * Left: segment 1 ↔ segment 2 ↔ segment 3.
        * Right: segment 1 ↔ segment 2 ↔ segment 3.
      The trap that was opened in anterior_part_of_lateral_nucleus/
      left/ (and its right counterpart) is now CLOSED on both sides,
      across all three segments. Stage 4 audit will see six continuity
      edges (three per hemisphere) forming one continuous field.
    - The arcuate → tuberal LHA edge is the tuberal segment's
      distinctive input (direct feeding projection). The right arcuate
      leaf reciprocates when drafted
      (tuberal/medial_area/right/arcuate_nucleus/).
    - The DMH → tuberal LHA edge is the circadian-to-feeding-arousal
      relay; the right DMH reciprocates when drafted
      (tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus/).
    - No independent fragment; no two-mode restatement; no hormone
      directions; no memory interfaces (all inherited through ../left/
      from the anterior pole). Strict delta discipline.
    - The tuberal segment has no structural-identity trap with the
      anterior or posterior segments; the continuity edges declare the
      field relationship. Do not flag them as duplicates in Stage 4.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/tuberal/lateral_area/.
""""""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.lateral_area.right
Anatomical Role:
    Right hemisphere of the tuberal part of the lateral hypothalamic
    area (LHA). The MIDDLE segment of the right LHA orexin/MCH field:
    segment 2 of the three-segment continuum whose segment 1 is
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/
    (pattern exemplar) and whose segment 3 is
    posterior/lateral_area/right/posterior_part_of_lateral_nucleus/.

    See ../left/__init__.py (this file's delta parent) and
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/
    __init__.py (the pattern exemplar) for the full anatomical
    description, the two-mode framing, the hormone directions, the
    memory interfaces, and the MCH-dominance guardrail. This file is a
    delta of a delta; it does not restate that content.

    UNIQUE ROLE — MIDDLE SEGMENT / CONNECTOR (reproduced):
    Unlike segment 1 (start) and segment 3 (end), segment 2 is the
    MIDDLE LINK of the field. It must declare continuity to BOTH:
        - ↔ anterior pole (segment 1) — the start of the chain.
        - ↔ posterior segment (segment 3) — the end of the chain.
    The posterior segment has already declared its side of segment 2 ↔
    segment 3 (in posterior/lateral_area/right/
    posterior_part_of_lateral_nucleus/). The anterior pole has already
    declared its side of segment 1 ↔ segment 2 (in
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/).
    This file closes the middle on the right.

    DISTINCTIVE INPUT — ARCUATE FEEDING PROJECTIONS (reproduced):
    The tuberal segment is the most metabolically driven of the three
    LHA segments; the right arcuate feeding hub
    (tuberal/medial_area/right/arcuate_nucleus/) projects DIRECTLY
    onto it:
        - Arcuate NPY/AgRP neurons → tuberal MCH neurons (hunger →
          rest/conservation).
        - Arcuate-adjacent leptin/ghrelin signals → tuberal ORX
          neurons (satiety/hunger → arousal/foraging).

    LHA CONTINUUM (critical — three segments of ONE field):
    Segment 1 (anterior) → Segment 2 (THIS FILE) → Segment 3
    (posterior). Stage 4 audit must treat the three segments as ONE
    neurochemical field; do NOT flag them as duplicates. Continuity
    edges, not structural-identity warnings.

Functional Mode:
    Same two-mode function as ../left/ and the anterior pole
    (ORX-dominant arousal/foraging vs. MCH-dominant rest/conservation),
    with the tuberal segment's distinctive weighting toward FEEDING
    (arcuate → tuberal LHA projections). No documented functional
    asymmetry between left and right tuberal LHA segments. Do not
    fabricate one. See ../left/__init__.py § Functional Mode.

Hormonal Modulation:
    Same as ../left/. Ghrelin ↑ ORX and ↑ MCH (hunger drives both
    modes depending on context); leptin ↓ ORX and ↓ MCH (satiety
    suppresses); NPY/AgRP (arcuate) → MCH (directed projection; densest
    of the three segments). See ../left/__init__.py § Hormonal
    Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term,
    reinforcement_value_based_learning (most heavily weighted of the
    three segments — feeding outcomes dominant), temporal_sequence_
    learning, emotional_valence; writes no stored content directly.
    See ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The LHA arousal/feeding fragment is
    emitted by the anterior pole (pattern exemplar) and augmented by
    the tuberal and posterior segments at the hypothalamic level.
    AGGREGATION RULE: aggregate the right tuberal LHA contribution at
    the hypothalamic level; do not emit an independent tuberal-LHA
    fragment. See the anterior pole file § Model Integration for the
    MCH-dominance guardrail.

Right-specific reciprocal connections to enforce in Stage 4:

    LHA continuity (the critical edges — THIS SEGMENT'S DEFINING
    FEATURE):
    - ↔ anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (SAME LHA field, segment 2 to segment 1; continuity edge, not
      duplicate; right-side).
    - ↔ posterior/lateral_area/right/posterior_part_of_lateral_nucleus
      (SAME LHA field, segment 2 to segment 3; continuity edge, not
      duplicate; right-side).

    Tuberal-specific (new in this segment):
    - ← tuberal/medial_area/right/arcuate_nucleus (arcuate NPY/AgRP →
      tuberal MCH; arcuate-adjacent leptin/ghrelin → tuberal ORX; the
      tuberal segment's distinctive direct feeding input; the arcuate
      leaf reciprocates when drafted; right-side).
    - ← tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus
      (DMH → tuberal LHA; circadian relay to feeding-arousal; the DMH
      reciprocates when drafted; right-side).

    Shared with the anterior pole (do not duplicate):
    - → LC, VTA, raphe, basal forebrain (orexin arousal targets) — full
      list in the anterior pole file.

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - DELTA OF A DELTA, middle segment, right side. Mirror of ../left/.
      Do not duplicate the two-mode framing, hormone directions,
      memory interfaces, or model fragment.
    - LHA CONTINUUM FULLY CLOSED — BOTH HEMISPHERES NOW COMPLETE: with
      this file, the middle segment of the LHA field is declared on
      both hemispheres, and its continuity edges to both segments 1
      and 3 exist on both sides. The three-segment LHA chain is now
      FULLY CONNECTED across the entire tree:
        * Left: segment 1 ↔ segment 2 ↔ segment 3.
        * Right: segment 1 ↔ segment 2 ↔ segment 3.
      The trap that was opened in anterior_part_of_lateral_nucleus/
      left/ (and its right counterpart) is now CLOSED on both sides,
      across all three segments. Stage 4 audit will see six continuity
      edges (three per hemisphere) forming one continuous field.
    - The arcuate → tuberal LHA edge is the tuberal segment's
      distinctive input (direct feeding projection). The right arcuate
      leaf reciprocates when drafted
      (tuberal/medial_area/right/arcuate_nucleus/).
    - The DMH → tuberal LHA edge is the circadian-to-feeding-arousal
      relay; the right DMH reciprocates when drafted
      (tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus/).
    - No independent fragment; no two-mode restatement; no hormone
      directions; no memory interfaces (all inherited through ../left/
      from the anterior pole). Strict delta discipline.
    - The tuberal segment has no structural-identity trap with the
      anterior or posterior segments; the continuity edges declare the
      field relationship. Do not flag them as duplicates in Stage 4.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/tuberal/lateral_area/.
"""