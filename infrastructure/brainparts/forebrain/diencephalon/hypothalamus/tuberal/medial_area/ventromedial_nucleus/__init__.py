"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.ventromedial_nucleus
Anatomical Role:
    The ventromedial nucleus of the hypothalamus (VMH). A large,
    spherical nucleus in the mediobasal tuberal hypothalamus, situated
    ventral to the DMH and anterior to the arcuate. It is one of the
    most extensively studied hypothalamic nuclei, with FOUR principal
    functional roles documented across its subdivisions (documented
    WITHIN each hemisphere's leaf, not as child nodes):

        1. Satiety and meal termination: the classic "satiety center."
           VMH lesions produce hyperphagia and obesity; the nucleus
           integrates satiety signals (leptin, insulin, CCK, serotonin)
           and drives meal termination.

        2. Defensive aggression: the ventrolateral VMH (VMHvl) drives
           defensive aggression (via projections to the periaqueductal
           gray and the hypothalamic attack area). Estrogen and
           testosterone modulate the aggression circuit.

        3. Thermoregulation (thermogenesis): the VMH drives
           brown-adipose-tissue (BAT) thermogenesis and shivering via
           sympathetic outflow. It is the thermogenic EFFECTOR
           complement to the preoptic thermoregulatory CONTROLLER.

        4. Female sexual behavior: the ventrolateral VMH (VMHvl) is the
           principal hypothalamic nucleus for female sexual receptivity
           (lordosis in rodents). Estrogen receptor-alpha and
           progesterone receptor-rich; strongly sexually dimorphic
           (female-larger in the VMHvl; male-larger in the VMHdm).

    The VMH subdivisions (ventrolateral VMHvl, dorsomedial VMHdm,
    central VMHc, shell) are documented WITHIN each hemisphere's leaf,
    not as child nodes. Same convention as the habenula's LHb/MHb and
    the PVN's three sub-populations.

    FOUR TRAPS apply (reproduced from the parent tuberal/medial_area/
    container and cross-referenced):

    - TRAP 4: VMH vs. DMH (adjacent-nuclei trap). The VMH and DMH are
      adjacent but functionally distinct. VMH = satiety, aggression,
      thermoregulation, female sexual behavior. DMH = circadian relay.
      Do not merge; do not treat as a pair of similar structures.

    - TRAP 7a: VMH vs. AHN (thermoregulatory complementarity). The
      VMH's thermogenic drive (BAT activation, shivering) is the
      EFFECTOR arm; the AHN's thermoregulatory control
      (anterior/medial_area/left|right/anterior_hypothalamic_nucleus/)
      is the parasympathetic thermoregulatory arm. The two are
      COMPLEMENTARY; they form a thermoregulatory triangle with the
      preoptic thermoregulatory controller. Do not merge.

    - TRAP 7b: VMH vs. PHN (sympathetic outflow complementarity). The
      VMH's thermogenic sympathetic drive is complementary to the
      PHN's (posterior/medial_area/left|right/posterior_nucleus/)
      whole-body sympathetic outflow. The two are COMPLEMENTARY, not
      duplicates; the VMH's sympathetic contribution is specifically
      thermogenic. Do not merge.

    - VMH vs. ARCUATE (feeding complementarity). The arcuate
      (tuberal/medial_area/left|right/arcuate_nucleus/) houses the
      FIRST-ORDER hunger/satiety populations (NPY/AgRP + POMC/CART);
      the VMH is the SATIETY CENTER and MEAL TERMINATION nucleus. The
      two are COMPLEMENTARY feeding roles (arcuate = first-order
      sensing; VMH = integrated meal termination). Do not merge; the
      two together define the feeding state.

Functional Mode:
    - Satiety and meal termination (primary): the VMH integrates
      satiety signals (leptin, insulin, CCK, serotonin) and drives
      meal termination. VMH lesions produce hyperphagia and obesity
      (the classic "ventromedial hypothalamic obesity syndrome"). The
      VMH is the downstream integrator that terminates meals based on
      the arcuate's first-order hunger/satiety signals.
    - Defensive aggression (VMHvl): the VMHvl drives defensive
      aggression via projections to the PAG and the hypothalamic
      attack area. Estrogen and testosterone modulate the aggression
      circuit; the VMHvl is sexually dimorphic (female-larger for
      receptivity; male-larger for aggression in some subregions).
    - Thermoregulation (thermogenic): the VMH drives BAT thermogenesis
      and shivering via sympathetic outflow (RVLM → IML →
      sympathetic → BAT). The VMH is the thermogenic EFFECTOR
      complement to the preoptic thermoregulatory CONTROLLER; the two
      together form the thermoregulatory system.
    - Female sexual behavior (VMHvl): the VMHvl is the principal
      hypothalamic nucleus for female sexual receptivity (lordosis in
      rodents). Estrogen receptor-alpha and progesterone
      receptor-rich; estrogen → progesterone priming → receptivity.
      Strongly sexually dimorphic (female-larger VMHvl).
    - The VMH is therefore a FOUR-ROLE nucleus: satiety, aggression,
      thermoregulation, female sexual behavior. The four roles are
      anatomically distributed across subdivisions (VMHc = satiety;
      VMHvl = aggression + sexual behavior; VMHdm = defensive +
      thermogenic) but functionally co-located in a single nucleus.

Hormonal Modulation (container-level summary; full list in left/):
    - Satiety (VMHc): leptin (↑ satiety), insulin (↑ satiety), CCK
      (↑ satiety), serotonin (↑ satiety); ghrelin (↓ satiety).
    - Aggression (VMHvl): testosterone (↑ aggression), estrogen
      (modulates), serotonin (↓ aggression), GABA.
    - Thermoregulation (VMHdm): PGE2 (↑ thermogenesis), pyrogens,
      estradiol (modulates).
    - Female sexual behavior (VMHvl): estradiol (↑ receptivity;
      positive modulator of the VMHvl circuit), progesterone
      (facilitates after estradiol priming), oxytocin (facilitates
      receptivity).
    - Direction summary: leptin ↑ satiety; ghrelin ↓ satiety;
      testosterone ↑ aggression; estradiol ↑ receptivity; PGE2 ↑
      thermogenesis. These are the actionable directions.

Memory Interfaces (container-level summary; full list in left/):
    - Reads: short_term (metabolic state, thermal state, arousal/
      aggression context, reproductive-hormonal state), episodic
      (feeding, aggression, thermoregulatory, and reproductive
      history), emotional_valence (stress and threat context).
    - Writes: none directly. The VMH drives somatic and autonomic
      output, not stored content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The container does not emit fragments itself. The VMH
      contributes TWO constituent inputs to aggregates established
      elsewhere:
        (1) Feeding/satiety: aggregated with the arcuate (arcuate =
            first-order hunger/satiety; VMH = satiety center and meal
            termination; together they define the feeding state).
        (2) Autonomic/thermoregulatory: aggregated with the AHN
            (parasympathetic thermoregulatory control) and the PHN
            (sympathetic outflow). The VMH contributes the thermogenic
            sympathetic drive; the aggregate carries the full
            thermoregulatory and autonomic state.
    - The aggression and female sexual behavior roles are documented
      in the leaf but do NOT emit separate fragments. They are
      contextual (behavioral) roles that the model can reference
      where relevant, not state biases that need their own prompt
      blocks.
    - AGGREGATION RULES (mandatory): the parent tuberal/medial_area/
      container's rules apply. The VMH's feeding contribution
      aggregates with the arcuate's; its thermoregulatory contribution
      aggregates with the AHN's and PHN's.
    - No independent VMH fragment is emitted.
    - Guardrails: the feeding fragment carries the standard "do not
      treat hunger as impairment" clause; the autonomic/thermoregulatory
      fragment carries the "do not treat sympathetic-dominance as
      impairment" clause (from AHN and PHN). The VMH does not add a new
      guardrail.

Children (one child pair — full leaf + delta):
    - left/    ★ FULL TIER 1 LEAF. The complete VMH content:
                 four roles, all hormone directions, all memory
                 interfaces, the feeding/satiety contribution, the
                 thermoregulatory contribution, and all reciprocal
                 connections (to AHN, PHN, arcuate, PAG, brainstem
                 thermoregulatory circuits).
    - right/   Delta mirror of left/, differing only in the right-side
                 reciprocal edges. No functional asymmetry documented.

Notes:
    - Tier 1 hub container. The full leaf lives in left/; right/ is a
      delta.
    - The VMH is marked ★ at the parent tuberal/medial_area/ container:
      it is the secondary content hub of the tuberal division after
      the arcuate (★★). The DMH (★) is the tertiary hub.
    - FOUR TRAPS reproduced above (VMH vs. DMH; VMH vs. AHN; VMH vs.
      PHN; VMH vs. arcuate). All apply to the VMH specifically. Do not
      omit any of them.
    - The VMH ↔ AHN and VMH ↔ PHN complementary pairs (Traps 7a/7b)
      are the thermoregulatory triangle: preoptic (controller) + AHN
      (parasympathetic thermoregulatory) + VMH (thermogenic effector)
      + PHN (sympathetic outflow). The four nuclei together form the
      thermoregulatory system; no single node is "the"
      thermoregulator. The VMH is the thermogenic EFFECTOR; the AHN
      and PHN are the autonomic effectors; the preoptic is the
      controller.
    - The VMH ↔ arcuate feeding complementarity is: arcuate =
      first-order hunger/satiety (NPY/AgRP + POMC/CART); VMH = satiety
      center and meal termination (integrated). The two together
      define the feeding state. The VMH leaf reciprocates the arcuate
      feeding edges.
    - The VMH's four roles are anatomically distributed across
      subdivisions (VMHc = satiety; VMHvl = aggression + sexual
      behavior; VMHdm = defensive + thermogenic). The subdivisions are
      documented WITHIN each hemisphere's leaf, not as child nodes.
      Same convention as habenula's LHb/MHb and PVN's sub-populations.
    - The VMH is NOT the arcuate (first-order vs. integrated satiety);
      NOT the DMH (satiety/aggression/thermoregulation/sexual vs.
      circadian relay); NOT the AHN (thermogenic effector vs.
      parasympathetic thermoregulatory); NOT the PHN (thermogenic
      sympathetic vs. whole-body sympathetic). The four traps make
      these distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, progesterone,
      testosterone), 03_* (HPT, metabolic), 04_* (satiety, leptin,
      ghrelin, CCK), 05_* (serotonin, GABA, PGE2-adjacent), 06_*
      (social, oxytocin), 07_* (fluid, PGE2); memory/stores/
      (short_term, episodic, emotional_valence); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          anterior/medial_area/left|right/anterior_hypothalamic_
          nucleus (VMH thermogenic effector vs. AHN parasympathetic
          thermoregulatory control; TRAP 7a; complementary pair, not
          duplicate).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          posterior/medial_area/left|right/posterior_nucleus (VMH
          thermogenic sympathetic drive vs. PHN whole-body sympathetic
          outflow; TRAP 7b; complementary pair, not duplicate).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          tuberal/medial_area/left|right/arcuate_nucleus (VMH satiety
          center and meal termination vs. arcuate first-order
          hunger/satiety; complementary feeding roles, not duplicate).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus (VMH vs. DMH; TRAP 4; adjacent nuclei, distinct
          functions, do not merge).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          midbrain/tegmentum/periaqueductal_gray (defensive aggression
          motor patterns; PAG is midline-adjacent — verify).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          hindbrain/myelencephalon/medulla_oblongata/
          rostral_ventrolateral_medulla and spinal_cord/gray_matter/
          left|right/lateral_horn (thermogenic sympathetic outflow via
          RVLM → IML → BAT; RVLM is midline-adjacent — verify).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          anterior/medial_area/left|right/preoptic_area
          (thermoregulatory controller; the preoptic is the CONTROLLER,
          the VMH is the EFFECTOR; complementary roles).
        * tuberal/medial_area/left|right/ventromedial_nucleus ↔
          other_preoptic_nuclei/left|right (VMHvl female sexual
          behavior circuit vs. AVPV estrogen-positive-feedback surge
          circuit; distinct reproductive roles).
    - Connects upward to hypothalamus/tuberal/medial_area/.
"""