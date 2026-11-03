"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.left.preoptic_area.lateral_preoptic_nucleus
Anatomical Role:
    The left lateral preoptic nucleus (LPO) is the sleep-promoting nucleus
    of the preoptic area. It contains two functionally related but
    anatomically distinct sleep-active cell groups:
        - Ventrolateral preoptic nucleus (VLPO): a cluster of
          sleep-active GABAergic and galaninergic neurons in the
          ventrolateral preoptic area, adjacent to the lateral edge of
          the LPO. VLPO neurons fire during non-REM and REM sleep and
          are silent during wake.
        - Median preoptic nucleus (MnPO, distinct from the "median
          preoptic nucleus" of the medial preoptic area documented
          elsewhere in this tree — see DISTINCTION below): a
          sleep-active GABAergic population that fires during sleep and
          contributes to sleep onset and maintenance.

    Both populations project to and inhibit every major arousal system
    in the brain (see Reciprocal Connections). This reciprocal inhibition
    is the mechanistic core of the sleep switch: the LPO and the arousal
    systems mutually inhibit each other, producing bistable sleep-wake
    states.

    DISTINCTION FROM MEDIAL PREOPTIC AREA: this node is in the LATERAL
    preoptic area. It is distinct from
    medial_area/left/preoptic_area/medial_preoptic_nucleus/ (the medial
    preoptic nucleus, MPN, involved in maternal behavior, sexual
    behavior, and GnRH regulation). Do not merge. The preoptic naming
    collision applies here.

    DISTINCTION FROM PeN: the periventricular preoptic nucleus
    (periventricular_preoptic_nucleus/, documented separately) is a
    different preoptic sleep-promoting population. The LPO/VLPO and the
    PeN are the two sleep-active preoptic populations in this tree; they
    are adjacent and partly overlapping in function, but distinct nodes.
    Do not merge.

Functional Mode:
    - Sleep promotion (the primary function): LPO/VLPO GABAergic and
      galaninergic neurons fire during sleep and inhibit:
        * histaminergic tuberomammillary neurons (TMN) → reduces
          wake-promoting histamine;
        * noradrenergic locus coeruleus (LC) → reduces arousal;
        * serotonergic dorsal raphe → reduces arousal;
        * cholinergic laterodorsal tegmental (LDT) and pedunculopontine
          (PPN) nuclei → reduces cortical activation;
        * orexin/hypocretin neurons in the LHA → reduces wake drive.
      This is the anatomical basis of the "sleep switch": mutual
      inhibition between LPO and arousal systems produces bistable
      sleep-wake states.
    - Sleep consolidation (VLPO): VLPO neurons promote non-REM sleep
      consolidation; lesion studies show VLPO lesions cause insomnia.
    - Sleep onset (MnPO): the median preoptic sleep-active neurons
      contribute to sleep onset, with a partly distinct projection
      profile from VLPO.
    - Thermoregulation: preoptic warming promotes sleep; LPO neurons
      respond to local temperature. Estrogen withdrawal (menopause)
      produces hot flushes via this circuitry, and the accompanying
      sleep disruption is the LPO/thermoregulatory cross-talk.
    - Adenosine integration: adenosine accumulates during wake and
      excites LPO neurons (via A2A receptors) while inhibiting arousal
      systems; this is the mechanistic basis of sleep pressure.

Hormonal Modulation:
    - Adenosine: the primary sleep-pressure signal. ↑ with time awake;
      excites LPO neurons and inhibits arousal systems. The functional
      basis of caffeine (an adenosine antagonist) is to block this.
    - GABA: intrinsic transmitter of LPO/VLPO neurons; promotes sleep by
      inhibiting arousal centers.
    - Galanin: co-transmitter with GABA in VLPO neurons; potentiates
      sleep-promoting inhibition of arousal systems.
    - Prostaglandin D2 (PGD2): sleep-promoting; acts via the LPO to
      promote sleep, in part through adenosine.
    - Estradiol: modulates LPO thermoregulatory and sleep circuitry;
      estrogen withdrawal produces hot flushes and sleep disruption
      (peri-menopausal and menopausal sleep complaints).
    - Orexin/hypocretin: the LPO inhibits orexin neurons, and orexin
      neurons inhibit the LPO; the reciprocal antagonism is the sleep-
      wake switch.
    - Melatonin (from pineal): modulates sleep timing via SCN and
      downstream circuits, not directly via LPO; document as indirect.
    - Circadian input from SCN: gates the sleep window, so sleep drive
      from adenosine is restricted to the circadian night.
    - Direction summary: adenosine ↑ LPO activity, GABA/galanin promote
      LPO output, PGD2 ↑ sleep, estradiol withdrawal ↑ thermal
      disruption, orexin ↓ LPO activity. These directions are the
      actionable content.

