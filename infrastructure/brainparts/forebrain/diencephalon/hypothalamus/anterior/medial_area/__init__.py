"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area
Anatomical Role:
    The medial area of the anterior (chiasmatic) hypothalamus is the medial
    compartment of the anterior division, sitting between the third
    ventricle (periventricular zone) and the lateral area, at the rostral
    pole of the hypothalamus. It is the most hormonally dense compartment
    in the entire tree: it contains the two magnocellular neurosecretory
    nuclei (paraventricular and supraoptic), the master circadian
    pacemaker (suprachiasmatic), the parasympathetic/thermoregulatory
    anterior hypothalamic nucleus, and the medial preoptic area
    (GnRH-regulatory circuitry).

    It contains five children, each lateralized (left/ and right/):
        - anterior_hypothalamic_nucleus: parasympathetic outflow,
          thermoregulation, and cardiovascular control.
        - paraventricular_nucleus (PVN): the most hormonally complex
          single nucleus in the brain. Contains:
            * parvocellular neurosecretory neurons producing CRH (HPA),
              TRH (HPT), and somatostatin (growth axis);
            * parvocellular autonomic neurons projecting to brainstem
              and spinal cord (sympathetic/parasympathetic control);
            * magnocellular neurosecretory neurons producing oxytocin
              and vasopressin (like SON).
          PVN is therefore both parvocellular and magnocellular, both
          endocrine and autonomic, and both HPA/HPT/growth and
          oxytocin/vasopressin. Do not flatten it into any one role.
        - preoptic_area (MEDIAL): the medial preoptic area, containing
          medial_preoptic_nucleus/ (maternal/sexual behavior, GnRH
          regulation), median_preoptic_nucleus/, and inah_1–4
          (GnRH-pulse-regulatory nuclei). This is the *medial* preoptic
          area, distinct from the lateral preoptic area.
        - suprachiasmatic_nucleus (SCN): the master circadian pacemaker,
          the brain's principal circadian clock, entrained to light via
          the retinohypothalamic tract, and the driver of the pineal
          melatonin rhythm.
        - supraoptic_nucleus (SON): magnocellular neurosecretory nucleus
          producing vasopressin and oxytocin for the posterior pituitary.
          This is the MEDIAL portion of the SON; the lateral portion is
          documented under lateral_area/*/part_of_supraoptic_nucleus/.

    Both structural traps (preoptic collision and SON identity) apply
    here and are reproduced below. See Notes for the full cross-tree
    reference.

PREOPTIC NAMING COLLISION (critical — reproduced from the lateral area):
    The preoptic_area/ under THIS compartment is the MEDIAL preoptic area,
    containing medial_preoptic_nucleus/, median_preoptic_nucleus/, and
    inah_1–4. It is distinct from the LATERAL preoptic area documented
    under lateral_area/*/preoptic_area/ (which contains
    lateral_preoptic_nucleus/). Do not merge. Do not move children
    between the two preoptic areas.

