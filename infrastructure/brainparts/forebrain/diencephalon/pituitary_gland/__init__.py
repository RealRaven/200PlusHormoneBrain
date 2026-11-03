"""
Package: infrastructure.brainparts.forebrain.diencephalon.pituitary_gland
Anatomical Role:
    The pituitary gland (hypophysis) is a small, pea-sized endocrine
    organ situated in the sella turcica at the base of the skull,
    connected to the hypothalamus by the pituitary stalk
    (infundibulum). It is the endocrine effector arm of the
    hypothalamus: it receives hypothalamic hormones and secretes the
    downstream hormones that control the thyroid, adrenal cortex,
    gonads, growth, lactation, and fluid balance.

    It has THREE anatomically and developmentally distinct subdivisions
    (documented as children, not within this container):

        - adenohypophysis/ (anterior pituitary): GLANDULAR. Derived
          from Rathke's pouch (oral ectoderm). Produces and secretes
          SIX hormones under hypothalamic control via the hypophyseal
          portal system:
            * ACTH (corticotropes; controlled by CRH from PVN).
            * TSH (thyrotropes; controlled by TRH from PVN).
            * GH (somatotropes; controlled by GHRH from arcuate and
              somatostatin from PVN).
            * LH and FSH (gonadotropes; controlled by GnRH from
              preoptic area).
            * Prolactin (lactotropes; inhibited by dopamine from
              arcuate TIDA).
          The adenohypophysis is the "master gland" in the classic
          sense: it is the source of the tropic hormones that control
          the peripheral endocrine glands.

        - neurohypophysis/ (posterior pituitary): NEURAL. Derived from
          the diencephalon (neural ectoderm); an extension of the
          hypothalamus. Stores and releases TWO hormones produced by
          hypothalamic magnocellular neurons (SON, PVN):
            * Oxytocin.
            * Vasopressin (ADH).
          The neurohypophysis does NOT synthesize these hormones; it
          stores them in axon terminals and releases them into the
          systemic circulation. It is a neurohemal organ, not a
          glandular one.

        - pars_intermedia/: RUDIMENTARY IN HUMANS. Between the
          adenohypophysis and the neurohypophysis. Produces
          melanocyte-stimulating hormone (MSH) and endorphins in
          non-human species; in humans, it is vestigial and its
          functional contribution is minimal. Documented for
          anatomical completeness; not a functional hub.

    The pituitary gland is therefore the "master gland" in the classic
    endocrine sense (it controls the peripheral endocrine glands), but
    it is itself controlled by the hypothalamus (which is why the
    hypothalamus, not the pituitary, is the true master of the
    endocrine system). The pituitary is the EFFECTOR; the hypothalamus
    is the CONTROLLER.

    NAMING TRAPS (critical — three sub-divisions could be confused):

    - TRAP A: ADENOHYPOPHYSIS vs. NEUROHYPOPHYSIS (the classic trap).
      The anterior pituitary is GLANDULAR (synthesizes its own
      hormones; controlled by hypothalamic releasing/inhibiting
      hormones via the portal system); the posterior pituitary is
      NEURAL (stores and releases hypothalamic hormones; controlled by
      magnocellular axon terminals from SON/PVN). Two different organs
      with different embryonic origins, different control mechanisms,
      and different hormones. Do not merge; do not treat them as one
      structure.

    - TRAP B: PARS INTERMEDIA vs. ADENOHYPOPHYSIS and NEUROHYPOPHYSIS.
      The pars intermedia is a THIRD subdivision between the two,
      rudimentary in humans. It produces MSH and endorphins in some
      species but has minimal function in humans. Do not merge it with
      either the adenohypophysis or the neurohypophysis.

    - TRAP C: PITUITARY GLAND vs. PITUITARY STALK. The pituitary
      gland is the endocrine organ; the pituitary stalk
      (hypothalamus/pituitary_stalk/) is the conduit connecting it to
      the hypothalamus. Two distinct structures; the stalk is a Tier 3
      conduit, the gland is a Tier 2 organ. Do not merge.

Functional Mode:
    - Anterior pituitary endocrine output (adenohypophysis): six
      tropic/effector hormones under hypothalamic control:
        * ACTH → adrenal cortex → cortisol (HPA axis).
        * TSH → thyroid → T3/T4 (HPT axis).
        * GH → liver/IGF-1 and peripheral tissues (growth axis).
        * LH, FSH → gonads → sex steroids and gametogenesis (HPG
          axis).
        * Prolactin → mammary glands (lactation); inhibited by
          arcuate TIDA dopamine.
    - Posterior pituitary neurosecretory output (neurohypophysis): two
      hormones stored/released from hypothalamic magnocellular axons:
        * Oxytocin → uterus (parturition), mammary glands (milk
          ejection); central neuromodulator roles.
        * Vasopressin (ADH) → kidney (water reabsorption),
          vasculature (vasoconstriction); central neuromodulator roles.
    - Pars intermedia output (pars_intermedia; rudimentary in humans):
      MSH, endorphins; minimal functional significance in humans.
    - Feedback control: the pituitary is under negative-feedback
      control from its peripheral targets (cortisol ↓ CRH/ACTH;
      thyroid hormones ↓ TRH/TSH; IGF-1 ↓ GHRH/GH; sex steroids ↓
      GnRH/LH/FSH). Documented in the child leaves.
    - The pituitary is therefore the endocrine EFFECTOR arm of the
      hypothalamus: it receives hypothalamic commands and translates
      them into circulating hormones that control the peripheral
      endocrine glands and the whole-body endocrine state.

Hormonal Modulation (container-level summary; per-child wiring in the
three child leaves):
    - Adenohypophysis: ACTH, TSH, GH, LH, FSH, prolactin (all OUTPUTS).
      Modulated by hypothalamic releasing/inhibiting hormones (CRH,
      TRH, GHRH, somatostatin, GnRH, dopamine) and by peripheral
      feedback (cortisol, thyroid hormones, IGF-1, sex steroids,
      prolactin).
    - Neurohypophysis: oxytocin, vasopressin (STORED and RELEASED, not
      synthesized). Modulated by SON/PVN magnocellular activity
      (osmolarity, parturition cues, suckling cues).
    - Pars intermedia: MSH, endorphins (rudimentary in humans).
    - The container does not re-list the per-hormone detail; the three
      child leaves carry it.

Memory Interfaces (container-level summary):
    - The pituitary gland has minimal memory interfaces: it is a
      hormone source, not a memory structure. Its "memory" is the
      feedback set-point maintained by hypothalamic and peripheral
      signals.
    - Reads (for the pituitary's own feedback regulation): short_term
      (current peripheral hormone levels — cortisol, thyroid, IGF-1,
      sex steroids, prolactin), episodic (past endocrine events —
      puberty, pregnancy, lactation, stress history).
    - Writes: none directly. The pituitary does not write episodic,
      semantic, or procedural memory. It modulates the endocrine state
      under which other regions operate.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No container-level fragment. Each of the three child leaves emits
      its own fragment (or contributes to an aggregate emitted
      elsewhere).
    - Anterior pituitary (adenohypophysis): contributes the OUTPUT
      state to the HPA, HPT, HPG, growth, and prolactin fragments.
      The AGGREGATION RULES established in the hypothalamic nuclei
      apply: the pituitary's output is the READOUT of the
      hypothalamic state, not an independent signal.
    - Posterior pituitary (neurohypophysis): contributes the OUTPUT
      state to the fluid fragment (vasopressin) and the social/
      parturition/lactation fragment (oxytocin). The AGGREGATION RULES
      established in SON/PVN apply.
    - Pars intermedia: no fragment (rudimentary in humans).
    - Guardrails: the pituitary outputs feed the hypothalamic
      aggregates that already carry their "bias not impairment"
      clauses; the pituitary does not add new guardrails.

Children (three children — one full leaf per child, no left/right
split because the pituitary is midline/unpaired):
    - adenohypophysis/    ★★ TIER 2 ORGAN with SIX hormones. The
                             anterior pituitary. Glandular;
                             synthesizes ACTH, TSH, GH, LH, FSH,
                             prolactin. Controlled by hypothalamic
                             releasing/inhibiting hormones via the
                             portal system. THE CLOSURE TARGET for
                             EIGHT hypothalamic edges (see Notes).
    - neurohypophysis/    ★★ TIER 2 ORGAN with TWO hormones. The
                             posterior pituitary. Neural; stores and
                             releases oxytocin and vasopressin
                             produced by SON/PVN magnocellular
                             neurons. THE CLOSURE TARGET for FOUR
                             hypothalamic edges (see Notes).
    - pars_intermedia/    Tier 2 organ (rudimentary in humans). MSH,
                             endorphins. Minimal functional
                             significance. Documented for completeness;
                             short leaf.

    Each child is a SINGLE FILE (no left/ or right/ children) because
    the pituitary is midline/unpaired. Do not create left/ or right/
    under any of the three children.

Notes:
    - Container file: do not duplicate child hormone wiring. Each
      child owns its own specification.
    - THREE NAMING TRAPS reproduced in full above (adenohypophysis vs.
      neurohypophysis; pars intermedia vs. both; pituitary gland vs.
      pituitary stalk). Apply at every level where the pituitary is
      referenced.
    - THE PITUITARY IS A TIER 2 ORGAN, NOT A TIER 1 HUB. It is a
      hormone SOURCE (adenohypophysis, pars intermedia) and a hormone
      RELEASE SITE (neurohypophysis), not a processing region. Its
      children are Tier 2 organ leaves, not Tier 1 hub leaves.
      Compare with pineal_gland/ (the Tier 2 secerning organ exemplar)
      and median_eminence/ (the Tier 2 release-surface exemplar).
    - EIGHT DEFERRED EDGE CLOSURES: this container closes the pituitary
      ends of EIGHT edges declared from the hypothalamic nuclei
      earlier:
        (1) PVN → adenohypophysis (CRH via hypophyseal portal →
            ACTH).
        (2) PVN → adenohypophysis (TRH via hypophyseal portal → TSH).
        (3) PVN → adenohypophysis (somatostatin via hypophyseal
            portal → ↓ GH).
        (4) Arcuate GHRH → adenohypophysis (via hypophyseal portal →
            GH).
        (5) Arcuate TIDA → adenohypophysis (dopamine via hypophyseal
            portal → ↓ prolactin).
        (6) PeN/MPN/MnPO → adenohypophysis (GnRH via hypophyseal
            portal → LH/FSH).
        (7) PVN → neurohypophysis (oxytocin/vasopressin magnocellular
            axon terminals → systemic circulation).
        (8) SON → neurohypophysis (vasopressin/oxytocin magnocellular
            axon terminals → systemic circulation).
      Each of these was declared from the hypothalamic side; the
      pituitary side closes them.
    - The median eminence → adenohypophysis edge (portal pathway) and
      the pituitary stalk → both edges (conduit) are also part of the
      closure, bringing the total to ~10 edges that resolve when the
      adenohypophysis and neurohypophysis leaves are drafted.
    - The pituitary is UNPAIRED/midline; do not create left/ or right/
      under any child.
    - The pituitary gland is DISTINCT from the pituitary stalk
      (hypothalamus/pituitary_stalk/; Tier 3 conduit). The stalk is the
      conduit; the gland is the endocrine organ. Do not merge.
    - The pituitary gland is DISTINCT from the median eminence
      (hypothalamus/median_eminence/; Tier 2 release surface). The
      median eminence releases hypothalamic hormones into portal
      blood; the adenohypophysis receives them and secretes its own
      hormones. Two different release sites; two different
      directions of hormonal flow.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, LH, FSH, GnRH), 02_* (HPA, ACTH,
      CRH, cortisol), 03_* (HPT, TSH, TRH, GH, GHRH, somatostatin,
      IGF-1, thyroid hormones), 04_* (satiety, prolactin-adjacent),
      06_* (social, oxytocin, vasopressin central), 07_* (fluid,
      vasopressin peripheral); memory/stores/ (short_term, episodic);
      gateway/.
    - Reciprocal connections to enforce in Stage 4 (container-level
      summary; full list in the child leaves):
        * adenohypophysis ↔ anterior/medial_area/left|right/
          paraventricular_nucleus (CRH, TRH, somatostatin; PVN → anterior
          pituitary via portal).
        * adenohypophysis ↔ tuberal/medial_area/left|right/
          arcuate_nucleus (GHRH, TIDA dopamine; arcuate → anterior
          pituitary via portal).
        * adenohypophysis ↔ anterior/medial_area/left|right/
          preoptic_area and other_preoptic_nuclei/left|right (GnRH;
          preoptic + AVPV → anterior pituitary via portal).
        * adenohypophysis ↔ hypothalamus/median_eminence (the portal
          release site upstream of the anterior pituitary).
        * adenohypophysis ↔ hypothalamus/pituitary_stalk (the conduit
          upstream of both pituitary subdivisions).
        * neurohypophysis ↔ anterior/medial_area/left|right/
          supraoptic_nucleus and paraventricular_nucleus (vasopressin,
          oxytocin; magnocellular axon terminals).
        * neurohypophysis ↔ hypothalamus/pituitary_stalk (the conduit
          upstream of both pituitary subdivisions).
    - Connects upward to diencephalon/.
"""