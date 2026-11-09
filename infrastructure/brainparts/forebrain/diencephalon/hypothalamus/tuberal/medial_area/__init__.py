"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area
Anatomical Role:
    The medial area of the tuberal hypothalamus. It contains the three
    principal nuclei of the tuberal division's medial zone:
        - arcuate_nucleus/ (left/ and right/) — ★★ TUBERAL FLAGSHIP.
          The brain's hypothalamic feeding hub and reproductive
          pulse-generator, and the primary prolactin inhibitor:
            * NPY/AgRP neurons (hunger).
            * POMC/CART neurons (satiety).
            * Kisspeptin KNDy neurons (GnRH pulse generator; estradiol
              negative feedback).
            * TIDA dopaminergic neurons (primary prolactin inhibitor).
            * GHRH neurons (stimulatory arm of the growth axis).
          The arcuate is the most functionally dense nucleus in the
          entire tuberal division.
        - ventromedial_nucleus/ (left/ and right/) — ★ VMH. Satiety
          center, defensive aggression, and thermoregulation
          (sympathetic thermogenesis). Secondary hub after the arcuate.
        - dorsomedial_hypothalamic_nucleus/ (left/ and right/) — ★ DMH.
          The PRINCIPAL CIRCACIAN RELAY from the SCN to downstream
          effectors (feeding, temperature, sleep-wake, corticosterone).
          Closes the SCN → DMH edge declared in the SCN leaf.

    SEVEN TRAPS apply here (reproduced from parents and cross-referenced
    below; each must be resolved for Stage 4):

    1. ARCUATE TIDA vs. PeV A14 (the primary-vs-supplementary trap):
       the arcuate's tuberoinfundibular dopaminergic (TIDA) neurons are
       the PRIMARY prolactin inhibitor. The periventricular A14
       dopaminergic group (hypothalamus/periventricular_nucleus/left|
       right/) is a DIFFERENT tuberal dopaminergic population whose
       function is less established; it is NOT "the" prolactin
       inhibitor. Do not conflate.

    2. ARCUATE KNDy vs. AVPV (the pulse-vs-surge complementarity):
       the arcuate KNDy neurons are the GnRH PULSE generator (negative
       feedback); the AVPV (other_preoptic_nuclei/left|right/) is the
       GnRH SURGE relay (positive feedback). The two are COMPLEMENTARY,
       not duplicates. Do not conflate; do not merge.

    3. ARCUATE GHRH vs. PVN SOMATOSTATIN (the growth-axis complementarity):
       the arcuate GHRH neurons are the STIMULATORY arm of the growth
       axis; the PVN somatostatin neurons
       (anterior/medial_area/left|right/paraventricular_nucleus/) are
       the INHIBITORY arm. The two are COMPLEMENTARY, not duplicates.
       Do not conflate; do not merge.

    4. VMH vs. DMH (the adjacent-nuclei trap): the VMH (ventromedial)
       and DMH (dorsomedial) are adjacent but functionally distinct
       nuclei. VMH = satiety, aggression, thermoregulation. DMH =
       circadian relay. Do not merge; do not treat as a pair.

    5. DMH vs. posterior LHA (the circadian-adjacent trap): the DMH is
       the PRINCIPAL circadian relay (SCN → DMH → downstream); the
       posterior LHA segment 3 (posterior/lateral_area/left|right/
       posterior_part_of_lateral_nucleus/) is an orexin/MCH field
       segment that RECEIVES DMH input. Do not merge.

    6. DMH vs. SCN (the relay-vs-clock trap): the SCN
       (anterior/medial_area/left|right/suprachiasmatic_nucleus/) is
       the MASTER CLOCK; the DMH is the PRINCIPAL OUTPUT RELAY. Do not
       draft the DMH as if it were the clock. The DMH leaf must
       reciprocate the SCN → DMH edge declared in the SCN leaf.

    7. VMH vs. AHN and VMH vs. PHN (the autonomic complementary pairs):
       the VMH's thermogenic sympathetic drive is complementary to the
       AHN's parasympathetic thermoregulatory control
       (anterior/medial_area/left|right/anterior_hypothalamic_nucleus/)
       and to the PHN's sympathetic outflow
       (posterior/medial_area/left|right/posterior_nucleus/). The three
       nuclei form a thermoregulatory triangle; do not merge any of
       them; document the complementary relationships.

