"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuber_cinereum.right.tuberomammillary_nucleus
Anatomical Role:
    Right tuberomammillary nucleus (TMN). The brain's sole source of
    neuronal histamine, mirrored to the right hemisphere: a small,
    densely packed nucleus at the tuberal-mammillary junction of the
    right posterior hypothalamus. See
    ../../left/tuberomammillary_nucleus/__init__.py for the full
    anatomical description, the five-arousal-nuclei framing, the
    sleep-wake switch architecture, and the histamine output pathway.

    Reproduced framing (apply equally on the right):
    - Five ascending arousal nuclei: TMN (histamine), LC
      (norepinephrine), dorsal raphe (serotonin), LDT/PPN
      (acetylcholine), LHA orexin neurons (orexin). The right TMN is
      the histaminergic member.
    - Sleep-wake switch, wake-side arm: LPO/VLPO (GABAergic) inhibits
      the right TMN → sleep; LHA orexin (glutamatergic) excites the
      right TMN → wake. The two arms are reciprocally organized.

    Reproduced distinctions (apply equally on the right):
    - DISTINCT from the mammillary bodies (despite "tuberomammillary"):
      TMN = histaminergic wake; mammillary bodies = Papez circuit
      memory relay. Unrelated functions.
    - DISTINCT from the right tuberal nucleus (adjacent neighbor): TMN
      = well-studied hub; tuberal nucleus = small and poorly
      characterized. Do not treat as a pair.
    - DISTINCT from the tuberal division: TMN is in the tuber cinereum
      (floor), not the tuberal division (regional subdivision above).

Functional Mode:
    Same as ../../left/tuberomammillary_nucleus/. Histaminergic arousal
    (sole neuronal source of histamine); sleep-wake switch wake-side
    arm; one of five ascending arousal nuclei; histaminergic
    contribution to attention and cognition. No documented functional
    asymmetry between left and right TMN. Do not fabricate one. See
    ../../left/tuberomammillary_nucleus/ § Functional Mode.

Hormonal Modulation:
    Same as ../../left/tuberomammillary_nucleus/. Histamine (output,
    not modulator); orexin ↑ TMN activity (wake); GABA (LPO) ↓ TMN
    activity (sleep); adenosine ↓ TMN activity (sleep pressure);
    norepinephrine ↑ TMN activity; serotonin modulates; PGD2 ↓ TMN
    activity. See ../../left/tuberomammillary_nucleus/ § Hormonal
    Modulation for the full list and directions.

