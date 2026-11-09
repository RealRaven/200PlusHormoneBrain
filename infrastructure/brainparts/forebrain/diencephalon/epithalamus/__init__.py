"""
Package: infrastructure.brainparts.forebrain.diencephalon.epithalamus
Anatomical Role:
    The epithalamus is the most dorsal and caudal division of the
    diencephalon, sitting above the thalamus and bordering the third
    ventricle. It is a small but functionally distinct cluster: a
    secretory endocrine organ (pineal gland) and a pair of lateralized
    limbic-midbrain relay nuclei (habenular nuclei), connected by
    fiber tracts (stria medullaris, taenia thalami). It is the brain's
    primary interface for circadian timing (pineal) and aversive/reward-
    prediction-error signaling (habenula).

Functional Mode:
    - Circadian and seasonal timing: pineal gland secretes melatonin
      in response to suprachiasmatic (SCN) signaling via the sympathetic
      chain; melatonin gates sleep/wake, seasonal physiology, and
      reproductive timing.
    - Aversive salience and negative reward prediction error: the
      habenular nuclei (especially the lateral habenula) encode
      disappointment and aversion, and inhibit midbrain dopamine
      (VTA, substantia nigra) when outcomes are worse than expected.
      This is the core "anti-reward" pathway.
    - Limbic-to-midbrain relay: the stria medullaris carries septal,
      preoptic, and hypothalamic afferents into the habenula, which
      then projects (via the fasciculus retroflexus) to the midbrain
      interpeduncular nucleus and dopaminergic centers.
    - CSF-adjacent modulation: the epithalamus borders the third
      ventricle and contributes to its dorsal boundary; it is not
      a CSF-producing structure itself.

Hormonal Modulation (epithalamus-wide summary):
    - Pineal gland: melatonin (output); modulated by norepinephrine
      (SCN → sympathetic → pineal) and light input. Serotonin is the
      immediate precursor.
    - Habenular nuclei: modulated by dopamine (low DA → lateral
      habenula activation, forming a negative feedback loop), serotonin
      (raphe → habenula), and GABA (habenula → VTA/raphe inhibition).
      Lateral habenula is also modulated by opioids and stress hormones.
    - Detailed per-region wiring lives in the child packages
      (pineal_gland/, habenular_nuclei/left/, habenular_nuclei/right/).

Memory Interfaces (epithalamus-wide summary):
    - Pineal gland: reads temporal_sequence_learning (time-of-day
      context); writes nothing (it modulates timing, not content).
    - Habenular nuclei: reads reinforcement_value_based_learning
      (negative-outcome history) and emotional_valence (aversive tags);
      writes emotional_valence (negative tags on disappointing outcomes).
    - Fiber tracts (stria medullaris, taenia thalami): no direct
      memory interface — they are conduits, documented in their own
      files as Tier 3.

Model Integration (Gemma-4-E2B):
    - Epithalamus contributes two distinct fragments to the system
      prompt, applied after the diencephalon state block:
        (1) Circadian fragment (pineal):
            "Circadian phase: [night/day]. Melatonin level: [low/moderate/
             high]. If high, reduce verbosity, favor reflective or
             sleep-adjacent framing; if low, restore full cognitive
             engagement."
        (2) Aversive salience fragment (habenula):
            "Negative reward prediction error: [active/inactive].
             Aversion signal strength: [0-1]. If active, suppress
             approach-oriented language, flag risk, and weight
             loss-framing over gain-framing."
    - The two fragments are independent; one can be active without
      the other.

Children (tiers marked):
    ★ Tier 1/2 — cross-layered hub (FIRST-LEAF PATTERN EXEMPLAR):
    - habenular_nuclei/          Parent. Documents left/right
      ├── left/                  ★ Left lateral habenula — encodes
      │                             negative reward prediction error;
      │                             first file to write as the pattern
      │                             exemplar for all remaining leaves.
      └── right/                 ★ Right lateral habenula — same role,
                                    lateralized; document parallel to
                                    left/ to prove the L/R pattern.

    Tier 2 — secretory organ (organ-level, single file):
    - pineal_gland/              Melatonin output; circadian endocrine
                                 effector. Hormone role is primary here.

    Tier 3 — fiber tracts (structural only, no hormone/memory sections):
    - stria_medullaris/          Conduit: septal/preoptic/hypothalamic
      ├── left/                  afferents → habenula. Tier 3 template:
      └── right/                 role only.
    - taenia_thalami/            Conduit: dorsal thalamic surface to
      ├── left/                  habenula. Tier 3 template: role only.
      └── right/

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each child owns its own specification.
    - The habenular nuclei are designated the FIRST-LEAF PATTERN
      EXEMPLAR: after this container is written, the very next files
      should be habenular_nuclei/left/__init__.py and
      habenular_nuclei/right/__init__.py, fully written. Their template
      (role + hormones + memory + model fragment) becomes the shape
      that every Tier 1/2 leaf downstream will follow.
    - Fiber tracts (stria_medullaris, taenia_thalami) are explicitly
      Tier 3: role-only docstrings. Do not force hormone or memory
      sections onto them.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, serotonin, GABA,
      norepinephrine), chemicals_hormones/10_* (melatonin, circadian),
      memory/stores/ (reinforcement_value_based_learning,
      emotional_valence, temporal_sequence_learning), and gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * habenular_nuclei/left+right ↔
          midbrain/tegmentum/ventral_tegmental_area (via fasciculus
          retroflexus → interpeduncular nucleus → VTA; indirect but
          canonical)
        * habenular_nuclei/left+right ↔
          hindbrain/metencephalon/pons/tegmentum/dorsal_raphe_nucleus
          (habenulo-raphe pathway)
        * pineal_gland ↔
          hypothalamus/anterior/medial_area/left|right/
          suprachiasmatic_nucleus (SCN → sympathetic → pineal; indirect)
    - Connects upward to diencephalon/ and downward to each child
      package.
"""