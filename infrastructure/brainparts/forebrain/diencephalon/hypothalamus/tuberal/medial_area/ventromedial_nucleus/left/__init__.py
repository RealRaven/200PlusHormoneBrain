"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.ventromedial_nucleus.left
Anatomical Role:
    The left ventromedial nucleus of the hypothalamus (VMH). A large,
    spherical nucleus in the left mediobasal tuberal hypothalamus,
    ventral to the left DMH and anterior to the left arcuate. One of
    the most extensively studied hypothalamic nuclei, with FOUR
    principal functional roles distributed across subdivisions
    (documented WITHIN this file, not as child nodes):

        - VMHc (central subdivision): satiety and meal termination.
        - VMHvl (ventrolateral subdivision): defensive aggression
          (male-typical function) and female sexual behavior
          (female-typical function). Strongly sexually dimorphic
          (female-larger for receptivity circuits; male-larger for
          aggression circuits in some subregions).
        - VMHdm (dorsomedial subdivision): thermogenic sympathetic
          drive (BAT activation, shivering); defensive behavior.
        - VMH shell: surrounds the core subdivisions; contributes to
          the broader VMH functions.

    The four roles:
        1. Satiety and meal termination (VMHc; the anchor role): the
           classic "satiety center." Integrates satiety signals (leptin,
           insulin, CCK, serotonin) and drives meal termination.
           VMH lesions produce hyperphagia and obesity (the classic
           "ventromedial hypothalamic obesity syndrome").
        2. Defensive aggression (VMHvl): drives defensive aggression
           via projections to the PAG and the hypothalamic attack
           area. Testosterone and estrogen modulate the aggression
           circuit; sexually dimorphic (male-larger in aggression
           circuits).
        3. Thermoregulation (VMHdm): drives brown-adipose-tissue (BAT)
           thermogenesis and shivering via sympathetic outflow (RVLM →
           IML → sympathetic → BAT). It is the thermogenic EFFECTOR
           complement to the preoptic thermoregulatory CONTROLLER.
        4. Female sexual behavior (VMHvl): the principal hypothalamic
           nucleus for female sexual receptivity (lordosis in rodents).
           Estrogen receptor-alpha and progesterone receptor-rich;
           estrogen → progesterone priming → receptivity. Strongly
           sexually dimorphic (female-larger VMHvl).

    FOUR TRAPS (reproduced from the parent tuberal/medial_area/
    container and the VMH hub container):

    - TRAP 4: VMH vs. DMH (adjacent-nuclei trap). The left DMH
      (tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus/) is
      adjacent but functionally distinct. VMH = satiety/aggression/
      thermoregulation/sexual behavior. DMH = circadian relay. Do not
      merge.

    - TRAP 7a: VMH vs. AHN (thermoregulatory complementarity). The
      VMH's thermogenic sympathetic drive (BAT, shivering) is the
      EFFECTOR arm; the AHN's thermoregulatory control
      (anterior/medial_area/left/anterior_hypothalamic_nucleus/) is
      the parasympathetic thermoregulatory arm. COMPLEMENTARY; part of
      the thermoregulatory triangle (preoptic controller + AHN + VMH +
      PHN). Do not merge.

    - TRAP 7b: VMH vs. PHN (sympathetic outflow complementarity). The
      VMH's thermogenic sympathetic drive is complementary to the
      PHN's (posterior/medial_area/left/posterior_nucleus/) whole-body
      sympathetic outflow. COMPLEMENTARY, not duplicates; the VMH's
      sympathetic contribution is specifically thermogenic. Do not
      merge.

    - VMH vs. ARCUATE (feeding complementarity). The left arcuate
      (tuberal/medial_area/left/arcuate_nucleus/) houses the
      first-order hunger/satiety populations (NPY/AgRP + POMC/CART);
      the VMH is the satiety center and meal termination nucleus.
      COMPLEMENTARY feeding roles (arcuate = first-order sensing; VMH =
      integrated meal termination). Do not merge.

