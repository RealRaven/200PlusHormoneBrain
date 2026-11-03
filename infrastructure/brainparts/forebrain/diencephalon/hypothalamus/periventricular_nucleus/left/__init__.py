"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.periventricular_nucleus.left
Anatomical Role:
    The left periventricular zone. A heterogeneous band of cell groups
    lining the third ventricle in the left hemisphere, spanning the
    anterior, tuberal, and posterior divisions. It is NOT a single
    nucleus: it is a zone, and its cell groups have different functions
    in different rostrocaudal parts. The four documented groups:
        - Anterior periventricular group: scattered kisspeptin neurons
          (supplementary to the PeN and AVPV, both denser and more
          specialized); scattered sleep-promoting preoptic
          periventricular neurons (supplementary to the LPO/VLPO);
          scattered GnRH-adjacent interneurons. These are SUPPLEMENTARY
          contributions, not primary sources.
        - Tuberal periventricular group: the A14 dopaminergic cell group
          (a tuberal dopaminergic population projecting to the median
          eminence; its function is LESS established than the arcuate's
          TIDA dopamine; it is NOT the primary prolactin inhibitor);
          scattered somatostatin neurons (supplementary to the PVN's
          somatostatin neurons); scattered growth-regulatory neurons.
        - Posterior periventricular group: less well characterized;
          some dopaminergic and peptidergic cells whose functional
          significance is not established. Documented factually without
          overclaiming.
        - Other periventricular cell groups not classified under a
          specific division's medial or lateral area.

    All four groups are documented WITHIN this file, not as further
    child nodes. Same convention as mammillary_bodies/left/ carrying MM
    and LM, and other_preoptic_nuclei/left/ carrying AVPV and ADP.

    THREE NAMING TRAPS (critical — apply here and everywhere the
    periventricular zone is referenced):
    - PeN (periventricular preoptic nucleus): documented under
      lateral_area/left/periventricular_preoptic_nucleus/. The PeN is
      the dense anterior kisspeptin / GnRH-regulatory nucleus. THIS
      file's anterior periventricular kisspeptin is SCATTERED and
      SUPPLEMENTARY to the PeN. Do not merge; do not claim the
      periventricular zone's kisspeptin is "the" kisspeptin nucleus.
    - PVN (paraventricular nucleus): documented under
      medial_area/left/paraventricular_nucleus/. The PVN is the
      hypothalamus's most hormonally complex nucleus (CRH, TRH,
      somatostatin, oxytocin, vasopressin, autonomic). THIS file's
      tuberal somatostatin is SUPPLEMENTARY to the PVN's somatostatin.
      Do not merge; do not import PVN's five hormones into this file.
    - Arcuate nucleus (TIDA dopamine): documented under
      hypothalamus/tuberal/medial_area/left/arcuate_nucleus/ (when
      drafted). The arcuate's tuberoinfundibular dopaminergic (TIDA)
      neurons are the PRIMARY prolactin inhibitor. THIS file's A14
      dopaminergic group is a DIFFERENT tuberal dopaminergic
      population; its function is less established and it is NOT the
      primary prolactin inhibitor. Do not conflate; do not claim A14
      as "the" prolactin regulator.

Functional Mode (one function per cell group; supplementary framing
throughout):
    - A14 dopaminergic group (tuberal): a dopaminergic population
      projecting to the median eminence. Function less established
      than the arcuate's TIDA dopamine; supplementary dopaminergic
      contribution to the portal system. NOT the primary prolactin
      inhibitor. Document factually; do not overclaim.
    - Anterior periventricular kisspeptin (anterior): scattered
      periventricular kisspeptin neurons contributing to the broader
      kisspeptin network. SUPPLEMENTARY to the PeN (tonic drive /
      pulse frequency) and AVPV (positive feedback / surge). Document
      as a supplementary source, not as "the" kisspeptin nucleus.
    - Anterior periventricular sleep-promoting (anterior): scattered
      periventricular preoptic neurons contributing to sleep promotion.
      SUPPLEMENTARY to the LPO/VLPO (lateral_area/left/preoptic_area/
      lateral_preoptic_nucleus/) and the PeN's sleep-active population.
      Document as a supplementary sleep-promoting contribution, not as
      the primary one.
    - Tuberal somatostatin (tuberal): scattered somatostatin neurons
      contributing to growth-axis regulation. SUPPLEMENTARY to the
      PVN's somatostatin neurons. Document as a supplementary source.
    - Posterior periventricular (posterior): poorly characterized.
      Document factually; do not invent functional roles.
    - The zone is therefore a SUPPLEMENTARY contributor to every
      aggregate it feeds (reproductive, sleep, growth, prolactin-
      adjacent); it is never the primary source. Do not draft this
      file as if it were a hub; it is a catalogue of supplements.

Hormonal Modulation (per-cell-group; do not merge):
    - A14 dopaminergic: dopamine (output); modulated by estradiol and
      (indirectly) by prolactin feedback.
    - Anterior periventricular kisspeptin: estradiol (modulatory);
      kisspeptin (intrinsic); SCN vasopressin (circadian gating).
    - Anterior periventricular sleep-promoting: adenosine, GABA,
      galanin (modulatory) — the same signals that modulate the LPO;
      circadian drive from SCN.
    - Tuberal somatostatin: thyroid hormones and IGF-1 (feedback).
    - Posterior periventricular: not established; do not list.
    - Direction summary: estradiol modulates the kisspeptin and A14
      groups; adenosine/GABA modulate the sleep group; thyroid/IGF-1
      feedback modulates the somatostatin group. These are the
      actionable directions; do not overclaim beyond them.

