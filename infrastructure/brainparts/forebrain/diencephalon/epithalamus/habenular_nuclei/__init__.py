"""
Package: infrastructure.brainparts.forebrain.diencephalon.epithalamus.habenular_nuclei
Anatomical Role:
    The habenular nuclei are a pair of small, evolutionarily ancient
    epithalamic structures flanking the third ventricle, positioned at the
    dorsal-caudal pole of the diencephalon. Each hemisphere's habenula
    contains two subdivisions:
        - Lateral habenula (LHb): the dominant subdivision in primates.
          Encodes negative reward prediction error ("worse than expected"),
          disappointment, and aversion. Inhibits midbrain dopamine (VTA,
          substantia nigra pars compacta) and activates serotonergic raphe.
          This is the brain's core "anti-reward" pathway.
        - Medial habenula (MHb): smaller, cholinergic and substance-P
          rich. Projects via the fasciculus retroflexus to the
          interpeduncular nucleus. Implicated in nicotine withdrawal,
          avoidance learning, and anxiety-like states.
    The habenular complex is the primary limbic-to-midbrain relay for
    aversive signaling: it receives limbic forebrain afferents (via the
    stria medullaris) and projects back to dopamine and serotonin centers
    (via the fasciculus retroflexus).

Functional Mode:
    - Negative reward prediction error: LHb fires when outcomes are worse
      than predicted; this suppresses VTA/SNc dopamine and biases behavior
      toward avoidance, re-evaluation, and behavioral inhibition.
    - Aversive salience and behavioral suppression: sustained LHb activity
      produces learned helplessness-like states; chronic hyperactivity is
      implicated in major depression.
    - Reward-downshift signaling: LHb encodes the *omission* or *reduction*
      of expected reward, not just punishment.
    - Nicotine/avoidance (MHb): MHb-interpeduncular axis mediates nicotine
      withdrawal aversion and some forms of avoidance learning.
    - Anti-reward feedback loop: low dopamine → LHb activation → further
      dopamine suppression. This loop is the mechanistic core of the
      region's role in mood regulation.

Hormonal Modulation (parent-level summary; per-hemisphere wiring in children):
    - Dopamine (low DA → LHb activation; LHb activation → further DA
      suppression): the defining feedback loop.
    - Serotonin (raphe → habenula; habenula → raphe): bidirectional
      serotonergic modulation.
    - GABA (habenula → VTA/raphe inhibition): LHb output is glutamatergic
      to inhibitory interneurons, producing net inhibition of dopamine
      neurons.
    - Norepinephrine: modulates LHb excitability under stress.
    - Opioids: kappa-opioid signaling in LHb contributes to aversive
      states.
    - Substance P (MHb): primary neurotransmitter of the MHb-IPN axis.
    Full per-hemisphere wiring is documented in left/ and right/.

Memory Interfaces (parent-level summary):
    - Reads: reinforcement_value_based_learning (negative-outcome history),
      emotional_valence (aversive tags).
    - Writes: emotional_valence (negative tags on disappointing or
      aversive outcomes).
    - Does not write to episodic or semantic stores directly; it tags
      episodes with negative valence, which the hippocampus and cortex
      then consolidate.
    Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Parent-level fragment (applied after the epithalamus fragments,
      before any hemisphere-specific fragment):
        "Aversive salience channel active. Negative reward prediction
         error: [none / mild / strong]. If non-zero, weight loss-framing
         over gain-framing, flag risk, and reduce exploratory language.
         If strong, suppress approach-oriented output and prioritize
         harm-avoidance framing."
    - The left/ and right/ children may append hemisphere-specific
      fragments (see lateralization note below). The parent fragment is
      always present when the habenular channel is active.

Children (both are the FIRST-LEAF PATTERN EXEMPLAR — write these next):
    - left/    ★ Left habenular nucleus. Full template (role + hormones +
                 memory + model fragment). Written first; establishes the
                 leaf pattern for all remaining ~350 Tier 1/2 files.
    - right/   ★ Right habenular nucleus. Parallel to left/, differing
                 only in the lateralization paragraph and (if adopted)
                 a hemisphere-specific model fragment.

    Lateralization note (design choice, not established neuroscience):
      The functional difference between left and right habenula in humans
      is genuinely uncertain. Some imaging work suggests right-LHb
      dominance in negative affect and left-LHb involvement in reward
      downshift; other studies find no reliable lateralization. For this
      project, the left/right split is retained because it mirrors the
      anatomical tree, but the two child files may share most content.
      Recommended convention: document left/ fully; make right/ a
      one-paragraph delta that states "same as left/ except ..." unless
      you have a specific reason to differentiate. Do not fabricate
      lateralization claims the literature does not support.

Notes:
    - Parent/container file: do not duplicate full child wiring. The
      detailed hormone levels, memory schemas, and model fragments live
      in left/ and right/.
    - MHb vs LHb distinction lives *inside* each hemisphere's file, not
      as separate tree nodes. The tree splits by hemisphere, not by
      subdivision; document both subdivisions within left/ and right/.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, serotonin, GABA, norepinephrine,
      opioids), chemicals_hormones/01_* (substance P adjacent), memory/
      stores/ (reinforcement_value_based_learning, emotional_valence),
      and gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * habenular_nuclei/left+right ↔
          midbrain/tegmentum/ventral_tegmental_area (via fasciculus
          retroflexus → interpeduncular nucleus → VTA; indirect)
        * habenular_nuclei/left+right ↔
          midbrain/tegmentum/substantia_nigra/left|right/pars_compacta
        * habenular_nuclei/left+right ↔
          hindbrain/metencephalon/pons/tegmentum/dorsal_raphe_nucleus
          (habenulo-raphe pathway)
        * habenular_nuclei/left+right ↔
          epithalamus/stria_medullaris/left|right (primary afferent
          conduit from septal/preoptic/hypothalamic regions)
    - Connects upward to epithalamus/ and downward to left/ and right/.
"""