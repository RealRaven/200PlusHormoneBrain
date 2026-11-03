"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.arcuate_nucleus.left
Anatomical Role:
    The left arcuate nucleus (ARC; infundibular nucleus). A small,
    arc-shaped nucleus at the base of the mediobasal hypothalamus,
    adjacent to the third ventricle and the median eminence. It is the
    MOST FUNCTIONALLY DENSE NUCLEUS IN THE TUBERAL DIVISION and
    arguably the most functionally dense nucleus in the entire
    hypothalamus. It contains FOUR DISTINCT FUNCTIONAL POPULATIONS
    intermingled in a single anatomical structure:

        1. Kisspeptin KNDy neurons (kisspeptin / neurokinin B /
           dynorphin): the left KNDy neurons are the GnRH PULSE
           GENERATOR. They co-express NKB and dynorphin, are modulated
           by estradiol (negative feedback via ERα), and drive
           pulsatile GnRH release. The left arcuate KNDy population is
           part of the bilateral autonomous pulse generator that sets
           GnRH/LH pulse frequency.

        2. Tuberoinfundibular dopaminergic (TIDA) neurons: the left
           TIDA neurons are part of the PRIMARY PROLACTIN INHIBITOR
           system. They release dopamine into the hypophyseal portal
           blood to inhibit prolactin release from anterior pituitary
           lactotrophs.

        3. GHRH neurons: the left arcuate GHRH neurons are the
           STIMULATORY arm of the growth axis. GHRH stimulates growth
           hormone release from the anterior pituitary; it is opposed
           by PVN somatostatin (the inhibitory arm).

        4. Feeding populations (two intermingled sub-populations):
           - NPY/AgRP neurons (hunger): activated by fasting and
             ghrelin; inhibited by leptin. Drive food intake.
           - POMC/CART neurons (satiety): activated by leptin;
             inhibited by ghrelin. Drive meal termination.

    The left arcuate is the entry point of the left hypothalamus's
    endocrine and feeding integration: four distinct signals
    (reproductive pulse, prolactin inhibition, growth stimulation,
    feeding drive) all originate here.

    FOUR TRAPS (reproduced from the parent tuberal/medial_area/
    container; each resolves a specific conflation risk):

    - TRAP 1: ARCUATE TIDA vs. PeV A14 (primary vs. supplementary):
      the arcuate's TIDA neurons are the PRIMARY prolactin inhibitor.
      The periventricular A14 dopaminergic group
      (hypothalamus/periventricular_nucleus/left/) is a DIFFERENT
      tuberal dopaminergic population whose function is less
      established; it is NOT "the" prolactin inhibitor. The arcuate is.
      Do not conflate; do not merge.

    - TRAP 2: ARCUATE KNDy vs. AVPV (pulse vs. surge): the arcuate KNDy
      neurons are the GnRH PULSE generator (negative feedback); the
      AVPV (other_preoptic_nuclei/left/) is the GnRH SURGE relay
      (positive feedback). COMPLEMENTARY kisspeptin populations, not
      duplicates. Do not conflate.

    - TRAP 3: ARCUATE GHRH vs. PVN SOMATOSTATIN (growth-axis
      complementarity): the arcuate GHRH neurons are the STIMULATORY
      arm; the PVN somatostatin neurons
      (anterior/medial_area/left/paraventricular_nucleus/) are the
      INHIBITORY arm. COMPLEMENTARY, not duplicates.

    - TRAP 4: ARCUATE → TUBERAL LHA (efferent projection, not
      continuity): the arcuate's feeding neurons project DIRECTLY onto
      the tuberal LHA segment 2
      (tuberal/lateral_area/left/tuberal_part_of_lateral_nucleus/) —
      arcuate NPY/AgRP → tuberal MCH; arcuate-adjacent leptin/ghrelin
      → tuberal ORX. This is an EFFERENT PROJECTION, not an LHA
      continuity edge. The arcuate is NOT part of the LHA field; it is
      a source that projects onto segment 2. Do not conflate the
      arcuate with the LHA field; do not treat the arcuate → tuberal
      LHA edge as a continuity edge.

