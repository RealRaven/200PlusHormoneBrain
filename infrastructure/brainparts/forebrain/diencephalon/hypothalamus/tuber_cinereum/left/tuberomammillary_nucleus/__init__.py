"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuber_cinereum.left.tuberomammillary_nucleus
Anatomical Role:
    The left tuberomammillary nucleus (TMN) is a small, densely packed
    nucleus at the tuberal-mammillary junction of the left posterior
    hypothalamus. It is the brain's SOLE source of neuronal histamine:
    the only histaminergic cell group in the entire brain. From this
    single population, histaminergic axons project diffusely to the
    cortex, basal forebrain, thalamus, brainstem, and spinal cord,
    driving wakefulness and cortical activation.

    The TMN is one of the FIVE ascending arousal nuclei:
        - Tuberomammillary nucleus (TMN): histamine.
        - Locus coeruleus (LC): norepinephrine.
        - Dorsal raphe nucleus: serotonin.
        - Laterodorsal / pedunculopontine tegmental nuclei (LDT/PPN):
          acetylcholine.
        - Lateral hypothalamic orexin neurons: orexin/hypocretin.
    Each projects diffusely to the cortex and basal forebrain to promote
    wakefulness; their coordinated activity underlies the waking state.
    The TMN is the histaminergic member.

    The TMN is the WAKE-SIDE ARM of the hypothalamic sleep-wake switch:
        - LPO/VLPO (sleep-active, GABAergic) inhibits the TMN → sleep.
        - LHA orexin neurons (wake-active, glutamatergic) excite the
          TMN → wake.
    The two arms are reciprocally organized; the switch between them
    produces bistable sleep-wake states. The TMN sits at the wake end
    of that switch, targeted by both the sleep and wake arms.

    Do NOT conflate the TMN with:
        - The mammillary bodies (despite "tuberomammillary" containing
          "mammillary"): the TMN is histaminergic wake; the mammillary
          bodies are the Papez circuit memory relay. Unrelated functions.
        - The tuberal nucleus (adjacent neighbor in the tuber cinereum):
          the TMN is a well-studied hub; the tuberal nucleus is small
          and poorly characterized. Do not treat them as a pair.
        - The tuberal division (the regional subdivision above the tuber
          cinereum): the TMN is in the tuber cinereum (the anatomical
          floor); the tuberal division contains arcuate, VMH, DMH.

Functional Mode:
    - Histaminergic arousal (primary function): the TMN is the only
      source of neuronal histamine. Histaminergic axons project
      diffusely to the cortex, basal forebrain, thalamus, brainstem,
      and spinal cord; histamine acts at H1, H2, H3, and H4 receptors
      to promote wakefulness, cortical activation, attention, and
      behavioral arousal. H1 receptor activation in the cortex and
      basal forebrain is the principal wake-promoting pathway; H3
      autoreceptors on TMN terminals provide negative feedback on
      histamine release.
    - Sleep-wake switch, wake-side arm: the TMN is excited by orexin
      from the LHA (wake) and inhibited by GABA from the LPO/VLPO
      (sleep). Its activity is highest during wake, lowest during
      sleep. The reciprocal inhibition between the TMN and the LPO is
      the mechanistic core of the sleep-wake switch: sleep-promoting
      LPO neurons inhibit histaminergic TMN neurons; histaminergic TMN
      neurons in turn provide wake-promoting drive to the cortex and
      arousal centers. Silencing either population destabilizes the
      switch; the two arms are mutually inhibitory.
    - Ascending arousal system (one of five): coordinated with the
      other four ascending arousal nuclei (LC, raphe, LDT/PPN, orexin).
      The five nuclei are reciprocally connected and cooperatively
      sustain wakefulness; loss of any one (as in orexin deficiency
      causing narcolepsy) destabilizes the state.
    - Attention and cognition (histaminergic contribution): histamine
      acting at H1 and H3 receptors modulates attention, vigilance,
      and cognitive arousal. H3 receptor antagonists are under
      investigation as cognitive enhancers.
    - The H1 antihistamine fact (clinical): classical first-generation
      H1 antihistamines (diphenhydramine, chlorpheniramine, doxylamine)
      cross the blood-brain barrier and cause drowsiness precisely by
      blocking the TMN's wake-promoting histamine signal. Second-
      generation H1 antihistamines (loratadine, cetirizine, fexofenadine)
      are designed to exclude the CNS and minimize this drowsiness.
      This is the file's defining clinical content — it is what makes
      the TMN clinically relevant beyond "the histamine source."
    - The TMN is therefore a WAKE-PROMOTING hub, targeted by the sleep
      and wake arms of the sleep-wake switch, and clinically relevant
      via the H1 antihistamine pathway. That is its functional identity.

