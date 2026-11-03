"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuber_cinereum.right.tuberal_nucleus
Anatomical Role:
    Right hemisphere of the tuberal nucleus. Same small, poorly
    characterized collection of neurons in the right lateral tuberal
    region documented in ../../left/tuberal_nucleus/. See that file for
    the full anatomical description, the "presumed, not established"
    endocrine-adjacent framing, and the honest documentation of the
    thin literature.

    Reproduced distinctions (apply equally on the right):
    - DISTINCT from the right TMN (documented under
      ../tuberomammillary_nucleus/): unrelated neighbors within the same
      tuber cinereum. Do not conflate; do not treat them as a pair of
      similar structures.
    - DISTINCT from the tuberal division's right arcuate, VMH, and DMH:
      the tuberal nucleus is in the tuber cinereum (floor), not in the
      tuberal division (regional subdivision above it). Adjacent
      concepts, distinct tree nodes.
    - DISTINCT from the right arcuate nucleus (tuberal/medial_area/
      right/arcuate_nucleus/; when drafted): the arcuate is the primary
      tuberal endocrine nucleus; the tuberal nucleus is a supplementary,
      poorly characterized neighbor.

Functional Mode:
    Same as ../../left/tuberal_nucleus/. Anatomical position and cell
    composition documented as present; presumed endocrine-adjacent role
    (not established); no documented activational role; no documented
    memory interface. Do not invent functional roles for the right
    tuberal nucleus to fill space. No documented functional asymmetry
    between left and right. See ../../left/tuberal_nucleus/ § Functional
    Mode.

Hormonal Modulation:
    Same as ../../left/tuberal_nucleus/. Thin literature; estradiol and
    metabolic signals are presumed inputs, not established. Do not pad
    with the 12 axes. See ../../left/tuberal_nucleus/ § Hormonal
    Modulation.

Memory Interfaces:
    None. Same as ../../left/tuberal_nucleus/. No documented memory
    interface. Do not invent one.

Model Integration (Gemma-4-E2B):
    None. Same as ../../left/tuberal_nucleus/. No prompt fragment; the
    tuberal nucleus has no state to report. Only the TMN emits a
    wake/arousal fragment from this subtree (see
    ../../../__init__.py § Model Integration).

Reciprocal Connections (right-side only; the left-side edges are in
../../left/tuberal_nucleus/):
    - ↔ ../tuberomammillary_nucleus/ (anatomically adjacent within the
      right tuber cinereum; functionally unrelated; do not merge).
    - ↔ tuberal/medial_area/right/arcuate_nucleus (adjacent tuberal
      endocrine populations; continuity edge, not duplicate-structure
      warning; the arcuate is primary, the tuberal nucleus is
      supplementary; tuberal arcuate file to be drafted; right-side).
    - ↔ hypothalamus/median_eminence (anatomically adjacent
      tuberoinfundibular interface; midline — verify; the presumed
      endocrine-adjacent role is via this adjacency; no documented
      signaling edge beyond adjacency).
    - ↔ ../../left/tuberal_nucleus/ (hemisphere counterpart; no
      functional asymmetry assumed).

Notes:
    - Delta file of ../../left/tuberal_nucleus/. Not a full leaf. Do not
      duplicate.
    - Tier 2 organ-flavored delta. Short by design (~45 lines). Same
      template as the right deltas for inah_1, inah_2, and inah_4.
    - No structural-identity trap and no naming collision beyond the
      three abbreviated traps reproduced above (which are also declared
      at the parent tuber_cinereum container and the right-hemisphere
      container).
    - Do not invent an activational endocrine or memory role for the
      right tuberal nucleus. "Presumed, not established" is the correct
      epistemic stance for this nucleus on both hemispheres.
    - Do not add a prompt fragment. The tuberal nucleus has no state to
      report on the right either.
    - The right tuberal nucleus pair (left leaf + right delta) is now
      complete after this file. Only the TMN pair
      (tuberomammillary_nucleus/left|right/) remains in the entire
      tuber_cinereum subtree.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/tuberal_nucleus/ § Notes for the full list.
    - Connects upward to hypothalamus/tuber_cinereum/right/.
"""