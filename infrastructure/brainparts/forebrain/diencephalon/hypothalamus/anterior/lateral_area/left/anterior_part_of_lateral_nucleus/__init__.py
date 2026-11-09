"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.left.anterior_part_of_lateral_nucleus
Anatomical Role:
    The anterior part of the left lateral nucleus is the rostral pole of
    the lateral hypothalamic area (LHA) orexin/MCH field. It contains two
    intermingled neuronal populations in the left hemisphere:
        - Orexin/hypocretin (ORX/Hcrt) neurons: ~70,000 in humans, located
          exclusively in the hypothalamus, spanning the dorsomedial
          nucleus through the perifornical area into the LHA[reference:0].
          The anterior part of the lateral nucleus contains the rostral
          portion of this field.
        - Melanin-concentrating hormone (MCH) neurons: co-extensive with
          orexin neurons in the LHA, with a similar anterior-to-posterior
          distribution[reference:1]. MCH and orexin populations are
          intermingled but functionally antagonistic.

    CRITICAL DISTINCTION FROM LHA: this node is the *anterior pole* of
    the LHA orexin/MCH field, not the whole LHA. The LHA proper spans
    the tuberal and posterior divisions and is documented under
    hypothalamus/tuberal/lateral_area/. The anterior part documented here
    is the rostral head of the same neurochemical field. Stage 4 audit
    should treat the anterior and tuberal LHA orexin/MCH populations as
    a *continuum*, not as duplicate structures. Do not merge the nodes;
    document the continuity explicitly.

Functional Mode:
    - Arousal and wakefulness (orexin): orexin neurons project to the
      locus coeruleus (LC), ventral tegmental area (VTA), dorsal raphe,
      tuberomammillary nucleus, and basal forebrain, promoting wakefulness
      and stabilizing arousal[reference:2][reference:3]. Orexin deficiency
      causes narcolepsy[reference:4].
    - Feeding drive and food seeking (orexin): orexin neurons are
      activated by fasting and low glucose, and drive food-seeking and
      reward-based feeding via VTA dopamine activation[reference:5].
    - Reward and motivation (orexin): projections to VTA and nucleus
      accumbens make rewarding stimuli arousing and motivate approach
      behavior.
    - Sleep and energy conservation (MCH): MCH neurons discharge
      reciprocally to orexin neurons across the sleep-wake cycle, with
      highest activity during paradoxical sleep; they promote sleep,
      suppress locomotor activity, decrease body temperature and heart
      rate, and conserve energy[reference:9].
    - Appetitive state transitions (both): orexin and MCH "harmonize in
      a divergent yet overall cooperative manner to orchestrate feeding
      behavior through transitions between various appetitive states"
      [reference:10]. The two populations are antagonistic in valence but
      cooperative in timing.
    - The nucleus is functionally two-mode: ORX-dominant (arousal/foraging)
      vs. MCH-dominant (rest/conservation). It is not a single "feeding
      center".

Hormonal Modulation:
    - Orexin neurons:
        * Ghrelin: direct excitatory modulation; fasting activates orexin
          neurons via ghrelin[reference:11][reference:12].
        * Leptin: indirect inhibitory modulation; leptin blunts orexin
          activation under low glucose[reference:13][reference:14].
        * Glucose: inhibitory. Orexin neurons are glucose-inhibited (GI);
          falling glucose activates them[reference:15].
        * Orexin expression correlates negatively with blood glucose,
          leptin, and food intake.
    - MCH neurons:
        * Glucose: excitatory (opposite to orexin); glucose-induced
          excitation of MCH neurons promotes sleep and suppresses energy
          expenditure[reference:17].
        * Estrogen: acts to inhibit lateral hypothalamic MCH neurons
          receiving excitatory input from medial hypothalamic NPY neurons
          [reference:18].
        * NPY/AgRP (arcuate): excitatory input to MCH neurons[reference:19].
    - Both populations:
        * Monoamines (norepinephrine, serotonin, dopamine) and
          acetylcholine modulate orexin neurons[reference:20].
        * Circadian drive from the SCN modulates both populations
          (SCN → LHA projections)[reference:21].
    - Direction summary: ghrelin ↑ ORX, leptin ↓ ORX, glucose ↓ ORX and
      ↑ MCH, estrogen ↓ MCH, NPY ↑ MCH. These directions are the
      actionable content of this section; do not omit them.