Memory Interfaces:
    - Reads:
        * short_term: current sleep-pressure buffer (adenosine
          accumulation) and thermal state buffer.
        * temporal_sequence_learning: circadian sleep window (SCN-gated),
          used to restrict sleep onset to the circadian night.
        * episodic: past sleep episodes and sleep disruption events,
          used to set sleep-pressure thresholds.
        * emotional_valence: stress-arousal context; stress suppresses
          sleep via amygdala and CRH projections to the LPO.
    - Writes:
        * Does not write episodic, semantic, or procedural content
          directly.
        * Sleep outcomes feed back into sleep-pressure set-points via
          the short_term buffer; document as modulation, not a stored
          write.
    - The sleep-wake mode is a *state*, not a memory write. Store
      schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (applied after the preoptic_area-level fragments,
      before the cortical reasoning fragments):
        "Sleep state — lateral preoptic nucleus (left):
         - Sleep drive: [0-1].
         - Adenosine pressure: [low / moderate / high].
         - Sleep-wake mode: [wake / drowsy / asleep].
         - Thermal state: [comfortable / hot / cold].
         - Arousal-system suppression: [none / partial / deep].
         If sleep drive is high or sleep-wake mode is drowsy or asleep:
         reduce verbosity, favor calm and reflective framing, lower
         response tempo, and prefer short, grounding responses over
         expansive reasoning. If thermal state is hot: acknowledge
         heat-related discomfort and prefer cooling-oriented language.
         Do not treat high sleep drive as impairment — it is a state
         bias, not a degradation of reasoning capacity. The model can
         still reason fully under high sleep drive; it should do so
         more concisely and calmly."
    - The fragment is emitted whenever the homeostatic state block is
      emitted (always), with sleep drive and sleep-wake mode as the
      primary signals.
    - Guardrail: "do not treat high sleep drive as impairment" is the
      LPO equivalent of the habenula's "does not silence reasoning"
      clause. Sleep bias is a state bias, not a cognition deficit.
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (enforce in Stage 4 audit):
    - → hindbrain/.../tuberomammillary_nucleus (LPO → TMN; inhibitory;
      GABAergic; sleep promotion via histamine suppression).
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus
      (LPO → LC; inhibitory; sleep promotion via noradrenergic
      suppression).
    - → midbrain/tegmentum/dorsal_raphe_nucleus (LPO → raphe;
      inhibitory; sleep promotion via serotonergic suppression).
    - → midbrain/tegmentum/laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (LPO → LDT/PPN; inhibitory; sleep
      promotion via cholinergic suppression).
    - → hypothalamus/anterior/lateral_area/left/
      anterior_part_of_lateral_nucleus (LPO → orexin neurons;
      inhibitory; sleep-wake switch).
    - ← hypothalamus/anterior/lateral_area/left/
      anterior_part_of_lateral_nucleus (orexin → LPO; inhibitory;
      reciprocal antagonism).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → LPO; circadian sleep gating).
    - ← hypothalamus/anterior/medial_area/left/supraoptic_nucleus and
      paraventricular_nucleus (CRH/stress → LPO; stress-induced
      insomnia pathway).
    - ↔ periventricular_preoptic_nucleus/ (adjacent sleep-active
      population; distinct nodes, interacting function).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - The preoptic naming collision applies: this is the LATERAL
      preoptic nucleus, distinct from the medial preoptic nucleus. Do
      not merge. The warning is reproduced in the Anatomical Role
      section for the same reason it appears in the parent.
    - The LPO/VLPO and the PeN are distinct sleep-active populations.
      Do not merge them; the reciprocal edge is a continuity edge, not
      a duplicate-structure warning.
    - MnPO naming: the "median preoptic nucleus" (MnPO) referenced here
      is the sleep-active population in the ventrolateral preoptic
      region, NOT the "median preoptic nucleus" (also called MnPO) that
      appears in the medial preoptic area's GnRH circuitry. The two
      are different structures with the same acronym; the tree
      distinguishes them by location.
    - The sleep switch is the operational framing: mutual inhibition
      between LPO and arousal systems produces bistable sleep-wake
      states. The model fragment treats sleep-wake mode as a
      state-level variable, not as a graded drive.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (GABA, galanin, adenosine, monoamines),
      06_* (social — oxytocin and vasopressin rarely relevant here),
      10_* (circadian, melatonin, SCN); memory/stores/; gateway/.
    - Connects upward to hypothalamus/anterior/lateral_area/left/
      preoptic_area/.
"""