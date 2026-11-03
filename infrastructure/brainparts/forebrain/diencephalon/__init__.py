"""
Package: infrastructure.brainparts.forebrain.diencephalon
Anatomical Role:
    The diencephalon ("between-brain") is the central forebrain division
    situated between the midbrain and the telencephalon, surrounding the
    third ventricle. It contains the brain's primary relay, homeostatic,
    and endocrine structures. It is the single densest convergence point
    for the 12 hormone axes documented in chemicals_hormones/: nearly every
    axis either originates, terminates, or is modulated by a diencephalic
    structure.

Functional Mode:
    - Endocrine orchestration: hypothalamus → pituitary cascades drive all
      12 axes (HPA, HPG, metabolic/thyroid, satiety, social, fluid/
      electrolyte, immune, circadian, and the structural anchors).
    - Sensory and motor relay: thalamus gates all sensory input except
      olfaction to the cortex, and relays cortico-subcortical motor loops.
    - Circadian and seasonal timing: pineal gland (melatonin) and
      suprachiasmatic nucleus anchor biological time.
    - Aversive/reward salience gating: habenular nuclei encode negative
      reward prediction error and project to midbrain dopamine centers.
    - Motor modulation: subthalamic nucleus participates in the basal
      ganglia indirect pathway; zona incerta is a broad modulatory hub.

Hormonal Modulation (diencephalon-wide summary):
    - This is the endocrine interface of the brain. CRH, TRH, GnRH,
      dopamine (as prolactin inhibitor), oxytocin, vasopressin, and
      somatostatin are released here; ACTH, TSH, GH, LH, FSH, prolactin,
      ADH, oxytocin, and melatonin are secreted by diencephalic glands.
    - Detailed per-region modulation lives in each child package's
      __init__.py (hypothalamus, pituitary_gland, epithalamus/*,
      thalamus/*). Do not duplicate here.

Memory Interfaces (diencephalon-wide summary):
    - Reads: episodic (homeostatic history), emotional_valence (stress
      history, aversive tags), temporal_sequence_learning (circadian
      context), reinforcement_value_based_learning (negative outcome
      history for habenula).
    - Writes: hormonal state vector (not a memory store per se, but the
      state that regions read); emotional_valence (habenula aversive tags).
    - Full store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Diencephalon is where the *state block* of the system prompt is
      assembled: current hormone levels, circadian phase, homeostatic
      drive, and aversive/reward salience. This block precedes the
      cortical reasoning layer.
    - Diencephalon-level prompt preamble (applied once per inference,
      after the forebrain preamble):
        "Current internal state — hormone axes: [HPA, HPG, metabolic,
         satiety, social, fluid, immune, circadian]. Circadian phase:
         [day/night]. Homeostatic drive: [hunger, thirst, temperature,
         arousal]. Salience: [reward/aversion balance from habenula].
         Use this state to bias reasoning: high cortisol → prioritize
         threat detection; high melatonin → reduce verbosity; high
         ghrelin → surface food-seeking priorities."
    - Children append their own regional fragments after this block.

Children (Stage 1 hubs marked with ★):
    - hypothalamus/          ★ Master homeostatic and endocrine regulator.
                                Parent of pituitary control; origin of CRH,
                                TRH, GnRH, dopamine, oxytocin, vasopressin.
    - pituitary_gland/       ★ Endocrine effector; secretes ACTH, TSH, GH,
                                LH, FSH, prolactin, ADH, oxytocin, melatonin
                                precursors (via pineal).
    - thalamus/left/         ★ Sensory and motor relay (all modalities except
      thalamus/right/           olfaction; cortico-thalamo-cortical loops).
    - epithalamus/             Pineal gland (melatonin, circadian), habenular
                                nuclei (aversion, negative RPE), stria
                                medullaris, taenia thalami.
    - subthalamus/             Subthalamic nucleus (basal ganglia indirect
                                pathway), zona incerta (modulatory hub).
    - subcommissural_organ/    Circadian-adjacent secretory organ (TGF-β,
                                involved in CSF flow regulation).
    - third_ventricle/         CSF space (Tier 4 — structural only; no
                                direct hormonal or memory role).

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each child package owns its own specification.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/02_* (HPA), chemicals_hormones/05_* (monoamines),
      chemicals_hormones/10_* (circadian), memory/stores/, and gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * hypothalamus ↔ pituitary_gland (via pituitary_stalk / infundibulum)
        * habenular_nuclei/left/right ↔ midbrain/tegmentum/ventral_tegmental_area
        * thalamus/* ↔ telencephalon/.../cortex/* (thalamo-cortical loops)
        * suprachiasmatic_nucleus ↔ pineal_gland (via sympathetic chain;
          indirect but canonical)
    - Connects upward to forebrain/ and downward to each child package.
"""