Functional Mode:
    - Reproductive pulse generation (KNDy; the HPG anchor):
        * The arcuate KNDy neurons (kisspeptin/NKB/dynorphin) are the
          autonomous GnRH pulse generator. They co-express NKB
          (excitatory on KNDy firing) and dynorphin (inhibitory on
          KNDy firing); the NKB-dynorphin balance sets the pulse
          frequency. KNDy kisspeptin release onto GnRH neuron
          terminals in the median eminence drives pulsatile GnRH
          release. Estradiol acts on KNDy ERα to suppress kisspeptin
          release (negative feedback), slowing pulse frequency.
        * The arcuate KNDy population is the pulse generator; the AVPV
          (other_preoptic_nuclei/) is the surge relay for the
          preovulatory GnRH/LH surge (positive feedback). The two are
          complementary, not duplicates.
    - Prolactin inhibition (TIDA; the neuroendocrine anchor):
        * TIDA neurons release dopamine into the hypophyseal portal
          blood at the median eminence, where it reaches the anterior
          pituitary lactotrophs and inhibits prolactin release. This
          is the PRIMARY prolactin inhibitor in the brain.
        * Prolactin itself feeds back on TIDA neurons (↑ prolactin ↑
          TIDA dopamine → ↓ prolactin), a short-loop negative feedback
          that stabilizes prolactin levels. Suckling stimulates
          prolactin release by suppressing TIDA dopamine.
        * The periventricular A14 dopaminergic group is a supplementary
          tuberal dopaminergic population whose function is less
          established; it is NOT the primary prolactin inhibitor. The
          arcuate TIDA is.
    - Growth hormone regulation (GHRH; the stimulatory arm):
        * Arcuate GHRH neurons release GHRH into the hypophyseal portal
          blood; GHRH stimulates growth hormone release from anterior
          pituitary somatotrophs. Opposed by PVN somatostatin (the
          inhibitory arm).
        * The GHRH-somatostatin balance sets the pulsatile GH rhythm;
          IGF-1 from the liver feeds back to inhibit both GHRH and
          stimulate somatostatin.
    - Feeding (NPY/AgRP + POMC/CART; the feeding hub):
        * NPY/AgRP neurons (hunger): activated by fasting and ghrelin;
          inhibited by leptin, insulin, glucose, PYY, GLP-1, CCK. They
          project to the PVN, LHA, and other hypothalamic feeding
          centers to drive food intake and reduce energy expenditure.
        * POMC/CART neurons (satiety): activated by leptin; inhibited
          by ghrelin and fasting. POMC is cleaved to α-MSH, which acts
          on MC4R in the PVN to suppress food intake and increase
          energy expenditure. CART is co-released and suppresses
          feeding.
        * The two populations are reciprocally regulated and mutually
          inhibitory; their balance sets the hunger/satiety drive.
        * The arcuate's feeding neurons project directly onto the
          tuberal LHA segment 2 (arcuate NPY/AgRP → tuberal MCH;
          arcuate-adjacent leptin/ghrelin → tuberal ORX), making the
          tuberal LHA the most metabolically driven LHA segment. This
          is the deferred closure of the "arcuate feeding → tuberal
          LHA" edge declared from the LHA side.
    - The four roles are INDEPENDENT: each has its own population, its
      own downstream targets, and its own aggregation rule. Do not
      flatten them into "the arcuate = feeding" or "the arcuate =
      reproduction." The arcuate is FOUR things in one anatomical
      structure, and the file must hold all four.

