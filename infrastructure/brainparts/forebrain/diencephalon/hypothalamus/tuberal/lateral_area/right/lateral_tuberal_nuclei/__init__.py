"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.lateral_area.right.lateral_tuberal_nuclei
Anatomical Role:
    Right hemisphere of the lateral tuberal nuclei. Same small, sparse,
    poorly characterized collection of cell groups in the right lateral
    tuberal region documented in
    ../../../left/lateral_tuberal_nuclei/. See that file for the full
    anatomical description, the "presumed, not established"
    neuroendocrine-adjacent framing, and the honest documentation of
    the thin literature.

    Reproduced distinctions (apply equally on the right — three adjacent
    structures could be confused):
    - DISTINCT from the LHA orexin/MCH field
      (../../tuberal_part_of_lateral_nucleus/): the LHA segment 2 is
      the well-characterized orexin/MCH population (arousal/feeding);
      the lateral tuberal nuclei are a small, sparse, unrelated cell
      group in the same general lateral tuberal region. Do not merge;
      do not treat the lateral tuberal nuclei as "part of the LHA."
    - DISTINCT from the tuberal nucleus in the tuber cinereum
      (hypothalamus/tuber_cinereum/right/tuberal_nucleus/): the tuberal
      nucleus is in the tuber cinereum (floor); the lateral tuberal
      nuclei are in the lateral tuberal region (subdivision above).
      Adjacent concepts, distinct tree nodes.
    - DISTINCT from the arcuate nucleus
      (../../medial_area/right/arcuate_nucleus/): the arcuate is the
      primary tuberal endocrine and feeding nucleus (TIDA, kisspeptin
      KNDy, GHRH, NPY/AgRP, POMC/CART); the lateral tuberal nuclei are
      a small, poorly characterized neighbor.

Functional Mode:
    Same as ../../../left/lateral_tuberal_nuclei/. Anatomical position
    and cell composition documented as present; presumed
    neuroendocrine-adjacent role (not established); no documented
    activational role; no documented memory interface. Do not invent
    functional roles for the right lateral tuberal nuclei to fill
    space. No documented functional asymmetry between left and right.
    See ../../../left/lateral_tuberal_nuclei/ § Functional Mode.

Hormonal Modulation:
    Same as ../../../left/lateral_tuberal_nuclei/. Thin literature;
    estradiol and metabolic signals are presumed inputs, not
    established. Do not pad with the 12 axes. See
    ../../../left/lateral_tuberal_nuclei/ § Hormonal Modulation.

Memory Interfaces:
    None. Same as ../../../left/lateral_tuberal_nuclei/. No documented
    memory interface. Do not invent one.

Model Integration (Gemma-4-E2B):
    None. Same as ../../../left/lateral_tuberal_nuclei/. No prompt
    fragment; the lateral tuberal nuclei have no state to report. Only
    the LHA arousal/feeding fragment (emitted by the anterior pole)
    represents this region (see ../../../../__init__.py § Model
    Integration and the anterior pole file § Model Integration).

Reciprocal Connections (right-side only; the left-side edges are in
../../../left/lateral_tuberal_nuclei/):
    - ↔ ../tuberal_part_of_lateral_nucleus/ (anatomically adjacent
      within the right lateral tuberal region; the LHA segment 2 is the
      well-characterized orexin/MCH field; the lateral tuberal nuclei
      are a small, unrelated neighbor; do not merge; no documented
      signaling edge beyond adjacency).
    - ↔ ../../medial_area/right/arcuate_nucleus (adjacent tuberal
      endocrine nucleus; the arcuate is primary; the lateral tuberal
      nuclei are supplementary and poorly characterized; no documented
      signaling edge beyond adjacency; right-side; arcuate file to be
      drafted).
    - ↔ ../../../left/lateral_tuberal_nuclei/ (hemisphere counterpart;
      no functional asymmetry assumed).
    No other reciprocal edges are documented for the lateral tuberal
    nuclei. Do not invent them. Add edges only if the literature later
    establishes them.

Notes:
    - Delta file of ../../../left/lateral_tuberal_nuclei/. Not a full
      leaf. Do not duplicate.
    - Tier 2 organ-flavored delta. Short by design (~45 lines). Same
      template as inah_1/right/, inah_2/right/, inah_4/right/, and
      tuberal_nucleus/right/.
    - No structural-identity trap and no naming collision beyond the
      three abbreviated adjacent-structure distinctions reproduced
      above. These are also declared at the parent tuberal/lateral_
      area/ container (to be corrected — see the container note in the
      left leaf) and in the left leaf.
    - The "adjacency, not signaling" discipline applies on the right
      identically: the edges to the LHA segment 2 and to the arcuate
      are adjacency-only; no documented signaling edge. The Stage 4
      audit should not expect a signaling edge between the right
      lateral tuberal nuclei and either neighbor.
    - Do not invent an activational endocrine or memory role for the
      right lateral tuberal nuclei. "Presumed, not established" is the
      correct epistemic stance for this nucleus on both hemispheres.
    - Do not add a prompt fragment. The lateral tuberal nuclei have no
      state to report on the right either.
    - With this file, the lateral tuberal nuclei pair (left leaf +
      right delta) is complete. The remaining work in
      tuberal/lateral_area/ is the two tuberal_part_of_lateral_nucleus/
      deltas (the LHA segment 2 pair), plus the container correction to
      name both children.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../left/lateral_tuberal_nuclei/ § Notes for the full list.
    - Connects upward to hypothalamus/tuberal/lateral_area/right/.
"""