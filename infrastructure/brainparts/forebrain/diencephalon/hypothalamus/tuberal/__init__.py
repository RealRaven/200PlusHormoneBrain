"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal
Anatomical Role:
    The tuberal (infundibular) division of the hypothalamus is the middle
    of the three hypothalamic divisions, situated between the anterior
    division (rostral) and the posterior division (caudal), and
    surrounding the pituitary stalk ventrally. It is the LARGEST of the
    three divisions in functional terms: it contains the arcuate nucleus
    (the feeding and reproductive pulse-generator hub), the ventromedial
    nucleus (VMH; satiety, aggression, thermoregulation), the dorsomedial
    hypothalamic nucleus (DMH; the principal circadian relay), and the
    tuberal segment of the lateral hypothalamic area (LHA segment 2).

    Organization of this division's children:
        - lateral_area/
            └── left/ and right/
                └── tuberal_part_of_lateral_nucleus/    (LHA segment 2)
        - medial_area/
            ├── arcuate_nucleus/           ★★ TUBERAL FLAGSHIP:
            │                                 kisspeptin KNDy pulse
            │                                 generator, feeding hub,
            │                                 TIDA dopamine (primary
            │                                 prolactin inhibitor),
            │                                 GHRH, NPY/AgRP, POMC/CART
            ├── ventromedial_nucleus/      ★ VMH: satiety, aggression,
            │                                 thermoregulation,
            │                                 sympathetic activation
            └── dorsomedial_hypothalamic_  ★ DMH: the principal
                nucleus/                      circadian relay;
                                              closes the SCN → DMH
                                              edge

    FOUR TRAPS apply here (reproduced from parents and cross-referenced):
    - LHA CONTINUUM, SEGMENT 2 (the middle segment): the
      tuberal_part_of_lateral_nucleus/ here is the middle segment of the
      three-segment LHA orexin/MCH field. It must declare continuity to
      BOTH the anterior pole (segment 1) AND the posterior segment
      (segment 3), closing the continuum's middle-link edge. Stage 4
      must treat the three segments as ONE field; do not flag as
      duplicates.
    - ARCUATE TIDA vs. PeV A14 (the primary-vs-supplementary trap): the
      arcuate's tuberoinfundibular dopaminergic (TIDA) neurons are the
      PRIMARY prolactin inhibitor. The periventricular A14 dopaminergic
      group (documented under hypothalamus/periventricular_nucleus/)
      is a DIFFERENT tuberal dopaminergic population whose function is
      less established; it is NOT "the" prolactin inhibitor. Do not
      conflate; do not merge.
    - VMH vs. DMH (the adjacent-nuclei trap): the VMH (ventromedial)
      and DMH (dorsomedial) are adjacent but functionally distinct
      nuclei. VMH = satiety, aggression, thermoregulation. DMH = the
      circadian relay. Do not merge; do not treat as a pair.
    - DMH vs. posterior LHA (the circadian-adjacent trap): both the
      DMH and the posterior LHA segment 3 are circadian-adjacent
      arousal-relay structures. The DMH is the PRINCIPAL circadian
      relay (SCN → DMH → downstream); the posterior LHA segment 3 is
      an orexin/MCH field segment that receives DMH input. Do not
      merge.