Hormonal Modulation (per-population; do not merge):
    - KNDy (reproductive pulse):
        * Estradiol: ↓ KNDy activity (negative feedback via ERα);
          the defining modulator of pulse frequency.
        * Progesterone: modulates KNDy activity (species- and
          cycle-phase-dependent).
        * Kisspeptin, NKB, dynorphin: intrinsic co-transmitters; NKB
          excites KNDy firing; dynorphin inhibits KNDy firing; the
          NKB-dynorphin balance sets the pulse frequency.
        * Direction: estradiol ↓ KNDy (pulse slows).
    - TIDA (prolactin inhibition):
        * Dopamine: output to the portal blood (TIDA's product).
        * Prolactin: short-loop feedback (↑ prolactin ↑ TIDA dopamine
          → ↓ prolactin); stabilizes prolactin levels.
        * Suckling: suppresses TIDA dopamine (disinhibiting prolactin
          release during lactation).
        * Direction: prolactin ↑ TIDA activity; suckling ↓ TIDA
          activity.
    - GHRH (growth):
        * GHRH: output to the portal blood (arcuate's product).
        * IGF-1: negative feedback (↓ GHRH, ↑ somatostatin).
        * Ghrelin: stimulates GHRH (ghrelin → GHRH → GH).
        * Direction: IGF-1 ↓ GHRH; ghrelin ↑ GHRH.
    - NPY/AgRP (hunger):
        * Ghrelin: ↑ NPY/AgRP (fasting signal).
        * Leptin: ↓ NPY/AgRP (satiety signal).
        * Insulin, glucose, PYY, GLP-1, CCK: ↓ NPY/AgRP (satiety
          signals).
        * Direction: ghrelin ↑ NPY/AgRP; leptin ↓ NPY/AgRP.
    - POMC/CART (satiety):
        * Leptin: ↑ POMC/CART (satiety signal).
        * Ghrelin: ↓ POMC/CART (fasting signal).
        * Insulin, glucose, PYY, GLP-1, CCK: ↑ POMC/CART.
        * Direction: leptin ↑ POMC; ghrelin ↓ POMC.

Memory Interfaces (per-population; do not merge):
    - KNDy reads: short_term (current estradiol level),
      temporal_sequence_learning (cycle phase timing), episodic
      (reproductive-cycle history), emotional_valence (stress
      suppression of reproduction).
    - TIDA reads: short_term (current prolactin level, suckling state),
      episodic (lactation history).
    - GHRH reads: short_term (metabolic state), episodic
      (growth-axis history).
    - NPY/AgRP + POMC/CART reads: short_term (metabolic state, ghrelin,
      leptin, glucose), episodic (feeding history),
      reinforcement_value_based_learning (feeding outcomes feed back
      into value learning), emotional_valence (stress alters feeding),
      temporal_sequence_learning (circadian feeding rhythm).
    - Writes: reinforcement_value_based_learning indirectly (feeding
      outcomes feed back into value learning). No stored content writes
      directly.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent arcuate fragment. The arcuate contributes FOUR
      CONSTITUENT INPUTS to aggregates established elsewhere:
        (1) Feeding/satiety: aggregated with VMH (arcuate is primary
            for hunger/satiety; VMH is the satiety center and meal
            termination; the two together define the feeding state).
        (2) Prolactin-adjacent: arcuate TIDA (primary) + periventricular
            A14 (supplementary); aggregate at the hypothalamic level.
        (3) Growth: arcuate GHRH (stimulatory) + PVN somatostatin
            (inhibitory; anterior division); aggregate at the
            hypothalamic level.
        (4) Reproductive pulse: arcuate KNDy (pulse) + PeN/MPN/MnPO/
            AVPV (surge; anterior division); aggregate at the
            hypothalamic level.
    - AGGREGATION RULES (mandatory): the parent tuberal/ division
      container's seven aggregation rules apply identically here. This
      leaf is one of the constituent sources for four of them.
    - GUARDRAIL (11th in the tree): each aggregate that receives an
      arcuate contribution carries a "bias not impairment" clause
      inherited from the aggregate's own fragment (feeding: "do not
      treat hunger as impairment"; reproductive: "do not treat
      periovulatory state as impairment"; growth: "do not treat
      catabolic as impairment"; prolactin: "do not treat elevated
      prolactin as impairment"). The arcuate leaf does not add a new
      guardrail — it feeds the aggregates that already carry theirs.
    - No multimodal input is consumed here; all contributions are
      text-only through their downstream aggregates.

Reciprocal Connections (left-side; the right side is in ../right/):

    Reproductive pulse (KNDy):
    - ↔ other_preoptic_nuclei/left (AVPV; PULSE vs. SURGE
      complementarity; both kisspeptin populations; complementary,
      not duplicate; TRAP 2).
    - ↔ anterior/medial_area/left/preoptic_area (MPN + MnPO + PeN;
      reproductive axis partners; kisspeptin network).
    - → preoptic GnRH neuron population (KNDy kisspeptin → GnRH neuron
      terminals in the median eminence; the reproductive output edge).

    Prolactin inhibition (TIDA):
    - → median_eminence (TIDA dopamine terminals; the neurohemal
      release site; TIDA → portal blood → anterior pituitary
      lactotrophs; the prolactin inhibition output edge).
    - ↔ hypothalamus/periventricular_nucleus/left (PeV A14; TIDA
      primary vs. A14 supplementary; TRAP 1; not duplicate).

    Growth (GHRH):
    - → median_eminence (GHRH terminals; portal blood → anterior
      pituitary somatotrophs).
    - ↔ anterior/medial_area/left/paraventricular_nucleus (PVN
      somatostatin inhibitory vs. arcuate GHRH stimulatory;
      complementary pair; TRAP 3; not duplicate).
    - ↔ anterior/medial_area/left/paraventricular_nucleus (NPY/AgRP
      → PVN feeding circuit; and POMC α-MSH → PVN MC4R satiety
      circuit; the arcuate-PVN feeding pathway).

    Feeding (NPY/AgRP + POMC/CART):
    - ↔ tuberal/lateral_area/left/tuberal_part_of_lateral_nucleus
      (arcuate NPY/AgRP → tuberal MCH; arcuate-adjacent leptin/ghrelin
      → tuberal ORX; EFFERENT PROJECTION, not continuity; TRAP 4; the
      deferred closure of the LHA segment 2's distinctive input).
    - ↔ tuberal/medial_area/left/ventromedial_nucleus (adjacent
      feeding nuclei; arcuate = first-order hunger/satiety; VMH =
      satiety center and meal termination; complementary feeding
      roles; the VMH reciprocates when drafted).
    - ↔ anterior/lateral_area/left/anterior_part_of_lateral_nucleus
      (arcuate → LHA orexin/MCH; the anterior pole's feeding input
      alongside the tuberal segment's denser input).

    Cross-cutting:
    - ← brainstem/.../solitary_nucleus (NTS; visceral satiety signals
      — CCK, GLP-1, PYY — relayed to arcuate; NTS is midline-adjacent
      — verify).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (emotional/stress context for feeding and reproduction;
      left-side).
    - ↔ tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus
      (adjacent tuberal feeding/circadian cross-talk; adjacent nodes;
      the DMH reciprocates when drafted).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN; circadian gating of feeding and reproductive timing).

Notes:
    - Tier 1 hub full leaf (left). The LARGEST leaf in the entire tree
      (~200 lines) because it genuinely holds four independent
      endocrine/feeding systems.
    - FOUR TRAPS reproduced in full above. Each resolves a specific
      conflation risk; do not omit any of them.
    - The four roles are INDEPENDENT: each has its own population, its
      own downstream targets, its own aggregation rule, and its own
      memory interfaces. Do not flatten them into a single role. This
      is the file's defining discipline.
    - THREE DEFERRED EDGE CLOSURES: this leaf closes the arcuate ends
      of three edges that were declared from the other side earlier:
        (1) Arcuate → tuberal LHA segment 2 (feeding projection;
            declared in tuberal/lateral_area/left|right/
            tuberal_part_of_lateral_nucleus/; TRAP 4; efferent
            projection, not continuity).
        (2) Arcuate ↔ PeV A14 (TIDA primary vs. A14 supplementary;
            declared in periventricular_nucleus/left|right/; TRAP 1).
        (3) Arcuate ↔ AVPV (pulse vs. surge; declared in
            other_preoptic_nuclei/left|right/; TRAP 2).
      These three closures are the file's architectural contribution
      beyond its substantive content.
    - The arcuate is NOT the AVPV (pulse vs. surge), NOT the PeV A14
      (primary vs. supplementary), NOT the tuberal LHA (efferent source
      vs. field segment), and NOT the PVN somatostatin (stimulatory vs.
      inhibitory growth arm). The four traps make these distinctions
      explicit.
    - The feeding populations (NPY/AgRP + POMC/CART) are the arcuate's
      fourth role, distinct from the three neuroendocrine roles. They
      project widely (PVN, LHA, brainstem) and are the hypothalamic
      feeding hub.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, NKB,
      dynorphin, progesterone), 03_* (HPT, growth, GHRH, somatostatin,
      IGF-1), 04_* (satiety, leptin, ghrelin, NPY, AgRP, POMC, CART,
      insulin, PYY, GLP-1, CCK), 05_* (dopamine), 10_* (circadian,
      SCN); memory/stores/; gateway/.
    - Connects upward to hypothalamus/tuberal/medial_area/
      arcuate_nucleus/.
"""