Functional Mode:
    - Feeding (arcuate + VMH; the anchor function):
        * Arcuate: NPY/AgRP (hunger; ↑ by fasting/ghrelin; ↓ by
          leptin) and POMC/CART (satiety; ↑ by leptin; ↓ by ghrelin)
          are the two first-order feeding populations. They project to
          the PVN, LHA, and other hypothalamic feeding centers.
        * VMH: satiety center; lesions produce hyperphagia and obesity.
          Integrates satiety signals (leptin, insulin, CCK) and drives
          meal termination.
        * Both contribute to the feeding/satiety aggregate fragment.
    - Reproductive pulse generation (arcuate; the HPG anchor):
        * Arcuate KNDy neurons (kisspeptin/NKB/dynorphin) are the
          autonomous GnRH pulse generator, modulated by estradiol
          (negative feedback). The AVPV (other_preoptic_nuclei/) is
          the positive-feedback surge relay; the two are complementary.
    - Prolactin inhibition (arcuate; TIDA): tuberoinfundibular
      dopaminergic neurons release dopamine into the hypophyseal portal
      blood to inhibit prolactin release. The PRIMARY prolactin
      inhibitor in the brain. The periventricular A14 dopaminergic
      group is supplementary, not primary.
    - Growth (arcuate GHRH + PVN somatostatin): arcuate GHRH stimulates
      GH release; PVN somatostatin inhibits it. The two arms form the
      growth axis.
    - Circadian relay (DMH): the principal SCN → DMH → downstream
      pathway for circadian gating of feeding, body temperature,
      sleep-wake, and corticosterone rhythms. The DMH is the RELAY, not
      the clock (the SCN is).
    - Satiety and aggression and thermoregulation (VMH; secondary
      functions): defensive aggression (via PAG and the hypothalamic
      attack area); sympathetic thermogenesis (BAT activation,
      shivering).
    - The tuberal medial area is therefore the integration point for
      feeding, reproduction, growth, circadian, and autonomic
      functions. It is the most functionally dense division of the
      hypothalamus, and the arcuate is its most functionally dense
      nucleus.

Hormonal Modulation (sub-container summary; per-nucleus wiring in
leaves):
    - Arcuate: leptin (↓ NPY/AgRP; ↑ POMC), ghrelin (↑ NPY/AgRP),
      insulin, glucose, PYY, GLP-1, CCK; estradiol (↓ KNDy via ERα),
      progesterone, kisspeptin (intrinsic), NKB (intrinsic), dynorphin
      (intrinsic); dopamine (TIDA output), prolactin (feedback); GHRH
      (output), IGF-1 (feedback).
    - VMH: leptin (↑ satiety), insulin, CCK, serotonin; PGE2, pyrogens,
      estradiol (hot-flush cross-talk); testosterone, serotonin, GABA
      (aggression).
    - DMH: SCN input (SCN → DMH); melatonin (indirect feedback);
      glucocorticoids; leptin (↑), ghrelin (↑).
    - Direction summary: leptin ↓ NPY/AgRP and ↑ POMC; ghrelin ↑
      NPY/AgRP; estradiol ↓ KNDy; dopamine (TIDA) ↓ prolactin;
      SCN → DMH; PGE2 ↑ VMH thermogenesis. These are the actionable
      directions.

Memory Interfaces (sub-container summary):
    - Arcuate: reads short_term (metabolic, reproductive, prolactin),
      episodic (feeding/reproductive history), emotional_valence
      (stress), temporal_sequence_learning (feeding rhythm, estrous
      timing). Writes reinforcement_value_based_learning indirectly.
    - VMH: reads short_term (metabolic, thermal, arousal/aggression),
      episodic (aggression/thermoregulatory history), emotional_valence.
    - DMH: reads short_term (circadian phase, stress, feeding),
      temporal_sequence_learning (the DMH's primary read — relays SCN
      output), episodic (circadian-disruption history).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The sub-container does not emit fragments itself. The three
      leaves emit their own fragments (via aggregation rules
      established at the parent tuberal/ division container):
        (1) Arcuate → feeding/satiety (arcuate+VMH aggregate), prolactin-
            adjacent (arcuate TIDA + PeV A14 aggregate), growth (arcuate
            GHRH + PVN somatostatin aggregate), reproductive pulse
            (arcuate KNDy + PeN/MPN/MnPO/AVPV aggregate).
        (2) VMH → feeding/satiety (with arcuate), autonomic/thermo-
            regulatory (with AHN and PHN).
        (3) DMH → circadian relay (with SCN; the DMH fragment is a
            constituent of the SCN aggregate).
    - The seven aggregation rules from the parent tuberal/ container
      apply identically here. The leaves implement them; this
      sub-container references them.
    - No fragment is emitted at the sub-container level.
    - Guardrails: the leaves carry their own (feeding, reproductive,
      autonomic, circadian) guardrails, consistent with the tree's
      established pattern.

Children (three children — all Tier 1 full leaves with deltas):
    - arcuate_nucleus/        ★★ TUBERAL FLAGSHIP. Most functionally
        ├── left/                dense nucleus in the tuberal
        └── right/               division. Feeding hub, kisspeptin
                                 KNDy pulse generator, TIDA prolactin
                                 inhibitor, GHRH growth arm, NPY/AgRP
                                 and POMC/CART feeding populations.
    - ventromedial_nucleus/   ★ VMH. Satiety, defensive aggression,
        ├── left/                thermoregulation (sympathetic
        └── right/               thermogenesis).
    - dorsomedial_hypothalamic_nucleus/  ★ DMH. Principal circadian
        ├── left/                relay (SCN → DMH → downstream).
        └── right/

    All three are Tier 1 full leaves with left/ and right/ pairs. No
    pointer deltas here (the mammillary-nuclei pattern is unique to
    the posterior division).

