"""
Package: infrastructure.brainparts.forebrain.diencephalon.subthalamus.zona_incerta.left
Anatomical Role:
    The left zona incerta (ZI). A broad, elongated band of cells in the
    left subthalamus, situated between the left subthalamic nucleus
    (ventral) and the left thalamus (dorsal), extending mediolaterally
    across the left subthalamic region. It is a HETEROGENEOUS
    MODULATORY HUB: its cell types, connections, and functions overlap
    with several systems (arousal, nociception, visceral regulation,
    motor gating), and it is less well characterized than the STN.

    The zona incerta was historically named the "zone of uncertainty"
    because early neuroanatomists could not assign it a clear function.
    Modern work is narrowing its roles, but it remains a broad,
    multi-system modulatory hub rather than a single functional unit.
    This file preserves that framing honestly: the zona incerta's
    functions are documented as far as the literature supports, and
    no further.

    The left zona incerta is FUNCTIONALLY DISTINCT from the left STN:
        - Left STN: a well-studied, discrete basal ganglia nucleus
          (Tier 1 hub; indirect pathway; hemiballismus; DBS target).
        - Left zona incerta: a broad, heterogeneous modulatory hub
          (Tier 2 organ-flavored; arousal/nociception/visceral/motor
          gating; investigational DBS target).

    NAMING TRAPS (reproduced from the parent subthalamus/ and
    zona_incerta/ containers):

    - ZONA INCERTA vs. LATERAL HYPOTHALAMIC AREA (the primary trap):
      the left zona incerta sits adjacent to the left lateral
      hypothalamic area (LHA; hypothalamus/anterior/lateral_area/left/
      and its tuberal and posterior segments). Some authors treat the
      zona incerta as a DORSAL EXTENSION of the LHA; this tree places
      it under subthalamus/, not under hypothalamus/. The two are
      anatomically adjacent but DISTINCT TREE NODES. Do not merge; do
      not move zona incerta under hypothalamus/.

    - ZONA INCERTA vs. SUBTHALAMIC NUCLEUS: the left STN (well-studied
      basal ganglia hub) and the left zona incerta (broad modulatory
      hub) are ADJACENT within the left subthalamus. Do not merge; do
      not treat them as a pair of similar nuclei.

    - ZONA INCERTA vs. THALAMUS: the left zona incerta sits just
      ventral to the left thalamus, but it is a SUBTHALAMIC structure,
      not a thalamic one. Do not move it under thalamus/.

    NO STRUCTURAL-IDENTITY TRAP: the left zona incerta is a single
    (though heterogeneous) structure. There is no split-structure or
    duplicate-location issue. Do not invent one.

Functional Mode:
    The left zona incerta is HETEROGENEOUS: it has multiple, partly
    overlapping functional roles, and no single role is "the" anchor.
    The four documented roles, in decreasing order of confidence:

    - Arousal (moderate evidence):
        * The left zona incerta receives inputs from the brainstem
          reticular activating system and projects to the left cortex
          and left basal forebrain; it CONTRIBUTES TO arousal and
          cortical activation.
        * Its arousal role is less characterized than the LPO/TMN/LC/
          raphe/LDT-orexin arousal system, and less discrete. The
          zona incerta is NOT "the" arousal hub; it is one of several
          brainstem and diencephalic contributors.
        * Direction: zona incerta activity ↑ during arousal; its
          contribution is upstream modulation, not a primary
          arousal state.

    - Nociception (moderate evidence):
        * The left zona incerta receives spinothalamic-adjacent inputs
          and projects to the left posterior thalamus and left
          periaqueductal gray; it CONTRIBUTES TO nociceptive
          processing and pain modulation.
        * Its nociceptive role is less characterized than the PAG's
          descending pain modulation. The zona incerta is a
          contributor, not "the" pain hub.
        * Direction: noxious stimuli ↑ zona incerta activity;
          descending modulation is one of its contributions.

    - Visceral regulation (moderate evidence):
        * The left zona incerta receives inputs from left hypothalamic
          visceral nuclei and projects to brainstem autonomic centers;
          it CONTRIBUTES TO visceral regulation (cardiovascular,
          gastrointestinal).
        * The primary hypothalamic and brainstem visceral controllers
          are the PVN, the NTS, and the RVLM; the zona incerta's
          contribution is modulatory, not primary.
        * Direction: visceral state modulates zona incerta activity;
          its contribution is upstream modulation.

    - Motor gating (moderate evidence):
        * The left zona incerta receives inputs from the left basal
          ganglia (via STN-adjacent circuitry) and projects to the
          left superior colliculus and left cortex; it CONTRIBUTES TO
          motor gating, particularly orienting and saccadic behavior.
        * Its motor role overlaps functionally with the STN's
          action-selection role, but is less discrete. Do not draft
          the zona incerta as a "second STN"; it is a broad motor
          gating contributor, not a well-defined action-selection
          hub.
        * Direction: motor preparatory state modulates zona incerta
          activity; its contribution is to orienting and gating, not
          to discrete action selection.

    - The left zona incerta is therefore a broad modulatory hub, not a
      single functional unit. Do not draft it as "the zona incerta =
      arousal" or "the zona incerta = pain"; it overlaps with multiple
      systems. Its functional identity is "broad modulatory hub" with
      heterogeneous, partially characterized roles.

    - DBS EXPLORATORY USE (secondary clinical fact): the left zona
      incerta has been explored as an alternative DBS target for
      Parkinson's disease and essential tremor, particularly when the
      left STN is not accessible or when targeting the zona incerta's
      cerebello-thalamic-adjacent territory is preferred. This is
      SECONDARY to the STN's established use; zona incerta DBS is
      investigational and less established.

Hormonal Modulation (heterogeneous; partially characterized):
    - The left zona incerta receives heterogeneous modulatory inputs
      from:
        * Brainstem reticular activating system (arousal).
        * Left hypothalamic visceral and autonomic nuclei.
        * Left basal ganglia (via STN-adjacent circuitry).
        * Spinothalamic-adjacent nociceptive pathways.
    - Modulators: norepinephrine, dopamine, GABA, and several
      hypothalamic peptides. Document as "heterogeneous modulatory
      inputs, partially characterized." Do not over-specify directions
      that the literature does not support.
    - Direction summary: heterogeneous modulatory inputs (arousal,
      visceral, basal ganglia, nociceptive); no single dominant
      modulator. Document as such.
    - The zona incerta is NOT a neuroendocrine nucleus: it is not a
      principal target of the 12 endocrine axes. Its modulators are
      brainstem and hypothalamic transmitters, not the endocrine
      axes. Do not pad the section with the 12 axes.

Memory Interfaces:
    - Reads:
        * short_term: current arousal state, nociceptive state, visceral
          state, and motor state buffers. The left zona incerta's
          multiple roles depend on these.
    - Writes: none directly. The left zona incerta drives modulatory
      output (arousal, nociception, visceral, motor gating); it does
      not write stored content.
    - No documented higher memory interface (no episodic, semantic,
      procedural, or reinforcement_value_based_learning read). The
      zona incerta is not a memory-adjacent node — unlike the STN,
      which reads procedural and reinforcement memory.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No left zona incerta fragment. The left zona incerta's functions
      are contextual and heterogeneous; the model prompt does not
      need a zona incerta block because none of its roles is a
      discrete state the language model should be conditioned on.
    - The arousal/thermoregulatory fragments (from LPO, TMN, AHN, VMH,
      PHN) already carry the model-relevant arousal state; the zona
      incerta is downstream modulation, not an independent state.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same discipline as the STN.
    - The zona incerta DBS context is documented in Functional Mode
      for completeness, but is not a prompt field.
    - No multimodal input is consumed here; no fragments are emitted.

Reciprocal Connections (left-side; the right side is in ../right/):

    Adjacency (not signaling):
    - ↔ subthalamus/left/subthalamic_nucleus (adjacent nuclei within
      the left subthalamus; distinct functions; do not merge; the STN
      is the basal ganglia hub, the zona incerta is the broad
      modulatory hub; no documented signaling edge between them
      beyond adjacency).
    - ↔ hypothalamus/.../lateral_area (ADJACENCY; the left zona
      incerta sits near the left LHA; some authors treat ZI as dorsal
      LHA extension; this tree keeps them distinct; do not merge;
      document as adjacency, not signaling).

    Arousal:
    - ← brainstem/.../reticular_formation (reticular activating system
      inputs; arousal).
    - → telencephalon/cerebral_hemispheres/left/cortex (arousal;
      direct cortical projections).
    - → telencephalon/cerebral_hemispheres/left/subcortical/
      basal_forebrain (arousal; basal forebrain relay).

    Nociception:
    - ← spinothalamic-adjacent pathways (spinothalamic-adjacent inputs;
      nociceptive).
    - ↔ midbrain/tegmentum/periaqueductal_gray (nociception; PAG is
      midline-adjacent — verify).
    - ↔ thalamus/left/posterior_nucleus_group/ventral_posterior_nucleus
      (posterior thalamic nociceptive relay; the zona incerta
      contributes to the spinothalamic-posterior thalamus pathway).

    Visceral regulation:
    - ← hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (visceral inputs from the left PVN).
    - → brainstem/.../solitary_nucleus (visceral regulation; NTS is
      midline-adjacent — verify).
    - → brainstem/.../rostral_ventrolateral_medulla (visceral
      regulation; RVLM is midline-adjacent — verify).

    Motor gating:
    - ← telencephalon/.../subcortical/basal_ganglia (basal ganglia
      inputs; motor gating).
    - → midbrain/.../superior_colliculus (orienting and saccadic
      behavior; motor gating).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      premotor_cortex (motor gating).

    Heterogeneous:
    - ← brainstem/.../laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (cholinergic arousal inputs; both
      midline-adjacent — verify).
    - ↔ midbrain/tegmentum/ventral_tegmental_area (dopaminergic
      modulation; VTA is midline-adjacent — verify).

Notes:
    - Tier 2 organ-flavored leaf (left). NOT a Tier 1 hub. The zona
      incerta's functions are heterogeneous and partially
      characterized; do not draft it as a well-studied hub like the
      STN.
    - THE "ZONE OF UNCERTAINTY" FRAMING IS PRESERVED HONESTLY: four
      overlapping roles (arousal, nociception, visceral, motor
      gating), none of which is "the" anchor. The "contributes to"
      language is deliberate. Do not flatten to "the zona incerta =
      arousal" or "the zona incerta = pain."
    - THREE TRAPS reproduced in full above (ZI vs. LHA; ZI vs. STN;
      ZI vs. thalamus). The ZI vs. LHA trap is the primary one; the
      "some authors treat ZI as dorsal LHA extension" framing is
      preserved and explicitly rejected by this tree's placement
      under subthalamus/.
    - NO SUBDIVISIONS: the zona incerta's subdivisions are not well
      enough characterized to be documented as separate tree nodes or
      as separate content within this leaf. The four roles are
      overlapping functional contributions, not discrete
      subdivisions. Do not invent subdivisions.
    - NO FRAGMENT: same as the STN. The zona incerta's roles are
      contextual/heterogeneous, not state-level. Do not add a
      fragment.
    - DBS USE IS EXPLORATORY AND SECONDARY to the STN's established
      use. Do not draft zona incerta DBS as equivalent to STN DBS.
    - THE ZONA INCERTA IS NOT THE STN (adjacent; distinct functions);
      NOT THE LHA (adjacent; this tree keeps them distinct); NOT THE
      THALAMUS (subthalamic, not thalamic). The three traps make
      these distinctions explicit.
    - The zona incerta's heterogeneous modulatory inputs are
      documented as "partially characterized"; do not over-specify
      directions that the literature does not support.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, norepinephrine, GABA,
      peptides, acetylcholine); memory/stores/ (short_term);
      gateway/.
    - Connects upward to diencephalon/subthalamus/zona_incerta/.
"""