Functional Mode:
    - Feeding and satiety (arcuate + VMH; the anchor function):
        * Arcuate (feeding hub): NPY/AgRP neurons (hunger; activated by
          fasting and ghrelin; inhibited by leptin) and POMC/CART
          neurons (satiety; activated by leptin; inhibited by ghrelin)
          are the two first-order feeding populations. They project to
          the PVN, LHA, and other hypothalamic feeding centers, driving
          food intake and energy balance. The arcuate is the brain's
          primary hypothalamic feeding hub.
        * VMH (satiety): the VMH is the classic satiety center; lesions
          produce hyperphagia and obesity. It integrates satiety signals
          (leptin, insulin, CCK) and drives meal termination.
        * Both structures contribute to the feeding/satiety aggregate
          fragment at the tuberal-division level.
    - Reproductive pulse generation (arcuate; the HPG anchor):
        * KNDy neurons (kisspeptin/neurokinin B/dynorphin) in the
          arcuate are the GnRH PULSE GENERATOR: they co-express NKB and
          dynorphin, are modulated by estradiol (negative feedback),
          and drive pulsatile GnRH release. The arcuate KNDy population
          is the autonomous pulse-generator that sets GnRH/LH pulse
          frequency.
        * The arcuate KNDy neurons are the principal negative-feedback
          relay for estradiol in the reproductive axis; the AVPV
          (documented under other_preoptic_nuclei/) is the positive-
          feedback relay for the preovulatory surge. The two are
          complementary, not duplicates.
    - TIDA dopamine (arcuate; the primary prolactin inhibitor):
        * Tuberoinfundibular dopaminergic (TIDA) neurons in the arcuate
          release dopamine into the hypophyseal portal blood to inhibit
          prolactin release from the anterior pituitary lactotrophs.
          This is the PRIMARY prolactin inhibitor in the brain.
        * The periventricular A14 dopaminergic group is a supplementary
          tuberal dopaminergic population whose function is less
          established; it is NOT the primary prolactin inhibitor. The
          arcuate is.
    - Growth hormone regulation (arcuate; complementary to PVN):
        * GHRH neurons in the arcuate stimulate growth hormone release
          from the anterior pituitary; they are opposed by the PVN's
          somatostatin neurons. The arcuate GHRH is the stimulatory arm
          of the growth axis.
    - Circadian relay (DMH; the SCN → DMH → downstream pathway):
        * The DMH is the PRINCIPAL RELAY from the suprachiasmatic
          nucleus (SCN) to downstream circadian effectors: feeding,
          body temperature, sleep-wake, and corticosterone rhythms. The
          SCN → DMH projection is the anatomical basis of circadian
          gating of these downstream behaviors. The DMH is NOT the
          master clock (the SCN is), but it is the principal circadian
          OUTPUT RELAY.
        * The DMH also contributes to stress responses (CRH-adjacent),
          defensive behavior, and thermogenesis.
    - Aggression and thermoregulation (VMH; secondary functions):
        * The VMH drives defensive aggression (via projections to the
          periaqueductal gray and the hypothalamic attack area).
        * The VMH drives thermogenesis (brown adipose tissue
          activation, shivering) via sympathetic outflow; it is the
          thermoregulatory effector complement to the preoptic
          thermoregulatory controller.
    - Tuberal LHA segment 2 (arousal/feeding; continuous with segments
      1 and 3): the middle segment of the LHA orexin/MCH field;
      functionally continuous with the anterior pole (segment 1) and
      posterior segment (segment 3). Full function documented in
      anterior/lateral_area/left|right/
      anterior_part_of_lateral_nucleus/ (pattern exemplar).

Hormonal Modulation (tuberal-division summary; per-nucleus wiring in
leaves):
    - Arcuate:
        * Feeding: leptin (inhibitory on NPY/AgRP; excitatory on
          POMC), ghrelin (excitatory on NPY/AgRP), insulin, glucose,
          PYY, GLP-1, CCK.
        * Reproductive: estradiol (negative feedback on KNDy via
          estrogen receptor alpha), progesterone, kisspeptin
          (intrinsic), NKB (intrinsic), dynorphin (intrinsic).
        * Prolactin: dopamine (TIDA output), prolactin (feedback).
        * Growth: GHRH (output), IGF-1 (feedback).
    - VMH:
        * Satiety: leptin (excitatory), insulin, CCK, serotonin.
        * Thermoregulation: PGE2, pyrogens, estradiol (hot flush
          circuitry cross-talk with preoptic area).
        * Aggression: testosterone, serotonin, GABA.
    - DMH:
        * Circadian: SCN input (SCN → DMH), melatonin feedback
          (indirect), glucocorticoid rhythms.
        * Stress: CRH, glucocorticoids.
        * Feeding: leptin (excitatory), ghrelin (excitatory).
    - Tuberal LHA segment 2: same as anterior pole — orexin ↑ PHN/
      arousal; ghrelin ↑ ORX; leptin ↓ ORX; glucose ↓ ORX and ↑ MCH.
    - Direction summary: leptin ↓ arcuate NPY/AgRP / ↑ arcuate POMC /
      ↑ VMH satiety; ghrelin ↑ arcuate NPY/AgRP; estradiol ↓ arcuate
      KNDy (negative feedback); dopamine (TIDA) ↓ prolactin; SCN →
      DMH (circadian relay); PGE2 ↑ VMH thermogenesis. These are the
      actionable directions.