Notes:
    - Sub-container file. It opens the last substantive content block
      in the entire hypothalamus. The three nuclei below are the last
      three Tier 1 hub leaves remaining in the tree.
    - SEVEN TRAPS are reproduced in full above. Every one of them
      applies to a specific child or pair of children:
        * Trap 1 (TIDA vs. A14) → arcuate
        * Trap 2 (KNDy vs. AVPV) → arcuate
        * Trap 3 (GHRH vs. somatostatin) → arcuate + PVN
        * Trap 4 (VMH vs. DMH) → VMH + DMH
        * Trap 5 (DMH vs. posterior LHA) → DMH + posterior LHA
        * Trap 6 (DMH vs. SCN) → DMH + SCN
        * Trap 7 (VMH vs. AHN + VMH vs. PHN) → VMH + AHN + PHN
      Do not omit any of them.
    - The arcuate is marked ★★ (double star): it is the highest-priority
      leaf in the entire tuberal division. Draft it first among the
      three.
    - The VMH and DMH are marked ★: they are the secondary and
      tertiary content hubs, respectively.
    - The DMH leaf must reciprocate the SCN → DMH edge declared in the
      SCN leaf (anterior/medial_area/left|right/suprachiasmatic_
      nucleus/). This is the deferred closure of a circadian edge that
      has been pending since the SCN pair was drafted.
    - The arcuate leaf must reciprocate:
        * Periventricular A14 (TIDA primary vs. A14 supplementary;
          not duplicate).
        * AVPV (pulse vs. surge; complementary pair).
        * PVN (GHRH stimulatory vs. somatostatin inhibitory;
          complementary pair).
        * LHA segment 2 (arcuate feeding → tuberal LHA; the tuberal
          LHA segment's distinctive input, already declared from the
          LHA side).
    - The VMH leaf must reciprocate:
        * AHN (thermogenic sympathetic drive vs. parasympathetic
          thermoregulatory control; complementary pair).
        * PHN (thermogenic drive vs. sympathetic outflow; complementary
          pair).
        * PAG (defensive aggression motor patterns; PAG is
          midline-adjacent — verify).
    - The DMH leaf must reciprocate:
        * SCN (SCN → DMH; the deferred circadian relay closure).
        * Posterior LHA segment 3 (DMH → posterior LHA; the
          circadian-to-arousal gating pathway).
        * Tuberal LHA segment 2 (DMH → tuberal LHA; the
          circadian-to-feeding-arousal gating pathway).
    - The arcuate is NOT the AVPV; the arcuate is the pulse generator,
      the AVPV is the surge relay. They are both kisspeptin
      populations, but functionally complementary, not duplicates.
    - The DMH is NOT the SCN; the DMH is the relay, the SCN is the
      clock. Do not draft the DMH as if it were the clock.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, NKB,
      dynorphin, progesterone), 03_* (HPT, growth, GHRH, somatostatin,
      IGF-1), 04_* (satiety, leptin, ghrelin, NPY, AgRP, POMC, CART,
      insulin, PYY, GLP-1, CCK), 05_* (dopamine, GABA, monoamines,
      serotonin), 07_* (fluid, PGE2), 10_* (circadian, SCN); memory/
      stores/ (short_term, episodic, emotional_valence,
      temporal_sequence_learning, reinforcement_value_based_learning);
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          hypothalamus/periventricular_nucleus/left|right (TIDA primary
          vs. A14 supplementary; not duplicate).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          other_preoptic_nuclei/left|right (AVPV; pulse vs. surge;
          complementary pair).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          anterior/medial_area/left|right/paraventricular_nucleus
          (GHRH stimulatory vs. somatostatin inhibitory; complementary
          pair; and NPY/AgRP/POMC → PVN feeding circuit).
        * tuberal/medial_area/left|right/arcuate_nucleus ↔
          tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus (arcuate feeding → tuberal LHA; the tuberal LHA
          segment's distinctive input).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ anterior/medial_area/left|right/
          suprachiasmatic_nucleus (SCN → DMH; the deferred circadian
          relay closure).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus (DMH → posterior LHA;
          circadian-to-arousal gating).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ tuberal/lateral_area/left|right/
          tuberal_part_of_lateral_nucleus (DMH → tuberal LHA;
          circadian-to-feeding-arousal gating).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          anterior/medial_area/left|right/anterior_hypothalamic_
          nucleus (VMH thermogenic sympathetic vs. AHN parasympathetic;
          complementary pair).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          posterior/medial_area/left|right/posterior_nucleus (VMH
          thermogenic drive vs. PHN sympathetic outflow; complementary
          pair).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          midbrain/tegmentum/periaqueductal_gray (defensive aggression
          motor patterns; PAG is midline-adjacent — verify).
    - Connects upward to hypothalamus/tuberal/.
"""