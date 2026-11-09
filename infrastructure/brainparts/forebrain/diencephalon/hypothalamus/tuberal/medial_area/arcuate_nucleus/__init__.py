"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.arcuate_nucleus
Anatomical Role:
    The arcuate nucleus (ARC; also called the infundibular nucleus) is a
    small, arc-shaped nucleus at the base of the mediobasal
    hypothalamus, adjacent to the third ventricle and the median
    eminence. It is the MOST FUNCTIONALLY DENSE NUCLEUS IN THE TUBERAL
    DIVISION and arguably the most functionally dense nucleus in the
    entire hypothalamus. It contains four distinct functional
    populations intermingled in a single anatomical structure:

        1. Kisspeptin KNDy neurons (kisspeptin / neurokinin B /
           dynorphin): the GnRH PULSE GENERATOR. These neurons
           co-express NKB and dynorphin, are modulated by estradiol
           (negative feedback via ERα), and drive pulsatile GnRH
           release. The arcuate KNDy population is the autonomous pulse
           generator that sets GnRH/LH pulse frequency.

        2. Tuberoinfundibular dopaminergic (TIDA) neurons: the
           PRIMARY PROLACTIN INHIBITOR. These neurons release dopamine
           into the hypophyseal portal blood to inhibit prolactin
           release from anterior pituitary lactotrophs.

        3. GHRH neurons: the STIMULATORY arm of the growth axis. GHRH
           stimulates growth hormone release from the anterior
           pituitary; it is opposed by PVN somatostatin (the inhibitory
           arm).

        4. Feeding populations (two intermingled sub-populations):
           - NPY/AgRP neurons (hunger): activated by fasting and
             ghrelin; inhibited by leptin. Drive food intake.
           - POMC/CART neurons (satiety): activated by leptin;
             inhibited by ghrelin. Drive meal termination.

    The arcuate is the entry point of the hypothalamus's endocrine and
    feeding integration: four distinct signals (reproductive pulse,
    prolactin inhibition, growth stimulation, feeding drive) all
    originate here.

    FOUR TRAPS apply (reproduced from the parent tuberal/medial_area/
    container):

    - TRAP 1: ARCUATE TIDA vs. PeV A14 (primary vs. supplementary):
      the arcuate's TIDA neurons are the PRIMARY prolactin inhibitor.
      The periventricular A14 dopaminergic group
      (hypothalamus/periventricular_nucleus/left|right/) is a DIFFERENT
      tuberal dopaminergic population whose function is less
      established; it is NOT "the" prolactin inhibitor. The arcuate is.
      Do not conflate; do not merge.

    - TRAP 2: ARCUATE KNDy vs. AVPV (pulse vs. surge): the arcuate KNDy
      neurons are the GnRH PULSE generator (negative feedback); the
      AVPV (other_preoptic_nuclei/left|right/) is the GnRH SURGE relay
      (positive feedback). The two are COMPLEMENTARY kisspeptin
      populations, not duplicates. Do not conflate; do not merge.

    - TRAP 3: ARCUATE GHRH vs. PVN SOMATOSTATIN (growth-axis
      complementarity): the arcuate GHRH neurons are the STIMULATORY
      arm; the PVN somatostatin neurons
      (anterior/medial_area/left|right/paraventricular_nucleus/) are
      the INHIBITORY arm. The two are COMPLEMENTARY, not duplicates.
      Do not conflate.

    - TRAP 4: ARCUATE vs. TUBERAL LHA SEGMENT 2 (feeding-to-arousal
      projection, not continuity): the arcuate's feeding neurons
      project DIRECTLY onto the tuberal LHA segment 2
      (tuberal/lateral_area/left|right/tuberal_part_of_lateral_
      nucleus/) — arcuate NPY/AgRP → tuberal MCH; arcuate-adjacent
      leptin/ghrelin → tuberal ORX. This is a DIFFERENT relationship
      from the LHA continuum: the arcuate is NOT part of the LHA
      field; it is an EFFERENT SOURCE that projects onto segment 2.
      Do not conflate the arcuate with the LHA field; do not treat the
      arcuate → tuberal LHA edge as a continuity edge.