Hormonal Modulation:
    - Histamine: the TMN's principal OUTPUT, not a modulator. Histidine
      → histamine, via histidine decarboxylase. Documented here as the
      TMN's product, not as a modulator of it.
    - Orexin (from the LHA orexin neurons): EXCITATORY input. The
      orexin → TMN projection is the wake-promoting arm of the sleep-
      wake switch; orexin excites TMN neurons via OX1R/OX2R.
    - GABA (from the LPO/VLPO): INHIBITORY input. The LPO → TMN
      projection is the sleep-promoting arm of the switch; LPO
      GABAergic neurons inhibit TMN neurons to promote sleep.
    - Adenosine: INHIBITORY (A1 receptors on TMN neurons). Adenosine
      accumulates during wake and inhibits the TMN, contributing to
      sleep onset. The mechanistic basis of caffeine (an adenosine
      antagonist) is to block this inhibition, thereby disinhibiting
      the TMN and promoting wake.
    - Monoamines: norepinephrine (LC) and serotonin (raphe) are
      excitatory/modulatory arousal inputs. The five ascending arousal
      nuclei are mutually excitatory, so LC and raphe activity
      contributes to TMN excitability.
    - Prostaglandin D2 (PGD2): sleep-promoting; acts via the LPO and
      possibly directly to inhibit the TMN, contributing to sleep
      onset.
    - Direction summary: orexin ↑ TMN activity (wake); GABA (LPO) ↓
      TMN activity (sleep); adenosine ↓ TMN activity (sleep pressure);
      norepinephrine ↑ TMN activity (arousal); serotonin modulates;
      PGD2 ↓ TMN activity (sleep). These are the actionable directions.