Memory Interfaces:
    - Reads:
        * short_term: current metabolic state (glucose, ghrelin, leptin
          signals) and arousal/sleep drive buffers. The ORX/MCH mode
          switch depends on these.
        * reinforcement_value_based_learning: prior feeding and reward
          outcomes, used to weight food-seeking vs. rest.
        * temporal_sequence_learning: circadian phase (SCN → LHA), used
          to gate arousal and feeding drive to time of day.
        * emotional_valence: stress/arousal context; orexin is activated
          by stress and contributes to arousal under threat.
    - Writes:
        * reinforcement_value_based_learning: orexin-mediated reward
          signals from VTA/NAc feed back into value learning; document
          as a modulation, not a direct write.
        * Does not write episodic or semantic content directly.
    - The ORX/MCH mode switch is a *state*, not a memory write. Store
      schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (applied after the lateral_area-level fragments,
      before the cortical reasoning fragments):
        "Arousal/feeding state — anterior lateral nucleus (left):
         - Orexin tone: [low / moderate / high].
         - MCH tone: [low / moderate / high].
         - Dominant mode: [ORX-dominant / balanced / MCH-dominant].
         - Feeding motivation: [0-1].
         - Metabolic signal: [fasted / fed]. Glucose: [low/normal].
         If ORX-dominant: increase response urgency, exploratory framing,
         and food-seeking or reward-oriented language. If MCH-dominant:
         reduce arousal, favor rest-adjacent and energy-conserving tone,
         and lower response tempo. If balanced: default to neutral
         engagement. Do not treat MCH-dominance as impairment; it is a
         state bias, not a degradation."
    - The fragment is emitted whenever the homeostatic state block is
      emitted (always), with the dominant mode as the primary signal.
    - Guardrail: the "do not treat MCH-dominance as impairment" clause is
      the orexin/MCH equivalent of the habenula's "does not silence
      reasoning" guardrail. It prevents the model from over-suppressing
      under high MCH tone.
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (enforce in Stage 4 audit):
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus
      (orexin → LC; excitatory; arousal).
    - → midbrain/tegmentum/ventral_tegmental_area (orexin → VTA;
      excitatory; reward/motivation).
    - → midbrain/tegmentum/dorsal_raphe_nucleus (orexin → raphe;
      arousal)[reference:24].
    - → telencephalon/cerebral_hemispheres/left/subcortical/
      basal_forebrain (orexin → basal forebrain; arousal)[reference:25].
    - → cerebral cortex (orexin → cortex; direct and via LC/VTA)[reference:26].
    - ↔ hypothalamus/tuberal/lateral_area/left/ (same ORX/MCH field;
      anterior-to-tuberal continuity; document as continuum, not
      duplicate)[reference:27].
    - ↔ hypothalamus/anterior/medial_area/left/arcuate_nucleus/ (NPY/AgRP
      → MCH; leptin/ghrelin → ORX)[reference:28][reference:29].
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → LHA; circadian gating)[reference:30].

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - The LHA distinction is the single most important note in this
      file. The anterior pole here and the tuberal LHA are one
      neurochemical field split by the tree's rostrocaudal divisions.
      The Stage 4 audit must confirm the reciprocal edge to
      tuberal/lateral_area/left/ and must not flag the two as duplicate
      structures.
    - Orexin and MCH are intermingled but antagonistic; the file must
      not collapse them into one "lateral hypothalamic feeding center".
      The "dominant mode" in the model fragment is the operational
      consequence of this.
    - The arcuate → LHA edge (NPY/AgRP → MCH, leptin/ghrelin → ORX) is
      the metabolic input that makes this nucleus a feeding hub. It is
      also documented in arcuate_nucleus/ (when drafted); keep the two
      descriptions consistent in direction.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, ghrelin, leptin, NPY, AgRP,
      glucose), 05_* (monoamines, acetylcholine), 10_* (circadian, SCN);
      memory/stores/; gateway/.
    - Connects upward to hypothalamus/anterior/lateral_area/left/.
"""