Functional Mode:
    The full four-role description (KNDy pulse, TIDA prolactin, GHRH
    growth, NPY/AgRP + POMC/CART feeding) is documented in
    left/__init__.py (the full leaf). Summary here:
        - Reproductive pulse generation (KNDy): GnRH pulse frequency;
          estradiol negative feedback.
        - Prolactin inhibition (TIDA): dopamine into the portal blood
          → ↓ prolactin release; the PRIMARY prolactin inhibitor.
        - Growth (GHRH): stimulatory arm of the growth axis; opposing
          PVN somatostatin.
        - Feeding (NPY/AgRP + POMC/CART): the brain's hypothalamic
          feeding hub; the two intermingled populations drive hunger
          and satiety respectively.
    The arcuate is the entry point of tuberal endocrine and feeding
    integration; its four roles are independent (each has its own
    population and its own downstream targets) but co-located.

Hormonal Modulation (container-level summary; full list in left/):
    - KNDy: estradiol (↓ pulse; negative feedback via ERα);
      progesterone; kisspeptin, NKB, dynorphin (intrinsic).
    - TIDA: dopamine (output); prolactin (feedback; ↑ prolactin ↑
      TIDA dopamine → ↓ prolactin).
    - GHRH: GHRH (output); IGF-1 (feedback; ↓ GHRH).
    - NPY/AgRP: ghrelin (↑); leptin (↓); fasting (↑); refeeding (↓).
    - POMC/CART: leptin (↑); ghrelin (↓); insulin, glucose, PYY,
      GLP-1, CCK.
    - Direction summary: estradiol ↓ KNDy (negative feedback);
      dopamine (TIDA) ↓ prolactin; IGF-1 ↓ GHRH; ghrelin ↑ NPY/AgRP;
      leptin ↑ POMC and ↓ NPY/AgRP. These are the actionable
      directions.

Memory Interfaces (container-level summary; full list in left/):
    - Reads: short_term (metabolic state, reproductive-hormonal state,
      prolactin level), episodic (feeding and reproductive history),
      emotional_valence (stress suppression of feeding and
      reproduction), temporal_sequence_learning (circadian feeding
      rhythm, estrous cycle timing).
    - Writes: reinforcement_value_based_learning indirectly (feeding
      outcomes feed back into value learning).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The container does not emit fragments itself. The arcuate
      contributes FOUR constituent inputs to aggregates established
      elsewhere:
        (1) Feeding/satiety: aggregated with VMH (the arcuate is
            primary for hunger/satiety; the VMH is the satiety center;
            the two together define the feeding state).
        (2) Prolactin-adjacent: arcuate TIDA (primary) + periventricular
            A14 (supplementary); aggregate at the hypothalamic level.
        (3) Growth: arcuate GHRH (stimulatory) + PVN somatostatin
            (inhibitory; anterior division); aggregate at the
            hypothalamic level.
        (4) Reproductive pulse: arcuate KNDy (pulse) + PeN/MPN/MnPO/
            AVPV (surge; anterior division); aggregate at the
            hypothalamic level.
    - AGGREGATION RULES (mandatory): the parent tuberal/ division
      container's seven aggregation rules apply identically here. The
      leaves implement them; this container references them.
    - No independent arcuate fragment is emitted. The four roles
      aggregate into existing fragments.
    - Guardrails: the feeding, reproductive, growth, and prolactin
      fragments each carry their own "bias not impairment" clause (in
      the aggregate that carries them). The arcuate does not add a new
      guardrail.

Children (one child pair — full leaf + delta):
    - left/    ★★ FULL TIER 1 LEAF. The complete arcuate content:
                 four roles, all hormone directions, all memory
                 interfaces, the feeding/satiety fragment spec, the
                 prolactin-adjacent fragment spec, the growth fragment
                 spec, the reproductive pulse fragment spec, and all
                 reciprocal connections.
    - right/   Delta mirror of left/, differing only in the right-side
                 reciprocal edges. No functional asymmetry documented.

    No pointer deltas (the mammillary-nuclei pattern is unique to the
    posterior division). The arcuate is a real, distinct nucleus
    documented here in full.