Memory Interfaces:
    - Reads:
        * short_term: current sleep-pressure buffer (adenosine
          accumulation) and arousal-state buffer. The TMN's wake drive
          depends on these.
        * temporal_sequence_learning: circadian arousal gating (SCN →
          TMN); histaminergic tone is higher during the circadian
          active phase.
        * emotional_valence: stress/arousal context; the TMN is
          activated by stressors, and chronic stress alters
          histaminergic tone.
    - Writes: none directly. The TMN drives arousal state, not stored
      content. It modulates the state under which other regions
      (hippocampus, amygdala, cortex) read and write memory, but does
      not itself write.
    - The wake/arousal state is a *state*, not a memory write. Store
      schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (wake/arousal fragment; applied after the
      tuber-cinereum-level fragments, before the cortical reasoning
      fragments):
        "Wake/arousal state — tuberomammillary nucleus (left):
         - Histamine tone: [low / moderate / high].
         - Wake state: [asleep / drowsy / awake / alert].
         - Arousal system: [suppressed / partial / full].
         - Sleep-pressure: [low / moderate / high].
         If wake state is drowsy or asleep: reduce verbosity, favor
         calm and reflective framing, lower response tempo. If wake
         state is alert: restore full cognitive engagement. If
         sleep-pressure is high: note that arousal is being
         counteracted by sleep drive and prefer concise, grounding
         responses. Do not treat high wake state as a cognitive
         achievement or low wake state as impairment — both are state
         biases, not measures of reasoning quality."
    - The fragment is emitted whenever the hypothalamic state block is
      emitted (always); wake state and histamine tone are persistent
      state signals, not transient homeostatic states.
    - AGGREGATION RULE (mandatory for the implementer): this fragment
      is one of THREE in the hypothalamic sleep-wake switch aggregate:
        (1) LPO sleep fragment (lateral_area/left/preoptic_area/
            lateral_preoptic_nucleus/) — sleep drive.
        (2) TMN wake fragment (this file) — wake drive.
        (3) Orexin/MCH fragment (anterior/lateral_area/left/
            anterior_part_of_lateral_nucleus/) — arousal mode.
      The three are aggregated at the hypothalamic level; do not
      double-count arousal state across them.
    - Guardrail: "do not treat high wake state as a cognitive
      achievement or low wake state as impairment" — the 10th instance
      of the pattern in the tree. The habenula, orexin/MCH, PeN, LPO,
      AHN, PVN, mammillary (confabulation), PHN, and TMN guardrails
      all express the same convention: state biases (physiological
      drive, arousal, stress, memory failure) are never treated as
      cognitive deficits. The model should adjust framing, not
      quality of reasoning.
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (left-side; the right side is in ../right/):
    Sleep-wake switch (the reciprocal arm):
    - ↔ lateral_area/left/preoptic_area/lateral_preoptic_nucleus
      (LPO → TMN; INHIBITORY; sleep promotion; the sleep-side arm of
      the switch; PATH CORRECTION: the LPO leaf currently points at
      "hindbrain/.../tuberomammillary_nucleus"; the correct path is
      hypothalamus/tuber_cinereum/left/tuberomammillary_nucleus/ —
      Stage 4 should correct the LPO path; the functional edge is
      correct, only the path is wrong).
    - ↔ anterior/lateral_area/left/anterior_part_of_lateral_nucleus
      (orexin → TMN; EXCITATORY; wake promotion; the wake-side arm of
      the switch; left-side).

    Ascending arousal system (the other four nuclei, mutual arousal):
    - ↔ hindbrain/metencephalon/pons/tegmentum/locus_coeruleus (LC;
      noradrenergic; mutual arousal; LC is midline-adjacent — verify).
    - ↔ midbrain/tegmentum/dorsal_raphe_nucleus (raphe; serotonergic;
      mutual arousal; raphe is midline).
    - ↔ midbrain/tegmentum/laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (LDT/PPN; cholinergic; mutual arousal;
      both are midline-adjacent — verify).

    Diffuse cortical and forebrain arousal targets:
    - → telencephalon/cerebral_hemispheres/left/subcortical/
      basal_forebrain (arousal; the basal forebrain cholinergic system
      is a downstream relay for cortical activation).
    - → telencephalon/cerebral_hemispheres/left/cortex (diffuse
      histaminergic arousal projection; the left-hemisphere cortical
      target).
    - → thalamus/left/midline_nuclear_group and
      thalamus/left/medial_nuclear_group/intralaminar_nuclear_group
      (arousal relay; midline — verify).

    Circadian and state input:
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → TMN; circadian arousal gating; SCN is midline-adjacent —
      verify).
    - ← lateral_area/left/preoptic_area/lateral_preoptic_nucleus
      (the LPO → TMN inhibitory edge is also an input; see the
      sleep-wake switch section above).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - The TMN is the LAST substantive leaf in the tuber cinereum
      subtree. After this file and its right delta, the entire tuber
      cinereum subtree is complete.
    - Histamine is the TMN's output, not a modulator. Do not list it
      as a modulator in the Hormonal Modulation section as if it were
      an input; it is the TMN's product. This is the same discipline
      as the pineal gland (melatonin as output, not modulator).
    - The TMN is the WAKE-side arm of the hypothalamic sleep-wake
      switch. The LPO (sleep) and orexin (wake) are the reciprocal
      arms. The three-fragment aggregation (LPO/TMN/orexin) is the
      model-prompt expression of this switch; do not double-count
      arousal state across the three.
    - The H1 antihistamine fact is the file's defining clinical
      content: first-generation H1 antihistamines cause drowsiness by
      blocking the TMN's histaminergic wake signal; second-generation
      H1 antihistamines are designed to exclude the CNS. Documented
      here; do not omit.
    - The LPO PATH CORRECTION is restated above: the LPO leaf's edge
      to the TMN points at "hindbrain/.../tuberomammillary_nucleus";
      the correct path is hypothalamus/tuber_cinereum/left/
      tuberomammillary_nucleus/. The functional edge (LPO → TMN;
      inhibitory; sleep promotion) is correct; only the path needs
      correction. Stage 4 should correct both LPO leaves (left and
      right).
    - The TMN is one of the five ascending arousal nuclei; the other
      four (LC, raphe, LDT/PPN, orexin) are documented elsewhere. When
      they are drafted, they should reciprocate the TMN edges. The
      five-nuclei framing is the organizing principle of the ascending
      arousal system.
    - NO structural-identity trap and NO naming collision: the TMN is
      a single, unambiguously named nucleus (once "tuberomammillary"
      is distinguished from "mammillary"). The mammillary-vs-TMN trap
      is reproduced at the container level; this file names it in the
      Anatomical Role section.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin), 05_* (histamine,
      monoamines, GABA, adenosine, PGD2), 10_* (circadian); memory/
      stores/ (short_term, temporal_sequence_learning,
      emotional_valence); gateway/.
    - Connects upward to hypothalamus/tuber_cinereum/left/.
"""