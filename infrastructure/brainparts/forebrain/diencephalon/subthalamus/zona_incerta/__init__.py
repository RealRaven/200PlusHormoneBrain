"""
Package: infrastructure.brainparts.forebrain.diencephalon.subthalamus.zona_incerta
Anatomical Role:
    The zona incerta (ZI) is a broad, elongated band of cells in the
    subthalamus, situated between the subthalamic nucleus (ventral) and
    the thalamus (dorsal), extending mediolaterally across the
    subthalamic region. It is a HETEROGENEOUS MODULATORY HUB: its cell
    types, connections, and functions overlap with several systems
    (arousal, nociception, visceral regulation, motor gating), and it
    is less well characterized than the STN.

    The zona incerta was historically named the "zone of uncertainty"
    because early neuroanatomists could not assign it a clear function.
    Modern work is narrowing its roles, but it remains a broad,
    multi-system modulatory hub rather than a single functional unit.
    The "zone of uncertainty" framing is preserved honestly in this
    file — the zona incerta's functions are documented as far as the
    literature supports, and no further.

    The zona incerta is a member of the subthalamus region but is
    FUNCTIONALLY DISTINCT from the STN:
        - STN: a well-studied, discrete basal ganglia nucleus (Tier 1
          hub; indirect pathway; hemiballismus; DBS target).
        - Zona incerta: a broad, heterogeneous modulatory hub (Tier 2
          organ-flavored; arousal/nociception/visceral/motor gating;
          investigational DBS target).

    NAMING TRAPS (critical — three confusions apply here):

    - ZONA INCERTA vs. LATERAL HYPOTHALAMIC AREA (the primary trap):
      the zona incerta sits adjacent to the lateral hypothalamic area
      (LHA; hypothalamus/anterior/lateral_area/ and its tuberal and
      posterior segments). Some authors treat the zona incerta as a
      DORSAL EXTENSION of the LHA; this tree places it under
      subthalamus/, not under hypothalamus/. The two are anatomically
      adjacent but DISTINCT TREE NODES. Do not merge; do not move
      zona incerta under hypothalamus/.

    - ZONA INCERTA vs. SUBTHALAMIC NUCLEUS: the STN (well-studied
      basal ganglia hub) and the zona incerta (broad modulatory hub)
      are ADJACENT within the subthalamus. Do not merge; do not treat
      them as a pair of similar nuclei. The STN is the subthalamus's
      clinical anchor; the zona incerta is its poorly characterized
      neighbor.

    - ZONA INCERTA vs. THALAMUS: the zona incerta is named for its
      position relative to the thalamus (it sits just ventral to it),
      but it is a SUBTHALAMIC structure, not a thalamic one. Do not
      move it under thalamus/.

Functional Mode:
    The zona incerta is HETEROGENEOUS: it has multiple, partly
    overlapping functional roles, and no single role is "the" anchor.
    The four documented roles, in decreasing order of confidence:

    - Arousal (moderate evidence):
        * The zona incerta receives inputs from the reticular
          activating system and projects to the cortex and basal
          forebrain; it contributes to arousal and cortical
          activation.
        * The zona incerta's arousal role is less characterized than
          the LPO/TMN/LC/raphe/LDT-orexin arousal system, and less
          discrete. Document as "contributes to arousal" rather than
          "is the arousal hub."

    - Nociception (moderate evidence):
        * The zona incerta receives spinothalamic-adjacent inputs and
          projects to the posterior thalamus and periaqueductal gray;
          it contributes to nociceptive processing and pain modulation.
        * The zona incerta's nociceptive role is less characterized
          than the PAG's descending pain modulation; document as a
          "contributor" not "the" pain hub.

    - Visceral regulation (moderate evidence):
        * The zona incerta receives inputs from hypothalamic visceral
          nuclei and projects to brainstem autonomic centers;
          it contributes to visceral regulation (cardiovascular,
          gastrointestinal).
        * Document as "contributes to visceral regulation"; the
          primary hypothalamic and brainstem visceral controllers are
          the PVN, the NTS, and the RVLM.

    - Motor gating (moderate evidence):
        * The zona incerta receives inputs from the basal ganglia (via
          the STN-adjacent circuitry) and projects to the superior
          colliculus and cortex; it contributes to motor gating
          (particularly orienting and saccadic behavior).
        * The zona incerta's motor role overlaps functionally with the
          STN's action-selection role, but is less discrete. Document
          as "contributes to motor gating" alongside the STN.

    - The zona incerta is therefore a broad modulatory hub, not a
      single functional unit. Do not draft it as "the zona incerta =
      arousal" or "the zona incerta = pain"; it overlaps with
      multiple systems. Its functional identity is "broad modulatory
      hub" with heterogeneous, partially characterized roles.

    - DBS EXPLORATORY USE (secondary clinical fact): the zona incerta
      has been explored as an alternative DBS target for Parkinson's
      disease and essential tremor, particularly when the STN is not
      accessible or when targeting the zona incerta's
      cerebello-thalamic-adjacent territory is preferred. This is
      SECONDARY to the STN's established use; zona incerta DBS is
      investigational and less established.

Hormonal Modulation (zona incerta-specific; heterogeneous):
    - The zona incerta receives heterogeneous modulatory inputs from:
        * Brainstem reticular activating system (arousal).
        * Hypothalamic visceral and autonomic nuclei.
        * Basal ganglia (via STN-adjacent circuitry).
        * Spinothalamic-adjacent nociceptive pathways.
    - The zona incerta's modulators are therefore diverse:
      norepinephrine, dopamine, GABA, and several hypothalamic
      peptides. Document as "heterogeneous modulatory inputs,
      partially characterized."
    - The zona incerta is NOT a neuroendocrine nucleus: it is not a
      principal target of the 12 endocrine axes. Its modulators are
      brainstem and hypothalamic transmitters, not the endocrine
      axes. Do not pad the section with the 12 axes.
    - Direction summary: heterogeneous modulatory inputs (arousal,
      visceral, basal ganglia, nociceptive); no single dominant
      modulator. Document as such; do not over-specify directions
      that the literature does not support.

Memory Interfaces:
    - Reads:
        * short_term: current arousal state, nociceptive state, visceral
          state, and motor state buffers. The zona incerta's multiple
          roles depend on these.
    - Writes: none directly. The zona incerta drives modulatory
      output (arousal, nociception, visceral, motor gating); it does
      not write stored content.
    - No documented higher memory interface (no episodic, semantic,
      procedural, or reinforcement_value_based_learning read). The
      zona incerta is not a memory-adjacent node (unlike the STN,
      which reads procedural and reinforcement memory).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No zona incerta fragment. Same discipline as the STN: motor and
      arousal gating are functional facts, not state signals for the
      language model.
    - The zona incerta's functions are contextual and heterogeneous;
      the model prompt does not need a zona incerta block because
      none of its roles is a discrete state the language model should
      be conditioned on. The arousal/thermoregulatory fragments (from
      LPO, TMN, AHN, VMH, PHN) already carry the model-relevant
      arousal state; the zona incerta is downstream modulation, not
      an independent state.
    - AGGREGATION RULES: no fragments are emitted from this container
      or from the zona incerta leaves. Deliberate absence.
    - The zona incerta DBS context is documented in the leaves for
      completeness, but is not a prompt field.

Children (one child pair — Tier 2 leaf + delta):
    - left/    Tier 2 organ-flavored leaf. Left zona incerta: the
                 four roles (arousal, nociception, visceral, motor
                 gating), heterogeneous modulatory inputs, DBS
                 exploratory use, reciprocal connections.
    - right/   Tier 2 delta mirror of left/, differing only in the
                 right-side reciprocal edges. No functional asymmetry
                 documented.

    Both hemispheres are Tier 2 organ-flavored leaves (not Tier 1
    hubs): the zona incerta's functions are heterogeneous and
    partially characterized, not discrete. Same discipline as
    INAH-1/2, the tuberal nucleus, and the lateral tuberal nuclei.

Notes:
    - Hub container. Both children are Tier 2 organ-flavored leaves
      (not Tier 1 hubs). The zona incerta is not a well-studied hub
      like the STN; it is a broad modulatory hub.
    - THREE NAMING TRAPS reproduced above (ZI vs. LHA; ZI vs. STN; ZI
      vs. thalamus). All apply to the zona incerta specifically. Do
      not omit any of them.
    - THE ZONA INCERTA vs. LHA TRAP is the most important: some
      authors treat the zona incerta as a dorsal LHA extension, but
      this tree places it under subthalamus/. Do not merge; do not
      move it. Reproduce this warning at every level where the zona
      incerta is referenced.
    - THE "ZONE OF UNCERTAINTY" FRAMING IS PRESERVED HONESTLY. The
      zona incerta's functions are documented as far as the
      literature supports, and no further. Do not over-write it as a
      "hub" with a single anchor function. It has four partially
      overlapping roles (arousal, nociception, visceral, motor
      gating), none of which is "the" anchor.
    - The zona incerta's subdivisions (if any) are not well enough
      characterized to be documented as separate tree nodes or even
      as separate content within the leaf. Document the four roles
      as overlapping functional contributions, not as discrete
      subdivisions.
    - NO FRAGMENT: same as the STN. The zona incerta's roles are
      contextual/heterogeneous, not state-level. Do not add a
      fragment.
    - The zona incerta DBS use is EXPLORATORY and SECONDARY to the
      STN's established use. Do not draft it as equivalent to STN
      DBS.
    - The zona incerta is NOT the STN (adjacent; the STN is the
      well-studied basal ganglia hub, the zona incerta is the broad
      modulatory hub); NOT the LHA (some authors treat ZI as dorsal
      LHA extension; this tree does not); NOT the thalamus (ZI sits
      ventral to the thalamus but is subthalamic). The three traps
      make these distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, norepinephrine, GABA,
      peptides); memory/stores/ (short_term); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * zona_incerta/left|right ↔ subthalamus/left|right/
          subthalamic_nucleus (adjacent nuclei; distinct functions; do
          not merge; the STN is the basal ganglia hub, the zona
          incerta is the broad modulatory hub).
        * zona_incerta/left|right ↔ hypothalamus/.../lateral_area
          (ADJACENCY; the zona incerta sits near the LHA; some authors
          treat ZI as dorsal LHA extension; this tree keeps them
          distinct; do not merge; document as adjacency, not
          signaling).
        * zona_incerta/left|right ↔ telencephalon/.../basal_ganglia
          (motor gating; basal ganglia inputs).
        * zona_incerta/left|right ↔ brainstem/.../reticular_formation
          (arousal; reticular activating system inputs).
        * zona_incerta/left|right ↔ midbrain/tegmentum/
          periaqueductal_gray (nociception; PAG is midline-adjacent —
          verify).
        * zona_incerta/left|right ↔ brainstem/.../solitary_nucleus
          (visceral regulation; NTS is midline-adjacent — verify).
        * zona_incerta/left|right ↔ midbrain/.../superior_colliculus
          (motor gating; orienting and saccadic behavior).
        * zona_incerta/left|right ↔ cortex (arousal; direct cortical
          projections).
    - Connects upward to diencephalon/subthalamus/.
"""