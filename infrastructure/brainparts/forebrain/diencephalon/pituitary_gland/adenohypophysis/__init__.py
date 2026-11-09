"""
Package: infrastructure.brainparts.forebrain.diencephalon.pituitary_gland.adenohypophysis
Anatomical Role:
    The adenohypophysis (anterior pituitary) is the GLANDULAR subdivision
    of the pituitary, derived embryologically from Rathke's pouch (oral
    ectoderm). It is the most hormonally dense single organ in the tree:
    it contains SIX hormone-producing cell types, each under distinct
    hypothalamic control via the hypophyseal portal system:

        - Corticotropes → ACTH (adrenocorticotropic hormone).
        - Thyrotropes → TSH (thyroid-stimulating hormone).
        - Somatotropes → GH (growth hormone).
        - Gonadotropes → LH (luteinizing hormone) and FSH
          (follicle-stimulating hormone).
        - Lactotropes → Prolactin.

    Five cell types, six hormones (gonadotropes make two). The
    adenohypophysis is the "master gland" in the classic endocrine
    sense: its tropic hormones control the adrenal cortex, thyroid,
    gonads, growth, and lactation.

    The adenohypophysis is CONTROLLED by the hypothalamus via the
    hypophyseal portal system (see the median eminence and pituitary
    stalk), and by peripheral hormones via negative feedback. It is the
    EFFECTOR; the hypothalamus is the CONTROLLER.

    DISTINCTIONS (reproduced from the parent pituitary_gland/
    container; critical — apply at every level):

    - ADENOHYPOPHYSIS vs. NEUROHYPOPHYSIS: GLANDULAR (synthesizes its
      own hormones) vs. NEURAL (stores and releases hypothalamic
      hormones). Different embryonic origins (oral ectoderm vs. neural
      ectoderm), different control mechanisms (portal vs. axon
      terminals), different hormones. Do not merge.

    - ADENOHYPOPHYSIS vs. PARS INTERMEDIA: distinct subdivisions; the
      pars intermedia is rudimentary in humans and produces MSH/
      endorphins. Do not merge.

    - ADENOHYPOPHYSIS vs. MEDIAN EMINENCE: the median eminence
      RELEASES hypothalamic hormones into portal blood; the
      adenohypophysis RECEIVES them and secretes its own hormones. Two
      different release sites; two different directions of flow.

    - ADENOHYPOPHYSIS vs. PITUITARY STALK: the stalk is the conduit;
      the adenohypophysis is the endocrine organ. Distinct tree nodes;
      distinct tiers (Tier 3 vs. Tier 2).

Functional Mode:
    The adenohypophysis secretes six hormones, each under its own
    hypothalamic control and with its own peripheral target and
    feedback:

    - ACTH (corticotropes; HPA axis):
        * Hypothalamic control: CRH from the paraventricular nucleus
          (PVN) → portal blood → corticotropes → ACTH.
        * Target: adrenal cortex → cortisol.
        * Feedback: cortisol ↓ CRH (PVN) and ↓ ACTH (corticotropes).
        * Circadian: ACTH and cortisol have a circadian rhythm (morning
          peak) driven by SCN → PVN → CRH → ACTH → cortisol.
    - TSH (thyrotropes; HPT axis):
        * Hypothalamic control: TRH from the PVN → portal blood →
          thyrotropes → TSH.
        * Target: thyroid gland → T3/T4.
        * Feedback: thyroid hormones ↓ TRH (PVN) and ↓ TSH
          (thyrotropes).
    - GH (somatotropes; growth axis):
        * Hypothalamic control: GHRH from the arcuate (stimulatory) and
          somatostatin from the PVN (inhibitory) → portal blood →
          somatotropes → GH. The GHRH-somatostatin balance sets the
          pulsatile GH rhythm.
        * Target: liver → IGF-1; peripheral tissues → growth and
          metabolism.
        * Feedback: IGF-1 ↓ GHRH (arcuate) and ↑ somatostatin (PVN);
          GH itself ↓ GHRH.
    - LH and FSH (gonadotropes; HPG axis):
        * Hypothalamic control: GnRH from the preoptic area (PeN/MPN/
          MnPO/AVPV) → portal blood → gonadotropes → LH/FSH. Pulsatile
          GnRH drives pulsatile LH; the preovulatory surge drives the
          LH surge.
        * Target: gonads → sex steroids (estradiol, testosterone,
          progesterone) and gametogenesis.
        * Feedback: sex steroids ↓ GnRH (arcuate KNDy for negative
          feedback; AVPV for positive feedback) and ↓ LH/FSH
          (gonadotropes, except the preovulatory surge).
    - Prolactin (lactotropes; lactation and beyond):
        * Hypothalamic control: DOPAMINE from arcuate TIDA neurons is
          the dominant INHIBITORY control (tonic inhibition). The
          portal system delivers dopamine to lactotropes; ↓ dopamine
          → ↑ prolactin. (Contrast with CRH/TRH/GHRH/GnRH, which are
          stimulatory; dopamine is the exception.)
        * Target: mammary glands → lactation; also reproductive and
          behavioral functions.
        * Feedback: prolactin ↑ TIDA dopamine (short-loop feedback)
          → ↓ prolactin. Suckling ↓ TIDA dopamine → ↑ prolactin.

Hormonal Modulation (outputs first, then hypothalamic inputs, then
peripheral feedback — this is a Tier 2 organ convention):

    - SIX OUTPUTS (the adenohypophysis's own secretions):
        * ACTH (corticotropes).
        * TSH (thyrotropes).
        * GH (somatotropes).
        * LH, FSH (gonadotropes).
        * Prolactin (lactotropes).

    - SIX HYPOTHALAMIC INPUTS (the releasing/inhibiting hormones,
      via portal blood):
        * CRH (PVN; stimulatory → ACTH).
        * TRH (PVN; stimulatory → TSH).
        * GHRH (arcuate; stimulatory → GH).
        * Somatostatin (PVN; inhibitory → ↓ GH).
        * GnRH (preoptic area; stimulatory → LH/FSH).
        * Dopamine (arcuate TIDA; INHIBITORY → ↓ prolactin).

    - PERIPHERAL FEEDBACK (from the adenohypophysis's targets):
        * Cortisol ↓ CRH and ACTH.
        * Thyroid hormones ↓ TRH and TSH.
        * IGF-1 ↓ GHRH and ↑ somatostatin; GH ↓ GHRH.
        * Sex steroids ↓ GnRH and LH/FSH (except the preovulatory
          surge).
        * Prolactin ↑ TIDA dopamine (short-loop).

    - Direction summary: CRH ↑ ACTH; TRH ↑ TSH; GHRH ↑ GH; somatostatin
      ↓ GH; GnRH ↑ LH/FSH; dopamine ↓ prolactin; cortisol ↓ ACTH;
      thyroid hormones ↓ TSH; IGF-1 ↓ GH; sex steroids ↓ LH/FSH;
      prolactin ↑ TIDA dopamine. These are the actionable directions;
      do not omit them.

    - Clinical facts (the file's defining clinical content):
        * HYPERPITUITARISM (pituitary adenoma): the most common
          pituitary tumor; usually a prolactinoma (lactotroph adenoma
          → hyperprolactinemia → amenorrhea + galactorrhea); also GH
          adenoma (acromegaly), ACTH adenoma (Cushing disease). The
          pituitary adenoma can also compress the optic chiasm →
          bitemporal hemianopsia (the classic visual field deficit).
        * HYPOPITUITARISM (pituitary insufficiency): global or
          selective deficiency of anterior pituitary hormones;
          causes include pituitary adenoma compression, Sheehan
          syndrome (postpartum pituitary necrosis from hemorrhage),
          radiation, surgery, and infiltrative disease.
        * STALK EFFECT (hyperprolactinemia from stalk compression):
          a pituitary adenoma compressing the stalk blocks descending
          dopaminergic inhibition → prolactin rises; the other axes
          fall because portal releasing hormones also cannot reach
          the anterior pituitary. (See hypothalamus/pituitary_stalk/
          for the stalk-effect description.)
        * PROLACTINOMA: the most common functioning pituitary adenoma;
          hyperprolactinemia → amenorrhea, galactorrhea, infertility,
          reduced libido.
        * ACROMEGALY / GIGANTISM: GH adenoma → excess GH → acromegaly
          in adults, gigantism in children.
        * CUSHING DISEASE: ACTH adenoma → excess ACTH → excess
          cortisol.

Memory Interfaces (minimal — Tier 2 organ convention):
    - Reads:
        * short_term: current peripheral hormone levels (cortisol,
          thyroid hormones, IGF-1, sex steroids, prolactin). The
          feedback set-points that regulate the adenohypophysis's
          output depend on these.
        * episodic: past endocrine events (puberty, pregnancy,
          lactation, stress history, pituitary pathology history).
    - Writes: none directly. The adenohypophysis is a hormone source,
      not a memory structure. Its "memory" is the feedback set-point
      maintained by hypothalamic and peripheral signals.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent adenohypophysis fragment. The adenohypophysis's
      output is the READOUT of the hypothalamic state, not an
      independent signal. It contributes to FIVE hypothalamic
      aggregates:
        (1) HPA aggregate (ACTH): feeds the cortisol state.
        (2) HPT aggregate (TSH): feeds the thyroid state.
        (3) Growth aggregate (GH): feeds the growth-axis state.
        (4) HPG aggregate (LH, FSH): feeds the reproductive state.
        (5) Prolactin-adjacent aggregate (prolactin): feeds the
            lactational state.
    - The AGGREGATION RULES from the hypothalamic nuclei (PVN, arcuate,
      preoptic area) apply: the adenohypophysis's output feeds the
      aggregates they emit. Do not emit a separate adenohypophysis
      fragment; the aggregates already carry the hormonal state.
    - Guardrails: the five aggregates carry their "bias not impairment"
      clauses (HPA: stressed; HPT: hypothyroid; growth: catabolic;
      HPG: periovulatory; prolactin: elevated). The adenohypophysis
      does not add new guardrails.
    - No multimodal input is consumed here; the contributions are
      text-only through the downstream aggregates.

Reciprocal Connections (organized by hypothalamic input and peripheral
output):

    Hypothalamic control (INPUT — the six deferred edges this file
    closes):
    - ← anterior/medial_area/left|right/paraventricular_nucleus (CRH
      via hypophyseal portal → ACTH; PVN → anterior pituitary; THE
      DEFERRED CLOSURE for CRH).
    - ← anterior/medial_area/left|right/paraventricular_nucleus (TRH
      via hypophyseal portal → TSH; THE DEFERRED CLOSURE for TRH).
    - ← anterior/medial_area/left|right/paraventricular_nucleus
      (somatostatin via hypophyseal portal → ↓ GH; THE DEFERRED
      CLOSURE for somatostatin).
    - ← tuberal/medial_area/left|right/arcuate_nucleus (GHRH via
      hypophyseal portal → GH; THE DEFERRED CLOSURE for GHRH).
    - ← tuberal/medial_area/left|right/arcuate_nucleus (dopamine via
      hypophyseal portal → ↓ prolactin; THE DEFERRED CLOSURE for
      TIDA dopamine).
    - ← anterior/medial_area/left|right/preoptic_area and
      other_preoptic_nuclei/left|right (GnRH via hypophyseal portal →
      LH/FSH; THE DEFERRED CLOSURE for GnRH).
    - ← hypothalamus/median_eminence (the portal release site; the
      conduit through which the six hypothalamic hormones reach the
      adenohypophysis).
    - ← hypothalamus/pituitary_stalk (the conduit; the portal vessels
      travel through the stalk).

    Peripheral targets (OUTPUT — the six tropic/effector actions):
    - → adrenal cortex → cortisol (via ACTH; peripheral endocrine
      target).
    - → thyroid gland → T3/T4 (via TSH; peripheral endocrine target).
    - → liver → IGF-1; peripheral tissues → growth and metabolism (via
      GH; peripheral endocrine target).
    - → gonads → sex steroids and gametogenesis (via LH/FSH; peripheral
      endocrine target).
    - → mammary glands → lactation (via prolactin; peripheral effector
      target).

    Adjacency (not signaling):
    - ↔ neurohypophysis/ (anatomically adjacent within the pituitary
      gland; the adenohypophysis is glandular, the neurohypophysis is
      neural; do not merge; no signaling edge between them — their
      control and outputs are distinct).
    - ↔ pars_intermedia/ (anatomically adjacent; the pars intermedia
      is rudimentary in humans; do not merge).

Notes:
    - Tier 2 organ leaf (SEVEN-HORMONE subvariant — actually
      six-hormone-secreting cell types, five cell lineages because
      gonadotropes make two). The most hormonally dense single organ
      in the tree.
    - SINGLE FILE. The adenohypophysis is midline/unpaired; no left/
      or right/ children.
    - SIX DEFERRED EDGE CLOSURES: this file closes the adenohypophysis
      ends of the six edges declared from the hypothalamic nuclei
      earlier:
        (1) PVN → adenohypophysis (CRH).
        (2) PVN → adenohypophysis (TRH).
        (3) PVN → adenohypophysis (somatostatin).
        (4) Arcuate GHRH → adenohypophysis.
        (5) Arcuate TIDA → adenohypophysis (dopamine → ↓ prolactin).
        (6) Preoptic GnRH → adenohypophysis.
      Each was declared from the hypothalamic side; this file closes
      the pituitary side.
    - THE FIVE DEFINING CLINICAL FACTS: hyperpituitarism (pituitary
      adenoma, most commonly prolactinoma); hypopituitarism (Sheehan
      syndrome, compressive, infiltrative); stalk effect
      (hyperprolactinemia from stalk compression); acromegaly/
      gigantism (GH adenoma); Cushing disease (ACTH adenoma). These
      are what make the adenohypophysis clinically important beyond
      being "the six-hormone gland." Documented in Functional Mode;
      do not omit.
    - THE DOPAMINE EXCEPTION: five of the six hypothalamic inputs are
      stimulatory (CRH, TRH, GHRH, GnRH) or their counterpart
      (somatostatin inhibitory); dopamine is the ONE inhibitory
      hypothalamic input with a major tonic role (prolactin
      inhibition). This exception is the anatomical basis of the
      stalk-effect phenomenon and prolactinoma pathophysiology. Do
      not treat dopamine as just "another hypothalamic hormone."
    - The adenohypophysis is NOT a Tier 1 hub: it is a Tier 2 organ
      (hormone source). Do not draft it as a processing region. Same
      discipline as pineal_gland/.
    - The adenohypophysis is DISTINCT from the neurohypophysis (six
      glandular hormones vs. two stored hormones), the pars intermedia
      (rudimentary), the median eminence (release surface), and the
      pituitary stalk (conduit). Four distinct nodes; do not merge.
    - The adenohypophysis's outputs are READOUTS of the hypothalamic
      state, not independent signals. The five aggregates (HPA, HPT,
      growth, HPG, prolactin) carry the hormonal state; the
      adenohypophysis feeds them.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, LH, FSH, GnRH), 02_* (HPA, ACTH,
      CRH, cortisol), 03_* (HPT, TSH, TRH, GH, GHRH, somatostatin,
      IGF-1, thyroid hormones), 04_* (satiety, prolactin-adjacent,
      dopamine), 05_* (dopamine), 10_* (circadian, SCN); memory/
      stores/ (short_term, episodic); gateway/.
    - Connects upward to diencephalon/pituitary_gland/.
"""