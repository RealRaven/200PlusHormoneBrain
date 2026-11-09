"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.anterior_hypothalamic_nucleus
Anatomical Role:
    The left anterior hypothalamic nucleus (AHN) is a small, densely
    packed nucleus in the medial anterior hypothalamus, situated between
    the preoptic area rostrally and the ventromedial/paraventricular
    region caudally. It is a principal hypothalamic controller of
    parasympathetic outflow and thermoregulation, and it participates in
    cardiovascular and osmoregulatory control. It is not a
    neurosecretory nucleus: its outputs are neural projections to
    brainstem autonomic centers, not hormones.

    The AHN is functionally adjacent to and partly overlapping with the
    preoptic thermoregulatory circuitry (preoptic_area/), but it is a
    distinct nucleus with a distinct projection profile. Do not merge
    with preoptic_area/.

Functional Mode:
    - Parasympathetic outflow: the AHN drives parasympathetic
      preganglionic neurons in the dorsal motor nucleus of the vagus
      (DMV) and the nucleus ambiguus (NA), promoting rest-and-digest
      functions (slowed heart rate, increased gastric motility,
      pupil constriction, salivation).
    - Thermoregulation: the AHN contributes to heat-conservation and
      heat-dissipation responses, complementing the preoptic
      thermoregulatory circuitry. Activation drives autonomic and
      behavioral thermoregulatory effects.
    - Cardiovascular control: the AHN modulates heart rate and blood
      pressure via projections to the nucleus tractus solitarius (NTS)
      and the rostroventrolateral medulla (RVLM), and via direct
      projections to spinal sympathetic/parasympathetic preganglionic
      neurons.
    - Osmoregulatory contribution: the AHN contributes to fluid-balance
      responses via projections to the supraoptic and paraventricular
      nuclei, complementing the osmosensory circuitry of the OVLT/SFO.
    - Behavioral arousal (minor): the AHN's projections to the
      hypocretin/orexin region of the lateral hypothalamus contribute a
      minor arousal-modulation role, but this is not the primary
      function. Document as a supporting role, not the anchor.

Hormonal Modulation:
    - Angiotensin II: excitatory input (via the subfornical organ and
      OVLT); angiotensin II activates the AHN as part of the central
      osmoregulatory/volume-control circuit.
    - Atrial natriuretic peptide (ANP): inhibitory input; opposes
      angiotensin II action in the AHN.
    - Prostaglandin E2 (PGE2): activates thermoregulatory circuits
      including the AHN; the endogenous pyrogen pathway for fever.
    - Estradiol: modulates thermoregulatory and autonomic function;
      estrogen withdrawal (menopause) produces hot flushes via
      preoptic/AHN circuitry.
    - Thyroid hormones: modulate thermoregulatory set-point, indirectly
      via the preoptic/AHN circuits.
    - GABA, glutamate: intrinsic modulatory transmitters.
    - Direction summary: angiotensin II ↑ AHN activity (volume
      depletion), ANP ↓ AHN activity, PGE2 ↑ thermoregulatory drive,
      estradiol withdrawal ↑ thermal disruption. These directions are
      the actionable content; do not omit them.
    - The AHN is primarily an autonomic *output* nucleus, not a target
      of most of the 12 axes. Its hormonal inputs are concentrated in
      the fluid axis (chemicals_hormones/07_*) and the thermoregulatory
      subset of the metabolic axis. Document it as an autonomic effector
      for these axes, not as a whole-endocrine target.

