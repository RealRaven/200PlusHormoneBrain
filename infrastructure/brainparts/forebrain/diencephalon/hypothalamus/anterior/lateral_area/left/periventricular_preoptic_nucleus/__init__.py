"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.left.periventricular_preoptic_nucleus
Anatomical Role:
    The left periventricular preoptic nucleus (PePO) is a component of the
    periventricular zone of the preoptic area, situated immediately
    adjacent to the third ventricle. It is a "marked lateral extension of
    the periventricular cell group" and contains several functionally
    distinct neuronal populations intermingled in the left hemisphere[reference:1]:
        - Kisspeptin (KP) neurons: the rostral periventricular kisspeptin
          population (often grouped with the anteroventral periventricular
          nucleus, AVPV, as "AVPV/PeN" in rodents). These neurons are the
          principal relay for estrogen positive feedback onto GnRH
          neurons, and they receive direct circadian input from the SCN[reference:2].
        - GnRH-regulatory interneurons: GABAergic and glutamatergic
          neurons that synapse onto GnRH neuron somata and proximal
          dendrites in the preoptic area. GnRH neurons themselves are
          scattered (medial septum, OVLT, anterior hypothalamic area) and
          do not all sit within this nucleus[reference:3].
        - Sleep-promoting neurons: GABAergic and galaninergic neurons
          that inhibit histaminergic tuberomammillary neurons and
          cholinergic/noradrenergic brainstem arousal centers[reference:4].
        - Thermoregulatory neurons: heat-loss and heat-conservation
          circuitry shared with the broader preoptic area.

    DISTINCTION FROM AVPV: the anteroventral periventricular nucleus
    (AVPV) is a separate node in this tree's logic, although the
    literature often groups AVPV and PeN as a single kisspeptin
    continuum. This file documents the PeN component (the periventricular
    extension proper). When the AVPV is drafted under
    anterior/medial_area/ (or wherever the tree places it), the two files
    must declare a reciprocal continuity edge, not a duplicate-structure
    warning — they are adjacent kisspeptin populations, not one split
    nucleus.

    DISTINCTION FROM MEDIAL PREOPTIC NUCLEUS: this is the *periventricular*
    preoptic nucleus, distinct from the medial preoptic nucleus (MPN) and
    the medial preoptic area. Do not merge.

Functional Mode:
    - GnRH pulse generation (basal): kisspeptin neurons in the PeN provide
      tonic excitatory drive to GnRH neurons, setting the pulse frequency
      of the HPG axis. This is the "pulse generator" component of PeN
      function, as distinct from the arcuate KNDy pulse generator.
    - GnRH surge generation (positive feedback): under rising estradiol
      in the late follicular phase, PeN kisspeptin neurons are activated
      and drive the preovulatory GnRH/LH surge[reference:5]. This is the
      principal estrogen-positive-feedback node in the anterior division.
    - Circadian gating of the surge: PeN kisspeptin neurons receive
      vasopressinergic input from the SCN; this monosynaptic pathway is
      enhanced by estrogen and is the anatomical basis for the
      time-of-day restriction of the LH surge[reference:6].
    - Sleep promotion: PeN (and adjacent preoptic) GABAergic neurons
      inhibit histaminergic tuberomammillary neurons and brainstem
      cholinergic/noradrenergic arousal centers, promoting non-REM
      sleep onset[reference:7].
    - Thermoregulation: heat-loss and heat-conservation, shared with the
      broader preoptic area. Estrogen withdrawal (menopause) produces
      hot flushes via this circuitry.
    - The nucleus is therefore tri-modal: reproductive (KP/GnRH),
      sleep-promoting (GABAergic), and thermoregulatory. Do not collapse
      these into one function; they are independent populations that
      happen to share a periventricular address.

Hormonal Modulation:
    - Estradiol: the defining modulator.
        * Positive feedback (high, sustained estradiol in late follicular
          phase): activates PeN kisspeptin neurons → GnRH/LH surge[reference:8].
        * Negative feedback (low-to-moderate estradiol, most of the
          cycle): suppresses GnRH pulse amplitude via arcuate KNDy
          neurons, with PeN contributing to pulse frequency regulation.
        * Estrogen also increases the number of KP-immunoreactive neurons
          and their vasopressinergic SCN input in ovariectomised
          rodents[reference:9].
    - Vasopressin (from SCN): excitatory/inhibitory depending on circuit
      context; the SCN→PeN vasopressin pathway is inhibitory-symmetric
      at the ultrastructural level and gates the surge to the correct
      time of day[reference:10].
    - Kisspeptin (KNDy co-transmitters from arcuate): modulates PeN KP
      neuron activity as part of the broader kisspeptin network.
    - GABA: intrinsic PeN GABAergic neurons both regulate GnRH neurons
      and promote sleep.
    - Galanin: co-transmitter in sleep-promoting PeN neurons.
    - Prostaglandin E2 (PGE2): thermoregulatory effector input; PGE2
      acting on PeN preoptic neurons drives heat-loss responses.
    - Thyroid hormones: modulate thermoregulatory set-point via preoptic
      circuitry.
    - Direction summary: estradiol ↑ KP activity (surge), SCN vasopressin
      ↑ gating (time-locked), PGE2 ↑ heat-loss, GABA ↑ sleep. These
      directions are the actionable content of this section; do not omit
      them.