Memory Interfaces:
    - Reads (per cell group):
        * A14 dopaminergic: short_term (current reproductive-hormonal
          state); episodic (cycle history).
        * Anterior periventricular kisspeptin: short_term (estradiol,
          circadian phase); temporal_sequence_learning (SCN-gated
          surge timing).
        * Anterior periventricular sleep-promoting: short_term (sleep
          pressure); temporal_sequence_learning (circadian sleep
          window).
        * Tuberal somatostatin: short_term (metabolic state); episodic
          (growth-axis history).
        * Posterior periventricular: not established.
    - Writes: none directly. The periventricular zone emits
      supplementary state signals, not stored content.
    - The parent container's Memory Interfaces section summarizes the
      same; this file documents the per-group detail.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent prompt fragment. The periventricular zone's four
      contributions are CONSTITUENT INPUTS to aggregates already
      established by other nuclei. AGGREGATION RULES (mandatory for
      the implementer):
        (1) A14 dopaminergic → prolactin-adjacent aggregate (currently
            carried by the arcuate's fragment when drafted; the A14
            contribution is supplementary).
        (2) Anterior periventricular kisspeptin → reproductive
            aggregate (aggregated with PeN + MPN + MnPO + AVPV).
        (3) Anterior periventricular sleep-promoting → sleep aggregate
            (aggregated with LPO).
        (4) Tuberal somatostatin → growth aggregate (aggregated with
            PVN).
    - SUPPLEMENTARY discipline: these are contributions, not
      independent fragments. Do not emit any periventricular fragment
      directly into the system prompt. Aggregate at the appropriate
      division level (anterior for reproductive/sleep; tuberal for
      growth/prolactin-adjacent) before injection.
    - The aggregate fragments already carry the standard "bias not
      impairment" guardrail; the periventricular zone does not add a
      new guardrail.
    - No multimodal input is consumed here; all contributions are
      text-only through their downstream aggregates.

Reciprocal Connections (left-side; organized by cell group):
    A14 dopaminergic (tuberal):
    - ↔ hypothalamus/tuberal/medial_area/left/arcuate_nucleus (adjacent
      tuberal dopaminergic populations; different functions; the
      arcuate's TIDA is primary for prolactin inhibition, A14 is
      supplementary; document as supplementation, NOT duplicate).
    - → hypothalamus/median_eminence (supplementary dopaminergic
      portal contribution).

    Anterior periventricular kisspeptin:
    - ↔ lateral_area/left/periventricular_preoptic_nucleus (PeN;
      adjacent periventricular kisspeptin populations; PeN is dense
      and primary, periventricular zone is scattered and supplementary;
      document as supplementation, NOT duplicate).
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area/
      median_preoptic_nucleus (MnPO; periventricular GnRH-regulatory
      neighbors).
    - ↔ other_preoptic_nuclei/left (AVPV; adjacent kisspeptin
      populations; supplementary periventricular contribution to the
      broader kisspeptin network).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → periventricular kisspeptin; circadian gating; SCN is
      midline-adjacent — verify).

    Anterior periventricular sleep-promoting:
    - ↔ lateral_area/left/preoptic_area/lateral_preoptic_nucleus (LPO;
      adjacent sleep circuitry; LPO is primary, periventricular zone
      is supplementary; document as supplementation, NOT duplicate).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → periventricular sleep neurons; circadian sleep gating;
      SCN is midline-adjacent — verify).

    Tuberal somatostatin:
    - ↔ hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (PVN; somatostatin co-contribution; PVN is primary, periventricular
      zone is supplementary; document as supplementation, NOT
      duplicate).
    - → hypothalamus/median_eminence (supplementary somatostatin portal
      contribution).

    Cross-cutting:
    - ↔ hypothalamus/median_eminence (anatomically adjacent; the portal
      pathway is shared; supplementary contributions feed it).
    - ↔ hypothalamus/pituitary_stalk (the periventricular contributions
      travel through the stalk to the anterior pituitary; anatomically
      adjacent).

Notes:
    - Tier 1 catch-all leaf (left). Full template. right/ is a delta.
    - THREE NAMING TRAPS reproduced in full: PeN, PVN, arcuate (TIDA
      vs. A14). The A14 trap is the newest: the A14 dopaminergic group
      is NOT "the" prolactin inhibitor; the arcuate's TIDA is. Do not
      let a future contributor conflate them.
    - SUPPLEMENTARY-NOT-PRIMARY discipline is the file's defining
      property. Every cell group in this file supplements a primary
      source documented elsewhere (PeN, AVPV, PVN, arcuate, LPO). The
      file must not be drafted as if the periventricular zone were a
      hub; it is a catalogue of supplements.
    - Heterogeneous zone, not a single nucleus. Four cell groups in
      one file, four different functions, three different divisions
      (anterior, tuberal, posterior). Do not flatten into "periventricular
      function."
    - No independent fragment: all four contributions aggregate into
      the appropriate division-level aggregates. The AGGREGATION RULES
      are mandatory for the implementer.
    - Do not create A14_group/, anterior_periventricular_kisspeptin/,
      sleep_promoting_periventricular/, etc. as child nodes. Same
      convention as mammillary_bodies/left/ and other_preoptic_nuclei/
      left/. All four are documented within this file.
    - The posterior periventricular group is poorly characterized.
      Document factually; do not invent functional roles to fill
      space. Same discipline as INAH-1/2 and striohypothalamic/
      ventral preoptic.
    - The container's trap analysis is reproduced here because a
      contributor entering at the leaf level must see the traps. Do
      not remove.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin), 03_*
      (HPT, growth, somatostatin, IGF-1, thyroid), 05_* (dopamine,
      GABA, galanin, adenosine), 10_* (circadian, SCN); memory/stores/
      (short_term, episodic, emotional_valence, temporal_sequence_
      learning); gateway/.
    - Connects upward to hypothalamus/periventricular_nucleus/.
"""