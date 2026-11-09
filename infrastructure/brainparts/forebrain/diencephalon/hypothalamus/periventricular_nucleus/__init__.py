"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.periventricular_nucleus
Anatomical Role:
    A catch-all container for the periventricular zone of the
    hypothalamus: the band of cell groups lining the third ventricle,
    spanning the anterior, tuberal, and posterior divisions. It sits as
    a direct child of hypothalamus/ (not under any one division) because
    the zone itself cuts across all three divisions. It is a CATCH-ALL
    container for periventricular structures that are not classified
    under a specific division's medial or lateral area.

    The container holds the following cell groups, documented WITHIN
    the left/ and right/ hemisphere leaves (not as further child nodes):
        - Anterior periventricular group: scattered GnRH-adjacent
          kisspeptin neurons, preoptic periventricular neurons, and
          sleep-promoting periventricular neurons. Overlaps functionally
          with the periventricular preoptic nucleus (PeN, documented
          separately under lateral_area/*/periventricular_preoptic_
          nucleus/) and the AVPV (documented under other_preoptic_
          nuclei/*), but is anatomically distinct from both.
        - Tuberal periventricular group: the A14 dopaminergic cell
          group (a dopaminergic tuberal population whose function is
          less established than the arcuate's tuberoinfundibular
          dopamine); scattered somatostatin neurons; scattered
          growth-hormone-regulatory neurons. These feed the median
          eminence portal system alongside the arcuate and PVN
          contributions.
        - Posterior periventricular group: less well characterized;
          some dopaminergic and peptidergic cells whose functional
          significance is not established.
        - Other periventricular cell groups: any periventricular
          neurons not classified under a specific division's medial or
          lateral area.

    DISTINCTIONS (critical — three naming traps apply here):
    - PERIVENTRICULAR PREOPTIC NUCLEUS (PeN): the PeN is a distinct
      structure documented under lateral_area/*/periventricular_
      preoptic_nucleus/. It is a kisspeptin/GnRH-regulatory nucleus in
      the anterior division. THIS container is the broader periventricular
      zone, not the PeN. Do not merge.
    - PARAVENTRICULAR NUCLEUS (PVN): the PVN is a distinct structure
      documented under medial_area/*/paraventricular_nucleus/. It is the
      hypothalamus's most hormonally complex nucleus (CRH, TRH,
      somatostatin, oxytocin, vasopressin, autonomic control). THIS
      container is the periventricular zone, not the PVN. Do not merge.
    - ARCUATE NUCLEUS: the arcuate is the primary tuberoinfundibular
      dopamine source (TIDA) that inhibits prolactin. The A14
      periventricular dopaminergic group is a distinct tuberal
      dopaminergic population whose function is less established; do
      not conflate the two, and do not claim the A14 group is the
      primary prolactin inhibitor.

Functional Mode:
    - Neuroendocrine portal contributions (primary): scattered neurons
      in the periventricular zone project to the median eminence and
      contribute to the hypophyseal portal system. The periventricular
      contributions are SCATTERED and SECONDARY to the well-defined
      contributions from the PVN (CRH, TRH, somatostatin), arcuate
      (GnRH-adjacent kisspeptin, GHRH, TIDA dopamine), and preoptic
      area (GnRH). The periventricular zone is a supplementary source,
      not a primary one.
    - A14 dopaminergic group (tuberal periventricular): a dopaminergic
      population with a documented projection to the median eminence.
      Its function is less established than the arcuate's TIDA
      dopamine; it is NOT the primary prolactin inhibitor. Document it
      factually as a dopaminergic periventricular group, not as "the"
      prolactin regulator.
    - GnRH-adjacent kisspeptin (anterior periventricular): scattered
      periventricular kisspeptin neurons contribute to the broader
      kisspeptin network that modulates GnRH. They are distinct from
      the PeN (which is the denser anterior periventricular kisspeptin
      population) and from the AVPV (which is the positive-feedback
      relay). Document as a supplementary kisspeptin source, not as a
      primary one.
    - Sleep-promoting neurons (anterior periventricular): some
      periventricular preoptic neurons contribute to sleep promotion,
      overlapping functionally with the LPO/VLPO (documented under
      lateral_area/*/preoptic_area/lateral_preoptic_nucleus/) and the
      PeN (documented under lateral_area/*/periventricular_preoptic_
      nucleus/). Document as a supplementary sleep-promoting
      contribution, not as the primary one.
    - Somatostatin neurons (tuberal periventricular): scattered
      somatostatin neurons contribute to growth-axis regulation
      alongside the PVN's somatostatin neurons. Document as a
      supplementary source, not as a primary one.
    - The container is therefore NOT a single functional unit: it is a
      heterogeneous periventricular zone whose cell groups feed multiple
      neuroendocrine and behavioral aggregates as SUPPLEMENTARY
      contributions. Do not treat the file as a coherent hub; treat it
      as a catalogue of supplementary periventricular contributions.

Hormonal Modulation (container-level summary; per-group wiring in
children):
    - A14 dopaminergic group: dopamine (output); modulated by estradiol
      and prolactin feedback (indirect).
    - GnRH-adjacent kisspeptin: estradiol (modulatory); kisspeptin
      (intrinsic); SCN vasopressin (circadian gating).
    - Sleep-promoting periventricular: adenosine, GABA, galanin
      (modulatory), same signals as the LPO.
    - Somatostatin: thyroid hormones and IGF-1 (feedback).
    - Direction summary: estradiol modulates the kisspeptin and
      dopaminergic groups; adenosine/GABA modulate the sleep group;
      thyroid/IGF-1 feedback modulates the somatostatin group. These
      are the actionable directions; do not overclaim beyond them.

Memory Interfaces (container-level summary):
    - Reads: short_term (current reproductive-hormonal state, osmotic
      state, sleep pressure, metabolic state), episodic (cycle/sleep/
      metabolic history), emotional_valence (stress context),
      temporal_sequence_learning (circadian timing).
    - Writes: none directly. The periventricular zone emits
      supplementary neuroendocrine and state signals, not stored
      content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No container-level prompt fragment. The periventricular zone's
      contributions are documented as CONSTITUENT INPUTS to the
      aggregates already established by other nuclei:
        (1) Dopaminergic A14 → prolactin-adjacent aggregate (currently
            documented in the arcuate's fragment when drafted; the A14
            contribution is supplementary).
        (2) Kisspeptin → reproductive aggregate (aggregated with PeN +
            MPN + MnPO + AVPV).
        (3) Sleep-promoting → sleep aggregate (aggregated with LPO).
        (4) Somatostatin → growth aggregate (aggregated with PVN).
    - AGGREGATION RULE (mandatory): the periventricular zone's
      contributions are SUPPLEMENTARY; do not emit independent
      periventricular fragments. Aggregate at the appropriate
      division level (anterior for reproductive, tuberal for growth/
      prolactin, anterior for sleep) before injection.
    - Guardrails: the aggregate fragments already carry the standard
      "bias not impairment" clause; the periventricular zone does not
      add a new guardrail.

Children (one child pair — each hemisphere's file carries all the
periventricular cell groups):
    - left/    ★ Left hemisphere. Full leaf (not a delta). Documents
                 the left anterior, tuberal, and posterior periventricular
                 groups, the A14 dopaminergic group, scattered
                 kisspeptin, sleep-promoting, and somatostatin neurons.
                 The authoritative file for this container.
    - right/   ★ Right hemisphere. Delta mirror of left/, differing
                 only in the right-side reciprocal edges. No functional
                 asymmetry documented.

Notes:
    - Tier 1 catch-all container with a single child pair. Both left/
      and right/ are full leaves.
    - THREE NAMING TRAPS apply here (reproduced in Anatomical Role):
      Periventricular preoptic nucleus (PeN); Paraventricular nucleus
      (PVN); Arcuate nucleus (TIDA dopamine). Do not merge; do not
      claim the A14 dopaminergic group is "the" prolactin inhibitor.
    - The periventricular zone is a HETEROGENEOUS ZONE, not a single
      nucleus. This is why the container is a catch-all and why the
      left/right leaves document multiple cell groups within each
      hemisphere's file.
    - The container's contributions are SUPPLEMENTARY, not primary:
      primary neuroendocrine sources are PVN (CRH, TRH, somatostatin),
      arcuate (kisspeptin, GHRH, TIDA dopamine), preoptic area (GnRH),
      SON (vasopressin, oxytocin). The periventricular zone supplements
      these; it does not replace them. State this explicitly so the
      implementer does not over-weight periventricular contributions.
    - The container cuts across divisions (anterior, tuberal,
      posterior) — that is why it is a direct child of hypothalamus/,
      not under any one division. Do not move it.
    - Do not create anterior_periventricular/, tuberal_periventricular/,
      posterior_periventricular/, A14_group/, etc. as child nodes.
      They are documented WITHIN the left/ and right/ hemisphere
      leaves. Same convention as mammillary_bodies/*/left|right and
      other_preoptic_nuclei/*/left|right.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin), 03_* (HPT,
      growth, somatostatin, IGF-1, thyroid hormones), 05_* (dopamine,
      GABA, galanin, adenosine), 10_* (circadian, SCN); memory/stores/
      (short_term, episodic, emotional_valence, temporal_sequence_
      learning); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * periventricular_nucleus/left|right (kisspeptin) ↔
          lateral_area/left|right/periventricular_preoptic_nucleus
          (PeN; adjacent periventricular kisspeptin populations;
          DIFFERENT structures; document as supplementation, not
          duplicate).
        * periventricular_nucleus/left|right (A14 dopamine) ↔
          hypothalamus/tuberal/medial_area/left|right/arcuate_nucleus
          (adjacent tuberal dopaminergic populations; different
          functions; document as supplementation, not duplicate).
        * periventricular_nucleus/left|right (somatostatin) ↔
          hypothalamus/anterior/medial_area/left|right/
          paraventricular_nucleus (somatostatin co-contribution;
          PVN is primary, PeV is supplementary).
        * periventricular_nucleus/left|right (sleep) ↔
          lateral_area/left|right/preoptic_area/
          lateral_preoptic_nucleus (adjacent sleep circuitry;
          supplementary contribution).
        * periventricular_nucleus/left|right → hypothalamus/
          median_eminence (supplementary portal contributions).
        * periventricular_nucleus/left|right ↔ hypothalamus/
          median_eminence and pituitary_stalk (anatomically adjacent;
          the portal pathway is shared).
    - Connects upward to hypothalamus/.
"""