Memory Interfaces:
    - Reads:
        * short_term: current autonomic state (sympathetic/parasympathetic
          balance) and thermal state buffers.
        * episodic: past thermoregulatory and autonomic events (fever
          history, volume-depletion episodes, hot-flush history), used
          to set response thresholds.
        * emotional_valence: stress/arousal context; sympathetic
          activation is modulated by limbic input.
        * temporal_sequence_learning: time-of-day context; autonomic
          tone has a circadian component driven by the SCN.
    - Writes: none directly. The AHN emits neural autonomic commands,
      not stored content. It contributes to the homeostatic state
      vector via autonomic tone and thermoregulatory output.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (applied after the medial_area-level fragments,
      before the cortical reasoning fragments):
        "Autonomic state — anterior hypothalamic nucleus (left):
         - Thermal state: [comfortable / hot / cold].
         - Autonomic tone: [parasympathetic-dominant / balanced /
           sympathetic-dominant].
         - Volume state: [euvolemic / hypovolemic / hypervolemic].
         - Fever context: [none / low-grade / febrile].
         If thermal state is hot: acknowledge heat discomfort and prefer
         cooling-oriented language. If sympathetic-dominant: flag
         hyperarousal context and prefer grounding, slow-tempo framing.
         If parasympathetic-dominant: prefer calm, restorative framing.
         If febrile: acknowledge discomfort, reduce extraneous output,
         and prefer rest-adjacent tone. Do not treat
         sympathetic-dominance as impairment — it is a state bias, not a
         cognition deficit."
    - AGGREGATION RULE (mandatory for the implementer): this fragment
      is a *constituent input* to the anterior-division thermoregulatory/
      autonomic fragment, which also aggregates the preoptic
      contribution (lateral_area/left/preoptic_area/lateral_preoptic_nucleus/
      and medial_area/left/preoptic_area/). Do not emit this fragment
      as an independent un-aggregated state block — that would
      double-count the autonomic/thermal signal. Aggregate at the
      anterior-division level before injection.
    - The fragment is otherwise emitted whenever the anterior-division
      thermoregulatory/autonomic fragment is emitted.
    - Guardrail: "do not treat sympathetic-dominance as impairment" —
      consistent with the habenula, orexin/MCH, PeN, and LPO
      conventions.

Reciprocal Connections (enforce in Stage 4 audit):
    - → hindbrain/myelencephalon/medulla_oblongata/cranial_nerve_nuclei/
      left/dorsal_motor_nucleus_vagus (parasympathetic outflow;
      excitatory; rest-and-digest).
    - → hindbrain/myelencephalon/medulla_oblongata/cranial_nerve_nuclei/
      left/nucleus_ambiguus (parasympathetic outflow; excitatory;
      cardiac and respiratory control).
    - → hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
      (NTS; reciprocal autonomic feedback; NTS is midline-adjacent —
      verify).
    - → hindbrain/myelencephalon/medulla_oblongata/rostral_ventrolateral_medulla
      (RVLM; inhibitory; reduces sympathetic outflow; RVLM is
      midline-adjacent — verify).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      angiotensin II input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input;
      SFO is midline).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN; circadian autonomic gating).
    - ↔ hypothalamus/anterior/medial_area/left/supraoptic_nucleus
      (osmoregulatory cross-talk; AHN modulates SON activity).
    - ↔ hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (autonomic co-regulation; PVN is the other major forebrain
      autonomic controller).
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area
      (thermoregulatory co-regulation; distinct but interacting).

Notes:
    - Tier 1 leaf (left). Full template. right/ is a delta.
    - NO structural-identity trap: AHN is a single nucleus in this tree.
      Do not invent a structural-identity warning.
    - NO naming collision: unlike the preoptic area and SON, "anterior
      hypothalamic nucleus" is unambiguous in this tree. Do not
      reproduce a warning that doesn't exist.
    - DISTINCTION FROM PREOPTIC AREA: AHN is adjacent to but distinct
      from preoptic_area/. They share thermoregulatory function but are
      separate nodes. The reciprocal edge declares the co-regulation;
      the tree keeps them distinct.
    - The AHN is primarily autonomic output; its hormonal inputs are
      concentrated in the fluid axis and thermoregulatory subset.
      Do not overstate its endocrine role.
    - The aggregation rule for the thermoregulatory/autonomic fragment
      is mandatory: aggregate with the preoptic contributions before
      emission.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/03_* (thyroid), 07_* (fluid, angiotensin II,
      ANP), 05_* (GABA, glutamate, PGE2 adjacent to monoamines); memory/
      stores/; gateway/.
    - Connects upward to hypothalamus/anterior/medial_area/left/.
"""