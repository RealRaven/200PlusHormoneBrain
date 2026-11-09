"""
Package: infrastructure.brainparts.forebrain
Anatomical Role:
    The forebrain (prosencephalon) is the most rostral of the three primary
    brain vesicles and the seat of higher cognition, emotion, motivation, and
    endocrine regulation. It comprises two major subdivisions:
        - Diencephalon: thalamus, hypothalamus, epithalamus, subthalamus,
          pituitary gland, and the third ventricle. Relay, homeostasis, and
          endocrine control.
        - Telencephalon: cerebral hemispheres (cortex, subcortical structures,
          white matter, commissures) and lateral ventricles. Cognition,
          memory, emotion, and voluntary action.

Functional Mode:
    - Higher-order integration: sensory relay (thalamus) → cortical processing
      → executive control (prefrontal cortex) → limbic/motivational output
      (amygdala, hippocampus, basal ganglia, hypothalamus).
    - Endocrine orchestration: hypothalamic–pituitary cascades originate here
      and drive all 12 hormone axes documented in chemicals_hormones/.
    - Memory formation and recall: episodic (hippocampus), semantic (cortex),
      emotional valence (amygdala), and reinforcement learning (basal ganglia,
      VTA) are all anchored in forebrain structures.

Hormonal Modulation (forebrain-wide summary):
    - HPA axis (cortisol, CRH, ACTH): biases amygdala salience, suppresses
      hippocampal encoding under chronic stress, impairs prefrontal executive
      function at high chronic levels.
    - HPG axis (GnRH, estradiol, testosterone): modulates hypothalamic drive
      and limbic-social circuits.
    - Neuro modulators (dopamine, serotonin, norepinephrine, GABA): tune
      prefrontal working memory, striatal reward learning, and amygdala
      reactivity.
    - Detailed per-region modulation is documented in each child package's
      __init__.py, not here.

Memory Interfaces (forebrain-wide summary):
    - Reads: episodic (context retrieval), semantic (knowledge), emotional_
      valence (affective tagging), reinforcement_value_based_learning
      (outcome history), procedural (habit/skill caches).
    - Writes: episodic (hippocampus), semantic (cortical consolidation),
      emotional_valence (amygdala), procedural and stimulus_response_s_r_
      learning (basal ganglia), reinforcement_value_based_learning (VTA,
      substantia nigra).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The forebrain is the primary context-construction layer. Regions within
      it assemble the system-prompt blocks that precede every model call.
    - Forebrain-level prompt preamble (applied once per inference):
        "You are operating in forebrain mode: higher-order reasoning, memory
         retrieval, and motivated action. Downstream regional state blocks
         will follow."
    - Child regions append their own fragments after this preamble.

Children (documented in Stage 1 & Stage 3):
    - diencephalon/   : thalamus, hypothalamus, epithalamus, subthalamus,
                        pituitary_gland, subcommissural_organ, third_ventricle.
    - telencephalon/  : cerebral_hemispheres (cortex, subcortical, white_matter),
                        commissures, lateral_ventricles.

Notes:
    - This file is a container/orientation docstring. Do not duplicate child
      hormone or memory wiring here; each child package owns its own
      specification.
    - Vocabulary used above (hormone names, memory store names) is defined
      in Stage 0 files: chemicals_hormones/02_*, chemicals_hormones/05_*,
      memory/stores/, and gateway/.
    - Connects upward to brainparts/ (root) and downward to diencephalon/ and
      telencephalon/.
"""