Functional Mode:
    - Satiety and meal termination (VMHc; the anchor function):
        * The VMHc integrates satiety signals (leptin, insulin, CCK,
          serotonin, PYY, GLP-1) relayed from the arcuate and the
          brainstem (NTS). It drives meal termination and suppresses
          further food intake.
        * Classic "ventromedial hypothalamic obesity syndrome": VMH
          lesions → hyperphagia (overeating) + obesity. The lesion
          removes the satiety brake; feeding continues past normal
          satiety. This is the file's defining clinical fact about
          the VMH's satiety role.
        * The VMH is the DOWNSTREAM INTEGRATOR of feeding; the arcuate
          is the first-order sensor. The two together define the
          feeding state.
    - Defensive aggression (VMHvl):
        * The VMHvl drives defensive aggression (the "attack" response
          in rodents; defensive behavior in humans) via projections to
          the PAG and the hypothalamic attack area (AHN-adjacent).
        * Testosterone (organizing and activational) increases
          aggression; estrogen modulates the circuit. Sexually
          dimorphic (male-larger in aggression circuits in some
          subregions).
        * Optogenetic activation of VMHvl elicits attack behavior;
          inhibition suppresses it.
    - Thermoregulation (VMHdm; thermogenic effector):
        * The VMHdm drives BAT thermogenesis and shivering via
          sympathetic outflow (VMH → RVLM → IML → sympathetic chain →
          BAT). Activation increases core temperature; lesions impair
          cold defense.
        * The VMH is the EFFECTIVE EFFECTOR in the thermoregulatory
          triangle; the preoptic area is the CONTROLLER that senses
          temperature and issues command signals to the VMH and AHN.
        * The sympathetic contribution from the VMH is specifically
          THERMOGENIC; the PHN's sympathetic contribution is
          whole-body (cardiovascular, pupillary, arousal). The two
          are complementary, not duplicates.
    - Female sexual behavior (VMHvl):
        * The VMHvl is the principal hypothalamic nucleus for female
          sexual receptivity (lordosis in rodents). Estrogen
          receptor-alpha and progesterone receptor-rich.
        * Estrogen → progesterone priming → receptivity. The
          estrous-cycle hormonal sequence (rising estradiol then
          progesterone) activates the VMHvl receptivity circuit.
        * Strongly sexually dimorphic (female-larger VMHvl); male-typical
          VMHvl circuits instead drive aggression.
        * Oxytocin, kisspeptin, and GnRH inputs modulate the
          receptivity circuit in coordination with the reproductive
          axis.
    - The four roles are anatomically distributed across subdivisions
      but functionally co-located in a single nucleus. Each has its own
      population, its own downstream targets, and its own functional
      context; do not flatten them into a single role.

Hormonal Modulation (per role; do not merge):
    - Satiety (VMHc):
        * Leptin: ↑ VMHc activity (satiety signal; via arcuate
          POMC → VMH relay and direct receptor expression).
        * Insulin: ↑ VMHc activity (satiety signal).
        * CCK, PYY, GLP-1: ↑ VMHc activity (satiety signals relayed
          from the NTS).
        * Serotonin: ↑ VMHc activity (satiety; the basis of
          serotonergic appetite suppression).
        * Ghrelin: ↓ VMHc activity (fasting signal).
        * Direction: leptin ↑ satiety; ghrelin ↓ satiety.
    - Defensive aggression (VMHvl; male-typical):
        * Testosterone: ↑ VMHvl aggression circuit activity (organizing
          and activational).
        * Estrogen: modulates the aggression circuit (via aromatized
          testosterone).
        * Serotonin: ↓ aggression (the anti-aggression neuromodulator).
        * GABA: intrinsic modulation.
        * Direction: testosterone ↑ aggression; serotonin ↓ aggression.
    - Thermoregulation (VMHdm):
        * PGE2: ↑ VMHdm thermogenic activity (fever pathway).
        * Pyrogens (IL-1β, etc.): ↑ VMHdm thermogenesis (fever).
        * Estradiol: modulates thermoregulatory tone (hot-flush
          cross-talk with the preoptic area).
        * Direction: PGE2 ↑ thermogenesis; pyrogens ↑ thermogenesis.
    - Female sexual behavior (VMHvl; female-typical):
        * Estradiol: ↑ VMHvl receptivity circuit activity
          (estrogen-priming phase).
        * Progesterone: ↑ receptivity after estradiol priming
          (progesterone-facilitation phase).
        * Oxytocin: ↑ receptivity (facilitation).
        * Kisspeptin, GnRH: modulate the receptivity circuit in
          coordination with the reproductive axis.
        * Direction: estradiol ↑ receptivity; progesterone (after
          estradiol priming) ↑ receptivity; oxytocin ↑ receptivity.
    - Sex differences: the VMHvl circuit is functionally dimorphic:
      female-typical (receptivity) vs. male-typical (aggression). The
      same subregion carries different functions by sex. Document this
      factually; do not overclaim beyond what the literature
      establishes.

