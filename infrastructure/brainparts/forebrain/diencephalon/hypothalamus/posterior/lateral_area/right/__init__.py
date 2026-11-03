"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.lateral_area.right
Anatomical Role:
    Right hemisphere of the posterior part of the lateral hypothalamic
    area (LHA). The third and final segment of the LHA orexin/MCH field
    in the right hemisphere: the caudal pole of the same neurochemical
    field whose anterior pole is documented in anterior/lateral_area/
    right/anterior_part_of_lateral_nucleus/ and whose tuberal segment
    is documented in tuberal/lateral_area/right/
    tuberal_part_of_lateral_nucleus/ (when drafted).

    See ../left/__init__.py (this file's delta parent) and
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/
    __init__.py (the pattern exemplar) for the full anatomical
    description, the two-mode framing (ORX-dominant arousal/foraging
    vs. MCH-dominant rest/conservation), and the continuum trap. This
    file is a delta of the left delta; it does not restate that
    content.

    LHA CONTINUUM (critical — three segments of ONE field, not three
    nuclei):
    - Segment 1 (anterior): anterior/lateral_area/right/
      anterior_part_of_lateral_nucleus/ — pattern exemplar.
    - Segment 2 (tuberal): tuberal/lateral_area/right/
      tuberal_part_of_lateral_nucleus/ — to be drafted.
    - Segment 3 (posterior, THIS FILE): caudal pole; closes the field.
    Stage 4 audit must treat the three segments as ONE neurochemical
    field split by the tree's rostrocaudal divisions; do NOT flag them
    as duplicates. Do not merge the nodes; document the continuity
    explicitly. Continuity edge, not structural-identity warning.

Functional Mode:
    Same two-mode function as ../left/ and the anterior pole:
    ORX-dominant (arousal/foraging) vs. MCH-dominant
    (rest/conservation). The posterior segment's caudal emphasis
    includes orexin projections to the same brainstem arousal centers
    the anterior pole targets, plus projections to the posterior
    thalamic arousal nuclei. No documented functional asymmetry
    between left and right posterior LHA segments. Do not fabricate
    one. See ../left/__init__.py § Functional Mode.

Hormonal Modulation:
    Same as ../left/ and the anterior pole. See
    anterior/lateral_area/right/anterior_part_of_lateral_nucleus/
    __init__.py § Hormonal Modulation for the ghrelin/leptin/glucose/
    estrogen/NPY directions. Do not restate.

Memory Interfaces:
    Same as ../left/ and the anterior pole: reads short_term,
    reinforcement_value_based_learning, temporal_sequence_learning,
    emotional_valence; writes no stored content directly. See the
    anterior pole file § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The LHA arousal/feeding fragment
    is emitted by the anterior pole (the pattern exemplar) and is
    augmented by the tuberal and posterior segments at the
    hypothalamic level. AGGREGATION RULE (mandatory): the right
    posterior LHA segment's contribution aggregates at the
    hypothalamic level; do not emit an independent posterior-LHA
    fragment. See the anterior pole file § Model Integration for the
    fragment shape and the MCH-dominance guardrail (MCH-dominance is a
    state bias, not impairment).

Right-specific reciprocal connections to enforce in Stage 4 (the full
LHA edge list lives in the anterior pole file; this list adds the
right-side posterior-specific edges):

    LHA continuity (the critical edges):
    - ↔ anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (SAME LHA field, segment 3 to segment 1; continuity edge, not
      duplicate; right-side).
    - ↔ tuberal/lateral_area/right/tuberal_part_of_lateral_nucleus
      (SAME LHA field, segment 3 to segment 2; continuity edge, not
      duplicate; right-side; tuberal LHA file to be drafted).

    Posterior-specific (new in this segment):
    - ↔ posterior/medial_area/right/posterior_nucleus (complementary
      arousal drive vs. sympathetic output; distinct nodes; right-side).
    - ← tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus
      (circadian → DMH → posterior LHA arousal relay; the DMH
      reciprocates when drafted; right-side).
    - → thalamus/right/midline_nuclear_group/paraventricular_nucleus
      (posterior thalamic arousal relay; the thalamic PVT is distinct
      from the hypothalamic PVN — do not conflate; the thalamic PVT
      node is documented under thalamus/*/midline_nuclear_group/
      when drafted; right-side).

    Shared with the anterior pole (do not duplicate):
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus,
      midbrain/tegmentum/ventral_tegmental_area,
      midbrain/tegmentum/dorsal_raphe_nucleus,
      telencephalon/.../basal_forebrain — orexin arousal targets; the
      full list is in the anterior pole file. This file's posterior
      segment contributes projections to the same targets but does not
      re-enumerate them.

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - DELTA OF A DELTA: this file is a delta of ../left/, which is
      itself a delta of the anterior pole. Inherits through the
      tuberal segment (to be drafted). Same pattern as ../left/; do
      not draft this as a full leaf.
    - LHA CONTINUUM CLOSURE (both hemispheres): with this file, the
      third and final segment of the LHA field is documented on BOTH
      hemispheres. The trap opened in
      anterior_part_of_lateral_nucleus/left/ (and its right
      counterpart) is now CLOSED on both sides: three segments, one
      field, three continuity edges per hemisphere, no duplicates.
      The only remaining work for the LHA field is the TUBERAL
      segment pair (tuberal/lateral_area/left|right/), which must
      declare its own continuity edges to both the anterior pole and
      this posterior segment when drafted.
    - The thalamic PVT vs. hypothalamic PVN trap is reproduced in
      abbreviated form above because it applies on the right
      identically. The thalamic PVT is a different structure from the
      hypothalamic PVN; the right posterior LHA → right thalamic PVT
      edge is arousal relay, not endocrine.
    - No independent fragment; no two-mode restatement; no hormone
      directions; no memory interfaces (all inherited through
      ../left/ from the anterior pole). Strict delta discipline.
    - The DMH → posterior LHA edge (circadian-to-arousal gating) will
      be reciprocated by the DMH file when drafted
      (tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus/).
    - Midline targets (none in this file's specific edges, but the
      general LHA → arousal targets include midline structures like
      the LC and raphe) are flagged in the anterior pole file with
      "verify"; do not duplicate the flags here.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/posterior/lateral_area/.
"""