Memory Interfaces:
    Same as ../../left/tuberomammillary_nucleus/. Reads short_term
    (sleep pressure, arousal state), temporal_sequence_learning
    (circadian arousal gating), emotional_valence (stress/arousal).
    Writes no stored content directly. See
    ../../left/tuberomammillary_nucleus/ § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The wake/arousal fragment (histamine
    tone, wake state, arousal system, sleep-pressure, and the "do not
    treat high wake state as a cognitive achievement or low wake state
    as impairment" guardrail) is emitted once at the left/ level and
    represents the bilateral TMN. Emitting a separate right-side
    fragment would double-count the arousal signal. See
    ../../left/tuberomammillary_nucleus/ § Model Integration.

    Reproduced AGGREGATION RULE (mandatory, applies identically on the
    right): this fragment is one of THREE in the hypothalamic sleep-wake
    switch aggregate:
        (1) LPO sleep fragment (lateral_area/right/preoptic_area/
            lateral_preoptic_nucleus/).
        (2) TMN wake fragment (bilateral, emitted from the left leaf).
        (3) Orexin/MCH fragment (anterior/lateral_area/right/
            anterior_part_of_lateral_nucleus/).
    The three are aggregated at the hypothalamic level; do not
    double-count arousal state across them.

Right-specific reciprocal connections to enforce in Stage 4:

    Sleep-wake switch (the reciprocal arm):
    - ↔ lateral_area/right/preoptic_area/lateral_preoptic_nucleus
      (LPO → TMN; INHIBITORY; sleep promotion; PATH CORRECTION: the
      right LPO leaf currently points at
      "hindbrain/.../tuberomammillary_nucleus"; the correct path is
      hypothalamus/tuber_cinereum/right/tuberomammillary_nucleus/ —
      Stage 4 should correct the right LPO path; the functional edge
      is correct, only the path is wrong).
    - ↔ anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (orexin → TMN; EXCITATORY; wake promotion; wake-side arm of the
      switch; right-side).

    Ascending arousal system (the other four nuclei, mutual arousal):
    - ↔ hindbrain/metencephalon/pons/tegmentum/locus_coeruleus (LC;
      noradrenergic; mutual arousal; LC is midline-adjacent — verify).
    - ↔ midbrain/tegmentum/dorsal_raphe_nucleus (raphe; serotonergic;
      mutual arousal; raphe is midline).
    - ↔ midbrain/tegmentum/laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (LDT/PPN; cholinergic; mutual arousal;
      both are midline-adjacent — verify).

    Diffuse cortical and forebrain arousal targets:
    - → telencephalon/cerebral_hemispheres/right/subcortical/
      basal_forebrain (arousal; basal forebrain cholinergic relay;
      right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex (diffuse
      histaminergic arousal projection; right hemisphere).
    - → thalamus/right/midline_nuclear_group and
      thalamus/right/medial_nuclear_group/intralaminar_nuclear_group
      (arousal relay; midline — verify).

    Circadian and state input:
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → TMN; circadian arousal gating; SCN is midline-adjacent —
      verify).
    - ← lateral_area/right/preoptic_area/lateral_preoptic_nucleus
      (the LPO → TMN inhibitory edge is also an input; see the
      sleep-wake switch section above).

    - ↔ ../../left/tuberomammillary_nucleus/ (hemisphere counterpart;
      no functional asymmetry assumed).

Notes:
    - Delta file of ../../left/tuberomammillary_nucleus/. Not a full
      leaf. Do not duplicate.
    - THIS IS THE FINAL FILE IN THE ENTIRE TUBER CINEREUM SUBTREE.
      With this file, the subtree is complete on both hemispheres:
      - tuber_cinereum/__init__.py (container)
      - tuber_cinereum/left/__init__.py (left container)
      - tuber_cinereum/right/__init__.py (right container delta)
      - tuber_cinereum/left/tuberal_nucleus/ (Tier 2 leaf)
      - tuber_cinereum/right/tuberal_nucleus/ (Tier 2 delta)
      - tuber_cinereum/left/tuberomammillary_nucleus/ (★ Tier 1 hub)
      - tuber_cinereum/right/tuberomammillary_nucleus/ (this delta)
    - Histamine is the TMN's OUTPUT, not a modulator. Same discipline
      as ../../left/. Do not list it as a modulator on the right
      either.
    - The H1 antihistamine clinical fact (first-generation H1
      antihistamines cause drowsiness by blocking the TMN's
      histaminergic wake signal; second-generation H1 antihistamines
      are designed to exclude the CNS) applies bilaterally. Reproduced
      here in abbreviated form; the full clinical description lives in
      ../../left/tuberomammillary_nucleus/ and is NOT duplicated.
    - The LPO path correction is restated above for the right side
      because the right LPO leaf has the same placeholder path issue.
      Stage 4 should correct both LPO leaves (left and right).
    - The 10th guardrail ("do not treat high wake state as a cognitive
      achievement or low wake state as impairment") applies on the
      right identically. The guardrail is reproduced in the Model
      Integration section above.
    - No independent fragment: the wake/arousal fragment is bilateral,
      emitted from the left leaf. Same convention as
      habenular_nuclei/right/ and the other deltas in the tree.
    - Midline targets (LC, raphe, LDT/PPN, thalamic midline/intralaminar
      nuclei, SCN) are flagged with "verify" so Stage 4 does not force
      a hemisphere split on structures that are not hemisphere-split
      in the tree. Right basal forebrain, right cortex, right LPO, and
      right orexin neurons are hemisphere-split and require right-side
      targets explicitly.
    - The five-arousal-nuclei network is mutual: the right TMN connects
      to the right/adjacent LC, raphe, LDT/PPN, and orexin nodes. When
      those are drafted, they should reciprocate the right TMN edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/tuberomammillary_nucleus/ § Notes for the full list.
    - Connects upward to hypothalamus/tuber_cinereum/right/.
"""