Memory Interfaces:
    - Reads:
        * short_term: current metabolic state (satiety buffer), thermal
          state buffer, arousal/aggression context buffer, and
          reproductive-hormonal state buffer.
        * episodic: feeding history, aggression history,
          thermoregulatory history, reproductive history.
        * emotional_valence: stress and threat context (aggression and
          defensive behavior are threat-sensitive; feeding is
          stress-sensitive).
    - Writes: none directly. The VMH drives somatic and autonomic
      output, not stored content. It modulates the state under which
      other regions (arcuate, hippocampus, amygdala, cortex) read and
      write memory, but does not itself write.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent VMH fragment. The VMH contributes TWO CONSTITUENT
      INPUTS to aggregates established elsewhere:
        (1) Feeding/satiety: aggregated with the arcuate (arcuate =
            first-order hunger/satiety; VMH = satiety center and meal
            termination; together they define the feeding state). The
            aggregate's guardrail ("do not treat hunger as impairment")
            covers both contributions.
        (2) Autonomic/thermoregulatory: aggregated with the AHN
            (parasympathetic thermoregulatory control) and the PHN
            (whole-body sympathetic outflow). The VMH contributes the
            thermogenic sympathetic drive; the aggregate carries the
            full thermoregulatory and autonomic state. The aggregate's
            guardrail ("do not treat sympathetic-dominance as
            impairment") covers all three contributions.
    - The aggression and female sexual behavior roles are documented
      in this leaf but do NOT emit separate fragments. They are
      contextual (behavioral) roles that the model can reference
      where relevant, not state biases that need their own prompt
      blocks.
    - AGGREGATION RULES (mandatory for the implementer): the parent
      tuberal/medial_area/ container's rules apply. The VMH's feeding
      contribution aggregates with the arcuate's; its thermoregulatory
      contribution aggregates with the AHN's and PHN's. Do not emit a
      separate VMH fragment.
    - The VMH leaf is one of the rare leaves in the tree that feeds
      TWO aggregates but emits ZERO independent fragments. It is a
      constituent-only contributor.
    - No multimodal input is consumed here; all contributions are
      text-only through their downstream aggregates.

Reciprocal Connections (left-side; the right side is in ../right/):

    Feeding complementarity (the anchor):
    - ↔ tuberal/medial_area/left/arcuate_nucleus (VMH = satiety
      center/meal termination vs. arcuate = first-order
      hunger/satiety; COMPLEMENTARY feeding roles, not duplicate; the
      arcuate leaf declared this relationship; this file closes it on
      the VMH side).

    Thermoregulatory triangle (complementary pairs):
    - ↔ anterior/medial_area/left/anterior_hypothalamic_nucleus (VMH
      thermogenic effector vs. AHN parasympathetic thermoregulatory
      control; TRAP 7a; complementary pair, not duplicate; the AHN leaf
      declared this relationship; this file closes it on the VMH side).
    - ↔ posterior/medial_area/left/posterior_nucleus (VMH thermogenic
      sympathetic drive vs. PHN whole-body sympathetic outflow; TRAP
      7b; complementary pair, not duplicate; the PHN leaf declared
      this relationship; this file closes it on the VMH side).
    - ↔ anterior/medial_area/left/preoptic_area (thermoregulatory
      CONTROLLER; the preoptic is the controller, the VMH is the
      effector; complementary roles; the preoptic initiates thermal
      commands that the VMH executes).

    Thermoregulatory effector output:
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic premotor output;
      RVLM is midline-adjacent — verify).
    - → spinal_cord/gray_matter/left/lateral_horn (sympathetic
      preganglionic output to BAT and vasculature; thermogenic
      sympathetic pathway).
    - → left brown adipose tissue (via the sympathetic chain;
      thermogenesis effector; the pathway is downstream of the IML —
      verify).

    Adjacent-but-distinct:
    - ↔ tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus
      (VMH vs. DMH; TRAP 4; adjacent nuclei, distinct functions, do
      not merge; the DMH is the circadian relay, the VMH is the
      satiety/aggression/thermoregulation/sexual hub).

    Aggression and defensive behavior:
    - → midbrain/tegmentum/periaqueductal_gray (defensive aggression
      motor patterns; PAG is midline-adjacent — verify).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (threat/aggression context; the amygdala → VMH edge is part of
      the defensive-aggression circuit).

    Feeding input (upstream):
    - ← tuberal/medial_area/left/arcuate_nucleus (arcuate NPY/AgRP and
      POMC → VMH; the first-order feeding signals that the VMH
      integrates; the VMH is downstream of the arcuate in the feeding
      hierarchy).
    - ← brainstem/.../solitary_nucleus (NTS; visceral satiety signals
      — CCK, PYY, GLP-1 — relayed to VMH; NTS is midline-adjacent —
      verify).

    Female sexual behavior:
    - ← other_preoptic_nuclei/left (AVPV; the estrogen-positive-feedback
      surge relay; kisspeptin/GnRH coordination with the VMHvl
      receptivity circuit; distinct reproductive roles, complementary
      within the reproductive axis).
    - ← anterior/medial_area/left/preoptic_area/medial_preoptic_nucleus
      (MPN; maternal/sexual behavior coordination; adjacent reproductive
      nodes).
    - ↔ anterior/medial_area/left/suprachiasmatic_nucleus (SCN;
      circadian gating of female sexual receptivity to the species-
      typical time of day; SCN is midline-adjacent — verify).

    Cross-cutting:
    - ← anterior/medial_area/left/suprachiasmatic_nucleus (SCN;
      circadian gating of feeding, thermoregulation, and sexual
      behavior rhythms).

