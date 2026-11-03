"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuber_cinereum.left
Anatomical Role:
    Left hemisphere of the tuber cinereum. Contains two nuclei, both in
    the left hemisphere:
        - tuberomammillary_nucleus/   ★ Tier 1 hub leaf. The brain's
                                        sole source of neuronal
                                        histamine; the principal
                                        wake-promoting nucleus of the
                                        posterior hypothalamus; one of
                                        the five ascending arousal
                                        nuclei; the inhibitory target
                                        of the LPO (sleep promotion)
                                        and the excitatory target of
                                        LHA orexin (wake promotion).
        - tuberal_nucleus/            Tier 2 organ-flavored leaf. A
                                        small collection of neurons in
                                        the lateral tuberal region;
                                        functionally poorly
                                        characterized; the literature
                                        is thin.
    See ../../__init__.py (the parent tuber_cinereum container) for the
    full anatomical description of the tuber cinereum, the TMN-vs-
    mammillary and TMN-vs-tuberal-nucleus traps, and the "tuber cinereum
    vs. tuberal division" trap. This file is the left-hemisphere
    container; it does not re-describe the nuclei.

    The asymmetric child discipline applies: the TMN is a full Tier 1
    hub leaf; the tuberal nucleus is a Tier 2 organ-flavored leaf. Do
    not force the full Tier 1 template onto the tuberal nucleus, and do
    not reduce the TMN to a Tier 2 stub. Same discipline as the parent
    container; restated here so a contributor entering at the hemisphere
    level sees it.

    THREE NAMING TRAPS (reproduced from ../../__init__.py — must be
    declared at every level):
    - TUBER CINEREUM vs. TUBERAL DIVISION: this node and the sibling
      hypothalamus/tuberal/ division are ADJACENT BUT DISTINCT tree
      nodes. The tuber cinereum is the anatomical floor of the tuberal
      region; the tuberal division is the regional subdivision
      containing arcuate, VMH, DMH, and tuberal LHA. Do not merge.
    - TMN vs. MAMMILLARY BODIES: "tuberomammillary" contains
      "mammillary"; the TMN sits at the tuberal-mammillary junction.
      But the TMN (histaminergic wake hub) is functionally unrelated to
      the mammillary bodies (Papez circuit memory relay). Do not merge.
    - TMN vs. TUBERAL NUCLEUS (intra-container): the TMN and the
      tuberal nucleus are two distinct nuclei with unrelated functions.
      Do not treat them as a pair of similar structures.

Functional Mode:
    Same as the parent tuber_cinereum container and the two nuclei. See
    ../../__init__.py § Functional Mode and the two leaf files
    (./tuberomammillary_nucleus/ and ./tuberal_nucleus/) for the full
    descriptions. No documented functional asymmetry between left and
    right tuber cinereum. Do not fabricate one.

Hormonal Modulation:
    Same as the parent. TMN: histamine output; orexin excitatory input;
    GABA (LPO) inhibitory input; monoamines modulatory; adenosine
    inhibitory. Tuberal nucleus: poorly characterized; document
    presumed metabolic input as not established. See ../../__init__.py
    § Hormonal Modulation.

Memory Interfaces:
    Same as the parent. TMN: reads short_term (sleep pressure),
    temporal_sequence_learning (circadian arousal gating),
    emotional_valence (stress/arousal). Writes no stored content
    directly. Tuberal nucleus: poorly characterized; no documented
    memory interface. See ../../__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No hemisphere-level prompt fragment. The TMN's wake/arousal
    fragment is emitted by ./tuberomammillary_nucleus/ (the full leaf)
    and represents the bilateral TMN; the tuberal nucleus emits no
    fragment (poorly characterized). See ../../__init__.py § Model
    Integration for the fragment spec, the AGGREGATION RULE (three-way
    aggregation with LPO sleep and LHA orexin/MCH fragments at the
    hypothalamic level), and the guardrail ("do not treat high wake
    state as a cognitive achievement or low wake state as impairment").

Children (asymmetric — one Tier 1 hub, one Tier 2 leaf):
    - tuberomammillary_nucleus/   ★ Tier 1 hub leaf. Wake-promoting;
                                    histaminergic; LPO target; orexin
                                    target; one of five ascending
                                    arousal nuclei.
    - tuberal_nucleus/            Tier 2 organ-flavored leaf. Small;
                                    poorly characterized; thin
                                    literature.

Left-specific reciprocal connections to enforce in Stage 4 (do not
duplicate the right-side or mirror edges here — those belong in
right/__init__.py):
    - tuberomammillary_nucleus/ ↔
      lateral_area/left/preoptic_area/lateral_preoptic_nucleus (LPO →
      TMN; inhibitory; sleep promotion; PATH CORRECTION: the LPO leaf
      currently points at "hindbrain/.../tuberomammillary_nucleus";
      the correct path is hypothalamus/tuber_cinereum/left/
      tuberomammillary_nucleus/ — Stage 4 should correct the LPO path,
      functional edge is correct).
    - tuberomammillary_nucleus/ ↔
      anterior/lateral_area/left/anterior_part_of_lateral_nucleus
      (orexin → TMN; excitatory; wake promotion; left-side).
    - tuberomammillary_nucleus/ →
      telencephalon/cerebral_hemispheres/left/subcortical/
      basal_forebrain (arousal; cortical activation).
    - tuberomammillary_nucleus/ → cortex (diffuse histaminergic arousal
      projection; left hemisphere).
    - tuberomammillary_nucleus/ →
      thalamus/left/midline_nuclear_group and
      thalamus/left/medial_nuclear_group/intralaminar_nuclear_group
      (arousal relay; midline — verify).
    - tuberomammillary_nucleus/ ↔
      midbrain/tegmentum/dorsal_raphe_nucleus,
      hindbrain/metencephalon/pons/tegmentum/locus_coeruleus,
      midbrain/tegmentum/laterodorsal_tegmental_nucleus,
      midbrain/tegmentum/pedunculopontine_nucleus (mutual arousal
      network with the other four ascending arousal nuclei; all midline
      or midline-adjacent — verify).
    - tuberomammillary_nucleus/ ←
      anterior/medial_area/left/suprachiasmatic_nucleus (SCN → TMN;
      circadian arousal gating; SCN is midline-adjacent — verify).
    - tuberal_nucleus/ ↔
      tuberal/medial_area/left/arcuate_nucleus (adjacent tuberal
      endocrine regulation; continuity edge, not duplicate-structure
      warning; tuberal arcuate file to be drafted).

Notes:
    - Left-hemisphere container. Not a delta of the parent — it is the
      authoritative left-hemisphere container. right/ is a delta of
      this file (lateral_area/right/ convention).
    - The asymmetric child discipline is reproduced from the parent:
      TMN is Tier 1 hub, tuberal nucleus is Tier 2 leaf. Do not flatten
      them into the same template.
    - All three naming traps are reproduced because they apply to
      specific children within THIS hemisphere container (tuberal
      nucleus vs. TMN inside the container; tuber cinereum vs. tuberal
      division across the tree; TMN vs. mammillary bodies across the
      tree).
    - The LPO path correction is restated here because the TMN edge is
      a specific edge of this container's child. Stage 4 will see the
      correction at both the parent container and this left container.
    - The TMN ↔ LPO and TMN ↔ orexin edges form the hypothalamic
      sleep-wake switch from the wake side: LPO inhibits TMN (sleep);
      orexin excites TMN (wake). The three-fragment aggregation
      (LPO/TMN/orexin) is the model-prompt expression of this switch.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/tuber_cinereum/.
"""