Notes:
    - Tier 1 hub container (not a pointer, not a division container).
      The full leaf lives in left/; right/ is a delta.
    - The arcuate is marked ★★ (double star) at the parent tuberal/
      division container. It is the highest-priority leaf in the
      entire tuberal division. Draft it first among the three tuberal
      medial leaves (arcuate, VMH, DMH).
    - FOUR TRAPS reproduced above. All four apply to the arcuate
      specifically:
        * Trap 1 (TIDA vs. A14) → prolactin role.
        * Trap 2 (KNDy vs. AVPV) → reproductive pulse role.
        * Trap 3 (GHRH vs. somatostatin) → growth role.
        * Trap 4 (arcuate vs. tuberal LHA) → feeding role.
      Do not omit any of them.
    - The arcuate's four roles are INDEPENDENT: each has its own
      population, its own downstream targets, and its own aggregation
      rule. Do not flatten them into "the arcuate = feeding" or "the
      arcuate = reproduction." The arcuate is FOUR things in one
      anatomical structure, and the file must hold all four.
    - The arcuate leaf must reciprocate:
        * Periventricular A14 (TIDA primary vs. A14 supplementary;
          not duplicate).
        * AVPV (pulse vs. surge; complementary pair).
        * PVN (GHRH stimulatory vs. somatostatin inhibitory;
          complementary pair; and NPY/AgRP/POMC → PVN feeding
          circuit).
        * Tuberal LHA segment 2 (arcuate feeding → tuberal LHA;
          efferent projection, not continuity edge; the deferred
          closure of the LHA segment 2's distinctive input).
    - The arcuate is NOT the AVPV; the arcuate is the pulse generator,
      the AVPV is the surge relay. Both are kisspeptin populations,
      but functionally complementary, not duplicates.
    - The arcuate is NOT the periventricular A14; the arcuate TIDA is
      the primary prolactin inhibitor, the A14 is supplementary. Do
      not let a future contributor conflate them.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, NKB,
      dynorphin, progesterone), 03_* (HPT, growth, GHRH, somatostatin,
      IGF-1), 04_* (satiety, leptin, ghrelin, NPY, AgRP, POMC, CART,
      insulin, PYY, GLP-1, CCK), 05_* (dopamine), 10_* (circadian);
      memory/stores/; gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * arcuate_nucleus/left|right ↔
          hypothalamus/periventricular_nucleus/left|right (TIDA
          primary vs. A14 supplementary; not duplicate).
        * arcuate_nucleus/left|right ↔ other_preoptic_nuclei/left|
          right (AVPV; pulse vs. surge; complementary pair).
        * arcuate_nucleus/left|right ↔
          anterior/medial_area/left|right/paraventricular_nucleus
          (GHRH stimulatory vs. somatostatin inhibitory; complementary
          pair; and NPY/AgRP/POMC → PVN feeding circuit).
        * arcuate_nucleus/left|right ↔
          tuberal/lateral_area/left|right/tuberal_part_of_lateral_
          nucleus (arcuate feeding → tuberal LHA; efferent projection;
          the deferred closure of the LHA segment 2's distinctive
          input).
        * arcuate_nucleus/left|right ↔
          tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus (adjacent tuberal feeding/circadian cross-talk;
          adjacent nodes; the DMH reciprocates when drafted).
        * arcuate_nucleus/left|right ↔
          tuberal/medial_area/left|right/ventromedial_nucleus (adjacent
          feeding nuclei; arcuate = hunger/satiety first-order;
          VMH = satiety center and meal termination; complementary
          feeding roles; the VMH reciprocates when drafted).
    - Connects upward to hypothalamus/tuberal/medial_area/.
"""