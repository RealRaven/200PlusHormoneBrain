"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.pituitary_stalk
Anatomical Role:
    Tier 3 mixed conduit. The pituitary stalk (infundibulum) is the
    short anatomical connection between the hypothalamus and the
    pituitary gland. It is the tree's first DUAL-CHANNEL conduit: it
    carries two physically distinct systems in parallel.
        - Channel 1 — Hypophyseal portal vessels (vascular): arterial
          blood descends from the superior hypophyseal artery to the
          primary capillary plexus in the median eminence; portal
          venous blood then ascends through the stalk to the secondary
          capillary plexus in the anterior pituitary (adenohypophysis).
          The six releasing/inhibiting hormones (CRH, TRH, GnRH, GHRH,
          somatostatin, dopamine) travel via this vascular channel.
        - Channel 2 — Magnocellular axons (neural): unmyelinated axons
          from the supraoptic (SON) and paraventricular (PVN) nuclei
          descend through the stalk to terminate in the posterior
          pituitary (neurohypophysis), where they release vasopressin
          and oxytocin into the systemic circulation.
    The pituitary stalk is NOT a processing region: it has no intrinsic
    neural processing, no endocrine secretion, and no memory function.
    It is a conduit for both a vascular portal system and a neural axon
    bundle. The two channels are anatomically distinct and terminate at
    different parts of the pituitary; do not conflate.

Functional Mode:
    - Hypophyseal portal transport (Channel 1; primary function):
      carries the six releasing/inhibiting hormones from the median
      eminence to the anterior pituitary. This is the vascular basis of
      the HPA, HPT, HPG, growth, and prolactin axes' hypothalamic
      control. Direction: arterial blood descends, portal blood
      ascends.
    - Magnocellular axonal transport (Channel 2; primary function):
      carries SON and PVN axons from the hypothalamus to the posterior
      pituitary. This is the basis of vasopressin and oxytocin release
      into the systemic circulation. Direction: descending axons from
      hypothalamus to posterior pituitary.
    - Anatomical pathway for both channels: the stalk passes through
      the diaphragma sellae (a dural fold) as it enters the sella
      turcica. This anatomical constriction is why stalk compression
      (by pituitary adenoma, or by any mass lesion) produces a
      stereotyped clinical syndrome.
    - Stalk-effect (the one substantive clinical fact): compression or
      interruption of the pituitary stalk — typically by a pituitary
      adenoma, but also by trauma, surgery, or infiltrative disease —
      interrupts the DESCENDING dopaminergic portal flow that inhibits
      prolactin release. The result is hyperprolactinemia
      (stalk-effect hyperprolactinemia), often with hypopituitarism of
      the other axes (because portal releasing hormones also cannot
      reach the anterior pituitary). This is the stalk's one
      characteristic pathology and should be documented.
    - The pituitary stalk does not process the signals it carries: it
      is a conduit. All processing occurs upstream (hypothalamic
      nuclei) and downstream (pituitary gland).

Hormonal Modulation:
    None. Tier 3 conduits are not hormone targets or sources. Do not add
    a hormone section. The hormones that pass THROUGH the stalk are
    documented in the median eminence (portal channel) and in SON/PVN
    (magnocellular channel); do not duplicate them here.

Memory Interfaces:
    None. Tier 3 conduits do not read or write memory. Do not add a
    memory section.

Model Integration (Gemma-4-E2B):
    None. Tier 3 conduits do not contribute prompt fragments. The portal
    hormones' fragments are emitted by the nuclei that produce them
    (PVN, arcuate, preoptic area); the vasopressin/oxytocin fragments
    are emitted by the SON/PVN aggregate (fluid fragment). The stalk is
    a physical pathway, not a signal emitter. Do not add a fragment.

Reciprocal Connections:
    - ← hypothalamus/median_eminence (Channel 1: portal vessels exit
      the median eminence and traverse the stalk; the median eminence
      is upstream of this conduit).
    - ← hypothalamus/anterior/medial_area/left|right/supraoptic_nucleus
      and paraventricular_nucleus (Channel 2: magnocellular axons
      descend from SON/PVN through the stalk to the posterior
      pituitary).
    - → pituitary_gland/anterior (Channel 1: portal blood arrives at
      the adenohypophysis; the six releasing/inhibiting hormones
      reach their target cells).
    - → pituitary_gland/neurohypophysis (Channel 2: magnocellular axon
      terminals release vasopressin and oxytocin into the systemic
      circulation at the neurohypophysis).
    - ↔ hypothalamus/optic_chiasm (anatomical adjacency at the base of
      the hypothalamus; both structures are crossed by the stalk's
      vicinity; no signaling edge — purely spatial).

Notes:
    - Tier 3 MIXED CONDUIT subtype. Distinct from stria_medullaris
      (pure neural axons) and optic_chiasm (pure decussation): the
      pituitary stalk carries both a vascular portal system and a
      neural axon bundle. Document both channels separately; do not
      collapse into one.
    - The TWO channels terminate at DIFFERENT pituitary subdivisions:
      Channel 1 → adenohypophysis (anterior pituitary); Channel 2 →
      neurohypophysis (posterior pituitary). Do not conflate the
      targets.
    - The stalk-effect (hyperprolactinemia from descending dopaminergic
      flow interruption) is the file's one substantive clinical fact.
      Document it; do not omit. It is what makes the stalk clinically
      important beyond being "the connection."
    - The pituitary stalk is NOT a processing region, NOT an endocrine
      organ, and NOT a memory structure. Do not draft it as any of
      those. Its only functional identity is "the conduit between
      hypothalamus and pituitary, carrying both the portal vascular
      system and the magnocellular axon bundle."
    - Unpaired midline structure. Do not create left/ or right/
      children.
    - The six portal hormones (CRH, TRH, GnRH, GHRH, somatostatin,
      dopamine) and the two magnocellular hormones (vasopressin,
      oxytocin) pass through the stalk; they are documented in their
      producing nuclei and their pituitary targets. Do not duplicate
      the hormones here.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, GnRH), 02_* (HPA, CRH), 03_*
      (HPT, TRH, somatostatin, GHRH), 04_* (satiety, dopamine-adjacent),
      06_* (social, oxytocin, vasopressin central), 07_* (fluid,
      vasopressin peripheral); memory/stores/ is not applicable;
      gateway/.
    - Connects upward to hypothalamus/.
"""