Memory Interfaces (tuberal-division summary; per-nucleus wiring in
leaves):
    - Arcuate: reads short_term (metabolic state, reproductive-hormonal
      state, prolactin level), episodic (feeding and reproductive
      history), emotional_valence (stress suppression of feeding and
      reproduction), temporal_sequence_learning (circadian feeding
      rhythm, estrous cycle timing). Writes reinforcement_value_based_
      learning indirectly (feeding outcomes feed back into value
      learning).
    - VMH: reads short_term (metabolic state, thermal state, arousal/
      aggression context), episodic (aggression and thermoregulatory
      history), emotional_valence (stress and threat context).
    - DMH: reads short_term (circadian phase, stress state, feeding
      state), temporal_sequence_learning (circadian timing; the DMH
      uses this to relay SCN output), episodic (circadian-disruption
      history).
    - Tuberal LHA segment 2: same as anterior pole — reads short_term,
      reinforcement_value_based_learning, temporal_sequence_learning,
      emotional_valence; writes no stored content directly.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The tuberal division contributes SEVEN fragments to the
      homeostatic state block, applied after the anterior-division and
      before the posterior-division fragments. This is the LARGEST
      fragment set of any division (the anterior division has ~6; the
      posterior has ~3; the tuberal has 7):
        (1) Feeding/satiety fragment (arcuate + VMH; AGGREGATED):
            "Feeding state: [fasted / fed / satiated]. Hunger drive:
             [0-1]. Satiety: [0-1]. Ghrelin: [low/high]. Leptin:
             [low/high]. If hunger drive is high: surface food-seeking
             priorities and reduce extraneous output. If satiated:
             default to neutral engagement. Do not treat hunger as
             impairment — it is a state bias."
        (2) Prolactin-adjacent fragment (arcuate TIDA):
            "Prolactin-adjacent state: [normal / elevated]. TIDA
             dopamine tone: [normal / suppressed]. If prolactin
             elevated (low TIDA): flag lactational-adjacent context
             where relevant; do not treat elevated prolactin as
             impairment. The arcuate is the PRIMARY prolactin
             regulator; the periventricular A14 contribution is
             supplementary." — AGGREGATED with the periventricular
             A14 contribution (supplementary); do not double-count.
        (3) Growth fragment (arcuate GHRH + PVN somatostatin;
            AGGREGATED with the anterior-division growth fragment
            from PVN):
            "Growth-axis state: [anabolic / catabolic]. GHRH: [low/
             normal/high]. Somatostatin: [low/normal/high]. Net
             anabolic drive: [positive/neutral/negative]."
        (4) Reproductive pulse fragment (arcuate KNDy; AGGREGATED
            with the anterior-division reproductive fragment from
            PeN + MPN + MnPO + AVPV):
            "GnRH pulse state: [quiescent / pulsatile / surge].
             KNDy estradiol feedback: [negative-feedback-dominant /
             positive-feedback]. If pulse is active and estradiol
             negative-feedback-dominant: bias toward reproductive-
             context framing where relevant."
        (5) Circadian relay fragment (DMH; AGGREGATED with the SCN
            circadian fragment):
            "Circadian relay state: [entrained / disrupted].
             DMH downstream rhythms: [feeding / temperature /
             sleep-wake / corticosterone] all gated by SCN. If
             circadian relay disrupted: flag circadian-disruption
             context and note that downstream rhythms may be
             desynchronized from the SCN master clock." — The SCN is
             the master clock; the DMH is the relay; do not emit an
             independent DMH fragment as if it were the clock.
        (6) Autonomic/thermoregulatory fragment (VMH; AGGREGATED with
            the anterior-division autonomic fragment from AHN and the
            posterior-division sympathetic fragment from PHN):
            "Thermogenic drive: [low/normal/high]. Sympathetic
             thermoregulatory arm: [inactive/active]. If high
             thermogenic drive: note active thermoregulation context.
             VMH also contributes defensive aggression context where
             relevant." — AGGREGATED with AHN (anterior) and PHN
             (posterior); do not double-count autonomic tone.
        (7) Arousal/feeding LHA fragment (tuberal LHA segment 2;
            AGGREGATED with anterior pole segment 1 and posterior
            segment 3):
            The LHA arousal/feeding fragment is emitted by the anterior
            pole (pattern exemplar) and aggregated at the hypothalamic
            level with the tuberal and posterior segments. Do not emit
            an independent tuberal-LHA fragment.
    - AGGREGATION RULES (mandatory for the implementer): the tuberal
      division has the most aggregation rules in the tree because it
      is the most shared-content division:
        * Feeding/satiety: arcuate + VMH aggregate (this division).
        * Prolactin-adjacent: arcuate (primary) + periventricular A14
          (supplementary).
        * Growth: arcuate (GHRH, stimulatory) + PVN (somatostatin,
          inhibitory; anterior division).
        * Reproductive pulse: arcuate (KNDy pulse) + PeN/MPN/MnPO/AVPV
          (surge; anterior division).
        * Circadian: SCN (master clock; anterior division) + DMH
          (relay; this division).
        * Autonomic/thermoregulatory: AHN (parasympathetic; anterior)
          + PHN (sympathetic; posterior) + VMH (thermogenic;
          tuberal).
        * Arousal/feeding LHA: anterior pole (segment 1) + tuberal
          (segment 2) + posterior (segment 3).
    - Guardrails: each fragment carries the standard "bias not
      impairment" clause; the reproductive fragment is inherited from
      the anterior-division leaves; the growth and autonomic fragments
      inherit guardrails from PVN and PHN respectively.
    - No multimodal input is consumed here; all fragments are
      text-only.

