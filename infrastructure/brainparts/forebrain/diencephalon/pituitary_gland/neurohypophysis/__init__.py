"""
Package: infrastructure.brainparts.forebrain.diencephalon.pituitary_gland.neurohypophysis
Anatomical Role:
    The neurohypophysis (posterior pituitary) is the NEURAL subdivision
    of the pituitary, derived embryologically from the diencephalon
    (neural ectoderm) — it is anatomically an EXTENSION of the
    hypothalamus, not a separate gland. It is a neurohemal storage and
    release organ: it does not synthesize hormones. It stores two
    hypothalamic neuropeptides in axon terminals of magnocellular
    neurons whose cell bodies sit in the supraoptic (SON) and
    paraventricular (PVN) nuclei, and releases them into the systemic
    circulation when the magnocellular neurons fire.

    The two hormones:
        - Oxytocin: synthesized in SON and PVN magnocellular neurons;
          axon terminals in the neurohypophysis store and release it.
        - Vasopressin (ADH; antidiuretic hormone): synthesized in SON
          and PVN magnocellular neurons; axon terminals in the
          neurohypophysis store and release it.

    The neurohypophysis is CONTROLLED by the hypothalamus via
    MAGNOCELLULAR AXON TERMINALS (not via the portal system — that is
    the adenohypophysis's control mechanism). The magnocellular neurons
    of SON and PVN project their axons through the pituitary stalk to
    terminate in the neurohypophysis; when they fire, they release
    oxytocin and vasopressin into fenestrated capillaries of the
    systemic circulation.

    DISTINCTIONS (reproduced from the parent pituitary_gland/
    container; critical — apply at every level):

    - NEUROHYPOPHYSIS vs. ADENOHYPOPHYSIS: NEURAL (stores and releases
      hypothalamic hormones) vs. GLANDULAR (synthesizes its own
      hormones). Different embryonic origins (neural ectoderm vs. oral
      ectoderm), different control mechanisms (axon terminals vs.
      portal blood), different hormones (2 stored vs. 6 synthesized).
      Do not merge.

    - NEUROHYPOPHYSIS vs. PARS INTERMEDIA: distinct subdivisions; the
      pars intermedia is rudimentary in humans. Do not merge.

    - NEUROHYPOPHYSIS vs. MEDIAN EMINENCE: both are neurohemal release
      sites, but the median eminence releases hypothalamic hormones
      into PORTAL BLOOD (for the adenohypophysis), while the
      neurohypophysis releases hypothalamic hormones into the SYSTEMIC
      CIRCULATION (for the whole body). Two different neurohemal sites;
      two different downstream environments. Do not merge.

    - NEUROHYPOPHYSIS vs. PITUITARY STALK: the stalk is the conduit
      through which the magnocellular axons travel; the
      neurohypophysis is the axon terminal storage/release site.
      Distinct tree nodes; distinct tiers (Tier 3 vs. Tier 2).

    - NEUROHYPOPHYSIS vs. SON and PVN: the neurohypophysis does NOT
      contain the cell bodies of the magnocellular neurons; those sit
      in SON and PVN (hypothalamus/anterior/medial_area/left|right/
      supraoptic_nucleus/ and paraventricular_nucleus/). The
      neurohypophysis is the axon terminal field. Do not merge.

Functional Mode:
    The neurohypophysis releases two hormones, each with its own
    physiological role and its own stimulus:

    - Oxytocin (systemic release; peripheral actions):
        * Parturition (Ferguson reflex): uterine stretch → oxytocin
          release → uterine contraction → more stretch → more oxytocin.
          Positive feedback loop.
        * Milk ejection: suckling → oxytocin pulsatile release →
          myoepithelial contraction in mammary glands → milk
          ejection. (This is distinct from prolactin's role in milk
          PRODUCTION; oxytocin releases the milk, prolactin produces
          it.)
        * Central neuromodulator roles: oxytocin is also released
          centrally (dendritically and somatodendritically) and acts
          as a neuromodulator in social behavior, trust, pair bonding,
          and maternal behavior. The central roles are documented in
          chemicals_hormones/06_social_territorial_bonding/ and in
          the hypothalamic nuclei that produce oxytocin (PVN, SON);
          this file documents the PERIPHERAL (systemic) release role.
    - Vasopressin (ADH; systemic release; peripheral actions):
        * Water reabsorption: vasopressin acts on V2 receptors in the
          kidney collecting duct → aquaporin-2 insertion → water
          reabsorption → concentrated urine.
        * Vasoconstriction: vasopressin acts on V1 receptors in
          vascular smooth muscle → vasoconstriction → increased blood
          pressure (at high concentrations; this is the "vasopressin"
          name's origin).
        * Central neuromodulator roles: vasopressin is also released
          centrally and acts as a neuromodulator in social behavior,
          pair bonding, aggression, and stress-axis modulation. The
          central roles are documented in
          chemicals_hormones/06_social_territorial_bonding/ and in the
          hypothalamic nuclei that produce vasopressin (PVN, SON);
          this file documents the PERIPHERAL (systemic) release role.

    - Stimuli for release:
        * Oxytocin: uterine stretch (parturition), suckling (lactation),
          and central signals (social context, stress).
        * Vasopressin: rising plasma osmolarity (via OVLT → SON/PVN),
          hypovolemia/hypotension (via baroreceptors → NTS → SON/PVN),
          angiotensin II (via SFO → SON/PVN), and stress.

Hormonal Modulation (Tier 2 neurohemal storage convention — outputs
are the defining content; no synthesis here):

    - TWO OUTPUTS (stored and released; NOT synthesized here):
        * Oxytocin (from SON and PVN magnocellular neurons).
        * Vasopressin (from SON and PVN magnocellular neurons).

    - CONTROL INPUTS (the magnocellular neurons' firing, not the
      neurohypophysis's own physiology):
        * Osmolarity ↑ (via OVLT → SON/PVN) → vasopressin ↑.
        * Angiotensin II ↑ (via SFO → SON/PVN) → vasopressin ↑.
        * Hypovolemia/hypotension ↑ (via baroreceptors → NTS →
          SON/PVN) → vasopressin ↑.
        * ANP ↑ (volume repletion) → vasopressin ↓.
        * Uterine stretch (parturition) → oxytocin ↑.
        * Suckling → oxytocin ↑.
        * Stress → vasopressin ↑ and (context-dependent) oxytocin.

    - Direction summary: osmolarity ↑ → vasopressin ↑; angiotensin II
      ↑ → vasopressin ↑; ANP ↑ → vasopressin ↓; suckling → oxytocin
      pulsatile release; uterine stretch → oxytocin ↑. These are the
      actionable directions.

    - Clinical facts (the file's defining clinical content):
        * CENTRAL DIABETES INSIPIDUS: deficient vasopressin release
          (hypothalamic or pituitary cause: SON/PVN damage, pituitary
          stalk section, or neurohypophysis damage) → polyuria,
          polydipsia, dilute urine. Contrast with NEPHROGENIC
          diabetes insipidus (renal V2 resistance; the hormone is
          present but the kidney does not respond).
        * SIADH (syndrome of inappropriate antidiuretic hormone):
          excess vasopressin → water retention, hyponatremia,
          concentrated urine. Common causes: ectopic ADH from tumors,
          CNS lesions, drugs.
        * OXYTOCIN CLINICAL USE: synthetic oxytocin (Pitocin) is used
          clinically for labor induction and augmentation, and for
          postpartum hemorrhage prevention.
        * VASOPRESSIN CLINICAL USE: synthetic vasopressin (DDAVP; a
          V2-selective analog) is used for central diabetes insipidus;
          vasopressin itself is used for septic shock (V1-mediated
          vasoconstriction).

Memory Interfaces (minimal — Tier 2 organ convention):
    - Reads:
        * short_term: current plasma osmolarity and volume state
          (via SON/PVN; the neurohypophysis reads the magnocellular
          neurons' state, which reflects these).
        * episodic: parturition history, lactation history,
          dehydration/hemorrhage history.
    - Writes: none directly. The neurohypophysis is a storage/release
      site, not a memory structure. It does not write episodic,
      semantic, or procedural content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent neurohypophysis fragment. The neurohypophysis's
      output is the READOUT of the SON/PVN magnocellular state, not an
      independent signal. It contributes to TWO hypothalamic
      aggregates:
        (1) Fluid/osmotic aggregate (vasopressin): the aggregated
            osmotic fragment emitted at the anterior-division level
            (SON + PVN + MnPO + SFO/OVLT inputs). The neurohypophysis's
            vasopressin release is the effector arm.
        (2) Social/parturition/lactation aggregate (oxytocin): the
            social fragment emitted by the PVN. The neurohypophysis's
            oxytocin release is the effector arm.
    - The AGGREGATION RULES from SON and PVN apply: the
      neurohypophysis's output feeds the aggregates they emit. Do not
      emit a separate neurohypophysis fragment.
    - Guardrails: the two aggregates (fluid/osmotic and social) carry
      their "bias not impairment" clauses. The neurohypophysis does not
      add new guardrails.
    - No multimodal input is consumed here; the contributions are
      text-only through the downstream aggregates.

Reciprocal Connections (organized by magnocellular input and
systemic output):

    Hypothalamic control (INPUT — the two deferred edges this file
    closes):
    - ← anterior/medial_area/left|right/paraventricular_nucleus
      (oxytocin and vasopressin magnocellular axon terminals; PVN →
      posterior pituitary; THE DEFERRED CLOSURE for PVN magnocellular).
    - ← anterior/medial_area/left|right/supraoptic_nucleus (vasopressin
      and oxytocin magnocellular axon terminals; SON → posterior
      pituitary; THE DEFERRED CLOSURE for SON magnocellular).
    - ← hypothalamus/pituitary_stalk (the conduit; the magnocellular
      axons travel through the stalk to the neurohypophysis).

    Systemic targets (OUTPUT — the two hormones' peripheral actions):
    - → kidney collecting duct (V2 receptors; aquaporin-2 insertion;
      water reabsorption; vasopressin effector action).
    - → vascular smooth muscle (V1 receptors; vasoconstriction at high
      vasopressin concentrations).
    - → uterus myometrium (oxytocin receptors; uterine contraction;
      parturition).
    - → mammary gland myoepithelium (oxytocin receptors; milk
      ejection).

    Adjacency (not signaling):
    - ↔ adenohypophysis/ (anatomically adjacent within the pituitary
      gland; the adenohypophysis is glandular, the neurohypophysis is
      neural; do not merge; no signaling edge between them — their
      control and outputs are distinct).
    - ↔ pars_intermedia/ (anatomically adjacent; the pars intermedia
      is rudimentary in humans; do not merge).

Notes:
    - Tier 2 organ leaf — the NEUROHEMAL STORAGE variant. Distinct from
      pineal_gland/ (single-hormone SYNTHESIS) and adenohypophysis/
      (six-hormone SYNTHESIS). The neurohypophysis is the tree's first
      organ that STORES and RELEASES rather than synthesizes; the
      defining property is that its hormones are produced by hypothalamic
      neurons (SON, PVN), not by the organ itself.
    - SINGLE FILE. The neurohypophysis is midline/unpaired; no left/
      or right/ children.
    - TWO DEFERRED EDGE CLOSURES: this file closes the neurohypophysis
      ends of the two remaining pituitary deferred edges:
        (1) PVN → neurohypophysis (oxytocin, vasopressin magnocellular
            axon terminals).
        (2) SON → neurohypophysis (vasopressin, oxytocin magnocellular
            axon terminals).
      With this file, ALL EIGHT pituitary deferred edges are now
      closed:
        - Six via adenohypophysis/ (CRH, TRH, somatostatin, GHRH,
          TIDA, GnRH).
        - Two via this file (PVN magno → posterior; SON → posterior).
    - THE FIVE DEFINING CLINICAL FACTS: central diabetes insipidus
      (deficient vasopressin → polyuria/polydipsia; contrast with
      nephrogenic DI); SIADH (excess vasopressin → hyponatremia);
      synthetic oxytocin clinical use (labor induction, postpartum
      hemorrhage); synthetic vasopressin clinical use (DDAVP for
      central DI; vasopressin for septic shock). These are what make
      the neurohypophysis clinically important beyond being "the two-
      hormone storage site." Documented in Functional Mode; do not
      omit.
    - THE SYSTEMIC vs. PORTAL DISTINCTION (the defining anatomical
      fact): the neurohypophysis releases into SYSTEMIC circulation;
      the adenohypophysis receives hypothalamic hormones from PORTAL
      blood. Two different release-target environments. The median
      eminence is the portal release site; the neurohypophysis is a
      systemic release site. Both are neurohemal, but their downstream
      environments are entirely different. Do not conflate.
    - The neurohypophysis is NOT a Tier 1 hub: it is a Tier 2 organ
      (storage/release site). Do not draft it as a processing region.
    - The neurohypophysis does NOT synthesize oxytocin and vasopressin;
      the SON and PVN magnocellular neurons do. This is the organ's
      defining property. Do not draft it as a synthesis site.
    - The neurohypophysis is DISTINCT from the adenohypophysis (storage/
      release vs. synthesis), the pars intermedia (rudimentary), the
      median eminence (portal vs. systemic release), the pituitary
      stalk (conduit), and SON/PVN (cell bodies vs. axon terminals).
      Five distinct nodes; do not merge.
    - The central neuromodulator roles of oxytocin and vasopressin are
      documented in chemicals_hormones/06_social_territorial_bonding/
      and in the SON/PVN leaves; this file documents the PERIPHERAL
      (systemic) release role. Do not conflate the two.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/06_* (social, oxytocin, vasopressin central),
      07_* (fluid, vasopressin peripheral, osmolarity, angiotensin II,
      ANP); memory/stores/ (short_term, episodic); gateway/.
    - Connects upward to diencephalon/pituitary_gland/.
""""""
Package: infrastructure.brainparts.forebrain.diencephalon.pituitary_gland.neurohypophysis
Anatomical Role:
    The neurohypophysis (posterior pituitary) is the NEURAL subdivision
    of the pituitary, derived embryologically from the diencephalon
    (neural ectoderm) — it is anatomically an EXTENSION of the
    hypothalamus, not a separate gland. It is a neurohemal storage and
    release organ: it does not synthesize hormones. It stores two
    hypothalamic neuropeptides in axon terminals of magnocellular
    neurons whose cell bodies sit in the supraoptic (SON) and
    paraventricular (PVN) nuclei, and releases them into the systemic
    circulation when the magnocellular neurons fire.

    The two hormones:
        - Oxytocin: synthesized in SON and PVN magnocellular neurons;
          axon terminals in the neurohypophysis store and release it.
        - Vasopressin (ADH; antidiuretic hormone): synthesized in SON
          and PVN magnocellular neurons; axon terminals in the
          neurohypophysis store and release it.

    The neurohypophysis is CONTROLLED by the hypothalamus via
    MAGNOCELLULAR AXON TERMINALS (not via the portal system — that is
    the adenohypophysis's control mechanism). The magnocellular neurons
    of SON and PVN project their axons through the pituitary stalk to
    terminate in the neurohypophysis; when they fire, they release
    oxytocin and vasopressin into fenestrated capillaries of the
    systemic circulation.

    DISTINCTIONS (reproduced from the parent pituitary_gland/
    container; critical — apply at every level):

    - NEUROHYPOPHYSIS vs. ADENOHYPOPHYSIS: NEURAL (stores and releases
      hypothalamic hormones) vs. GLANDULAR (synthesizes its own
      hormones). Different embryonic origins (neural ectoderm vs. oral
      ectoderm), different control mechanisms (axon terminals vs.
      portal blood), different hormones (2 stored vs. 6 synthesized).
      Do not merge.

    - NEUROHYPOPHYSIS vs. PARS INTERMEDIA: distinct subdivisions; the
      pars intermedia is rudimentary in humans. Do not merge.

    - NEUROHYPOPHYSIS vs. MEDIAN EMINENCE: both are neurohemal release
      sites, but the median eminence releases hypothalamic hormones
      into PORTAL BLOOD (for the adenohypophysis), while the
      neurohypophysis releases hypothalamic hormones into the SYSTEMIC
      CIRCULATION (for the whole body). Two different neurohemal sites;
      two different downstream environments. Do not merge.

    - NEUROHYPOPHYSIS vs. PITUITARY STALK: the stalk is the conduit
      through which the magnocellular axons travel; the
      neurohypophysis is the axon terminal storage/release site.
      Distinct tree nodes; distinct tiers (Tier 3 vs. Tier 2).

    - NEUROHYPOPHYSIS vs. SON and PVN: the neurohypophysis does NOT
      contain the cell bodies of the magnocellular neurons; those sit
      in SON and PVN (hypothalamus/anterior/medial_area/left|right/
      supraoptic_nucleus/ and paraventricular_nucleus/). The
      neurohypophysis is the axon terminal field. Do not merge.

Functional Mode:
    The neurohypophysis releases two hormones, each with its own
    physiological role and its own stimulus:

    - Oxytocin (systemic release; peripheral actions):
        * Parturition (Ferguson reflex): uterine stretch → oxytocin
          release → uterine contraction → more stretch → more oxytocin.
          Positive feedback loop.
        * Milk ejection: suckling → oxytocin pulsatile release →
          myoepithelial contraction in mammary glands → milk
          ejection. (This is distinct from prolactin's role in milk
          PRODUCTION; oxytocin releases the milk, prolactin produces
          it.)
        * Central neuromodulator roles: oxytocin is also released
          centrally (dendritically and somatodendritically) and acts
          as a neuromodulator in social behavior, trust, pair bonding,
          and maternal behavior. The central roles are documented in
          chemicals_hormones/06_social_territorial_bonding/ and in
          the hypothalamic nuclei that produce oxytocin (PVN, SON);
          this file documents the PERIPHERAL (systemic) release role.
    - Vasopressin (ADH; systemic release; peripheral actions):
        * Water reabsorption: vasopressin acts on V2 receptors in the
          kidney collecting duct → aquaporin-2 insertion → water
          reabsorption → concentrated urine.
        * Vasoconstriction: vasopressin acts on V1 receptors in
          vascular smooth muscle → vasoconstriction → increased blood
          pressure (at high concentrations; this is the "vasopressin"
          name's origin).
        * Central neuromodulator roles: vasopressin is also released
          centrally and acts as a neuromodulator in social behavior,
          pair bonding, aggression, and stress-axis modulation. The
          central roles are documented in
          chemicals_hormones/06_social_territorial_bonding/ and in the
          hypothalamic nuclei that produce vasopressin (PVN, SON);
          this file documents the PERIPHERAL (systemic) release role.

    - Stimuli for release:
        * Oxytocin: uterine stretch (parturition), suckling (lactation),
          and central signals (social context, stress).
        * Vasopressin: rising plasma osmolarity (via OVLT → SON/PVN),
          hypovolemia/hypotension (via baroreceptors → NTS → SON/PVN),
          angiotensin II (via SFO → SON/PVN), and stress.

Hormonal Modulation (Tier 2 neurohemal storage convention — outputs
are the defining content; no synthesis here):

    - TWO OUTPUTS (stored and released; NOT synthesized here):
        * Oxytocin (from SON and PVN magnocellular neurons).
        * Vasopressin (from SON and PVN magnocellular neurons).

    - CONTROL INPUTS (the magnocellular neurons' firing, not the
      neurohypophysis's own physiology):
        * Osmolarity ↑ (via OVLT → SON/PVN) → vasopressin ↑.
        * Angiotensin II ↑ (via SFO → SON/PVN) → vasopressin ↑.
        * Hypovolemia/hypotension ↑ (via baroreceptors → NTS →
          SON/PVN) → vasopressin ↑.
        * ANP ↑ (volume repletion) → vasopressin ↓.
        * Uterine stretch (parturition) → oxytocin ↑.
        * Suckling → oxytocin ↑.
        * Stress → vasopressin ↑ and (context-dependent) oxytocin.

    - Direction summary: osmolarity ↑ → vasopressin ↑; angiotensin II
      ↑ → vasopressin ↑; ANP ↑ → vasopressin ↓; suckling → oxytocin
      pulsatile release; uterine stretch → oxytocin ↑. These are the
      actionable directions.

    - Clinical facts (the file's defining clinical content):
        * CENTRAL DIABETES INSIPIDUS: deficient vasopressin release
          (hypothalamic or pituitary cause: SON/PVN damage, pituitary
          stalk section, or neurohypophysis damage) → polyuria,
          polydipsia, dilute urine. Contrast with NEPHROGENIC
          diabetes insipidus (renal V2 resistance; the hormone is
          present but the kidney does not respond).
        * SIADH (syndrome of inappropriate antidiuretic hormone):
          excess vasopressin → water retention, hyponatremia,
          concentrated urine. Common causes: ectopic ADH from tumors,
          CNS lesions, drugs.
        * OXYTOCIN CLINICAL USE: synthetic oxytocin (Pitocin) is used
          clinically for labor induction and augmentation, and for
          postpartum hemorrhage prevention.
        * VASOPRESSIN CLINICAL USE: synthetic vasopressin (DDAVP; a
          V2-selective analog) is used for central diabetes insipidus;
          vasopressin itself is used for septic shock (V1-mediated
          vasoconstriction).

Memory Interfaces (minimal — Tier 2 organ convention):
    - Reads:
        * short_term: current plasma osmolarity and volume state
          (via SON/PVN; the neurohypophysis reads the magnocellular
          neurons' state, which reflects these).
        * episodic: parturition history, lactation history,
          dehydration/hemorrhage history.
    - Writes: none directly. The neurohypophysis is a storage/release
      site, not a memory structure. It does not write episodic,
      semantic, or procedural content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent neurohypophysis fragment. The neurohypophysis's
      output is the READOUT of the SON/PVN magnocellular state, not an
      independent signal. It contributes to TWO hypothalamic
      aggregates:
        (1) Fluid/osmotic aggregate (vasopressin): the aggregated
            osmotic fragment emitted at the anterior-division level
            (SON + PVN + MnPO + SFO/OVLT inputs). The neurohypophysis's
            vasopressin release is the effector arm.
        (2) Social/parturition/lactation aggregate (oxytocin): the
            social fragment emitted by the PVN. The neurohypophysis's
            oxytocin release is the effector arm.
    - The AGGREGATION RULES from SON and PVN apply: the
      neurohypophysis's output feeds the aggregates they emit. Do not
      emit a separate neurohypophysis fragment.
    - Guardrails: the two aggregates (fluid/osmotic and social) carry
      their "bias not impairment" clauses. The neurohypophysis does not
      add new guardrails.
    - No multimodal input is consumed here; the contributions are
      text-only through the downstream aggregates.

Reciprocal Connections (organized by magnocellular input and
systemic output):

    Hypothalamic control (INPUT — the two deferred edges this file
    closes):
    - ← anterior/medial_area/left|right/paraventricular_nucleus
      (oxytocin and vasopressin magnocellular axon terminals; PVN →
      posterior pituitary; THE DEFERRED CLOSURE for PVN magnocellular).
    - ← anterior/medial_area/left|right/supraoptic_nucleus (vasopressin
      and oxytocin magnocellular axon terminals; SON → posterior
      pituitary; THE DEFERRED CLOSURE for SON magnocellular).
    - ← hypothalamus/pituitary_stalk (the conduit; the magnocellular
      axons travel through the stalk to the neurohypophysis).

    Systemic targets (OUTPUT — the two hormones' peripheral actions):
    - → kidney collecting duct (V2 receptors; aquaporin-2 insertion;
      water reabsorption; vasopressin effector action).
    - → vascular smooth muscle (V1 receptors; vasoconstriction at high
      vasopressin concentrations).
    - → uterus myometrium (oxytocin receptors; uterine contraction;
      parturition).
    - → mammary gland myoepithelium (oxytocin receptors; milk
      ejection).

    Adjacency (not signaling):
    - ↔ adenohypophysis/ (anatomically adjacent within the pituitary
      gland; the adenohypophysis is glandular, the neurohypophysis is
      neural; do not merge; no signaling edge between them — their
      control and outputs are distinct).
    - ↔ pars_intermedia/ (anatomically adjacent; the pars intermedia
      is rudimentary in humans; do not merge).

Notes:
    - Tier 2 organ leaf — the NEUROHEMAL STORAGE variant. Distinct from
      pineal_gland/ (single-hormone SYNTHESIS) and adenohypophysis/
      (six-hormone SYNTHESIS). The neurohypophysis is the tree's first
      organ that STORES and RELEASES rather than synthesizes; the
      defining property is that its hormones are produced by hypothalamic
      neurons (SON, PVN), not by the organ itself.
    - SINGLE FILE. The neurohypophysis is midline/unpaired; no left/
      or right/ children.
    - TWO DEFERRED EDGE CLOSURES: this file closes the neurohypophysis
      ends of the two remaining pituitary deferred edges:
        (1) PVN → neurohypophysis (oxytocin, vasopressin magnocellular
            axon terminals).
        (2) SON → neurohypophysis (vasopressin, oxytocin magnocellular
            axon terminals).
      With this file, ALL EIGHT pituitary deferred edges are now
      closed:
        - Six via adenohypophysis/ (CRH, TRH, somatostatin, GHRH,
          TIDA, GnRH).
        - Two via this file (PVN magno → posterior; SON → posterior).
    - THE FIVE DEFINING CLINICAL FACTS: central diabetes insipidus
      (deficient vasopressin → polyuria/polydipsia; contrast with
      nephrogenic DI); SIADH (excess vasopressin → hyponatremia);
      synthetic oxytocin clinical use (labor induction, postpartum
      hemorrhage); synthetic vasopressin clinical use (DDAVP for
      central DI; vasopressin for septic shock). These are what make
      the neurohypophysis clinically important beyond being "the two-
      hormone storage site." Documented in Functional Mode; do not
      omit.
    - THE SYSTEMIC vs. PORTAL DISTINCTION (the defining anatomical
      fact): the neurohypophysis releases into SYSTEMIC circulation;
      the adenohypophysis receives hypothalamic hormones from PORTAL
      blood. Two different release-target environments. The median
      eminence is the portal release site; the neurohypophysis is a
      systemic release site. Both are neurohemal, but their downstream
      environments are entirely different. Do not conflate.
    - The neurohypophysis is NOT a Tier 1 hub: it is a Tier 2 organ
      (storage/release site). Do not draft it as a processing region.
    - The neurohypophysis does NOT synthesize oxytocin and vasopressin;
      the SON and PVN magnocellular neurons do. This is the organ's
      defining property. Do not draft it as a synthesis site.
    - The neurohypophysis is DISTINCT from the adenohypophysis (storage/
      release vs. synthesis), the pars intermedia (rudimentary), the
      median eminence (portal vs. systemic release), the pituitary
      stalk (conduit), and SON/PVN (cell bodies vs. axon terminals).
      Five distinct nodes; do not merge.
    - The central neuromodulator roles of oxytocin and vasopressin are
      documented in chemicals_hormones/06_social_territorial_bonding/
      and in the SON/PVN leaves; this file documents the PERIPHERAL
      (systemic) release role. Do not conflate the two.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/06_* (social, oxytocin, vasopressin central),
      07_* (fluid, vasopressin peripheral, osmolarity, angiotensin II,
      ANP); memory/stores/ (short_term, episodic); gateway/.
    - Connects upward to diencephalon/pituitary_gland/.
"""