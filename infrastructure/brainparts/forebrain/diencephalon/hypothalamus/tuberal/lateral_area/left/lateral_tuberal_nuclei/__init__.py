"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.lateral_area.left.lateral_tuberal_nuclei
Anatomical Role:
    The left lateral tuberal nuclei. A small, poorly characterized
    collection of cell groups in the left lateral tuberal region of the
    hypothalamus. They are documented as a distinct anatomical entity
    but their functional literature is thin — much thinner than the
    neighboring LHA orexin/MCH field
    (../tuberal_part_of_lateral_nucleus/) or the arcuate nucleus
    (../../medial_area/left/arcuate_nucleus/). The lateral tuberal
    nuclei are small, sparse, and not densely innervated by the major
    hypothalamic circuits; they are documented for tree completeness
    and anatomical precision, not as a functional hub.

    DISTINCTIONS (critical — three adjacent structures could be
    confused):
    - DISTINCT FROM THE LHA OREXIN/MCH FIELD: the lateral tuberal
      nuclei sit in the same general lateral tuberal region as the LHA
      orexin/MCH segment 2 (documented under
      ../tuberal_part_of_lateral_nucleus/), but they are a SEPARATE
      anatomical entity. The LHA field is the orexin/MCH population
      (arousal/feeding); the lateral tuberal nuclei are a small,
      sparse, unrelated cell group. Do not merge; do not treat the
      lateral tuberal nuclei as "part of the LHA."
    - DISTINCT FROM THE TUBERAL NUCLEUS (tuber cinereum): the tuberal
      nucleus (hypothalamus/tuber_cinereum/left/tuberal_nucleus/) is a
      small nucleus in the tuber cinereum (the anatomical floor). The
      lateral tuberal nuclei are a different small collection in the
      lateral tuberal region (the regional subdivision above the
      floor). Adjacent anatomical concepts; distinct tree nodes. Do not
      merge.
    - DISTINCT FROM THE ARCUATE NUCLEUS: the arcuate
      (../../medial_area/left/arcuate_nucleus/) is the primary
      tuberal endocrine and feeding nucleus (TIDA, kisspeptin KNDy,
      GHRH, NPY/AgRP, POMC/CART). The lateral tuberal nuclei are a
      small, poorly characterized neighbor. Do not conflate.

    Do not over-write this file: the lateral tuberal nuclei are small
    and poorly characterized. Document factually, do not invent
    functional roles to fill space. Same discipline as the tuberal
    nucleus in the tuber cinereum, INAH-1/2, and the
    striohypothalamic/ventral preoptic regions.

Functional Mode:
    - Anatomical position and cell composition: small, sparse
      collection of neurons in the lateral tuberal region. Documented
      as present; cell types and connectivity not well characterized.
    - Presumed neuroendocrine-adjacent role: sometimes described as
      lateral tuberal neurosecretory cell groups, but the evidence is
      thin and inconsistent. Document as "presumed, not established."
      Do not claim a specific hormonal output.
    - No documented activational role: unlike the arcuate (feeding,
      kisspeptin KNDy, TIDA) or the LHA orexin/MCH field (arousal/
      feeding), the lateral tuberal nuclei have no established adult
      function. Do not invent one.
    - No documented memory interface: the lateral tuberal nuclei have
      no established episodic, semantic, procedural, or
      reinforcement-learning interface.
    - The nuclei are documented for tree completeness (they sit in the
      lateral tuberal region, adjacent to the LHA field) and for
      anatomical precision (they are a distinct entity from both the
      LHA field and the arcuate); they are not a functional hub.

Hormonal Modulation:
    - Thin literature: no well-established hormonal modulators.
      Estradiol and metabolic signals have been reported as
      "presumed" inputs (lateral tuberal endocrine context), but the
      evidence is not established.
    - Direction summary: estradiol and metabolic signals are presumed
      modulators; do not list additional modulators beyond what the
      literature establishes, and do not claim a specific hormonal
      output.
    - The lateral tuberal nuclei are NOT a significant endocrine
      source or target. Do not pad the section with the 12 axes.

Memory Interfaces:
    None. The lateral tuberal nuclei have no documented memory
    interface. Do not invent one.

Model Integration (Gemma-4-E2B):
    None. The lateral tuberal nuclei do not emit a prompt fragment.
    They are small, poorly characterized cell groups; they have no
    state to report to the model. The parent lateral_area sub-container
    and the LHA segment leaves specify that only the LHA arousal/
    feeding fragment (emitted by the anterior pole) represents this
    region; the lateral tuberal nuclei do not.

Reciprocal Connections:
    - ↔ ../tuberal_part_of_lateral_nucleus/ (anatomically adjacent
      within the left lateral tuberal region; the LHA segment 2 is the
      well-characterized orexin/MCH field; the lateral tuberal nuclei
      are a small, unrelated neighbor; do not merge; no documented
      signaling edge beyond adjacency).
    - ↔ ../../medial_area/left/arcuate_nucleus (adjacent tuberal
      endocrine nucleus; the arcuate is primary; the lateral tuberal
      nuclei are supplementary and poorly characterized; no documented
      signaling edge beyond adjacency; arcuate file to be drafted).
    No other reciprocal edges are documented for the lateral tuberal
    nuclei. Do not invent them. Add edges only if the literature later
    establishes them.

Notes:
    - Tier 2 organ-flavored leaf. Short by design (~45 lines). The
      lateral tuberal nuclei have thin functional literature; do not
      over-write them. Same template as the tuberal nucleus in the
      tuber cinereum, inah_1/, and inah_2/.
    - No structural-identity trap and no naming collision beyond the
      three adjacent-structure distinctions (LHA field vs. lateral
      tuberal nuclei; tuberal nucleus vs. lateral tuberal nuclei;
      arcuate vs. lateral tuberal nuclei). Reproduced in abbreviated
      form above.
    - DISTINCT FROM THE LHA FIELD: the lateral tuberal nuclei share
      the lateral tuberal region with the LHA orexin/MCH segment 2,
      but they are a separate anatomical entity. This is the most
      likely conflation (both are "in the lateral tuberal area"); the
      distinction is stated explicitly.
    - DISTINCT FROM THE TUBERAL NUCLEUS (tuber cinereum): both are
      "tuberal nuclei," but the tuberal nucleus is in the tuber
      cinereum (floor) and the lateral tuberal nuclei are in the
      lateral tuberal region (subdivision above). Adjacent concepts,
      distinct tree nodes.
    - DISTINCT FROM THE ARCUATE: the arcuate is the primary tuberal
      endocrine nucleus; the lateral tuberal nuclei are a small,
      poorly characterized neighbor.
    - Do not invent an activational endocrine or memory role. The
      literature does not support one. "Presumed, not established" is
      the correct epistemic stance.
    - Do not add a prompt fragment. The lateral tuberal nuclei have no
      state to report.
    - The LHA segment 2 leaves (tuberal_part_of_lateral_nucleus/) do
      NOT reference the lateral tuberal nuclei, and vice versa: the
      LHA field and the lateral tuberal nuclei are documented as
      separate entities without a signaling edge between them. The
      "↔ adjacent" edge above is adjacency, not signaling; the Stage 4
      audit should not expect a signaling edge.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol; presumed input), 03_*
      (HPT, metabolic; presumed input); memory/stores/ is not
      applicable; gateway/.
    - Connects upward to hypothalamus/tuberal/lateral_area/left/.
"""