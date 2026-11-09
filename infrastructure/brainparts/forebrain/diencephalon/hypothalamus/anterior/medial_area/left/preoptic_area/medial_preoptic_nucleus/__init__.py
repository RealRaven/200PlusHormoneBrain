"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.preoptic_area.medial_preoptic_nucleus
Anatomical Role:
    The left medial preoptic nucleus (MPN) is the principal hypothalamic
    nucleus for reproductive behavior, maternal behavior, and GnRH
    regulation. It is a sexually dimorphic structure: its volume,
    neuronal density, and connectivity differ by sex, and it contains
    four interstitial nuclei of the anterior hypothalamus (INAH 1–4)
    that are the sexually dimorphic components proper:
        - inah_1/: interstitial nucleus of the anterior hypothalamus 1.
        - inah_2/: interstitial nucleus of the anterior hypothalamus 2.
        - inah_3/: interstitial nucleus of the anterior hypothalamus 3,
          the human homologue of the rodent sexually dimorphic nucleus
          of the preoptic area (SDN-POA). Larger in males; implicated
          in sexual behavior and (controversially) sexual orientation.
        - inah_4/: interstitial nucleus of the anterior hypothalamus 4;
          often grouped with INAH-3 in human studies.

    The INAH nuclei are documented as child leaves of this file (Tier 2
    organ-flavored shape), not as separate anatomical structures. They
    are components of the MPN in the tree's logic, and their file
    primary role is sexually dimorphic volume and hormonal modulation.

    DISTINCTIONS (critical — reproduced from the parent preoptic_area/
    and restated here because a contributor entering at this leaf must
    see them):
    - DISTINCT FROM PEPTIDERGIC PeN: the periventricular preoptic nucleus
      (periventricular_preoptic_nucleus/, in the lateral area) is a
      separate GnRH-regulatory nucleus. The MPN and PeN interact
      (reciprocal kisspeptin and GnRH-regulatory edges) but are distinct
      nodes. The reciprocal edge is a continuity edge, not a
      duplicate-structure warning.
    - DISTINCT FROM MEDIAN PREOPTIC NUCLEUS: the median_preoptic_nucleus/
      sibling is the median preoptic nucleus of the medial preoptic
      area, involved in GnRH regulation, osmoregulation, and
      cardiovascular control. It is a distinct node. Do not merge.
    - PREOPTIC COLLISION: this node is inside the MEDIAL preoptic area,
      not the lateral preoptic area. It is distinct from
      lateral_area/*/preoptic_area/lateral_preoptic_nucleus/ (the
      VLPO-adjacent sleep nucleus). Do not merge.
    - MnPO DISAMBIGUATION: the "MnPO" acronym refers to
      median_preoptic_nucleus/ (the medial sibling), not to the
      ventrolateral sleep-active population of the LPO. Do not confuse
      the two.

Functional Mode:
    - Maternal behavior: MPN lesions abolish maternal behavior in
      rodents; MPN activation (via estradiol and prolactin signaling)
      promotes pup retrieval, nest building, nursing, and maternal
      aggression. The MPN is the principal hypothalamic node for the
      maternal behavioral circuit.
    - Female sexual behavior: the MPN (via estradiol and progesterone
      signaling) promotes proceptive and receptive behaviors, and gates
      the LH surge in coordination with PeN and the SCN.
    - Male sexual behavior: the MPN (via testosterone and estradiol
      aromatization) promotes mounting, intromission, and ejaculation;
      the MPN is the male sexual behavior hub, projecting to the
      periaqueductal gray and the ventral tegmental area.
    - GnRH regulation: the MPN contributes to GnRH pulsatility and to
      the preovulatory surge via kisspeptin and direct projections to
      GnRH neurons. Its role is permissive/modulatory; the principal
      surge generator is the PeN (lateral area) and the arcuate KNDy
      pulse generator (tuberal area).
    - Parental behavior (both sexes): the MPN is active in paternal
      behavior in biparental species and in alloparental behavior;
      the circuit is not strictly maternal.
    - Thermoregulatory and cardiovascular contribution (minor): the MPN
      shares preoptic thermoregulatory circuitry with the preoptic area
      broadly; document as a supporting role, not an anchor.
    - The nucleus is therefore reproductive-behavior-central (maternal,
      sexual, parental) and GnRH-modulatory; it is not a primary
      thermoregulatory or autonomic nucleus.

Hormonal Modulation:
    - Estradiol: the defining modulator. Aromatized from testosterone in
      males and circulating in females, estradiol activates MPN neurons
      to promote maternal behavior, female sexual behavior, and the
      GnRH surge contribution.
    - Progesterone: in females, progesterone initially facilitates then
      (with progesterone withdrawal) triggers maternal behavior and
      sexual receptivity; the progesterone-estradiol sequence is the
      hormonal basis of the maternal transition.
    - Prolactin: promotes maternal behavior, particularly the onset of
      nursing and the maintenance of maternal responsiveness.
    - Testosterone: in males, aromatized to estradiol in the MPN to
      activate male sexual behavior; testosterone itself also
      contributes.
    - Oxytocin: facilitatory on maternal behavior via MPN projections;
      oxytocin receptor density in the MPN is estrogen-dependent.
    - Kisspeptin: from the PeN and arcuate KNDy populations; modulates
      GnRH-regulatory output.
    - GABA, glutamate: intrinsic modulatory transmitters.
    - Stress hormones (CRH, cortisol): suppress MPN reproductive
      behavior under chronic stress; the classic "stress inhibits
      reproduction" pathway.
    - Direction summary: estradiol ↑ MPN activity (maternal, sexual,
      GnRH surge), progesterone withdrawal ↑ maternal onset, prolactin
      ↑ maternal onset, testosterone (aromatized) ↑ male sexual behavior,
      oxytocin ↑ maternal behavior, CRH/cortisol ↓ MPN reproductive
      behavior. These directions are the actionable content; do not omit
      them.

Memory Interfaces:
    - Reads:
        * short_term: current reproductive-hormonal state (estradiol,
          progesterone, prolactin, testosterone levels) and social
          context buffer. Reproductive behavior depends on both.
        * episodic: past reproductive and maternal events (pregnancy,
          parturition, lactation, mating history), used to set
          behavioral thresholds and prime the circuit.
        * emotional_valence: stress context; chronic stress suppresses
          MPN reproductive behavior via CRH/cortisol.
        * reinforcement_value_based_learning: reproductive and parental
          outcomes feed back into the value of reproductive contexts.
        * temporal_sequence_learning: circadian timing of reproductive
          behavior (mating typically occurs at species-typical times of
          day; coordinated with SCN).
    - Writes:
        * reinforcement_value_based_learning: reproductive outcomes
          (mating success, maternal success) feed back into the value
          learning of reproductive and parental contexts. Document as
          a modulation, not a direct write.
        * Does not write episodic or semantic content directly.
    - The reproductive behavioral state is a *state*, not a memory
      write. Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (reproductive/parental constituent input):
        "Reproductive/parental state — medial preoptic nucleus (left):
         - Reproductive mode: [quiescent / follicular / periovulatory /
           luteal / lactational].
         - Estradiol: [low/moderate/high]. Progesterone:
           [low/moderate/high]. Prolactin: [low/moderate/high].
         - Parental drive: [0-1]. Maternal behavior context:
           [inactive / active].
         - GnRH-modulatory contribution: [normal / suppressed].
         If parental drive is high or maternal behavior context is
         active: bias toward protective, caregiving, and affiliative
         framing; increase tolerance for the demands of vulnerable
         others. If reproductive mode is periovulatory and estradiol is
         high: bias toward reproductive-context framing where relevant,
         and increase salience of social/affiliative cues. Do not treat
         high parental drive or periovulatory state as impairment — they
         are state biases, not degradations of reasoning capacity."
    - AGGREGATION RULE (mandatory for the implementer): this fragment
      is a *constituent input* to the anterior-division reproductive
      fragment, which also aggregates the PeN contribution
      (lateral_area/left/periventricular_preoptic_nucleus/) and the
      median preoptic nucleus contribution
      (median_preoptic_nucleus/). Do not emit this fragment as an
      independent un-aggregated state block — that would double-count
      the reproductive signal. Aggregate at the anterior-division level
      before injection.
    - Guardrail: "do not treat high parental drive or periovulatory
      state as impairment" — consistent with the habenula, orexin/MCH,
      PeN, LPO, AHN, and PVN conventions.

Children (four INAH nuclei — Tier 2 organ-flavored leaves, short):
    - inah_1/   Interstitial nucleus of the anterior hypothalamus 1.
                 Very small; primary role is sexually dimorphic volume
                 and hormonal modulation. Minimal endocrine or memory
                 content.
    - inah_2/   Interstitial nucleus of the anterior hypothalamus 2.
                 Very small; same shape as inah_1/.
    - inah_3/   Interstitial nucleus of the anterior hypothalamus 3,
                 the human homologue of the rodent SDN-POA. Larger in
                 males; implicated in sexual behavior. Tier 2
                 organ-flavored leaf (slightly longer than inah_1/2/4
                 but not full Tier 1).
    - inah_4/   Interstitial nucleus of the anterior hypothalamus 4;
                 often grouped with INAH-3 in human studies. Tier 2
                 organ-flavored leaf.

    These four are components of the MPN, not separate anatomical
    structures. Document them as short Tier 2 leaves with the primary
    role being sexually dimorphic volume and hormonal modulation. Do
    not force the full Tier 1 template onto them.

Reciprocal Connections (enforce in Stage 4 audit):
    - ↔ lateral_area/left/periventricular_preoptic_nucleus (PeN;
      GnRH-regulatory partners; kisspeptin and direct projections;
      continuity edge, not duplicate-structure warning).
    - ↔ lateral_area/left/preoptic_area/lateral_preoptic_nucleus (LPO;
      adjacent preoptic sleep circuitry; reciprocal stress-arousal
      cross-talk; keep distinct).
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area/
      median_preoptic_nucleus (MnPO; adjacent preoptic nodes; distinct
      functions).
    - → midbrain/tegmentum/periaqueductal_gray (maternal/sexual
      behavior motor patterns; PAG is midline-adjacent — verify).
    - → midbrain/tegmentum/ventral_tegmental_area (reproductive
      motivation and reward; VTA is midline-adjacent — verify).
    - ↔ telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/amygdala (reproductive and social context;
      stria terminalis and ventral amygdalofugal pathway).
    - ↔ telencephalon/.../subcortical/extended_amygdala/
      bed_nucleus_of_stria_terminalis (BNST; reproductive and stress
      context integration).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → MPN; circadian timing of reproductive behavior; SCN is
      midline-adjacent — verify).
    - ← hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (PVN CRH; stress suppression of reproductive behavior).
    - ← hypothalamus/tuberal/medial_area/left/arcuate_nucleus (kisspeptin
      KNDy input; GnRH regulation).
    - ← brainstem/.../locus_coeruleus (noradrenergic input; arousal
      context for sexual behavior).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - This is the parent of the four INAH nuclei. The INAH are
      documented as child leaves (Tier 2 organ-flavored) because they
      are components of the MPN, not separate structures in the tree's
      logic. Do not flatten them into siblings of the MPN, and do not
      merge them into the MPN's main file.
    - NO structural-identity trap: MPN is a single nucleus on both
      sides; the INAH are components of it, not a split-structure
      issue. Do not invent a structural-identity warning.
    - Continuity edges (not duplicate-structure warnings) to note:
        * MPN ↔ PeN (GnRH-regulatory partners).
        * MPN ↔ MnPO (adjacent preoptic nodes, distinct functions).
      These are continuity edges because the nodes are genuinely
      distinct; the audit should not flag them as duplicates.
    - The preoptic collision and MnPO disambiguation are reproduced in
      the Anatomical Role section because a contributor entering at the
      leaf must see them. Do not remove.
    - The INAH 1–4 files can be short. Their primary role is sexually
      dimorphic volume; their endocrine and memory content is minimal.
      Do not over-write them.
    - Sex differences: MPN volume, INAH volume, and receptor densities
      are sex-dependent. This is a genuine structural feature of the
      nucleus, not a design choice; document it factually and without
      over-claiming functional consequences.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, progesterone, testosterone,
      kisspeptin, GnRH, prolactin), 05_* (GABA, glutamate), 06_* (social,
      oxytocin), 02_* (HPA, CRH, cortisol); memory/stores/; gateway/.
    - Connects upward to hypothalamus/anterior/medial_area/left/
      preoptic_area/.
"""