Memory Interfaces:
    - Reads:
        * short_term: current estradiol level, circadian phase, and
          sleep-pressure buffer. The surge and sleep-onset decisions
          both depend on these.
        * temporal_sequence_learning: time-of-day context (SCN-gated),
          used to restrict the LH surge and sleep onset to the correct
          circadian window.
        * episodic: past reproductive-cycle events and sleep history,
          used to set sensitivity thresholds.
        * emotional_valence: stress context, which suppresses GnRH
          pulsatility and alters sleep architecture.
    - Writes:
        * reinforcement_value_based_learning: reproductive and sleep
          outcomes feed back into the value of context-appropriate
          behavioral states (indirect; document as modulation).
        * Does not write episodic or semantic content directly.
    - The tri-modal state (reproductive/sleep/thermoregulatory) is a
      *state*, not a memory write. Store schemas are defined in
      memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (applied after the lateral_area-level fragments,
      before the cortical reasoning fragments):
        "Preoptic state — periventricular preoptic nucleus (left):
         - Reproductive mode: [quiescent / follicular / periovulatory / luteal].
         - Estradiol feedback: [negative / positive-surge].
         - GnRH pulse state: [quiescent / pulsatile / surge].
         - Circadian gate: [open / closed] for the LH surge.
         - Sleep drive: [0-1].
         - Thermal state: [comfortable / hot / cold].
         If reproductive mode is periovulatory and the circadian gate is
         open: bias toward reproductive-context framing where relevant,
         and increase salience of social/affiliative cues. If sleep drive
         is high: reduce verbosity and favor calm, rest-adjacent tone.
         If thermal state is hot: acknowledge heat-related discomfort and
         prefer cooling-oriented language. Do not treat high sleep drive
         or periovulatory state as impairment — they are state biases."
    - The fragment is emitted whenever the homeostatic state block is
      emitted (always), with the reproductive mode and sleep drive as the
      primary signals.
    - Guardrail: "do not treat high sleep drive or periovulatory state as
      impairment" — the PeN equivalent of the habenula's "does not silence
      reasoning" clause. State biases are not degradations.
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (enforce in Stage 4 audit):
    - → preoptic GnRH neuron population (KP → GnRH; excitatory; the
      principal reproductive output edge).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → PeN vasopressinergic input; circadian gating of the surge).
    - ↔ hypothalamus/tuberal/medial_area/left/arcuate_nucleus (KNDy
      kisspeptin population; reciprocal kisspeptin network between
      arcuate and PeN).
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus
      (PeN → LC; inhibitory; sleep promotion via noradrenergic
      suppression).
    - → hindbrain/.../tuberomammillary_nucleus (PeN → TMN; inhibitory;
      histaminergic suppression; sleep promotion).
    - → brainstem cholinergic arousal centers (PeN → laterodorsal
      tegmental / pedunculopontine nuclei; inhibitory; sleep promotion).
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area (adjacent
      thermoregulatory and sleep circuitry; distinct but interacting).
    - ↔ anteroventral periventricular nucleus (AVPV; adjacent kisspeptin
      population; reciprocal continuity edge, not duplicate-structure
      warning — see Notes).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - NO structural-identity trap here: unlike the supraoptic split or the
      LHA continuum, PeN is a single nucleus in this tree. The only
      continuity edge is to the AVPV (adjacent kisspeptin population), and
      that is declared as a continuity edge, not a split-structure warning.
      Do not invent a structural-identity warning for this file.
    - The AVPV distinction is the one naming trap to guard against: the
      literature often says "AVPV/PeN" as a single unit, but this tree
      treats them as separate nodes. When the AVPV is drafted, both files
      must declare the reciprocal continuity edge.
    - The tri-modal framing (reproductive/sleep/thermoregulatory) is
      deliberate: the three functions are independent populations that
      share a periventricular address. The model fragment exposes all
      three as separate state fields so the model can use them
      independently.
    - The SCN→PeN vasopressin edge is the anatomical basis for the
      circadian gating of the LH surge. It must be reciprocated in
      suprachiasmatic_nucleus/ when that file is drafted.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, GnRH), 03_*
      (thyroid), 05_* (GABA, galanin), 07_* (vasopressin), 10_*
      (circadian, SCN); memory/stores/ (short_term, episodic,
      temporal_sequence_learning, emotional_valence); gateway/.
    - Connects upward to hypothalamus/anterior/lateral_area/left/.
"""