Notes:
    - Tier 1 full leaf (left). THE LAST FULL LEAF IN THE ENTIRE
      HYPOTHALAMUS SUBTREE. After its right delta, only container
      corrections remain in the hypothalamus.
    - The VMH is the ONLY leaf in the entire tree that closes THREE
      deferred complementary-pair edges (VMH ↔ AHN; VMH ↔ PHN; VMH ↔
      arcuate) simultaneously. Each was declared from the other side
      earlier:
        (1) VMH ↔ AHN: declared in
            anterior/medial_area/left/anterior_hypothalamic_nucleus/
            (the AHN leaf's sympathetic/parasympathetic complementarity
            note).
        (2) VMH ↔ PHN: declared in
            posterior/medial_area/left/posterior_nucleus/ (the PHN
            leaf's sympathetic/parasympathetic complementarity note).
        (3) VMH ↔ arcuate: declared in
            tuberal/medial_area/left/arcuate_nucleus/ (the arcuate
            leaf's feeding complementarity note).
      This file closes all three on the VMH side.
    - FOUR TRAPS reproduced in full above. Each resolves a specific
      conflation risk; do not omit any of them.
    - The VMH ↔ AHN and VMH ↔ PHN complementary pairs (Traps 7a/7b)
      are the thermoregulatory triangle with the preoptic area
      (controller) + AHN (parasympathetic arm) + VMH (thermogenic
      effector) + PHN (whole-body sympathetic). The four nuclei
      together form the thermoregulatory system; no single node is
      "the" thermoregulator.
    - The VMH ↔ arcuate feeding complementarity: arcuate =
      first-order hunger/satiety; VMH = satiety center and meal
      termination. The two together define the feeding state; the two
      leaves close the complementary relationship from both sides.
    - SEX DIFFERENCES: the VMHvl circuit is functionally dimorphic
      (female-typical receptivity vs. male-typical aggression). The
      same subregion carries different functions by sex. Document
      factually; do not overclaim beyond what the literature
      establishes.
    - The classic "ventromedial hypothalamic obesity syndrome" (VMH
      lesions → hyperphagia + obesity) is the file's defining clinical
      fact about the VMH's satiety role. Document it; do not omit.
    - The subdivisions (VMHc, VMHvl, VMHdm, shell) are documented
      WITHIN this file, not as child nodes. Same convention as
      habenula's LHb/MHb and PVN's sub-populations. Do not create
      vmhc/, vmhvl/, vmhdm/, or shell/ as child nodes.
    - The VMH's aggression and female sexual behavior roles do NOT
      emit separate fragments. They are behavioral/contextual roles,
      not state biases. The model can reference them where relevant
      but the prompt does not need VMH-specific aggression or
      receptivity blocks.
    - The VMH is NOT the arcuate (first-order vs. integrated satiety);
      NOT the DMH (satiety/aggression/thermoregulation/sexual vs.
      circadian relay); NOT the AHN (thermogenic effector vs.
      parasympathetic thermoregulatory); NOT the PHN (thermogenic
      sympathetic vs. whole-body sympathetic). The four traps make
      these distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, progesterone,
      testosterone), 03_* (HPT, metabolic), 04_* (satiety, leptin,
      ghrelin, CCK, PYY, GLP-1, insulin), 05_* (serotonin, GABA),
      07_* (fluid, PGE2); memory/stores/ (short_term, episodic,
      emotional_valence); gateway/.
    - Connects upward to hypothalamus/tuberal/medial_area/
      ventromedial_nucleus/.
"""