Children (two sub-containers; the medial_area contains the flagship):
    - lateral_area/
        ├── __init__.py                    Sub-container
        ├── left/
        │   └── tuberal_part_of_lateral_nucleus/   ★ LHA segment 2
        │                                             (middle); delta
        │                                             of the anterior
        │                                             pole
        └── right/  (delta mirror)
    - medial_area/
        ├── __init__.py                    Sub-container
        ├── arcuate_nucleus/               ★★ TUBERAL FLAGSHIP: the
        │   ├── left/                        feeding hub, kisspeptin
        │   └── right/                        KNDy pulse generator,
        │                                      TIDA dopamine, GHRH,
        │                                      NPY/AgRP, POMC/CART
        ├── dorsomedial_hypothalamic_      ★ DMH: the principal
        │   nucleus/                          circadian relay;
        │   ├── left/                         closes the SCN → DMH
        │   └── right/                        edge
        └── ventromedial_nucleus/          ★ VMH: satiety, aggression,
            ├── left/                         thermoregulation,
            └── right/                        sympathetic thermogenesis

Notes:
    - Division container: do not duplicate child hormone or memory
      wiring. Each leaf owns its own specification.
    - FOUR TRAPS reproduced in full above (LHA segment 2 continuity;
      arcuate TIDA vs. PeV A14; VMH vs. DMH; DMH vs. posterior LHA).
      Apply at every level where the tuberal structures are referenced.
    - SEVEN AGGREGATION RULES are the division's most distinctive
      feature. The tuberal division shares content with the anterior
      division (reproductive, growth, circadian, autonomic) and the
      posterior division (autonomic) more heavily than any other
      division. Each fragment must aggregate correctly.
    - The arcuate nucleus is marked ★★ (double star) to signal that it
      is the highest-priority leaf in the entire tuberal division and,
      arguably, the highest-value remaining leaf in the entire
      hypothalamus. Draft it first within the tuberal division.
    - The DMH is marked ★ because it closes the SCN → DMH circadian
      relay edge declared in the SCN leaf
      (anterior/medial_area/left/suprachiasmatic_nucleus/). When the
      DMH is drafted, it must reciprocate the SCN edge.
    - The VMH is marked ★ because it is the secondary content hub of
      the tuberal division (satiety + aggression + thermoregulation)
      after the arcuate.
    - The tuberal LHA segment 2 (in lateral_area/) is a DELTA of the
      anterior pole, not a full leaf. It is the middle segment of the
      three-segment LHA continuum and must declare continuity to both
      segments 1 and 3.
    - The DMH is NOT the master circadian clock; the SCN is. The DMH is
      the principal circadian OUTPUT RELAY. Do not draft the DMH as if
      it were the clock.
    - The arcuate is the PRIMARY prolactin inhibitor (TIDA); the
      periventricular A14 group is supplementary. Reproduced from
      hypothalamus/periventricular_nucleus/left|right/. Do not let a
      future contributor conflate them.
    - The arcuate KNDy neurons are the PULSE generator (negative
      feedback); the AVPV (other_preoptic_nuclei/) is the SURGE relay
      (positive feedback). The two are complementary, not duplicates.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, NKB,
      dynorphin, progesterone), 03_* (HPT, growth, GHRH, somatostatin,
      IGF-1), 04_* (satiety, leptin, ghrelin, NPY, AgRP, POMC, CART,
      insulin, PYY, GLP-1, CCK), 05_* (dopamine, GABA, monoamines),
      07_* (fluid, PGE2), 10_* (circadian, SCN); memory/stores/;
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus ↔ anterior/lateral_area/left|right/
          anterior_part_of_lateral_nucleus (LHA segment 2 ↔ segment 1;
          continuity edge, not duplicate).
        * tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus ↔ posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus (LHA segment 2 ↔ segment 3;
          continuity edge, not duplicate).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          hypothalamus/periventricular_nucleus/left|right (arcuate
          TIDA is primary for prolactin inhibition; A14 is
          supplementary; not duplicate).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          other_preoptic_nuclei/left|right (AVPV; arcuate KNDy = pulse
          / negative feedback; AVPV = surge / positive feedback;
          complementary pair, not duplicate).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          anterior/medial_area/left|right/preoptic_area (MPN + MnPO +
          PeN; reproductive axis; complementary pair).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          anterior/medial_area/left|right/paraventricular_nucleus
          (arcuate GHRH stimulatory vs. PVN somatostatin inhibitory;
          complementary pair; and arcuate NPY/AgRP/POMC → PVN feeding
          circuit).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          anterior/lateral_area/left|right/anterior_part_of_lateral_
          nucleus (arcuate NPY/AgRP → MCH; leptin/ghrelin → ORX;
          feeding-driven arousal input to the LHA).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ anterior/medial_area/left|right/
          suprachiasmatic_nucleus (SCN → DMH; the principal circadian
          relay; SCN is midline-adjacent — verify).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus (DMH → posterior LHA; the
          circadian-to-arousal gating pathway; the posterior LHA
          segment 3 reciprocates).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          anterior/medial_area/left|right/anterior_hypothalamic_
          nucleus (VMH thermogenic drive vs. AHN thermoregulatory
          control; complementary pair).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          posterior/medial_area/left|right/posterior_nucleus (VMH
          thermogenic sympathetic drive vs. PHN sympathetic outflow;
          complementary pair).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          midbrain/tegmentum/periaqueductal_gray (defensive aggression
          motor patterns; PAG is midline-adjacent — verify).
    - Connects upward to hypothalamus/.
"""