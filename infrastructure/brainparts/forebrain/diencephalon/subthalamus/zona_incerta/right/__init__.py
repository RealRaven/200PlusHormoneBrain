"""
Package: infrastructure.brainparts.forebrain.diencephalon.subthalamus.zona_incerta.right
Anatomical Role:
    The right zona incerta (ZI). Same broad, elongated band of cells in
    the right subthalamus documented in ../left/, situated between the
    right subthalamic nucleus (ventral) and the right thalamus (dorsal),
    and a HETEROGENEOUS MODULATORY HUB: its cell types, connections,
    and functions overlap with several systems (arousal, nociception,
    visceral regulation, motor gating), and it is less well
    characterized than the STN.

    The "zone of uncertainty" historical framing is preserved on the
    right identically: the zona incerta was named for the difficulty of
    assigning it a clear function, and the modern literature narrows
    but does not resolve it into a discrete functional unit. See
    ../left/__init__.py for the full anatomical description, the
    four-role overlapping-contributions framing, and the honest
    documentation of the partially characterized literature.

    Reproduced THREE TRAPS (apply equally on the right):
    - ZONA INCERTA vs. LATERAL HYPOTHALAMIC AREA (the primary trap):
      the right zona incerta sits adjacent to the right LHA; some
      authors treat ZI as dorsal LHA extension; this tree keeps them
      distinct; do not merge; do not move zona incerta under
      hypothalamus/.
    - ZONA INCERTA vs. SUBTHALAMIC NUCLEUS: the right STN (well-studied
      basal ganglia hub) and the right zona incerta (broad modulatory
      hub) are ADJACENT; distinct functions; do not merge.
    - ZONA INCERTA vs. THALAMUS: the right zona incerta sits just
      ventral to the right thalamus, but it is subthalamic, not
      thalamic. Do not move it under thalamus/.

    NO STRUCTURAL-IDENTITY TRAP: same as ../left/. Do not invent one.

Functional Mode:
    Same four overlapping roles as ../left/, each with the "contributes
    to" framing (not "is the"):
    - Arousal (moderate evidence): contributes to arousal via reticular
      inputs and cortical projections; NOT the arousal hub
      (LPO/TMN/LC/raphe/orexin are).
    - Nociception (moderate evidence): contributes to nociceptive
      processing and pain modulation; NOT the pain hub (PAG and
      spinothalamic pathways are).
    - Visceral regulation (moderate evidence): contributes to visceral
      regulation; NOT the primary visceral controller (PVN, NTS, RVLM
      are).
    - Motor gating (moderate evidence): contributes to motor gating,
      orienting, saccadic behavior; NOT the action selector (STN is).
    No single role is the anchor; the four are overlapping functional
    contributions, not discrete subdivisions.
    DBS use is EXPLORATORY and SECONDARY to the STN's established use,
    same as ../left/. See ../left/ § Functional Mode for the full
    four-role description and the DBS exploratory framing.
    No documented functional asymmetry between left and right zona
    incerta. Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. Heterogeneous modulatory inputs (reticular
    activating system, hypothalamic visceral nuclei, basal ganglia,
    spinothalamic-adjacent pathways); norepinephrine, dopamine, GABA,
    and several hypothalamic peptides; documented as "partially
    characterized." No single dominant modulator. The zona incerta is
    not a neuroendocrine nucleus; do not pad with the 12 axes. See
    ../left/ § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (arousal, nociceptive, visceral,
    motor state buffers). Writes none directly. No documented higher
    memory interface (no episodic, semantic, procedural, or
    reinforcement_value_based_learning read). See ../left/ § Memory
    Interfaces.

Model Integration (Gemma-4-E2B):
    No right zona incerta fragment. The four roles are contextual and
    heterogeneous; none is a discrete state the language model should
    be conditioned on. Same deliberate absence as ../left/ and the
    STN. The model-relevant arousal state is already carried by the
    LPO/TMN/AHN/VMH/PHN aggregates. See ../left/ § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:

    Adjacency (not signaling):
    - ↔ subthalamus/right/subthalamic_nucleus (adjacent nuclei within
      the right subthalamus; distinct functions; do not merge;
      right-side).
    - ↔ hypothalamus/.../lateral_area (ADJACENCY; the right zona
      incerta sits near the right LHA; some authors treat ZI as dorsal
      LHA extension; this tree keeps them distinct; right-side).

    Arousal:
    - ← brainstem/.../reticular_formation (reticular activating system
      inputs; arousal).
    - → telencephalon/cerebral_hemispheres/right/cortex (arousal;
      right-side).
    - → telencephalon/cerebral_hemispheres/right/subcortical/
      basal_forebrain (arousal; right-side).

    Nociception:
    - ← spinothalamic-adjacent pathways (spinothalamic-adjacent inputs;
      nociceptive).
    - ↔ midbrain/tegmentum/periaqueductal_gray (nociception; PAG is
      midline-adjacent — verify).
    - ↔ thalamus/right/posterior_nucleus_group/ventral_posterior_nucleus
      (posterior thalamic nociceptive relay; right-side).

    Visceral regulation:
    - ← hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (visceral inputs from the right PVN; right-side).
    - → brainstem/.../solitary_nucleus (visceral regulation; NTS is
      midline-adjacent — verify).
    - → brainstem/.../rostral_ventrolateral_medulla (visceral
      regulation; RVLM is midline-adjacent — verify).

    Motor gating:
    - ← telencephalon/.../subcortical/basal_ganglia (basal ganglia
      inputs; motor gating; right-side).
    - → midbrain/.../superior_colliculus (orienting and saccadic
      behavior; motor gating).
    - → telencephalon/cerebral_hemispheres/right/cortex/frontal/
      premotor_cortex (motor gating; right-side).

    Heterogeneous:
    - ← brainstem/.../laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (cholinergic arousal inputs; both
      midline-adjacent — verify).
    - ↔ midbrain/tegmentum/ventral_tegmental_area (dopaminergic
      modulation; VTA is midline-adjacent — verify).

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - Tier 2 organ-flavored delta. Short by design (~55 lines). Same
      template as the right deltas for INAH-1/2/4, the tuberal nucleus,
      and the lateral tuberal nuclei.
    - THE "ZONE OF UNCERTAINTY" FRAMING IS PRESERVED ON THE RIGHT: four
      overlapping roles, "contributes to" language, no discrete
      subdivisions, no single anchor. Do not flatten to "the right
      zona incerta = arousal" or "= pain."
    - THREE TRAPS reproduced in abbreviated form above; the full text
      is in ../left/ and the parent zona_incerta/ and subthalamus/
      containers. The ZI vs. LHA trap is the primary one and applies
      on the right identically.
    - NO SUBDIVISIONS on the right either: the zona incerta's
      subdivisions are not well enough characterized to document.
    - NO FRAGMENT: same as ../left/ and the STN. The four roles are
      contextual/heterogeneous, not state-level. Deliberate absence.
    - DBS USE IS EXPLORATORY AND SECONDARY on the right identically.
      Do not draft right zona incerta DBS as equivalent to right STN
      DBS.
    - ENTIRE SUBTHALAMUS BLOCK NOW COMPLETE: with this file, the
      subthalamus is fully documented on both hemispheres — the STN
      pair (Tier 1 hub), the zona incerta pair (Tier 2 hub), and the
      subthalamus container. The subthalamus is the LAST diencephalon
      block before the thalamus.
    - Midline targets (PAG, NTS, RVLM, LDT/PPN, VTA) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree. Right LHA,
      right PVN, right basal ganglia, right superior colliculus, right
      cortex, right basal forebrain, right premotor cortex, right
      posterior thalamus, and right zona incerta adjacency to right
      STN are hemisphere-split and require right-side targets
      explicitly.
    - Vocabulary used above is defined in Stage 0 files; see ../left/
      § Notes for the full list.
    - Connects upward to diencephalon/subthalamus/zona_incerta/.
"""