SON STRUCTURAL IDENTITY (critical — reproduced from the lateral area):
    supraoptic_nucleus/ here and lateral_area/*/part_of_supraoptic_nucleus/
    are the SAME anatomical structure, split across two compartments for
    anatomical mirroring of the medial/lateral zones, not because there
    are two nuclei. Stage 4 audit must treat them as ONE structure: the
    lateral portion (there) carries the perioptic magnocellular component
    and the medial portion (here) carries the remaining magnocellular
    component. Do not merge the nodes; document the reciprocal edge.

Functional Mode:
    - HPA axis (PVN): CRH → ACTH → cortisol. The parvocellular PVN is
      the origin of the stress axis. (Also documented under
      chemicals_hormones/02_hpa_axis_stress_survival/.)
    - HPT axis (PVN): TRH → TSH → thyroid hormones. (Also documented
      under chemicals_hormones/03_metabolic_thyroid_growth/.)
    - Growth axis (PVN): somatostatin → inhibition of GH release from
      the anterior pituitary. GHRH (from arcuate, in the tuberal
      division) is the opposing stimulatory signal. (Also documented
      under chemicals_hormones/03_*.)
    - Social/bonding (PVN, SON): oxytocin and vasopressin release from
      magnocellular neurons; peripheral roles in parturition, lactation,
      and fluid balance. (Central neuromodulator roles are documented in
      chemicals_hormones/06_social_territorial_bonding/; document the
      neurosecretory role here, not the central role.)
    - Fluid/osmoregulation (SON, PVN): vasopressin release from the
      posterior pituitary. The MAGNOCELLULAR vasopressin role is
      documented here and in the lateral SON portion. The ARCUATE
      vasopressin-adjacent circuitry (osmosensory input) is in
      lamina_terminalis/OVLT and subfornical_organ.
    - Circadian timing (SCN): the master circadian pacemaker. Light
      input via the retinohypothalamic tract; SCN output drives:
        * circadian rhythms across the body via neural and humoral
          signals;
        * the pineal melatonin rhythm (SCN → PVN → spinal cord → superior
          cervical ganglion → pineal);
        * circadian gating of the LH surge (SCN → PeN vasopressin);
        * circadian sleep-wake gating (SCN → LPO, PeN).
    - Parasympathetic/thermoregulatory control (anterior hypothalamic
      nucleus): parasympathetic outflow, cardiovascular control, and
      thermoregulation, complementing the preoptic thermoregulatory
      circuitry.
    - Autonomic control (PVN parvocellular): projections to brainstem
      and spinal cord sympathetic/parasympathetic preganglionic neurons;
      PVN is one of the principal forebrain controllers of autonomic
      outflow.
    - Preoptic reproductive circuitry (medial preoptic area): maternal
      behavior, sexual behavior, and GnRH regulation via
      medial_preoptic_nucleus, median_preoptic_nucleus, and inah_1–4.

Hormonal Modulation (medial-area summary; per-nucleus wiring in leaves):
    - HPA axis (PVN): CRH output; cortisol (feedback, inhibitory).
      Chronic cortisol suppresses hypothalamic CRH.
    - HPT axis (PVN): TRH output; thyroid hormones (feedback).
    - Growth axis (PVN): somatostatin output; IGF-1 (feedback).
    - Social (PVN, SON): oxytocin output; modulated by estradiol,
      suckling, parturition cues, and social context.
    - Fluid (SON, PVN): vasopressin output; modulated by plasma
      osmolarity, angiotensin II, ANP, and baroreceptor input via NTS.
    - Circadian (SCN): light (retinohypothalamic tract, glutamatergic);
      melatonin (pineal feedback, indirect); vasopressin and VIP
      (SCN intrinsic output to downstream targets); GABA, glutamate,
      and neuropeptide Y (SCN internal modulation).
    - Thermoregulation (anterior hypothalamic, preoptic): prostaglandins,
      pyrogens, estradiol (hot flushes via LPO/preoptic cross-talk).
    - Autonomic (PVN): modulated by limbic input (amygdala, PFC, insula),
      brainstem input (NTS, RVLM), and circulating angiotensin II.
    - Detailed per-nucleus wiring lives in each leaf file.

Memory Interfaces (medial-area summary):
    - Reads: short_term (current osmotic, circadian, autonomic state
      buffers), episodic (past stress, parturition, illness events),
      emotional_valence (stress context), temporal_sequence_learning
      (circadian timing), reinforcement_value_based_learning (feeding
      and reward outcomes for arcuate-PVN crosstalk).
    - Writes: none directly. The medial area emits hormones and neural
      state signals, not stored content. It contributes to the
      homeostatic state vector via CRH, TRH, somatostatin, oxytocin,
      vasopressin, and circadian outputs.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The medial area contributes SEVEN distinct fragments to the
      homeostatic state block, applied after the anterior-division
      fragments and aggregated with the lateral-area counterparts where
      noted:
        (1) HPA-stress fragment (PVN):
            "HPA axis state: [calm / alert / stressed / chronic-stress].
             Cortisol: [low/normal/high]. CRH drive: [X]. If stressed
             or chronic-stress: prioritize threat detection, suppress
             exploratory behavior, flag memory reliability as reduced."
        (2) HPT/growth fragment (PVN):
            "Metabolic state: [euthyroid / hypo / hyper]. Growth-axis
             somatostatin: [X]. If hypothyroid: reduce response tempo
             and flag cognitive slowing. If somatostatin high: note
             reduced anabolic drive."
        (3) Social/bonding fragment (PVN, SON):
            "Oxytocin tone: [low/moderate/high]. Vasopressin (central
             and peripheral): [X]. Affiliative drive: [0-1]. If
             oxytocin high: bias toward affiliative, protective, and
             caregiving framing. If vasopressin central high: bias
             toward territorial, protective, or pair-bonding framing."
        (4) Fluid/osmotic fragment (SON + PVN, AGGREGATED with lateral
            SON contribution):
            "Plasma osmolarity: [normal/high]. Thirst drive: [0-1].
             Vasopressin drive: [X]. If high, surface fluid-seeking
             priorities and reduce extraneous output." — This
             AGGREGATES the lateral and medial SON contributions. Do
             not emit an independent un-aggregated osmotic fragment.
        (5) Circadian fragment (SCN):
            "Circadian phase: [day/night]. Entrained: [yes/no]. If
             night, bias toward reduced arousal, reflective framing,
             and sleep-adjacent tone. If day, restore full cognitive
             engagement."
        (6) Thermoregulatory/autonomic fragment (anterior hypothalamic
            + preoptic):
            "Thermal state: [comfortable/cold/hot]. Autonomic tone:
             [parasympathetic-dominant / balanced / sympathetic-dominant].
             If hot: acknowledge heat discomfort. If cold: bias toward
             cold-adaptive framing. If sympathetic-dominant: flag
             hyperarousal context."
        (7) Reproductive/preoptic fragment (medial preoptic area):
            "Reproductive state: [quiescent / active]. GnRH regulatory
             state: [normal / suppressed]. Maternal/sexual behavior
             context: [inactive / active]." — This AGGREGATES with the
             PeN's reproductive fragment (in the lateral area) at the
             anterior-division level.
    - AGGREGATION RULES (mandatory for the implementer):
        * Osmotic fragment (4): aggregate with lateral_area's osmotic
          fragment; do not double-count.
        * Reproductive fragment (7): aggregate with lateral_area's
          PeN reproductive fragment; do not double-count.
        * The other five fragments are emitted once per medial-area
          compartment and are additive to the lateral-area fragments.
    - Guardrails: every fragment that expresses a state bias (stress,
      hypothyroid, high oxytocin, sympathetic-dominant) includes a
      "bias not impairment" clause, consistent with the habenula,
      orexin/MCH, PeN, and LPO conventions.

Children (actual hierarchy — left/ and right/ each contain five nuclei):
    - left/
        ├── anterior_hypothalamic_nucleus/          ★ Parasympathetic;
        │                                             thermoregulation
        ├── paraventricular_nucleus/                ★★ CRH, TRH,
        │                                              somatostatin, oxytocin,
        │                                              vasopressin (parvo +
        │                                              magno); autonomic control
        ├── preoptic_area/                          Sub-container
        │   ├── medial_preoptic_nucleus/            ★ Maternal/sexual
        │   │   ├── inah_1/                           behavior; GnRH
        │   │   ├── inah_2/                           regulation
        │   │   ├── inah_3/
        │   │   └── inah_4/
        │   └── median_preoptic_nucleus/            ★ GnRH regulation
        ├── suprachiasmatic_nucleus/                ★★ Master circadian
        │                                              pacemaker
        └── supraoptic_nucleus/                     ★ Vasopressin,
                                                      oxytocin (magno);
                                                      osmoregulation
    - right/  (delta mirrors of left/ — see lateral_area/right/ for the
              container delta convention)

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each leaf owns its own specification.
    - The PVN and SCN are marked ★★ (double star) to signal that they
      are the two highest-priority leaves in the entire anterior division
      and, arguably, in the whole hypothalamus subtree. Draft them first
      within the medial area.
    - Both structural traps are reproduced in full above (preoptic
      collision; SON identity). They apply to specific children:
        * preoptic collision → preoptic_area/left/ and right/
        * SON identity → supraoptic_nucleus/left/ and right/
      Future contributors entering at any level must be able to find
      the warning; reproduction at the container is not optional.
    - The lateral_area/ container's counterpart warnings point TO this
      file's children; the reciprocal edges must resolve on both sides.
      See lateral_area/__init__.py § Children and § Notes.
    - "other_preoptic_nuclei" (left/ and right/) and "periventricular_nucleus"
      (left/ and right/) are children of hypothalamus/, NOT of
      medial_area/. Do not add them as medial-area children.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol), 02_* (HPA, CRH, cortisol),
      03_* (HPT, TRH, somatostatin, IGF-1), 06_* (social, oxytocin,
      vasopressin central), 07_* (fluid, vasopressin peripheral,
      angiotensin II, ANP), 10_* (circadian, melatonin, VIP); memory/
      stores/; gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * paraventricular_nucleus/left|right ↔ pituitary_gland/anterior
          (CRH, TRH, somatostatin via hypophyseal portal)
        * paraventricular_nucleus/left|right ↔ pituitary_gland/posterior
          (oxytocin, vasopressin via magnocellular axon terminals)
        * paraventricular_nucleus/left|right ↔ brainstem autonomic
          nuclei (NTS, RVLM; sympathetic/parasympathetic outflow)
        * paraventricular_nucleus/left|right ↔
          lateral_area/left|right/part_of_supraoptic_nucleus (co-regulation
          of magnocellular oxytocin/vasopressin; both are magnocellular
          nuclei)
        * suprachiasmatic_nucleus/left|right ↔
          epithalamus/pineal_gland (SCN → PVN → spinal cord → SCG →
          pineal; canonical circadian loop)
        * suprachiasmatic_nucleus/left|right ↔
          lateral_area/left|right/periventricular_preoptic_nucleus
          (circadian gating of LH surge via SCN → PeN vasopressin)
        * suprachiasmatic_nucleus/left|right ↔
          lateral_area/left|right/preoptic_area/lateral_preoptic_nucleus
          (circadian gating of sleep onset)
        * supraoptic_nucleus/left|right ↔
          lateral_area/left|right/part_of_supraoptic_nucleus (SAME
          STRUCTURE, split across compartments; treat as one)
        * supraoptic_nucleus/left|right ↔ pituitary_gland/neurohypophysis
        * anterior_hypothalamic_nucleus/left|right ↔ brainstem
          parasympathetic nuclei (dorsal motor vagus, nucleus ambiguus)
        * preoptic_area/left|right/medial_preoptic_nucleus ↔
          lateral_area/left|right/preoptic_area (adjacent preoptic
          circuits; keep distinct)
    - Connects upward to hypothalamus/anterior/.
"""