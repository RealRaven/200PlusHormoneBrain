"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuber_cinereum.right
Anatomical Role:
    Right hemisphere of the tuber cinereum. Contains the same two nuclei
    as ../left/, mirrored to the right hemisphere:
        - tuberomammillary_nucleus/   ★ Tier 1 hub leaf. Right TMN;
                                        histaminergic wake-promoting
                                        nucleus.
        - tuberal_nucleus/            Tier 2 organ-flavored leaf. Small;
                                        poorly characterized.
    See ../left/__init__.py for the full hemisphere-container framing
    and ../../__init__.py for the full tuber cinereum description, the
    three naming traps, and the "tuber cinereum vs. tuberal division"
    trap. This file is a hemisphere-container delta; it does not
    re-describe the nuclei.

    Reproduced asymmetric child discipline (applies on the right, same
    as on the left): TMN is Tier 1 hub; tuberal nucleus is Tier 2 leaf.
    Do not force the same template onto both.

    Reproduced critical traps (all apply equally on the right):
    - TUBER CINEREUM vs. TUBERAL DIVISION: this node and
      hypothalamus/tuberal/ are ADJACENT BUT DISTINCT tree nodes. Do
      not merge.
    - TMN vs. MAMMILLARY BODIES: "tuberomammillary" contains
      "mammillary"; the TMN (histaminergic wake hub) is functionally
      unrelated to the mammillary bodies (Papez circuit memory relay).
      Do not merge.
    - TMN vs. TUBERAL NUCLEUS: intra-container; two distinct nuclei
      with unrelated functions. Do not treat as a pair of similar
      structures.

Functional Mode:
    Same as ../left/ and the parent container. See ../../__init__.py
    § Functional Mode and the two right-side leaf files
    (./tuberomammillary_nucleus/ and ./tuberal_nucleus/). No documented
    functional asymmetry between left and right tuber cinereum. Do not
    fabricate one.

Hormonal Modulation:
    Same as ../left/. See ../../__init__.py § Hormonal Modulation for
    the TMN and tuberal nucleus inputs.

Memory Interfaces:
    Same as ../left/. See ../../__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No hemisphere-level prompt fragment. The TMN's wake/arousal
    fragment is emitted by ./tuberomammillary_nucleus/ (the right full
    leaf) and represents the bilateral TMN; the tuberal nucleus emits
    no fragment. See ../../__init__.py § Model Integration for the
    fragment spec, the AGGREGATION RULE (three-way aggregation with
    LPO sleep and LHA orexin/MCH fragments), and the guardrail ("do
    not treat high wake state as a cognitive achievement or low wake
    state as impairment"). Those apply identically on the right.

Children (asymmetric — deltas of the left nuclei):
    - tuberomammillary_nucleus/   ★ Delta of ../left/
                                    tuberomammillary_nucleus/. Right
                                    hemisphere; Tier 1 hub.
    - tuberal_nucleus/            Delta of ../left/tuberal_nucleus/.
                                    Right hemisphere; Tier 2 leaf.

Right-specific reciprocal connections to enforce in Stage 4 (do not
duplicate the left-side edges in ../left/):
    - tuberomammillary_nucleus/ ↔
      lateral_area/right/preoptic_area/lateral_preoptic_nucleus (LPO →
      TMN; inhibitory; sleep promotion; PATH CORRECTION: the right LPO
      leaf currently points at "hindbrain/.../tuberomammillary_nucleus";
      the correct path is hypothalamus/tuber_cinereum/right/
      tuberomammillary_nucleus/ — Stage 4 should correct the right LPO
      path; functional edge is correct).
    - tuberomammillary_nucleus/ ↔
      anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (orexin → TMN; excitatory; wake promotion; right-side).
    - tuberomammillary_nucleus/ →
      telencephalon/cerebral_hemispheres/right/subcortical/
      basal_forebrain (arousal; right-side).
    - tuberomammillary_nucleus/ → cortex (diffuse histaminergic arousal
      projection; right hemisphere).
    - tuberomammillary_nucleus/ →
      thalamus/right/midline_nuclear_group and
      thalamus/right/medial_nuclear_group/intralaminar_nuclear_group
      (arousal relay; midline — verify).
    - tuberomammillary_nucleus/ ↔
      midbrain/tegmentum/dorsal_raphe_nucleus,
      hindbrain/metencephalon/pons/tegmentum/locus_coeruleus,
      midbrain/tegmentum/laterodorsal_tegmental_nucleus,
      midbrain/tegmentum/pedunculopontine_nucleus (mutual arousal
      network; midline — verify).
    - tuberomammillary_nucleus/ ←
      anterior/medial_area/right/suprachiasmatic_nucleus (SCN → TMN;
      circadian arousal gating; SCN is midline-adjacent — verify).
    - tuberal_nucleus/ ↔ tuberal/medial_area/right/arcuate_nucleus
      (adjacent tuberal endocrine regulation; continuity edge;
      tuberal arcuate file to be drafted).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Hemisphere-container delta of ../left/. Inherits everything
      structural and functional from ../left/ and ../../. Do not
      duplicate the parent or left-container content.
    - The asymmetric child discipline is reproduced above (TMN Tier 1;
      tuberal nucleus Tier 2). Same as ../left/.
    - All three naming traps are reproduced in abbreviated form above;
      the full text is at ../../__init__.py. A contributor entering at
      the right-hemisphere container must see them.
    - The LPO path correction is restated above for the right side
      because the right TMN edge has the same placeholder path issue.
      Stage 4 should correct both LPO leaves (left and right).
    - No hemisphere-level fragment: TMN's fragment is in the TMN leaf;
      tuberal nucleus emits none. Same as ../left/.
    - The TMN ↔ LPO and TMN ↔ orexin edges form the right-side arm of
      the hypothalamic sleep-wake switch. The three-fragment aggregation
      (LPO/TMN/orexin) applies on the right too; the fragments are
      bilateral, aggregated at the hypothalamic level.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/tuber_cinereum/.
"""